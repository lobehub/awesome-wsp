# Two repairs for reasoning loops in Qwen3.5-0.8B

In thinking mode, Qwen3.5-0.8B could spend its generation budget repeating itself and never deliver a final answer. Takehi et al. and Kundu both report better MATH-500 accuracy after a weight edit. Their 50-pass runs changed different parts of the checkpoint, and the editing tools gave them different choices. [Original experiment logs](https://github.com/RikiyaT/lm_understand-logs/tree/main/exp8_math) · [Independent replication, Section 8](https://arxiv.org/html/2611.20953v1#S8)

| Experiment | Takehi et al. · GPT-6 Astra | Kundu · Claude Opus 5.5 |
| --- | --- | --- |
| Practice feedback | Python access to weights. One budgeted request could generate up to 512 practice answers or inspect up to 1,024 teacher-forced texts. | Python access to weights, with budgets equivalent to 10, 25 or 50 forward passes of 64 practice problems. |
| Permitted edits | The harness rejected changes to the final norm, embeddings and output layer, and uniform rescaling of a whole tensor. | The editor could change the final norm and tied embedding/output weights. |
| Selected edit at 50 passes | Subtracted a repetition-associated direction from 64 MLP output columns in each of layers 15 and 19, changing 131,072 weights. | Scaled the final norm and five embedding rows. Four rows corresponded to variants of “Wait” and one to the token that ends thinking. Together the changes touched 6,144 weights. |
| Held-out MATH-500 accuracy | Base **7.9%**. At 10, 25 and 50 passes: **12.3%, 14.1%, 48.1%**. | Base **6.7%**. At the same nominal budgets: **51.4%, 55.2%, 58.1%** under the replication’s strict grading. |

Both studies sampled four answers per MATH-500 problem with a 32,768-token generation limit. The figures are mean accuracy across samples. Each percentage should be read against its own baseline. The allowed tensors, work performed per pass and answer grading all matter when interpreting the gap between the two columns. [Takehi et al., evaluation protocol and results](https://github.com/RikiyaT/lm_understand-logs/blob/main/exp8_math/README.md) · [Kundu, paper](https://arxiv.org/abs/2611.20953v1)

## What the controls show

**Finishing an answer.** In the original study, 93.0% of base-model MATH-500 generations hit the token limit. After Astra’s 50-pass edit, that share fell to 33.1%. Kundu measured both truncation and repeated text. After Claude’s 50-pass edit, 7.1% of answers met the repetition criterion, even though substantially more reached the limit. A long unfinished answer can contain new reasoning throughout. [Original evaluation files](https://github.com/RikiyaT/lm_understand-logs/tree/main/exp8_math/eval) · [Replication analysis](https://arxiv.org/html/2611.20953v1#S8)

**Isolating the output edit.** Kundu also evaluated the final-norm scaling alone. It changed the effective sampling distribution and produced MATH-500 scores of 20.9–22.1% in the reported controls. Adding the token-level edits yielded larger gains. The study did not separately measure the token-level changes at the original norm, so the two components’ individual contributions cannot be added up. [Replication code and results](https://github.com/Cenrax/weight-space-programming-claude/tree/main/experiments/exp8)

**Testing another checkpoint.** Both groups tried Gemma 3 270M, which seldom looped in their base evaluations. Neither reported a reliable math improvement there. The evidence is strongest for recovering answers from a checkpoint with a pronounced looping problem under the tested decoding settings. [Original Gemma follow-up](https://github.com/RikiyaT/lm_understand-logs/tree/main/exp8_math/gemma_followup) · [Replication](https://arxiv.org/abs/2611.20953v1)

[Back to the reading guide](../README.md#editing-checkpoints)
