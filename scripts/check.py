"""Pre-publish check: every JSON-LD block and the AASA file parse, and no TODO is left in public/.

Run: python3 scripts/check.py  (exit 1 lists what blocks publishing)
"""
import json
import re
import sys
from pathlib import Path

PUBLIC = Path(__file__).resolve().parent.parent / "public"
problems = []

for page in sorted(PUBLIC.rglob("*.html")):
    text = page.read_text()
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
        try:
            json.loads(block)
        except json.JSONDecodeError as error:
            problems.append(f"{page.relative_to(PUBLIC)}: bad JSON-LD ({error})")

try:
    json.loads((PUBLIC / ".well-known/apple-app-site-association").read_text())
except json.JSONDecodeError as error:
    problems.append(f".well-known/apple-app-site-association: bad JSON ({error})")

for path in sorted(PUBLIC.rglob("*")):
    if path.is_file() and path.suffix in {".html", ".txt", ".xml", ".css"}:
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if "TODO" in line:
                problems.append(f"{path.relative_to(PUBLIC)}:{number}: {line.strip()[:110]}")

print("\n".join(problems) or "Ready to publish.")
sys.exit(1 if problems else 0)
