"""Simple file-based storage for attendance records."""

import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
from app.config import DATA_DIR


class AttendanceStorage:
    """File-based storage for attendance records."""
    
    def __init__(self, db_file: str = "attendance.json"):
        self.db_path = DATA_DIR / db_file
        self.records: List[Dict] = []
        self.load()
    
    def load(self) -> None:
        """Load records from file."""
        if self.db_path.exists():
            try:
                with open(self.db_path, 'r') as f:
                    self.records = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.records = []
        else:
            self.records = []
    
    def save(self) -> None:
        """Save records to file."""
        try:
            with open(self.db_path, 'w') as f:
                json.dump(self.records, f, indent=2)
        except IOError as e:
            raise Exception(f"Failed to save attendance records: {e}")
    
    def add_record(self, student_id: str, subject: str, verified: bool = True) -> Dict:
        """Add a new attendance record."""
        record = {
            "student_id": student_id,
            "subject": subject,
            "timestamp": datetime.now().isoformat(),
            "verified": verified
        }
        self.records.append(record)
        self.save()
        return record
    
    def get_student_records(self, student_id: str) -> List[Dict]:
        """Get all records for a student."""
        return [r for r in self.records if r.get("student_id") == student_id]
    
    def get_subject_records(self, subject: str) -> List[Dict]:
        """Get all records for a subject."""
        return [r for r in self.records if r.get("subject") == subject]
    
    def get_all_records(self) -> List[Dict]:
        """Get all attendance records."""
        return self.records.copy()
