import sys

def input_action():
    return (int(sys.stdin.readline().rstrip()))

def solution(iter):
    res = []
    for i in range(0, iter):
        a, b = map(int, sys.stdin.readline().split())
        res.append(a + b)
    return (res)

def output_action(res):
    for i in res:
        print(i)

def main():
    iter = input_action()
    res = solution(iter)
    output_action(res)

main()
