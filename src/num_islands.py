def num_islands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    # implment a union find data structure
    # iterate by row then column
    # for each cell, and the cell to its right
    # or bottom, if both are 1, union the cells

    # label each node as (row, col) indicies

    if not grid:
        return 0

    class UnionFind:
        def __init__(self, nodes):
            self.group = {}
            self.sets = {}
            for index in range(0, len(nodes)):
                self.group[nodes[index]] = index
                self.sets[index] = {nodes[index]}

        def find(self, node):
            return self.group[node]

        def union(self, node_1, node_2):
            [(s_node, s_set), (l_node, l_set)] = sorted(
                [
                    (node_1, self.sets[self.group[node_1]]),
                    (node_2, self.sets[self.group[node_2]])
                ],
                key=lambda x: len(x[1])
            )

            to_delete = self.find(s_node)
            for node in s_set:
                self.group[node] = self.find(l_node)
                self.sets[self.find(l_node)].add(node)
            del self.sets[to_delete]

    # get all nodes:
    all_nodes = []
    rows = len(grid)
    cols = len(grid[0])
    for i in range(0, rows):
        for j in range(0, cols):
            if grid[i][j] == '1':
                all_nodes.append((i, j))

    # initialize Union Find DS
    unf = UnionFind(all_nodes)

    # find all connected components with Union Find
    for i in range(0, rows):
        for j in range(0, cols):
            if grid[i][j] == '1':
                if i != rows - 1:
                    if grid[i + 1][j] == '1':
                        if unf.find((i, j)) != unf.find((i + 1, j)):
                            unf.union((i, j), (i + 1, j))
                if j != cols - 1:
                    if grid[i][j + 1] == '1':
                        if unf.find((i, j)) != unf.find((i, j + 1)):
                            unf.union((i, j), (i, j + 1))

    # return num of connected components
    return len(unf.sets)
