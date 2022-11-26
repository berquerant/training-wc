import sys


def main():
    line, word, byte = 0, 0, 0

    for l in sys.stdin:
        line += 1
        byte += len(l.encode())
        word += len(l.split())

    print(line, word, byte)


if __name__ == "__main__":
    main()
