#!/usr/bin/env python3
"""Count stylistic features in a file of posts.

Reproduces the numbers in references/research-notes.md from your own copy of
the data. The posts themselves are not part of this repository.

Usage:
    python3 scripts/analyze_posts.py posts.json

posts.json is a JSON list of objects with a "text" field and, optionally,
"created_at" (ISO date) and "note_tweet": {"text": ...} for long posts, which is
the shape the X API returns. Nothing is sent anywhere; the script only reads the file.
"""
import collections
import json
import re
import statistics
import sys


def full_text(post):
    note = post.get("note_tweet") or {}
    return (note.get("text") or post.get("text") or "").replace("&amp;", "&")


def kind(text):
    if re.search(r"Complete and Total Endorsement|has my (?:Complete|Full)", text, re.I):
        return "endorsement"
    if re.search(r"GET OUT AND VOTE|VOTE FOR|Election Day", text):
        return "vote-call"
    return "other"


FEATURES = [
    ("ends with !", lambda x: x.rstrip().endswith("!")),
    ("ALL-CAPS word of 4+ letters", lambda x: bool(re.search(r"\b[A-Z]{4,}\b", x))),
    ("entirely in capitals", lambda x: x.upper() == x and len(x) > 20),
    ("parenthetical", lambda x: "(" in x and ")" in x),
    ("question mark", lambda x: "?" in x),
    ("scare quotes", lambda x: bool(re.search(r"[“\"][A-Za-z ]{2,25}[”\"]", x))),
    ("triple exclamation marks", lambda x: "!!!" in x),
    ("Sad!", lambda x: bool(re.search(r"\bSad!", x, re.I))),
    ("believe me", lambda x: "believe me" in x.lower()),
    ("Thank you for your attention to this matter", lambda x: "thank you for your attention" in x.lower()),
    ("label opener (WORD:)", lambda x: bool(re.match(r"[A-Z][A-Z &]{3,25}[:!…]", x))),
    ("in (the) history", lambda x: bool(re.search(r"in (the )?history", x, re.I))),
    ("never (seen) before", lambda x: bool(re.search(r"never (seen )?before", x, re.I))),
    (", ME", lambda x: bool(re.search(r",\s*ME\b", x))),
    ("Fake News", lambda x: "fake news" in x.lower()),
    ("Radical Left", lambda x: "radical left" in x.lower()),
]


def report(label, texts):
    n = len(texts)
    if not n:
        return
    print(f"\n== {label}: {n} posts")
    print(f"   median words: {statistics.median(len(t.split()) for t in texts)}")
    print(f"   exclamation marks per post: {sum(t.count('!') for t in texts) / n:.2f}")
    for name, test in FEATURES:
        hits = sum(1 for t in texts if test(t))
        print(f"   {name}: {hits} ({100 * hits / n:.0f}%)")
    closers = collections.Counter()
    for t in texts:
        clean = re.sub(r"https?://\S+", "", t).strip()
        last = re.split(r"(?<=[.!?])\s+", clean)[-1] if clean else ""
        if 0 < len(last) <= 45 and last.endswith("!"):
            closers[last] += 1
    print("   closers: " + ", ".join(f"{k} ({v})" for k, v in closers.most_common(12)))


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as handle:
        posts = json.load(handle)
    texts = [full_text(p) for p in posts]
    texts = [t for t in texts if t and not t.startswith("RT @")]
    by_kind = collections.defaultdict(list)
    for t in texts:
        by_kind[kind(t)].append(t)
    report("all posts", texts)
    for name in ("other", "endorsement", "vote-call"):
        report(name, by_kind[name])


if __name__ == "__main__":
    main()
