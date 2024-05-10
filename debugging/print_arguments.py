#!/usr/bin/python3
import sys

for i in range(1, len(sys.argv)):  # 从1开始，跳过脚本名称
    print(sys.argv[i])
