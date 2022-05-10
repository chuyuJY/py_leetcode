import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 双队列
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return []
        # 负无穷
        curRes = -float('inf')
        curDeque = collections.deque([root])
        sufDeque = collections.deque([])
        while curDeque:
            cur = curDeque[0]
            if cur:
                if cur.left:
                    sufDeque.append(cur.left)
                if cur.right:
                    sufDeque.append(cur.right)
                curRes = max(curRes, cur.val)
            curDeque.popleft()
            if not curDeque:
                res.append(curRes)
                curRes = -float('inf')
                curDeque = sufDeque
                sufDeque = collections.deque([])
        return res
# 单队列
