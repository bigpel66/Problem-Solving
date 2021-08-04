import sys

def input_action():
    return (ord(sys.stdin.readline().rstrip()))

def output_action(val):
    print(val)

def main():
    val = input_action()
    output_action(val)

main()
