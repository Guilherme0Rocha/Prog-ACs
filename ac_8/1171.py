def main():
    num = int(input())
    nums = []
    for i in range(num):
        elementos = int(input())
        nums.append(elementos)

    nums.sort()
    while nums != []:
        num = nums.count(nums[0])
        print("{} aparece {} vez(es)".format(nums[0], num))
        for i in range(num):
            nums.remove(nums[0])


main()