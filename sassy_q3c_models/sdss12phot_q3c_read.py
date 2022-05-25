#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.sdss12phot_q3c_orm import *


# +
# __doc__ string
# -
__doc__ = """ python3 sdss12phot_q3c_read.py --help """


# +
# constant(s)
# -
SDSS12PHOT_Q3C_DIVISOR = 50000
SDSS12PHOT_Q3C_CATALOG_FILE = os.path.abspath(os.path.expanduser('sdss12_photometric_catalog.csv'))


# +
# function: sdss12phot_q3c_read()
# -
# noinspection PyBroadException
def sdss12phot_q3c_read(_file: str = '', _verbose: bool = False) -> None:

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
    _sid = 0
    _max_name = 0
    with open(_file, 'r') as _fd:
        for _line in _fd:
            _sid += 1

            # split up row and check the number of entries
            _row = _line.split(',')
            if len(_row) != SDSS12PHOT_COLUMNS:
                print(f"<ERROR> row contains {len(_row)} columns, expected {SDSS12PHOT_COLUMNS}")
                _sid -= 1
                continue

            # get clean data
            else:
                _sdss12phot_q3c, _sdss12phot_rec = {}, None
                try:
                    _sdss12phot_q3c['ra'] = float(_row[0].strip())
                except:
                    _sdss12phot_q3c['ra'] = math.nan

                try:
                    _sdss12phot_q3c['dec'] = float(_row[1].strip())
                except:
                    _sdss12phot_q3c['dec'] = math.nan

                try:
                    _sdss12phot_q3c['mode'] = int(_row[2].strip())
                except:
                    _sdss12phot_q3c['mode'] = -1

                _sdss12phot_q3c['q_mode'] = _row[3].strip()

                try:
                    _sdss12phot_q3c['classifier'] = int(_row[4].strip())
                except:
                    _sdss12phot_q3c['classifier'] = -1

                _sdss12phot_q3c['sdss12'] = _row[5].strip()
                _max_name = len(_sdss12phot_q3c['sdss12']) if len(_sdss12phot_q3c['sdss12']) > _max_name else _max_name

                _sdss12phot_q3c['m_sdss12'] = _row[6].strip()

                try:
                    _sdss12phot_q3c['obsdate'] = float(_row[7].strip())
                except:
                    _sdss12phot_q3c['obsdate'] = math.nan

                try:
                    _sdss12phot_q3c['quality'] = int(_row[8].strip())
                except:
                    _sdss12phot_q3c['quality'] = -1

                try:
                    _sdss12phot_q3c['umag'] = float(_row[9].strip())
                except:
                    _sdss12phot_q3c['umag'] = math.nan

                try:
                    _sdss12phot_q3c['e_umag'] = float(_row[10].strip())
                except:
                    _sdss12phot_q3c['e_umag'] = math.nan

                try:
                    _sdss12phot_q3c['gmag'] = float(_row[11].strip())
                except:
                    _sdss12phot_q3c['gmag'] = math.nan

                try:
                    _sdss12phot_q3c['e_gmag'] = float(_row[12].strip())
                except:
                    _sdss12phot_q3c['e_gmag'] = math.nan

                try:
                    _sdss12phot_q3c['rmag'] = float(_row[13].strip())
                except:
                    _sdss12phot_q3c['rmag'] = math.nan

                try:
                    _sdss12phot_q3c['e_rmag'] = float(_row[14].strip())
                except:
                    _sdss12phot_q3c['e_rmag'] = math.nan

                try:
                    _sdss12phot_q3c['imag'] = float(_row[15].strip())
                except:
                    _sdss12phot_q3c['imag'] = math.nan

                try:
                    _sdss12phot_q3c['e_imag'] = float(_row[16].strip())
                except:
                    _sdss12phot_q3c['e_imag'] = math.nan

                try:
                    _sdss12phot_q3c['zmag'] = float(_row[17].strip())
                except:
                    _sdss12phot_q3c['zmag'] = math.nan

                try:
                    _sdss12phot_q3c['e_zmag'] = float(_row[18].strip())
                except:
                    _sdss12phot_q3c['e_zmag'] = math.nan

                try:
                    _sdss12phot_q3c['zsp'] = float(_row[19].strip())
                except:
                    _sdss12phot_q3c['zsp'] = math.nan

                try:
                    _sdss12phot_q3c['zsh'] = float(_row[20].strip())
                except:
                    _sdss12phot_q3c['zsh'] = math.nan

                try:
                    _sdss12phot_q3c['e_zsh'] = float(_row[21].strip())
                except:
                    _sdss12phot_q3c['e_zsh'] = math.nan

                try:
                    _sdss12phot_q3c['lastcol'] = float(_row[22].strip())
                except:
                    _sdss12phot_q3c['lastcol'] = math.nan

                # create record
                try:
                    _sdss12phot_rec = Sdss12PhotQ3cRecord(sid=_sid, **_sdss12phot_q3c)
                except Exception as _x:
                    print(f"<ERROR> failed to create record _sdss12phot_rec={_sdss12phot_rec}, error={_x}")
                else:
                    if (_sid % SDSS12PHOT_Q3C_DIVISOR == 0) and _verbose:
                        print(f"created record _sdss12phot_rec={_sdss12phot_rec.serialized()} OK")

                # add record to database
                try:
                    session.add(_sdss12phot_rec)
                    session.commit()
                except Exception as _d:
                    session.rollback()
                    print(f"<ERROR> failed to insert record {_sdss12phot_rec.serialized()} into database, error={_d}")
                else:
                    if (_sid % SDSS12PHOT_Q3C_DIVISOR == 0) and _verbose:
                        print(f"inserted record {_sdss12phot_rec.serialized()} into database OK")

    # disconnec database
    session.close()


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description='Read SDSS12 Photometric Catalog', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--file', default=SDSS12PHOT_Q3C_CATALOG_FILE, help="""Input file [%(default)s]""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        sdss12phot_q3c_read(_file=_a.file.strip(), _verbose=bool(_a.verbose))
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
