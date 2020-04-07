# https://leetcode.com/problems/decompress-run-length-encoded-list/


class SelfImplement:
    def decompressRLElist(self, nums):
        results = []
        for i in range(0, len(nums), 2):
            results += nums[i]*[nums[i+1]]
        return results

print(SelfImplement().decompressRLElist([1,2,3,4]))