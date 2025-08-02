import sys

from flowchart.graph import construct_graph


def main():
    for path in sys.argv[1:]:
        process(path)


def process(path: str):
    with open(path) as finput:
        input = finput.readlines()

    graph = construct_graph(input)
    print(graph.to_string())

    graph.write_png(f"{path}.png")
    graph.write_svg(f"{path}.svg")


if __name__ == "__main__":
    main()
