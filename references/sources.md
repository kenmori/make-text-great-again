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
| Complete Donald Trump Tweets Archive (MarkHershey, GitHub) | https://github.com/MarkHershey/CompleteTrumpTweetsArchive | Corpus for the frequency study in `research-notes.md`: 23,075 posts from 2017-01-20 to 2021-01-08, of which 14,391 are original (non-retweet) posts | 2026-11-12 | Fetched (`data/realDonaldTrump_in_office.csv`) and analyzed. Only aggregate counts and short recurring phrases are used; the data itself is not redistributed here. |
| Official X API, full-archive search | https://api.x.com/2/tweets/search/all | Second corpus for `research-notes.md`: all 330 text-only, non-repost posts by the account from 2023-01-01 to 2026-11-13 | 2026-11-13 | Fetched once with the repository owner's API access and analyzed. Only counts and short recurring phrases are used; the posts are not redistributed. `scripts/analyze_posts.py` reproduces the counts from such a file. |
| Screenshots of 43 posts dated 2026-11-04 | (supplied by the repository owner; not redistributed) | Second sample for `research-notes.md`: the 2026 endorsement template | 2026-11-12 | All 43 read. Only the structure and short recurring phrases are described; no post is reproduced and the images are not in this repository. |
| Screenshots of 17 posts dated 2025-03-22 to 2025-06-26 | (supplied by the repository owner; not redistributed) | Third sample for `research-notes.md`: announcements, attacks on news outlets, decrees | 2026-11-12 | All 17 read. Only shapes and short recurring phrases are described; no post is reproduced and the images are not in this repository. |
| Official X account | https://x.com/realDonaldTrump | Primary public material (style observation only) | 2026-11-12 | The page shell loads (HTTP 200) but contains no posts: the timeline is rendered by scripts and requires a logged-in session, and an automated browser is refused. Not scraped; no posts reproduced. Later posts were read through the official API instead (row above). |

## Notes

- The style descriptions in `style-guide.md` are our own paraphrase, grounded in
  the counts in `research-notes.md`: short verdict closers, capitalized nouns,
  epithet + name pairs, formula sentences, history frames, and grievance words.
- Habits that postdate the corpus, such as the sign-off
  "Thank you for your attention to this matter!", come from general public
  observation and are marked as such in `research-notes.md`.
- This project is an unofficial parody. It is not affiliated with, endorsed by, or
  representative of Donald Trump or any organization.
