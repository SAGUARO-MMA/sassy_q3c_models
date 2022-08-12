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
SDSS12PHOTOZ_Q3C_DIVISOR = 50000
SDSS12PHOTOZ_Q3C_CATALOG_FILE = os.path.abspath(os.path.expanduser('/science/catalogs/sdss12_photoz.000782.tsv'))


# +
# function: sdss12photoz_q3c_read()
# -
# noinspection PyBroadException
def sdss12photoz_q3c_read(_file: str = SDSS12PHOTOZ_Q3C_CATALOG_FILE, _verbose: bool = False) -> None:

    # check input(s)
    _file = os.path.abspath(os.path.expanduser(_file))
    if not os.path.exists(_file):
        raise Exception(f"invalid input, _file={_file}")

    # connect to database
    # if _verbose:
    #     print(f"connecting to database postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    # try:
    #     engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    #     get_session = sessionmaker(bind=engine)
    #     session = get_session()
    # except Exception as _c:
    #     raise Exception(f"failed connecting to database "
    #                     f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}, error={_c}")
    # else:
    #     if _verbose:
    #         print(f"connected to database postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME} OK")

    # read the file
    _lc, _sid = 0, 0
    _header, _row, _dict = [], [], {}
    with open(_file, 'r') as _fd:
        for _line in _fd:

            # first line of file should be a header
            if _line[0] == '#' and _lc == 0:
                _header = _line.strip()[1:].split('\t')

            # get elements and create dictionary
            else:
                _lc += 1
                _sid += 1
                _line = _line.replace('\t', '?')
                _row = _line.strip().split('?')
                if len(_row) != SDSS12PHOTOZ_COLUMNS:
                    print(f"<ERROR> line {_lc}: row contains {len(_row)} columns, expected {SDSS12PHOTOZ_COLUMNS}")
                    _sid -= 1
                    continue
                else:
                    _dict = dict(zip(_header, _row))
                    if [_k for _k in _dict] == SDSS12PHOTOZ_HEADERS:
                        _dict = dict(zip(SDSS12PHOTOZ_KEYS, _row))

                if not verify_keys(_d=_dict, _s=set(SDSS12PHOTOZ_KEYS)):
                    print(f"<ERROR> line {_lc}: _dict = {_dict} is INVALID")
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
                        objid=_dict['objid'].strip(),
                        specid=_dict['specid'].strip(),
                        spobjid=int(_dict['spobjid']) if _dict['spobjid'].strip() != '' else -1,
                        parentid=int(_dict['parentid']) if _dict['parentid'].strip() != '' else -1,
                        flags=int(_dict['flags']) if _dict['flags'].strip() != '' else -1,
                        status=int(_dict['status']) if _dict['status'].strip() != '' else -1,
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
                        f_zsp=int(_dict['f_zsp']) if _dict['e_zsp'].strip() != '' else math.nan,
                        vdisp=float(_dict['vdisp']) if _dict['e_zsp'].strip() != '' else math.nan,
                        e_vdisp=float(_dict['e_vdisp']) if _dict['e_zsp'].strip() != '' else math.nan,
                        spinst=_dict['spinst'].strip(),
                        sptype=_dict['sptype'].strip(),
                        spclass=_dict['spclass'].strip(),
                        spubclass=_dict['spubclass'].strip(),
                        spsignal=float(_dict['spsignal']) if _dict['spsignal'].strip() != '' else math.nan,
                        u_flags=int(_dict['u_flags']) if _dict['u_flags'].strip() != '' else -1,
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
                        g_flags=int(_dict['g_flags']) if _dict['g_flags'].strip() != '' else -1,
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
                        r_flags=int(_dict['r_flags']) if _dict['r_flags'].strip() != '' else -1,
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
                        i_flags=int(_dict['i_flags']) if _dict['i_flags'].strip() != '' else -1,
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
                        z_flags=int(_dict['z_flags']) if _dict['z_flags'].strip() != '' else -1,
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
                except Exception as _:
                    print(f'<ERROR> failed to create record _rec={_rec}')
                    continue
                else:
                    if _sid % SDSS12PHOTOZ_Q3C_DIVISOR == 0:
                        print(f"<OK> _lc={_lc}, _sid={_sid}, created dictionary _dict = {_dict}")
                        print(f'<OK> _lc={_lc}, _sid={_sid}, created record _rec={_rec.serialized()}')

                # add record to database
                # try:
                #     session.add(_sdss12photoz_rec)
                #     session.commit()
                # except Exception as _d:
                #     session.rollback()
                #     print(f"<ERROR> failed to insert record {_sdss12photoz_rec.serialized()} into database, error={_d}")
                # else:
                #     if (_sid % SDSS12PHOTOZ_Q3C_DIVISOR == 0) and _verbose:
                #         print(f"inserted record {_sdss12photoz_rec.serialized()} into database OK")

    # disconnect database
    # session.close()


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description='Read SDSS12 PhotoZ File', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--file', default=SDSS12PHOTOZ_Q3C_CATALOG_FILE, help="""Input file [%(default)s]""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    # try:
    sdss12photoz_q3c_read(_file=_a.file.strip(), _verbose=bool(_a.verbose))
    # except Exception as _:
    #     if bool(_a.verbose):
    #         print(f"{_}")
    #     print(f"Use: {__doc__}")
