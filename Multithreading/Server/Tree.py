'''class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.k = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=' ')
        inorder(root.right)

def vertical(root):
    try:
        print(root.val, root.k)
        root.left.k = root.k - 1
        root.right.k = root.k + 1
        vertical(root.left)
        vertical(root.right)
    except:
        pass
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.right.left = TreeNode(6)
t.right.right = TreeNode(7)
inorder(t)
print()
t.k = 0
vertical(t)'''

# Definition for a binary tree node.
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.k = None

class Solution:
    def __init__(self):
        self.k_value = {}

    def vertical(self, root):
        try:
            if root.k in self.k_value:
                self.k_value[root.k].append(root.val)
            else:
                self.k_value[root.k] = [root.val]
            #print(root.left.k, root.right.k)
            if root.left:
                root.left.k = root.k - 1
            if root.right:
                root.right.k = root.k + 1
            self.vertical(root.left)
            self.vertical(root.right)
        except:
            pass

    def verticalTraversal(self, root):
        root.k = 0
        self.vertical(root)
        ans = []
        #print(self.k_value)
        for i in sorted(self.k_value):
            ans.append(self.k_value[i])
        return ans
t = TreeNode(0)
t.right = TreeNode(1)
s = Solution()
print('Ans =',s.verticalTraversal(t))

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.k = None


class Solution:
    def __init__(self):
        self.k_value = {}

    def vertical(self, root):
        try:
            if root.k in self.k_value:
                self.k_value[root.k].append(root.val)
            else:
                self.k_value[root.k] = [root.val]
            if root.left:
                root.left.k = root.k - 1
            if root.right:
                root.right.k = root.k + 1
            self.vertical(root.left)
            self.vertical(root.right)
        except:
            pass

    def verticalTraversal(self, root):
        root.k = 0
        self.vertical(root)
        ans = []
        # print(self.k_value)
        for i in sorted(self.k_value):
            ans.append(sorted(self.k_value[i]))
        return ans
