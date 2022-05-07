#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.glade_plus_q3c_orm import *


# +
# __doc__ string
# -
__doc__ = """ python3 glade_plus_q3c_read.py --help """


# +
# constant(s)
# -
random.seed(os.getpid())
GLADE_PLUS_Q3C_DIVISOR = 50000
GLADE_PLUS_Q3C_CATALOG_FILE = os.path.abspath(os.path.expanduser('GLADE+.txt'))


# +
# function: glade_plus_q3c_read()
# -
# noinspection PyBroadException
def glade_plus_q3c_read(_file: str = '', _verbose: bool = False) -> None:

    # check input(s)
    _file = os.path.abspath(os.path.expanduser(_file))
    if not isinstance(_file, str) or not os.path.exists(_file):
        raise Exception(f"invalid input, _file={_file}")

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

    # read the file
    _gid = 0
    with open(_file, 'r') as _fd:
        for _line in _fd:
            _gid += 1

            # split up row and check the number of entries
            _row = _line.split()
            if len(_row) != GLADE_PLUS_COLUMNS:
                print(f"<ERROR> row contains {len(_row)} columns, expected {GLADE_PLUS_COLUMNS}")
                _gid -= 1

            # get clean data
            else:
                _glade_plus_q3c, _glade_plus_rec = {}, None
                try:
                    _glade_plus_q3c['gn'] = int(_row[0]) if _row[0].strip() != 'null' else -1
                    _glade_plus_q3c['pgc'] = int(_row[1]) if _row[1].strip() != 'null' else -1
                    _glade_plus_q3c['gwgc'] = _row[2]
                    _glade_plus_q3c['hyperleda'] = _row[3]
                    _glade_plus_q3c['twomass'] = _row[4]
                    _glade_plus_q3c['wise'] = _row[5]
                    _glade_plus_q3c['sdss'] = _row[6]
                    _glade_plus_q3c['o_flag'] = _row[7]
                    _glade_plus_q3c['ra'] = float(_row[8]) if _row[8].strip() != 'null' else math.nan
                    _glade_plus_q3c['dec'] = float(_row[9]) if _row[9].strip() != 'null' else math.nan
                    _glade_plus_q3c['b'] = float(_row[10]) if _row[10].strip() != 'null' else math.nan
                    _glade_plus_q3c['b_err'] = float(_row[11]) if _row[11].strip() != 'null' else math.nan
                    _glade_plus_q3c['b_flag'] = int(_row[12]) if _row[12].strip() != 'null' else -1
                    _glade_plus_q3c['b_abs'] = float(_row[13]) if _row[13].strip() != 'null' else math.nan
                    _glade_plus_q3c['j'] = float(_row[14]) if _row[14].strip() != 'null' else math.nan
                    _glade_plus_q3c['j_err'] = float(_row[15]) if _row[15].strip() != 'null' else math.nan
                    _glade_plus_q3c['h'] = float(_row[16]) if _row[16].strip() != 'null' else math.nan
                    _glade_plus_q3c['h_err'] = float(_row[17]) if _row[17].strip() != 'null' else math.nan
                    _glade_plus_q3c['k'] = float(_row[18]) if _row[18].strip() != 'null' else math.nan
                    _glade_plus_q3c['k_err'] = float(_row[19]) if _row[19].strip() != 'null' else math.nan
                    _glade_plus_q3c['w1'] = float(_row[20]) if _row[20].strip() != 'null' else math.nan
                    _glade_plus_q3c['w1_err'] = float(_row[21]) if _row[21].strip() != 'null' else math.nan
                    _glade_plus_q3c['w2'] = float(_row[22]) if _row[22].strip() != 'null' else math.nan
                    _glade_plus_q3c['w2_err'] = float(_row[23]) if _row[23].strip() != 'null' else math.nan
                    _glade_plus_q3c['w1_flag'] = int(_row[24]) if _row[24].strip() != 'null' else -1
                    _glade_plus_q3c['b_j'] = float(_row[25]) if _row[25].strip() != 'null' else math.nan
                    _glade_plus_q3c['b_j_err'] = float(_row[26]) if _row[26].strip() != 'null' else math.nan
                    _glade_plus_q3c['z_helio'] = float(_row[27]) if _row[27].strip() != 'null' else math.nan
                    _glade_plus_q3c['z_cmb'] = float(_row[28]) if _row[28].strip() != 'null' else math.nan
                    _glade_plus_q3c['z_flag'] = int(_row[29]) if _row[29].strip() != 'null' else -1
                    _glade_plus_q3c['v_err'] = float(_row[30]) if _row[30].strip() != 'null' else math.nan
                    _glade_plus_q3c['z_err'] = float(_row[31]) if _row[31].strip() != 'null' else math.nan
                    _glade_plus_q3c['d_l'] = float(_row[32]) if _row[32].strip() != 'null' else math.nan
                    _glade_plus_q3c['d_l_err'] = float(_row[33]) if _row[33].strip() != 'null' else math.nan
                    _glade_plus_q3c['dist_flag'] = int(_row[34]) if _row[34].strip() != 'null' else -1
                    _glade_plus_q3c['mstar'] = float(_row[35]) if _row[35].strip() != 'null' else math.nan
                    _glade_plus_q3c['mstar_err'] = float(_row[36]) if _row[36].strip() != 'null' else math.nan
                    _glade_plus_q3c['mrate'] = float(_row[37]) if _row[37].strip() != 'null' else math.nan
                    _glade_plus_q3c['mrate_err'] = float(_row[38]) if _row[38].strip() != 'null' else math.nan
                except Exception as _e:
                    print(f"{_gid}: _line={_line}")
                    print(f"{_gid}: _row={_row}, len={len(_row)}")
                    print(f"<ERROR> failed to create dictionary _glade_plus_q3c={_glade_plus_q3c}, error={_e}")
                else:
                    if (_gid % GLADE_PLUS_Q3C_DIVISOR == 0) and _verbose:
                        print(f"{_gid}: _line={_line}")
                        print(f"{_gid}: _row={_row}, len={len(_row)}")
                        print(f"created _glade_plus_q3c={_glade_plus_q3c} OK")

                # create record
                try:
                    _glade_plus_rec = GladePlusQ3cRecord(gid=_gid, **_glade_plus_q3c)
                except Exception as _x:
                    print(f"<ERROR> failed to create record _glade_plus_rec={_glade_plus_rec}, error={_x}")
                else:
                    if (_gid % GLADE_PLUS_Q3C_DIVISOR == 0) and _verbose:
                        print(f"created record _glade_plus_rec={_glade_plus_rec.serialized()} OK")

                # add record to database
                try:
                    session.add(_glade_plus_rec)
                    session.commit()
                except Exception as _d:
                    session.rollback()
                    print(f"<ERROR> failed to insert record {_glade_plus_rec.serialized()} into database, error={_d}")
                else:
                    if (_gid % GLADE_PLUS_Q3C_DIVISOR == 0) and _verbose:
                        print(f"inserted record {_glade_plus_rec.serialized()} into database OK")

    session.close()


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description='Read GLADE+ Catalog', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--file', default=GLADE_PLUS_Q3C_CATALOG_FILE, help="""Input file [%(default)s]""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        glade_plus_q3c_read(_file=_a.file.strip(), _verbose=bool(_a.verbose))
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
