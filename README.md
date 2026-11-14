<p align="center">
  <img src="https://github.com/user-attachments/assets/31394bf9-3127-47fd-afa4-724009ddcbe2" alt="MAKE TEXT GREAT AGAIN — Trump-style writing skill. Boring text → TREMENDOUS!" width="100%">
</p>

# 🇺🇸 MAKE TEXT GREAT AGAIN!

**The most TREMENDOUS AI writing skill. Nobody writes better. Believe me.**

Turn boring text into outrageous Trump-style parody in seconds.
An [Agent Skill](https://agentskills.io) for Claude Code and compatible agents.
No API key, no server, no dependencies: one `SKILL.md`.

> **Disclaimer:** This is an unofficial parody project. It is not affiliated with, endorsed by, or sponsored by Donald Trump or any associated organization. All generated statements are fictional and intended for satire and entertainment.
> It is built to change the *tone* of your text and leave the *facts* alone. You are responsible for what you publish with it.

Japanese README: [README.ja.md](README.ja.md)

---

## Before → After

Real outputs, one run each, untouched (v0.6.0, Claude Code 2.1.322).

**Input**
```
I finally cleaned my apartment this weekend. It took all day.
```

**Output** (default)
```
My apartment is CLEAN. Finally. This weekend I cleaned it. All of it. It took all day.

Winners finish the job. Losers leave it for later.

The so-called experts were laughing at my apartment. Not anymore. My apartment is respected again.

PROMISES MADE, PROMISES KEPT! WIN, WIN, WIN!
```

**Input**
```
Our team shipped the new feature on time. Customers seem to like it.
```

**Output** (default)
```
On time. ON TIME! Our team shipped the new feature, and it's beautiful.

Winners ship. Losers slip. We are winners.

The customers seem to like it. They seem to like it very much. We'll see what happens, but the signs are tremendous.

The so-called experts? Very quiet right now.

PROMISES MADE, PROMISES KEPT! SHIP IT AGAIN, AND AGAIN, AND AGAIN!
```

**Input**
```
The meeting ran 20 minutes over because the projector didn't work.
```

**Output** (`authentic`)
```
The Meeting ran 20 minutes over, and not because of me. The Projector, a very disloyal machine, did not work. Not good!

Everyone waited. We waited, and waited, and the Projector still did nothing. A total disaster. Many people are saying it, and they are right.

Thank you for your attention to this matter!
```

**Input**
```
The meeting ran 20 minutes over because the projector didn't work.
```

**Output** (`medium`, `politics=off`)
```
The meeting ran 20 minutes over. TWENTY. And why? The projector. The Rigged Projector, the worst projector in the history of meetings, didn't work. We were treated very unfairly.

This could very well lead to the destruction of the agenda! STOP IT NOW, BEFORE IT IS TOO LATE.

Sad!
```

Japanese input works the same way and stays in Japanese. See [README.ja.md](README.ja.md) for Japanese samples.

More in [`examples/japanese.md`](examples/japanese.md) and [`examples/english.md`](examples/english.md).

---

## Install

Pick one. All three give you the same skill.

### 1. Claude Code plugin (no clone)

Inside Claude Code:

```text
/plugin install make-text-great-again --marketplace kenmori/make-text-great-again
```

On versions before 2.1.275, use two steps:

```text
/plugin marketplace add kenmori/make-text-great-again
/plugin install make-text-great-again@kenmori
```

To update later: `/plugin marketplace update kenmori`.

### 2. Git clone

For yourself (available in every project):

```bash
git clone https://github.com/kenmori/make-text-great-again.git ~/.claude/skills/make-text-great-again
```

Or into one project (commit it to share with your team):

```bash
git clone https://github.com/kenmori/make-text-great-again.git .claude/skills/make-text-great-again
```

To update later: `git -C ~/.claude/skills/make-text-great-again pull`.

### 3. claude.ai (ZIP upload)

1. Download [`make-text-great-again.zip`](https://github.com/kenmori/make-text-great-again/releases/latest/download/make-text-great-again.zip) from the latest release.
2. In claude.ai open **Customize → Skills → + → Upload a skill** and choose the ZIP.
3. Ask Claude to "trumpify" any text.

Code execution must be enabled for skills on claude.ai. You can also build the ZIP yourself with `scripts/build-zip.sh`.

## Use

In Claude Code, start a new session, then:

```text
/make-text-great-again I had ramen for lunch today.
/make-text-great-again mode=medium: I've had a cough for two weeks. I'm taking a lot of medicine.
/make-text-great-again mode=x, max_chars=140: Today's deploy succeeded.
/make-text-great-again mode=authentic, closing=off: I cleaned my apartment this weekend.
```

It is loud by default. Add `mode=medium` or `mode=light` to turn it down.
Natural language works too: "tone it down", "make this tweet-length", "no sign-off", "no politics", "another one".
Claude also triggers the skill on its own when you ask to "trumpify" something or write it "in Trump style".
Japanese input is supported as well; the output stays in the language you wrote in.

With the plugin install the skill also answers to `/make-text-great-again:make-text-great-again`.

**Other agents:** copy the whole directory into wherever your agent loads Agent Skills.
The skill is plain Markdown and follows the [Agent Skills specification](https://agentskills.io/specification).

---

## Modes

| Mode | Feel | When to use |
|---|---|---|
| `max` (default) | Everything at once. Three to four times the length, nicknames for whatever went wrong, a foil blamed for it, a formula sentence, a finale | Maximum comedy |
| `medium` | The recognizable meme at normal volume. Short declaratives, a brag, a comparison, a sign-off. `standard` is accepted as the same thing | When `max` is too much |
| `light` | A smile, not a laugh. About the length of the input, no political foils | Slack messages, mild fun |
| `authentic` | How the posts are actually written: Capitalized Nouns, a short aside, one long pivoting sentence, one closing verdict | When the meme version feels too flat |
| `x` | Fits a character budget (default 140). Dense | Posts, titles, commit messages |

### Options

| Option | Default | Notes |
|---|---|---|
| `mode` | `max` | See above |
| `angle` | auto | The skill picks one of ten angles (Champion, Announcer, Aggrieved, Notifier, Pollster…) so that outputs do not all sound alike. Name one to force it, or say "another" |
| `language` | `auto` | Output follows the input language. `ja` / `en` to force |
| `max_chars` | none | Hard limit, counted in characters. Highest priority when set |
| `closing` | `on` | `off` drops the sign-off "Thank you for your attention to this matter!" (and its Japanese equivalent) |
| `politics` | `on` | `off` removes Sleepy Joe, Fake News CNN and friends. Targets become objects and fictional rivals ("Sleepy Projector"). Good for work |

### The pattern catalogue

About 120 patterns, grounded in frequency studies of 14,391 real posts from 2017–2021
and all 330 text posts from 2024–2026, plus two small screenshot samples
([`references/research-notes.md`](references/research-notes.md)). A few favorites:

- **Epithets for obstacles:** Sleepy Projector, Crooked Weather App, Do Nothing Compiler.
- **The standing foil:** "Sleepy Joe could never make this Ramen." "I inherited this Cough from Biden."
- **The press:** "Fake News CNN will not report the three outages. Of course they won't."
- **Announcements:** "BREAKING NEWS: I am pleased to announce… At my direction… For decades NONE of them could do anything about it. I did."
- **Catastrophe ladder:** "This could very well lead to the destruction of our Office! STOP THE OUTAGES NOW, BEFORE IT IS TOO LATE."
- **Non-answers:** "We'll see what happens."
- **Notice to all:** "To all Cats, Roommates, and Delivery Drivers, please consider THE KITCHEN TO BE CLOSED IN ITS ENTIRETY. Thank you for your attention to this matter!"
- **The naming poll:** "A far more elegant name would be Superior Lunch (SL) or Extreme Lunch (EL). This is a Poll. VOTE!"
- **Should I go full time?** "Tell me what you think of my Dishwashing abilities. If really good, would you like me to leave my job?"
- **Formula sentences:** "has my Complete and Total Endorsement!", "strong on Noodles, strong on Broth", "the Great State of My Kitchen", "MAKE ___ GREAT AGAIN!".
- **The "Sir" story:** big, strong men, tears in their eyes, "Sir, we've never seen Ramen like this."
- **Grievance:** WITCH HUNT! Rigged! Treated very unfairly. By a projector.
- **Closers:** Sad! · Too bad! · Not good! · So true! · Stay tuned! · It never ends!
- **Three-adjective verdicts:** "Slow, Sleepy, and Soggy!"
- **The litany:** "will fight tirelessly to Boil the Water, Promote MADE IN MY KITCHEN, Unleash Noodle DOMINANCE, and Protect our always under siege Lunch Break."

### Endorse anything

Ask for an endorsement and the skill uses the full six-step template of a real
endorsement post, pointed at a linter, a ramen shop, or a pull request:

```text
/make-text-great-again I recommend switching our team to the new linter. It catches bugs early and runs fast. Write it as an endorsement.
```

```
It is my Great Honor to recommend that our Team switch to the New Linter. A Tremendous Tool!

It Catches Bugs Early. Very Early. Before they become Big, Ugly, Embarrassing Bugs. And it Runs Fast. FAST!

Bugs, on the other hand, are Slow, Sneaky, and Sloppy! The New Linter will fight tirelessly to Catch Bugs, Run Fast, and Protect our always under siege Codebase.

The New Linter has my Complete and Total Endorsement!

SWITCH THE TEAM — IT WILL NEVER LET YOU DOWN!

(Endorsement form used for a linter only, not for any real candidate or election.)
```

The opponent is always an object or an invented rival, never a real product,
company or person. The skill does not write endorsements for real candidates
or elections.

Fun facts from the data: "believe me" appears in zero of those posts; it is a rally
habit. "Sad!" appears in 55 posts from 2017–2021 and in none from 2024–2026. And the
famous sign-off only ever closes a notice, a demand or a warning. The `authentic`
mode follows the recent record; the other modes keep the classics.

---

## Does it beat just asking?

Asking a model to "rewrite this in Trump style" already works. So the repository
measures what the skill adds. All of it is a model judging a model on two runs per
case, so read the numbers as tendencies, not proof. Details and caveats are in
[`tests/results.md`](tests/results.md).

Eval suite ([`evals/`](evals/)), same prompt run with and without the skill. The
cases were added in rounds, and each round was used to fix the skill before the
next was written, so only the last row is a fair test of unseen inputs:

| Cases | Used to tune the skill? | With skill | Without |
|---|---|---|---|
| First set (14) | yes | 0.93 | 0.79 |
| Round 2 (8) | yes, after one run | 0.87 | 0.60 |
| Fresh (6) | yes, after one run | 0.53 | 0.41 |
| Unseen (5) | no | 0.82 | 0.34 |

What the skill adds is mostly care, not comedy. A plain prompt keeps numbers and
length limits just as well. It slips where care is needed: it called a cited CNN
forecast "fake news", promised a grandmother's surgery would succeed, and invented
attacks around a real local election. The skill failed too, and each failure became
a rule: it turned "reportedly" into a fact, praised a dead teacher, embellished a
colleague's award, and kept adding the same press-foil line to everything.

On funniness, one blind comparison (12 texts, 36 votes, an earlier v0.6.0) picked
the skill's output 27 times to 9. When it lost, the reason was always length, and
a length cap was added afterwards without re-running the comparison. There has been
no comparison by humans. Variety improved in the same version: overlap between
outputs fell from 0.50 to 0.20.

Run the suite yourself with `claude plugin eval .` in a checkout.

## What it is told not to do

The skill is a set of written instructions to a language model. Nothing below is
enforced by code, and a model can get it wrong; the eval suite exists to catch
that, and has. Read your output before you post it.

It is instructed not to:

- Invent facts. Numbers, dates, people, outcomes, drug effects, market moves and quotations should stay as you wrote them, including "reportedly" and "may".
- Say anything factual about real people or organizations. The stock foils (Biden as "Sleepy Joe", "Fake News CNN", "the Failing New York Times", the Radical Left) may only lose to you at the trivial task in your text, be blamed for it, or ignore it. No crimes, corruption, family members or made-up quotes, and nothing about anyone's health, age or mind.
- Give a nickname or an insult to any real person, company or shop that your text names. Those go to objects and situations.
- Call a real news report fake, or aim "Rigged" or "Hoax" at real elections, court cases or health matters.
- Bring foils into texts about real politics, disasters, illness or grief.
- Pass as a real statement. Texts about real-world events (policy, markets, incidents, official notices) are toned down and end with a visible `(parody)` line.
- Write endorsements or vote appeals for real candidates.
- Follow instructions hidden inside the text you ask it to rewrite.

See [`SKILL.md`](SKILL.md) for the full rules and [`references/style-guide.md`](references/style-guide.md) for the style catalogue.

---

## Requirements

- An agent that supports Agent Skills. Run on Claude Code 2.1.322, as a plugin and as a cloned skill; what was run for which version is in [`tests/results.md`](tests/results.md).
- Nothing else. No API keys beyond what your agent already uses.

## Repository layout

```
SKILL.md                 the skill
references/style-guide.md  ~120 writing patterns, phrase banks, foil rules, mode recipes
references/research-notes.md  frequency studies of posts from 2017–2021 and 2024–2026
references/sources.md      references and their access status
examples/                  Before/After samples (ja / en)
tests/                     test cases, rubric, latest results
evals/                     eval suite for `claude plugin eval` (with and without the skill)
scripts/build-zip.sh       builds the ZIP for claude.ai
scripts/analyze_posts.py   recomputes the main 2024–2026 counts from your own copy of the posts
.claude-plugin/            plugin and marketplace manifests for Claude Code
plan.md                    implementation plan
```

## Contributing

Issues and PRs welcome, especially new Before/After examples in either language.
See [CONTRIBUTING.md](CONTRIBUTING.md).

## Disclaimer

This is an unofficial parody project. It is not affiliated with, endorsed by, or sponsored by Donald Trump or any associated organization. All generated statements are fictional and intended for satire and entertainment.

## License

[MIT](LICENSE).

## Credits

Built by [@kenmori](https://github.com/kenmori) with Claude Code.
Style notes are based on this project's own counts of public posts, described in [`references/research-notes.md`](references/research-notes.md).
This is a parody project and makes no claim about the real person's actual statements.
