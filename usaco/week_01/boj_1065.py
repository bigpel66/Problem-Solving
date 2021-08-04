import sys

def input_action():
    iter = int(sys.stdin.readline())
    return (iter)

def solution(iter):
    cnt = 0
    for i in range(iter):
        if i + 1 < 100:
            cnt += 1
        else:
            digit = list(map(int, str(i + 1)))
            if digit[0] - digit[1] == digit[1] - digit[2]:
                cnt += 1
    return (cnt)

def output_action(cnt):
    sys.stdout.write(str(cnt))

def main():
    iter = input_action()
    cnt = solution(iter)
    output_action(cnt)

main()
