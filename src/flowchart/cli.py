import sys

from flowchart.graph import construct_graph


def main(prog="dot"):
    path = sys.argv[1]
    with open(path) as finput:
        graph = construct_graph(finput.readlines())
        print(graph.to_string())

        graph.write_png(f"{path}.png", prog=prog)
        graph.write_svg(f"{path}.svg", prog=prog)


if __name__ == "__main__":
    main()
