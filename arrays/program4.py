class Solution:
    def plusOne(self, digits):
        # start your solution
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        # if we are here, it means all were 9: e.g. 999 -> 1000
        return [1] + [0] * n
        # end your solution

def main():
    n = int(input())
    digits = list(map(int, input().split()))

    sol = Solution()
    result = sol.plusOne(digits)

    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()