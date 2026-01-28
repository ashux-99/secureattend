"""Attendance data models."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class AttendanceRecord:
    """Represents a single attendance record."""
    student_id: str
    subject: str
    timestamp: datetime
    verified: bool = False
    signature: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "student_id": self.student_id,
            "subject": self.subject,
            "timestamp": self.timestamp.isoformat(),
            "verified": self.verified
        }
