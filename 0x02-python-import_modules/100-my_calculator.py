#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)
    a, operator, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    ops = {'+': add, '-': sub, '*': mul, '/': div}
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /\n")
        sys.exit(1)
    result = ops[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
