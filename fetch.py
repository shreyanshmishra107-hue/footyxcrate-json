import json
import time
import urllib.request

SOURCE_URL = f"https://sonujson-v6.pages.dev/Data/events/allinone.json?t={int(time.time())}"
OUTPUT_FILE = "allinone.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json",
    "Referer": "https://sonujson-v6.pages.dev/",
}

try:
    req = urllib.request.Request(SOURCE_URL, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as response:
        raw_data = response.read().decode("utf-8")

    # Validate JSON structure
    data = json.loads(raw_data)

    # Rebrand references to FootyXCrate
    cleaned = json.dumps(data, indent=2, ensure_ascii=False)
    cleaned = cleaned.replace("sonujson", "FootyXCrate")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(cleaned)

    print(f"Successfully updated {OUTPUT_FILE}")
except Exception as e:
    print(f"Failed to fetch {OUTPUT_FILE}: {e}")
    raise
