import pytest

from flowchart.parser import parse_flowchart


def test_bulb():
    with open("tests/fixtures/bulb.flow") as finput:
        lines = iter(finput.readlines())

    actual = list(parse_flowchart(lines))
    expected = [
        #
        {"node": "Lamp doesn't work"},
        ##
        {"node": "Lamp plugged in", "class": ["diamond"]},
        {"to": "Lamp plugged in", "from": "Lamp doesn't work"},
        ###
        {"node": "Plug in lamp"},
        {"to": "Plug in lamp", "from": "Lamp plugged in", "label": "No"},
        ###
        {"node": "Bulb burned out?", "class": ["diamond"]},
        {"to": "Bulb burned out?", "from": "Lamp plugged in", "label": "Yes"},
        ####
        {"node": "Replace bulb"},
        {"to": "Replace bulb", "from": "Bulb burned out?", "label": "Yes"},
        ####
        {"node": "Repair lamp"},
        {"to": "Repair lamp", "from": "Bulb burned out?", "label": "No"},
    ]

    assert actual == expected
