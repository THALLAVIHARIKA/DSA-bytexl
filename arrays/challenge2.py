class Solution:
    def findDuplicate(self, nums):
        # start your solution
        tortoise=nums[0]
        hare=nums[0]

        while True:
            tortoise=nums[tortoise]
            hare=nums[nums[hare]]
            if tortoise==hare:
                break
        tortoise=nums[0]
        while tortoise!=hare:
            tortoise=nums[tortoise]
            hare=nums[hare]
        return hare
        # end your solution

def main():
    n = int(input())
    nums = list(map(int, input().split()))

    sol = Solution()
    result = sol.findDuplicate(nums)

    print(result)

if __name__ == "__main__":
    main()