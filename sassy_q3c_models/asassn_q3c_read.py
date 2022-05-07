#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.asassn_q3c_orm import *


# +
# __doc__ string
# -
__doc__ = """ python3 asassn_q3c_read.py --help """


# +
# constant(s)
# -
ASASSN_BAD_VALUES = ['', 'null', '-']
ASASSN_CATALOG_FILE = os.path.abspath(os.path.expanduser('asassn_catalog.csv'))
ASASSN_DIVISOR = 10000
ASASSN_FALSE_VALUES = ['f', 'false', '0']
ASASSN_TRUE_VALUES = ['t', 'true', '1']
ASASSN_TYPES = {'asassn_id': 'str', 'source_id': 'str', 'asassn_name': 'str', 'other_names': 'str', 'ra': 'float',
                'dec': 'float', 'l': 'float', 'b': 'float', 'mean_vmag': 'float', 'amplitude': 'float',
                'period': 'float', 'variable_type': 'str', 'class_probability': 'float', 'lksl_statistic': 'float',
                'rfr_score': 'float', 'epoch_hjd': 'float', 'gdr2_id': 'bigint', 'phot_g_mean_mag': 'float',
                'e_phot_g_mean_mag': 'float', 'phot_bp_mean_mag': 'float', 'e_phot_bp_mean_mag': 'float',
                'phot_rp_mean_mag': 'float', 'e_phot_rp_mean_mag': 'float', 'bp_rp': 'float', 'parallax': 'float',
                'parallax_error': 'float', 'parallax_over_error': 'float', 'pmra': 'float', 'pmra_error': 'float',
                'pmdec': 'float', 'pmdec_error': 'float', 'vt': 'float', 'dist': 'float', 'allwise_id': 'str',
                'j_mag': 'float', 'e_j_mag': 'float', 'h_mag': 'float', 'e_h_mag': 'float', 'k_mag': 'float',
                'e_k_mag': 'float', 'w1_mag': 'float', 'e_w1_mag': 'float', 'w2_mag': 'float', 'e_w2_mag': 'float',
                'w3_mag': 'float', 'e_w3_mag': 'float', 'w4_mag': 'float', 'e_w4_mag': 'float', 'j_k': 'float',
                'w1_w2': 'float', 'w3_w4': 'float', 'apass_dr9_id': 'bigint', 'apass_vmag': 'float',
                'e_apass_vmag': 'float', 'apass_bmag': 'float', 'e_apass_bmag': 'float', 'apass_gpmag': 'float',
                'e_apass_gpmag': 'float', 'apass_rpmag': 'float', 'e_apass_rpmag': 'float', 'apass_ipmag': 'float',
                'e_apass_ipmag': 'float', 'b_v': 'float', 'e_b_v': 'float', 'vector_x': 'float', 'vector_y': 'float',
                'vector_z': 'float', 'reference': 'str', 'periodic': 'bool', 'classified': 'bool',
                'asassn_discovery': 'bool', 'created_at': 'str', 'updated_at': 'str', 'edr3_source_id': 'str',
                'galex_id': 'str', 'fuvmag': 'float', 'e_fuvmag': 'float', 'nuvmag': 'float', 'e_nuvmag': 'float',
                'tic_id': 'str', 'pm': 'float', 'ruwe': 'float'}


# +
# function: asassn_q3c_read()
# -
# noinspection PyBroadException
def asassn_q3c_read(_file: str = ASASSN_CATALOG_FILE, _delimeter: str = ',', _verbose: bool = False) -> None:

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
    _aid, _first_line = 0, True
    with open(_file, 'r') as _fd:

        for _line in _fd:
            if _first_line:
                _first_line = False
                _columns = _line.replace("\n", "").strip().split(sep=f"{_delimeter}")
                continue
            _aid += 1

            # split up row and check the number of entries
            _line = _line.replace("\n", "").strip()
            _row = _line.split(sep=f"{_delimeter}")
            if len(_row) != ASASSN_COLUMNS:
                print(f"<ERROR> _aid={_aid}, _row='{_row}' contains {len(_row)} columns, "
                      f"expected {len(ASASSN_COLUMNS)}")
                _aid -= 1

            # get clean data
            else:
                _asassn_q3c, _asassn_rec = None, None
                try:
                    _asassn_q3c = dict(zip(ASASSN_HEADERS, _row))
                    if (_aid % ASASSN_DIVISOR == 0) and _verbose:
                        print(f"<OK> _aid={_aid}, _row={_row}, _asassn_q3c={_asassn_q3c}")
                    for _k, _v in _asassn_q3c.items():
                        if ASASSN_TYPES.get(_k) == 'bool':
                            if _v.lower().strip() in ASASSN_TRUE_VALUES:
                                _asassn_q3c[_k] = True
                            else:
                                _asassn_q3c[_k] = False
                        elif ASASSN_TYPES.get(_k) == 'float':
                            if _v.lower().strip() in ASASSN_BAD_VALUES:
                                _asassn_q3c[_k] = math.nan
                            else:
                                try:
                                    _asassn_q3c[_k] = float(_v)
                                except Exception as _ef:
                                    print(f"<ERROR> _aid={_aid}, failed to convert "
                                          f"_asassn_q3c[{_k}]={_asassn_q3c[_k]} to float, error='{_ef}'")
                                    _asassn_q3c[_k] = math.nan
                        elif ASASSN_TYPES.get(_k) == 'int' or ASASSN_TYPES.get(_k) == 'bigint':
                            if _v.lower().strip() in ASASSN_BAD_VALUES:
                                _asassn_q3c[_k] = -1
                            else:
                                try:
                                    _asassn_q3c[_k] = int(_v)
                                except Exception as _ei:
                                    print(f"<ERROR> _aid={_aid}, failed to convert "
                                          f"_asassn_q3c[{_k}]={_asassn_q3c[_k]} to int, error='{_ei}'")
                                    _asassn_q3c[_k] = -1
                        else:
                            pass
                except Exception as _e:
                    print(f"<ERROR> _aid={_aid}, _row={_row}, _asassn_q3c={_asassn_q3c}, error='{_e}'")
                else:
                    if (_aid % ASASSN_DIVISOR == 0) and _verbose:
                        print(f"<OK> _aid={_aid}, created _asassn_q3c={_asassn_q3c} OK")

                # create record
                try:
                    _asassn_rec = AsAssnQ3cRecord(aid=_aid, **_asassn_q3c)
                except Exception as _x:
                    print(f"<ERROR> failed to create record _asassn_rec={_asassn_rec}, error={_x}")
                else:
                    if (_aid % ASASSN_DIVISOR == 0) and _verbose:
                        print(f"created record _asassn_rec={_asassn_rec.serialized()} OK")

                # add record to database
                try:
                    pass
                    session.add(_asassn_rec)
                    session.commit()
                except Exception as _d:
                    session.rollback()
                    print(f"<ERROR> failed to insert record {_asassn_rec.serialized()} into database, error={_d}")
                else:
                    if (_aid % ASASSN_DIVISOR == 0) and _verbose:
                        print(f"inserted record {_asassn_rec.serialized()} into database OK")

    session.close()


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description='Read ASASSN Catalog', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--file', default=ASASSN_CATALOG_FILE, help="""Input file [%(default)s]""")
    _p.add_argument(f'--delimeter', default=",", help="""Input file [%(default)s]""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        asassn_q3c_read(_file=_a.file.strip(), _delimeter=f'{_a.delimeter}', _verbose=bool(_a.verbose))
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
