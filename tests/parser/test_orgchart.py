from flowchart.parser import parse_flowchart


def test_orgchart():
    with open("tests/fixtures/orgchart.flow") as finput:
        lines = iter(finput.readlines())

    actual = list(parse_flowchart(lines))
    expected = [
        #
        {"node": "Sarah Chen", "class": ["size_lg", "color_black"]},
        ##
        {"node": "Robert Wilson", "class": ["color_blue"]},
        {"to": "Robert Wilson", "from": "Sarah Chen"},
        ###
        {"node": "David Brown"},
        {"to": "David Brown", "from": "Robert Wilson"},
        ####
        {"node": "Jennifer Lee"},
        {"to": "Jennifer Lee", "from": "David Brown"},
        #####
        {"node": "Andrew Miller", "class": ["color_green"]},
        {"to": "Andrew Miller", "from": "Jennifer Lee"},
        #####
        {"node": "Carrie Richards", "class": ["color_green"]},
        {"to": "Carrie Richards", "from": "Jennifer Lee"},
        ######
        {"node": "Terry Peralta", "class": ["color_green"]},
        {"to": "Terry Peralta", "from": "Carrie Richards"},
        ##
        {"node": "Lisa Anderson", "class": ["color_purple"]},
        {"to": "Lisa Anderson", "from": "Sarah Chen"},
        ###
        {"node": "Camille Mitchell", "class": ["color_purple"]},
        {"to": "Camille Mitchell", "from": "Lisa Anderson"},
        ####
        {"node": "Christopher White", "class": ["color_purple"]},
        {"to": "Christopher White", "from": "Camille Mitchell"},
    ]

    assert actual == expected
