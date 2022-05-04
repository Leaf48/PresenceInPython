from random import randint, random
from pypresence import Presence
from time import sleep

words = [
    "click here!",
    "dont click here",
    "click to earn money"
]

clientID = "971441562653454347"
RPC = Presence(clientID)
RPC.connect()
RPC.update(
    state="Rich Presence using pypresence!",
    large_image="cute_1",
    buttons=[{"label": words[randint(0, 2)], "url": "https://www.youtube.com/watch?v=LiNxfFkymTk"}]
    )

while True:
    sleep(15)