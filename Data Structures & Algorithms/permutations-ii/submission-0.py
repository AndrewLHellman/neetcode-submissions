class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        perms = [[]]
        for num in nums:
            seen = set()
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, num)
                    new_perm = tuple(perm_copy)
                    if new_perm not in seen:
                        new_perms.append(perm_copy)
                        seen.add(new_perm)
            perms = new_perms
        
        return perms