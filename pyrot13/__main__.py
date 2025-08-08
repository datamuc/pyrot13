import sys

from pyrot13 import rot13


def main() -> None:
    while chunk := sys.stdin.read(4096):
        sys.stdout.write(rot13(chunk))


if __name__ == "__main__":
    main()
