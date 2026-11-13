"""Validation schema for Pellucid annotation records."""

REQUIRED_FIELDS = ("record_id", "text")


def validate_record(record: dict) -> bool:
    if not isinstance(record, dict):
        return False
    for field in REQUIRED_FIELDS:
        if not record.get(field):
            return False
    labels = record.get("labels", [])
    if not isinstance(labels, list):
        return False
    return all(isinstance(label, str) and label.strip() for label in labels)
