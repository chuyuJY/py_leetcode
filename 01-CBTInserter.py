import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        # 定义两个双端队列
        # 一个存储当前行
        # 一个存储下一行
        self.curDeque = collections.deque([self.root])
        self.sufDeque = collections.deque([])
        # 把子节点已满的cur节点给去除
        while self.curDeque:
            cur = self.curDeque[0]
            # 找到不满的节点，就可以退出了
            if not cur.left:
                break
            elif not cur.right:
                self.sufDeque.append(cur.left)
                break
            else:
                # 删除首个节点
                self.curDeque.popleft()
                self.sufDeque.append(cur.left)
                self.sufDeque.append(cur.right)
                # 若cur节点全都是满的，那么往下
                if not self.curDeque:
                    self.curDeque = self.sufDeque
                    self.sufDeque = collections.deque([])

    def insert(self, val: int) -> int:
        cur = self.curDeque[0]
        if not cur.left:
            cur.left = TreeNode(val=val)
            self.sufDeque.append(cur.left)
        else:
            cur.right = TreeNode(val=val)
            self.sufDeque.append(cur.right)
            self.curDeque.popleft()
            if not self.curDeque:
                self.curDeque = self.sufDeque
                self.sufDeque = collections.deque([])
        return cur.val

    def get_root(self) -> TreeNode:
        return self.root