class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = root.val
        def dfs(root: TreeNode) -> int:
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            self.res = max(self.res, leftMax + root.val + rightMax)
            outputMax = root.val + max(leftMax, rightMax)
            return max(outputMax, 0)
        dfs(root)
        return self.res



if __name__ == '__main__':
    def test1():
        a = 2
        test2(a)
    def test2(a: int):
        test3(a)
        print(a)
        test3(a)
        print(a)
    def test3(a: int):
        a -= 1
    print(test1())