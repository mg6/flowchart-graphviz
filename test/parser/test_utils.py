from flowchart.parser import extract_reference


def test_is_reference():
    line = "(Node A)"
    assert extract_reference(line) == "Node A"
