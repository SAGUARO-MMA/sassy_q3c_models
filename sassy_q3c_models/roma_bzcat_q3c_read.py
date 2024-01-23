#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.roma_bzcat_q3c_orm import *
from astropy import units as u
from astropy.coordinates import SkyCoord


# +
# __doc__ string
# -
__doc__ = """ python3 roma_bzcat_q3c_read.py --help """


# +
# constant(s)
# -
ROMA_BZCAT_Q3C_CATALOG_FILE = os.path.abspath(os.path.expanduser('/science/catalogs/roma_bzcat/Roma_BZCAT.tsv'))


# +
# function: convert_ra_dec()
# -
def convert_ra_dec(_radec: str = '') -> tuple:
    try:
        _coord = SkyCoord(_radec, unit=(u.hourangle, u.deg))
        return _coord.ra.value, _coord.dec.value
    except:
        return math.nan, math.nan


# +
# function: roma_bzcat_q3c_read()
# -
# noinspection PyBroadException
def roma_bzcat_q3c_read(_file: str = ROMA_BZCAT_Q3C_CATALOG_FILE, _verbose: bool = False) -> None:

    # check input(s)
    _file = os.path.abspath(os.path.expanduser(_file))
    if not os.path.exists(_file):
        print(f"<ERROR> invalid input, _file={_file}")
        return

    # connect to database
    try:
        if _verbose:
            print(f"connecting to database postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        get_session = sessionmaker(bind=engine)
        session = get_session()
    except Exception as _e0:
        print(f"<ERROR> failed connecting to database postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}, error='{_e0}'")
        return

    # read the file
    _rid = 1
    _header = []
    with open(_file, 'r') as _fd:
        for _line in _fd:

            # initialize
            _rec, _row, _dict = None, [], {}

            # get header
            if '#Seq' in _line.strip():
                _header = _line.strip()[1:].split('|')
                for _v in _header:
                    if _v not in ROMA_BZCAT_HEADERS:
                        print(f"<ERROR> unexpected {_header} != {ROMA_BZCAT_HEADERS}")
                        return

            # get elements
            elif _line.strip()[0] != '#':
                _row = _line.strip().split('|')
                if len(_row) != ROMA_BZCAT_COLUMNS:
                    print(f"<ERROR> row contains {len(_row)} columns, expected {ROMA_BZCAT_COLUMNS}")
                    continue

                # create dictionary
                _dict = dict(zip(_header, _row))
                if [_k for _k in _dict] == ROMA_BZCAT_HEADERS:
                    _dict = dict(zip(ROMA_BZCAT_KEYS, _row))
                    if not verify_keys(_d=_dict, _s=set(ROMA_BZCAT_KEYS)):
                        print(f"<ERROR> _dict = {_dict} is invalid")
                        continue
                print(f"<INFO> _dict={_dict}")

                # create orm object
                _rec = None
                _tval = convert_ra_dec(f"{_dict['ra']} {_dict['dec']}") if (_dict['ra'].strip()!='' and _dict['dec'].strip()!='') else (math.nan, math.nan)
                try:
                    _rec = RomaBzcatQ3cRecord(
                        rid=_rid,
                        name=_dict['name'].strip(),
                        ra=_tval[0],
                        dec=_tval[1],
                        l=float(_dict['l']) if _dict['l'].strip() != '' else math.nan,
                        b=float(_dict['b']) if _dict['b'].strip() != '' else math.nan,
                        z=float(_dict['z']) if _dict['z'].strip() != '' else math.nan,
                        z_err=float(_dict['z_err']) if (_dict['z_err'].strip()!='' and _dict['z_err'].strip()!='?') else math.nan,
                        rmag=float(_dict['rmag']) if _dict['rmag'].strip() != '' else math.nan,
                        classification=_dict['classification'].strip(),
                        flux=float(_dict['flux']) if _dict['flux'].strip() != '' else math.nan,
                        flux_143=float(_dict['flux_143']) if _dict['flux_143'].strip() != '' else math.nan,
                        flux_xray=float(_dict['flux_xray']) if _dict['flux_xray'].strip() != '' else math.nan,
                        flux_fermi=float(_dict['flux_fermi']) if _dict['flux_fermi'].strip() != '' else math.nan,
                        aro=float(_dict['aro']) if _dict['aro'].strip() != '' else math.nan
                    )
                except Exception as _e1:
                    print(f"<ERROR> failed to create record _rec={_rec}, error='{_e1}'")
                    continue

                # add record to database
                try:
                    session.add(_rec)
                    session.commit()
                    print(f"_rid={_rid}, commiting record(s) OK")
                except Exception as _e2:
                    session.rollback()
                    print(f"<ERROR> _rid={_rid}, failed to insert record {_rec.serialized()} into database, error='{_e2}'")
                    continue
                else:      
                    print(f"_rid={_rid}, inserted record {_rec.serialized()} into database OK")

                # incement counter
                _rid += 1

    # disconnect database
    if _verbose:
        print(f"disconnecting to database postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    session.commit()
    session.close()


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description='Read Roma BZCAT File', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--file', default=ROMA_BZCAT_Q3C_CATALOG_FILE, help="""Input file [%(default)s]""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        roma_bzcat_q3c_read(_file=_a.file.strip(), _verbose=bool(_a.verbose))
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
