"""Pellucid annotation helpers."""

import json
from typing import Dict, Iterable, List

from .schema import validate_record


def load_records(path: str) -> List[Dict]:
    records = []
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def annotate(records: Iterable[Dict], labeler: str) -> List[Dict]:
    out = []
    for record in records:
        item = dict(record)
        item.setdefault("labels", [])
        item["labeler"] = labeler
        if validate_record(item):
            out.append(item)
    return out


def consensus_label(records: Iterable[Dict], field: str = "label") -> str:
    counts: Dict[str, int] = {}
    for record in records:
        label = str(record.get(field, ""))
        counts[label] = counts.get(label, 0) + 1
    if not counts:
        return ""
    return max(counts.items(), key=lambda kv: kv[1])[0]
