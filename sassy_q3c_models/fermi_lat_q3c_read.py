#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.fermi_lat_q3c_orm import *


# +
# __doc__ string
# -
__doc__ = """ python3 fermi_lat_q3c_read.py --help """


# +
# constant(s)
# -
FERMI_LAT_Q3C_CATALOG_FILE = os.path.abspath(os.path.expanduser('/science/catalogs/fermi_lat/J_MNRAS_490_4770.tsv'))


# +
# function: fermi_lat_q3c_read()
# -
# noinspection PyBroadException
def fermi_lat_q3c_read(_file: str = FERMI_LAT_Q3C_CATALOG_FILE, _verbose: bool = False) -> None:

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
    _fid = 1
    _header = []
    with open(_file, 'r') as _fd:
        for _line in _fd:

            # initialize
            _rec, _row, _dict = None, [], {}

            # get header
            # ['Name', 'GLAT', 'GLON', 'lBLLac', 'PBLLac', 'PFSRQ', 'Class', 'lBLLacLit', 'Classlit', 'Simbad', 'RA', 'Dec']
            # ['name', 'b', 'l', 'lbllac', 'pbllac', 'pfsrq', 'classification', 'lbllaclit', 'classlit', 'simbad', 'ra', 'dec']
            if '#Name' in _line.strip():
                print(f"<INFO> _line[1:] = {_line[1:]}")
                _header = _line.strip()[1:].split('|')
                print(f"<INFO> _header = {_header}")
                for _v in _header:
                    if _v not in FERMI_LAT_HEADERS:
                        print(f"<ERROR> unexpected {_header} != {FERMI_LAT_HEADERS}")
                        return

            # get elements
            elif _line.strip()[0] != '#':
                _row = _line.strip().split('|')
                if len(_row) != FERMI_LAT_COLUMNS:
                    print(f"<ERROR> row contains {len(_row)} columns, expected {FERMI_LAT_COLUMNS}")
                    continue

                # create dictionary
                _dict = dict(zip(_header, _row))
                if [_k for _k in _dict] == FERMI_LAT_HEADERS:
                    _dict = dict(zip(FERMI_LAT_KEYS, _row))
                    if not verify_keys(_d=_dict, _s=set(FERMI_LAT_KEYS)):
                        print(f"<ERROR> _dict = {_dict} is invalid")
                        continue
                print(f"<INFO> _dict={_dict}")

                # create orm object
                _rec = None
                try:
                    _rec = FermiLatQ3cRecord(
                        fid=_fid,
                        name=_dict['name'].strip(),
                        b=float(_dict['b']) if _dict['b'].strip() != '' else math.nan,
                        l=float(_dict['l']) if _dict['l'].strip() != '' else math.nan,
                        lbllac=float(_dict['lbllac']) if _dict['lbllac'].strip() != '' else math.nan,
                        pbllac=float(_dict['pbllac']) if _dict['pbllac'].strip() != '' else math.nan,
                        pfsrq=float(_dict['pfsrq']) if _dict['pfsrq'].strip() != '' else math.nan,
                        classification=_dict['classification'].strip(),
                        lbllaclit=float(_dict['lbllaclit']) if _dict['lbllaclit'].strip() != '' else math.nan,
                        classlit=_dict['classlit'].strip(),
                        simbad=_dict['simbad'].strip(),
                        ra=float(_dict['ra']) if _dict['ra'].strip() != '' else math.nan,
                        dec=float(_dict['dec']) if _dict['dec'].strip() != '' else math.nan
                    )

                except Exception as _e1:
                    print(f"<ERROR> failed to create record _rec={_rec}, error='{_e1}'")
                    continue

                # add record to database
                try:
                    session.add(_rec)
                    session.commit()
                    print(f"_fid={_fid}, committed record {_rec.serialized()} into database OK")
                except Exception as _e2:
                    session.rollback()
                    print(f"<ERROR> _fid={_fid}, failed to insert record {_rec.serialized()} into database, error='{_e2}'")
                    continue
                else:      
                    print(f"_fid={_fid}, inserted record {_rec.serialized()} into database OK")

                # incement counter
                _fid += 1

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
    _p = argparse.ArgumentParser(description='Read Fermi LAT File', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--file', default=FERMI_LAT_Q3C_CATALOG_FILE, help="""Input file [%(default)s]""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        fermi_lat_q3c_read(_file=_a.file.strip(), _verbose=bool(_a.verbose))
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
