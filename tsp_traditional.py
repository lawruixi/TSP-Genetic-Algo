import itertools

cityList = [(3, 2), (2, 4), (3, 4), (3, 1), (0, 2), (2, 3), (3, 3), (0, 1), (1, 3), (1, 0)]

min_distance = 999999999
optimal_path = None;


def distance(city1, city2):
    """
    Returns distance between two cities.

    :param city1 (int, int): first city coordinates
    :param city2 (int, int): second city coordinates
    """

    x1, y1 = city1;
    x2, y2 = city2;
    return (((x2 - x1)**2) + ((y2 - y1) ** 2))**0.5;

for i in itertools.permutations(cityList):
    current_distance = 0;

    for j in range(len(i) - 2):
        current_distance += distance(i[j], i[j+1])
    current_distance += distance(i[-1], i[0]);

    # min_distance = min(min_distance, current_distance);
    if(current_distance < min_distance):
        min_distance = current_distance;
        optimal_path = i;

print(optimal_path)
print(min_distance);
