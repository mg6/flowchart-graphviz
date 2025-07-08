from flowchart.parser import parse_flowchart


def test_orgchart():
    with open("test/fixtures/orgchart.flow") as finput:
        lines = iter(finput.readlines())

    actual = list(parse_flowchart(lines))
    expected = [
        #
        {"node": "Sarah Chen"},
        ##
        {"node": "Robert Wilson"},
        {"to": "Robert Wilson", "from": "Sarah Chen"},
        ###
        {"node": "David Brown"},
        {"to": "David Brown", "from": "Robert Wilson"},
        ####
        {"node": "Jennifer Lee"},
        {"to": "Jennifer Lee", "from": "David Brown"},
        #####
        {"node": "Andrew Miller"},
        {"to": "Andrew Miller", "from": "Jennifer Lee"},
        #####
        {"node": "Carrie Richards"},
        {"to": "Carrie Richards", "from": "Jennifer Lee"},
        ######
        {"node": "Terry Peralta"},
        {"to": "Terry Peralta", "from": "Carrie Richards"},
        ##
        {"node": "Lisa Anderson"},
        {"to": "Lisa Anderson", "from": "Sarah Chen"},
        ###
        {"node": "Camille Mitchell"},
        {"to": "Camille Mitchell", "from": "Lisa Anderson"},
        ####
        {"node": "Christopher White"},
        {"to": "Christopher White", "from": "Camille Mitchell"},
    ]

    assert actual == expected
