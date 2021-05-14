nums = {}

n, p, q = map(int, input().split())


def test(x):
    if x == 0:
        return 1
    if x in nums.keys():
        return nums[x]
    nums[x] = test(x // p) + test(x // q)
    return test(x)


print(test(n))
