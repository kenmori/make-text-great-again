# English examples (Before / After)

All outputs are from `/make-text-great-again`. Generation varies between runs, so
these are representative rather than exact. None of them change the original facts.

---

## 1. Cleaning the apartment

**Input**
```
I finally cleaned my apartment this weekend. It took all day.
```

**Mode:** `standard`

**Output**
```
This weekend, I cleaned my apartment. The whole thing. Nobody cleans like me. Nobody.
It took all day. All day! Other people would have quit. Not me. I kept going.
Many people are saying it's the cleanest apartment they've ever seen. Is that true? Probably. TREMENDOUS!
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
We shipped the feature. ON TIME. Everybody said it couldn't be done. We did it.
The customers? They like it. They LOVE it. I'm hearing great things. Tremendous things.
Other teams are still in meetings. SAD! We ship. HUGE WIN!
Thank you for your attention to this matter!
```

**Mode:** `x`, `max_chars=140`

**Output** (136 chars)
```
We shipped the feature ON TIME. Customers love it. Other teams? Still in meetings. SAD! We ship. HUGE WIN! Thank you for your attention!
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
The meeting ran 20 minutes over. Twenty minutes. The projector didn't work. Not great, folks.
Projector problems. Very sad. But we got through it. We always do.
Thank you for your attention to this matter!
```

**Mode:** `authentic`

**Output**
```
So the meeting ran 20 minutes over, twenty minutes (and I'm always on time, people know this about me, I'm very punctual), because the projector, which is supposed to be a very simple machine, didn't work. Didn't work at all. Can you believe it? The other guys would've cancelled. I didn't cancel. We finished the meeting. Believe me.
Thank you for your attention to this matter!
```
