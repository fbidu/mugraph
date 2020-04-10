"""
μ-graph - a microservice dependency documentation tool
"""
import mistune
import networkx as nx


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

    def __init__(self, filepath):
        """
        Parameters
        ----------
        filepath: str
            The full path for the markdown file to be parsed
        """
        self.root_name = None
        self.consumes = set()
        self.produces = set()
        self.graph = nx.DiGraph()

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
        at_consumes = False

        for token in self.tokens:

            # The most import processing happens when the token is a heading
            # That is, it starts with at least one # char
            if token.get("type") == "heading":

                text = token["children"][0]["text"]
                level = token["level"]

                """
                *** Skip-level checking ***
                The headers within a session should increase by one step
                at the time. That is, this is invalid:

                  # Title

                  ## Consumes
                  #### ERROR

                But the header may not _always_ be incremental:

                    # Title

                    ## Consumes
                    ### Hey hey
                    ### I'm valid!

                And they can decrease sharply to another H2:
                    # Title

                    ## Consumes
                    ### Hey hey
                    #### I have
                    ##### TONS
                    ###### Of details

                    ## Produces
                    ### This is valid, btw

                """

                if level != 2 and level not in (last_level, last_level + 1):
                    exception = (
                        f"Current level {level} is incompatible with "
                        f"last level {last_level}"
                    )
                    raise ParserException(exception)

                last_level = level

                """
                *** Header Checking ***

                There should be only one top header
                """
                if level == 1:
                    if self.root_name:
                        raise ParserException("Duplicated header")
                    self.root_name = text

                """
                *** Produces-Consumes Checking ***

                The only allowed titles at second level headers is "produces"
                and "consumes". This way we can keep a simple "at_consumes"
                boolean flag to check where we should put the subsequent
                texts.
                """
                if level == 2:
                    if text.lower() not in ("consumes", "produces"):
                        raise ParserException(
                            f"'{text}' not allowed as a level two header"
                        )

                    at_consumes = bool(text.lower() == "consumes")

                if level == 3:
                    if at_consumes:
                        self.consumes.add(text)
                    else:
                        self.produces.add(text)

        # After all the tokens are parsed, we can add them to the graph
        for item in self.consumes:
            self.graph.add_edge(item, self.root_name)

        for item in self.produces:
            self.graph.add_edge(self.root_name, item)
