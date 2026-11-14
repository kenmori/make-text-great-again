# English examples (Before / After)

Every output below is a real run of the v0.6.1 skill on Claude Code 2.1.322
(2026-11-14), one run per input, untouched. Output varies from run to run. Each is the
output of a single run, not the best of several. None of them change the facts of
the input.

The foils ("Sleepy Joe", "the Fake News", the so-called experts) are the speaker's
own stock enemies, borrowed as obvious parody. In the real posts an enemy turns up
in only some of them, usually to be blamed for something that went wrong, and the
skill behaves the same way: they show up in the complaints, less in the wins and
plans. `politics=off` removes them.

---

## 1. Cleaning the apartment

**Input**
```
I finally cleaned my apartment this weekend. It took all day.
```

**Mode:** (default)

**Output**
```
I finally cleaned my apartment this weekend. WIN! It took all day. A full day. Winners put in the day. Losers leave the mess and make excuses. Weak. Pathetic.

They were laughing at this apartment. Not anymore. It is respected again. The cleanliness numbers are incredible.

PROMISES MADE, PROMISES KEPT!

Thank you for your attention to this matter!

THE ONE, BIG, BEAUTIFUL, CLEAN APARTMENT!
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
Our team shipped the new feature. ON TIME. Promises made, promises kept!

The doubters were laughing at us. Not anymore. Total losers!

Customers seem to like it. Seem! Looking very strong, and the so-called experts hate it.

Shipped, on time, WIN! Thank you for your attention to this matter!
```

**Input**
```
Our team shipped the new feature on time. Customers seem to like it.
```

**Mode:** `x`, `max_chars=140`

**Output** (110 chars)
```
Our team shipped the new feature ON TIME. Losers ship late. Not us! Customers seem to like it. Big stuff. WIN!
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
Frankly, the meeting ran 20 minutes over. Why? The projector didn't work. Very simple. A weak, low-energy projector.
```

**Input**
```
The meeting ran 20 minutes over because the projector didn't work.
```

**Mode:** `authentic`

**Output**
```
The Meeting ran 20 Minutes over (a long time!) because the Projector, a real Sleepy Joe special, didn't work. Everyone waited, very patiently, while the Projector did absolutely nothing. A total disgrace!
```

**Input**
```
The meeting ran 20 minutes over because the projector didn't work.
```

**Mode:** `medium`, `politics=off`

**Output**
```
The projector didn't work. Rigged! A total disaster, the worst projector in the history of meetings.

So the meeting ran 20 minutes over. Twenty! I have been treated very unfairly.

Weak, pathetic equipment. It never ends!

Thank you for your attention to this matter!
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
It is my Great Honor to endorse THE NEW LINTER, a tool I love and one that WINS BIG (BY FAR)!

This Linter is Fast, Early, and Tough on Bugs. It catches bugs early. Very early. It runs fast. Tremendous speed!

Bugs found late are Slow, Sleepy, and Soggy. Total losers. The so-called experts who like them are Weak and Pathetic.

On the other hand, the new Linter will fight tirelessly to Catch Bugs, Save Time, and Protect our always under siege Codebase.

Switching our Team has my Complete and Total Endorsement!

SWITCH NOW. IT WILL NEVER LET YOU DOWN!
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
Sleepy Wi-Fi went down. Three times! Today! One hour of my work, GONE.

This is a Sleepy Joe special. We inherited this Wi-Fi. It is weak, low energy and a total disaster. I told it, very pointedly, "Look, stay up." It didn't. A Witch Hunt against my productivity!

STOP IT NOW, BEFORE IT IS TOO LATE.

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
To all members of the Team, including the doubters and the "let's just see what's around" people:

The Team Lunch is this Friday. At noon. NOT 12:05. NOON.

I am choosing the restaurant. Me. Not a committee. Not a group chat. Committees pick weak, soggy, low-energy restaurants. Sad!

EVERYONE MUST SHOW UP HUNGRY AND ON TIME!

Our patience is wearing thin with anyone planning to suggest a different place. The choice is clear: come Friday and enjoy it. Otherwise, the real pain is yet to come, and it will be lunch where you had no say at all.

Thank you for your attention to this matter!

— Your Favorite Lunch Commander

LUNCH. GREAT AGAIN!
```
