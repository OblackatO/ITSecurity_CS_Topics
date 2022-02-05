from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        visited_nodes = []
        queue = []
        queue.append(self)
        visited_nodes.append(self.val)
        while queue:
            current_node = queue.pop(0)
            leaf_node = False
            if current_node.left is None and current_node.right is None:
                leaf_node = True
            if current_node.left:
                queue.append(current_node.left)
                visited_nodes.append(current_node.left.val)
            else:
                if leaf_node is False:
                    visited_nodes.append(None)
            if current_node.right:
                queue.append(current_node.right)
                visited_nodes.append(current_node.right.val)
            else:
                if leaf_node is False:
                    visited_nodes.append(None)
        return visited_nodes

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.val and root.left and root.right:
            temp_left = root.left
            root.left = root.right
            root.right = temp_left
            self.invertTree(root.left)
            self.invertTree(root.right)


if __name__ == '__main__':
    root = TreeNode(
        4,
        left=TreeNode(2,
            left=TreeNode(1),
            #right=TreeNode(3)
        ),
        right=TreeNode(7,
            left=TreeNode(6),
            right=TreeNode(9)
        )
    )
    solution = Solution()
    print(f"Initial tree: {root.printTree()}")
    solution.invertTree(root)
    print(f"Inverted tree: {root.printTree()}")
