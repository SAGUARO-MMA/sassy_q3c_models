#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.gaiadr3variable_q3c_orm import *


# +
# __doc__ string
# -
__doc__ = """ python3 gaiadr3vairable_q3c_read.py --help """


# +
# constant(s)
# -
GAIADR3VARIABLE_Q3C_DIVISOR = 10000
GAIADR3VARIABLE_Q3C_CATALOG_FILE = os.path.abspath(os.path.expanduser('/science/catalogs/gaiadr3variable.00.tsv'))


# +
# function: get_max_idx()
# -
def get_max_idx(_table: str = 'GAIADR3VARIABLE_q3c', _index: str = 'gid') -> int:
    """ returns max row number in database table for key or -1 """
    try:
        with create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}').connect() as _c:
            _ret = [_ for _ in _c.execute(f"SELECT MAX({_index}) FROM {_table};")]
            return tuple(_ret[0])[0] if (_ret and len(_ret) == 1) else -1
    except Exception:
        return -1


# +
# function: GAIADR3VARIABLE_q3c_read()
# -
# noinspection PyBroadException
def GAIADR3VARIABLE_q3c_read(_file: str = GAIADR3VARIABLE_Q3C_CATALOG_FILE, _index: int = -1, _verbose: bool = False) -> None:

    # check input(s)
    _file = os.path.abspath(os.path.expanduser(_file))
    if not os.path.exists(_file):
        print(f"<ERROR> invalid input, _file={_file}")
        return
    if _index < 0:
        print(f"<ERROR> invalid input, _index={_index}")
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
    else:   
        if _verbose:
            print(f"<INFO> connected to database postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME} OK, _index={_index}")

    # read the file
    _gid = _index
    _header = []
    with open(_file, 'r') as _fd:
        for _line in _fd:

            # initialize
            _rec, _row, _dict = None, [], {}

            # get header
            if '# source_id' in _line.strip():
                _header = _line.strip()[1:].split('\t')
                if _header != GAIADR3VARIABLE_HEADERS:
                    print(f"<ERROR> unexpected {_header} != {GAIADR3VARIABLE_HEADERS}")
                    return

            # get elements
            elif _line.strip()[0] != '#':
                _line = _line.replace('\t', '?')
                _row = _line.strip().split('?')
                if len(_row) != GAIADR3VARIABLE_COLUMNS:
                    print(f"<ERROR> row contains {len(_row)} columns, expected {GAIADR3VARIABLE_COLUMNS}")
                    continue

                # create dictionary
                _dict = dict(zip(_header, _row))
                if [_k for _k in _dict] == GAIADR3VARIABLE_HEADERS:
                    _dict = dict(zip(GAIADR3VARIABLE_KEYS, _row))
                    if not verify_keys(_d=_dict, _s=set(GAIADR3VARIABLE_KEYS)):
                        print(f"<ERROR> _dict = {_dict} is invalid")
                        continue

                # create orm object
                try:
                    _rec = GAIADR3VARIABLEQ3cRecord(
                        gid=_gid,
                        ra=float(_dict['ra']) if _dict['ra'].strip() != '' else math.nan,
                        ra_error=float(_dict['ra_error']) if _dict['ra_error'].strip() != '' else math.nan,
                        dec=float(_dict['dec']) if _dict['dec'].strip() != '' else math.nan,
                        dec_error=float(_dict['dec_error']) if _dict['dec_error'].strip() != '' else math.nan,
                        pmra=float(_dict['pmra']) if _dict['pmra'].strip() != '' else math.nan,
                        pmra_error=float(_dict['pmra_error']) if _dict['ra_error'].strip() != '' else math.nan,
                        pmdec=float(_dict['pmdec']) if _dict['pmdec'].strip() != '' else math.nan,
                        pmdec_error=float(_dict['pmdec_error']) if _dict['pmdec_error'].strip() != '' else math.nan,
                        parallax=float(_dict['parallax']) if _dict['parallax'].strip() != '' else math.nan,
                        parallax_error=float(_dict['parallax_error']) if _dict['parallax_error'].strip() != '' else math.nan,
                        solution_id=int(_dict['solution_id']) if _dict['solution_id'].strip() != '' else -1,
                        source_id=int(_dict['source_id']) if _dict['source_id'].strip() != '' else -1,
                        classification=_dict['classification'].strip(),
                        best_class_name=_dict['best_class_name'].strip(),
                        best_class_score=float(_dict['best_class_score']) if _dict['best_class_score'].strip() != '' else math.nan,
                        num_selected_g_fov=int(_dict['num_selected_g_fov']) if _dict['num_selected_g_fov'].strip() != '' else -1,
                        mean_obs_time_g_fov=float(_dict['mean_obs_time_g_fov']) if _dict['mean_obs_time_g_fov'].strip() != '' else math.nan,
                        time_duration_g_fov=float(_dict['time_duration_g_fov']) if _dict['time_duration_g_fov'].strip() != '' else math.nan,
                        min_mag_g_fov=float(_dict['min_mag_g_fov']) if _dict['min_mag_g_fov'].strip() != '' else math.nan,
                        max_mag_g_fov=float(_dict['max_mag_g_fov']) if _dict['max_mag_g_fov'].strip() != '' else math.nan,
                        mean_mag_g_fov=float(_dict['mean_mag_g_fov']) if _dict['mean_mag_g_fov'].strip() != '' else math.nan,
                        median_mag_g_fov=float(_dict['median_mag_g_fov']) if _dict['median_mag_g_fov'].strip() != '' else math.nan,
                        range_mag_g_fov=float(_dict['range_mag_g_fov']) if _dict['range_mag_g_fov'].strip() != '' else math.nan,
                        trimmed_range_mag_g_fov=float(_dict['trimmed_range_mag_g_fov']) if _dict['trimmed_range_mag_g_fov'].strip() != '' else math.nan,
                        std_dev_mag_g_fov=float(_dict['std_dev_mag_g_fov']) if _dict['std_dev_mag_g_fov'].strip() != '' else math.nan,
                        skewness_mag_g_fov=float(_dict['skewness_mag_g_fov']) if _dict['skewness_mag_g_fov'].strip() != '' else math.nan,
                        kurtosis_mag_g_fov=float(_dict['kurtosis_mag_g_fov']) if _dict['kurtosis_mag_g_fov'].strip() != '' else math.nan,
                        mad_mag_g_fov=float(_dict['mad_mag_g_fov']) if _dict['mad_mag_g_fov'].strip() != '' else math.nan,
                        abbe_mag_g_fov=float(_dict['abbe_mag_g_fov']) if _dict['abbe_mag_g_fov'].strip() != '' else math.nan,
                        iqr_mag_g_fov=float(_dict['iqr_mag_g_fov']) if _dict['iqr_mag_g_fov'].strip() != '' else math.nan,
                        stetson_mag_g_fov=float(_dict['stetson_mag_g_fov']) if _dict['stetson_mag_g_fov'].strip() != '' else math.nan,
                        std_dev_over_rms_err_mag_g_fov=float(_dict['std_dev_over_rms_err_mag_g_fov']) if _dict['std_dev_over_rms_err_mag_g_fov'].strip() != '' else math.nan,
                        outlier_median_g_fov=float(_dict['outlier_median_g_fov']) if _dict['outlier_median_g_fov'].strip() != '' else math.nan,
                        num_selected_bp=int(_dict['num_selected_bp'], 16) if _dict['num_selected_bp'].strip() != '' else -1,
                        mean_obs_time_bp=float(_dict['mean_obs_time_bp']) if _dict['mean_obs_time_bp'].strip() != '' else math.nan,
                        time_duration_bp=float(_dict['time_duration_bp']) if _dict['time_duration_bp'].strip() != '' else math.nan,
                        min_mag_bp=float(_dict['min_mag_bp']) if _dict['min_mag_bp'].strip() != '' else math.nan,
                        max_mag_bp=float(_dict['max_mag_bp']) if _dict['max_mag_bp'].strip() != '' else math.nan,
                        mean_mag_bp=float(_dict['mean_mag_bp']) if _dict['mean_mag_bp'].strip() != '' else math.nan,
                        median_mag_bp=float(_dict['median_mag_bp']) if _dict['median_mag_bp'].strip() != '' else math.nan,
                        range_mag_bp=float(_dict['range_mag_bp'] if _dict['range_mag_bp'].strip() != '' else math.nan),
                        trimmed_range_mag_bp=float(_dict['trimmed_range_mag_bp']) if _dict['trimmed_range_mag_bp'].strip() != '' else math.nan,
                        std_dev_mag_bp=float(_dict['std_dev_mag_bp']) if _dict['std_dev_mag_bp'].strip() != '' else math.nan,
                        skewness_mag_bp=float(_dict['skewness_mag_bp']) if _dict['skewness_mag_bp'].strip() != '' else math.nan,
                        kurtosis_mag_bp=float(_dict['kurtosis_mag_bp']) if _dict['kurtosis_mag_bp'].strip() != '' else math.nan,
                        mad_mag_bp=float(_dict['mad_mag_bp']) if _dict['mad_mag_bp'].strip() != '' else math.nan,
                        abbe_mag_bp=float(_dict['abbe_mag_bp']) if _dict['abbe_mag_bp'].strip() != '' else math.nan,
                        iqr_mag_bp=float(_dict['iqr_mag_bp']) if _dict['iqr_mag_bp'].strip() != '' else math.nan,
                        stetson_mag_bp=float(_dict['stetson_mag_bp']) if _dict['stetson_mag_bp'].strip() != '' else math.nan,
                        std_dev_over_rms_err_mag_bp=float(_dict['std_dev_over_rms_err_mag_bp']) if _dict['std_dev_over_rms_err_mag_bp'].strip() != '' else math.nan,
                        outlier_median_bp=float(_dict['outlier_median_bp']) if _dict['outlier_median_bp'].strip() != '' else math.nan,
                        num_selected_rp=int(_dict['num_selected_rp']) if _dict['num_selected_rp'].strip() != '' else -1,
                        mean_obs_time_rp=float(_dict['mean_obs_time_rp']) if _dict['mean_obs_time_rp'].strip() != '' else math.nan,
                        time_duration_rp=float(_dict['time_duration_rp']) if _dict['time_duration_rp'].strip() != '' else math.nan,
                        min_mag_rp=float(_dict['min_mag_rp']) if _dict['min_mag_rp'].strip() != '' else math.nan,
                        max_mag_rp=float(_dict['max_mag_rp']) if _dict['max_mag_rp'].strip() != '' else math.nan,
                        mean_mag_rp=float(_dict['mean_mag_rp']) if _dict['mean_mag_rp'].strip() != '' else math.nan,
                        median_mag_rp=float(_dict['median_mag_rp'] if _dict['median_mag_rp'].strip() != '' else math.nan),
                        range_mag_rp=float(_dict['range_mag_rp']) if _dict['range_mag_rp'].strip() != '' else math.nan,
                        trimmed_range_mag_rp=float(_dict['trimmed_range_mag_rp']) if _dict['trimmed_range_mag_rp'].strip() != '' else math.nan,
                        std_dev_mag_rp=float(_dict['std_dev_mag_rp']) if _dict['std_dev_mag_rp'].strip() != '' else math.nan,
                        skewness_mag_rp=float(_dict['skewness_mag_rp']) if _dict['skewness_mag_rp'].strip() != '' else math.nan,
                        kurtosis_mag_rp=float(_dict['kurtosis_mag_rp']) if _dict['kurtosis_mag_rp'].strip() != '' else math.nan,
                        mad_mag_rp=float(_dict['mad_mag_rp']) if _dict['mad_mag_rp'].strip() != '' else math.nan,
                        abbe_mag_rp=float(_dict['abbe_mag_rp']) if _dict['abbe_mag_rp'].strip() != '' else math.nan,
                        iqr_mag_rp=float(_dict['iqr_mag_rp']) if _dict['iqr_mag_rp'].strip() != '' else math.nan,
                        stetson_mag_rp=float(_dict['stetson_mag_rp']) if _dict['stetson_mag_rp'].strip() != '' else math.nan,
                        std_dev_over_rms_err_mag_rp=float(_dict['std_dev_over_rms_err_mag_rp']) if _dict['std_dev_over_rms_err_mag_rp'].strip() != '' else math.nan,
                        outlier_median_rp=float(_dict['outlier_median_rp']) if _dict['outlier_median_rp'].strip() != '' else math.nan,
                        in_vari_classification_result=bool(_dict['in_vari_classification_result']) if _dict['in_vari_classification_result'].strip() != '' else False,
                        in_vari_rrlyrae=bool(_dict['in_vari_rrlyrae']) if _dict['in_vari_rrlyrae'].strip() != '' else False,
                        in_vari_cepheid=bool(_dict['in_vari_cepheid']) if _dict['in_vari_cepheid'].strip() != '' else False,
                        in_vari_planetary_transit=bool(_dict['in_vari_planetary_transit']) if _dict['in_vari_planetary_transit'].strip() != '' else False,
                        in_vari_short_timescale=bool(_dict['in_vari_short_timescale']) if _dict['in_vari_short_timescale'].strip() != '' else False,
                        in_vari_long_period_variable=bool(_dict['in_vari_long_period_variable']) if _dict['in_vari_long_period_variable'].strip() != '' else False,
                        in_vari_eclipsing_binary=bool(_dict['in_vari_eclipsing_binary']) if _dict['in_vari_eclipsing_binary'].strip() != '' else False,
                        in_vari_rotation_modulation=bool(_dict['in_vari_rotation_modulation']) if _dict['in_vari_rotation_modulation'].strip() != '' else False,
                        in_vari_ms_oscillator=bool(_dict['in_vari_ms_oscillator']) if _dict['in_vari_ms_oscillator'].strip() != '' else False,
                        in_vari_agn=bool(_dict['in_vari_agn']) if _dict['in_vari_agn'].strip() != '' else False,
                        in_vari_microlensing=bool(_dict['in_vari_microlensing']) if _dict['in_vari_microlensing'].strip() != '' else False,
                        in_vari_compact_companion=bool(_dict['in_vari_compact_companion']) if _dict['in_vari_compact_companion'].strip() != '' else False)
                except Exception as _e1:
                    print(f"<ERROR> failed to create record _rec={_rec}, error='{_e1}'")
                    continue
                else:
                    if (_gid % GAIADR3VARIABLE_Q3C_DIVISOR == 0) and _verbose:
                        print(f"<INFO> _gid={_gid}, created record _rec={_rec.serialized()}")

                # add record to database
                try:
                    session.add(_rec)
                    if (_gid % GAIADR3VARIABLE_Q3C_DIVISOR == 0) and _verbose:
                        session.commit()
                        print(f"_gid={_gid}, commiting record(s) OK")
                except Exception as _e2:
                    session.rollback()
                    print(f"<ERROR> _gid={_gid}, failed to insert record {_rec.serialized()} into database, error='{_e2}'")
                    continue
                else:      
                    if (_gid % GAIADR3VARIABLE_Q3C_DIVISOR == 0) and _verbose:
                        print(f"_gid={_gid}, inserted record {_rec.serialized()} into database OK")

                # incement counter
                _gid += 1

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
    _p = argparse.ArgumentParser(description='Read Gaia Variable Star File', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--file', default=GAIADR3VARIABLE_Q3C_CATALOG_FILE, help="""Input file [%(default)s]""")
    _p.add_argument(f'--index', default=f"{get_max_idx()}", help="""Index [%(default)s]""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        GAIADR3VARIABLE_q3c_read(_file=_a.file.strip(), _index=int(_a.index)+1, _verbose=bool(_a.verbose))
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
