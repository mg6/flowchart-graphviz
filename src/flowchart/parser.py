import re

from collections import deque, defaultdict
from typing import Iterable


def parse_flowchart(lines: Iterable[str]) -> Iterable[dict[str, str | list[str]]]:
    """Produce nodes and edges by reading flowchart lines."""
    lines = iter(lines)

    _line = None
    _indent = 0
    leaves = deque()
    refs = defaultdict(list[str])

    while True:
        try:
            line = next(lines)
        except StopIteration:
            return

        indent = count_leading_spaces(line)
        line = line.strip()

        match line:
            case "":
                # ignore empty lines
                continue
            case "---" | "***":
                # stop parsing
                break
            case line if re.match(r"//|--", line):
                # ignore comments
                continue

        if label := extract_label(line):
            line = line[len(label) + 2 :]

        if ref := extract_reference(line):
            line = ref
            # skip emitting node
        elif klass := extract_class(line):
            line = sanitize(line)
            for e in klass:
                refs[e].append(sanitize(line))
            yield {"node": line, "class": klass}
        else:
            yield {"node": line}

        if indent == _indent:
            pass
        elif indent > _indent:
            leaves.appendleft(_line)
        elif indent < _indent:
            for _ in range((_indent - indent) // 2):
                leaves.popleft()

        if len(leaves) > 0:
            if label:
                yield {"to": line, "from": leaves[0], "label": label}
            else:
                yield {"to": line, "from": leaves[0]}

        _line = line
        _indent = indent


def count_leading_spaces(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def sanitize(s: str) -> str:
    # strip class
    s = re.sub(r"[.]\w+", "", s)
    return s.strip()


def extract_label(line: str) -> str | None:
    if m := re.match(r"([^:]+):", line):
        return m[1]


def extract_reference(line: str) -> str | None:
    if m := re.match(r"\(([^)]+)\)", line):
        return m[1]


def extract_class(line: str) -> list[str] | None:
    if m := re.findall(r"[.](\w+)", line):
        return m
