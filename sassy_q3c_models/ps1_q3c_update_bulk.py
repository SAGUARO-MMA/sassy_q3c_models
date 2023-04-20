#!/usr/bin/env python3


# +
# import(s)
# -
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

DB_HOST = 'localhost'
DB_NAME = 'sassy'
DB_PASS = 'SASSy_520'
DB_PORT = 5432
DB_USER = 'sassy'


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
        if _verbose:
            print(_f.info())
            print(_f[0].header.cards)
        objid = _f[1].data['objid']
        ps_score = _f[1].data['ps_score']
        if _verbose:
            print(f"objid={objid}, type={type(objid)}, length={len(objid)}")
            print(f"ps_score={ps_score}, type={type(ps_score)}, length={len(ps_score)}")

        # update record(s)
        for _i, _e in enumerate(objid):
            if _i > 5:
                break
            try:
                query = session.query(Ps1Q3cRecord)
                query = ps1_q3c_orm_filters(query, {'objid': int(_e)})
                for _r in Ps1Q3cRecord.serialize_list(query.all()):
                    # if _verbose and (_i % _nelms) == 0:
                    print(f"objid {_e}, ps_score={ps_score[_i]}, _r={_r}")
                    if 'ps_score' in _r and f"{_r['ps_score']}"=="nan":
                        _r['ps_score'] = ps_score[_i]
                        # if _verbose and (_i % _nelms) == 0:
                        print(f"updating objid {_e}, ps_score={ps_score[_i]}, _r={_r}")
                        # session.update(_pr)
                        # if _verbose and (_i % _nelms == 0):
                        #     print(f"commiting Ps1Q3cRecord() into database, _i={_i}")
                        #     session.commit()
            except Exception as _e2:
                # session.rollback()
                print(f"<ERROR> failed to lookup database, error='{_e2}'")
                continue


        # update database
        #try:
        #except Exception as _e4:
        #    print(f"Failed to insert Ps1Q3cRecord() into database, _pr={_pr.serialized()}, _i={_i}, error='{_e4}'")

    # close
    #session.commit()
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
    #try:
    ps1_q3c_update_bulk(_file=_a.file.strip(), _nelms=int(_a.nelms), _verbose=bool(_a.verbose))
    #except Exception as _:
    #    print(f"{_}\n{__doc__}")
