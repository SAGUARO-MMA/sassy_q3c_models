#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.gwgc_q3c_orm import *


# +
# __doc__ string
# -
__doc__ = """ python3 gwgc_q3c_read.py --help """


# +
# constant(s)
# -
GWGC_CATALOG_FILE = os.path.abspath(os.path.expanduser('gwgc.dat'))
GWGC_DIVISOR = 2500
GWGC_FORMAT = {
    'pgc':       [0,     7,  'int',     'None',    'Identifier from HYPERLEDA'],
    'name':      [8,    36,  'string',  'None',    'Common name of galaxy or globular'],
    'ra':        [37,   46,  'float',   'hours',   'J2000 Right Ascension'],
    'dec':       [47,   55,  'float',   'degrees', 'J2000 Declination'],
    'tt':        [56,   60,  'float',   'None',    'Morphological type code'],
    'b_app':     [61,   66,  'float',   'mag',     'Apparent blue magnitude'],
    'a':         [67,   74,  'float',   'arcmin',  'Major diameter'],
    'e_a':       [75,   82,  'float',   'arcmin',  'Error in major diameter'],
    'b':         [83,   90,  'float',   'arcmin',  'Minor diameter'],
    'e_b':       [91,   98,  'float',   'arcmin',  'Error in minor diameter'],
    'b_div_a':   [99,  104,  'float',   'None',    'Ratio of minor to major diameters'],
    'e_b_div_a': [105, 110,  'float',   'None',    'Error in ratio of minor to major diameters'],
    'pa':        [111, 116,  'float',   'degrees', 'Position angle of galaxy'],
    'b_abs':     [117, 123,  'float',   'mag',     'Absolute blue magnitude'],
    'dist':      [124, 131,  'float',   'Mpc',     'Distance'],
    'e_dist':    [132, 138,  'float',   'Mpc',     'Error in Distance'],
    'e_b_app':   [139, 143,  'float',   'mag',     'Error in apparent blue magnitude'],
    'e_b_abs':   [144, 148,  'float',   'mag'      'Error in absolute blue magnitude']
}


# +
# function: read_gwgc_q3c_read()
# -
def gwgc_q3c_read(_file: str = '', _verbose: bool = False) -> None:

    # check input(s)
    _file = os.path.abspath(os.path.expanduser(_file))
    if not isinstance(_file, str) or not os.path.exists(_file):
        raise Exception(f'invalid input, _file={_file}')

    # read contents
    with open(os.path.abspath(os.path.expanduser(_file)), 'r') as _fd:
        _lines = set(_fd.readlines())

    # get results
    _all_results = []
    for _i, _e in enumerate(_lines):
        _this_result = {}
        for _l in GWGC_FORMAT:
            _xoffset, _yoffset = GWGC_FORMAT[_l][0], GWGC_FORMAT[_l][1]
            _value = _e[_xoffset:_yoffset].strip()
            if GWGC_FORMAT[_l][2].strip().lower() == 'int':
                _this_result[_l] = -1 if _value == '' else int(_value)
            elif GWGC_FORMAT[_l][2].strip().lower() == 'float':
                _this_result[_l] = float(math.nan) if _value == '' else float(_value)
            else:
                _this_result[_l] = _value
            _this_result['gid'] = int(_i+1)
        if _this_result['gid'] % GWGC_DIVISOR == 0 and _verbose:
            print(f"_this_result = {_this_result}")
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

    # loop around records
    _record = None
    for _record in _all_results:
        _gwgc_q3c = GwgcQ3cRecord(
            gid=_record['gid'],
            pgc=_record['pgc'],
            name=_record['name'],
            rah=_record['ra'],
            ra=float(_record['ra']) * 15.0,
            dec=_record['dec'],
            tt=_record['tt'],
            b_app=_record['b_app'],
            a=_record['a'],
            e_a=_record['e_a'],
            b=_record['b'],
            e_b=_record['e_b'],
            b_div_a=_record['b_div_a'],
            e_b_div_a=_record['e_b_div_a'],
            pa=_record['pa'],
            b_abs=_record['b_abs'],
            dist=_record['dist'],
            e_dist=_record['e_dist'],
            e_b_app=_record['e_b_app'],
            e_b_abs=_record['e_b_abs'])
        if _record['gid'] % GWGC_DIVISOR == 0 and _verbose:
            print(f'Inserting {_gwgc_q3c.serialized()}')
        # update database with results
        try:
            session.add(_gwgc_q3c)
            session.commit()
            if _record['gid'] % GWGC_DIVISOR == 0 and _verbose:
                print(f"Inserted object {_record['name']} database OK")
        except Exception as _e:
            session.rollback()
            raise Exception(f"Failed to insert object {_record['name']} database, error={_e}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description='Read GWGC Catalog', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--file', default=GWGC_CATALOG_FILE, help="""Input file [%(default)s]""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        gwgc_q3c_read(_file=_a.file.strip(), _verbose=bool(_a.verbose))
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
