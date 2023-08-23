#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.ps1_q3c_orm import *
from sassy_q3c_models.ps1_q3c_orm_filters import *

import argparse
import astropy.io.fits as fits
import os
import math
import numpy


# +
# __doc__ string
# -
__doc__ = """ python3 ps1_q3c_update_bulk.py --help """


# +
# constant(s)
# -
DEF_FILE = '/science/catalogs/ps1_psc/hlsp_ps1-psc_ps1_gpc1_0_multi_v1_cat.fits'
DEF_NELMS = 50000


# +
# function: ps1_q3c_update_bulk()
# -
# noinspection PyBroadException
def ps1_q3c_update_bulk(_file: str = '', _nelms: int = DEF_NELMS, _verbose: bool = False):

    # check input(s)
    _file = os.path.abspath(os.path.expanduser(_file))
    if not os.path.exists(_file):
        raise Exception(f"invalid input, _file={_file}")
    _nelms = _nelms if _nelms > 0 else DEF_NELMS

    # connect to database
    session = None
    try:
        engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        get_session = sessionmaker(bind=engine)
        session = get_session()
    except Exception as _e1:
        raise Exception(f'Failed to connect to database, error={_e1}')

    # process file
    with fits.open(_file) as _f:
        objid = _f[1].data['objid']
        ps_score = _f[1].data['ps_score']

        # report mismatch
        if len(objid) != len(ps_score):
            print(f"<ERROR> data mismatch in '{_file}': objid and ps_score arrays have different sizes!")
            close(_f)

        # update record(s)
        else:
            for _i, _e in enumerate(objid):
                try:
                    session.query(Ps1Q3cRecord).filter(Ps1Q3cRecord.objid==int(_e)).update({'ps_score': float(ps_score[_i])}, synchronize_session='evaluate')
                    if _verbose and (_i % _nelms) == 0:
                       print(f"record update for objid={_e} with ps_score={ps_score[_i]}")
                       session.commit()
                except Exception as _e2:
                    session.rollback()
                    print(f"<ERROR> failed to update database, _i={_i}, _e={_e}, error='{_e2}'")
                    continue

    # close
    session.commit()
    if hasattr(session, 'close'):
        session.close()


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description='Update Ps1Q3c Table', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument('--file', default=DEF_FILE, help="""Input file [%(default)s]""")
    _p.add_argument('--nelms', default=DEF_NELMS, help="""Number of elements between screen updates [%(default)s]""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        ps1_q3c_update_bulk(_file=_a.file.strip(), _nelms=int(_a.nelms), _verbose=bool(_a.verbose))
    except Exception as _:
        print(f"{_}\n{__doc__}")
