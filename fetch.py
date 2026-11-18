import json
import os
import time
import urllib.request

SOURCE_URL = f"https://sonujson-v6.pages.dev/Data/events/allinone.json?t={int(time.time())}"
OUTPUT_DIR = "Data/events"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "allinone.json")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json",
    "Referer": "https://sonujson-v6.pages.dev/",
}

os.makedirs(OUTPUT_DIR, exist_ok=True)

req = urllib.request.Request(SOURCE_URL, headers=HEADERS)
with urllib.request.urlopen(req, timeout=20) as response:
    raw_data = response.read().decode("utf-8")

data = json.loads(raw_data)
cleaned = json.dumps(data, indent=2, ensure_ascii=False).replace("sonujson", "FootyXCrate")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(cleaned)

print(f"Updated {OUTPUT_FILE}")
