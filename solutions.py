from collections import Counter

def question1(s, t):
    """Test if the substring of a string s is an anagram of string t.

    Args:
        s (str): The string that contains the substring.
        t (str): The string that is the anagram of the substring.

    Returns:
        bool
    """

    t_len = len(t)
    for idx in xrange(len(s) - t_len + 1):
        if Counter(t) == Counter(s[idx:idx+t_len]):
            return True
    return False

def question2(string):
    """Finds the longest palindromic substring of a string.

    Args:
        string (str): The test string.

    Returns:
        str: The longest palindromic substring.
    """

    length = len(string)
    max_length = 1
    start = 0
    table = [[False for idx in string] for idx in string]
    for idx in xrange(length):
        table[idx][idx] = True
    for idx in xrange(length - 1):
        if string[idx] == string[idx+1]:
            table[idx][idx+1] = True
            start = idx
            max_length = 2
    for sub_length in xrange(3, length + 1):
        for idx in xrange(length - sub_length + 1):
            end = idx + sub_length - 1
            if table[idx+1][end-1] and string[idx] == string[end]:
                table[idx][end] = True
                if sub_length > max_length:
                    start = idx
                    max_length = sub_length
    return string[start:start+max_length]

def question3(graph):
    """Finds the minimum spanning tree contained in a graph.

    Args:
        graph (dict): The undirected graph as adjacency list.

    Returns:
        dict: The minimum spanning tree as adjacency list.
    """

    picked = {}
    edges = sort_edges(graph)
    while len(picked) < len(graph):
        edge = edges.pop()
        if edge[1] not in picked or edge[2] not in picked:
            picked.setdefault(edge[1], []).append((edge[2], edge[0]))
            picked.setdefault(edge[2], []).append((edge[1], edge[0]))
    return picked

def sort_edges(graph):
    """Helper function for question3. Sorts all edges in a graph.

    Args:
        graph (dict): The undirected graph as adjacency list.

    Returns:
        list: List of edges sorted by weight in descending order.
    """

    vertices = graph.keys()
    edges = set()
    for vertex in vertices:
        for node in graph[vertex]:
            if node[0] > vertex:
                edges.add((node[1], vertex, node[0]))
            else:
                edges.add((node[1], node[0], vertex))
    return sorted(list(edges), reverse=True)


def question4(tree, root, num1, num2):
    """Finds least common ancestor between two nodes of BST.

    Args:
        tree (list): BST represented by adjacency matrix.
        root (int): Non-negative integer representing the root .
        num1 (int): Non-negative integer representing one of the nodes.
        num2 (int): Non-negative integer representing one of the nodes.

    Returns:
        int: Integer representing the least common ancestor.
    """

    if not valid_input(tree, root, num1, num2):
        return None
    if num1 > num2:
        num2, num1 = num1, num2
    return lca_helper(tree, root, num1, num2)

def valid_input(tree, root, num1, num2):
    """Helper function for question4. Make sure inputs are valid.

    Args:
        tree (list): BST represented by adjacency matrix.
        root (int): Non-negative integer representing the root .
        num1 (int): Non-negative integer representing one of the nodes.
        num2 (int): Non-negative integer representing one of the nodes.

    Returns:
        bool
    """

    valid = True
    if tree and not isinstance(tree, list):
        valid = False
    if not root:
        valid = False
    if root < 0 or root > len(tree):
        valid = False
    if num1 < 0 or num1 > len(tree):
        valid = False
    if num2 < 0 or num2 > len(tree):
        valid = False
    return valid

def lca_helper(tree, root, num1, num2):
    """Helper function for question4. Recusivly finds least common ancestor.

    Args:
        tree (list): BST represented by adjacency matrix.
        root (int): Non-negative integer representing the root .
        num1 (int): Non-negative integer representing one of the nodes.
        num2 (int): Non-negative integer representing one of the nodes.

    Returns:
        int: Integer representing the least common ancestor.
    """

    if num1 < root and num2 > root:
        return root
    if num1 == root or num2 == root:
        return root
    left = None
    right = None
    for idx, node in enumerate(tree[root]):
        if node == 1:
            if idx < root:
                left = idx
            else:
                right = idx
    if num1 < root:
        return lca_helper(tree, left, num1, num2)
    else:
        return lca_helper(tree, right, num1, num2)

def question5(ll_head, n):
    """Finds the nth element from the back of a singly linked list.

    Args:
        ll_head (Node): Node that is the head of the linked list.
        n (int): Denotes the nth element from the back.

    Returns:
        Value of the node at nth number from the end
    """

    if not ll_head or not n or n == 0:
        return None
    if not isinstance(n, int):
        return "Error: Second argument must be an integer."
    items = []
    current = ll_head
    while current:
        items.append(current.data)
        current = current.next
    if n > len(items):
        return None
    return items[len(items)-n]
