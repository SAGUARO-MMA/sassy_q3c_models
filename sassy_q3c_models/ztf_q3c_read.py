#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.ztf_q3c_orm import *


# +
# __doc__ string
# -
__doc__ = """ python3 ztf_q3c_read.py --help """


# +
# constant(s)
# -
MAX_SIZE = 2**31 - 1
ZTF_DIVISOR = 10000


# +
# function: get_avro_ztf_q3c()
# -
# noinspection PyBroadException,PyUnusedLocal
def get_avro_ztf_q3c(_file: str = ''):
    """ returns dictionary of avro data from file or {} """

    # check input(s)
    _x = {}
    if not os.path.exists(_file):
        return _x

    # read file
    with open(_file, 'rb') as _f:
        _fr = fastavro.reader(_f)
        schema = _fr.writer_schema
        for _p in _fr:
            _x = {
                "aimage": _p['candidate'].get('aimage', math.nan),
                "aimagerat": _p['candidate'].get('aimagerat', math.nan),
                "alert_candid": _p.get('candid', -MAX_SIZE),
                "avro": '',
                "bimage": _p['candidate'].get('bimage', math.nan),
                "bimagerat": _p['candidate'].get('bimagerat', math.nan),
                "candid": _p['candidate'].get('candid', -MAX_SIZE),
                "chinr": _p['candidate'].get('chinr', math.nan),
                "chipsf": _p['candidate'].get('chipsf', math.nan),
                "classtar": _p['candidate'].get('classtar', math.nan),
                "clrcoeff": _p['candidate'].get('clrcoeff', math.nan),
                "clrcounc": _p['candidate'].get('clrcounc', math.nan),
                "clrmed": _p['candidate'].get('clrmed', math.nan),
                "clrrms": _p['candidate'].get('clrrms', math.nan),
                "cutoutdifference": _p['cutoutDifference'].get('fileName', ''),
                "cutoutscience": _p['cutoutScience'].get('fileName', ''),
                "cutouttemplate": _p['cutoutTemplate'].get('fileName', ''),
                "dec": _p['candidate'].get('dec', math.nan),
                "decnr": _p['candidate'].get('decnr', math.nan),
                "deltamaglatest": math.nan,
                "deltamagref": math.nan,
                "diffmaglim": _p['candidate'].get('diffmaglim', math.nan),
                "distpsnr1": _p['candidate'].get('distpsnr1', math.nan),
                "distpsnr2": _p['candidate'].get('distpsnr2', math.nan),
                "distpsnr3": _p['candidate'].get('distpsnr3', math.nan),
                "distnr": _p['candidate'].get('distnr', math.nan),
                "drb": _p['candidate'].get('drb', math.nan),
                "drbversion": _p['candidate'].get('drbversion', ''),
                "dsnrms": _p['candidate'].get('dsnrms', math.nan),
                "dsdiff": _p['candidate'].get('dsdiff', math.nan),
                "elong": _p['candidate'].get('elong', math.nan),
                "exptime": _p['candidate'].get('exptime', math.nan),
                "fid": _p['candidate'].get('fid', -MAX_SIZE),
                "filtername": '',
                "field": _p['candidate'].get('field', -MAX_SIZE),
                "fwhm": _p['candidate'].get('fwhm', math.nan),
                "gal_b": math.nan,
                "gal_l": math.nan,
                "isdiffpos": _p['candidate'].get('isdiffpos', ''),
                "iso": '',
                "jd": _p['candidate'].get('jd', math.nan),
                "jdendhist": _p['candidate'].get('jdendhist', math.nan),
                "jdendref": _p['candidate'].get('jdendref', math.nan),
                "jdstarthist": _p['candidate'].get('jdstarthist', math.nan),
                "jdstartref": _p['candidate'].get('jdstartref', math.nan),
                "magap": _p['candidate'].get('magap', math.nan),
                "magapbig": _p['candidate'].get('magapbig', math.nan),
                "magdiff": _p['candidate'].get('magdiff', math.nan),
                "magfromlim": _p['candidate'].get('magfromlim', math.nan),
                "maggaia": _p['candidate'].get('maggaia', math.nan),
                "maggaiabright": _p['candidate'].get('maggaiabright', math.nan),
                "magnr": _p['candidate'].get('magnr', math.nan),
                "magpsf": _p['candidate'].get('magpsf', math.nan),
                "magzpsci": _p['candidate'].get('magzpsci', math.nan),
                "magzpscirms": _p['candidate'].get('magzpscirms', math.nan),
                "magzpsciunc": _p['candidate'].get('magzpsciunc', math.nan),
                "mindtoedge": _p['candidate'].get('mindtoedge', math.nan),
                "nbad": _p['candidate'].get('nbad', 0),
                "ncovhist": _p['candidate'].get('ncovhist', 0),
                "ndethist": _p['candidate'].get('ndethist', 0),
                "neargaia": _p['candidate'].get('neargaia', math.nan),
                "neargaiabright": _p['candidate'].get('neargaiabright', math.nan),
                "nframesref": _p['candidate'].get('nframesref', 0),
                "nid": _p['candidate'].get('nid', -MAX_SIZE),
                "nmatches": _p['candidate'].get('nmatches', 0),
                "nmtchps": _p['candidate'].get('nmtchps', 0),
                "nneg": _p['candidate'].get('nneg', 0),
                "objectidps1": _p['candidate'].get('objectidps1', -MAX_SIZE),
                "objectidps2": _p['candidate'].get('objectidps2', -MAX_SIZE),
                "objectidps3": _p['candidate'].get('objectidps3', -MAX_SIZE),
                "oid": _p.get('objectId', ''),
                "pdiffimfilename": _p['candidate'].get('pdiffimfilename', ''),
                "pid": _p['candidate'].get('pid', -MAX_SIZE),
                "programid": _p['candidate'].get('programid', -MAX_SIZE),
                "programpi": _p['candidate'].get('programpi', ''),
                "publisher": _p.get('publisher', ''),
                "ra": _p['candidate'].get('ra', math.nan),
                "ranr": _p['candidate'].get('ranr', math.nan),
                "rb": _p['candidate'].get('rb', math.nan),
                "rbversion": _p['candidate'].get('rbversion', ''),
                "rcid": _p['candidate'].get('rcid', -MAX_SIZE),
                "rfid": _p['candidate'].get('rfid', -MAX_SIZE),
                "scorr": _p['candidate'].get('scorr', math.nan),
                "seeratio": _p['candidate'].get('seeratio', math.nan),
                "sgmag1": _p['candidate'].get('sgmag1', math.nan),
                "sgmag2": _p['candidate'].get('sgmag2', math.nan),
                "sgmag3": _p['candidate'].get('sgmag3', math.nan),
                "sgscore1": _p['candidate'].get('sgscore1', math.nan),
                "sgscore2": _p['candidate'].get('sgscore2', math.nan),
                "sgscore3": _p['candidate'].get('sgscore3', math.nan),
                "sharpnr": _p['candidate'].get('sharpnr', math.nan),
                "sigmagap": _p['candidate'].get('sigmagap', math.nan),
                "sigmagapbig": _p['candidate'].get('sigmagapbig', math.nan),
                "sigmagnr": _p['candidate'].get('sigmagnr', math.nan),
                "sigmapsf": _p['candidate'].get('sigmapsf', math.nan),
                "simag1": _p['candidate'].get('simag1', math.nan),
                "simag2": _p['candidate'].get('simag2', math.nan),
                "simag3": _p['candidate'].get('simag3', math.nan),
                "sky": _p['candidate'].get('sky', math.nan),
                "srmag1": _p['candidate'].get('srmag1', math.nan),
                "srmag2": _p['candidate'].get('srmag2', math.nan),
                "srmag3": _p['candidate'].get('srmag3', math.nan),
                "ssdistnr": _p['candidate'].get('ssdistnr', math.nan),
                "ssmagnr": _p['candidate'].get('ssmagnr', math.nan),
                "ssnamenr": _p['candidate'].get('ssnamenr', ''),
                "ssnrms": _p['candidate'].get('ssnrms', math.nan),
                "sumrat": _p['candidate'].get('sumrat', math.nan),
                "szmag1": _p['candidate'].get('szmag1', math.nan),
                "szmag2": _p['candidate'].get('szmag2', math.nan),
                "szmag3": _p['candidate'].get('szmag3', math.nan),
                "tblid": _p['candidate'].get('tblid', -MAX_SIZE),
                "tooflag": _p['candidate'].get('tooflag', -1),
                "xpos": _p['candidate'].get('xpos', math.nan),
                "ypos": _p['candidate'].get('ypos', math.nan),
                "zid": -MAX_SIZE,
                "zpclrcov": _p['candidate'].get('zpclrcov', math.nan),
                "zpmed": _p['candidate'].get('zpmed', math.nan)
            }
            # correction(s)
            _x['filtername'] = ZTF_FILTERS.get(_x['fid']) if (_x['fid'] in ZTF_FILTERS.keys()) else ''
            if _x['jd'] is not math.nan:
                _iso = Time(_x['jd'], format='jd').datetime
                _x['avro'] = f"{DB_AVRO}/{_iso.year}/{str(_iso.month).zfill(2)}/{str(_iso.day).zfill(2)}/" \
                             f"{_x['alert_candid']}.avro"
                _x['iso'] = _iso.isoformat()
            _x['ssnamenr'] = _x['ssnamenr'] if _x['ssnamenr'].lower() != 'null' else ''
            if (_x['ra'] is not math.nan) and (_x['dec'] is not math.nan):
                _c = SkyCoord(_x['ra'], _x['dec'], unit='deg')
                _g = _c.galactic
                _x['gal_l'], _x['gal_b'] = _g.l.value, _g.b.value
            if (_x['magnr'] is not math.nan) and (_x['magpsf'] is not math.nan) and (_x['distnr'] < 2.0):
                _x['deltamagref'] = _x['magnr'] - _x['magpsf']
            _deltamaglatest = None
            if _p['prv_candidates']:
                _pc = sorted(_p['prv_candidates'], key=lambda x: x['jd'], reverse=True)
                for _cn in _pc:
                    if not _deltamaglatest and (_x['fid'] == _cn['fid']) and _cn['magpsf']:
                        _deltamaglatest = _x['magpsf'] - _cn['magpsf']
            _x['deltamaglatest'] = _deltamaglatest if isinstance(_deltamaglatest, float) else math.nan

    # return
    return _x


# +
# function: get_next_index()
# -
# noinspection PyBroadException
def get_next_index(_table: str = 'ztf_q3c', _key: str = 'zid'):
    """ returns next usable index in database table for key or -1 """
    _sql = f"SELECT nextval(pg_get_serial_sequence('{_table}', '{_key}'));"
    try:
        with create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}').connect() as _c:
            _ret = [_r for _r in _c.execute(_sql)]
            return tuple(_ret[0])[0] if (_ret and len(_ret) == 1) else -1
    except Exception:
        return -1


# +
# function: get_max_idx()
# -
def get_max_idx(_table: str = 'ztf_q3c', _index: str = 'zid') -> int:
    """ returns max row number in database table for key or -1 """
    try:
        with create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}').connect() as _c:
            _ret = [_ for _ in _c.execute(f"SELECT MAX({_index}) FROM {_table};")]
            return tuple(_ret[0])[0] if (_ret and len(_ret) == 1) else -1
    except Exception:
        return -1


# +
# function: get_last_row()
# -
# noinspection PyBroadException
def get_last_row(_table: str = 'ztf_q3c'):
    """ returns last row number in database table for key or -1 """
    _sql = f"SELECT COUNT(*) FROM {_table};"
    try:
        with create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}').connect() as _c:
            _ret = [_r for _r in _c.execute(_sql)]
            return tuple(_ret[0])[0] if (_ret and len(_ret) == 1) else -1
    except Exception:
        return -1


# +
# function: get_max_index()
# -
# noinspection PyBroadException
def get_max_index(_table: str = 'ztf_q3c', _key: str = 'zid'):
    """ returns last row number in database table for key or -1 """
    _sql = f"SELECT MAX({_key}) FROM {_table};"
    try:
        with create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}').connect() as _c:
            _ret = [_r for _r in _c.execute(_sql)]
            return tuple(_ret[0])[0] if (_ret and len(_ret) == 1) else -1
    except Exception:
        return -1


# +
# function: ztf_q3c_read()
# -
# noinspection PyBroadException
def ztf_q3c_read(_dir: str = '', _verbose: bool = False):

    # set default(s)
    _files, _ic = [], 0

    # get file(s)
    _dir = os.path.abspath(os.path.expanduser(_dir))
    if os.path.isdir(_dir):
        _files = glob.glob(f"{_dir}/*.avro")
    else:
        return

    # noinspection PyBroadException
    try:
        # connect to database
        if _verbose:
            print(f"Connecting to database via 'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'")
        engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        get_session = sessionmaker(bind=engine)
        session = get_session()
    except Exception as _e:
        raise Exception(f'Failed to connect to database, error={_e}')
        return
    else:
        if _verbose:
            print(f"Connected to database via 'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'")

    # loop around file(s)
    _ic = get_max_index()
    for _f in _files:
        _ic += 1
        _ztc_q3c_rec = None
        try:
            _data = {**get_avro_ztf_q3c(_file=_f), **{'zid': _ic}}
            _ztc_q3c_rec = ZtfQ3cRecord(**_data)
            if (_ic % ZTF_DIVISOR == 0) and _verbose:
                print(f'inserting {_ztc_q3c_rec} into database at position {_ic}')
            session.add(_ztc_q3c_rec)
            session.commit()
        except Exception as _x:
            session.rollback()
            _ic -= 1
            print(f'failed inserting {_ztc_q3c_rec} into database, error={_x}')
            continue

# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _pa = argparse.ArgumentParser(description='Read ZTF Data', formatter_class=argparse.RawTextHelpFormatter)
    _pa.add_argument(f'--dir', default=f'{os.getcwd()}', help="""Directory [%(default)s]""")
    _pa.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _pa.parse_args()

    # execute
    ztf_q3c_read(_dir=_a.dir.strip(), _verbose=bool(_a.verbose))
