def some_undirected_cyclic(graph):
    from collections import deque
    start = graph.start
    end = graph.end
    red_vertices = graph.node_colours

    def bfs_paths(source, target):
        has_red = red_vertices[source]
        queue = deque([(has_red, source, [source])])

        while queue:
            (has_red, vertex, path) = queue.popleft()
            
            for neighbor in graph.edges[vertex]:
                if neighbor not in path:
                    has_red = has_red or red_vertices[neighbor]
                    new_path = path + [neighbor]

                    if neighbor == target:
                        if has_red:
                            return True
                    else:
                        queue.append((has_red, neighbor, new_path))
        return False

    return bfs_paths(start, end)