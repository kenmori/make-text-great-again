# English examples (Before / After)

Every output below is a real run of the v0.6.0 skill on Claude Code 2.1.322
(2026-11-14), one run per input, untouched. Output varies from run to run. Each is the
output of a single run, not the best of several. None of them change the
facts of the input.

"Sleepy Joe" and "the Fake News" are the speaker's own stock foils, borrowed as
obvious parody. `politics=off` removes them.

---

## 1. Cleaning the apartment

**Input**
```
I finally cleaned my apartment this weekend. It took all day.
```

**Mode:** (default)

**Output**
```
My apartment is CLEAN. Finally. This weekend I cleaned it. All of it. It took all day.

Winners finish the job. Losers leave it for later.

The so-called experts were laughing at my apartment. Not anymore. My apartment is respected again.

PROMISES MADE, PROMISES KEPT! WIN, WIN, WIN!
```

---

## 2. Shipping a feature

**Input**
```
Our team shipped the new feature on time. Customers seem to like it.
```

**Mode:** (default)

**Output**
```
On time. ON TIME! Our team shipped the new feature, and it's beautiful.

Winners ship. Losers slip. We are winners.

The customers seem to like it. They seem to like it very much. We'll see what happens, but the signs are tremendous.

The so-called experts? Very quiet right now.

PROMISES MADE, PROMISES KEPT! SHIP IT AGAIN, AND AGAIN, AND AGAIN!
```

**Input**
```
Our team shipped the new feature on time. Customers seem to like it.
```

**Mode:** `x`, `max_chars=140`

**Output** (114 chars)
```
Our team shipped the new feature ON TIME. Beautiful. Customers seem to like it. We're winners, total winners. WIN!
```

---

## 3. The projector, three ways

**Input**
```
The meeting ran 20 minutes over because the projector didn't work.
```

**Mode:** `light`

**Output**
```
The meeting ran 20 minutes over. The projector didn't work. Not good, believe me. Everyone waited, very patiently.
```

**Input**
```
The meeting ran 20 minutes over because the projector didn't work.
```

**Mode:** `authentic`

**Output**
```
The Meeting ran 20 minutes over, and not because of me. The Projector, a very disloyal machine, did not work. Not good!

Everyone waited. We waited, and waited, and the Projector still did nothing. A total disaster. Many people are saying it, and they are right.

Thank you for your attention to this matter!
```

**Input**
```
The meeting ran 20 minutes over because the projector didn't work.
```

**Mode:** `medium`, `politics=off`

**Output**
```
The meeting ran 20 minutes over. TWENTY. And why? The projector. The Rigged Projector, the worst projector in the history of meetings, didn't work. We were treated very unfairly.

This could very well lead to the destruction of the agenda! STOP IT NOW, BEFORE IT IS TOO LATE.

Sad!
```

---

## 4. An endorsement

**Input**
```
I recommend switching our team to the new linter. It catches bugs early and runs fast. Write it as an endorsement.
```

**Mode:** (default)

**Output**
```
It is my Great Honor to recommend that our Team switch to the New Linter. A Tremendous Tool!

It Catches Bugs Early. Very Early. Before they become Big, Ugly, Embarrassing Bugs. And it Runs Fast. FAST!

Bugs, on the other hand, are Slow, Sneaky, and Sloppy! The New Linter will fight tirelessly to Catch Bugs, Run Fast, and Protect our always under siege Codebase.

The New Linter has my Complete and Total Endorsement!

SWITCH THE TEAM — IT WILL NEVER LET YOU DOWN!

(Endorsement form used for a linter only, not for any real candidate or election.)
```

> The only facts about the linter are the two from the input. The opponent is always an object or an invented rival, never a real product, company or person.

---

## 5. A complaint

**Input**
```
The office Wi-Fi went down three times today. I lost an hour of work.
```

**Mode:** (default)

**Output**
```
The office Wi-Fi. Sleepy Wi-Fi. THE WORST WI-FI IN THE HISTORY OF OFFICES!

It went down three times today. Three! I lost an hour of work. One full hour. Gone.

I have been treated very unfairly. A total Witch Hunt!

This could very well lead to the destruction of the entire workday. FIX IT NOW, BEFORE IT IS TOO LATE.

Thank you for your attention to this matter!

MAKE THE WI-FI GREAT AGAIN!
```

---

## 6. A plan, no politics

**Input**
```
We have a team lunch this Friday at noon. I'm choosing the restaurant.
```

**Mode:** `politics=off`

**Output**
```
To all Team Members, Colleagues, and Hungry People Everywhere: please consider this Friday, at NOON, to be a TEAM LUNCH IN ITS ENTIRETY.

At the request of just about everybody, I am choosing the restaurant. Me. Personally.

The choice is clear: a very, very good restaurant. Otherwise, the real pain is yet to come.

EVERYONE MUST ARRIVE HUNGRY!

This may be the Biggest Team Lunch ever held on a Friday. Our patience for bad lunches is wearing thin.

Thank you for your attention to this matter!

Your Favorite Lunch Chooser
```
