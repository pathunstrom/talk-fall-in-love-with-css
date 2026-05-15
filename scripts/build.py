import typing as t
from dataclasses import dataclass
from pathlib import Path

import dykes

file_order = [
	"Introduction/intro.md",
	"Basics/the-document.md",
	"Basics/structure-of-css.md",
	"Basics/the-cascade.md",
	"Cool-Stuff/root.md",
	"Cool-Stuff/colors.md",
	"Cool-Stuff/custom-properties.md",
	"Cool-Stuff/nested-css.md",
	"Cool-Stuff/layout.md",
	"Cool-Stuff/has.md",
	"Cool-Stuff/media-queries.md"
]

@dataclass
class Builder:
	"""
	Assemble a single script file from collection.
	"""
	root: t.Annotated[Path, "The root of the script files.", dykes.options.Flags("-r", "--root")] = Path(".")
	output: t.Annotated[Path, "Where to drop the finished file.", dykes.options.Flags("-o", "--output")] = Path(".") / "script.md"


def build(root, output_path):
	with output_path.open("w") as output_file:
		for slug in file_order:
			with (root/slug).open() as read_file:
				output_file.writelines(read_file)
	print("Job Done.")


def main():
	arguments = dykes.parse_args(Builder)
	build(arguments.root, arguments.output)

if __name__ == "__main__":
	main()
