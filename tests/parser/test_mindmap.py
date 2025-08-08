from flowchart.parser import parse_flowchart


def test_mindmap():
    with open("tests/fixtures/mindmap.flow") as finput:
        lines = iter(finput.readlines())

    actual = list(parse_flowchart(lines))
    expected = [
        #
        {"node": "Mind Mapping", "class": ["size_lg"]},
        ##
        {"node": "Learning Style", "class": ["color_blue"]},
        {"to": "Learning Style", "from": "Mind Mapping"},
        ###
        {"node": "Read", "class": ["color_blue"]},
        {"to": "Read", "from": "Learning Style"},
        {"node": "Listen", "class": ["color_blue"]},
        {"to": "Listen", "from": "Learning Style"},
        {"node": "Summarize", "class": ["color_blue"]},
        {"to": "Summarize", "from": "Learning Style"},
        ##
        {"node": "Motivation", "class": ["color_orange"]},
        {"to": "Motivation", "from": "Mind Mapping"},
        ###
        {"node": "Tips", "class": ["color_orange"]},
        {"to": "Tips", "from": "Motivation"},
        {"node": "Roadmap", "class": ["color_orange"]},
        {"to": "Roadmap", "from": "Motivation"},
        ##
        {"node": "Review", "class": ["color_green"]},
        {"to": "Review", "from": "Mind Mapping"},
        ###
        {"node": "Notes", "class": ["color_green"]},
        {"to": "Notes", "from": "Review"},
        {"node": "Method", "class": ["color_green"]},
        {"to": "Method", "from": "Review"},
        {"node": "Discuss", "class": ["color_green"]},
        {"to": "Discuss", "from": "Review"},
    ]

    assert actual == expected
