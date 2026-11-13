from pathlib import Path
from urllib.request import Request, urlopen
import csv

PACK_DIR = Path(__file__).resolve().parent
# If extracted inside an existing project, place images in that project's dataset/raw.
ROOT = PACK_DIR.parent if (PACK_DIR.parent / 'dataset' / 'raw').exists() else PACK_DIR
DATA = ROOT / 'dataset' / 'raw'
SOURCES = [
    ('butterfly', 'butterfly_001.jpg', 'https://upload.wikimedia.org/wikipedia/commons/b/b0/Picture_of_butterfly.jpg', 'Umar2z', 'CC0 1.0', 'https://commons.wikimedia.org/wiki/File:Picture_of_butterfly.jpg'),
    ('cat', 'cat_001.jpg', 'https://upload.wikimedia.org/wikipedia/commons/0/08/Picture_of_cat.jpg', 'Theeyes 07', 'CC0 1.0', 'https://commons.wikimedia.org/wiki/File:Picture_of_cat.jpg'),
    ('dog', 'dog_001.jpg', 'https://upload.wikimedia.org/wikipedia/commons/e/e1/Photo_of_a_dog.jpg', 'ContaDeletada2906', 'CC0 1.0', 'https://commons.wikimedia.org/wiki/File:Photo_of_a_dog.jpg'),
    ('elephant', 'elephant_001.jpg', 'https://upload.wikimedia.org/wikipedia/commons/c/ca/Elephant_animal.jpg', 'Swethasakthivel', 'CC0 1.0', 'https://commons.wikimedia.org/wiki/File:Elephant_animal.jpg'),
    ('horse', 'horse_001.jpg', 'https://upload.wikimedia.org/wikipedia/commons/e/ef/Horse_in_a_pen.jpg', 'Jojovavasasa', 'CC0 1.0', 'https://commons.wikimedia.org/wiki/File:Horse_in_a_pen.jpg'),
]

for cls in ['butterfly', 'cat', 'dog', 'elephant', 'horse']:
    (DATA / cls).mkdir(parents=True, exist_ok=True)

rows = []
for cls, filename, url, author, license_name, page in SOURCES:
    destination = DATA / cls / filename
    if not destination.exists():
        request = Request(url, headers={'User-Agent': 'DL029 educational dataset downloader/1.0'})
        with urlopen(request, timeout=45) as response, destination.open('wb') as out:
            out.write(response.read())
    rows.append([filename, cls, author, license_name, page, url, 'No changes'])
    print(f'Downloaded: {cls}/{filename}')

with (ROOT / 'ATTRIBUTION.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['filename', 'class', 'creator', 'license', 'source_page', 'direct_file_url', 'changes'])
    writer.writerows(rows)

print('\nStarter images downloaded. This is only 1 image per class, NOT enough to train or submit a reliable classifier.')
print('Use a larger, properly licensed dataset for final training and record every source/license.')
