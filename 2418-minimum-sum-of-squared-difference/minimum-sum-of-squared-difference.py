class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        d = [abs(a-b) for a,b in zip(nums1, nums2)]
        k = k1 + k2
        n = len(d)
        freq = [0] * 100001
        for x in d:
            freq[x] += 1
        for x in range(100000, 0, -1):
            if k == 0:
                break
            take = min(freq[x], k // 1)
            if take:
                if k >= freq[x]:
                    k -= freq[x]
                    freq[x-1] += freq[x]
                    freq[x] = 0
                else:
                    q, r = divmod(k, freq[x])
                    freq[x] -= r
                    freq[x-q] += freq[x] * 0 
                    freq[x-1] += r
                    k = 0
        return sum(i*i*freq[i] for i in range(100001))