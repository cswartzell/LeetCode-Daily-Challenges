#I like that this is forcing you to really show if you understand what the
#ordering means and how they are derived:
#inorder means All the way down lefts, up one and return (repeat), go right, but only return if no lefts
#preorder means Current Node, all the way down lefts, all down rights, back up to parent
#Wait... Im confused on the listed output. Its just listed in BFS order. I can just
#do BFS on the inorder list and ignore the preorder list right?
#Nope. need to read the problem. The args as simple lists, not list of nodes
#All we have is the value for the nodes in the btree, we must derive the
#structure of the tree from differences in the two lists

#hmm... we know the values are unique. How can we work with that...

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if not preorder:
#             return none         #so this can be reversed to just if preorder: with a failure having no return value, meaning return None

#         #build the current node
#         root = TreeNode(preorder[0])

#         #find the inorder[index] that matches the preorder[preorder_root_index]
#         inorder_idx = 0
#         while inorder[inorder_idx] != preorder[0]:
#             inorder_idx += 1

#         root.left = self.buildTree(preorder[1:], inorder[:inorder_idx])
#         root.right = self.buildTree(preorder[1 + len(inorder[:inorder_idx]):], inorder[inorder_idx+1:])

#         return root

        
        
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:    
        
        
        
        
        
        def arr_to_tree(preorder_idx, sublist):
            #return if empty
            if not sublist:
                return None
            
            #build the current node, using the preorder_idx to find the val
            root = TreeNode(preorder[preorder_idx])
            
            #find the inorder[index] that matches the preorder[preorder_root_index]
            inorder_idx = 0
            while sublist[inorder_idx] != preorder[preorder_idx]:
                inorder_idx += 1
            
            #slice our current array into parts
            #left is everything to the left of the root val, as found in the last step
            #right is everything to the right of the same
            left_subarray = sublist[:inorder_idx]
            right_subarray = sublist[inorder_idx+1:]
            
            #For the left half, use the very next preorder_idx as the root, and pass the left subarray
            root.left = arr_to_tree(preorder_idx + 1, left_subarray)
            #For the right half, the preorder_idx is the next element AFTER all of the ones being used in the left half
            # as there are len(left) elements in the left half, the right index is the current preorder_idx+1+len(left)
            root.right = arr_to_tree(preorder_idx + 1 + len(left_subarray), right_subarray)
            
            return root
        
        #We know the "next" value of pre-order will be the root for the given subtree
        #We start by calling our helper function, telling it the first root is preorder[0] 
        #and pass the whole array as the first "sub_tree" to our recursive function.
        #It will return the built tree each time, and here will return the final answer
        return arr_to_tree(0, inorder)
        
        
        
        
#         #Ok, starting over, following the solution.
        
#         def arr_to_tree(left, right):
#             nonlocal pre_idx
#             if left > right:
#                 return None
#             root_val = preorder[pre_idx]
#             root = TreeNode(root_val)                   
                               
#             pre_idx += 1
            
#             root.left = arr_to_tree(left, ino_dict[root_val]-1)
#             root.right = arr_to_tree(ino_dict[root_val]+1, right)
            
#             return root
        
#         #We know the vals are unique, so rather than iterating through the inorder
#         #list on each recursion to find the index of the root (from preorder)
#         #lets just hash it now:
        
#         #Hey look, a neat trick for dictionary comprehension
#         ino_dict = {key:value for (key, value) in enumerate(inorder)}
                                  
#         pre_idx = 0  
#         return arr_to_tree(pre_idx,len(preorder)-1)
        
        #Quick test, what happens in slicing when given args out of range?
        #Nice, it doesnt give a shit. A slice out of range is merely empty
        #Instead of throwing an error. No need to list[max(len,what_wewant):]
        # test_list = [1,2,3,4,5,6]
        # left = test_list[0:4]
        # right = test_list[9:]
        # pass
        
        
        
        
        #garbage garbage garbage....
        #         #base case
#         if len(preorder) == 1:
#             return TreeNode(preorder[0])
        
#         #may be useful, otherwise delete
#         inorder = deque(inorder)
#         preorder = deque(preorder)
        
#         #We can use the first element of inorder as the root of our tree 
#         bstack = [preorder[0]]
        
#         pre_idx = 0
#         left_tree = deque()
#         right_tree = deque()    
        
#         def split( pre_idx, left_tree, right_tree)):
#             ino_idx = 0    
#             #until we reach the current node in inorder, everything will be left forks in preorder
#             while left_tree[ino_idx] != preorder[pre_idx]:
#                 ino_idx += 1
#             left_tree = left_tree[:ino_idx]
#             right_tree = 
#         split(0, preorder, right_tree)
        
#         #Now actually build it        
#         # btree = TreeNode()
#         # curr_node = btree
