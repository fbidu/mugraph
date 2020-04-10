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


def test_double_root_failes():
    """
    tests if the parser fails when processing a file
    with two headers
    """
    sample_file = Path("tests/doubleh1.md")

    with pytest.raises(ParserException) as excep:
        Parser(sample_file.absolute())
        assert excep.value == "Duplicated header"
