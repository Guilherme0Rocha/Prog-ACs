def r(x, y):
    return ((3 * int(x)) ** 2) + (int(y) ** 2)
def b(x, y):
    return (2*(int(x) ** 2)) + ((5 * int(y)) ** 2)
def c(x, y):
    return (-100 * int(x)) + (int(y) ** 3)
def maior(x, y):
    if max(r(x, y), b(x, y), c(x, y)) == r(x,y):
        return "Rafael ganhou"
    elif max(r(x, y), b(x, y), c(x, y)) == b(x, y):
        return "Beto ganhou"
    elif max(r(x, y), b(x, y), c(x, y)) == c(x, y):
        return "Carlos ganhou"

def main():
    num = int(input())
    while num > 0:
        num -=1
        nums = (input()).split(" ")
        x, y = nums[0], nums[1]
        print(maior(x,y))



main()