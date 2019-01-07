# https://mikecvet.wordpress.com/2010/07/02/parallel-mapreduce-in-python/
# data from http://berkeleyearth.org/data/
# kaggle aggregated at https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data

import sys
from multiprocessing import Pool
import numpy as np

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
        key = getValByKey(row, 'City') + '.' + getValByKey(row, 'Country')
        if not (key in result):
            result[key] = []

        dt = getValByKey(row, 'dt')
        if '/' in dt:
            dt_elements = dt.split('/')
            month = dt_elements[0]
            year = dt_elements[2]
        elif '-' in dt:
            dt_elements = dt.split('-')
            year = dt_elements[0]
            month = dt_elements[1]
        else:
            print 'Date format error', dt
            continue

        month_year = str(month) + '/' + str(year)

        avgtemp = getValByKey(row, 'AverageTemperature')

        if len(avgtemp) == 0:
            continue

        val = month_year + '_' + avgtemp

        #print 'mapper appending', val, 'to', key

        result[key].append(val)

    return result

def reducer(tuple_list):
    #print tuple_list

    if not (isinstance(tuple_list, list)):
        tuple_list = [tuple_list]

    data = dict()
    result = dict()

    for tuple in tuple_list:
        if len(tuple) < 2:
            print 'Tuple error', tuple
            continue

        city_country = tuple[0]
        rows = tuple[1]

        if not (city_country in data):
            data[city_country] = dict()

        for row in rows:
            elements = row.split('_')

            if len(elements) < 2:
                print 'Date parsing error', elements
                continue

            month_year = elements[0]

            try:
                temp = float(elements[1])
            except:
                print 'Temperature parsing error', elements[1] 
                continue

            month_year_elements = month_year.split('/')

            if len(month_year_elements) < 2:
                print 'Month/Year parsing error', month_year_elements
                continue

            month = month_year_elements[0]
            year = month_year_elements[1]

            if not (month_year in data[city_country]):
                data[city_country][month_year] = []
   
            #print 'reducer appending', temp, 'to', city_country, ':', month_year

            data[city_country][month_year].append(temp)

    for city_country in data:
        if not (city_country in result):
            result[city_country] = dict() 

        for month_year in data[city_country]:
            if len(data[city_country][month_year]) > 0:
                mn = np.mean(data[city_country][month_year])
                #print 'result appending', mn, 'to', city_country, ':', month_year
                result[city_country][month_year] = mn

    return result         

def partition(mappings_list):
    # mappings is an array of dicts of city.country keys to month/year_temperature values, which we want to aggregate into a single dict organized by key, so that each reducer will receive only values from the same key
    result = dict()

    for mappings in mappings_list:
        for key in mappings:
            for val in mappings[key]:
                if not (key in result):
                    result[key] = []

                result[key].append(val) 

    return result

filename = sys.argv[1]
processes = int(sys.argv[2])
header = ''

csvlines = []
csvfile = open(filename, 'r')
lineno = 0
for line in csvfile:
    if lineno > 0: # don't read the header line into the list to be processed
        csvlines.append(line)
    else:
        header = line
    lineno = lineno + 1
numlines = len(csvlines)

lines_per_process = numlines / processes

# break up lines into an array of "processes" elements, each element containing an array of the N'th cluster of numlines / processes lines of text
process_data_array = []
for i in range(processes):
    start = i * (numlines / processes)
    end = (i+1) * (numlines / processes)
    process_data_array.append(csvlines[start:end])

if processes == 1:
    mappings = []
    mapping = mapper(process_data_array[0]) # only one element if one process
    mappings.append(mapping)
    shuffled = partition(mappings)
    reduced = reducer(shuffled.items())
else:
    pool = Pool(processes=processes,)

    mapping = pool.map(mapper, process_data_array)
    shuffled = partition(mapping) # shuffled is an array of mapping dicts
    reduced = pool.map(reducer, shuffled.items()) # items is a list of (key, value) tuples

if not (isinstance(reduced, list)):
    reduced = [reduced]

for i in range(len(reduced)):
    for city_country in reduced[i]:
        for month_year in reduced[i][city_country]:
            print "In", city_country, "for month/year", month_year, "the average temperature for the month was", reduced[i][city_country][month_year]
