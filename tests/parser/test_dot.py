from flowchart.graph import construct_graph


def test_skip_comment():
    with open("tests/fixtures/bulb.flow") as finput:
        lines = finput.readlines()

    actual = construct_graph(lines).to_string()
    assert "Yes" in actual
    assert "NOT" not in actual
    assert "123" not in actual
    assert "---" not in actual
    assert "//" not in actual
