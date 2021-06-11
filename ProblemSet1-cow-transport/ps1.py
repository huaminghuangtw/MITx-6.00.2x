from ps1_partition import get_partitions
import time
from os.path import dirname, join


def load_cows(filename):
	"""
	Read the contents of the given file.
	Assumes the file contents contain data in the form of comma-separated cow name,
	weight pairs, and return a dictionary containing cow names as keys and
	corresponding weights as values.

	@Parameters:
	filename - the name of the data file as a string

	@Returns:
	a dictionary of cow name (string), weight (int) pairs
	"""
	cow_dict = dict()

	current_dir = dirname(__file__)
	file_path = join(current_dir, filename)
	with open(file_path, 'r') as f:
		for line in f:
			line_data = line.split(',')
			cow_dict[line_data[0]] = int(line_data[1])

	return cow_dict

# ----------------------------------------------------------------------------------------------------------------------

# Problem 1
def greedy_cow_transport(cows, limit=10):
	"""
	Uses a greedy heuristic to determine an allocation of cows that attempts to
	minimize the number of spaceship trips needed to transport all the cows.
	The returned allocation of cows may or may not be optimal.
	The greedy heuristic should follow the following method:

	1. As long as the current trip can fit another cow, add the largest cow that
	   will fit to the trip
	2. Once the trip is full, begin a new trip to transport the remaining cows

	Does not mutate the given dictionary of cows.

	@Parameters:
	cows - a dictionary of name (string), weight (int) pairs
	limit - weight limit of the spaceship (an int)
	
	@Returns:
	A list of lists, with each inner list containing the names of cows transported
	on a particular trip and the overall list containing all the trips
	"""
	# sort a dictionary as a list of (key, value) tuples by values in descending order
	sorted_cows = sorted(cows.items(), key=lambda item: item[1], reverse=True)

	trips = []
	trip = []
	total_weight = 0

	while(sorted_cows):
		cows_copy = sorted_cows.copy()
		for item in cows_copy:
			cow = item[0]
			weight = item[1]
			total_weight += weight
			if (total_weight <= limit):
				trip.append(cow)
				sorted_cows.remove(item)
			else:
				total_weight -= weight
		trips.append(trip)
		trip = []
		total_weight = 0

	return trips

# ----------------------------------------------------------------------------------------------------------------------

# Problem 2
def brute_force_cow_transport(cows, limit=10):
	"""
	Finds the allocation of cows that minimizes the number of spaceship trips
	via brute force.
	The brute force algorithm should follow the following method:

	1. Enumerate all possible ways that the cows can be divided into separate trips
	2. Select the allocation that minimizes the number of trips without making any trip
	   that does not obey the weight limitation
			
	Does not mutate the given dictionary of cows.

	@Parameters:
	cows - a dictionary of name (string), weight (int) pairs
	limit - weight limit of the spaceship (an int)
	
	@Returns:
	A list of lists, with each inner list containing the names of cows transported
	on a particular trip and the overall list containing all the trips
	"""
	candidates = []

	cow_names = cows.keys()

	g = get_partitions(cow_names)
	while (True):
		try:
			valid = True
			allocation = next(g)
			for trip in allocation:
				total_weight = 0
				for cow in trip:
					total_weight += cows[cow]
				if (total_weight > limit):
					valid = False
					break
			if (valid):
				candidates.append(allocation)
		except StopIteration:
			break

	result = []
	minNumberOfTrips = len(cows)
	for candidate in candidates:
		numberOfTrips = len(candidate)
		if (numberOfTrips <= minNumberOfTrips):
			minNumberOfTrips = numberOfTrips
			result = candidate

	return result

# ----------------------------------------------------------------------------------------------------------------------

# Problem 3
def compare_cow_transport_algorithms(limit=10):
	"""
	Using the data from ps1_cow_data.txt and the specified weight limit, run your
	greedy_cow_transport and brute_force_cow_transport functions here.
	Use the default weight limits of 10 for both greedy_cow_transport and
	brute_force_cow_transport.
	
	Print out the number of trips returned by each method, and how long each
	method takes to run in seconds.

	@Returns:
	Does not return anything.
	"""
	cows = load_cows("ps1_cow_data.txt")

	start = time.time()
	print("Number of trips by greedy algorithm: ", end='')
	print(len(greedy_cow_transport(cows, limit)))
	end = time.time()
	print("Time used for greedy algorithm: ", end='')
	print(end - start)
	print()

	start = time.time()
	print("Number of trips by brute force algorithm: ", end='')
	print(len(brute_force_cow_transport(cows, limit)))
	end = time.time()
	print("Time used for brute force algorithm: ", end='')
	print(end - start)
	print()


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers.
Uncomment the last two lines to print the result of your problem.
"""
if __name__ == '__main__':
	cows = load_cows("ps1_cow_data.txt")
	limit = 10

	print("Cows:")
	print(cows)
	print()
	sorted_cows = sorted(cows.items(), key=lambda item: item[1], reverse=True)
	print("Sorted cows:")
	print(sorted_cows)
	print()

	print("------------------------------------------------------------")
	print("Weight limit of each trip =", limit)
	print()

	print("Greedy algorithm:")
	print(greedy_cow_transport(cows))
	print()
	print("Brute force algorithm:")
	print(brute_force_cow_transport(cows))
	print()

	compare_cow_transport_algorithms(limit)