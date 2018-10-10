"""
from Leet Code

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real
number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.
Example: Given a / b = 2.0, b / c = 3.0. queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . return
[6.0, 0.5, -1.0, 1.0, -1.0 ]. The input is: vector<pair<string, string>> equations, vector<double>& values,
vector<pair<string, string>> queries , where eq uations.size() == values.size(), and the values are positive. This
represents the equations. Return vector<double>. According to the example above: equations = [ ["a", "b"], ["b",
"c"] ], values = [2.0, 3.0], queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is
no contradiction.

Solution
For each variable a, we create a node, for each pair of of divisor/dividened, we create a
directed edge from divisor to the dividened with cost = quotient. When traversing the graph,
we can go in opposite directions of edges, as directions will only affect how results are
calculated.

Find a query x / y, find path from x to y in the graph. If such a path does not exist, return -1.
Otherwise, starting with result = 1, trace all edges from y to x, if the edge points toward y, divid
res by its cost, otherwise muliply res by its cost. Value of result after tracing all edges in path
is the final return value.
"""


class Node:
    def __init__(self, var):
        self.var = var
        self.edges = {}
        self.discovered = False
        self.parent = None

    def add_edge(self, other, val, direc):
        """
        type other: var of other Node
        type direc: bool, True => out-going
        """
        self.edges[other] = val, direc


def evaluate_division(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """

    nodes = __build_graph(equations, values)
    res = []
    for [v1, v2] in queries:
        for k in nodes:
            nodes[k].discovered = False
            nodes[k].parent = None
        res.append(__find_path_and_val(v1, v2, nodes))
    return res

    # edge cases:
    # 1. variable not in graph
    # 2. only 1 equation


def __build_graph(equations, values):
    """
    return {var_name => node}
    """
    nodes = {}
    for [v_1, v_2], val in zip(equations, values):
        if v_1 not in nodes:
            nodes[v_1] = Node(v_1)
        if v_2 not in nodes:
            nodes[v_2] = Node(v_2)
        nodes[v_1].add_edge(v_2, val, True)
        nodes[v_2].add_edge(v_1, val, False)
    return nodes


def __find_path_and_val(src, dst, nodes_dict):  # basic BFS
    # edge case of src/dst not in graph
    if (src not in nodes_dict) or (dst not in nodes_dict):
        return -1

    nodes_dict[src].discovered = True
    level = [src]
    next_level = []
    while len(level) > 0:
        for i in level:
            for other in nodes_dict[i].edges:
                if nodes_dict[other].discovered:  # avoid loops
                    continue
                else:
                    nodes_dict[other].parent = i
                    nodes_dict[other].discovered = True
                    if other == dst:
                        break
                    next_level.append(other)
        level = next_level
        next_level = []
    if nodes_dict[dst].discovered:
        res = 1
        cur = nodes_dict[dst]
        while cur.parent is not None:
            val, direc = cur.edges[cur.parent]
            if direc:
                res /= val
            else:
                res *= val
            cur = nodes_dict[cur.parent]
        return res
    else:
        return -1
