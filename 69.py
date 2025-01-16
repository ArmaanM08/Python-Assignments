import argparse

parser = argparse.ArgumentParser(description="A simple CLI app.")
parser.add_argument("--input", type=str, help="Input file path")
parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")

args = parser.parse_args()

if args.verbose:
    print("Verbose mode enabled.")
if args.input:
    print(f"Input file: {args.input}")