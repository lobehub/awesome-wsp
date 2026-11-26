# Further studies in weight-space programming

[Back to the main reading list](README.md)

These studies extend the introductory list with replications, comparisons and applications. For each experiment, the annotation identifies a control, baseline or test condition that matters when interpreting the result.

[Replications and controls](#replications-and-controls) · [Editing language and vision models](#editing-language-and-vision-models) · [Control, games and verification](#control-games-and-verification) · [Scientific models and decision systems](#scientific-models-and-decision-systems)

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
