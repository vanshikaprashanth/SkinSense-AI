from pathlib import Path
from datetime import datetime
import sqlite3
import uuid

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
UPLOADS = DATA / "uploads"
DB = DATA / "skinsense.db"

def init_db():
    UPLOADS.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB) as con:
        con.execute("""CREATE TABLE IF NOT EXISTS checkins (
            id TEXT PRIMARY KEY, created_at TEXT, filename TEXT, image_file TEXT,
            note TEXT, width INTEGER, height INTEGER, brightness REAL)""")
        con.commit()

def save_record(image_bytes, filename, note, metrics):
    suffix = Path(filename).suffix.lower()
    if suffix not in {".jpg", ".jpeg", ".png"}:
        suffix = ".jpg"
    image_name = f"{uuid.uuid4()}{suffix}"
    (UPLOADS / image_name).write_bytes(image_bytes)
    created = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    with sqlite3.connect(DB) as con:
        con.execute("INSERT INTO checkins VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (
            str(uuid.uuid4()), created, Path(filename).name, image_name, note,
            metrics["width"], metrics["height"], metrics["brightness"]))
        con.commit()

def get_records():
    with sqlite3.connect(DB) as con:
        con.row_factory = sqlite3.Row
        return [dict(x) for x in con.execute("SELECT * FROM checkins ORDER BY created_at DESC").fetchall()]

def get_image_path(name):
    return UPLOADS / Path(name).name
