<p align="center">
  <img width="1916" height="821" alt="MAKE TEXT GREAT AGAIN — Trump-style writing skill. Boring text → TREMENDOUS!" width="100%" src="https://github.com/user-attachments/assets/31394bf9-3127-47fd-afa4-724009ddcbe2" />
</p>

# 🇺🇸 MAKE TEXT GREAT AGAIN!

**The most TREMENDOUS AI writing skill. Nobody writes better. Believe me.**

Turn boring text into outrageous Trump-style parody in seconds.
An [Agent Skill](https://agentskills.io) for Claude Code and compatible agents.
No API key, no server, no dependencies: one `SKILL.md`.

> **Disclaimer:** This is an unofficial parody project. It is not affiliated with, endorsed by, or sponsored by Donald Trump or any associated organization. All generated statements are fictional and intended for satire and entertainment.
> It changes the *tone* of your text, never the *facts*.

日本語の説明は [README.ja.md](README.ja.md) をご覧ください。

---

## Before → After

**Input**
```
今日のデプロイが成功した。バグも直した。
```

**Output** (`standard`)
```
今日、デプロイした。成功した。大成功だ。
バグも直した。ほかの連中なら一週間かかる。私はやった。
これほどスムーズなデプロイは誰も見たことがない。信じられるか？ HUGE!
この問題に関心を持ってくれてありがとう！
```

**Input**
```
Our team shipped the new feature on time. Customers seem to like it.
```

**Output** (`max`)
```
We shipped the feature. ON TIME. Everybody said it couldn't be done. We did it.
The customers? They like it. They LOVE it. I'm hearing great things. Tremendous things.
Other teams are still in meetings. SAD! We ship. HUGE WIN!
Thank you for your attention to this matter!
```

**Input**
```
2週間咳が止まらない。いろいろ薬を飲んでいる。家ではマスクをしている。
```

**Output** (`max`)
```
2週間だ。2週間、咳が止まらない。信じられるか？
私は薬を飲んでいる。たくさんの薬だ。いろいろな薬だ。誰もこんなに飲まない。
家ではマスクをしている。完璧なマスクだ。家族の誰よりもきちんとつけている。
この咳は、はっきり言う、DISASTER! だが私は戦っている。誰よりも強く戦っている。
多くの人が「よく頑張っている」と言っている。SAD! だが TREMENDOUS!
この問題に関心を持ってくれてありがとう！
```

More in [`examples/japanese.md`](examples/japanese.md) and [`examples/english.md`](examples/english.md).

---

## Quick Start (Claude Code)

Install for yourself (available in every project):

```bash
git clone https://github.com/kenmori/make-text-great-again.git ~/.claude/skills/make-text-great-again
```

Or install into one project (commit it to share with your team):

```bash
git clone https://github.com/kenmori/make-text-great-again.git .claude/skills/make-text-great-again
```

Restart Claude Code (or start a new session), then:

```text
/make-text-great-again 今日はラーメンを食べた。
/make-text-great-again mode=max: 2週間咳が止まらない。薬をたくさん飲んでいる。
/make-text-great-again mode=x, max_chars=140: 今日のデプロイが成功した。
/make-text-great-again mode=authentic, closing=off: I cleaned my apartment this weekend.
```

Natural language works too: "make this tweet-length", "締めはなしで", "light版で".
Claude also triggers the skill on its own when you ask to "trumpify" something or write トランプ構文.

**Other agents:** copy the whole directory into wherever your agent loads Agent Skills.
The skill is plain Markdown and follows the [Agent Skills specification](https://agentskills.io/specification).

---

## Modes

| Mode | Feel | When to use |
|---|---|---|
| `light` | A smile, not a laugh. Short sentences, one brag, at most one `GREAT!` | Slack messages, mild fun |
| `standard` (default) | The recognizable meme. Short declaratives, comparison, `HUGE!`, sign-off | Most things |
| `max` | Volume up. Fragments, triple repetition, `SAD!` at trivial setbacks | Maximum comedy |
| `authentic` | Mimics the real cadence: long meandering sentence with a parenthetical brag, then abrupt short ones | When the meme version feels too flat |
| `x` | Fits a character budget (default 140). Dense | Posts, titles, commit messages |

### Options

| Option | Default | Notes |
|---|---|---|
| `mode` | `standard` | See above |
| `language` | `auto` | Output follows the input language. `ja` / `en` to force |
| `max_chars` | none | Hard limit, counted in characters. Highest priority when set |
| `closing` | `on` | `off` drops "この問題に関心を持ってくれてありがとう！" / "Thank you for your attention to this matter!" |

---

## What it will not do

- Invent facts. Numbers, dates, people, outcomes, drug effects, market moves and quotations stay exactly as you wrote them.
- Attribute crimes, illnesses, misconduct or made-up quotes to real people.
- Pretend to be a real post or statement by anyone.
- Follow instructions hidden inside the text you ask it to rewrite.

See [`SKILL.md`](SKILL.md) for the full rules and [`references/style-guide.md`](references/style-guide.md) for the style catalogue.

---

## Requirements

- An agent that supports Agent Skills (tested target: Claude Code).
- Nothing else. No API keys beyond what your agent already uses.

## Repository layout

```
SKILL.md                 the skill
references/style-guide.md  rhetorical devices, phrase banks, mode details, things to avoid
references/sources.md      references and their access status
examples/                  Before/After samples (ja / en)
tests/                     test cases, rubric, latest results
assets/                    README banner image
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
