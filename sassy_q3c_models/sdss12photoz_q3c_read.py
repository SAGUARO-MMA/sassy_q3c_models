#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.sdss12photoz_q3c_orm import *


# +
# __doc__ string
# -
__doc__ = """ python3 sdss12photoz_q3c_read.py --help """


# +
# constant(s)
# -
SDSS12PHOTOZ_Q3C_DIVISOR = 10000
SDSS12PHOTOZ_Q3C_CATALOG_FILE = os.path.abspath(os.path.expanduser('/science/catalogs/sdss12_photoz.000000.tsv'))


# +
# function: get_max_idx()
# -
def get_max_idx(_table: str = 'sdss12photoz_q3c', _index: str = 'sid') -> int:
    """ returns max row number in database table for key or -1 """
    try:
        with create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}').connect() as _c:
            _ret = [_ for _ in _c.execute(f"SELECT MAX({_index}) FROM {_table};")]
            return tuple(_ret[0])[0] if (_ret and len(_ret) == 1) else -1
    except Exception:
        return -1


# +
# function: sdss12photoz_q3c_read()
# -
# noinspection PyBroadException
def sdss12photoz_q3c_read(_file: str = SDSS12PHOTOZ_Q3C_CATALOG_FILE, _index: int = -1, _verbose: bool = False) -> None:

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
    _sid = _index
    _header = []
    with open(_file, 'r') as _fd:
        for _line in _fd:

            # initialize
            _rec, _row, _dict = None, [], {}

            # get header
            if '#RAdeg' in _line.strip():
                _header = _line.strip()[1:].split('\t')
                if _header != SDSS12PHOTOZ_HEADERS:
                    print(f"<ERROR> unexpected {_header} != {SDSS12PHOTOZ_HEADERS}")
                    return

            # get elements
            elif _line.strip()[0] != '#':
                _line = _line.replace('\t', '?')
                _row = _line.strip().split('?')
                if len(_row) != SDSS12PHOTOZ_COLUMNS:
                    print(f"<ERROR> row contains {len(_row)} columns, expected {SDSS12PHOTOZ_COLUMNS}")
                    continue

                # create dictionary
                _dict = dict(zip(_header, _row))
                if [_k for _k in _dict] == SDSS12PHOTOZ_HEADERS:
                    _dict = dict(zip(SDSS12PHOTOZ_KEYS, _row))
                    if not verify_keys(_d=_dict, _s=set(SDSS12PHOTOZ_KEYS)):
                        print(f"<ERROR> _dict = {_dict} is invalid")
                        continue

                # create orm object
                try:
                    _rec = Sdss12PhotoZQ3cRecord(
                        sid=_sid,
                        ra=float(_dict['ra']) if _dict['ra'].strip() != '' else math.nan,
                        dec=float(_dict['dec']) if _dict['dec'].strip() != '' else math.nan,
                        mode=int(_dict['mode']) if _dict['mode'].strip() != '' else -1,
                        q_mode=_dict['q_mode'].strip(),
                        classifier=int(_dict['classifier']) if _dict['classifier'].strip() != '' else -1,
                        sdss12=_dict['sdss12'].strip(),
                        m_sdss12=_dict['m_sdss12'].strip(),
                        sdssid=_dict['sdssid'].strip(),
                        objid=f"0x{_dict['objid'].strip()}",
                        specid=_dict['specid'].strip(),
                        spobjid=f"0x{_dict['spobjid'].strip()}",
                        parentid=f"0x{_dict['parentid'].strip()}",
                        flags=f"0x{_dict['flags'].strip()}",
                        status=int(_dict['status'], 16) if _dict['status'].strip() != '' else -1,
                        e_ra=float(_dict['e_ra']) if _dict['e_ra'].strip() != '' else math.nan,
                        e_dec=float(_dict['e_dec']) if _dict['e_dec'].strip() != '' else math.nan,
                        obsdate=float(_dict['obsdate']) if _dict['obsdate'].strip() != '' else math.nan,
                        quality=int(_dict['quality']) if _dict['quality'].strip() != '' else -1,
                        umag=float(_dict['umag']) if _dict['umag'].strip() != '' else math.nan,
                        e_umag=float(_dict['e_umag']) if _dict['e_umag'].strip() != '' else math.nan,
                        gmag=float(_dict['gmag']) if _dict['gmag'].strip() != '' else math.nan,
                        e_gmag=float(_dict['e_gmag']) if _dict['e_gmag'].strip() != '' else math.nan,
                        rmag=float(_dict['rmag']) if _dict['rmag'].strip() != '' else math.nan,
                        e_rmag=float(_dict['e_rmag']) if _dict['e_rmag'].strip() != '' else math.nan,
                        imag=float(_dict['imag']) if _dict['imag'].strip() != '' else math.nan,
                        e_imag=float(_dict['e_imag']) if _dict['e_imag'].strip() != '' else math.nan,
                        zmag=float(_dict['zmag']) if _dict['zmag'].strip() != '' else math.nan,
                        e_zmag=float(_dict['e_zmag']) if _dict['e_zmag'].strip() != '' else math.nan,
                        zsp=float(_dict['zsp']) if _dict['zsp'].strip() != '' else math.nan,
                        e_zsp=float(_dict['e_zsp']) if _dict['e_zsp'].strip() != '' else math.nan,
                        f_zsp=int(_dict['f_zsp'], 16) if _dict['f_zsp'].strip() != '' else -1,
                        vdisp=float(_dict['vdisp']) if _dict['e_zsp'].strip() != '' else math.nan,
                        e_vdisp=float(_dict['e_vdisp']) if _dict['e_zsp'].strip() != '' else math.nan,
                        spinst=_dict['spinst'].strip(),
                        sptype=_dict['sptype'].strip(),
                        spclass=_dict['spclass'].strip(),
                        spubclass=_dict['spubclass'].strip(),
                        spsignal=float(_dict['spsignal']) if _dict['spsignal'].strip() != '' else math.nan,
                        u_flags=f"0x{_dict['u_flags'].strip()}",
                        u_prob=int(_dict['u_prob']) if _dict['u_prob'].strip() != '' else -1,
                        u_photo=int(_dict['u_photo']) if _dict['u_photo'].strip() != '' else -1,
                        u_date=float(_dict['u_date']) if _dict['u_date'].strip() != '' else math.nan,
                        u_prime_mag=float(_dict['u_prime_mag']) if _dict['u_prime_mag'].strip() != '' else math.nan,
                        e_u_prime_mag=float(_dict['e_u_prime_mag']) if _dict['e_u_prime_mag'].strip() != '' else math.nan,
                        u_pmag=float(_dict['u_pmag']) if _dict['u_pmag'].strip() != '' else math.nan,
                        e_u_pmag=float(_dict['e_u_pmag']) if _dict['e_u_pmag'].strip() != '' else math.nan,
                        u_upmag=float(_dict['u_upmag'] if _dict['u_upmag'].strip() != '' else math.nan),
                        e_u_upmag=float(_dict['e_u_upmag']) if _dict['e_u_upmag'].strip() != '' else math.nan,
                        u_prad=float(_dict['u_prad']) if _dict['u_prad'].strip() != '' else math.nan,
                        e_u_prad=float(_dict['e_u_prad']) if _dict['e_u_prad'].strip() != '' else math.nan,
                        u_ora=float(_dict['u_ora']) if _dict['u_ora'].strip() != '' else math.nan,
                        u_odec=float(_dict['u_odec']) if _dict['u_odec'].strip() != '' else math.nan,
                        u_dvrad=float(_dict['u_dvrad']) if _dict['u_dvrad'].strip() != '' else math.nan,
                        u_dvell=float(_dict['u_dvell']) if _dict['u_dvell'].strip() != '' else math.nan,
                        u_pa=float(_dict['u_pa']) if _dict['u_pa'].strip() != '' else math.nan,
                        g_flags=f"0x{_dict['g_flags'].strip()}",
                        g_prob=int(_dict['g_prob']) if _dict['g_prob'].strip() != '' else -1,
                        g_photo=int(_dict['g_photo']) if _dict['g_photo'].strip() != '' else -1,
                        g_date=float(_dict['g_date']) if _dict['g_date'].strip() != '' else math.nan,
                        g_prime_mag=float(_dict['g_prime_mag']) if _dict['g_prime_mag'].strip() != '' else math.nan,
                        e_g_prime_mag=float(_dict['e_g_prime_mag']) if _dict['e_g_prime_mag'].strip() != '' else math.nan,
                        g_pmag=float(_dict['g_pmag']) if _dict['g_pmag'].strip() != '' else math.nan,
                        e_g_pmag=float(_dict['e_g_pmag']) if _dict['e_g_pmag'].strip() != '' else math.nan,
                        g_upmag=float(_dict['g_upmag'] if _dict['g_upmag'].strip() != '' else math.nan),
                        e_g_upmag=float(_dict['e_g_upmag']) if _dict['e_g_upmag'].strip() != '' else math.nan,
                        g_prad=float(_dict['g_prad']) if _dict['g_prad'].strip() != '' else math.nan,
                        e_g_prad=float(_dict['e_g_prad']) if _dict['e_g_prad'].strip() != '' else math.nan,
                        g_ora=float(_dict['g_ora']) if _dict['g_ora'].strip() != '' else math.nan,
                        g_odec=float(_dict['g_odec']) if _dict['g_odec'].strip() != '' else math.nan,
                        g_dvrad=float(_dict['g_dvrad']) if _dict['g_dvrad'].strip() != '' else math.nan,
                        g_dvell=float(_dict['g_dvell']) if _dict['g_dvell'].strip() != '' else math.nan,
                        g_pa=float(_dict['g_pa']) if _dict['g_pa'].strip() != '' else math.nan,
                        r_flags=f"0x{_dict['r_flags'].strip()}",
                        r_prob=int(_dict['r_prob']) if _dict['r_prob'].strip() != '' else -1,
                        r_photo=int(_dict['r_photo']) if _dict['r_photo'].strip() != '' else -1,
                        r_date=float(_dict['r_date']) if _dict['r_date'].strip() != '' else math.nan,
                        r_prime_mag=float(_dict['r_prime_mag']) if _dict['r_prime_mag'].strip() != '' else math.nan,
                        e_r_prime_mag=float(_dict['e_r_prime_mag']) if _dict['e_r_prime_mag'].strip() != '' else math.nan,
                        r_pmag=float(_dict['r_pmag']) if _dict['r_pmag'].strip() != '' else math.nan,
                        e_r_pmag=float(_dict['e_r_pmag']) if _dict['e_r_pmag'].strip() != '' else math.nan,
                        r_upmag=float(_dict['r_upmag'] if _dict['r_upmag'].strip() != '' else math.nan),
                        e_r_upmag=float(_dict['e_r_upmag']) if _dict['e_r_upmag'].strip() != '' else math.nan,
                        r_prad=float(_dict['r_prad']) if _dict['r_prad'].strip() != '' else math.nan,
                        e_r_prad=float(_dict['e_r_prad']) if _dict['e_r_prad'].strip() != '' else math.nan,
                        r_ora=float(_dict['r_ora']) if _dict['r_ora'].strip() != '' else math.nan,
                        r_odec=float(_dict['r_odec']) if _dict['r_odec'].strip() != '' else math.nan,
                        r_dvrad=float(_dict['r_dvrad']) if _dict['r_dvrad'].strip() != '' else math.nan,
                        r_dvell=float(_dict['r_dvell']) if _dict['r_dvell'].strip() != '' else math.nan,
                        r_pa=float(_dict['r_pa']) if _dict['r_pa'].strip() != '' else math.nan,
                        i_flags=f"0x{_dict['i_flags'].strip()}",
                        i_prob=int(_dict['i_prob']) if _dict['i_prob'].strip() != '' else -1,
                        i_photo=int(_dict['i_photo']) if _dict['i_photo'].strip() != '' else -1,
                        i_date=float(_dict['i_date']) if _dict['i_date'].strip() != '' else math.nan,
                        i_prime_mag=float(_dict['i_prime_mag']) if _dict['i_prime_mag'].strip() != '' else math.nan,
                        e_i_prime_mag=float(_dict['e_i_prime_mag']) if _dict['e_i_prime_mag'].strip() != '' else math.nan,
                        i_pmag=float(_dict['i_pmag']) if _dict['i_pmag'].strip() != '' else math.nan,
                        e_i_pmag=float(_dict['e_i_pmag']) if _dict['e_i_pmag'].strip() != '' else math.nan,
                        i_upmag=float(_dict['i_upmag'] if _dict['i_upmag'].strip() != '' else math.nan),
                        e_i_upmag=float(_dict['e_i_upmag']) if _dict['e_i_upmag'].strip() != '' else math.nan,
                        i_prad=float(_dict['i_prad']) if _dict['i_prad'].strip() != '' else math.nan,
                        e_i_prad=float(_dict['e_i_prad']) if _dict['e_i_prad'].strip() != '' else math.nan,
                        i_ora=float(_dict['i_ora']) if _dict['i_ora'].strip() != '' else math.nan,
                        i_odec=float(_dict['i_odec']) if _dict['i_odec'].strip() != '' else math.nan,
                        i_dvrad=float(_dict['i_dvrad']) if _dict['i_dvrad'].strip() != '' else math.nan,
                        i_dvell=float(_dict['i_dvell']) if _dict['i_dvell'].strip() != '' else math.nan,
                        i_pa=float(_dict['i_pa']) if _dict['i_pa'].strip() != '' else math.nan,
                        z_flags=f"0x{_dict['z_flags'].strip()}",
                        z_prob=int(_dict['z_prob']) if _dict['z_prob'].strip() != '' else -1,
                        z_photo=int(_dict['z_photo']) if _dict['z_photo'].strip() != '' else -1,
                        z_date=float(_dict['z_date']) if _dict['z_date'].strip() != '' else math.nan,
                        z_prime_mag=float(_dict['z_prime_mag']) if _dict['z_prime_mag'].strip() != '' else math.nan,
                        e_z_prime_mag=float(_dict['e_z_prime_mag']) if _dict['e_z_prime_mag'].strip() != '' else math.nan,
                        z_pmag=float(_dict['z_pmag']) if _dict['z_pmag'].strip() != '' else math.nan,
                        e_z_pmag=float(_dict['e_z_pmag']) if _dict['e_z_pmag'].strip() != '' else math.nan,
                        z_upmag=float(_dict['z_upmag'] if _dict['z_upmag'].strip() != '' else math.nan),
                        e_z_upmag=float(_dict['e_z_upmag']) if _dict['e_z_upmag'].strip() != '' else math.nan,
                        z_prad=float(_dict['z_prad']) if _dict['z_prad'].strip() != '' else math.nan,
                        e_z_prad=float(_dict['e_z_prad']) if _dict['e_z_prad'].strip() != '' else math.nan,
                        z_ora=float(_dict['z_ora']) if _dict['z_ora'].strip() != '' else math.nan,
                        z_odec=float(_dict['z_odec']) if _dict['z_odec'].strip() != '' else math.nan,
                        z_dvrad=float(_dict['z_dvrad']) if _dict['z_dvrad'].strip() != '' else math.nan,
                        z_dvell=float(_dict['z_dvell']) if _dict['z_dvell'].strip() != '' else math.nan,
                        z_pa=float(_dict['z_pa']) if _dict['z_pa'].strip() != '' else math.nan,
                        pmra=float(_dict['pmra']) if _dict['pmra'].strip() != '' else math.nan,
                        e_pmra=float(_dict['e_pmra']) if _dict['e_pmra'].strip() != '' else math.nan,
                        pmdec=float(_dict['pmdec']) if _dict['pmdec'].strip() != '' else math.nan,
                        e_pmdec=float(_dict['e_pmdec']) if _dict['e_pmdec'].strip() != '' else math.nan,
                        sigra=float(_dict['sigra']) if _dict['sigra'].strip() != '' else math.nan,
                        sigdec=float(_dict['sigdec']) if _dict['sigdec'].strip() != '' else math.nan,
                        m=int(_dict['m']) if _dict['m'].strip() != '' else -1,
                        n=int(_dict['n']) if _dict['n'].strip() != '' else -1,
                        g_o_plate=float(_dict['g_o_plate']) if _dict['g_o_plate'].strip() != '' else math.nan,
                        r_e_plate=float(_dict['r_e_plate']) if _dict['r_e_plate'].strip() != '' else math.nan,
                        g_j_plate=float(_dict['g_j_plate']) if _dict['g_j_plate'].strip() != '' else math.nan,
                        r_f_plate=float(_dict['r_f_plate']) if _dict['r_f_plate'].strip() != '' else math.nan,
                        i_n_plate=float(_dict['i_n_plate']) if _dict['i_n_plate'].strip() != '' else math.nan,
                        zph=float(_dict['zph']) if _dict['zph'].strip() != '' else math.nan,
                        e_zph=float(_dict['e_zph']) if _dict['e_zph'].strip() != '' else math.nan,
                        ave_zph=float(_dict['ave_zph']) if _dict['ave_zph'].strip() != '' else math.nan,
                        chi2=float(_dict['chi2']) if _dict['chi2'].strip() != '' else math.nan,
                        abs_u_mag=float(_dict['abs_u_mag']) if _dict['abs_u_mag'].strip() != '' else math.nan,
                        abs_g_mag=float(_dict['abs_g_mag']) if _dict['abs_g_mag'].strip() != '' else math.nan,
                        abs_r_mag=float(_dict['abs_r_mag']) if _dict['abs_r_mag'].strip() != '' else math.nan,
                        abs_i_mag=float(_dict['abs_i_mag']) if _dict['abs_i_mag'].strip() != '' else math.nan,
                        abs_z_mag=float(_dict['abs_z_mag']) if _dict['abs_z_mag'].strip() != '' else math.nan)
                except Exception as _e1:
                    print(f"<ERROR> failed to create record _rec={_rec}, error='{_e1}'")
                    continue
                else:
                    if (_sid % SDSS12PHOTOZ_Q3C_DIVISOR == 0) and _verbose:
                        print(f"<INFO> _sid={_sid}, created record _rec={_rec.serialized()}")

                # add record to database
                try:
                    session.add(_rec)
                    if (_sid % SDSS12PHOTOZ_Q3C_DIVISOR == 0) and _verbose:
                        session.commit()
                        print(f"_sid={_sid}, commiting record(s) OK")
                except Exception as _e2:
                    session.rollback()
                    print(f"<ERROR> _sid={_sid}, failed to insert record {_rec.serialized()} into database, error='{_e2}'")
                    continue
                else:      
                    if (_sid % SDSS12PHOTOZ_Q3C_DIVISOR == 0) and _verbose:
                        print(f"_sid={_sid}, inserted record {_rec.serialized()} into database OK")

                # incement counter
                _sid += 1

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
    _p = argparse.ArgumentParser(description='Read SDSS12 PhotoZ File', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--file', default=SDSS12PHOTOZ_Q3C_CATALOG_FILE, help="""Input file [%(default)s]""")
    _p.add_argument(f'--index', default=f"{get_max_idx()}", help="""Index [%(default)s]""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        sdss12photoz_q3c_read(_file=_a.file.strip(), _index=int(_a.index)+1, _verbose=bool(_a.verbose))
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
