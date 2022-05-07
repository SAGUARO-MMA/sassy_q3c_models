#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.non_detections_orm import *


# +
# __doc__ string
# -
__doc__ = """ python3 non_detections_read.py --help """


# +
# function: get_avro_non_detections()
# -
# noinspection PyBroadException,PyUnusedLocal
def get_avro_non_detections(_file: str = '') -> list:
    """ returns list of non-detections in file or [] """

    # read file
    _ret = []
    with open(_file, 'rb') as _f:
        _fr = fastavro.reader(_f)
        schema = _fr.writer_schema
        # loop around packets (typically only one packet per file, but it could change)
        for _packet in _fr:
            if 'prv_candidates' not in _packet or _packet['prv_candidates'] is None:
                continue
            if ('objectId' not in _packet) or ('objectId' in _packet and _packet['objectId'] == ''):
                continue
            # get prv_candidates
            _oid = _packet['objectId']
            _p = _packet['prv_candidates']
            for _i in range(len(_p)):
                # this is the non-detection data
                if 'candid' in _p[_i] and _p[_i]['candid'] is None:
                    if ('fid' not in _p[_i]) or ('fid' in _p[_i] and not isinstance(_p[_i]['fid'], int)):
                        continue
                    if ('jd' not in _p[_i]) or ('jd' in _p[_i] and not isinstance(_p[_i]['jd'], float)):
                        continue
                    if ('diffmaglim' not in _p[_i]) or \
                            ('diffmaglim' in _p[_i] and not isinstance(_p[_i]['diffmaglim'], float)):
                        continue
                    _ret.append({'fid': int(f"{_p[_i]['fid']}"), 'oid': _oid, 'jd': float(f"{_p[_i]['jd']}"),
                                 'diffmaglim': float(f"{_p[_i]['diffmaglim']}")})

    # return data
    return _ret


# +
# function: get_next_index()
# -
# noinspection PyBroadException
def get_next_index(_table: str = 'non_detections', _key: str = 'nid') -> int:
    """ returns next usable index in database table for key or -1 """
    _sql = f"SELECT nextval(pg_get_serial_sequence('{_table}', '{_key}'));"
    with create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}').connect() as _c:
        _ret = [_r for _r in _c.execute(_sql)]
        return tuple(_ret[0])[0] if (_ret and len(_ret) == 1) else -1


# +
# function: get_last_row()
# -
# noinspection PyBroadException
def get_last_row(_table: str = 'non_detections') -> int:
    """ returns last row number in database table for key or -1 """
    _sql = f"SELECT COUNT(*) FROM {_table};"
    try:
        with create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}').connect() as _c:
            _ret = [_r for _r in _c.execute(_sql)]
            return tuple(_ret[0])[0] if (_ret and len(_ret) == 1) else -1
    except Exception:
        return -1


# +
# function: non_detections_read()
# -
# noinspection PyBroadException
def non_detections_read(_dir: str = '', _verbose: bool = False) -> None:

    # set default(s)
    _files, _non_detections, _ic = [], [], 0

    # get file(s)
    _dir = os.path.abspath(os.path.expanduser(_dir))
    if os.path.isdir(_dir):
        _files = glob.glob(f"{_dir}/*.avro")
    else:
        return

    # noinspection PyBroadException
    try:
        # connect to database
        engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        get_session = sessionmaker(bind=engine)
        session = get_session()
    except Exception as _e:
        raise Exception(f'Failed to connect to database, error={_e}')

    # loop around file(s)
    # _ic = get_next_index()
    for _f in _files:
        _data = get_avro_non_detections(_file=_f)
        for _d in _data:
            try:
                if session.query(NonDetectionsRecord).filter(NonDetectionsRecord.oid == _d['oid']).filter(
                        NonDetectionsRecord.jd == _d['jd']).count() == 0:
                    _nd_rec = NonDetectionsRecord(nid=_ic, oid=_d['oid'], fid=_d['fid'], jd=_d['jd'],
                                                  diffmaglim=_d['diffmaglim'])
                    if _verbose:
                        print(f'inserting {_nd_rec.serialized()} into database')
                    session.add(_nd_rec)
                    session.commit()
                    _ic += 1
            except Exception as _f:
                session.rollback()
                print(f"Failed to insert object {_d} database, error={_f}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _pa = argparse.ArgumentParser(description='Read NonDetections Data', formatter_class=argparse.RawTextHelpFormatter)
    _pa.add_argument(f'--dir', default=f'{os.getcwd()}', help="""Directory [%(default)s]""")
    _pa.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _pa.parse_args()

    # execute
    try:
        non_detections_read(_dir=_a.dir.strip(), _verbose=bool(_a.verbose))
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
