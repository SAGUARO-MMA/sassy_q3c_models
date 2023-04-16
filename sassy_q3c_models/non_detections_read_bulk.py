#!/usr/bin/env python3


# +
# import(s)
# -
# +
# import(s)
# -
from sassy_q3c_models.non_detections_orm import *


# +
# __doc__ string
# -
__doc__ = """ python3 non_detections_read_bulk.py --help """


# +
# constant(s)
# -
DEF_NELMS = 50000


# +
# function: db_get_valid()
# -
def db_get_valid(_session: Any = None, _ilist: list = None):

    # check input(s)
    if _session is None or _ilist is None:
        return

    # count record(s)
    _valid = []
    for _elem in _ilist:
        try:
            if _session.query(NonDetectionsRecord).filter(NonDetectionsRecord.oid == _elem['oid']).filter(NonDetectionsRecord.jd == _elem['jd']).count() == 0:
                _valid.append((_elem['diffmaglim'], _elem['oid'], _elem['jd'], _elem['fid']))
        except Exception as _e:
            _session.rollback()
            print(f"<ERROR> failed to insert values into database, error='{_e}'")
            continue

    # return valid entries
    return _valid


# +
# db_bulk_insert()
# -
def db_bulk_insert(_connection: Any = None, _cursor: Any = None, _ivalid: list = None):

    # check input(s)
    if _connection is None or _cursor is None or _ivalid is None:
        return

    # bulk ingest
    try:
        psycopg2.extras.execute_values(
            _cursor,
            """INSERT INTO non_detections (diffmaglim, oid, jd, fid) VALUES %s""", _ivalid, page_size=100)
        _connection.commit()
    except Exception as _e:
        _cursor.execute("rollback;")
        print(f"<ERROR> failed to insert values into database, error='{_e}'")


# +
# function: non_detections_read_bulk()
# -
# noinspection PyBroadException
def non_detections_read_bulk(_file: str = '', _dir: str = '', _nelms: int = DEF_NELMS, _verbose: bool = False):

    # check input(s)
    _file = os.path.abspath(os.path.expanduser(_file))
    _dir = os.path.abspath(os.path.expanduser(_dir))
    _nelms = _nelms if _nelms > 0 else DEF_NELMS

    if not os.path.exists(_file):
        print(f"invalid input, _file={_file}")
        return
    if not os.path.exists(_dir) or not os.path.isdir(_dir):
        print(f"invalid input, _dir={_dir}")
        return

    # set default(s)
    _files, _non_detections, _total, _fc, _ic = [], [], 0, 0, 0

    # get all files
    if _dir != '':
        _dir = os.path.abspath(os.path.expanduser(_dir))
        if os.path.isdir(_dir):
            _files = glob.glob(f"{_dir}/*.avro")

    if _file != '':
        _file = os.path.abspath(os.path.expanduser(_file))
        if os.path.exists(_file):
            _files.append(_file)

    # proceed if we have files to process
    _total = len(_files)
    if _total == 0:
        print(f"{get_utc()}> No files to process")
        return
    else:
        print(f"{get_utc()}> Processing {_total} files")

    # connect to database (method 1)
    try:
        if _verbose:
            print(f"Connecting to database via 'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'")
        engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        get_session = sessionmaker(bind=engine)
        session = get_session()
    except Exception as _e1:
        print(f"<ERROR> failed to connect to database, error='{_e1}'")
        return
    else:
        if _verbose:
            print(f"Connected to database via 'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'")

    # connect to database (method 2)
    try:
        connection = psycopg2.connect(host=DB_HOST, database=DB_NAME,
                                      user=DB_USER, password=DB_PASS, port=int(DB_PORT))
        connection.autocommit = True
        cursor = connection.cursor()
    except Exception as _e2:
        print(f"<ERROR> failed to connect to database, error='{_e2}'")
        return

    # process files
    for _fe in _files:

        # (re)set variable(s)
        _oid, _packets = '', []
        if os.path.exists(_fe) and os.path.isdir(_fe):
            print(f"<ERROR> _fe={_fe}")
            continue

        # read the data
        try:
            with open(_fe, 'rb') as _f:
                _reader = fastavro.reader(_f)
                _schema = _reader.writer_schema
                for _packet in _reader:
                    _packets.append(_packet)
                _fc += 1
        except Exception as _e3:
            print(f"<ERROR> failed to read data from {_fe}, error='{_e3}'")
            continue

        # process the data
        for _i in range(len(_packets)):
            if 'objectId' in _packets[_i] and 'prv_candidates' in _packets[_i]:
                _oid = _packets[_i]['objectId']
                _prv = _packets[_i]['prv_candidates']
                if _prv is not None:
                    _prv = sorted(_prv, key=lambda x: x['jd'], reverse=True)
                    for _cand in _prv:
                        if all(_cand[_k1] is None for _k1 in
                               ('candid', 'isdiffpos', 'ra', 'dec', 'magpsf', 'sigmapsf', 'ranr', 'decnr')) and \
                                all(_cand[_k2] is not None for _k2 in ('diffmaglim', 'jd', 'fid')):
                            _non_detections.append({'oid': _oid, 'diffmaglim': float(_cand['diffmaglim']),
                                                    'jd': float(_cand['jd']), 'fid': int(_cand['fid'])})
                            _ic += 1

        # submit after _nelms records have been found
        if _ic > _nelms and len(_non_detections) > 0:
            print(f"{get_utc()}> Inserting {len(_non_detections)} record(s) into database "
                  f"({_fc*100.0/_total:.2f}% complete)")
            _valid = db_get_valid(_session=session, _ilist=_non_detections)
            if _valid:
                db_bulk_insert(_connection=connection, _cursor=cursor, _ivalid=_valid)
                if _verbose:
                    print(f"{get_utc()}> Inserted {len(_valid)} valid record(s), rejected {_nelms-len(_valid)} duplicate(s)")
            # reset
            _ic, _non_detections = 0, []

    # tidy up stragglers
    if len(_non_detections) > 0:
        print(f"{get_utc()}> Inserting {len(_non_detections)} straggler(s) into database "
              f"({_fc*100.0/_total:.2f}% complete)")
        _valid = db_get_valid(_session=session, _ilist=_non_detections)
        if _valid:
            db_bulk_insert(_connection=connection, _cursor=cursor, _ivalid=_valid)
            if _verbose:
                print(f"{get_utc()}> Inserted {len(_valid)} valid straggler(s), rejected {_nelms-len(_valid)} duplicate(s)")

    # close
    cursor.close()
    connection.close()
    session.close()


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description='Populate NonDetection Table', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument('--file', default='', help="""Input file [%(default)s]""")
    _p.add_argument('--directory', default='', help="""Input directory [%(default)s]""")
    _p.add_argument('--nelms', default=DEF_NELMS, help="""Number of elements between screen updates [%(default)s]""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    non_detections_read_bulk(_file=_a.file.strip(), _dir=_a.directory.strip(), _nelms=int(_a.nelms), _verbose=bool(_a.verbose))
