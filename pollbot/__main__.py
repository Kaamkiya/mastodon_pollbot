"""
Mastodon poll bot

Posts random polls to https://mastodon.bot/@polls
"""

import os
import json
import random

from mastodon import Mastodon

m = Mastodon(api_base_url="https://mastodon.bot",
             access_token=os.getenv("MASTODON_ACCESS_TOKEN"))

with open("polls.json", "r", encoding="utf-8") as f:
    polls = json.loads(f.read())

used_polls = polls["used"]

while True:
    poll = random.choice(polls["polls"])
    if poll["id"] not in used_polls:
        break

# 24 hours of 60 minutes with 60 seconds each, across 3 days
p = m.make_poll(poll["options"], 24 * 60 * 60 * 3)

m.status_post(poll["question"], poll=p)

polls["used"].append(poll["id"])

with open("polls.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(polls, indent=2))

