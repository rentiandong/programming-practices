from heapq import heappop, heappush


class FrontierNode:
    def __init__(self, label, cost):
        self.label = label
        self.cost = cost  # path length from a pre-defined start

    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self):
        return f'{self.label}: {self.cost}'


def min_path(start, arr):
    """
    :param start: starting node
    :param arr: list of (start, end, cost) directed edges
    :return: {node => min path length}
    """

    # turn arr into adjacency list
    adj_list = {}
    for begin, end, cost in arr:
        if begin in adj_list:
            adj_list[begin][end] = cost
        else:
            adj_list[begin] = {end: cost}

    # initialize fields for algorithm
    path_len = {start: 0}
    frontier = []
    for node in adj_list[start]:
        new_node = FrontierNode(node, adj_list[start][node])
        heappush(frontier, new_node)

    while frontier:
        f = heappop(frontier)
        if f.label not in path_len:
            path_len[f.label] = f.cost
        else:  # if we run into an outdated frontier
            continue
        if f.label not in adj_list:  # if we arrive at a node with no outgoing edge
            continue
        for new_node in adj_list[f.label]:
            if new_node not in path_len:
                m_path = path_len[f.label]
                edge_cost = adj_list[f.label][new_node]
                new_cost = m_path + edge_cost
                ft_node = FrontierNode(new_node, new_cost)
                heappush(frontier, ft_node)

    return path_len
