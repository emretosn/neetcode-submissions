# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        one, two = deque(), deque()
        one.append(p)
        two.append(q)

        while one:
            for _ in range(len(one)):
                no = one.popleft()
                nt = two.popleft()
                if not no and not nt:
                    continue
                elif no is None or nt is None:
                    return False
                elif no.val != nt.val:
                    return False
                
                one.append(no.left)
                one.append(no.right)
                
                two.append(nt.left)
                two.append(nt.right)
        return True
