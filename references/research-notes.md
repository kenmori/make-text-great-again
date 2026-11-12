# Research notes — what the posts actually look like

A frequency study of the public posting style this skill parodies. It exists so the
style guide is grounded in counts instead of memory of the meme.

## Corpus and method

- **Data:** every post from the @realDonaldTrump account between 2017-01-20 and
  2021-01-08, from the public archive listed in `sources.md` (23,075 rows).
- **Filter:** retweets and link-only posts removed, leaving **14,391 original posts**.
- **Method:** plain counting with a short script: closing sentences, capitalized
  runs, opening words, parentheticals, epithet + name pairs, n-grams, and a list
  of candidate phrases. Counts below are "posts containing the phrase".
- **Not in the corpus:** posts after January 2021. Later habits (the sign-off
  "Thank you for your attention to this matter!", very long all-caps posts) are
  noted from general public observation and marked as such.
- No post is reproduced here. Only short recurring phrases and their counts.

## Shape of a post

| Feature | Posts | Share |
|---|---|---|
| Ends with `!` | 6,414 | 44.6% |
| Contains an ALL-CAPS word of 4+ letters | 4,614 | 32.1% |
| Capitalizes a common noun mid-sentence (Country, Border, Military, Crime…) | 3,386 | 23.5% |
| Uses an ellipsis, usually to continue across posts | 2,967 | 20.6% |
| Contains quotation marks | 2,122 | 14.7% |
| Contains a parenthetical aside | 1,433 | 10.0% |
| Contains a question mark | 964 | 6.7% |
| Entirely in capitals | 249 | 1.7% |

Median length is 27 words. Average is 0.9 exclamation marks per post, so the real
thing is **less** exclamation-heavy than the meme: one strong closer beats five.

## Closers (final short sentence)

`Thank you!` 301 · `Enjoy!` 110 · `MAKE AMERICA GREAT AGAIN!` 86 · `Wow!` 62 ·
`Sad!` 55 · `Witch Hunt!` 30 · `Great!` 32 · `Fake News!` 21 · `Too bad!` 18 ·
`Stay tuned!` 17 · `So true!` 17 · `True!` 16 · `Disgraceful!` 15 · `Crazy!` 15 ·
`Not good!` 14 · `PRESIDENTIAL HARASSMENT!` 14 · `Nice!` 13 · `See you soon!` 13 ·
`JOBS, JOBS, JOBS!` 19 · `Great job!` 7 · `Working hard!` 7 · `Wrong!` 7 ·
`Pathetic!` 6 · `Can't let that happen!` 4 · `It never ends!` 4 · `Just asking!` 3

Finding: the closer is a **verdict on what was just said**, two or three words,
and usually the only exclamation in the post.

## Capitalized words

Most frequent all-caps items outside acronyms: `GREAT` 197, `VOTE` 97, `JOBS` 88,
`THANK YOU` 71, `NEVER` 63, `NOTHING` 57, `VERY` 40, `ZERO` 35, `EVER` 32,
`MUCH` 28, `WIN!` 30, `BIG!` 13, `FAST!` 16, `MASSIVE` 8, `WEAK` 8.

Finding: capitals land on **small intensifiers** (NEVER, NOTHING, VERY, ZERO,
MUCH, EVER), not on the nouns you would expect.

## Epithet + name ("nicknames")

`Fake News` 831 · `Radical Left` 220 · `Crooked …` 208 · `Do Nothing Democrats` 189 ·
`Sleepy Joe` 188 · `Crazy …` 183 · `Failing …` 115 · `Lamestream Media` 88 ·
`Mini …` 29 · `Shifty …` 20 · `Nervous …` 12 · `Lyin' …` 11 · `Wacky …` 5 · `Sloppy …` 2

Finding: the formula is **one belittling adjective, capitalized, welded to the
name**, then reused every time until it replaces the name. Institutions get the
same treatment as people ("Failing", "Fake", "Lamestream").

## Opponents and blame

`Biden` appears in 459 posts, `Obama` in 405, `Hillary` in 251, `China` in 489.
Recurring frames: "inherited a mess", "under Obama", "Obama-Biden",
"more in 47 months than … in 47 years", "If Biden wins, China wins".

Finding: a foil is always available. Good outcomes are personal; bad outcomes
were inherited from, or caused by, the foil.

## Self-praise frames

`record` 302 · `numbers` 249 · `respect` 240 · `great job` 232 · `incredible` 214 ·
`tremendous` 199 · `which I …` 185 · `beautiful` 160 · `greatest` 156 ·
`in the history of` 132 · `ratings` 130 · `polls` 132 · `winning` 105 · `by far` 82 ·
`big win` 65 · `than ever before` 48 · `like never before` 27 ·
`more than any` 28 · `your favorite President` 23 · `not even close` 19 ·
`the likes of which` 12

## Grievance frames

`witch hunt` 353 · `totally` 276 · `hoax` 232 · `a total …` 157 · `phony` 156 ·
`rigged` 140 · `scam` 136 · `disgrace` 139 · `unfair` 122 · `disaster` 121 ·
`mess` 109 · `so-called` 71 · `treated` 65 · `enemy of the people` 48 ·
`harassment` 39 · `very unfair` 38

## Formula sentences

- Endorsement: "has my Complete and Total Endorsement" — 210 posts.
- Credentials list: "strong on Crime, the Border, … loves our Military and our Vets" — 180 posts.
- Place honorific: "the Great State of …" — 192 posts.
- Honor: "It was my great honor to …" — 111 posts.
- Promise: "will never let you down" — 29 posts.

## Openers

`Thank you` 332 · `Congratulations to` 165 · `I will be` 120 · `The Fake News` 88 ·
`Heading to` 82 · `Looking forward to` 63 · `Remember,` 58 · `Just out` 48 ·
`Wow` 167 · `Getting ready to` 42 · `Just landed in` 38 · `Just spoke to` 37 ·
`I am pleased to announce` 30 · `Can you believe` 15

## Parentheticals

Most common contents: `(by far)`, `(to put it mildly)`, `(as usual)`,
`(and others)`, `(a record)`, `(just kidding)`, `(do you believe this?)`,
`(I hope!)`, `(which I think they will)`, `(but fair)`, `(by a lot)`.

Finding: the aside is short, three words on average, and either inflates
("by far") or winks ("just kidding").

## Intensifiers

`so much` 162 · `so many` 134 · `very good` 127 · `far more` 75 · `very important` 68 ·
`very bad` 61 · `highly respected` 54 · `very big` 50 · `so true` 43 · `very strong` 42 ·
`very unfair` 30 · `totally corrupt` 14 · `totally discredited` 10

## What the meme gets wrong

| Stock phrase | Posts containing it |
|---|---|
| "believe me" | 0 |
| "bigly" / "big league" | 0 |
| "many such cases" | 0 |
| "frankly" | 8 |
| "folks" | 6 |
| "people are saying" | 2 |

These are **spoken** habits from rallies and interviews, or older posts. They are
still recognizable and the skill keeps them, but as speech flavor. Written posts
lean on capitalized nouns, epithets, formula sentences, and a short verdict at the end.

## Later habits (general observation, not in this corpus)

- Sign-off "Thank you for your attention to this matter!" on formal-sounding posts.
- Long posts with whole sentences in capitals.
- "…the likes of which nobody has ever seen before" as an all-purpose amplifier.
- "would never have happened if I were President" as the standard counterfactual.
- Rally stories in which large, tough men approach in tears and begin with "Sir".
- Announcing that something will be revealed "soon", then moving on.
