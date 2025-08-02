from flowchart.parser import parse_flowchart


def test_simple():
    with open("tests/fixtures/simple.flow") as finput:
        lines = iter(finput.readlines())

    actual = list(parse_flowchart(lines))
    expected = [
        #
        {"node": "Node A"},
        ##
        {"node": "Node B"},
        {"to": "Node B", "from": "Node A", "label": "goes to"},
        ##
        {"node": "Node C"},
        {"to": "Node C", "from": "Node A", "label": "and"},
        ###
        {"to": "Node A", "from": "Node C", "label": "goes back to"},
    ]

    assert actual == expected
