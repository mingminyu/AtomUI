from typing import List
from markdown_it import MarkdownIt
from markdown_it.token import Token


class MarkdownParser:
    md_parser = MarkdownIt()

    def split_code_block_content(self, text: str) -> List[Token]:
        """split markdown content into code and non-code content list"""
        tokens = [md_token for md_token in self.md_parser.parse(text) if md_token.content != '']
        # 实际上还可以通过 itertools.groupby 来将非代码块内容进行合并
        return tokens
