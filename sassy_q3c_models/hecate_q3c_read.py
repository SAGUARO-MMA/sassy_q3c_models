#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.hecate_q3c_orm import *


# +
# __doc__ string
# -
__doc__ = """ python3 hecate_q3c_read.py --help """


# +
# constant(s)
# -
random.seed(os.getpid())
HECATE_Q3C_DIVISOR = 1000
HECATE_Q3C_CATALOG_FILE = os.path.abspath(os.path.expanduser('HECATE_v1.1.csv'))
HECATE_BAD_VALUES = ['" "', '', 'null', '-']
HECATE_TRUE_VALUES = ['t', 'true', '1']
HECATE_FALSE_VALUES = ['f', 'false', '0']


# +
# function: hecate_q3c_read()
# -
# noinspection PyBroadException
def hecate_q3c_read(_file: str = HECATE_Q3C_CATALOG_FILE, _delimeter: str = ',', _verbose: bool = False) -> None:

    # check input(s)
    _file = os.path.abspath(os.path.expanduser(_file))
    if not isinstance(_file, str) or not os.path.exists(_file):
        raise Exception(f"invalid input, _file={_file}")

    # connect to database
    if _verbose:
        print(f"connecting to database postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    try:
        engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        get_session = sessionmaker(bind=engine)
        session = get_session()
    except Exception as _c:
        raise Exception(f"failed connecting to database postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}, error={_c}")
    else:
        if _verbose:
            print(f"connected to database postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME} OK")

    # read the file
    _hid = 0
    with open(_file, 'r') as _fd:
        for _line in _fd:
            if _line[0] in '#!+':
                continue
            _hid += 1

            # split up row and check the number of entries
            _line = _line.replace("\n", "")
            _row = _line.split(sep=f"{_delimeter}")
            if len(_row) != HECATE_COLUMNS:
                _hid -= 1
                print(f"<ERROR> {_hid}: _line={_line}")
                print(f"<ERROR> {_hid}: _row={_row}, len={len(_row)}")
                print(f"<ERROR> row contains {len(_row)} columns, expected {HECATE_COLUMNS}")

            # get clean data
            else:
                _q3c, _rec = {}, None
                if (_hid % HECATE_Q3C_DIVISOR == 0) and _verbose:
                    print(f"<OK> {_hid}: _line={_line}")
                    print(f"<OK>{_hid}: _row={_row}, len={len(_row)}")
                try:
                    _q3c['pgc'] = int(_row[0]) if _row[0].strip().lower() not in HECATE_BAD_VALUES else -1
                    _q3c['objname'] = _row[1]
                    _q3c['id_ned'] = _row[2]
                    _q3c['id_nedd'] = _row[3]
                    _q3c['id_iras'] = _row[4]
                    _q3c['id_2mass'] = _row[5]
                    _q3c['sdss_photid'] = _row[6]
                    _q3c['sdss_specid'] = _row[7]
                    _q3c['ra'] = float(_row[8]) if _row[8].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['dec'] = float(_row[9]) if _row[9].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['f_astrom'] = int(_row[10]) if _row[10].strip().lower() not in HECATE_BAD_VALUES else -1
                    _q3c['r1'] = float(_row[11]) if _row[11].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['r2'] = float(_row[12]) if _row[12].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['pa'] = float(_row[13]) if _row[13].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['rsource'] = _row[14] if _row[14].strip().lower() not in HECATE_BAD_VALUES else ''
                    _q3c['rflag'] = int(_row[15]) if _row[15].strip().lower() not in HECATE_BAD_VALUES else -1
                    _q3c['t'] = float(_row[16]) if _row[16].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_t'] = float(_row[17]) if _row[17].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['incl'] = float(_row[18]) if _row[18].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['v'] = float(_row[19]) if _row[19].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_v'] = float(_row[20]) if _row[20].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['v_vir'] = float(_row[21]) if _row[21].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_v_vir'] = float(_row[22]) if _row[22].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['ndist'] = int(_row[23]) if _row[23].strip().lower() not in HECATE_BAD_VALUES else -1
                    _q3c['edist'] = True if _row[24].strip().lower() in HECATE_TRUE_VALUES else False
                    _q3c['d'] = float(_row[25]) if _row[25].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_d'] = float(_row[26]) if _row[26].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['d_lo68'] = float(_row[27]) if _row[27].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['d_hi68'] = float(_row[28]) if _row[28].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['d_lo95'] = float(_row[29]) if _row[29].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['d_hi95'] = float(_row[30]) if _row[30].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['dmethod'] = _row[31]
                    _q3c['ut'] = float(_row[32]) if _row[32].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['bt'] = float(_row[33]) if _row[33].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['vt'] = float(_row[34]) if _row[34].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['it'] = float(_row[35]) if _row[35].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_ut'] = float(_row[36]) if _row[36].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_bt'] = float(_row[37]) if _row[37].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_vt'] = float(_row[38]) if _row[38].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_it'] = float(_row[39]) if _row[39].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['ag'] = float(_row[40]) if _row[40].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['ai'] = float(_row[41]) if _row[41].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['s12'] = float(_row[42]) if _row[42].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['s25'] = float(_row[43]) if _row[43].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['s60'] = float(_row[44]) if _row[44].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['s100'] = float(_row[45]) if _row[45].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['q12'] = float(_row[46]) if _row[46].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['q25'] = float(_row[47]) if _row[47].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['q60'] = float(_row[48]) if _row[48].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['q100'] = float(_row[49]) if _row[49].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['wf1'] = float(_row[50]) if _row[50].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['wf2'] = float(_row[51]) if _row[51].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['wf3'] = float(_row[52]) if _row[52].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['wf4'] = float(_row[53]) if _row[53].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_wf1'] = float(_row[54]) if _row[54].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_wf2'] = float(_row[55]) if _row[55].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_wf3'] = float(_row[56]) if _row[56].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_wf4'] = float(_row[57]) if _row[57].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['wfpoint'] = True if _row[58] in HECATE_TRUE_VALUES else False
                    _q3c['wftreat'] = True if _row[59] in HECATE_TRUE_VALUES else False
                    _q3c['j'] = float(_row[60]) if _row[60].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['h'] = float(_row[61]) if _row[61].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['k'] = float(_row[62]) if _row[62].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_j'] = float(_row[63]) if _row[63].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_h'] = float(_row[64]) if _row[64].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_k'] = float(_row[65]) if _row[65].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['flag_2mass'] = int(_row[66]) if _row[66].strip().lower() not in HECATE_BAD_VALUES else -1
                    _q3c['u'] = float(_row[67]) if _row[67].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['g'] = float(_row[68]) if _row[68].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['r'] = float(_row[69]) if _row[69].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['i'] = float(_row[70]) if _row[70].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['z'] = float(_row[71]) if _row[71].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_u'] = float(_row[72]) if _row[72].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_g'] = float(_row[73]) if _row[73].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_r'] = float(_row[74]) if _row[74].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_i'] = float(_row[75]) if _row[75].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['e_z'] = float(_row[76]) if _row[76].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['logl_tir'] = float(_row[77]) if _row[77].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['logl_fir'] = float(_row[78]) if _row[78].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['logl_60u'] = float(_row[79]) if _row[79].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['logl_12u'] = float(_row[80]) if _row[80].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['logl_22u'] = float(_row[81]) if _row[81].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['logl_k'] = float(_row[82]) if _row[82].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['ml_ratio'] = float(_row[83]) if _row[83].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['logsfr_tir'] = float(_row[84]) if _row[84].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['logsfr_fir'] = float(_row[85]) if _row[85].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['logsfr_60u'] = float(_row[86]) if _row[86].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['logsfr_12u'] = float(_row[87]) if _row[87].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['logsfr_22u'] = float(_row[88]) if _row[88].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['logsfr_hec'] = float(_row[89]) if _row[89].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['sfr_hec_flag'] = _row[90]
                    _q3c['logm_hec'] = float(_row[91]) if _row[91].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['logsfr_gsw'] = float(_row[92]) if _row[92].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['logm_gsw'] = float(_row[93]) if _row[93].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['min_snr'] = float(_row[94]) if _row[94].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['metal'] = float(_row[95]) if _row[95].strip().lower() not in HECATE_BAD_VALUES else math.nan
                    _q3c['flag_metal'] = int(_row[96]) if _row[96].strip().lower() not in HECATE_BAD_VALUES else -1
                    _q3c['class_sp'] = int(_row[97]) if _row[97].strip().lower() not in HECATE_BAD_VALUES else -1
                    _q3c['agn_s17'] = _row[98]
                    _q3c['agn_hec'] = _row[99]
                except Exception as _e:
                    print(f"{_hid}: _line={_line}")
                    print(f"{_hid}: _row={_row}, len={len(_row)}")
                    print(f"<ERROR> failed to create dictionary _q3c={_q3c}, error={_e}")
                else:
                    if (_hid % HECATE_Q3C_DIVISOR == 0) and _verbose:
                        print(f"{_hid}: _line={_line}")
                        print(f"{_hid}: _row={_row}, len={len(_row)}")
                        print(f"created _q3c={_q3c} OK")

                # create record
                try:
                    _rec = HecateQ3cRecord(hid=_hid, **_q3c)
                except Exception as _x:
                    print(f"<ERROR> failed to create record _rec={_rec}, error={_x}")
                else:
                    if (_hid % HECATE_Q3C_DIVISOR == 0) and _verbose:
                        print(f"created record _rec={_rec.serialized()} OK")

                # add record to database
                try:
                    session.add(_rec)
                    session.commit()
                except Exception as _d:
                    session.rollback()
                    print(f"<ERROR> failed to insert record {_rec.serialized()} into database, error={_d}")
                else:
                    if (_hid % HECATE_Q3C_DIVISOR == 0) and _verbose:
                        print(f"inserted record {_rec.serialized()} into database OK")

    session.close()


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description='Read HECATE Catalog', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--file', default=HECATE_Q3C_CATALOG_FILE, help="""Input file [%(default)s]""")
    _p.add_argument(f'--delimeter', default=",", help="""Input file [%(default)s]""")
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        hecate_q3c_read(_file=_a.file.strip(), _delimeter=f'{_a.delimeter}', _verbose=bool(_a.verbose))
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
