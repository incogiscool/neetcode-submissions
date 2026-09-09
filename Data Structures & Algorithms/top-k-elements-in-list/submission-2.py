class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Loop through, count the nums in a hashmap with key as the num and val as count
        # make arr of size k and find k largest numbers

        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        items = list(counts.items())

        items.sort(key=lambda x: x[1], reverse=True)
        
        ans = []

        for i in range(k):
            ans.append(items[i][0])

        return ans






        