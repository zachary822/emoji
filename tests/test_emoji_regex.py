import pytest

import emoji_regex


class TestEmojiRegex:
    def test_matches_longest_possible(self):
        assert emoji_regex.emoji_regex.match("👩🏻‍❤️‍💋‍👨🏻").group(0) == "👩🏻‍❤️‍💋‍👨🏻"

    @pytest.mark.parametrize(
        "test_str,match",
        [
            ("😝😬", "😝"),
            ("👩🏻👩🏻‍❤️‍💋‍👨🏻", "👩🏻"),
            ("👩🏻‍❤️‍💋‍👨🏻👨🏻", "👩🏻‍❤️‍💋‍👨🏻"),
        ],
    )
    def test_matches_individual(self, test_str, match):
        assert emoji_regex.emoji_regex.match(test_str).group(0) == match
