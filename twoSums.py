class SelfImplement:
    def build_pair_num_idx(self, nums):
        self.dict_index = {}
        for idx, num in enumerate(nums):
            self.dict_index[num] = idx

    def twoSum(self, nums, target):
        pair_idx_num = [(idx, num) for (idx, num) in enumerate(nums)]
        sorted_pair = sorted(pair_idx_num, key = lambda x: x[1])

        for current_idx, (origin_idx, first_num) in enumerate(sorted_pair):
            result_idx = []
            result_idx.append(origin_idx)
            tmp_target = target
            tmp_target -= first_num
            for origin_second_idx, second_num in sorted_pair[current_idx+1:]:
                if tmp_target == second_num:
                    result_idx.append(origin_second_idx)
                    return result_idx

class Solution:
    def twoSum(self, nums, target):
        dict_index = {}
        for idx, num in enumerate(nums):
            remain = target - num
            if remain in dict_index:
                return [idx, dict_index[remain]]
            else:
                dict_index[num] = idx


nums = [2,7,11,15]
targets = 9
print(Solution().twoSum(nums, targets))