import pytest
from app import sanitize_input

def test_sanitize_input():
    assert sanitize_input("someinput") == 'sanitized'
    assert sanitize_input("input with ' SQL") == 'unsanitized'
    assert sanitize_input("input with ; SQL") == 'unsanitized'
    assert sanitize_input("input with \" SQL") == 'unsanitized'
    assert sanitize_input("input with \\ SQL") == 'unsanitized'
    assert sanitize_input("input with $ SQL") == 'unsanitized'
    assert sanitize_input("input with % SQL") == 'unsanitized'
    assert sanitize_input("input with & SQL") == 'unsanitized'
    assert sanitize_input("input with # SQL") == 'unsanitized'
    assert sanitize_input("input with * SQL") == 'unsanitized'
    assert sanitize_input("input with ( SQL") == 'unsanitized'
    assert sanitize_input("input with ) SQL") == 'unsanitized'
    assert sanitize_input("input with [ SQL") == 'unsanitized'
    assert sanitize_input("input with ] SQL") == 'unsanitized'
    assert sanitize_input("input with { SQL") == 'unsanitized'
    assert sanitize_input("input with } SQL") == 'unsanitized'
    assert sanitize_input("input with | SQL") == 'unsanitized'
    assert sanitize_input("input with ` SQL") == 'unsanitized'
    assert sanitize_input("input with < SQL") == 'unsanitized'
    assert sanitize_input("input with > SQL") == 'unsanitized'
    assert sanitize_input("input with ? SQL") == 'unsanitized'
    assert sanitize_input("input with + SQL") == 'unsanitized'
    assert sanitize_input("input with - SQL") == 'sanitized'
    assert sanitize_input("") == 'sanitized'
    assert sanitize_input("    ") == 'sanitized'
    assert sanitize_input("Alphanumeric123") == 'sanitized'
    assert sanitize_input("!@#$%^&*()_-+=<>?/") == 'unsanitized'
    assert sanitize_input("abc@123") == 'unsanitized'
    assert sanitize_input("a" * 1000) == 'sanitized'
    assert sanitize_input("input with ' and ; SQL") == 'unsanitized'
    assert sanitize_input("123@456") == 'unsanitized'
    assert sanitize_input("!abc123") == 'unsanitized'
    assert sanitize_input("def456#") == 'unsanitized'







if __name__ == '__main__':
    pytest.main()