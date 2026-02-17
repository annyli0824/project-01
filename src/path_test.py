from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parent.parent
RAW_DIR = ROOT / "data" / "raw"
OUT_DIR = ROOT / "outputs"

print("HERE:", HERE)
print("ROOT:", ROOT)
print("RAW_DIR:", RAW_DIR)
print("OUT_DIR:", OUT_DIR)
