# Run the LoopedWSP maze weights

A coding agent wrote the weights of a transformer block that advances a search through a maze. This example runs the released network on a fixed 7×7 grid and checks the path with the authors’ verifier. You need a CPU, an internet connection for the download, and Python with NumPy. [Authors’ walkthrough](https://mbzuai-oryx.github.io/LoopedWSP/) · [Interactive browser demo](https://mbzuai-oryx.github.io/LoopedWSP/demo/maze.html)

From a checkout of Awesome WSP, run:

```sh
uv run --no-project --python 3.13 --with numpy==2.5.5 python examples/maze/run.py
```

With Python and NumPy already installed, use `python3 examples/maze/run.py`. The launcher downloads the upstream runner, maze configuration and weights from commit `2752cd9` into a temporary directory. [Pinned upstream release](https://github.com/mbzuai-oryx/LoopedWSP/tree/2752cd9f2d2e1e3e30e6686b3dbc23d8bcab875c/weights) · [Runner](https://raw.githubusercontent.com/mbzuai-oryx/LoopedWSP/2752cd9f2d2e1e3e30e6686b3dbc23d8bcab875c/weights/run.py) · [Configuration](https://raw.githubusercontent.com/mbzuai-oryx/LoopedWSP/2752cd9f2d2e1e3e30e6686b3dbc23d8bcab875c/weights/networks/maze.json) · [Weights](https://raw.githubusercontent.com/mbzuai-oryx/LoopedWSP/2752cd9f2d2e1e3e30e6686b3dbc23d8bcab875c/weights/networks/maze.npz)

## Read the output

The [input grid](maze.txt) has one start (`S`), one goal (`G`), walls (`#`) and open spaces. Each `o` below marks an intermediate cell on the selected path.

```text
#######
#S#ooG#
#o#o# #
#ooo# #
### # #
#     #
#######
check: valid path True, shortest True, the D<L<R<U-smallest shortest path (dataset tie-break) True
```

The first check tests whether the marked cells form a valid path. The second checks its length against a breadth-first search. The third checks which shortest path the model selected when several have the same length, using down, left, right, up as the move priority. A failed check makes the launcher exit with an error.

To try another input, edit `maze.txt` and run the command again. Use a square grid, with one start and one goal connected by open cells. Each run verifies that particular input.
