# English examples (Before / After)

All outputs are from `/make-text-great-again`. Generation varies between runs, so
these are representative rather than exact. None of them change the original facts.

"Sleepy Joe" and "the Fake News" are the speaker's own stock foils, borrowed as
**obvious parody**: they get blamed for a projector or out-cleaned in an apartment,
and nothing factual is claimed about anyone. `politics=off` removes them.

---

## 1. Cleaning the apartment

**Input**
```
I finally cleaned my apartment this weekend. It took all day.
```

**Mode:** `standard`

**Output**
```
This weekend, I cleaned my Apartment. Finally. The whole thing. Nobody cleans like me. Nobody.
It took all day. ALL day! Other people would have quit. That's what losers do. Not me.
Sleepy Joe could never clean an Apartment like this. Not even close.
Many people are saying it's the cleanest Apartment in the history of the building. Is that true? Probably. TREMENDOUS!
Thank you for your attention to this matter!
```

---

## 2. Shipping a feature

**Input**
```
Our team shipped the new feature on time. Customers seem to like it.
```

**Mode:** `max`

**Output**
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

**Mode:** `x`, `max_chars=140`

**Output** (135 chars)
```
Just out: we shipped the new Feature ON TIME. Customers like it. Sleepy Joe could NEVER ship on time. Sad! We ship. BIG WIN! Thank you!
```

---

## 3. The projector

**Input**
```
The meeting ran 20 minutes over because the projector didn't work.
```

**Mode:** `light`

**Output**
```
The meeting ran 20 minutes over. Twenty minutes. The projector didn't work. Not good!
But we got through it. We always do (as usual).
Thank you for your attention to this matter!
```

**Mode:** `authentic`

**Output**
```
The Meeting ran 20 minutes over, TWENTY minutes (to put it mildly, not good), because the Projector, a very simple machine, not many people know this, did NOT work. Sleepy Projector. Did nothing. Under Sleepy Joe the Meeting would still be going on. The other guys would have cancelled. I didn't cancel. We finished, and the Meeting is respected again.
Too bad!
```

**Mode:** `max`, `politics=off`

**Output**
```
Just out: the Meeting ran 20 minutes over. TWENTY minutes. Can you believe it?
The Projector didn't work. Sleepy Projector. A Do Nothing Projector. It did NOTHING. A total disaster. Pathetic!
I have been treated very unfairly. No meeting attendee in history has been treated more unfairly. A total Witch Hunt, by a Projector!
The other guys would have cancelled. That's what losers do. I didn't cancel. Meeting, Meeting, Meeting! We finished it.
Big, strong coworkers, tears in their eyes: "Sir, nobody runs over by 20 minutes like you." So true!
We will put a Tariff on Sleepy Projector. A big one. It never ends!
MAKE MEETINGS GREAT AGAIN!
Thank you for your attention to this matter!
```
