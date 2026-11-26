# Weight-space programming research index

[Reading guide](README.md) · [BibTeX](references.bib)

**Weight operations** · [Read](#reading-weights) · [Edit](#editing-checkpoints) · [Write](#writing-networks) · [Evaluate](#benchmarks)

**Further studies** · [Replications](#replications-and-controls) · [Language and vision](#editing-language-and-vision-models) · [Control and games](#control-games-and-verification) · [Scientific applications](#scientific-models-and-decision-systems)

## Original experiments

In *Sparks of Weight-Space Programming*, Takehi, Teoh, Zhang and Khattab ask an agent to identify policies, repair failures and build networks. Read the Qwen experiment alongside its logs. The agent could run Python and inspect forward-pass results while searching for the edit that reduced repeated reasoning. [Research article](https://rikiyat.github.io/blog/weight-space-programming/) · [Experiment logs](https://github.com/RikiyaT/lm_understand-logs) · [Edited checkpoint](https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming)

## Reading weights

- **Auditing zero-shot weight reading.** In an exploratory study, an LLM sees the weights of small image classifiers as text, with no forward passes. When CIFAR-10 labels are permuted, it still finds a numerical split in the output layer but assigns the wrong meanings to the class pairs it interprets. The permutation is a useful control for familiarity with public datasets. [Preprint](https://arxiv.org/abs/2611.08070)
- **Mixed Signals.** On EEG and ECG networks, the authors test three abilities separately. The agent can repair some deliberately planted faults and construct networks from a few subjects' data. Identifying the original task from weights alone proves unreliable. [Preprint](https://arxiv.org/abs/2611.13758)

## Editing checkpoints

- **WSP-Scope** — An agent searches for localized edits to two sizes of Qwen3.5. Six of 16 searches keep the original checkpoint. The authors test accepted edits on held-out questions and on tasks beyond the editing objective. [Paper](https://arxiv.org/abs/2611.09382) · [Code](https://github.com/WSP-Scope/WSP-Scope-Project)

- **WeightCode** — An agent writes an executable program that reads a trained network and computes a weight update. Rerunning the program on independently trained vision transformers tests whether the editing procedure transfers. Copying the original numerical update provides a control. [Paper](https://arxiv.org/abs/2611.25476) · [Code](https://github.com/Gen-Verse/WeightCode)

- **Language Models Can Rewrite Their Own Weights** — A 27B model inspects its own answers, runs candidate edits and selects changes using practice problems. The authors measure held-out accuracy and recovery of a damaged copy. Smaller models in the same family struggle in this setup. [Preprint](https://arxiv.org/abs/2611.21885)

## Writing networks

- **LoopedWSP** — An algorithmic task and a looped transformer architecture. Explicit weights that implement repeated computation for mazes, Sudoku and other reasoning tasks. The release includes the generated weights. [Research article](https://mbzuai-oryx.github.io/LoopedWSP/) · [Code and weights](https://github.com/mbzuai-oryx/LoopedWSP)

- **Interpretable weight-space programming** — An agent writes model code and receives validation scores across revisions. Transformers for tasks such as addition and sorting, and encoding models whose features can be inspected to study neural responses. [Paper](https://arxiv.org/abs/2611.18114) · [Code, prompts and logs](https://github.com/csinva/weight-space-programming-autoresearch)

- **Weight-Space Programming Doesn't Need Transformers** — A small set of labeled science questions and freedom to choose the architecture. Sparse lookup-based models for the AI2 Reasoning Challenge. The comparison measures accuracy, parameter count and inference time. [Paper](https://arxiv.org/abs/2611.22055) · [Code and models](https://github.com/effl-lab/Weight-Space-Programming)

- **Zero-shot WSP for structured datasets** — A small labeled table and a fixed feed-forward architecture, with no execution feedback. Literal weights and biases for prediction or classification. Rotated synthetic data test whether the programmer can discover structure oblique to the input coordinates. [Preprint](https://arxiv.org/abs/2611.19292)

- **Physics2Weight** — A governing equation and its initial and boundary conditions. A neural approximation to a PDE solution. The four-equation study reports both solution error and how closely predictions satisfy the governing equation, which can diverge on nonlinear problems. [Preprint](https://arxiv.org/abs/2611.12954)

## Benchmarks

- **WeightBench** spans 42 tasks in five tracks covering reading, repair, construction, recognition of impossible edits and data-free compression. Consult the per-track scores and the number of tasks each model attempted before comparing aggregate results. [Paper](https://arxiv.org/abs/2611.18553) · [Task registry and harness](https://github.com/Aayush-Marasini/WeightBench)
- **IWIBench** tests ten editing objectives under bounded tensor access and a fixed rollout budget. A separate validator reapplies each patch and measures both the requested behavior and preservation of other capabilities. [Preprint](https://arxiv.org/abs/2611.08647)

When comparing results, check what the programmer could see before submission. Writing weights once from a task description, revising them against validation scores, and inspecting a running checkpoint give the programmer different amounts of information. For an edit, look for both a held-out test of the new behavior and a test of what the original network could already do.

## Replications and controls

- **Reading game policies and compiling them.** Across three new games, the reader recovered the layout of the board more reliably than the rules. In the writing experiment, independently reconstructed Python programs matched the actions of a written Breakout network on every state tested. [Preprint](https://arxiv.org/abs/2611.21449v1)

- **Same Fix, Different Weights.** Claude reproduced the improvement on a looping Qwen model through changes at the output. The original experiment had removed an internal loop direction. The two mechanisms can therefore produce similar benchmark gains. [Preprint](https://arxiv.org/abs/2611.20953v1) · [Repository](https://github.com/Cenrax/weight-space-programming-claude)

- **Precision controls for vision-language model repair.** Rescaling originally 16-bit weights in 32-bit arithmetic left a telltale pattern. Rounding the corrupted weights preserved answers on the test questions but eliminated exact unaided recovery in both VLMs. [Preprint](https://arxiv.org/abs/2611.23615v1)

- **Black-box versus white-box auditing.** On prediction networks trained on simulated clinical cohorts, access to predictions and a calculation tool matched access to weights on the tested audits. The authors release the simulated networks, prompts and replies. [Preprint](https://arxiv.org/abs/2611.07847v1) · [Repository](https://github.com/Chth1z/llm-clinical-network-audit)

- **Self-WSP.** A Qwen3.5-0.8B checkpoint proposes an edit to itself and continues as both solver and editor. Some edits improved held-out math accuracy, but random search sometimes performed comparably. [Preprint](https://arxiv.org/abs/2611.28833v1)

- **Deterministic forward-only editing.** Using the same library of editing operations for both methods, the authors compare a deterministic routing procedure with a 27B language model. This isolates how much choosing an operator contributes once the operators are already available. [Preprint](https://arxiv.org/abs/2611.34612v1)

## Editing language and vision models

- **Tool-free repair after quantization.** Given both the floating-point CNN and its degraded 4-bit copy, Opus recovered CIFAR-10 accuracy from 60.4% to 77.95% when allowed one answer per layer. Giving only the floating-point weights led to different rounding behavior. [Preprint](https://arxiv.org/abs/2611.33031v1) · [Repository](https://github.com/urbste/weight-space-programming-ptq)

- **TowerBridge.** An agent editing CLIP-style dual encoders repeatedly changed an output projection. The team distilled its strategy into a closed-form retrieval correction and tested it on eight additional CLIP checkpoints the agent had never edited. [Preprint](https://arxiv.org/abs/2611.31233v1)

- **Keel.** A multimodal editor investigates repeated reasoning on image questions and tests candidate changes to small Qwen vision-language models. The evaluation across six image benchmarks tracks both looping and answer accuracy. [Preprint](https://arxiv.org/abs/2611.25257v1)

- **Writing in-context learning into weights.** Editors use examples to make a task persist when the examples are removed from the prompt. Across six tasks, changed wording and unfinished editing runs both affect how closely the edits match fine-tuning. [Preprint](https://arxiv.org/abs/2611.26841v1) · [Repository](https://github.com/y3nk0/weight-space-programming-study)

- **Spatial reasoning with WSP and LoRA.** A published Qwen patch helped answers finish. A rank-one adapter trained on worked solutions delivered larger gains on the target spatial tasks, alongside a sharp drop on two neighboring distance tasks. [Preprint](https://arxiv.org/abs/2611.27089v1)

- **Diffusion editing with generated programs.** On 24 Stable Diffusion edits, the preregistered rewriting procedure showed no advantage over a strong baseline. In an exploratory comparison, revising programs improved a CLIP metric while whole-image joint success fell. [Preprint](https://arxiv.org/abs/2611.22228v1)

- **Training vision models to be editable.** Five LLMs edited convolutional networks and vision transformers. More than 2,600 edits let the authors compare how the target’s training procedure affects later edit success, side effects and held-out accuracy. [Preprint](https://arxiv.org/abs/2611.26408v1) · [Project](https://viscom.uni-ulm.de/wsp)

- **Reparameterizing object detectors.** A numerical procedure expands detector layers into an equivalent representation, edits them, then folds them back. The paper measures how much this change of coordinates buys across 17 detectors, including settings that preserve inference cost. [Preprint](https://arxiv.org/abs/2611.29882v1) · [Repository](https://github.com/WongKinYiu/ODWSP)

## Control, games and verification

- **Steering a real tractor.** Two editors modified or constructed a 253-parameter steering controller using simulated feedback. The field test compared path tracking on a real tractor with pure pursuit. Their tracking errors were of the same order. [Preprint](https://arxiv.org/abs/2611.21958v1)

- **Repairing a robot foundation model.** Small edits to a pretrained vision-language-action policy helped it recover from recurring stuck states in simulation. Reversed and random edits tested whether the intended correction explained the gain. [Preprint](https://arxiv.org/abs/2611.31715v1)

- **Compiling known game rules.** Writers received simulator source for 20 previously unpublished game families with held-out level data removed. The best fixed-architecture writer solved 56% of held-out levels with feedback. Python players from the four main writers solved 97–100%. [Preprint](https://arxiv.org/abs/2611.16981v1) · [Repository](https://github.com/JensLehmann/weight-space-programming-games)

- **Model checking written policies.** A probabilistic model checker evaluates a written policy against a formal requirement. In one run, fitting optimal actions raised action accuracy to 98.4% but broke the requirement. Feedback from the checker let the editor restore it. [Preprint](https://arxiv.org/abs/2611.11604v1) · [Repository](https://github.com/LAVA-LAB/COOL-MC/tree/wsp_verified)

## Scientific models and decision systems

- **Weights & Caches.** The team programs a tabular model from zero weights, repairs a regression failure in a pretrained model, and separately edits its inference cache. Only the first two experiments change parameters. [Preprint](https://arxiv.org/abs/2611.20174v1)

- **Writing medical image classifiers.** Two LLMs wrote small CNNs in a single reply without seeing any images. Both scored above chance on six MedMNIST tasks, but fitting the same architecture to just 256 labeled images gave higher AUC on every one. [Preprint](https://arxiv.org/abs/2611.12066v1) · [Repository](https://github.com/MaximilianLindholz/weight-space-programming-medical)

- **Editing a particle-physics classifier.** Adding a single soft neutral particle could change a jet classification. The authors compare agent-written edits with edits guided by sparse autoencoders and test whether the repair transfers to other signal classes. [Preprint](https://arxiv.org/abs/2611.27079v1) · [Repository](https://github.com/rbonnetguerrini/WSP-mech-interp-for-model-editing-in-particle-physics)

- **Scoring rules for exact optimization.** An LLM wrote small networks to guide routing and branching decisions. On held-out Atlanta crew schedules its branching rule beat the solver default, but a standard pseudocost rule was just as fast. [Preprint](https://arxiv.org/abs/2611.09559v1) · [Repository](https://github.com/butkeraites/llm-written-weights-or)

- **Closed-form classifiers on frozen encoders.** An LLM helped design programs that fit classifier heads to labeled examples on a frozen RoBERTa encoder. Results on six held-out datasets temper the stronger comparison with fine-tuning on the eleven datasets used to develop the recipe. [Preprint](https://arxiv.org/abs/2611.33972v1)

- **WeightLoop.** A fixed editor writes a reusable program that updates a predictor as measurements arrive. Offline replay tests whether those persistent changes improve the ranking of candidates for the next measurement. [Preprint](https://arxiv.org/abs/2611.07319v1)

## Foundations

- **Tracr** compiles a program written in RASP into transformer weights. Knowing the source algorithm gives researchers a reference for checking what an interpretability method recovers from the compiled model. [Publication](https://deepmind.google/research/publications/22295/) · [Compiler](https://github.com/google-deepmind/tracr)
- **AdderBoard** asks entrants to build the smallest transformer that adds two ten-digit integers. Its submissions and verifier let readers inspect different weight constructions for the same precisely specified task. [Challenge and verifier](https://github.com/anadim/AdderBoard)
