import sys

def input_action():
    return (map(int, sys.stdin.readline().split()))

def output_action(a, b):
    print(a + b, a - b, a * b, a // b, a % b, sep = '\n')

def main():
    a, b = input_action()
    output_action(a, b)

main()
