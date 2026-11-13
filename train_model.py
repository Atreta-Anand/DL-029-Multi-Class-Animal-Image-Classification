
from pathlib import Path
import time
from config import *
from utils import set_seed, save_json


def build_model(num_classes, image_size=IMAGE_SIZE, pretrained=True):
    import tensorflow as tf

    inp = tf.keras.Input((*image_size, 3))

    aug = tf.keras.Sequential([
        tf.keras.layers.RandomFlip("horizontal"),
        tf.keras.layers.RandomRotation(0.05),
        tf.keras.layers.RandomZoom(0.1),
        tf.keras.layers.RandomTranslation(0.05, 0.05),
        tf.keras.layers.RandomContrast(0.1)
    ], name="train_only_augmentation")

    x = aug(inp)
    x = tf.keras.layers.Rescaling(1./127.5, offset=-1)(x)

    base = tf.keras.applications.MobileNetV2(
        input_shape=(*image_size, 3),
        include_top=False,
        weights="imagenet" if pretrained else None
    )

    base.trainable = False
    x = base(x, training=False)

    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dropout(0.3)(x)

    out = tf.keras.layers.Dense(
        num_classes,
        activation="softmax"
    )(x)

    model = tf.keras.Model(inp, out)

    model.compile(
        optimizer=tf.keras.optimizers.Adam(LEARNING_RATE),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model


def train(epochs=EPOCHS, batch_size=BATCH_SIZE, pretrained=True):
    import tensorflow as tf

    set_seed(SEED)
    split = SPLIT_ROOT

    classes = sorted(
        p.name for p in (split / "train").iterdir()
        if p.is_dir()
    )

    if not 4 <= len(classes) <= 6:
        raise ValueError(f"Expected 4-6 classes, found {len(classes)}")

    def ds(name, shuffle):
        return tf.keras.utils.image_dataset_from_directory(
            split / name,
            class_names=classes,
            image_size=IMAGE_SIZE,
            batch_size=batch_size,
            shuffle=shuffle,
            seed=SEED
        ).prefetch(tf.data.AUTOTUNE)

    model = build_model(
        len(classes),
        pretrained=pretrained
    )

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    histdir = OUTPUT_DIR / "training"
    histdir.mkdir(parents=True, exist_ok=True)

    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=4,
            restore_best_weights=True
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor="val_loss",
            patience=2,
            factor=0.3
        ),
        tf.keras.callbacks.ModelCheckpoint(
            str(MODEL_DIR / "mobilenetv2_best.keras"),
            save_best_only=True
        )
    ]

    start = time.perf_counter()

    h = model.fit(
        ds("train", True),
        validation_data=ds("validation", False),
        epochs=epochs,
        callbacks=callbacks
    )

    duration = time.perf_counter() - start

    model.save(MODEL_DIR / "mobilenetv2.keras")

    values = {
        k: [float(x) for x in v]
        for k, v in h.history.items()
    }

    save_json(
        values,
        histdir / "mobilenetv2_history.json"
    )

    save_json({
        "architecture": "mobilenetv2",
        "classes": classes,
        "image_size": IMAGE_SIZE,
        "epochs_completed": len(h.epoch),
        "batch_size": batch_size,
        "training_seconds": duration,
        "pretrained_requested": pretrained
    }, MODEL_DIR / "mobilenetv2_metadata.json")

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    for metric in ("accuracy", "loss"):
        fig, ax = plt.subplots()

        ax.plot(values.get(metric, []), label="train")
        ax.plot(values.get("val_" + metric, []), label="validation")

        ax.set(
            title=f"MobileNetV2 {metric}",
            xlabel="Epoch",
            ylabel=metric
        )

        ax.legend()
        fig.tight_layout()

        fig.savefig(
            histdir / f"mobilenetv2_{metric}.png",
            dpi=150
        )

        plt.close(fig)

    return MODEL_DIR / "mobilenetv2.keras"


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()

    p.add_argument("--epochs", type=int, default=EPOCHS)
    p.add_argument("--batch-size", type=int, default=BATCH_SIZE)
    p.add_argument("--no-pretrained", action="store_true")

    a = p.parse_args()

    print(train(
        a.epochs,
        a.batch_size,
        not a.no_pretrained
    ))
