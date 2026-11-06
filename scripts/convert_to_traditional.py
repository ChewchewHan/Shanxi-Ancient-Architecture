from pathlib import Path
from opencc import OpenCC

ROOT = Path(".")
converter = OpenCC("s2twp")
extensions = {".md", ".csv", ".json", ".kml", ".txt"}
old_url = "https://github.com/ChewchewHan/VCG/blob/main/%E5%B1%B1%E8%A5%BF%E5%90%84%E5%B8%82.kml"
new_url = "https://www.bilibili.com/video/BV12eYXeTE2A"
old_file = "VCG/山西各市.kml"
new_file = "Bilibili 影片提供的地點資訊（整理後轉為 KML）"

for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in extensions:
        continue
    if ".git" in path.parts or ".github" in path.parts or "scripts" in path.parts:
        continue
    try:
        original = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    updated = converter.convert(original)
    updated = updated.replace(old_url, new_url).replace(old_file, new_file)
    if updated != original:
        path.write_text(updated, encoding="utf-8", newline="\n")
        print(f"Updated: {path}")
