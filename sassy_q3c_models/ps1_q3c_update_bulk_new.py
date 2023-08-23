#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.ps1_q3c_orm import *
from sassy_q3c_models.ps1_q3c_orm_filters import *

import argparse
import csv
import os
import math
import numpy


# +
# __doc__ string
# -
__doc__ = """ python3 ps1_q3c_update_bulk_new.py --help """


# +
# constant(s)
# -
DEF_FILE = '/science/catalogs/ps1/MyTable_p89_p90.csv'
DEF_NELMS = 50000

PS1_UPDATE_HEADERS = ['objID', 'objName', 'objInfoFlag', 'qualityFlag', 'nDetections', 'raMean', 'decMean', 
                      'raMeanErr', 'decMeanErr', 'gMeanPSFMag', 'gMeanPSFMagErr', 'rMeanPSFMag', 'rMeanPSFMagErr', 
                      'iMeanPSFMag', 'iMeanPSFMagErr', 'zMeanPSFMag', 'zMeanPSFMagErr', 'yMeanPSFMag', 'yMeanPSFMagErr']

# +
# function: ps1_q3c_update_bulk_new()
# -
# noinspection PyBroadException
def ps1_q3c_update_bulk_new(_file: str = '', _nelms: int = DEF_NELMS, _verbose: bool = False):

    # check input(s)
    _file = os.path.abspath(os.path.expanduser(_file))
    if not os.path.exists(_file):
        raise Exception(f"invalid input, _file={_file}")
    if not _file.lower().endswith('csv'):
        raise Exception(f'Unsupported file type (not .csv, .tsv)')
    _nelms = _nelms if _nelms > 0 else DEF_NELMS

    # set variable(s)
    _delimiter = ','
    _num = 0
    _gmags = 0
    _rmags = 0
    _imags = 0
    _ymags = 0
    _zmags = 0

    # get number of lines in file
    with open(_file, 'r') as _fd:
        _num = sum(1 for _l in _fd if (_l.strip() != '' and _l.strip()[0] not in r'#%!<>+\/'))
    _num -= 1
    if _verbose:
        print(f"'{_file}' is a csv file with {_num} data elements")

    # read the file
    _columns = {}
    with open(_file, 'r') as _fd:
        _r = csv.reader(_fd, delimiter=_delimiter)
        _headers = next(_r, None)

        # separate header line into column headings
        for _h in _headers:
            _columns[_h] = []

        # read rest of file into lists associated with each column heading
        for _row in _r:
            for _h, _v in zip(_headers, _row):
                _columns[_h].append(_v.strip())
    if _headers == PS1_UPDATE_HEADERS and _verbose:
        print(f"header check passed")

    # sanity check
    if len(_columns)*_num != sum([len(_v) for _v in _columns.values()]):
        raise Exception(f'Irregular number of elements in {_file}, please check {_file}')
    if _verbose:
        print(f"sanity check passed")

    # change the dictionary keys to remove unwanted characters
    for _k in list(_columns.keys()):
        _columns[_k.translate({ord(i): None for i in ' !@#$'})] = _columns.pop(_k)

    # check we got all the allowed headers
    if not (all(_k in _columns for _k in PS1_UPDATE_HEADERS)):
        raise Exception(f'Failed to get all allowed headers, please check {_file}'
                        f'\nfields expected are {PS1_UPDATE_HEADERS}')
    if _verbose:
        print(f"data check passed")

    # connect to database
    session = None
    try:
        engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        get_session = sessionmaker(bind=engine)
        session = get_session()
    except Exception as _e1:
        raise Exception(f'Failed to connect to database, error={_e1}')
    if _verbose:
        print(f"database connect passed")

    # loop around records
    for _i in range(0, _num):

        # data
        _data = {}
        _data = {**_data, **{'objname': _columns['objName'][_i]}}
        _data = {**_data, **{'objinfoflag': int(_columns['objInfoFlag'][_i])}}
        _data = {**_data, **{'qualityflag': int(_columns['qualityFlag'][_i])}}
        _data = {**_data, **{'ndetections': int(_columns['nDetections'][_i])}}
        _data = {**_data, **{'ramean': float(_columns['raMean'][_i])}}
        _data = {**_data, **{'decmean': float(_columns['decMean'][_i])}}
        _data = {**_data, **{'rameanerr': float(_columns['raMeanErr'][_i])}}
        _data = {**_data, **{'decmeanerr': float(_columns['decMeanErr'][_i])}}

        _gmag, _gmagerr = float(_columns['gMeanPSFMag'][_i]), float(_columns['gMeanPSFMagErr'][_i])
        if _gmag != -999.0:
            _gmags += 1
        _data = {**_data, **{'gmeanpsfmag': _gmag, 'gmeanpsfmagerr': _gmagerr}}

        _rmag, _rmagerr = float(_columns['rMeanPSFMag'][_i]), float(_columns['rMeanPSFMagErr'][_i])
        if _rmag != -999.0:
            _rmags += 1
        _data = {**_data, **{'rmeanpsfmag': _rmag, 'rmeanpsfmagerr': _rmagerr}}

        _imag, _imagerr = float(_columns['iMeanPSFMag'][_i]), float(_columns['iMeanPSFMagErr'][_i])
        if _imag != -999.0:
            _imags += 1
        _data = {**_data, **{'imeanpsfmag': _imag, 'imeanpsfmagerr': _imagerr}}

        _ymag, _ymagerr = float(_columns['yMeanPSFMag'][_i]), float(_columns['yMeanPSFMagErr'][_i])
        if _ymag != -999.0:
            _ymags += 1
        _data = {**_data, **{'ymeanpsfmag': _ymag, 'ymeanpsfmagerr': _ymagerr}}

        _zmag, _zmagerr = float(_columns['zMeanPSFMag'][_i]), float(_columns['zMeanPSFMagErr'][_i])
        if _zmag != -999.0:
            _zmags += 1
        _data = {**_data, **{'zmeanpsfmag': _zmag, 'zmeanpsfmagerr': _zmagerr}}

        _objid = int(_columns['objID'][_i])
        try:
            session.query(Ps1Q3cRecord).filter(Ps1Q3cRecord.objid==_objid).update(_data, synchronize_session='evaluate')
            if _verbose and (_i % _nelms) == 0:
               print(f"record update for objid={_objid} with _data={_data}")
               session.commit()
        except Exception as _e2:
            session.rollback()
            print(f"<ERROR> failed to update database, _i={_i}, _objid={_objid}, error='{_e2}'")
            continue

    # close
    session.commit()
    if hasattr(session, 'close'):
        session.close()
    if _verbose:
        print(f"_gmags={_gmags}")
        print(f"_rmags={_rmags}")
        print(f"_imags={_imags}")
        print(f"_zmags={_zmags}")
        print(f"_ymags={_ymags}")


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
        ps1_q3c_update_bulk_new(_file=_a.file.strip(), _nelms=int(_a.nelms), _verbose=bool(_a.verbose))
    except Exception as _:
        print(f"{_}\n{__doc__}")
