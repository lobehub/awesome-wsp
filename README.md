# Awesome Weight-Space Programming

A curated reading list on **weight-space programming (WSP)**, the study of how a programmer, often a language-model agent, can inspect a neural network's parameters, edit them, or construct a working network by assigning its weights directly.

A maze solver makes the idea concrete. In LoopedWSP, a coding agent writes the weight matrices of a small transformer so that one pass through its shared block advances a search through the maze. At inference time, that transformer solves new mazes on its own. Editing a pretrained model poses a different problem. The editor must locate a useful change in weights whose original roles it did not design. [LoopedWSP project](https://mbzuai-oryx.github.io/LoopedWSP/) · [WeightCode paper](https://arxiv.org/abs/2611.25476)

[Start here](#start-here) · [Reading weights](#reading-weights) · [Editing checkpoints](#editing-checkpoints) · [Writing networks](#writing-networks) · [Benchmarks](#benchmarks) · [Foundations](#foundations) · [BibTeX](references.bib)

## Start here

1. **Read the original experiments.** In *Sparks of Weight-Space Programming*, Takehi, Teoh, Zhang and Khattab ask an agent to identify policies, repair failures and build networks. Read the Qwen experiment alongside its logs. The agent could run Python and inspect forward-pass results while searching for the edit that reduced repeated reasoning. [Research article](https://rikiyat.github.io/blog/weight-space-programming/) · [Experiment logs](https://github.com/RikiyaT/lm_understand-logs) · [Edited checkpoint](https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming)
2. **Inspect a constructed network.** The LoopedWSP release includes both the prompts given to the programmer and the weights of the resulting solvers. Follow the maze example from a cell's state through one update, then look at what changes when the same block runs again. [Walkthrough](https://mbzuai-oryx.github.io/LoopedWSP/) · [Prompts](https://github.com/mbzuai-oryx/LoopedWSP/tree/main/prompts) · [Weights](https://github.com/mbzuai-oryx/LoopedWSP/tree/main/weights)
3. **Check what generalizes.** WeightBench puts reading, repair and construction in one evaluation. Its task registry is a useful place to check the target network, the information the programmer receives and how success is scored. [Paper](https://arxiv.org/abs/2611.18553) · [Benchmark repository](https://github.com/Aayush-Marasini/WeightBench)

## Reading weights

- **Auditing zero-shot weight reading.** In an exploratory study, an LLM sees the weights of small image classifiers as text, with no forward passes. When CIFAR-10 labels are permuted, it still finds a numerical split in the output layer but assigns the wrong meanings to the class pairs it interprets. The permutation is a useful control for familiarity with public datasets. [Preprint](https://arxiv.org/abs/2611.08070)
- **Mixed Signals.** On EEG and ECG networks, the authors test three abilities separately. The agent can repair some deliberately planted faults and construct networks from a few subjects' data. Identifying the original task from weights alone proves unreliable. [Preprint](https://arxiv.org/abs/2611.13758)

## Editing checkpoints

| Study | What the editor changes | What the evaluation tests |
| --- | --- | --- |
| **WSP-Scope** | An agent searches for localized edits to two sizes of Qwen3.5. | Six of 16 searches keep the original checkpoint. The authors test accepted edits on held-out questions and on tasks beyond the editing objective. [Paper](https://arxiv.org/abs/2611.09382) · [Code](https://github.com/WSP-Scope/WSP-Scope-Project) |
| **WeightCode** | An agent writes an executable program that reads a trained network and computes a weight update. | Rerunning the program on independently trained vision transformers tests whether the editing procedure transfers. Copying the original numerical update provides a control. [Paper](https://arxiv.org/abs/2611.25476) · [Code](https://github.com/Gen-Verse/WeightCode) |
| **Language Models Can Rewrite Their Own Weights** | A 27B model inspects its own answers, runs candidate edits and selects changes using practice problems. | The authors measure held-out accuracy and recovery of a damaged copy. Smaller models in the same family struggle in this setup. [Preprint](https://arxiv.org/abs/2611.21885) |

## Writing networks

| Study | What the programmer receives | What it builds |
| --- | --- | --- |
| **LoopedWSP** | An algorithmic task and a looped transformer architecture. | Explicit weights that implement repeated computation for mazes, Sudoku and other reasoning tasks. The release includes the generated weights. [Research article](https://mbzuai-oryx.github.io/LoopedWSP/) · [Code and weights](https://github.com/mbzuai-oryx/LoopedWSP) |
| **Interpretable weight-space programming** | An agent writes model code and receives validation scores across revisions. | Transformers for tasks such as addition and sorting, and encoding models whose features can be inspected to study neural responses. [Paper](https://arxiv.org/abs/2611.18114) · [Code, prompts and logs](https://github.com/csinva/weight-space-programming-autoresearch) |
| **Weight-Space Programming Doesn't Need Transformers** | A small set of labeled science questions and freedom to choose the architecture. | Sparse lookup-based models for the AI2 Reasoning Challenge. The comparison measures accuracy, parameter count and inference time. [Paper](https://arxiv.org/abs/2611.22055) · [Code and models](https://github.com/effl-lab/Weight-Space-Programming) |
| **Zero-shot WSP for structured datasets** | A small labeled table and a fixed feed-forward architecture, with no execution feedback. | Literal weights and biases for prediction or classification. Rotated synthetic data test whether the programmer can discover structure oblique to the input coordinates. [Preprint](https://arxiv.org/abs/2611.19292) |
| **Physics2Weight** | A governing equation and its initial and boundary conditions. | A neural approximation to a PDE solution. The four-equation study reports both solution error and how closely predictions satisfy the governing equation, which can diverge on nonlinear problems. [Preprint](https://arxiv.org/abs/2611.12954) |

## Benchmarks

- **WeightBench** spans 42 tasks in five tracks covering reading, repair, construction, recognition of impossible edits and data-free compression. Consult the per-track scores and the number of tasks each model attempted before comparing aggregate results. [Paper](https://arxiv.org/abs/2611.18553) · [Task registry and harness](https://github.com/Aayush-Marasini/WeightBench)
- **IWIBench** tests ten editing objectives under bounded tensor access and a fixed rollout budget. A separate validator reapplies each patch and measures both the requested behavior and preservation of other capabilities. [Preprint](https://arxiv.org/abs/2611.08647)

When comparing results, check what the programmer could see before submission. Writing weights once from a task description, revising them against validation scores, and inspecting a running checkpoint give the programmer different amounts of information. For an edit, look for both a held-out test of the new behavior and a test of what the original network could already do.

## Foundations

- **Tracr** compiles a program written in RASP into transformer weights. Knowing the source algorithm gives researchers a reference for checking what an interpretability method recovers from the compiled model. [Publication](https://deepmind.google/research/publications/22295/) · [Compiler](https://github.com/google-deepmind/tracr)
- **AdderBoard** asks entrants to build the smallest transformer that adds two ten-digit integers. Its submissions and verifier let readers inspect different weight constructions for the same precisely specified task. [Challenge and verifier](https://github.com/anadim/AdderBoard)

## Contributing

Add a paper, project or benchmark through a pull request. Link the authors' primary source and describe the target network, the weight operation and how the result was evaluated. Where available, link directly to released code, weights or logs. For work on program compilation or hand-built circuits, explain its connection to WSP in the Foundations section.
