import math

def main():
    while True:
        try:
            nums = input().split()
            m, n = int(nums[0]), int(nums[1])
            print(math.factorial(m) + math.factorial(n))
        except EOFError:
            break

main()