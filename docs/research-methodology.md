# Research Methodology

> **Version 4.0.0 candidate · Unreleased · Last verified 2026-09-01**

This page describes the public research policy at a high level. It does not
publish strategy logic, datasets, thresholds, trial counts, or results.

## CURRENT — rule-based primary research

Primary signal generation is rule-based. A research hypothesis must define a
mechanism, inputs, decision rules, failure conditions, and evaluation path
before it can be treated as a candidate for testing.

Machine learning is not used as a primary signal generator.

## CURRENT — conditional auxiliary machine learning

Machine learning may be considered only for auxiliary roles such as:

- meta-labeling;
- dynamic position sizing;
- regime detection.

An auxiliary ML component is eligible for research only after the corresponding
hard-rule baseline has qualified out of sample. It must then be evaluated as a
separate, trial-accounted hypothesis against that baseline.

This policy prevents a flexible model from replacing an unproven economic
mechanism.

## CURRENT — bounded synthetic engine evidence

A bounded execution-engine contract is qualified on deterministic synthetic
fixtures only. It has not processed market data and does not qualify a strategy,
an economic result, paper execution, live execution, or deployment.

The contract is deliberately narrower than the programme research scope. It
does not establish coverage of the programme research universe or design
horizon.

## CURRENT — route-specific anti-overfit design

The research design uses:

- temporal separation across development, validation, holdout, and forward
  partitions;
- hypothesis pre-registration before governed out-of-sample evaluation;
- purged, embargoed, anchored walk-forward evaluation and Deflated Sharpe Ratio
  (DSR) on the current synthetic engine route;
- Combinatorial Purged Cross-Validation (CPCV) and Probability of Backtest
  Overfitting (PBO) as programme methods only where applicable;
- cumulative trial accounting;
- sanity checks and reproducibility controls, including deterministic artefacts
  and checks before a result can be interpreted.

CPCV and PBO are not claimed for the current synthetic engine route. Their use
depends on an evaluation geometry for which they are applicable.

These methods reduce avoidable overfitting risk. They do not guarantee that a
strategy has economic value or will perform in the future.

## CURRENT — separation of claims

Research records distinguish:

- verified facts;
- research judgment;
- unknowns;
- target capabilities.

A failed or inconclusive research result is not rewritten as success. A target
architecture is not evidence of current operation.

## IN PROGRESS — stronger research controls

Controls around research access, trial accounting, failure handling, and
independent audit evidence are being strengthened.

The public implication is intentionally narrow: no current strategy result is
presented here as a deployment qualification or a current performance claim.

## TARGET — qualification before deployment

A future deployment candidate would need to pass, in order:

1. frozen research and evaluation rules;
2. statistical and reproducibility checks;
3. synthetic execution and accounting checks;
4. paper-trading review;
5. an explicit human decision to proceed.

Passing one stage would not imply that later stages are complete.

## What remains private

The following remain private:

- strategy identities, parameters, and feature definitions;
- temporal split dates and dataset identifiers;
- trial budgets, counters, and statistical thresholds;
- research outcomes and performance measurements;
- audit evidence, internal reviews, and qualification packs.

---

*Disuza Quantitative — Public Technical Reference · Version 4.0.0 candidate ·
Unreleased · Last verified 2026-09-01*
