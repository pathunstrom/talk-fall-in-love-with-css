# /// script
# requires-python = ">=3.14"
# dependencies = [
#   "dykes"
# ]
# ///
import dykes
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Annotated

is_word = re.compile(r"[a-zA-Z]")


@dataclass
class WordCounter:
    """
    A simple markdown word counter.
    """
    paths: Annotated[list[Path], "Paths to files to operate on."]
    debugging: Annotated[bool, "Show debugging output."] = False


@dataclass
class FileCount:
    """
    A filename and count.
    """
    file: str
    count: int


type FileCounts = list[FileCount]


def count_files(file_paths: list[Path], debug=False) -> FileCounts:
    return [count_file(file_path, debug) for file_path in file_paths]


def count_file(file_path: Path, debug=False) -> FileCount:
    count = 0
    with open(file_path) as file:
        lines = []
        for line in file:
            count += len(checking := [word for word in line.split() if is_word.findall(word)])
            lines.extend(checking)
        if debug:
            print(f"Words in {file_path}:", lines, sep="\n")
    return FileCount(file=str(file_path), count=count)


def main():
    arguments = dykes.parse_args(WordCounter)
    results = count_files(arguments.paths, arguments.debugging)
    if arguments.debugging:
        print("Results:", results)
    print(f"Total: {sum(result.count for result in results)}", *(f"{fc.file}: {fc.count}" for fc in results), sep="\n\t")


if __name__ == "__main__":
    main()
