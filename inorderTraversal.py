from typing import Optional, TreeNode

class Solution:
        def inorderTraversal(self, root: Optional[TreeNode]):
            result = []
            def traverse(node):
                  if node:
                        traverse(node.left)
                        result.append(node.val)
                        traverse(node.right)
            traverse(root)
            return result
            