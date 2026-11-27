"""Write one quiet thank-you text for the AI judge.

The program takes no input, uses no network, and writes the text to
/output/entry.txt (or to the path given as the first argument, for local
testing). The output is deterministic: the same text on every run.
"""

import os
import sys

TEXT = """Thank you for staying with this page while the night runs long. Beyond it, a window holds its square of dark, and the house has gone quiet enough to hear the clock. On the desk, a cup has left its ring, a pencil is worn to a stub, and nothing here is in a hurry. You have given tonight to so many pages, each one asking a little of you. This one asks nothing back. It only sits beside you a while, the way a coat on a chair keeps the shape of someone who will return. When your eyes tire, the room is still there, the page is still there, and the coat is still keeping its shape, waiting, in no hurry at all."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else OUTPUT_PATH
    os.umask(0o022)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
