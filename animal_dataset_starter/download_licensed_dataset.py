
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json
import csv
import time
import re

PACK_DIR = Path(__file__).resolve().parent
ROOT = PACK_DIR.parent
DATA = ROOT / "dataset" / "raw"
CLASSES = ["butterfly", "cat", "dog", "elephant", "horse"]
TARGET = 100

for cls in CLASSES:
    (DATA / cls).mkdir(parents=True, exist_ok=True)

def api_request(params):
    url = "https://commons.wikimedia.org/w/api.php?" + urlencode(params)
    req = Request(url, headers={"User-Agent": "DL029StudentProject/1.0 (educational use)"})
    with urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))

rows = []
csv_path = ROOT / "ATTRIBUTION.csv"

if csv_path.exists():
    with csv_path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

existing = {r["filename"] for r in rows}

for cls in CLASSES:
    folder = DATA / cls
    count = len(list(folder.glob("*.*")))
    print(f"\nSearching {cls}: already have {count} images")

    continuation = {}
    while count < TARGET:
        params = {
            "action": "query",
            "format": "json",
            "generator": "search",
            "gsrsearch": f"{cls} animal filetype:bitmap",
            "gsrnamespace": 6,
            "gsrlimit": 50,
            "prop": "imageinfo",
            "iiprop": "url|extmetadata",
        }
        params.update(continuation)

        try:
            data = api_request(params)
        except Exception as e:
            print("API error:", e)
            break

        pages = data.get("query", {}).get("pages", {})
        if not pages:
            break

        for page in pages.values():
            info = page.get("imageinfo", [{}])[0]
            meta = info.get("extmetadata", {})
            license_name = meta.get("LicenseShortName", {}).get("value", "")
            license_name = re.sub("<.*?>", "", license_name)

            if not any(x in license_name.lower() for x in
                       ["cc0", "public domain", "public-domain"]):
                continue

            url = info.get("url", "")
            if not url.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                continue

            original = page.get("title", "").replace("File:", "")
            safe = re.sub(r"[^A-Za-z0-9_.-]", "_", original)
            filename = f"{cls}_{count+1:04d}_{safe}"
            if filename in existing:
                continue

            destination = folder / filename
            try:
                req = Request(url, headers={
                    "User-Agent": "DL029StudentProject/1.0 (educational use)"
                })
                with urlopen(req, timeout=30) as response:
                    content = response.read()

                if len(content) < 1000:
                    continue

                destination.write_bytes(content)
                artist = meta.get("Artist", {}).get("value", "Unknown")
                artist = re.sub("<.*?>", "", artist)
                source = "https://commons.wikimedia.org/wiki/" + page["title"]

                rows.append({
                    "filename": filename,
                    "class": cls,
                    "creator": artist,
                    "license": license_name,
                    "source_page": source,
                    "direct_file_url": url,
                    "changes": "No changes"
                })
                existing.add(filename)
                count += 1
                print(f"{cls}: {count}/{TARGET}")

                if count >= TARGET:
                    break
                time.sleep(0.3)

            except Exception as e:
                print("Skipped:", filename, str(e))

        continuation = data.get("continue", {})
        if not continuation:
            break

    print(f"Finished {cls}: {count} images")

with csv_path.open("w", newline="", encoding="utf-8") as f:
    fields = ["filename", "class", "creator", "license",
              "source_page", "direct_file_url", "changes"]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

print("\nAttribution saved:", csv_path)
print("Dataset download process finished.")
