# AI Engineer Melbourne 2026 — Schedule

A single-file, vertical track schedule for [AI Engineer Melbourne 2026](https://webdirections.org/ai-engineer/).
Time runs top-to-bottom, tracks are columns. Click any session for details.

**Live:** https://mitch145.github.io/REPO_NAME/

## Features
- Day tabs (Wed Jun 3 / Thu Jun 4)
- Toggle tracks on/off, color-coded
- Search talks & speakers
- Session detail modal with speaker photos
- Live "NOW" marker during the conference

## Regenerating the data
Data is fetched from `data.webdirections.org` and embedded into `index.html`:

```sh
curl -s https://data.webdirections.org/ai-engineer/schedule.json -o schedule.json
python3 build.py   # rebuilds data.min.json + index.html from template.html
```
