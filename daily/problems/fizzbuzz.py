import argparse


def fizzbuzz(a: int):
    printstr = ""
    if a % 3 == 0:
        printstr = "Fizz"
    if a % 5 == 0:
        printstr += "Buzz"
    print(f"{printstr}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=int, help="Input value to fizzbuzz")
    args = parser.parse_args()
    fizzbuzz(args.input)
