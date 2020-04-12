
# https://leetcode.com/problems/maximum-subarray/
class Solution():
    def maxSubArray(self, list_num):
        if len(list_num) == 1: return list_num[0]

        prev_max_result = [list_num[0]]
        for idx, num in enumerate(list_num[1:], start=1):
            prev_max_result.append(max(num, num+prev_max_result[idx-1]))
        return max(prev_max_result)

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print('-'*50)
print(Solution().maxSubArray([-1,-1,-2,-2]))
print('-'*50)
print(Solution().maxSubArray([-2, -1]))
print('-'*50)
print(Solution().maxSubArray([3, -3, 2, -3]))
print('-'*50)
print(Solution().maxSubArray([8,-19,5,-4,20]))
print('-'*50)




class SelfImplement():
    def maxSubArray(self, list_num):
        start_idx = 0
        end_idx = 0
        prev_sum = 0
        max_sum = -10000
        if max(list_num) <= 0: return max(list_num)
        for idx, num in enumerate(list_num):
            if (num > 0 and prev_sum < 0 and num > max_sum) or (idx == 0 and num > 0) : # reset chain
                start_idx = idx
                end_idx = idx
                prev_sum = num
                max_sum = prev_sum
            elif num > 0 and prev_sum > 0:
                prev_sum += num
                if prev_sum > max_sum:
                    end_idx = idx
                max_sum = prev_sum
            elif (num < 0):
                prev_sum += num
            print(f'num {num} prev sum {prev_sum} max sum {max_sum} start {start_idx} end {end_idx}')
        return sum(list_num[start_idx:end_idx+1])



