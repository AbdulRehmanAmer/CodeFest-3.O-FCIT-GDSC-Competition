def sol(nums):
    nums = list(set(nums))
    nums.sort()

    nums.pop()
    if nums: return nums[-1]
    return "NO"
    
if __name__ == "__main__":
    n = input()
    nums = [int(x) for x in input().split()]
    
    print (sol(nums))
    