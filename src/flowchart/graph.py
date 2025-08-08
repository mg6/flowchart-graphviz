import pydot

from flowchart.parser import parse_flowchart


def construct_graph(lines: list[str], **kwargs) -> pydot.Dot:
    """Construct graph from parsed nodes and edges."""

    graph = pydot.Dot("G", **kwargs)

    for e in parse_flowchart(lines):
        match e:
            case {"node": name, **kwargs}:
                if "class" in kwargs:
                    kwargs["class"] = ",".join(kwargs["class"])
                node = pydot.Node(name, **kwargs)
                graph.add_node(node)

            case {"to": _to, "from": _from, **kwargs}:
                graph.add_edge(pydot.Edge(_from, _to, **kwargs))

            case other:
                raise ValueError(f"Unknown operation: {other}")

    return graph
