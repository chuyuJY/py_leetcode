import bisect
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        from sortedcontainers import SortedList
        st = SortedList()
        left, right = 0, 0
        while right < len(nums):
            # 窗口收缩
            # 此时其实right
            if right - left > k:
                st.remove(nums[left])
                left += 1
            st.add(nums[right])
            index = bisect.bisect_left(st, nums[right])
            # SortedList:已存在的元素，不会添加
            if index < len(st)-1 and abs(st[index+1]-st[index]) <= t:
                return True
            if index > 0 and abs(st[index]-st[index-1]) <= t:
                return True
            # 窗口右移
            right += 1
        return False


if __name__ == '__main__':
    test = Solution()
    list = [1, 2, 3, 1]
    print(test.containsNearbyAlmostDuplicate(list, 3, 0))
