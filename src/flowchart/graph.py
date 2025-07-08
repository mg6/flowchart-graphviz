import pydot

from flowchart.parser import parse_flowchart


def construct_graph(lines: list[str], **kwargs) -> pydot.Dot:
    """Construct graph from parsed nodes and edges."""

    graph = pydot.Dot("G", **kwargs)

    for e in parse_flowchart(iter(lines)):
        match e:
            case {"node": name}:
                node = pydot.Node(name)
                graph.add_node(node)
            case {"to": _to, "from": _from, "label": label}:
                graph.add_edge(pydot.Edge(_from, _to, label=label))
            case {"to": _to, "from": _from}:
                graph.add_edge(pydot.Edge(_from, _to))
            case other:
                raise ValueError(f"Unknown operation: {other}")

    return graph
