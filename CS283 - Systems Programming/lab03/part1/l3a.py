import sys
from multiprocessing import Pool

# global variable to gold the headers of Airline Delay csv file 
global headers
headers = ''

# function to get an array of the data in a specific column
def data_in_col(row, col):
    result = ''
    i = 0
    for header in headers.split(','):
        if header == col:
            result = row.split(',')[i]
            break
        i += 1
    result = result.strip().replace('\'', '')
    return result

#  function to map/append to an dictionary of different airports their respective weather and security delays
def mapper(process_data):
    result = dict()
    for row in process_data:
        # look at origin airport
        data = data_in_col(row, 'Origin')
        if (data not in result):
            result[data] = []
        # call function on headers 'WeatherDelay' and 'SecurityDelay' respectively to get back data
        weather_delay = data_in_col(row, 'WeatherDelay')
        security_delay = data_in_col(row, 'SecurityDelay')
        # check cases in which there was no delay (security/weather)
        if len(weather_delay) == 0 or len(security_delay) == 0:
            continue
        result[data].append(float(weather_delay) + float(security_delay))
    return result

# function to map values to each different airport
def partition(mappings_list):
    result = dict()
    for mappings in mappings_list:
        for key in mappings:
            for val in mappings[key]:
                if not (key in result):
                    result[key] = []
                result[key].append(val)
    return result

# function to sum and get repspective overall delays for each airport
# use a dictionary to store each airport and its overall delay time due to security/weather
def reducer(tuple_list):
    if list not in tuple_list:
        tuple_list = [tuple_list]
    data = dict()
    for tuple in tuple_list:
        airport = tuple[0]
        row = sum(tuple[1])
        data[airport] = []
        data[airport].append(row)
    return data

# main program
# extract information from csv file into an array and a header
filename = sys.argv[1]
nodes = int(sys.argv[2])
lines_in_file = []
my_file = open(filename, 'r')
counter = 0
for line in my_file:
    if counter > 0:
        lines_in_file.append(line)
    else:
        headers = line
    counter += 1
num_lines = len(lines_in_file)

# 
data = []
for i in range(nodes):
    start = i * (num_lines / nodes)
    end = (i + 1) * (num_lines / nodes)
    data.append(lines_in_file[start:end])

# run program with one processor
if nodes == 1:
    mappings = []
    mapping = mapper(data[0])
    mappings.append(mapping)
    shuffled = partition(mappings)
    reduced = reducer(shuffled.items())

    max_value = max(reduced.values())
    max_keys = [k for k, v in reduced.items() if v == max_value]

    print("\nThe " + str(max_keys[0]) + " airport had the longest delays due to security and weather combined \n")

# run program with multiple processors, 2,4,8...
else:
    pool = Pool(processes=nodes,)
    mapping = pool.map(mapper, data)
    shuffled = partition(mapping)
    print(shuffled)
    reduced = pool.map(reducer, shuffled.items())
    # 
    raw = {}
    for i in reduced:
        raw.update(i)
    max_value = max(raw.values())
    max_keys = [k for k, v in raw.items() if v == max_value]
    print("\nThe " + str(max_keys[0]) + " airport had the longest delays due to security and weather combined \n")

