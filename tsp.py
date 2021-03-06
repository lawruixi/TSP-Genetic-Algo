import random;
import datetime;

# Each city is represented by a tuple of (x, y) coordinates.
# We want to minimize distance, which we will calculate via Pythagorean Theorem.

#Change to remove all messages.
verbose = True;

cityList = []
CITIES_NUM= 10
MAX_X = 5
MAX_Y = 5
population = []
POPULATION_SIZE = 100
MUTATION_RATE = 0.05
GENERATIONS = 250

def print_text(text, sep='', end='\n'):
    if(verbose):
        print(text, sep=sep, end=end);

def generate_random_cities(cityList, CITIES_NUM, MAX_X, MAX_Y):
    """
    Generates random cities and populates cityList.

    :param cityList (int, int)[]: list of cities to populate
    :param CITIES_NUM int: number of cities to create
    """

    for i in range(CITIES_NUM):
        #Prevent duplicates
        is_valid = False;
        while(not is_valid):
            cityX = random.randrange(MAX_X);
            cityY = random.randrange(MAX_Y);
            if((cityX, cityY) not in cityList): is_valid = True
        cityList.append((cityX, cityY));

    return cityList;

def distance(city1, city2):
    """
    Returns distance between two cities.

    :param city1 (int, int): first city coordinates
    :param city2 (int, int): second city coordinates
    """

    x1, y1 = city1;
    x2, y2 = city2;
    return (((x2 - x1)**2) + ((y2 - y1) ** 2))**0.5;


def fitness(route):
    """
    Returns fitness for route, inversely proportional to distance.

    :param route (int, int)[]: list of cities in order to go to.
    """

    total_distance = 0;
    for i in range(CITIES_NUM-1):
        total_distance += distance(route[i], route[i+1]);
    total_distance += distance(route[0], route[CITIES_NUM - 1]);
    return 1 / total_distance;

def best_route(population):
    """
    Finds the best route given a population by comparing the fitness value.

    :param population (int, int)[][]: array describing population.
    """
    best_fitness = -1;
    best_route = None;
    for i in population:
        if(fitness(i) > best_fitness):
            best_route = i;
            best_fitness = fitness(i);
    return best_route;


def initialize_population(individuals, cityList):
    """
    Generates a population for the genetic algorithm.

    :param individuals int: number of individuals in the algorithm.
    :param cityList (int, int)[]: the city list to draw cities from.
    """

    print_text("Initializing population...")
    for i in range(individuals):
        #Randomly shuffle cityList for each route.
        population.append(random.sample(cityList, CITIES_NUM));

    print_text("Population initialized!")
    for i in range(individuals):
        print_text(population[i]);

    print_text("\n");
    return population;


def rank_routes(population):
    """
    Ranks routes based on fitness.
    Returns a dictionary based on route index : fitness

    :param population (int, int)[][]: list of routes of cities that represents the population.
    """

    routes_dict = {}

    print_text("Ranking routes...");

    for i in range(len(population)):
        routes_dict[i] = fitness(population[i]);

    print_text("Routes: ");
    print_text(routes_dict);
    print_text("\n");

    return routes_dict;

def best_distance(population):
    """
    Returns best distance of all the ranked routes.

    :param population (int, int)[][]: the population list
    """

    max_fitness = max([fitness(i) for i in population]);
    return 1/max_fitness;

def average_distance(population):
    """
    Returns mean distance across population.

    :param population (int, int)[][]: population list
    """

    fitness_list = [fitness(i) for i in population];
    sum_fitness = sum(fitness_list);
    average_fitness = sum_fitness / len(population);
    return 1 / average_fitness;


def selection(population, routes_dict, k):
    """
    Selects parents to "breed" and form a child.
    Based on tournament style, where the best of k random members are chosen.
    Returns tuple of parent1, parent2.

    :param population (int, int)[][]: list of routes that represents the population.
    :param routes_dict {int: int}: dictionary of ranked routes to fitness.
    """

    print_text("Selection!")

    shuffle1 = random.sample(population, len(population));
    grp1 = shuffle1[:k];
    print(grp1)
    parent1 = best_route(grp1);

    shuffle1 = random.sample(population, len(population));
    grp2 = shuffle1[:k];
    parent2 = best_route(grp2);

    print_text("Chosen parent1: \n", end='');
    print_text(parent1, end='');
    print_text(", fitness = " + str(fitness(parent1)))

    print_text("Chosen parent2: \n", end='');
    print_text(parent2, end='');
    print_text(", fitness = " + str(fitness(parent2)))

    print_text("\n");

    return (parent1, parent2);

def breed(parents):
    """
    Returns a child route from two parents via ordered crossover.

    :param parents ((int, int)[][], (int, int)[][]): a tuple of two routes representing the parents of the new child.
    """

    child1 = []
    child2 = []
    parent1, parent2 = parents;

    print_text("Breeding parents...")

    # determine two points to cut
    cut1 = random.randrange(0, len(parent1));
    cut2 = random.randrange(0, len(parent1));
    if(cut1 > cut2): cut1, cut2 = cut2, cut1;

    # cut_range = parent1[cut1:cut2]
    # child1 = cut_range + [item for item in parent2 if item not in cut_range];

    # cut_range = parent2[cut1:cut2]
    # child2 = cut_range + [item for item in parent1 if item not in cut_range];
    cut_range = parent1[cut1:cut2];
    child1 = []
    index = 0;
    i = 0;
    while i < cut1:
        if(parent2[index] not in cut_range): child1.append(parent2[index]); index += 1; i += 1;
        else: index += 1; continue;
    while i < cut2:
        child1.append(parent1[i]); i += 1;
    while i < len(parent2):
        if(parent2[index] not in cut_range): child1.append(parent2[index]); index += 1; i += 1;
        else: index += 1; continue;

    print("Child1")
    print(child1)


    cut_range = parent2[cut1:cut2];
    child2 = []
    index = 0;
    i = 0;
    while i < cut1:
        if(parent1[index] not in cut_range): child2.append(parent1[index]); index += 1; i += 1;
        else: index += 1; continue;
    while i < cut2:
        child2.append(parent2[i]); i += 1;
    # child2 += cut_range;
    # i += cut2 - cut1 + 1;
    while i < len(parent1):
        if(parent1[index] not in cut_range): child2.append(parent1[index]); index += 1; i += 1;
        else: index += 1; continue;

    print("Child2")
    print(child2)


    # cut_range = parent2[cut1:cut2];
    # child2 = []
    # for i in range(cut1):
    #     child2.append(parent1[i]);
    # child2 += cut_range;
    # for i in range(cut2, len(parent1)):
    #     child2.append(parent1[i])

    # for count in range(len(parent1)):
    #     if(cut1 <= count and count <= cut2):
    #         child1.append(parent1[count]);
    #     else:
    #         child1.append(parent2[count]);

    # for count in range(len(parent1)):
    #     if(cut1 <= count and count <= cut2):
    #         child2.append(parent2[count]);
    #     else:
    #         child2.append(parent1[count]);

    print_text("Breeding completed!")
    print_text("Child 1: \n" + str(child1) + ", fitness = " + str(fitness(child1)));
    print_text("Child 2: \n" + str(child2) + ", fitness = " + str(fitness(child2)));

    print_text("\n");

    return (child1, child2);

def breed_population(population, routes_dict):
    """
    Breeds a population to form the next population.

    :param population (int, int)[][]: population
    :param routes_dict {int: int}: dictionary of ranked routes to fitness.
    """
    new_population = []

    for i in range(len(population) // 2):
        (parent1, parent2) = selection(population, routes_dict, len(population) // 4);
        child1, child2 = breed((parent1, parent2));
        new_population.extend([child1, child2]);

    print_text("New population: ")
    for i in new_population:
        print_text(i, end='');
        print_text(", fitness = " + str(fitness(i)))

    print_text("\n");
    return new_population;

def mutate(individual, mutation_rate):
    """
    Mutates randomly by swapping two cities in the route.
    Returns the individual, whether changed or not.

    :param individual (int, int)[]: route to swap
    :param mutation_rate float: rate of mutation out of 1
    """

    print_text("Mutating...")
    print_text(individual, end='');
    print_text(", fitness = " + str(fitness(individual)))
    for i in range(len(individual)):
        if(random.random() > mutation_rate): print_text("No change."); continue;

        print_text("Mutation chosen!")
        swap_index_1 = i;
        swap_index_2 = int(random.random() * len(individual));
        print_text("Swapping indices " + str(swap_index_1) + " and " + str(swap_index_2));

        individual[swap_index_1], individual[swap_index_2] = individual[swap_index_2], individual[swap_index_1];
        print_text("Individual mutated:")
        print_text(individual, end='');
        print_text(", fitness = " + str(fitness(individual)))

    print_text("\n");
    return individual;



def mutate_population(population, mutation_rate):
    """
    Applies mutate() to the entire population.

    :param population (int, int)[][]: the population to undergo mutation.
    :param mutation_rate float: rate of mutation for each individual out of 1.
    """
    new_population = []
    for i in population:
        new_population.append(mutate(i, mutation_rate));
    return new_population;

def genetic_algorithm():
    """
    Putting it all together ;)

    """
    #For timing how long it takes
    now = datetime.datetime.now();

    global cityList;
    print_text("City List: ")
    print_text(cityList);

    population = []
    population = initialize_population(POPULATION_SIZE, cityList);
    print_text("Initial distance: ", end="");
    print_text(best_distance(population));

    for i in range(GENERATIONS):
        #Rank all the routes.
        routes_dict = rank_routes(population);
        population = breed_population(population, routes_dict);
        population = mutate_population(population, MUTATION_RATE);

        print_text("Population:")
        for i in population:
            print_text(i, end='');
            print_text(", fitness = " + str(fitness(i)))
        print_text("Distance: " + str(best_distance(population)))
        print_text("Average distance: " + str(average_distance(population)))

    print_text("Final distance: ", end="");
    print_text(best_distance(population));

    time_taken = datetime.datetime.now() - now;
    print_text("\nFinal time:\t" + str(time_taken))


cityList = generate_random_cities(cityList, CITIES_NUM, MAX_X, MAX_Y);
genetic_algorithm();
