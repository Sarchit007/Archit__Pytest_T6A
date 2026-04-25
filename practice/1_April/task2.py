"""
TASK 2: Pytest Markers Practice

Create 2 custom markers:
@pytest.mark.smoke
@pytest.mark.regression
Write:
2 test cases for smoke
2 test cases for regression
Each test should:
Contain a simple assertion
Run tests using:
Only smoke tests
Only regression tests
"""

import pytest

# Smoke
@pytest.mark.smoke
def test_number():
    assert 8 > 7, "Less than"


@pytest.mark.smoke
def test_string():
    assert 7 != 9, "Check it Again"


# Regression
@pytest.mark.regression
def test_comparison():
    assert 45 >= 33 , "Not greater than"


@pytest.mark.regression
def test_membership():
    l = ['23', '56', '78']
    assert '54' not in l, 'In the List'