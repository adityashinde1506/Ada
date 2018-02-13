import logging
import re

logger = logging.getLogger(__name__)


class Lexer(object):

    """
        Converts given string into a stream of tokens.
    """

    def __init__(self):
        self.tokens = ["(?P<WHITESPACE>\s)"]

    def __create_regex(self):
        """
            Creates a single regex string from all given tokens.
        """
        self.lexer_regex = "|".join(self.tokens)
        logger.debug(f"Generated tokenizer regex {self.lexer_regex}")

    def insert_tokens(self, token_list):

        """
            Accepts given list of tokens to build a tokenizer regex.
        """

        assert type(token_list) == list, "Token list should be a list of tuples of the format (token_name, regex)."

        self.tokens += token_list
        self.__create_regex()

    def parse_line(self, line):

        assert type(line) == str, "Function parse_line can only parse a single line string."

        pos = 0
        tokens = []

        while pos < len(line):
            substr = line[pos:]
            token = re.match(self.lexer_regex, substr)
            tokens.append((token.lastgroup, token.group()))
            pos += int(token.end())

        return tokens
