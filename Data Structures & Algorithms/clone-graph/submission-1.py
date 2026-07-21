"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        node_map = { node.val: Node(node.val) }
        visited = set()
        queue = deque()
        queue.append(node)

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor in visited:
                    continue
                if neighbor.val not in node_map:
                    node_map[neighbor.val] = Node(neighbor.val)
                node_map[neighbor.val].neighbors.append(node_map[cur.val])
                node_map[cur.val].neighbors.append(node_map[neighbor.val])
                queue.append(neighbor)
            visited.add(cur)
        
        return node_map[node.val]

