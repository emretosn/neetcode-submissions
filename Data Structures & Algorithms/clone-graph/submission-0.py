"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {node: Node(node.val)}
        q = deque([node])
        while q:
            pop = q.popleft()
            for n in pop.neighbors:
                if n not in clones:
                    clones[n] = Node(n.val)
                    q.append(n)
                clones[pop].neighbors.append(clones[n])
        return clones[node]