"""
Unit tests for the Parser module
"""
from pathlib import Path
import pytest
import mistune

from mugraph.parser import Parser, ParserException

# pylint:disable=redefined-outer-name


@pytest.fixture(scope="session")
def valid_sample():
    """
    Returns a parser for sample01
    """
    sample_file = Path("tests/sample01.md")
    parser = Parser(sample_file.absolute())
    return parser


@pytest.fixture(scope="session")
def valid_sample_ast():
    """
    Returns syntax tree for sample01
    """
    renderer = mistune.Markdown(renderer=mistune.AstRenderer())
    sample_file = Path("tests/sample01.md")
    return renderer.read(sample_file)


def test_root_name_is_detected(valid_sample):
    """
    tests if a the parser can correctly evaluate
    the main microservice's name
    """
    assert valid_sample.root_name == "Cashless"


def test_double_root_fails():
    """
    tests if the parser fails when processing a file
    with two headers
    """
    sample_file = Path("tests/doubleh1.md")

    with pytest.raises(ParserException) as excep:
        Parser(sample_file.absolute())

    assert str(excep.value) == "Duplicated header"


def test_skipy_header_fails():
    """
    if the headers increase more than 1 unit, like this:

        # Title
        ## Consumes
        #### ERROR!

    We shuold get an error
    """
    sample_file = Path("tests/skiphead.md")

    with pytest.raises(ParserException) as excep:
        Parser(sample_file.absolute())

    assert str(excep.value) == "Current level 5 is incompatible with last level 3"


def test_consumes_are_parsed(valid_sample):
    """
    this test checks if all the defined consumes are properly detected
    """
    assert valid_sample.consumes == {"Ticket Association"}


def test_produces_are_parsed(valid_sample):
    """
    this test checks if all the defined produces are properly detected
    """
    assert valid_sample.produces == {"RabbitMQ message", "HTTP API"}


def test_invalid_h2_fails():
    """
    tests if there are invalid title as second level headings. That is:

        # Title

        ## Produces <-- This is ok
        ## Consumes <-- This is also okay
        ## Error    <-- The only allowed 2nd level titles are
                        "produces" and "consumes"
    """
    sample_file = Path("tests/wrongh2.md")

    with pytest.raises(ParserException) as excep:
        Parser(sample_file.absolute())

    assert str(excep.value) == "'ERROR' not allowed as a level two header"


def test_graph_is_correct(valid_sample):
    """
    Checks if the generated graph is of the correct type
    and has the necessary edges
    """
    edges = set(valid_sample.graph.edges())
    assert ("Cashless", "RabbitMQ message") in edges
    assert ("Cashless", "HTTP API") in edges
    assert ("Ticket Association", "Cashless") in edges


def test_parser_adds_graph_description(valid_sample, valid_sample_ast):
    """
    If after the first heading theres a paragraph, its text
    should be add as a 'description' property in the
    generated graph.
    """
    assert "description" in valid_sample.graph.graph

    description = valid_sample.graph.graph["description"]
    expected_description = valid_sample_ast[1]["children"][0]["text"]
    expected_description = (
        f"{expected_description}\n{valid_sample_ast[2]['children'][0]['text']}"
    )
    assert description == expected_description
