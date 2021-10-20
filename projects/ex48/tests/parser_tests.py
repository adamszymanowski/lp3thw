from nose.tools import *
from ex48.parser import *
from ex48.lexicon import scan

tokens_1 = scan("go in the from")
tokens_2 = scan("bear kill bear")
tokens_3 = scan("in of the drum")


def test_parse_subject():
    assert_equal(parse_subject(tokens_1)[1], "player")
    assert_equal(parse_subject(tokens_2)[1], "bear")
    assert_raises(ParserError, parse_subject, tokens_3)

def test_parse_verb():
    assert_equal(parse_verb(tokens_1)[1], "go")
    assert_equal(parse_verb(tokens_2)[1], "kill")
    assert_raises(ParserError, parse_verb, tokens_3)

def test_parse_object():
    assert_equal(parse_object(tokens_2)[1], "bear")
    assert_raises(ParserError, parse_object, tokens_3)

def test_parse_sentence():
    sentence = parse_sentence(scan("go north"))
    assert_equal(sentence.subject, "player")
    assert_equal(sentence.verb, "go")
    assert_equal(sentence.object, "north")