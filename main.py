#!/usr/bin/env python3
"""Writes the entry's one-star cat review to /output/entry.txt."""

import os

# 122 characters
REVIEW = "One star. The human feeds me on time but opens the wrong door every single morning. I have filed a complaint with the sun."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(REVIEW)
