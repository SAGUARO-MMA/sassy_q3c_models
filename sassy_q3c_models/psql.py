#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# doc string(s)
# -
__doc__ = """ python3 psql.py --help """


# +
# constant(s)
# -
DB_CONNECT_MSG = f'{DB_HOST}:{DB_PORT}/{DB_NAME}'
DEFAULT_COMMAND = f'SELECT * FROM glade_plus_q3c WHERE q3c_radial_query(ra, dec, 23.5,  29.2, 5.0);'
FETCH_METHOD = ['fetchall', 'fetchone', 'fetchmany']
FETCH_MANY = 50
KEYS = ('authorization', 'command', 'database', 'method', 'nelms', 'port', 'server')
RESULTS_PER_PAGE = 50


# +
# class: Psql()
# -
# noinspection PyBroadException
class Psql(object):

    # +
    # method: __init__()
    # -
    def __init__(self, authorization: str = f'{DB_USER}:{DB_PASS}', database: str = f'{DB_NAME}', 
                 port: int = int(f'{DB_PORT}'), server: str = f'{DB_HOST}'):

        # get input(s)
        self.authorization = authorization
        self.database = database
        self.port = port
        self.server = server

        # private variable(s)
        self.__connection = None
        self.__cursor = None
        self.__connection_string = None
        self.__result = None
        self.__results = None

    # +
    # decorator(s)
    # -
    @property
    def authorization(self):
        return self.__authorization

    @authorization.setter
    def authorization(self, authorization: str = f'{DB_USER}:{DB_PASS}'):
        self.__authorization = authorization
        self.__username = self.__authorization.split(f':')[0] if ':' in self.__authorization else f'{DB_USER}'
        self.__password = self.__authorization.split(f':')[1] if ':' in self.__authorization else f'{DB_PASS}'

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, database: str = f'{DB_NAME}'):
        self.__database = database

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        self.__port = port

    @property
    def server(self):
        return self.__server

    @server.setter
    def server(self, server: str = f'{DB_HOST}'):
        self.__server = server

    # +
    # method: connect()
    # -
    def connect(self):
        """ connect to database """

        # set variable(s)
        self.__connection = None
        self.__cursor = None
        self.__connection_string = f"host='{self.__server}' dbname='{self.__database}' " \
            f"user='{self.__username}' password='{self.__password}'"

        # get connection
        try:
            self.__connection = psycopg2.connect(self.__connection_string)
        except Exception as _e1:
            self.__connection = None
            print(f'failed connecting to {DB_CONNECT_MSG}, error={_e1}')

        # get cursor
        try:
            self.__cursor = self.__connection.cursor()
        except Exception as _e2:
            self.__cursor = None
            print(f'failed getting cursor for {DB_CONNECT_MSG}, error={_e2}')

    # +
    # method: disconnect()
    # -
    def disconnect(self):
        """ disconnect from database """

        # disconnect cursor
        if self.__cursor is not None and hasattr(self.__cursor, 'close'):
            self.__cursor.close()

        # disconnect connection
        if self.__connection is not None and hasattr(self.__connection, 'close'):
            self.__connection.close()

        # reset variable(s)
        self.__connection = None
        self.__cursor = None

    # +
    # method: fetchall()
    # -
    def fetchall(self, command: str = ''):
        """ execute fetchall() command """

        # execute query
        try:
            self.__cursor.execute(command)
            self.__results = self.__cursor.fetchall()
        except Exception:
            self.__results = None

        # return result(s)
        return self.__results

    # +
    # method: fetchmany()
    # -
    def fetchmany(self, command: str = '', number: int = 0):
        """ execute fetchmany() command """

        # execute query
        try:
            self.__cursor.execute(command)
            self.__results = self.__cursor.fetchmany(number)
        except Exception:
            self.__results = None

        # return result(s)
        return self.__results

    # +
    # method: fetchone()
    # -
    def fetchone(self, command: str = ''):
        """ execute fetchone() command """

        # execute query
        try:
            self.__cursor.execute(command)
            self.__result = self.__cursor.fetchone()
        except Exception:
            self.__result = None

        # return result
        return self.__result


# +
# function: psql()
# -
def psql(_args: dict = None):

    # check input(s)
    if not all(_k in _args for _k in KEYS):
        raise Exception(f'invalid dictionary, _args={_args}')

    # set default(s)
    _authorization = _args['authorization'].strip()
    _command = _args['command'].strip()
    _database = _args['database'].strip()
    _method = _args['method'].strip().lower()
    _nelms = int(_args['nelms'])
    _port = int(_args['port'])
    _server = _args['server'].strip()
    _verbose = bool(_args['verbose'].strip())

    # instantiate class
    try:
        _t = Psql(_authorization, _database, _port, _server)
    except Exception as _e:
        raise Exception(f'failed to create class, error={_e}')

    # do something
    if _t:

        # connect
        _t.connect()

        # select
        if _method == 'fetchall':
            _all = _t.fetchall(_command)
            if _all:
                pprint.pprint(f'{_all}')

        elif _method == 'fetchone':
            _one = _t.fetchone(_command)
            if _one:
                pprint.pprint(f'{_one}')

        elif _method == 'fetchmany':
            _many = _t.fetchmany(_command, _nelms)
            if _many:
                pprint.pprint(f'{_many}')

        # disconnect
        _t.disconnect()


# +
# main()
# -
if __name__ == '__main__':

    # get command line argument(s)
    _p = argparse.ArgumentParser(description=f'Test PostGresQL Database Connection', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--authorization', default=f'{DB_USER}:{DB_PASS}', help=f"""database authorization=<str>:<str>, defaults to '%(default)s'""")
    _p.add_argument(f'--command', default=DEFAULT_COMMAND, help=f"""database command=<str>, defaults to '%(default)s'""")
    _p.add_argument(f'--database', default=f'{DB_NAME}', help=f"""database name=<str>, defaults to '%(default)s'""")
    _p.add_argument(f'--method', default=f'{FETCH_METHOD[1]}', help=f"""database method=<str>, in {FETCH_METHOD} defaults to %(default)s""")
    _p.add_argument(f'--nelms', default=FETCH_MANY, help=f"""database nelms=<int> (for fetchmany) defaults to %(default)s""")
    _p.add_argument(f'--port', default=int(DB_PORT), help=f"""database port=<int>, defaults to %(default)s""")
    _p.add_argument(f'--server', default=f'{DB_HOST}', help=f"""database server=<address>,  defaults to '%(default)s'""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        psql(dict(vars(_a)))
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
