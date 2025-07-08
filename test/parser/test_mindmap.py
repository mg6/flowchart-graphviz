from flowchart.parser import parse_flowchart


def test_mindmap():
    with open("test/fixtures/mindmap.flow") as finput:
        lines = iter(finput.readlines())

    actual = list(parse_flowchart(lines))
    expected = [
        #
        {"node": "Mind Mapping"},
        ##
        {"node": "Learning Style"},
        {"to": "Learning Style", "from": "Mind Mapping"},
        ###
        {"node": "Read"},
        {"to": "Read", "from": "Learning Style"},
        {"node": "Listen"},
        {"to": "Listen", "from": "Learning Style"},
        {"node": "Summarize"},
        {"to": "Summarize", "from": "Learning Style"},
        ##
        {"node": "Motivation"},
        {"to": "Motivation", "from": "Mind Mapping"},
        ###
        {"node": "Tips"},
        {"to": "Tips", "from": "Motivation"},
        {"node": "Roadmap"},
        {"to": "Roadmap", "from": "Motivation"},
        ##
        {"node": "Review"},
        {"to": "Review", "from": "Mind Mapping"},
        ###
        {"node": "Notes"},
        {"to": "Notes", "from": "Review"},
        {"node": "Method"},
        {"to": "Method", "from": "Review"},
        {"node": "Discuss"},
        {"to": "Discuss", "from": "Review"},
    ]

    assert actual == expected
