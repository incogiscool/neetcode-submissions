class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Loop through, count the nums in a hashmap with key as the num and val as count
        # make arr of size k and find k largest numbers

        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        sorted_dict = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_dict.keys())[0:k]





        