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
- **Not in the corpus:** posts after January 2021. Two small later samples, from
  2025 and from November 2026, are described separately below. Anything else about
  later habits is general public observation and marked as such.
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

## 2026 sample: the endorsement template

A second sample: 43 posts from the same account, all dated 2026-11-04 (election
day), read from screenshots supplied by the repository owner. Small and
one-sided by construction: every one of the 43 is a candidate endorsement.
It says nothing about how other kinds of posts are written, but it shows one
formula in full, and how fixed that formula has become. Median length is far
above the 2017–2021 corpus: these are four-paragraph posts.

**The skeleton, in order**

1. **Honor opener.** "It is my Great Honor to endorse …", or a status line:
   "… is doing an incredible job representing the wonderful people of …".
   The people of the district are always "incredible", "wonderful",
   "tremendous", "fantastic" or "amazing".
2. **Self-insertion.** The place is "a place I love and WON BIG", often with the
   years listed and a bracketed "(BY FAR)!".
3. **Credential stack.** A run of capitalized titles before the name:
   "A Brave …, successful …, and now, as …". Generational claims
   ("A Fifth Generation …"), "Highly Respected and very popular", "a Proven
   Leader", "a Proven Record of Success — He is a WINNER!", a career
   "loaded up" with accolades.
4. **Loyalty line.** "has been with us from the very beginning", "MAGA all the
   way", "has always been at my side".
5. **Opponent paragraph.** "His opponent, …, is a Radical Left …" followed by a
   list of things the opponent is "opposed to" or "wants", the conditional "if he
   and the … ever got in, all of these things will be terminated", and a
   three-adjective verdict.
6. **Pivot.** "On the other hand, as your next …," or "In contrast,".
7. **The litany.** "will fight tirelessly to" plus eight to ten capitalized verb
   phrases in a row, each with one word in full capitals (DOMINANCE, SECURE,
   LAW AND ORDER, MADE IN THE U.S.A., PEACE THROUGH STRENGTH).
8. **Closer.** "… has my Complete and Total Endorsement to be the next …. GET OUT
   AND VOTE FOR … — HE WILL NEVER LET YOU DOWN!" All 43 end on the
   never-let-you-down line. About half add a signature of title and full name
   in capitals.

**Recurring small habits**

- A fixed epithet welded inside a noun phrase and never varied: "our always
  under siege …".
- Saying a word, then saying it again in capitals: "our now very Secure Border, SECURE".
- A positive nickname in quotation marks before the first name.
- Scare quotes around one ordinary word: a career "loaded up" with wins, a
  somewhat "controversial" sign, the Republican "ticket".
- A bracketed boast mid-sentence: "(and one of the most respected of them all!)".
- A dash and a capitalized afterthought: "with accolades — and WINS!".
- A short proof sentence after an anecdote: "The sign is still there!".
- Positive three-adjective verdicts as well as negative ones: "Young, Strong, and Smart!".
- Insulting respellings of an opponent's name or party.
- "…, which means" followed by a list of four bad outcomes.
- "my friend, the Great …" for allies; "everyone is very proud of, as am I".
- Epithet + name is still in use in 2026 ("Crazy …", "Radical Left Lunatic").
- Typos survive posting: missing spaces and commas in the pasted template.

**What the skill takes from this, and what it does not**

The skill borrows the skeleton and the small habits. It does not borrow the
content: the policy claims, the statements about real candidates, and the
remarks about groups of people stay out. In parody the "candidate" is a ramen
shop or a linter, and the "opponent" is instant noodles.

## 2025 sample: announcements, attacks and decrees

A third sample: 17 posts dated March to June 2025 (one undated), read from
screenshots supplied by the repository owner. Unlike the 2026 sample it is mixed:
announcements, attacks on news outlets and opponents, policy boasts, one
endorsement, one image-only post. Too small to count frequencies; useful for
seeing post types the first corpus under-represents.

**Post types seen**

| Type | Posts | Shape |
|---|---|---|
| Formal announcement | 5 | "BREAKING NEWS: I am pleased to announce that…" or "Just completed…". Long, calm, capitalized nouns, ends on a promise or the sign-off. |
| Attack on an outlet or opponents | 5 | Epithet + name in the first line, a grievance, a sarcastic turn, a short all-caps verdict. |
| All-caps decree | 2 | One to three sentences, entirely in capitals, "MUST", ends with `!`. |
| Policy boast | 2 | A parallel list of good news, bracketed demands, blame for predecessors. |
| Pep talk | 1 | Three "Don't be…!" imperatives, a coined insult, a promise of GREATNESS. |
| Endorsement | 1 | The 2026 template in an earlier, shorter form. |
| Image only | 1 | No text. |

**The sign-off is confirmed.** "Thank you for your attention to this matter" closes
3 of the 17, each a solemn announcement or warning, once followed by a signature
of title and name. In the 2017–2021 corpus the phrase appears once. It is a
habit of the later period, and it belongs to the formal register: the contrast
with the content is the joke.

**News outlets as foils.** Two posts name outlets with their fixed epithets:
"Fake News CNN" and "the Failing New York Times". This matches the first
corpus, where `CNN` appears in 201 posts, `Fake News CNN` in 29 and
`Failing New York Times` in 42. Typical moves: the outlets "teamed up", tried to
"demean" a success, are "getting slammed by the public", and "you would think
they would be proud". Other outlets get one-off labels in scare quotes.

**Habits not seen in the first corpus, or much stronger here**

- "BREAKING NEWS:" as the first words of one's own announcement.
- "At my direction," before any achievement.
- Nobody-before-me frame: for a long time everyone knew about the problem, "but
  NONE of them were able to do anything about it. I am proud to be the President that…".
- Grand naming: a capitalized, scare-quoted official name for a thing
  ("THE ONE, BIG, BEAUTIFUL BILL", an "Infinite Life" Agreement, there is no end!).
- A euphemism followed by a blunt gloss in brackets with its own `!`: "take him out (kill!)".
- Bracketed demands and bracketed definitions: "(the slow moving Fed should cut
  rates!)", a coined insult followed by "(A new party based on Weak and Stupid people!)".
- Credibility assertion: "it went very well… If it wasn't, I would say so now,
  rather than later."
- "Sorry, but it's my job to…. THAT'S WHAT I GOT ELECTED TO DO."
- A name, then a superlative appositive in capitals: "…, THE WORST … IN THE HISTORY OF …,".
- "They have lost everything, especially their minds!"
- Scare quotes that demote a title: the so-called "Supreme Leader", our past "leaders".
- Ominous hedges: "at least not for now", "Our patience is wearing thin."
- The catastrophe ladder: "could very well lead to the destruction of our
  Country!" → "The danger is unparalleled!" → "STOP … NOW, BEFORE IT IS TOO LATE." →
  "If … do not fix this … IMMEDIATELY, our Country is in very serious trouble!"
- Sarcastic thanks: thanking someone for giving the villains "such a wonderful place to live".
- Total verdicts as closers: "TOTAL OBLITERATION!", "COMPLETELY DESTROYED!".
- Trailing escalation and trailing abundance: "and probably worse!", "and much more!".
- After the victory, the next demand: "NOW IS THE TIME FOR PEACE!", "Let the
  process begin!", "send this Bill to my desk AS SOON AS POSSIBLE! There is no time to waste."
- "There is not another … in the World that could have done this."
- Parallel good-news list: "… are down, … are down, … are down, there is NO …".
- Triple of a topic name as a label for a grievance ("Russia, Russia, Russia").
- Third-person self with "by all accounts".

**What the skill takes from this, and what it does not**

As with the 2026 sample, only the shapes. The subjects of these posts are wars,
immigration, courts and named officials. None of that content is reused, and the
skill does not apply these shapes to such subjects.

## Later habits (general observation, not in any sample)

- Long posts with whole sentences in capitals.
- "…the likes of which nobody has ever seen before" as an all-purpose amplifier.
- "would never have happened if I were President" as the standard counterfactual.
- Rally stories in which large, tough men approach in tears and begin with "Sir".
- Announcing that something will be revealed "soon", then moving on.
