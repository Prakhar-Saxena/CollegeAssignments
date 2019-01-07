import csv
import sys
import numpy as np

data = dict()

# Could thread this by making a producer / consumer where the consumer takes in a set of records
# If the records span cities, you will have to share elements of the dictionary and thus need locks
# But a more intelligent producer could just pass an entire city burst of data, assuming the file is grouped accordingly

with open(sys.argv[1], 'rb') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        city_country = row['City'] + '.' + row['Country']
        if not (city_country in data):
            data[city_country] = dict()
            
        dt = row['dt']
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

        if not (month_year in data[city_country]):
            data[city_country][month_year] = []

        if len(row['AverageTemperature']) > 0:
            data[city_country][month_year].append(float(row['AverageTemperature']))

    for city_country in data:
        for month_year in data[city_country]:
            if len(data[city_country][month_year]) > 0:
                print "In", city_country, "for month/year", month_year, "the average temperature for the month was", np.mean(data[city_country][month_year])
