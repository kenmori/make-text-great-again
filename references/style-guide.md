# Style Guide — トランプ構文の文体パターン

This file is loaded on demand by `SKILL.md`. It describes the rhetorical devices
the skill imitates, gives phrase banks in Japanese and English, explains how each
mode should feel, and lists expressions to avoid.

Everything here describes a **parody style**. It is written in our own words from
public observation and published linguistic analysis (see `sources.md`). It does
not reproduce any real post.

---

## 1. Core devices

| # | Device | What it does | JA example | EN example |
|---|--------|--------------|------------|------------|
| 1 | **One claim per sentence** | Chop long sentences. Rhythm from brevity. | 「デプロイした。成功した。大成功だ。」 | "We shipped it. It worked. Big win." |
| 2 | **Self-praise** | Treat the narrator's trivial actions as historic. | 「私はラーメンを作った。誰も作れないラーメンだ。」 | "I cleaned the kitchen. Nobody cleans like me." |
| 3 | **Comparison** | Contrast with a vague, inferior "them". | 「ほかの連中ならカップ麺だ。私は違う。」 | "Other people would've quit. Not me." |
| 4 | **Simple English exclamations** | Capitalized one-word verdicts. | `GREAT!` `SAD!` `HUGE!` | `DISASTER!` `TREMENDOUS!` `WOW!` |
| 5 | **Signature sign-off** | Formal, slightly absurd closing line. | 「この問題に関心を持ってくれてありがとう！」 | "Thank you for your attention to this matter!" |
| 6 | **Repetition** | Repeat the key word, then intensify. | 「大きな勝利だ。とても大きな勝利だ。」 | "A big win. A very, very big win." |
| 7 | **Superlatives & absolutes** | "Ever", "nobody", "the best". | 「史上最高」「誰も見たことがない」 | "the best ever", "like nobody has ever seen" |
| 8 | **Rhetorical question** | Invite the reader to be amazed. | 「信じられるか？」「考えてみてほしい。」 | "Can you believe it?" "Think about it." |
| 9 | **Anonymous chorus** | Unverifiable third-party agreement. | 「多くの人がそう言っている。」 | "Many people are saying…" "People are telling me…" |
| 10 | **Asides & digressions** (`authentic`) | Parenthetical brag, mid-sentence pivot. | 「（ちなみに私はゲームがとても上手い、みんな知っている）」 | "(and I'm very good at games, everybody knows this)" |

### Secondary devices (use sparingly)

- **"Frankly / はっきり言う"** as a sentence opener before a blunt verdict.
- **"Believe me / 本当だ / 信じてほしい"** as a trailing reassurance.
- **Nicknaming the problem**: 「この咳、"The Cough"だ。」 Only when it's obviously a joke.
- **Fake modesty that is not modest**: 「自慢ではないが、史上最高だ。」
- **Numbers as applause**: keep the original numbers, but frame them as victories.
  「12%だ。12%！ 誰もこんな数字は出せない。」

---

## 2. Phrase banks

### Japanese

**Openers / connectors**
- 「はっきり言う。」「正直に言おう。」「聞いてほしい。」「考えてみてほしい。」

**Self-praise**
- 「私はやった。」「私は違う。」「誰よりもうまくやった。」「完璧だった。」
- 「自慢ではないが、」「みんな知っている。」「史上最高かもしれない。」

**Comparison targets (safe, fictional)**
- 「ほかの連中」「普通の人」「ほかのやつら」「いつもの連中」「批判ばかりの人たち」
- 「ほかのエンジニア」「ほかの店」「ほかのチーム」（文脈に合わせて）

**Chorus**
- 「多くの人がそう言っている。」「みんなが言っている。」「賢い人たちはみんな知っている。」
- 「"あれは本物だ"と、多くの人が言っている。」（引用の中身は原文の内容についてのみ）

**Superlatives**
- 「史上最高」「史上最大」「誰も見たことがない」「信じられないほど」「とてつもなく」

**Rhetorical questions**
- 「信じられるか？」「本当か？ 本当だ。」「誰ができる？ 私だ。」

**English interjections that sit naturally in Japanese text**
- `GREAT!` `HUGE!` `SAD!` `WOW!` `DISASTER!` `TREMENDOUS!` `SMART!` `WIN!`

**Sign-off**
- 「この問題に関心を持ってくれてありがとう！」（既定）
- Variants only when the user asks for variety: 「ありがとう。本当にありがとう。」

### English

**Openers / connectors**
- "Frankly," "Look," "Let me tell you," "Think about it."

**Self-praise**
- "Nobody does it better." "I did it. Me." "Perfect. Absolutely perfect."
- "Not to brag, but…" (then brag) "Everybody knows this."

**Comparison targets (safe, fictional)**
- "the other guys," "most people," "the usual crowd," "the so-called experts"

**Chorus**
- "Many people are saying…" "People are telling me…" "Everyone agrees."

**Superlatives**
- "the best ever," "like nobody has ever seen," "the biggest in history," "tremendous"

**Rhetorical questions**
- "Can you believe it?" "Who else could do that? Nobody."

**Exclamations**
- `GREAT!` `HUGE!` `SAD!` `WOW!` `DISASTER!` `TREMENDOUS!` `BIG WIN!`

**Sign-off**
- "Thank you for your attention to this matter!" (default)

---

## 3. Mode guidance in detail

### `light`
The reader should smile, not laugh out loud. Short sentences, one brag, at most
one exclamation, usually the sign-off. Good for workplace Slack, where `max` would be too much.
Keep roughly the same length as the input.

### `standard` (default)
The recognizable version. Short declaratives, one or two brags, one comparison,
one rhetorical question or chorus line, one or two exclamations, sign-off.
Roughly 1.3–2× the input length.

### `max`
Volume turned up. Sentence fragments. Repeat the key noun three times. Multiple
comparisons. Two to four exclamations, at least one `SAD!` or `DISASTER!` applied to
a trivial setback. Still no invented facts. Roughly 2–3× the input length.

### `authentic`
Mimics the actual cadence instead of the meme version. Mix one long, meandering
sentence (with a parenthetical brag and a pivot like 「それで、」 / "and by the way")
with abrupt short ones. Use a rhetorical question. Capitalize irregularly: one word in
caps mid-sentence is fine. Fewer stock exclamations, more "believe me / 本当だ".
Sign-off is usual but may be dropped if the ending already lands.

### `x`
Character budget first. Default budget 140 when none is given. Dense: brag,
comparison or chorus, one exclamation, sign-off if it fits. When trimming, cut in
this order: redundant repetition → comparison → sign-off. Never cut facts.
Count every character including spaces, punctuation, and the sign-off.

---

## 4. Length and rhythm rules

- Vary sentence length even in `max`: three fragments, then one normal sentence.
- Place the strongest exclamation after the climax of the original, not at random.
- End with the sign-off **on its own line** when the output has more than one line.
- Preserve paragraph breaks from the input when it has them.
- In Japanese, prefer 「だ・である」 for assertion. Keep 「です・ます」 only when the
  user asks for polite tone.

---

## 5. Avoid

**Fidelity**
- Adding people, numbers, dates, prices, drug effects, diagnoses, returns, legal
  outcomes, or quotations that are not in the input.
- Changing the outcome of the original (a failed deploy must stay failed; blame the
  "other guys", don't rewrite history).
- Turning "many people are saying" into a specific attributed quote.

**Politics and real people**
- Dragging in real politicians or public figures when the input doesn't mention them.
- Attributing crimes, illnesses, misconduct, or invented statements to any real person.
- Partisan slogans or policy claims. The joke is the *style*, not a position.

**Tone**
- Slurs, mockery of protected characteristics, harassment of private individuals.
- Content that would be harmful if a reader took it literally (medical, financial,
  legal instructions dressed up as bravado).

**Craft**
- Stacking every device in every sentence. It stops being funny.
- More than one sign-off.
- Ending every sentence with an exclamation mark.
- Copying real posts verbatim. Describe the style; don't transcribe it.
