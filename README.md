# AI Lab 1 — Introduction to AI & Paradigms

**Week:** 1  
**Subject:** Artificial Intelligence Lab

## Overview
This repository contains the work completed for AI Lab 1, covering AI history, rule-based decision-making, and the limitations of conversational intelligence tests.

## Task 1: AI History Timeline
A chronological timeline of important AI milestones:
- **1950:** Alan Turing proposes the imitation game.
- **1956:** Dartmouth workshop helps establish AI as a research field.
- **1974–1980:** First AI winter.
- **1980s:** Expert systems become prominent.
- **2012:** Deep learning achieves a major image-recognition breakthrough.
- **2017:** Transformer architecture is introduced.
- **2022:** ChatGPT launches publicly.

The report explains the significance of each milestone and includes source links.

## Task 2: Rule-Based Scholarship Checker
**Python file:** `lab1_task2_rule_based.py`

The program uses four explicit conditions:
1. Score is at least 70.
2. Required documents are complete.
3. Income eligibility is satisfied.
4. Enrollment is verified.

It returns `Review` when all conditions pass and `Hold` otherwise.

**Note:** The threshold and added conditions are synthetic lab assumptions, not official scholarship policy. Review means human review, not automatic approval.

### Four test cases
- All conditions pass → Review
- Income eligibility fails → Hold
- Enrollment verification fails → Hold
- Score equals 70 and other conditions pass → Review

The program prints each case's inputs, expected result, actual result, pass status, and reason.

### How to run
```bash
python lab1_task2_rule_based.py
```

On Windows, you can also try:
```bash
py lab1_task2_rule_based.py
```

## Task 3: Conversational Test vs. General Intelligence
The written report explains what the Turing Test observes, why conversational success does not prove general intelligence, and an example of fluent but incorrect scholarship reasoning. It also proposes testing the checker against known expected outcomes and edge cases.

## Suggested repository files
- `README.md`
- `lab1_task2_rule_based.py`
- Word report for Task 1
- Word report for Task 2
- Written report for Task 3

Use the actual filenames of your saved reports.

## References
1. Turing, A. M. (1950). “Computing Machinery and Intelligence.” https://doi.org/10.1093/mind/LIX.236.433
2. Stanford Encyclopedia of Philosophy — The Turing Test: https://plato.stanford.edu/entries/turing-test/
3. IBM — History of Artificial Intelligence: https://www.ibm.com/think/topics/history-of-artificial-intelligence
4. Vaswani et al. (2017). “Attention Is All You Need.” https://arxiv.org/abs/1706.03762

---
This repository is prepared for educational lab work. Please verify your instructor's submission requirements before submitting.
