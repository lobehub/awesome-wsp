# Weight-space programming research index

[Reading guide](README.md) · [BibTeX](references.bib)

**Weight operations** · [Read](#reading-weights) · [Edit](#editing-checkpoints) · [Write](#writing-networks) · [Evaluate](#benchmarks)

**Further studies** · [Replications](#replications-and-controls) · [Language and vision](#editing-language-and-vision-models) · [Control and games](#control-games-and-verification) · [Scientific applications](#scientific-models-and-decision-systems)

## Original experiments

- [Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights](https://rikiyat.github.io/blog/weight-space-programming/) · *Rikiya Takehi et al., 2026*. In the Qwen repair experiment, the agent inspected weights and ran forward passes to find an edit that reduced repeated reasoning. [Experiment logs](https://github.com/RikiyaT/lm_understand-logs) · [Edited checkpoint](https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming)

## Reading weights

- [Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming"](https://arxiv.org/abs/2611.08070) · *Nazmus Sakib Ahmed, 2026*. Permuting CIFAR-10 labels preserved a numerical split the reader could detect in the output layer, but the reader assigned the wrong meanings to the class pairs.
- [Mixed Signals: Weight-Space Programming for EEG and ECG](https://arxiv.org/abs/2611.13758) · *Dara Varam et al., 2026*. Agents repaired planted faults in EEG and ECG networks, yet could not reliably identify a network’s task from its weights alone.

## Editing checkpoints

- [Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations](https://arxiv.org/abs/2611.09382) · *Junru Hu et al., 2026*. Six of 16 searches retained the original checkpoint, and edits that helped on the target task transferred unevenly to other benchmarks. [Code](https://github.com/WSP-Scope/WSP-Scope-Project)

- [WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming](https://arxiv.org/abs/2611.25476) · *Bo Li et al., 2026*. Rerunning a weight-editing program on independently trained vision models tests whether its procedure transfers beyond the checkpoint on which it was written. [Code](https://github.com/Gen-Verse/WeightCode)

- [Language Models Can Rewrite Their Own Weights](https://arxiv.org/abs/2611.21885) · *Jiajun Fan et al., 2026*. A 27B model evaluated its own edits on practice problems, and the authors used held-out problems and a damaged copy to test improvement and repair.

## Writing networks

- [Looped Weight-Space Programming: LLM-Written Transformers for Long Algorithmic Reasoning](https://mbzuai-oryx.github.io/LoopedWSP/) · *Abdelrahman Elsayed et al., 2026*. The released weights let readers trace how repeated applications of a single transformer block advance a maze search. [Code and weights](https://github.com/mbzuai-oryx/LoopedWSP)

- [Interpretable weight-space programming builds transparent transformers and brain encoding models](https://arxiv.org/abs/2611.18114) · *Yash Mehta et al., 2026*. A fresh agent rebuilt models from descriptions of at most 200 words, giving the authors a behavioral test of how well a written model could be explained. [Code, prompts and logs](https://github.com/csinva/weight-space-programming-autoresearch)

- [Weight-Space Programming Doesn't Need Transformers](https://arxiv.org/abs/2611.22055) · *Hyunjong Ok and Jaeho Lee, 2026*. When allowed to choose the architecture for science-question answering, the writers produced sparse lookup models that the authors compared on accuracy, size and inference time. [Code and models](https://github.com/effl-lab/Weight-Space-Programming)

- [Zero-Shot Weight-Space Programming for Prediction and Classification of Target Variables in Structured Datasets](https://arxiv.org/abs/2611.19292) · *Eduardo C. Garrido-Merchán, 2026*. With a labeled table and no execution feedback, the writer must both infer a prediction rule and express it as literal weights and biases.

- [Physics2Weight: Direct Neural Network Architecture and Weight Generation from Physical Laws Using Large Language Models](https://arxiv.org/abs/2611.12954) · *Shogo Sato et al., 2026*. Across four PDEs, comparing solution error with the residual in the governing equation reveals where an accurate-looking approximation violates a physical constraint.

## Benchmarks

- [WeightBench: Evaluating Language Models as Weight-Space Programmers](https://arxiv.org/abs/2611.18553) · *Aayush Marasini et al., 2026*. The five tracks cover 42 tasks, so the per-track scores and attempted-task counts matter when comparing agents. [Task registry and harness](https://github.com/Aayush-Marasini/WeightBench)
- [IWIBench: Evaluating Gradient-Free Model Driven Intra-weight Injection](https://arxiv.org/abs/2611.08647) · *Chris von Csefalvay et al., 2026*. A separate validator reapplies each candidate edit and tests both the requested behavior and preservation of other capabilities across ten text-editing objectives.

When comparing results, check what the programmer could see before submission. Writing weights once from a task description, revising them against validation scores, and inspecting a running checkpoint give the programmer different amounts of information. For an edit, look for both a held-out test of the new behavior and a test of what the original network could already do.

## Replications and controls

- [Replicating and Extending Weight-Space Programming: Frontier LLMs Compile Programs into Weights and Read Input Layers](https://arxiv.org/abs/2611.21449v1) · *Roksana Goworek et al., 2026*. Readers recovered board layout more reliably than game rules on three new games, while reconstructed Python programs reproduced the tested actions of a written Breakout network.

- [Same Fix, Different Weights: Replicating Weight-Space Programming with Claude](https://arxiv.org/abs/2611.20953v1) · *Subham Kundu, 2026*. Claude reduced looping in Qwen through output-layer changes, reproducing a behavioral gain that the original study reached through an internal edit. [Repository](https://github.com/Cenrax/weight-space-programming-claude)

- [Weight Space Programming for Vision Language Model Repair](https://arxiv.org/abs/2611.23615v1) · *Avinash Goutham Aluguvelly, 2026*. Rounding corrupted weights back to their original precision preserved the tested answers but removed the clue that had enabled exact unaided repair.

- [Computation, not weight access: large language models as auditors of clinical prediction networks](https://arxiv.org/abs/2611.07847v1) · *Zhiyu Liu and Xinyu Yang, 2026*. On the simulated clinical networks tested, an agent with a calculation tool matched white-box auditing using only the networks’ predictions. [Repository](https://github.com/Chth1z/llm-clinical-network-audit)

- [Self-WSP: Can Language Models Improve Themselves Through Weight-Space Programming?](https://arxiv.org/abs/2611.28833v1) · *Guoming Ling et al., 2026*. Some self-edits improved held-out math accuracy, but random search sometimes reached comparable results.

- [Do We Really Need an LLM for Weight-Space Programming? A Deterministic Forward-Only Paradigm and Its Capability Boundaries](https://arxiv.org/abs/2611.34612v1) · *Lin Yao, 2026*. Giving a deterministic router and a 27B language model the same editing operators isolates the contribution of operator selection.

## Editing language and vision models

- [Can a Frontier LLM Repair a Quantized Network by Tool-Free Weight-Space Programming?](https://arxiv.org/abs/2611.33031v1) · *Steffen Urban, 2026*. Given the original CNN and its rounded copy, Opus recovered CIFAR-10 accuracy from 60.4% to 77.95% when allowed one answer per layer. [Repository](https://github.com/urbste/weight-space-programming-ptq)

- [TowerBridge: Bridging the Dual-Encoder Modality Gap via Weight-Space Programming](https://arxiv.org/abs/2611.31233v1) · *Hani Alomari et al., 2026*. A correction distilled from repeated projection edits was tested on eight additional CLIP checkpoints that the agent had never edited.

- [Keel: A Frontier Model Teaches a Vision-Language Model by Rewriting Its Weights](https://arxiv.org/abs/2611.25257v1) · *Jiajun Fan et al., 2026*. Across six image benchmarks, the authors measured both repeated reasoning and answer accuracy after editing small Qwen vision-language models.

- [Weight-Space Programming Writes In-Context Learning and Matches Fine-Tuning in Language Models](https://arxiv.org/abs/2611.26841v1) · *Konstantinos Skianis and Aristidis Likas, 2026*. Across six tasks, reworded prompts and unfinished editing runs qualified the comparison between example-driven weight edits and fine-tuning. [Repository](https://github.com/y3nk0/weight-space-programming-study)

- [Writing Weights or Training Them? Spatial Reasoning through Weight-Space Programming and Low-Rank Adaptation](https://arxiv.org/abs/2611.27089v1) · *Yalin Yang et al., 2026*. A trained rank-one adapter made larger gains than the published Qwen patch on the target spatial tasks, but lost accuracy on neighboring distance tasks.

- [What Does Weight-Space Programming Add to Diffusion Editing? Program Construction versus Score-Guided Refinement](https://arxiv.org/abs/2611.22228v1) · *Zitian Gao et al., 2026*. The preregistered rewrite showed no advantage over a strong baseline, and an exploratory revision improved a CLIP metric while whole-image joint success fell.

- [Training Vision Models for LLM-Driven Weight-Space Programming](https://arxiv.org/abs/2611.26408v1) · *Timo Ropinski and Sebastian Kranz, 2026*. More than 2,600 edits to vision models let the authors measure how target-model training affects later edit success, side effects and held-out accuracy. [Project](https://viscom.uni-ulm.de/wsp)

- [Reparameterizing Your Object Detectors for Weight Space Programming](https://arxiv.org/abs/2611.29882v1) · *Chien-Yao Wang, 2026*. Expanding and folding detector layers tests how the choice of parameterization affects edits across 17 detectors, including settings that preserve inference cost. [Repository](https://github.com/WongKinYiu/ODWSP)

## Control, games and verification

- [Weight-space programming for tractor guidance controller: large language models natively write neural network weights that steer a real tractor](https://arxiv.org/abs/2611.21958v1) · *Timo Oksanen, 2026*. After simulation-guided editing, the 253-parameter controllers steered a real tractor with tracking errors of the same order as classical pure pursuit.

- [Sparks of Weight-Space Programming for Robot Foundation Models](https://arxiv.org/abs/2611.31715v1) · *Kyle Coelho and Eugen Solowjow, 2026*. Reversed and random edits serve as controls for targeted repairs of recurring stuck states in a simulated robot policy.

- [Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games](https://arxiv.org/abs/2611.16981v1) · *Jens Lehmann, 2026*. Given simulator source, the strongest fixed-network writer solved 56% of held-out levels with feedback, compared with 97–100% for the four main writers’ Python players. [Repository](https://github.com/JensLehmann/weight-space-programming-games)

- [Weight-Space Programming of Policies and Their Verification via Model Checking](https://arxiv.org/abs/2611.11604v1) · *Dennis Gross, 2026*. One repair improved action accuracy while breaking a formal requirement, and feedback from the model checker let the editor restore it. [Repository](https://github.com/LAVA-LAB/COOL-MC/tree/wsp_verified)

## Scientific models and decision systems

- [Weights & Caches: LLMs Can Program Tabular Foundation Models](https://arxiv.org/abs/2611.20174v1) · *Shi Bin Hoo et al., 2026*. The authors construct a tabular model from zero weights, repair a regression failure, and separately test inference-cache edits that leave parameters unchanged.

- [Weight-Space Programming for Medical Imaging: Do We Still Need Training Data?](https://arxiv.org/abs/2611.12066v1) · *Maximilian Lindholz et al., 2026*. Both writers produced above-chance classifiers without seeing images, but fitting the same architecture to 256 labeled images yielded higher AUC on all six MedMNIST tasks. [Repository](https://github.com/MaximilianLindholz/weight-space-programming-medical)

- [Weight-space programming and mechanistic interpretability for model editing in particle physics](https://arxiv.org/abs/2611.27079v1) · *Raphaël Bonnet-Guerrini et al., 2026*. The authors test whether edits that repair sensitivity to a soft neutral particle also generalize to signal classes outside the editing task. [Repository](https://github.com/rbonnetguerrini/WSP-mech-interp-for-model-editing-in-particle-physics)

- [Can a Language Model Write the Weights? An Empirical Study of LLM-Written Scoring Networks for Column Generation and MILP Branching, with a Bus-Driver Scheduling Application](https://arxiv.org/abs/2611.09559v1) · *Renan Butkeraites, 2026*. On held-out Atlanta crew schedules, an LLM-written branching rule beat the solver default but matched a standard pseudocost rule. [Repository](https://github.com/butkeraites/llm-written-weights-or)

- [Fine-Tuning Without Gradients? Closed-Form, LLM-Written Classifiers on a Frozen Encoder](https://arxiv.org/abs/2611.33972v1) · *Md Nasir Uddin et al., 2026*. Evaluating the closed-form classifier heads on six held-out datasets qualified the stronger comparison with fine-tuning on the eleven development datasets.

- [WeightLoop: Weight-Space Programming with Experimental Feedback](https://arxiv.org/abs/2611.07319v1) · *Mengran Li et al., 2026*. Offline replay tests whether a reusable editing program can turn successive measurements into persistent changes that improve the ranking of future candidates.

## Foundations

- [Tracr: Compiled Transformers as a Laboratory for Interpretability](https://deepmind.google/research/publications/22295/) · *David Lindner et al., 2023*. Compiling a known RASP program into transformer weights gives a reference computation against which to test interpretability methods. [Compiler](https://github.com/google-deepmind/tracr)
- [AdderBoard: A Community Challenge for Tiny Arithmetic Transformers](https://github.com/anadim/AdderBoard) · *Dimitris Papailiopoulos, 2026*. The verifier lets readers compare weight constructions for the same task of adding two ten-digit integers.
