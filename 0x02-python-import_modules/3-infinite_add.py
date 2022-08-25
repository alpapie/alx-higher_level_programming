#!/usr/bin/python3
if __name__ == "__main__":
        import sys
args_list = sys.argv[1:]
sum_argv = 0
for arg in args_list:
    sum_argv += int(arg)
print(sum_argv)
