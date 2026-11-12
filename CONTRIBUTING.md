# Contributing

Thanks for helping make text great again. Believe me, it's appreciated.

## What we welcome

- **New Before/After examples** in Japanese or English (`examples/`). Include `Input`, `Mode`, and `Output`. Run the same input a few times and submit an output whose features are stable, not a lucky one-off.
- **Style improvements** to `SKILL.md` or `references/style-guide.md`: better rhythm, funnier phrase banks, clearer mode separation.
- **New test cases** in `tests/cases.md`, especially inputs that trip the skill up.
- **Translations** of the README.
- Bug reports: an input, the mode, what you got, and what you expected.

## Ground rules

Every contribution must keep these properties. PRs that break them will not be merged.

1. **Facts stay put.** Numbers, dates, people, outcomes, medical effects, market moves and quotations in the input must survive unchanged in the output.
2. **No factual claims about real people.** The standing foils (Biden as "Sleepy Joe", the Fake News, the Radical Left and the rest of the roster in `references/style-guide.md`, section F) may only be compared unfavorably on, or blamed for, the trivial subject of the text. No crimes, corruption, health claims, family members, invented quotes, or epithets other than "Sleepy" for a real person. Do not add names to the roster.
3. **Parody, not impersonation.** Nothing that passes itself off as a genuine post or statement.
4. **Good-natured.** No slurs, no harassment, nothing harmful if read literally.
5. **Stay script-free.** The skill is plain Markdown. Don't add runtime dependencies, API calls or build steps to `SKILL.md`.

## Before you open a PR

- Run the validator:
  ```bash
  pip install skills-ref
  agentskills validate /path/to/make-text-great-again
  ```
- If you changed `SKILL.md` or the style guide, re-run the cases in `tests/cases.md` and update `tests/results.md`.
- Keep `SKILL.md` under 500 lines. Move detail into `references/`.
- Keep `name` in the frontmatter equal to the directory name (`make-text-great-again`).

## Issue labels

- `example request`: ask for a Before/After in a specific domain (cooking, dev, sports, ...).
- `good first issue`: small, self-contained, usually an example or a phrase bank entry.
- `style`: changes to how outputs read.
- `fidelity`: outputs that changed or invented facts, or broke the foil limits. Highest priority.

## License

By contributing you agree that your contribution is licensed under the MIT License in this repository.
