import re

with open("emoji_regex.bin") as f:
    emoji_regex = re.compile(f.read().rstrip())
