# Creates a decorator to handle the database connection/cursor opening/closing.
# Creates the cursor with RealDictCursor, thus it returns real dictionaries, where the column names are the keys.
import psycopg2
import psycopg2.extras
from csv import DictReader, DictWriter
import os


def read_file(filename):
    """
        Reads the questions from the file.
        Arguments:
            path/filename
        Returns:
            list of dictionaries of the file
    """
    with open(filename , 'r', newline='', encoding='utf-8') as csvfile:
        saved_file = list(DictReader(csvfile))
        # for dictionary in saved_file:
        #     dictionary['submission_time'] = datetime.datetime.utcfromtimestamp(float(dictionary['submission_time'])).strftime('%Y %b %w %A - %H:%M')
        return saved_file



def write_file(filename, new_question):
    """
        Writes the new question to the file.
        Arguments:
            new_question: dictionary
        Returns:
            None
    """
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        key_list =  list(read_file(filename)[0].keys())
        writer = DictWriter(csvfile, fieldnames=key_list)
        writer.writerow(new_question)


def get_connection_string():

    user_name = os.environ.get('PSQL_USER_NAME')
    password = os.environ.get('PSQL_PASSWORD')
    host = os.environ.get('PSQL_HOST')
    database_name = os.environ.get('PSQL_DB_NAME')

    env_variables_defined = user_name and password and host and database_name

    if env_variables_defined:
        return 'postgresql://{user_name}:{password}@{host}/{database_name}'.format(
            user_name=user_name,
            password=password,
            host=host,
            database_name=database_name
        )
    else:
        raise KeyError('Some necessary environment variable(s) are not defined')

def open_database():
    try:
        connection_string = get_connection_string()
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print('Database connection problem')
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret_value = function(dict_cur, *args, **kwargs)
        dict_cur.close()
        connection.close()
        return ret_value
    return wrapper

