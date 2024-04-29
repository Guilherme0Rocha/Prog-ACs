def r(x, y):
    ((3 * x) ** 2) + (y ** 2)
def b(x, y):
    (2*(x ** 2)) + ((5 * y) ** 2)
def c(x, y):
    (-100 * x) + (y ** 3)

def main():
    num = int(input())
    while num > 0:
        num -=1
        nums = (input()).split(" ")
        x, y = nums[0], nums[1]
        print(max(r(x, y), b(x, y), c(x, y)))



main()