"""
Unit tests for the Parser module
"""
from pathlib import Path
import pytest

from mugraph import Parser, ParserException


def test_root_name_is_detected():
    """
    tests if a the parser can correctly evaluate
    the main microservice's name
    """
    sample_file = Path("tests/sample01.md")
    parser = Parser(sample_file.absolute())
    assert parser.root_name == "Cashless"


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


def test_consumes_are_parsed():
    """
    this test checks if all the defined consumes are properly detected
    """
    sample_file = Path("tests/sample01.md")
    parser = Parser(sample_file.absolute())
    assert parser.consumes == {"Ticket Association"}


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
