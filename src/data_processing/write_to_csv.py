# src/data_processing/write_to_csv.py
from pathlib import Path
import csv
import json

# Project root: ...\LukGeo_koodi2025Final\
ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CFG = ROOT / "aineiston_kasittely" / "config_files" / "config.json"

def write_to_csv(data, output_file, config_path: Path | str = DEFAULT_CFG):
    # Resolve output path (allow relative or absolute)
    out_path = Path(output_file)
    if not out_path.is_absolute():
        out_path = ROOT / out_path

    # Ensure parent directory exists
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Load column names from config if available; otherwise infer from data
    column_names = None
    cfg_path = Path(config_path)
    if cfg_path.is_file():
        with cfg_path.open("r", encoding="utf-8") as f:
            cfg = json.load(f)
        column_names = cfg.get("column_names")

    if not column_names:
        if data:
            column_names = list(data[0].keys())  # fallback
        else:
            raise ValueError("No data rows and no column_names in config.json.")

    # Write CSV
    with out_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_names, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ Wrote CSV: {out_path}")
