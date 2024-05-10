#!/usr/bin/python3
import sys


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        print(f"{result} = {result // n} * {n}")  # 打印每一步的计算过程
        n = n - 1
    return result


if len(sys.argv) > 1:  # 确保有命令行参数输入
    try:
        f = factorial(int(sys.argv[1]))
        print(f"The factorial is {f}")
    except ValueError:
        print("Please enter a valid integer.")
else:
    print("Please provide an integer as an argument.")
