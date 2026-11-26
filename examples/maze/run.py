"""Run the published LoopedWSP maze weights on the accompanying square grid."""
from pathlib import Path
import subprocess
import sys
import tempfile
from urllib.request import urlopen

RELEASE = "https://raw.githubusercontent.com/mbzuai-oryx/LoopedWSP/2752cd9f2d2e1e3e30e6686b3dbc23d8bcab875c/weights"
FILES = ("run.py", "networks/maze.json", "networks/maze.npz")
MAZE = Path(__file__).with_name("maze.txt").resolve()
EXPECTED_CHECK = "check: valid path True, shortest True, the D<L<R<U-smallest shortest path (dataset tie-break) True"


def main():
    rows = MAZE.read_text().splitlines()
    if not rows or any(len(row) != len(rows) for row in rows):
        sys.exit("maze.txt must contain a square grid.")
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        (root / "networks").mkdir()
        for name in FILES:
            with urlopen(f"{RELEASE}/{name}", timeout=30) as response:
                (root / name).write_bytes(response.read())
        result = subprocess.run([sys.executable, root / "run.py", "maze", MAZE],
                                check=True, stdout=subprocess.PIPE, text=True)
    print(result.stdout, end="")
    if EXPECTED_CHECK not in result.stdout.splitlines():
        sys.exit("The upstream verifier did not confirm the expected shortest path.")


if __name__ == "__main__":
    main()
