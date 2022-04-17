def valid(graph, colors):
    last_vertex, last_color = len(colors) - 1, colors[-1]
    colored_neighbors = [i
            for i, has_edge
            in enumerate(graph[last_vertex])
            if has_edge and i < last_vertex]
    for neighbor in colored_neighbors:
        if colors[neighbor] == last_color:
            return False
    return True

def colorable(graph, k, colors=[]):
    if len(colors) == len(graph):
        return True

    for i in range(k):
        colors.append(i)
        if valid(graph, colors):
            if colorable(graph, k, colors):
                return True
        colors.pop()

    return False