"""Export functionality for attendance records."""

import csv
import json
from pathlib import Path
from typing import List, Dict
from datetime import datetime
from app.storage.attendance_db import AttendanceStorage


def export_to_csv(storage: AttendanceStorage, output_path: str) -> None:
    """
    Export attendance records to CSV.
    
    Args:
        storage: AttendanceStorage instance
        output_path: Path to output CSV file
    """
    records = storage.get_all_records()
    
    if not records:
        raise ValueError("No records to export")
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['student_id', 'subject', 'timestamp', 'verified'])
        writer.writeheader()
        writer.writerows(records)


def export_to_json(storage: AttendanceStorage, output_path: str) -> None:
    """
    Export attendance records to JSON.
    
    Args:
        storage: AttendanceStorage instance
        output_path: Path to output JSON file
    """
    records = storage.get_all_records()
    
    if not records:
        raise ValueError("No records to export")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
