#!/usr/bin/env python3


# +
# import(s)
# -
# +
# import(s)
# -
from sassy_q3c_models.ztf_fp_q3c_orm import *


# +
# __doc__ string
# -
__doc__ = """python3 ztf_fp_q3c_read_bulk.py --help"""


# +
# constant(s)
# -
DEF_NELMS = 50000


# +
# db_bulk_insert()
# -
def db_bulk_insert(_connection: Any = None, _cursor: Any = None, _irows: list = None):

    # check input(s)
    if _connection is None or _cursor is None or _irows is None:
        return
    if not all(len(_) == 31 for _ in _irows):
        print(f"<ERROR> not all fields present in _irows")
        return

    # bulk ingest
    try:
        print(f"<INFO> inserting {len(_irows)} rows into database")
        psycopg2.extras.execute_values(
            _cursor,
            """INSERT INTO ztf_fp_q3c (candid, oid, field, rcid, fid, pid, rfid, sciinpseeing, scibckgnd, scisigpix, 
                                       magzpsci, magzpsciunc, magzpscirms, clrcoeff, clrcounc, exptime, adpctdif1, adpctdif2, diffmaglim, programid, 
                                       jd, forcediffimflux, forcediffimfluxunc, procstatus, distnr, ranr, decnr, magnr, sigmagnr, chinr, 
                                       sharpnr) VALUES %s""", _irows, page_size=100)
        _connection.commit()
    except Exception as _:
        print(f"<ERROR> failed to insert values into database, error='{_}'")
        _cursor.execute("rollback;")


# +
# function: ztf_fp_q3c_read_bulk()
# -
# noinspection PyBroadException
def ztf_fp_q3c_read_bulk(_file: str = '', _dir: str = '', _nelms: int = DEF_NELMS, _verbose: bool = False):

    # check input(s)
    _file = os.path.abspath(os.path.expanduser(_file))
    _dir = os.path.abspath(os.path.expanduser(_dir))
    _nelms = _nelms if _nelms > 0 else DEF_NELMS

    _msg =  f"_file='{_file}', _dir='{_dir}', _nelms={_nelms}, _verbose={_verbose}"
    if not os.path.exists(_file) or not os.path.exists(_dir) or not os.path.isdir(_dir):
        raise Exception(f"invalid input(s), {_msg}")
    print(f"ztf_fp_q3c_read_bulk({_msg})")

    # set default(s)
    _files, _ztf_fp_q3c, _total, _fc, _ic = [], [], 0, 0, 0

    # get all files
    if _dir != '':
        _files = glob.glob(f"{_dir}/*.avro")

    if _file != '':
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
        connection = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS, port=int(DB_PORT))
        connection.autocommit = True
        cursor = connection.cursor()
    except Exception as _e2:
        print(f"<ERROR> failed to connect to database, error='{_e2}'")
        return

    # process files
    _headers = {_ for _ in ZTF_FP_Q3C_HEADERS if _ not in ['fpid', 'candid', 'oid']}
    print(f"<INFO> _headers={_headers}")
    for _fe in _files:

        if os.path.isdir(_fe):
            continue

        # (re)set variable(s)
        _packets = []

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
            _candid, _oid = -1, ''
            if 'objectId' in _packets[_i] and 'candid' in _packets[_i]:
                _oid = _packets[_i]['objectId']
                _candid = int(_packets[_i]['candid'])
            else:
                print(f"<WARNING> no 'candid' or 'objectid' in packet!")
                continue
            if 'fp_hists' in _packets[_i]:
                _fph = _packets[_i]['fp_hists']
                if _fph is None or len(_fph) == 0:
                    print(f"<WARNING> empty 'fp_hists' in packet! _fph={_fph}, _oid='{_oid}', _candid={_candid}")
                    continue
                else:
                    for _cand in _fph:
                        if _ic > _nelms:
                            print(f"_cand={_cand}")
                        if all(_ in _cand for _ in _headers):
                            _ztf_fp_q3c.append([
                                _candid, 
                                _oid,
                                int(_cand['field']), 
                                int(_cand['rcid']), 
                                int(_cand['fid']),
                                int(_cand['pid']), 
                                int(_cand['rfid']), 
                                float(_cand['sciinpseeing']), 
                                float(_cand['scibckgnd']),
                                float(_cand['scisigpix']), 
                                float(_cand['magzpsci']), 
                                float(_cand['magzpsciunc']),
                                float(_cand['magzpscirms']), 
                                float(_cand['clrcoeff']), 
                                float(_cand['clrcounc']),
                                float(_cand['exptime']), 
                                float(_cand['adpctdif1']), 
                                float(_cand['adpctdif2']),
                                float(_cand['diffmaglim']), 
                                int(_cand['programid']), 
                                float(_cand['jd']),
                                float(_cand['forcediffimflux']), 
                                float(_cand['forcediffimfluxunc']),
                                _cand['procstatus'], 
                                float(_cand['distnr']), 
                                float(_cand['ranr']), 
                                float(_cand['decnr']),
                                float(_cand['magnr']), 
                                float(_cand['sigmagnr']), 
                                float(_cand['chinr']), 
                                float(_cand['sharpnr'])])
                            _ic += 1
                        if _ic > _nelms:
                            print(f"_ztf_fp_q3c[-1]={_ztf_fp_q3c[-1]}")

        # submit after _nelms records have been found
        if _ic > _nelms and len(_ztf_fp_q3c) > 0:
            print(f"{get_utc()}> Inserting {len(_ztf_fp_q3c)} record(s) into database "
                  f"({_fc*100.0/_total:.2f}% complete)")
            db_bulk_insert(_connection=connection, _cursor=cursor, _irows=_ztf_fp_q3c)
            if _verbose:
                print(f"{get_utc()}> Inserted {len(_ztf_fp_q3c)} valid record(s)")
            # reset
            _ic, _ztf_fp_q3c = 0, []

    # tidy up stragglers
    if len(_ztf_fp_q3c) > 0:
        print(f"{get_utc()}> Inserting {len(_ztf_fp_q3c)} straggler(s) into database "
              f"({_fc*100.0/_total:.2f}% complete)")
        db_bulk_insert(_connection=connection, _cursor=cursor, _irows=_ztf_fp_q3c)
        if _verbose:
            print(f"{get_utc()}> Inserted {len(_ztf_fp_q3c)} valid straggler(s)")

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

    # execute
    try:
        _a = _p.parse_args()
        ztf_fp_q3c_read_bulk(_file=_a.file.strip(), _dir=_a.directory.strip(), _nelms=int(_a.nelms), _verbose=bool(_a.verbose))
    except Exception as _:
        print(f"{_}\n{__doc__}")
