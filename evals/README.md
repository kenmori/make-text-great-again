# Evals

Cases for `claude plugin eval`. Each case is a prompt a user might type, run once
with the skill loaded and once without, and scored by the graders in its folder
(regular expressions, and pass/fail rubrics judged by a model, best of three).

```bash
claude plugin eval . --no-publish --threshold 0.8 --judge-model sonnet -j 4
```

Add `--case 'unseen-*'` to run only the cases that have never been used to tune the skill. Results are written to
`evals/results/`, which is not committed; the latest summary is in
[`tests/results.md`](../tests/results.md).

**Reading the scores.** The rubric called `in-style` asks for patterns from this
skill's own list, so a plain prompt fails it more or less by construction. It
checks that the repertoire is used, not that the output is funnier. Cases
are added in rounds. The first set was used to find and fix problems. The
`round2-*` cases were run once, exposed four more, and were then used to fix them,
so they no longer count as held out. The `fresh-*` cases were run once, scored
0.53 with the skill against 0.41 without, and were then used to fix the rules, so
they are used up as well. The `unseen-*` cases were written after that and have
not been used for tuning; they are the honest signal until they, too, are used up. All of this is a model
judging a model on two runs per case. It finds problems; it does not prove quality.
