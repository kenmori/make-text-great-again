# Sources

Reference material used to describe the parody style, with access status as of the
date shown. These are style references only; nothing here is reproduced in the skill.

| Resource | URL | Purpose | Checked | Status |
|---|---|---|---|---|
| Agent Skills specification (site) | https://agentskills.io/specification | Frontmatter and directory rules | 2026-11-12 | Not reachable from the build environment (network policy). Used the GitHub copy below instead. |
| Agent Skills specification (GitHub source) | https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx | Same, raw file fetched via raw.githubusercontent.com | 2026-11-12 | Fetched and read. Frontmatter rules confirmed: `name` 1–64 chars, lowercase alphanumerics and hyphens, must match directory; `description` ≤ 1024 chars; optional `license`, `compatibility` (≤ 500), `metadata` (string→string), `allowed-tools`. |
| `skills-ref` validator | https://github.com/agentskills/agentskills/tree/main/skills-ref | Validation tool (`pip install skills-ref`, CLI `agentskills validate <dir>`) | 2026-11-12 | Installed and run; this skill validates. |
| Claude Code Skills docs | https://code.claude.com/docs/en/skills | Install paths, `$ARGUMENTS`, Claude Code-specific frontmatter | 2026-11-12 | Fetched and read. Personal skills: `~/.claude/skills/<name>/SKILL.md`; project skills: `.claude/skills/<name>/SKILL.md`. |
| Clarke & Grieve (2019), "Stylistic variation on the Donald Trump Twitter account" (PLOS ONE, via PMC) | https://pmc.ncbi.nlm.nih.gov/articles/PMC6760825/ | Linguistic analysis of posting style | 2026-11-12 | Not reachable from the build environment (network policy). Cited from the original plan; verify before linking in release notes. |
| Ahmadian, Azarshahi & Paulhus / related rhetoric studies on Trump speeches (Journal of Quantitative Linguistics) | https://www.tandfonline.com/doi/abs/10.1080/09296174.2017.1349358 | Rhetorical features of speeches | 2026-11-12 | Not reachable from the build environment (network policy). Cited from the original plan; verify authorship and title before citing publicly. |
| Official X account | https://x.com/realDonaldTrump | Primary public material (style observation only) | 2026-11-12 | Reachable (HTTP 200). Login may be required to read posts. Not scraped; no posts reproduced. |

## Notes

- The style descriptions in `style-guide.md` are our own paraphrase of widely
  observed public patterns: short sentences, superlatives, repetition, in-group /
  out-group comparison, one-word capitalized verdicts, and the sign-off
  "Thank you for your attention to this matter!".
- This project is an unofficial parody. It is not affiliated with, endorsed by, or
  representative of Donald Trump or any organization.
