class Solution:
    def sortArrayByParity(self, nums):
        # start your solution
        left = 0
        right = len(nums) - 1

        while left < right:
            # find odd from left
            while left < right and nums[left] % 2 == 0:
                left += 1
            # find even from right
            while left < right and nums[right] % 2 == 1:
                right -= 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums
        # end your solution

def main():
    n = int(input())
    nums = list(map(int, input().split()))

    sol = Solution()
    result = sol.sortArrayByParity(nums)

    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()