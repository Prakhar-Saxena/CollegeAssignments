from configparser import ConfigParser
import psycopg2 as ps
import sys

def config(filename='a4.ini', section='settings', pswd=''):
    parser = ConfigParser()
    parser.read(filename)
    db = {}# dict()
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
        db['password'] = pswd
    else:
        raise Exception('Section {0} not foung in the {1} file'.format(section,filename))

    return db

def connect(sql, pswd):
    conn = None
    try:
        params = config(filename='a4.ini', section='settings', pswd=str(pswd))

        print('Connecting to the PostgreSQL database...')
        conn = ps.connect(**params)
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute(sql)
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    pswd = sys.argv[1]
    # print(pswd)
    while True:
        # try:
            inp = int(input('1 - Find players named Antetokounmpo\n2 - Find teams for which players named Antetokounmpo played for over the years\n3 - Find games each season where each player named Antetokounmpo had teh most points.\n0 - Exit\n'))
            if inp == 0 :
                sys.exit()
            elif inp == 1:
                file = open('a4.q1', 'r')
                sql = file.readlines()[0]
                file.close()
                connect(pswd, sql)
            elif inp == 2:
                file = open('a4.q2', 'r')
                sql = file.readlines()[0]
                file.close()
                connect(pswd, sql)
            elif inp == 3:
                file = open('a4.q3', 'r')
                sql = file.readlines()[0]
                file.close()
                connect(pswd, sql)
        # except:
            # print('Something didn\'t work, try again.')

    connect()