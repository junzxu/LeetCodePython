# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.Map = {} #store nodes in copied graph
    def cloneGraph(self, node):
        if node is None:
            return
        head = UndirectedGraphNode(node.label)
        self.Map[node.label] = head
        for neighbor in node.neighbors:
            if neighbor == node:
                head.neighbors.append(head)
                continue
            if not self.Map.has_key(neighbor.label):
                new_neighbor = self.cloneGraph(neighbor)
            else:
                new_neighbor = self.Map[neighbor.label]
            head.neighbors.append(new_neighbor)
        return head
