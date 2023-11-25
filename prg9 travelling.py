from itertools import permutations

def tsp_brute_force(graph):
    # Get all permutations of cities (except the first one)
    cities = list(range(1, len(graph)))
    permutations_cities = permutations(cities)

    min_path = None
    min_distance = float('inf')

    # Iterate over all permutations
    for perm in permutations_cities:
        distance = 0
        last_city = 0  # Start from city 0

        # Calculate the total distance of the current permutation
        for city in perm:
            distance += graph[last_city][city]
            last_city = city

        # Add distance from last city to city 0
        distance += graph[last_city][0]

        # Update minimum distance and path
        if distance < min_distance:
            min_distance = distance
            min_path = (0,) + perm

    return min_path, min_distance

# Define a 2D array where dist[i][j] is the distance from city i to city j
dist = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]

path, distance = tsp_brute_force(dist)
print(f"The shortest path is {path} with total distance {distance}")
