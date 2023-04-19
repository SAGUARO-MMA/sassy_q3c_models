#!/usr/bin/env python3


# +
# import(s)
# -
# +
# import(s)
# -
from sassy_q3c_models.ps1_q3c_orm import *

import argparse
import os
import math


# +
# __doc__ string
# -
__doc__ = """ python3 ps1_q3c_read_bulk.py --help """


# +
# constant(s)
# -
DEF_NELMS = 50000
DEF_COLUMNS = 19


# +
# function: ps1_q3c_read_bulk()
# -
# noinspection PyBroadException
def ps1_q3c_read_bulk(_file: str = '', _nelms: int = DEF_NELMS, _verbose: bool = False):

    # check input(s)
    _file = os.path.abspath(os.path.expanduser(_file))
    _nelms = _nelms if _nelms > 0 else DEF_NELMS
    if not os.path.exists(_file):
        raise Exception(f"invalid input, _file={_file}")

    # connect to database
    session = None
    try:
        engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        get_session = sessionmaker(bind=engine)
        session = get_session()
    except Exception as _e:
        raise Exception(f'Failed to connect to database, error={_e}')

    # process file
    with open(_file, 'r') as _f:
        for _i, _l in enumerate(_f):
            if _l.strip()[0] == '#':
                continue
            _x = _l.strip().split(",")
            if len(_x) != DEF_COLUMNS:
                continue

            # parse line
            try:
                _objid=int(_x[0])
                _psps_objid=int(_x[1])
                _ra=float(_x[2])
                _dec=float(_x[3])
                _l=float(_x[4])
                _b=float(_x[5])
                _obj_class=_x[6]
                _prob_galaxy=float(_x[7])
                _prob_star=float(_x[8])
                _prob_qso=float(_x[9])
                _extra_class=float(_x[10])
                _celld_class=float(_x[11])
                _cellid_class=int(_x[12])
                _z_phot=float(_x[13])
                _z_err=float(_x[14])
                _z_zero=float(_x[15])
                _extra_photoz=int(_x[16])
                _celld_photoz=float(_x[17])
                _cellid_photoz=int(_x[18])
                _ps_score=math.nan

                if _verbose:
                    print(f"{_i} objid={_objid}, psps_objid={_psps_objid}, ra={_ra}, dec={_dec}, l={_l}, b={_b}, obj_class={_obj_class}, prob_galaxy={_prob_galaxy}, prob_star={_prob_star}, prob_qso={_prob_qso}, extra_class={_extra_class}, celld_class={_celld_class}, cellid_class={_cellid_class}, z_phot={_z_phot}, z_err={_z_err}, z_zero={_z_zero}, extra_photoz={_extra_photoz}, celld_photoz={_celld_photoz}, cellid_photoz={_cellid_photoz}, ps_score={_ps_score}")

            except Exception as _e2:
                print(f"ERROR: failed to parse line {_i}, '{_l}', error='{_e2}'")
                continue

            # create record
            _pr = None
            try:
                _pr = Ps1Q3cRecord(objid=_objid, psps_objid=_psps_objid, ra=_ra, dec=_dec, l=_l, b=_b, obj_class=_obj_class, prob_galaxy=_prob_galaxy, prob_star=_prob_star, prob_qso=_prob_qso, extra_class=_extra_class, celld_class=_celld_class, cellid_class=_cellid_class, z_phot=_z_phot, z_err=_z_err, z_zero=_z_zero, extra_photoz=_extra_photoz, celld_photoz=_celld_photoz, cellid_photoz=_cellid_photoz, ps_score=_ps_score)
            except Exception as _e3:
                print(f"ERROR: failed to create Ps1Q3cRecord(), error='{_e3}'")
                continue
            else:
                print(f"created Ps1Q3cRecord(), _pr={_pr.serialized()}")

            # insert into database
            try:
                    if _verbose:
                        print(f"inserting Ps1Q3cRecord() into database, _i={_i}")
                    #session.add(_pr)
                    if _i % _nelms == 0:
                        print(f"commiting Ps1Q3cRecord() into database, _i={_i}")
                        pass
                        #session.commit()
            except Exception as _e4:
                #session.rollback()
                print(f"Failed to insert Ps1Q3cRecord() into database, _i={_i}, error='{_e4}'")


    # close
    if hasattr(session, 'close'):
        session.close()


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description='Populate NonDetection Table', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument('--file', default='', help="""Input file [%(default)s]""")
    _p.add_argument('--nelms', default=DEF_NELMS, help="""Number of elements between screen updates [%(default)s]""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        ps1_q3c_read_bulk(_file=_a.file.strip(), _nelms=int(_a.nelms), _verbose=bool(_a.verbose))
    except Exception as _:
        print(f"{_}\n{__doc__}")
