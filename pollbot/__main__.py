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
    poll = random.choice(polls)
    if poll["id"] not in used_polls:
        break

p = m.make_poll(poll["options"], 24 * 60 * 60 * 3)

m.status_post(poll["question"], poll=p)

