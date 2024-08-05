class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        count = 0
        ans = count

        for num in nums:
            
            # Check if first element because we don't want to run while loops from middle elements (TLE)
            if num-1 not in s:
                count = 1
                while num+1 in s:
                    count += 1
                    num += 1
            else:
                pass
            
            ans = max(ans, count)
        
        return ans

        

if __name__ == "__main__":
    solution = Solution()
    nums = []
    print(solution.longestConsecutive(nums))