#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.tns_q3c_orm import *


# +
# __doc__ string
# -
__doc__ = """ python3 tns_q3c_read.py --help """


# +
# constant(s)
# -
random.seed(os.getpid())
TNS_Q3C_CATALOG_FILE = os.path.abspath(os.path.expanduser('tns_public_objects.csv'))
TNS_DIVISOR = 5000


# +
# function: tns_q3c_read()
# -
# noinspection PyBroadException
def tns_q3c_read(_file: str = '', _verbose: bool = False) -> None:

    # check input(s)
    _file = os.path.abspath(os.path.expanduser(_file))
    if not os.path.exists(_file):
        raise Exception(f"invalid input, _file={_file}")

    # get data
    with open(_file, "r") as _f:
        _lines = _f.readlines()
    if not _lines:
        raise Exception(f"ERROR: {os.path.basename(_file)} has no data")

    # is the data correct?
    _date_now = f"{get_utc().split('T')[0]} 00:00:00"
    _date_csv = f"{_lines[0].strip()}"
    if _date_csv != _date_now:
        raise Exception(f"ERROR: {os.path.basename(_file)} has date '{_date_csv}' but today is '{_date_now}'")
    _lines.pop(0)

    # do we have the correct number of columns?
    _headers = [_v.strip().replace('"', '') for _v in _lines[0].strip().split(',')]
    if len(_headers) != TNS_COLUMNS:
        raise Exception(f"ERROR: {os.path.basename(_file)} has incorrect headers")
    _lines.pop(0)

    # munge rest of data
    _lines = [_v.strip().replace('","', '*').strip() for _v in _lines]

    # connect to database
    if _verbose:
        print(f"connecting to database postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    try:
        engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        get_session = sessionmaker(bind=engine)
        session = get_session()
    except Exception as _c:
        raise Exception(f"failed connecting to database "
                        f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}, error={_c}")
    else:
        if _verbose:
            print(f"connected to database postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME} OK")

    # read the data
    _rogue = ""
    for _tid, _e in enumerate(_lines):

        # get line
        _tns_q3c, _tns_rec = {}, None
        _el = [_v.replace('"', '').strip() for _v in _e.split("*")]

        # process line
        if len(_el) != TNS_COLUMNS:
            print(f"<ERROR> row contains {len(_el)} columns, expected {TNS_COLUMNS}")
            continue
        else:
            try:
                _tid += 1
                _tns_q3c['tid'] = int(_tid)
                _tns_q3c['objid'] = int(_el[0]) if _el[0].strip() != '' else -1
                _tns_q3c['name_prefix'] = _el[1]
                _tns_q3c['name'] = _el[2]
                _tns_q3c['ra'] = float(_el[3]) if _el[3].strip() != '' else math.nan
                _tns_q3c['declination'] = float(_el[4]) if _el[4].strip() != '' else math.nan
                _tns_q3c['redshift'] = float(_el[5]) if _el[5].strip() != '' else math.nan
                _tns_q3c['typeid'] = int(_el[6]) if _el[6].strip() != '' else -1
                _tns_q3c['objtype'] = _el[7]
                _tns_q3c['reporting_groupid'] = int(_el[8]) if _el[8].strip() != '' else -1
                _tns_q3c['reporting_group'] = _el[9]
                _tns_q3c['source_groupid'] = int(_el[10]) if _el[10].strip() != '' else -1
                _tns_q3c['source_group'] = _el[11]
                _tns_q3c['discoverydate'] = _el[12]
                _tns_q3c['discoverymag'] = float(_el[13]) if _el[13].strip() != '' else math.nan
                _tns_q3c['discmagfilter'] = int(_el[14]) if _el[14].strip() != '' else -1
                _tns_q3c['filtername'] = _el[15]
                _tns_q3c['reporters'] = _el[16]
                _tns_q3c['time_received'] = _el[17]
                _tns_q3c['internal_names'] = _el[18]
                _tns_q3c['creationdate'] = _el[19]
                _tns_q3c['lastmodified'] = _el[20]
                _tns_rec = TnsQ3cRecord(**_tns_q3c)
            except Exception as _e:
                _tid -= 1
                print(f"<ERROR> failed to create dictionary _tns_q3c={_tns_q3c}, _tid={_tid}, _el={_el}, error={_e}")
            else:

                # create record
                try:
                    _tns_rec = TnsQ3cRecord(**_tns_q3c)
                except Exception as _x:
                    print(f"<ERROR> failed to create record _tns_rec={_tns_rec}, error={_x}")

                # add record to database
                try:
                    session.add(_tns_rec)
                    session.commit()
                except Exception as _d:
                    session.rollback()
                    print(f"<ERROR> failed to insert record {_tns_rec.serialized()} into database, error={_d}")
                else:
                    if _verbose and (_tid % TNS_DIVISOR == 0):
                        print(f"inserted record {_tns_rec.serialized()} into database OK")

    # close database
    session.close()


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description='Read TNS Catalog', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--file', default=TNS_Q3C_CATALOG_FILE, help="""Input file [%(default)s]""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        tns_q3c_read(_file=_a.file.strip(), _verbose=bool(_a.verbose))
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
