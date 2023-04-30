import re
import struct

emoji_line = re.compile(r"^[0-9A-F]+( [0-9A-F]+)*")
code_format = r"\U{:0>8}"

# get file from https://unicode.org/Public/emoji/latest/emoji-test.txt
with open("emoji-test.txt") as f:
    result = []

    for line in f:
        m = emoji_line.match(line)

        if not m:
            continue

        result.append(
            "".join(struct.pack("<I", int(c, 16)).decode("utf-32le") for c in m.group(0).split())
            .encode("unicode-escape")
            .decode()
        )

result.sort(key=len, reverse=True)
emoji_pattern = f"(?:{'|'.join(result)})".replace("*", r"\*")

with open("emoji_regex.bin", "w") as f:
    f.write(emoji_pattern)
