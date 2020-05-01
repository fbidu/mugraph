"""
μ-graph - a microservice dependency documentation tool
"""
from pathlib import Path

from networkx.readwrite.json_graph import cytoscape

from parser import Parser
from front import Dashboard


def main(filename):
    """
    calls the parser and returns the parsed edges
    """
    filepath = Path(filename).absolute()
    parser = Parser(filepath)
    print(parser.graph.edges())
    d = Dashboard(cytoscape.cytoscape_data(parser.graph))
    d.run()


if __name__ == "__main__":
    # pylint: disable=invalid-name
    import argparse

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("filename")
    args = arg_parser.parse_args()
    main(args.filename)
