from configparser import ConfigParser
import psycopg2 as ps
import sys

def config(filename='publickeys', section='publickeys'):
    parser = ConfigParser()
    parser.read(filename)
    pub = {}  # dict()
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            pub[param[0]] = param[1]
    else:
        raise Exception('Section {0} not foung in the {1} file'.format(section,filename))

    return pub