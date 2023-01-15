import psycopg2
from configparser import ConfigParser


# connection w/o config.ini
# conn = psycopg2.connect(host='localhost', port=5432, database='bank', user='postgres', password='')
# print(conn)
# conn.close()
# print(conn)

# get_config() method from config.ini
def get_config(filename='config.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db_config = {}
    if parser.has_section(section=section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1]
    else:
        raise Exception("Section {0} not found in {1} file".format(section, filename))
    return db_config


def connect():
    conn = None
    try:
        # Params from config.ini
        params = get_config()

        # Pass **params and connect
        conn: psycopg2._psycopg.connection | None = psycopg2.connect(**params)

        # for auto-complete
        cur: psycopg2._psycopg.cursor = ...

        # Create a cursor
        with conn.cursor() as cur:
            # Execute an SQL query (statement)
            cur.execute('SELECT * FROM customers')

            # Display the PostgreSQL database server version
            result = cur.fetchone()
            # print(cur.arraysize)

            # result = cur.fetchmany(2)
            # result = cur.fetchall()
            print(result)

        # Close the communication with PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()


