from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        index_dict = {}
        for num in nums:
            index_dict[num] = []
        for i, num in enumerate(nums):
            index_dict[num].append(i)
            
        idx = 1
        for num in sorted_nums:
            b = target - num
            while True:
                if sorted_nums[-idx] == b:
                    if num == b:
                        return index_dict[num]
                    else:
                        return [index_dict[num][0], index_dict[sorted_nums[-idx]][0]]
                elif sorted_nums[-idx] > b:
                    idx += 1
                else:
                    break
