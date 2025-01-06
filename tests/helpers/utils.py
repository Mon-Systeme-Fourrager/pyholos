def assert_is_ascending(values: list | tuple) -> bool:
    """Asserts that a vector of numeric values follows an ascending trend

    Args:
        values: values whose trend is to be checked
    """
    return all([x <= y for x, y in zip(values, values[1:])])

def assert_is_descending(values: list | tuple) -> bool:
    """Asserts that a vector of numeric values follows a descending trend

    Args:
        values: values whose trend is to be checked
    """
    return all([x >= y for x, y in zip(values, values[1:])])