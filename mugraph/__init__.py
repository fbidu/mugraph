"""
μ-graph - a microservice dependency documentation tool
"""
import mistune


class ParserException(Exception):
    """
    Generic parsing error
    """

    # pylint: disable=unnecessary-pass
    pass


class Parser:
    """
    mu-Graph main parser. It takes a markdown file and
    breaks it down into a graph

    Attributes
    ----------
    root_name: str
        The name for the main microservice, to be put in
        the center of the graph

    """

    # pylint: disable=too-few-public-methods

    root_name = None

    def __init__(self, filepath):
        """
        Parameters
        ----------
        filepath: str
            The full path for the markdown file to be parsed
        """
        self.__parser = mistune.Markdown(renderer=mistune.AstRenderer())
        self.parse(filepath)

    def parse(self, filepath):
        """
        Breaks a Markdown file into tokens.

        Parameters
        ----------
        filepath:
            The full path for the file to be parsed
        """
        self.tokens = self.__parser.read(filepath)

        last_level = 0

        for token in self.tokens:
            if token.get("type") == "heading":
                text = token["children"][0]["text"]
                level = token["level"]

                if level != 2 and level not in (last_level, last_level + 1):
                    exception = (
                        f"Current level {level} is incompatible with "
                        f"last level {last_level}"
                    )
                    raise ParserException(exception)

                last_level = level

                if level == 1:

                    if self.root_name:
                        raise ParserException("Duplicated header")

                    self.root_name = text
