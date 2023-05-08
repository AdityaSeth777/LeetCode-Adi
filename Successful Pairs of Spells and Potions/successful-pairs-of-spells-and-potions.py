class Solution(object):
    def successfulPairs(self, spells, potions, success):
        n = len(spells)
        m = len(potions)
        pairs = [0] * n
        potions.sort()
        for i in range(n):
            spell = spells[i]
            left = 0
            right = m - 1
            while left <= right:
                mid = left + (right - left) // 2
                product = spell * potions[mid]
                if product >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            pairs[i] = m - left
        return pairs