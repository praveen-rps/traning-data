from itertools import permutations


def tsp_brute_force(dist_matrix):
    cities = list(range(len(dist_matrix)))
    min_path = None
    min_cost = float('inf')

    for perm in permutations(cities[1:]):  # Fix starting city as 0 (A)
        path = [0] + list(perm) + [0]
        cost = sum(dist_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))

        if cost < min_cost:
            min_cost = cost
            min_path = path

    # Convert to city names (optional)
    city_names = ['A', 'B', 'C', 'D']
    path_names = [city_names[i] for i in min_path]

    print("Minimum Cost Path:", ' → '.join(path_names))
    print("Total Cost:", min_cost)


# Distance matrix
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp_brute_force(distances)