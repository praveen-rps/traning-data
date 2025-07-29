INF = float('inf')

def floydwarshall(graph):
    v = len(graph)
    dist = [row[:] for row in graph]

    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]

    for i in range(v):
        if dist[i][j] < 0:
            print("Nagative weights cycle detcted")
            return

    print("Shortest distance between every pay of vertices")

    for row in dist:
        for val in row:
            print(f"{val if val !=INF else 'INF' :>5}",end = "")
        print()

if __name__ == "__main__":
    graph = [
        [0,3,INF, 8],
        [INF, 0, -2, INF],
        [INF, INF, 0, 11],
        [INF,INF,INF,0]
    ]

    floydwarshall(graph)





