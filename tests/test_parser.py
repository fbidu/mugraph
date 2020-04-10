"""
Unit tests for the Parser module
"""
from pathlib import Path
from mugraph import Parser


def test_root_name_is_detected():
    """
    tests if a the parser can correctly evaluate
    the main microservice's name
    """
    sample_file = Path("tests/sample01.md")
    parser = Parser(sample_file.absolute())
    assert parser.root_name == "Cashless"
