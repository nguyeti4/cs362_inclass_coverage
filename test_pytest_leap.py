import pytest
import leap2


def test_leap():
    actual = leap2.leap("500")
    expected = "500 is not a leap year"
    assert actual==expected
def test_leap2():
    actual = leap2.leap("400")
    expected = "400 is a leap year"
    assert actual==expected
def test_leap3():
    actual = leap2.leap("-100")
    expected = "error: input needs to be a POSITIVE int"
    assert actual==expected