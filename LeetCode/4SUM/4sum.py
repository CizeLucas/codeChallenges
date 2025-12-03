from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #nums[i] + nums[j] + nums[lower] + nums[upper] == target
        
        result = []
        n = len(nums)
        nums.sort()
        print(nums)
        nSum = 4
        currQuadruplet = []

        self.recursive(nums, target, nSum, 0, currQuadruplet, result)

        print(result)
        return result

    #startingIndex is INCLUSIVE
    def recursive(self, sortedNums: List[int], target: int, k: int, startingIndex: int, currQuadruplet: List[int], result: List[List[int]]):
        if(k != 2):
            for index in range(startingIndex, len(sortedNums)):
                if(index > startingIndex and sortedNums[index] == sortedNums[index-1]):
                    continue
                
                currQuadruplet.append(sortedNums[index])
                self.recursive(sortedNums, (target - sortedNums[index]), k-1, index+1, currQuadruplet, result)
                currQuadruplet.pop()
            return

        # base case
        low, high = startingIndex, len(sortedNums)-1
        while(low < high):
            currSum = sortedNums[low] + sortedNums[high]
            if(currSum > target):
                high-=1
            elif(currSum < target):
                low+=1
            else: #currSum == target
                result.append(currQuadruplet + [sortedNums[low], sortedNums[high]])
                low+=1
                high-=1
                while(low < high and sortedNums[low] == sortedNums[low-1]):
                    low+=1
                while(low < high and sortedNums[high] == sortedNums[high+1]):
                    high-=1
            

sol = Solution()
sol.fourSum([1,0,-1,0,-2,2], 0)