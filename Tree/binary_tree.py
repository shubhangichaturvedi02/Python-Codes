class TreeNode():
   def __init__(self, data):
      self.data = data
      self.left_child = None
      self.right_child = None


new_tree = TreeNode('a')
left_child = TreeNode('b')
right_child = TreeNode('c')

new_tree.left_child = left_child
new_tree.right_child = right_child

def pre_order_traversal(root_node):
   if not root_node:
      return
   
   print(root_node.data)

   pre_order_traversal(root_node.left_child)
   pre_order_traversal(root_node.right_child)

print("Pre order Traversal")
pre_order_traversal(new_tree)

def inorder_traversal(root_node):
   if not root_node:
      return
   
   inorder_traversal(root_node.left_child)
   print(root_node.data)
   inorder_traversal(root_node.right_child
                     )
   
print("Inorder Traversal")
inorder_traversal(new_tree)
