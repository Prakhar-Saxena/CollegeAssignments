import sys
from multiprocessing import Pool
import time


def getValByKey(row, col):
    global header
    result = ''
    idx = 0
    for keycol in header.split(','):
        if keycol == col:
            result = row.split(',')[idx]
            break
        idx = idx + 1

    result = result.strip().replace('\'', '')
    return result


def mapper(process_data):
    result = dict()
    for row in process_data:
        key = getValByKey(row, 'Origin')
        if not (key in result):
            result[key] = []

        Wdelay = getValByKey(row, 'WeatherDelay')
        Sdelay = getValByKey(row, 'SecurityDelay')

        if len(Wdelay) == 0:
            continue
        if len(Sdelay) == 0:
            continue

        result[key].append(float(Wdelay) + float(Sdelay))

    return result


def partition(mappings_list):
    result = dict()
    for mappings in mappings_list:
        for key in mappings:
            for val in mappings[key]:
                if not (key in result):
                    result[key] = []
                result[key].append(val)
    return result


def reducer(tuple_list):
    if not (isinstance(tuple_list, list)):
        tuple_list = [tuple_list]

    data = dict()

    for tuple in tuple_list:
        airport = tuple[0]
        row = sum(tuple[1])

        data[airport] = []
        data[airport].append(row)

    return data


# ------------------------------------------------------------------------------------------------------------------- #


filename = sys.argv[1]
processes = int(sys.argv[2])
header = ''

csvlines = []
csvfile = open(filename, 'r')
lineno = 0
for line in csvfile:
    if lineno > 0:
        csvlines.append(line)
    else:
        header = line
    lineno = lineno + 1
numlines = len(csvlines)

lines_per_process = numlines / processes

process_data_array = []
for i in range(processes):
    start = i * (numlines / processes)
    end = (i + 1) * (numlines / processes)
    process_data_array.append(csvlines[start:end])

if processes == 1:

    start1 = time.time()
    mappings = []
    mapping = mapper(process_data_array[0])
    mappings.append(mapping)
    shuffled = partition(mappings)
    reduced = reducer(shuffled.items())

    elapse1 = time.time() - start1
    print("With " + str(processes) + " Nodes it took: " + str(elapse1))


else:

    start2 = time.time()
    pool = Pool(processes=processes,)
    mapping = pool.map(mapper, process_data_array)
    shuffled = partition(mapping)
    reduced = pool.map(reducer, shuffled.items())

    raw = {}
    for i in reduced:
        raw.update(i)

    max_value = max(raw.values())
    max_keys = [k for k, v in raw.items() if v == max_value]

    elapse2 = time.time() - start2
    print("With " + str(processes) + " Nodes it took: " + str(elapse2))
