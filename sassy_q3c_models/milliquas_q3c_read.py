#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.milliquas_q3c_orm import *


# +
# __doc__ string
# -
__doc__ = """ python3 milliquas_q3c_read.py --help """


# +
# constant(s)
# -
MILLIQUAS_CATALOG_FILE = os.path.abspath(os.path.expanduser('milliquas.txt'))
MILLIQUAS_FORMAT = {
    'ra':        [0,    11,  'float',   'degrees', 'J2000 Right Ascension'],
    'dec':       [12,   23,  'float',   'degrees', 'J2000 Declination'],
    'name':      [25,   50,  'string',  '',        'ID from the literature or J2000'],
    'objtype':   [51,   55,  'string',  '',        'Classification of object, and associations'],
    'rmag':      [56,   61,  'float',   'mag',     '?=0 Red optical magnitude'],
    'bmag':      [62,   67,  'float',   'mag',     '?=0 Blue optical magnitude'],
    'comment':   [68,   71,  'string',  '',        'Comment on optical object'],
    'rpsf':      [72,   73,  'char',    '',        'Red optical PSF class'],
    'bpsf':      [74,   75,  'char',    '',        'Blue optical PSF class'],
    'z':         [76,   82,  'float',   '',        '? redshift from the literature or estimated'],
    'namecit':   [83,   89,  'string',  '',        'Citation for name'],
    'zcit':      [90,   96,  'string',  '',        'Citation for redshift'],
    'qpct':      [97,  100,  'int',     '',        '? Probability this object is a QSO'],
    'xname':     [101, 123,  'string',  '',        'X-Ray ID, if any '],
    'rname':     [124, 146,  'string',  '',        'Radio ID, if any '],
    'lobe1':     [147, 169,  'string',  '',        'Radio lobe ID or extra R/X Id, if any '],
    'lobe2':     [170, 192,  'string',  '',        'Radio lobe ID or extra R/X Id, if any ']
}
MILLIQUAS_DIVISOR = 10000


# +
# function: read_milliquas_q3c_read()
# -
# noinspection PyBroadException
def milliquas_q3c_read(_file: str = '', _verbose: bool = False) -> None:

    # check input(s)
    _file = os.path.abspath(os.path.expanduser(_file))
    if not os.path.exists(_file):
        raise Exception(f'invalid input, _file={_file}')

    # read contents
    with open(_file, 'r') as _fd:
        _lines = _fd.readlines()

    # get results
    _all_results = []
    for _i, _e in enumerate(_lines):
        _this_result = {}
        for _k, _v in MILLIQUAS_FORMAT.items():
            _x, _y, _t = _v[0], _v[1], _v[2].strip().lower()
            _val = _e[_x:_y].strip()
            if 'int' in _t:
                try:
                    _this_result[_k] = int(_val)
                except:
                    _this_result[_k] = -1
            elif 'float' in _t:
                try:
                    _this_result[_k] = float(_val)
                except:
                    _this_result[_k] = -1
            else:
                _this_result[_k] = _val
        _this_result['mid'] = int(_i)
        _all_results.append(_this_result)

    # noinspection PyBroadException
    try:
        # connect to database
        if _verbose:
            print(f'connection string = postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        get_session = sessionmaker(bind=engine)
        session = get_session()
    except Exception as e:
        raise Exception(f'Failed to connect to database, error={e}')
    else:
        if _verbose:
            print(f"connected to database postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME} OK")

    # noinspection PyBroadException
    _record = None
    try:
        # loop around records
        for _record in _all_results:
            # create object for each record
            _milliquas_q3c = MilliQuasQ3cRecord(
                    mid=_record['mid'], 
                    ra=_record['ra'], 
                    dec=_record['dec'], 
                    name=_record['name'],
                    objtype=_record['objtype'],
                    rmag=_record['rmag'], 
                    bmag=_record['bmag'], 
                    comment=_record['comment'], 
                    rpsf=_record['rpsf'],
                    bpsf=_record['bpsf'], 
                    z=_record['z'], 
                    namecit=_record['namecit'], 
                    zcit=_record['zcit'],
                    qpct=_record['qpct'], 
                    xname=_record['xname'], 
                    rname=_record['rname'],
                    lobe1=_record['lobe1'], 
                    lobe2=_record['lobe2'])
            # update database with results
            if (_record['mid'] % MILLIQUAS_DIVISOR) == 0 and _verbose:
                print(f"Inserting object {_record['name']} database, mid={_record['mid']}")
                print(f"Inserting object {_milliquas_q3c.serialized()} database")
            session.add(_milliquas_q3c)
            session.commit()
    except Exception as e:
        session.rollback()
        raise Exception(f"Failed to insert object {_record['name']} database, error={e}")

    # disconnect database
    session.close()


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description='Read MILLIQUAS Catalog', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--file', default=MILLIQUAS_CATALOG_FILE, help="""Input file [%(default)s]""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        milliquas_q3c_read(_file=_a.file.strip(), _verbose=bool(_a.verbose))
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
