import sys

def input_action():
    list = [0] * 10000
    return (list)

def comb(i):
    sum = i
    while i:
        sum += i % 10
        i = i // 10
    return (sum)

def solution(list):
    for i in range(10000):
        val = comb(i + 1)
        if val <= 10000:
            list[val - 1] += 1

def output_action(list):
    for i in range(10000):
        if not list[i]:
            sys.stdout.write(str(i + 1) + '\n')

def main():
    list = input_action()
    solution(list)
    output_action(list)

main()
