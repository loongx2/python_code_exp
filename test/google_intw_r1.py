#!/usr/bin/python

import time

likes = {}

count = 0

def trigger():
    now = time.time()
    
    if now in likes:
        likes[now] += 1
    else:
        likes.update({now: 1})


def get_count():
    c_now = time.time()

    for key in likes:
        if c_now - key < 300:
            count += likes[key]
        else:
            likes.pop(key)
    return count
