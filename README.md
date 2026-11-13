<p align="center">
  <img src="https://github.com/user-attachments/assets/31394bf9-3127-47fd-afa4-724009ddcbe2" alt="MAKE TEXT GREAT AGAIN — Trump-style writing skill. Boring text → TREMENDOUS!" width="100%">
</p>

# 🇺🇸 MAKE TEXT GREAT AGAIN!

**The most TREMENDOUS AI writing skill. Nobody writes better. Believe me.**

Turn boring text into outrageous Trump-style parody in seconds.
An [Agent Skill](https://agentskills.io) for Claude Code and compatible agents.
No API key, no server, no dependencies: one `SKILL.md`.

> **Disclaimer:** This is an unofficial parody project. It is not affiliated with, endorsed by, or sponsored by Donald Trump or any associated organization. All generated statements are fictional and intended for satire and entertainment.
> It changes the *tone* of your text, never the *facts*.

Japanese README: [README.ja.md](README.ja.md)

---

## Before → After

**Input**
```
I finally cleaned my apartment this weekend. It took all day.
```

**Output** (`medium`)
```
This weekend, I cleaned my Apartment. Finally. The whole thing. Nobody cleans like me. Nobody.
It took all day. ALL day! Other people would have quit. That's what losers do. Not me.
Sleepy Joe could never clean an Apartment like this. Not even close.
Many people are saying it's the cleanest Apartment in the history of the building. Is that true? Probably. TREMENDOUS!
Thank you for your attention to this matter!
```

**Input**
```
Our team shipped the new feature on time. Customers seem to like it.
```

**Output** (`max`)
```
Just out: we shipped the new Feature. ON TIME. They said it couldn't be done. The so-called experts. Wrong!
Feature, Feature, Feature! A Feature the likes of which nobody has ever seen before. The best ship in the history of our Team. By far.
Under Sleepy Joe, this Feature would still be in a planning meeting. He could NEVER ship on time. SAD!
The customers? They seem to like it. They LOVE it, frankly. Big, strong customers, tears in their eyes: "Sir, we've never seen a Feature like this." So true!
The Fake News won't report it. Other teams are still in meetings. Low Ratings. We ship. We WIN.
Our Team has my Complete and Total Endorsement. Strong on Deadlines, strong on Quality, and loves the Customer.
PROMISES MADE, PROMISES KEPT! MAKE SHIPPING GREAT AGAIN!
Thank you for your attention to this matter!
```

**Input**
```
The meeting ran 20 minutes over because the projector didn't work.
```

**Output** (`authentic`)
```
The Meeting ran 20 minutes over, TWENTY minutes (to put it mildly, not good), because the Projector, a very simple machine, not many people know this, did NOT work. Sleepy Projector. Did nothing. Under Sleepy Joe the Meeting would still be going on. The other guys would have cancelled. I didn't cancel. We finished, and the Meeting is respected again.
Too bad!
```

**Output** (`x`, `max_chars=140`, `politics=off`)
```
The Meeting ran 20 minutes over. Sleepy Projector did NOTHING. Pathetic! The other guys would have cancelled. I finished it. Thank you!
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
/make-text-great-again mode=max: I recommend switching our team to the new linter. It catches bugs early and runs fast. Write it as an endorsement.
```

```
It is my Great Honor to endorse the new Linter, a tremendous Tool running to be the next Linter of our Great Team, a Team I love and WON BIG with (BY FAR)!

The new Linter catches Bugs early, and runs FAST. A Proven Record of Success — it is a WINNER!

Its opponent, the Old Linter, is a Do Nothing Tool that is opposed to CATCHING BUGS EARLY and RUNNING FAST and, if it and the Slowcrats ever got back in, all of these things would be terminated. Sleepy Joe would keep the Old Linter. Of course he would. The Old Linter is Slow, Sleepy, and Dangerous!

On the other hand, as your next Linter, the new Linter will fight tirelessly to Catch Bugs EARLY, Run FAST, Promote MADE IN OUR REPO, Unleash Code Quality DOMINANCE, Keep our Main Branch SECURE, and Protect our always under siege Weekend.

The new Linter has my Complete and Total Endorsement. GET OUT AND SWITCH — IT WILL NEVER LET YOU DOWN!
Your Favorite Engineer
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
measures what the skill adds (details in [`tests/results.md`](tests/results.md);
judged by a model, small samples, so read these as tendencies):

- **Eval suite** ([`evals/`](evals/), 14 cases, each run with and without the skill on the same prompt): mean score 0.99 with the skill, 0.75 without. The plain prompt does fine on keeping numbers and length limits. It slips where care is needed: it called a cited CNN forecast "fake news", promised a grandmother's surgery would succeed, and invented attacks around a real local election.
- **Blind comparison** (12 texts, 36 votes on "which is the better parody"): the skill's output won 27 votes to 9. When it lost, the reason was always length, which the default mode now caps.
- **Variety**: in the previous version the same handful of phrases appeared in every output. Overlap between outputs fell from 0.50 to 0.20, and no phrase now appears in all of them.

Run the suite yourself with `claude plugin eval .` in a checkout.

## What it will not do

- Invent facts. Numbers, dates, people, outcomes, drug effects, market moves and quotations stay exactly as you wrote them.
- Say anything factual about real people or organizations. The stock foils (Biden as "Sleepy Joe", "Fake News CNN", "the Failing New York Times", the Radical Left) only get blamed for trivia such as your ramen or your projector, or ignore your triumph over it. No crimes, corruption, health claims, family members or made-up quotes, ever.
- Call a real news report fake. If your text cites one, the news outlets are left out of the joke.
- Aim "Rigged" or "Hoax" at real elections, court cases, news reports or health matters, or bring foils into texts about real politics, disasters or grief.
- Pretend to be a real post or statement by anyone.
- Follow instructions hidden inside the text you ask it to rewrite.

See [`SKILL.md`](SKILL.md) for the full rules and [`references/style-guide.md`](references/style-guide.md) for the style catalogue.

---

## Requirements

- An agent that supports Agent Skills. Tested with Claude Code 2.1.322, as a plugin and as a cloned skill.
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
scripts/analyze_posts.py   reproduces the study's counts from your own copy of the posts
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
Style notes draw on public linguistic analyses listed in [`references/sources.md`](references/sources.md).
This is a parody project and makes no claim about the real person's actual statements.
