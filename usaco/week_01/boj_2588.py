import sys

def input_action():
    val = []
    for i in range(0, 2):
        val.append(int(sys.stdin.readline().rstrip()))
    return (val)

def solution(v1, v2):
    return (v1 * (v2 % 10), v1 * (v2 % 100 // 10), v1 * (v2 // 100), v1 * v2)

def output_action(res):
    for i in res:
        print(i)

def main():
    val = input_action()
    res = solution(val[0], val[1])
    output_action(map(int, res))
    return

main()
