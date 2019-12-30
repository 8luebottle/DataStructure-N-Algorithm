class TreeNode:
    def __init__(self, x):
        self.val   = x
        self.left  = None
        self.right = None

class Solution:
    def get_min_difference(self, TreeNode):
        output = []
        self.in_order_traversal(root, output)
        min_abs = float('inf')

        for i in range(l, len(output)):
            min_abs = min(min_abs, output[i] - output[i-1])
        return min_abs
    
    def in_order_traversal(self, root, output):
        if root == None:
            return # Nothing
        else:
            self.in_order_traversal(root.left, output)
            output.append(root.val)
            self.in_order_traversal(root.right, output)
