#!/usr/bin/env python3
"""Rebuild data.min.json + index.html for the AI Engineer Melbourne 2026 schedule.

1. Trims the full schedule.json down to only the fields the page renders.
2. Injects that JSON into template.html, producing the single-file index.html.

Refresh the source data first:
    curl -s https://data.webdirections.org/ai-engineer/schedule.json -o schedule.json
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
SESSION_FIELDS = ("id", "title", "description", "type", "track",
                  "start_time", "end_time", "duration_minutes", "location")
SPEAKER_FIELDS = ("full_name", "job_title", "employer", "photo_url")


def trim(schedule):
    out = {"conference": schedule["conference"],
           "updated_at": schedule["updated_at"], "days": []}
    for d in schedule["days"]:
        nd = {"date": d["date"], "label": d["label"], "tracks": []}
        for t in d["tracks"]:
            if not t["sessions"]:
                continue
            nt = {"name": t["name"], "sessions": []}
            for se in t["sessions"]:
                row = {k: se.get(k) for k in SESSION_FIELDS}
                row["speakers"] = [{k: sp.get(k) for k in SPEAKER_FIELDS}
                                   for sp in se.get("speakers", [])]
                nt["sessions"].append(row)
            nd["tracks"].append(nt)
        out["days"].append(nd)
    return out


def main():
    schedule = json.loads((ROOT / "schedule.json").read_text())
    data = trim(schedule)
    (ROOT / "data.min.json").write_text(json.dumps(data))

    template = (ROOT / "template.html").read_text()
    (ROOT / "index.html").write_text(
        template.replace("__DATA__", json.dumps(data)))

    n = sum(len(t["sessions"]) for d in data["days"] for t in d["tracks"])
    print(f"Built index.html — {n} sessions across {len(data['days'])} days")


if __name__ == "__main__":
    main()
