"""Record weekly observations of the repository's GitHub star count."""
import argparse
import csv
from datetime import date, datetime, timezone
from io import StringIO
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
DATA = ASSETS / "star-history.csv"
CHART = ASSETS / "star-history.svg"


def draw(observations):
    days = sorted(observations)
    start, end = days[0], days[-1]
    span = max(1, (end - start).days)
    peak = max(1, max(observations.values()))
    points = []
    for day in days:
        x = 60 + 624 * (day - start).days / span
        y = 150 - 90 * observations[day] / peak
        points.append((x, y))
    coordinates = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    x, y = points[-1]
    end_tick = f'<text x="684" y="177" text-anchor="end">{end}</text>' if start != end else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 195" role="img" aria-labelledby="t d">
  <title id="t">GitHub star history</title>
  <desc id="d">Weekly observations from {start} to {end}. Latest count: {observations[end]}.</desc>
  <rect width="720" height="195" rx="8" fill="#f8f4e9"/>
  <g font-family="system-ui,sans-serif" fill="#182e51">
    <text x="32" y="35" font-size="21">GitHub stars</text>
    <text x="684" y="35" text-anchor="end" font-size="20">{observations[end]}</text>
    <path d="M60 60H684 M60 150H684" stroke="#c5c5bc" fill="none"/>
    <text x="45" y="65" text-anchor="end">{peak}</text><text x="45" y="155" text-anchor="end">0</text>
    <text x="60" y="177">{start}</text>{end_tick}
    <polyline points="{coordinates}" stroke="#25466b" stroke-width="3" fill="none"/>
    <circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="#bf4f28"/>
  </g>
</svg>
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--record", type=int, metavar="STARS")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    with DATA.open(newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != ["date", "stars"]:
            parser.error("Expected date,stars CSV header")
        rows = [(date.fromisoformat(row["date"]), int(row["stars"])) for row in reader]
    observations = dict(rows)
    if len(rows) != len(observations) or rows != sorted(rows) or any(n < 0 for _, n in rows):
        parser.error("Expected ordered, unique dates and nonnegative star counts")
    if args.check:
        if not rows or CHART.read_text() != draw(observations):
            parser.error("Star chart differs from its observations")
        return
    today = datetime.now(timezone.utc).date()
    if args.record < 0 or (rows and rows[-1][0] > today):
        parser.error("Invalid count or observation date")
    observations[today] = args.record
    buffer = StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["date", "stars"])
    writer.writerows(sorted(observations.items()))
    DATA.write_text(buffer.getvalue())
    CHART.write_text(draw(observations))


if __name__ == "__main__":
    main()
