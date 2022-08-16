#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                       Table "public.sdss12photoz_q3c"
    Column     |         Type          | Collation | Nullable |                    Default                    
---------------+-----------------------+-----------+----------+-----------------------------------------------
 sid           | integer               |           | not null | nextval('sdss12photoz_q3c_sid_seq'::regclass)
 ra            | double precision      |           |          | 
 dec           | double precision      |           |          | 
 mode          | integer               |           |          | 
 q_mode        | character varying(1)  |           |          | 
 classifier    | integer               |           |          | 
 sdss12        | character varying(24) |           |          | 
 m_sdss12      | character varying(1)  |           |          | 
 sdssid        | character varying(32) |           |          | 
 objid         | character varying(24) |           |          | 
 specid        | character varying(32) |           |          | 
 spobjid       | character varying(24) |           |          | 
 parentid      | character varying(24) |           |          | 
 flags         | character varying(24) |           |          | 
 status        | integer               |           |          | 
 e_ra          | double precision      |           |          | 
 e_dec         | double precision      |           |          | 
 obsdate       | double precision      |           |          | 
 quality       | integer               |           |          | 
 umag          | double precision      |           |          | 
 e_umag        | double precision      |           |          | 
 gmag          | double precision      |           |          | 
 e_gmag        | double precision      |           |          | 
 rmag          | double precision      |           |          | 
 e_rmag        | double precision      |           |          | 
 imag          | double precision      |           |          | 
 e_imag        | double precision      |           |          | 
 zmag          | double precision      |           |          | 
 e_zmag        | double precision      |           |          | 
 zsp           | double precision      |           |          | 
 e_zsp         | double precision      |           |          | 
 f_zsp         | integer               |           |          | 
 vdisp         | double precision      |           |          | 
 e_vdisp       | double precision      |           |          | 
 spinst        | character varying(24) |           |          | 
 sptype        | character varying(24) |           |          | 
 spclass       | character varying(24) |           |          | 
 spubclass     | character varying(24) |           |          | 
 spsignal      | double precision      |           |          | 
 u_flags       | character varying(24) |           |          | 
 u_prob        | integer               |           |          | 
 u_photo       | integer               |           |          | 
 u_date        | double precision      |           |          | 
 u_prime_mag   | double precision      |           |          | 
 e_u_prime_mag | double precision      |           |          | 
 u_pmag        | double precision      |           |          | 
 e_u_pmag      | double precision      |           |          | 
 u_upmag       | double precision      |           |          | 
 e_u_upmag     | double precision      |           |          | 
 u_prad        | double precision      |           |          | 
 e_u_prad      | double precision      |           |          | 
 u_ora         | double precision      |           |          | 
 u_odec        | double precision      |           |          | 
 u_dvrad       | double precision      |           |          | 
 u_dvell       | double precision      |           |          | 
 u_pa          | double precision      |           |          | 
 g_flags       | character varying(24) |           |          | 
 g_prob        | integer               |           |          | 
 g_photo       | integer               |           |          | 
 g_date        | double precision      |           |          | 
 g_prime_mag   | double precision      |           |          | 
 e_g_prime_mag | double precision      |           |          | 
 g_pmag        | double precision      |           |          | 
 e_g_pmag      | double precision      |           |          | 
 g_upmag       | double precision      |           |          | 
 e_g_upmag     | double precision      |           |          | 
 g_prad        | double precision      |           |          | 
 e_g_prad      | double precision      |           |          | 
 g_ora         | double precision      |           |          | 
 g_odec        | double precision      |           |          | 
 g_dvrad       | double precision      |           |          | 
 g_dvell       | double precision      |           |          | 
 g_pa          | double precision      |           |          | 
 r_flags       | character varying(24) |           |          | 
 r_prob        | integer               |           |          | 
 r_photo       | integer               |           |          | 
 r_date        | double precision      |           |          | 
 r_prime_mag   | double precision      |           |          | 
 e_r_prime_mag | double precision      |           |          | 
 r_pmag        | double precision      |           |          | 
 e_r_pmag      | double precision      |           |          | 
 r_upmag       | double precision      |           |          | 
 e_r_upmag     | double precision      |           |          | 
 r_prad        | double precision      |           |          | 
 e_r_prad      | double precision      |           |          | 
 r_ora         | double precision      |           |          | 
 r_odec        | double precision      |           |          | 
 r_dvrad       | double precision      |           |          | 
 r_dvell       | double precision      |           |          | 
 r_pa          | double precision      |           |          | 
 i_flags       | character varying(24) |           |          | 
 i_prob        | integer               |           |          | 
 i_photo       | integer               |           |          | 
 i_date        | double precision      |           |          | 
 i_prime_mag   | double precision      |           |          | 
 e_i_prime_mag | double precision      |           |          | 
 i_pmag        | double precision      |           |          | 
 e_i_pmag      | double precision      |           |          | 
 i_upmag       | double precision      |           |          | 
 e_i_upmag     | double precision      |           |          | 
 i_prad        | double precision      |           |          | 
 e_i_prad      | double precision      |           |          | 
 i_ora         | double precision      |           |          | 
 i_odec        | double precision      |           |          | 
 i_dvrad       | double precision      |           |          | 
 i_dvell       | double precision      |           |          | 
 i_pa          | double precision      |           |          | 
 z_flags       | character varying(24) |           |          | 
 z_prob        | integer               |           |          | 
 z_photo       | integer               |           |          | 
 z_date        | double precision      |           |          | 
 z_prime_mag   | double precision      |           |          | 
 e_z_prime_mag | double precision      |           |          | 
 z_pmag        | double precision      |           |          | 
 e_z_pmag      | double precision      |           |          | 
 z_upmag       | double precision      |           |          | 
 e_z_upmag     | double precision      |           |          | 
 z_prad        | double precision      |           |          | 
 e_z_prad      | double precision      |           |          | 
 z_ora         | double precision      |           |          | 
 z_odec        | double precision      |           |          | 
 z_dvrad       | double precision      |           |          | 
 z_dvell       | double precision      |           |          | 
 z_pa          | double precision      |           |          | 
 pmra          | double precision      |           |          | 
 e_pmra        | double precision      |           |          | 
 pmdec         | double precision      |           |          | 
 e_pmdec       | double precision      |           |          | 
 sigra         | double precision      |           |          | 
 sigdec        | double precision      |           |          | 
 m             | integer               |           |          | 
 n             | integer               |           |          | 
 g_o_plate     | double precision      |           |          | 
 r_e_plate     | double precision      |           |          | 
 g_j_plate     | double precision      |           |          | 
 r_f_plate     | double precision      |           |          | 
 i_n_plate     | double precision      |           |          | 
 zph           | double precision      |           |          | 
 e_zph         | double precision      |           |          | 
 ave_zph       | double precision      |           |          | 
 chi2          | double precision      |           |          | 
 abs_u_mag     | double precision      |           |          | 
 abs_g_mag     | double precision      |           |          | 
 abs_r_mag     | double precision      |           |          | 
 abs_i_mag     | double precision      |           |          | 
 abs_z_mag     | double precision      |           |          | 
Indexes:
    "sdss12photoz_q3c_pkey" PRIMARY KEY, btree (sid)
    "idx_sdss12photoz_q3c_abs_g_mag" btree (abs_g_mag)
    "idx_sdss12photoz_q3c_abs_i_mag" btree (abs_i_mag)
    "idx_sdss12photoz_q3c_abs_r_mag" btree (abs_r_mag)
    "idx_sdss12photoz_q3c_abs_u_mag" btree (abs_u_mag)
    "idx_sdss12photoz_q3c_abs_z_mag" btree (abs_z_mag)
    "idx_sdss12photoz_q3c_ave_zph" btree (ave_zph)
    "idx_sdss12photoz_q3c_g_pmag" btree (g_pmag)
    "idx_sdss12photoz_q3c_g_prime_mag" btree (g_prime_mag)
    "idx_sdss12photoz_q3c_g_upmag" btree (g_upmag)
    "idx_sdss12photoz_q3c_gmag" btree (gmag)
    "idx_sdss12photoz_q3c_i_pmag" btree (i_pmag)
    "idx_sdss12photoz_q3c_i_prime_mag" btree (i_prime_mag)
    "idx_sdss12photoz_q3c_i_upmag" btree (i_upmag)
    "idx_sdss12photoz_q3c_imag" btree (imag)
    "idx_sdss12photoz_q3c_r_pmag" btree (r_pmag)
    "idx_sdss12photoz_q3c_r_prime_mag" btree (r_prime_mag)
    "idx_sdss12photoz_q3c_r_upmag" btree (r_upmag)
    "idx_sdss12photoz_q3c_rmag" btree (rmag)
    "idx_sdss12photoz_q3c_u_pmag" btree (u_pmag)
    "idx_sdss12photoz_q3c_u_prime_mag" btree (u_prime_mag)
    "idx_sdss12photoz_q3c_u_upmag" btree (u_upmag)
    "idx_sdss12photoz_q3c_umag" btree (umag)
    "idx_sdss12photoz_q3c_z_pmag" btree (z_pmag)
    "idx_sdss12photoz_q3c_z_prime_mag" btree (z_prime_mag)
    "idx_sdss12photoz_q3c_z_upmag" btree (z_upmag)
    "idx_sdss12photoz_q3c_zmag" btree (zmag)
    "idx_sdss12photoz_q3c_zph" btree (zph)
    "idx_sdss12photoz_q3c_zsp" btree (zsp)
    "sdss12photoz_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(ra, "dec")) CLUSTER
"""


# +
# constant(s)
# -
SDSS12PHOTOZ_DAT_URL = 'None'
SDSS12PHOTOZ_PAG_URL = 'https://vizier.u-strasbg.fr/viz-bin/VizieR?-source=+SDSS-DR12'
SDSS12PHOTOZ_PDF_URL = 'https://arxiv.org/pdf/1501.00963.pdf'
SDSS12PHOTOZ_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
SDSS12PHOTOZ_SORT_VALUE = ['sid', 'sdss12', 'ra', 'dec', 'obsdate', 'umag', 'gmag', 'rmag', 'imag', 'zsp', 'zph', 'ave_zph']
SDSS12PHOTOZ_HTUPLES = (
    # 0: 'RAdeg', 'DEdeg', 'mode', 'q_mode', 'cl', 'SDSS12', 'm_SDSS12', 'SDSS-ID', 'objID', 'Sp-ID']
    ("RAdeg", "ra"),
    ("DEdeg", "dec"),
    ("mode", "mode"),
    ("q_mode", "q_mode"),
    ("cl", "classifier"),
    ("SDSS12", "sdss12"),
    ("m_SDSS12", "m_sdss12"),
    ("SDSS-ID", "sdssid"),
    ("objID", "objid"),
    ("Sp-ID", "specid"),
    # 10: ['SpObjID', 'parentID', 'flags', 'Status', 'e_RAdeg', 'e_DEdeg', 'ObsDate', 'Q', 'umag', 'e_umag']
    ("SpObjID", "spobjid"),
    ("parentID", "parentid"),
    ("flags", "flags"),
    ("Status", "status"),
    ("e_RAdeg", "e_ra"),
    ("e_DEdeg", "e_dec"),
    ("ObsDate", "obsdate"),
    ("Q", "quality"),
    ("umag", "umag"),
    ("e_umag", "e_umag"),
    # 20: ['gmag', 'e_gmag', 'rmag', 'e_rmag', 'imag', 'e_imag', 'zmag', 'e_zmag', 'zsp', 'e_zsp']
    ("gmag", "gmag"),
    ("e_gmag", "e_gmag"),
    ("rmag", "rmag"),
    ("e_rmag", "e_rmag"),
    ("imag", "imag"),
    ("e_imag", "e_imag"),
    ("zmag", "zmag"),
    ("e_zmag", "e_zmag"),
    ("zsp", "zsp"),
    ("e_zsp", "e_zsp"),
    # 30: ['f_zsp', 'Vdisp', 'e_Vdisp', 'spInst', 'spType', 'spCl', 'subClass', 'spS/N', 'uFlags', 'us']
    ("f_zsp", "f_zsp"),
    ("Vdisp", "vdisp"),
    ("e_Vdisp", "e_vdisp"),
    ("spInst", "spinst"),
    ("spType", "sptype"),
    ("spCl", "spclass"),
    ("subClass", "spubclass"),
    ("spS/N", "spsignal"),
    ("uFlags", "u_flags"),
    ("us", "u_prob"),
    # 40: ['uc', 'uDate', "u'mag", "e_u'mag", 'upmag', 'e_upmag', 'uPmag', 'e_uPmag', 'uPrad', 'e_uPrad']
    ("uc", "u_photo"),
    ("uDate", "u_date"),
    ("u'mag", "u_prime_mag"),
    ("e_u'mag", "e_u_prime_mag"),
    ("upmag", "u_pmag"),
    ("e_upmag", "e_u_pmag"),
    ("uPmag", "u_upmag"),
    ("e_uPmag", "e_u_upmag"),
    ("uPrad", "u_prad"),
    ("e_uPrad", "e_u_prad"),
    # 50: ['uoRA', 'uoDE', 'udVrad', 'udVell', 'uPA', 'gFlags', 'gs', 'gc', 'gDate', "g'mag"]
    ("uoRA", "u_ora"),
    ("uoDE", "u_odec"),
    ("udVrad", "u_dvrad"),
    ("udVell", "u_dvell"),
    ("uPA", "u_pa"),
    ("gFlags", "g_flags"),
    ("gs", "g_prob"),
    ("gc", "g_photo"),
    ("gDate", "g_date"),
    ("g'mag", "g_prime_mag"),
    # 60: ["e_g'mag", 'gpmag', 'e_gpmag', 'gPmag', 'e_gPmag', 'gPrad', 'e_gPrad', 'goRA', 'goDE', 'gdVrad']
    ("e_g'mag", "e_g_prime_mag"),
    ("gpmag", "g_pmag"),
    ("e_gpmag", "e_g_pmag"),
    ("gPmag", "g_upmag"),
    ("e_gPmag", "e_g_upmag"),
    ("gPrad", "g_prad"),
    ("e_gPrad", "e_g_prad"),
    ("goRA", "g_ora"),
    ("goDE", "g_odec"),
    ("gdVrad", "g_dvrad"),
    # 70: ['gdVell', 'gPA', 'rFlags', 'rs', 'rc', 'rDate', "r'mag", "e_r'mag", 'rpmag', 'e_rpmag']
    ("gdVell", "g_dvell"),
    ("gPA", "g_pa"),
    ("rFlags", "r_flags"),
    ("rs", "r_prob"),
    ("rc", "r_photo"),
    ("rDate", "r_date"),
    ("r'mag", "r_prime_mag"),
    ("e_r'mag", "e_r_prime_mag"),
    ("rpmag", "r_pmag"),
    ("e_rpmag", "e_r_pmag"),
    # 80: ['rPmag', 'e_rPmag', 'rPrad', 'e_rPrad', 'roRA', 'roDE', 'rdVrad', 'rdVell', 'rPA', 'iFlags']
    ("rPmag", "r_upmag"),
    ("e_rPmag", "e_r_upmag"),
    ("rPrad", "r_prad"),
    ("e_rPrad", "e_r_prad"),
    ("roRA", "r_ora"),
    ("roDE", "r_odec"),
    ("rdVrad", "r_dvrad"),
    ("rdVell", "r_dvell"),
    ("rPA", "r_pa"),
    ("iFlags", "i_flags"),
    # 90: ['is', 'ic', 'iDate', "i'mag", "e_i'mag", 'ipmag', 'e_ipmag', 'iPmag', 'e_iPmag', 'iPrad']
    ("is", "i_prob"),
    ("ic", "i_photo"),
    ("iDate", "i_date"),
    ("i'mag", "i_prime_mag"),
    ("e_i'mag", "e_i_prime_mag"),
    ("ipmag", "i_pmag"),
    ("e_ipmag", "e_i_pmag"),
    ("iPmag", "i_upmag"),
    ("e_iPmag", "e_i_upmag"),
    ("iPrad", "i_prad"),
    # 100: ['e_iPrad', 'ioRA', 'ioDE', 'idVrad', 'idVell', 'iPA', 'zFlags', 'zs', 'zc', 'zDate']
    ("e_iPrad", "e_i_prad"),
    ("ioRA", "i_ora"),
    ("ioDE", "i_odec"),
    ("idVrad", "i_dvrad"),
    ("idVell", "i_dvell"),
    ("iPA", "i_pa"),
    ("zFlags", "z_flags"),
    ("zs", "z_prob"),
    ("zc", "z_photo"),
    ("zDate", "z_date"),
    # 110: [z'mag", "e_z'mag", 'zpmag', 'e_zpmag', 'zPmag', 'e_zPmag', 'zPrad', 'e_zPrad', 'zoRA', 'zoDE']
    ("z'mag", "z_prime_mag"),
    ("e_z'mag", "e_z_prime_mag"),
    ("zpmag", "z_pmag"),
    ("e_zpmag", "e_z_pmag"),
    ("zPmag", "z_upmag"),
    ("e_zPmag", "e_z_upmag"),
    ("zPrad", "z_prad"),
    ("e_zPrad", "e_z_prad"),
    ("zoRA", "z_ora"),
    ("zoDE", "z_odec"),
    # 120: ['zdVrad', 'zdVell', 'zPA', 'pmRA', 'e_pmRA', 'pmDE', 'e_pmDE', 'sigRA', 'sigDE', 'M']
    ("zdVrad", "z_dvrad"),
    ("zdVell", "z_dvell"),
    ("zPA", "z_pa"),
    ("pmRA", "pmra"),
    ("e_pmRA", "e_pmra"),
    ("pmDE", "pmdec"),
    ("e_pmDE", "e_pmdec"),
    ("sigRA", "sigra"),
    ("sigDE", "sigdec"),
    ("M", "m"),
    # 130: ['N', 'g(O)', 'r(E)', 'g(J)', 'r(F)', 'i(N)', 'photoz', 'e_photoz', 'nnAvgZ', 'chisq_photoz']
    ("N", "n"),
    ("g(O)", "g_o_plate"),
    ("r(E)", "r_e_plate"),
    ("g(J)", "g_j_plate"),
    ("r(F)", "r_f_plate"),
    ("i(N)", "i_n_plate"),
    ("photoz", "zph"),
    ("e_photoz", "e_zph"),
    ("nnAvgZ", "ave_zph"),
    ("chisq_photoz", "chi2"),
    # 140: ['absMagU', 'absMagG', 'absMagR', 'absMagI', 'absMagZ']
    ("absMagU", "abs_u_mag"),
    ("absMagG", "abs_g_mag"),
    ("absMagR", "abs_r_mag"),
    ("absMagI", "abs_i_mag"),
    ("absMagZ", "abs_z_mag")
)
SDSS12PHOTOZ_HEADERS = [_v[0] for _v in SDSS12PHOTOZ_HTUPLES]
SDSS12PHOTOZ_KEYS = [_v[1] for _v in SDSS12PHOTOZ_HTUPLES]
SDSS12PHOTOZ_COLUMNS = len(SDSS12PHOTOZ_HEADERS)


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: Sdss12PhotoZQ3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class Sdss12PhotoZQ3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'sdss12photoz_q3c'
    sid = db.Column(db.Integer, primary_key=True)

    # 0: ['RAdeg', 'DEdeg', 'mode', 'q_mode', 'cl', 'SDSS12', 'm_SDSS12', 'SDSS-ID', 'objID', 'Sp-ID']
    ra = db.Column(db.Float, nullable=False, index=True)
    dec = db.Column(db.Float, nullable=False, index=True)
    mode = db.Column(db.Integer, nullable=True, default=-1)
    q_mode = db.Column(db.String(DB_VARCHAR_1), nullable=False, default='')
    classifier = db.Column(db.Integer, nullable=True, default=-1)
    sdss12 = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')
    m_sdss12 = db.Column(db.String(DB_VARCHAR_1), nullable=False, default='')
    sdssid = db.Column(db.String(DB_VARCHAR_32), nullable=False, default='')
    objid = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')
    specid = db.Column(db.String(DB_VARCHAR_32), nullable=False, default='')

    # 10: ['SpObjID', 'parentID', 'flags', 'Status', 'e_RAdeg', 'e_DEdeg', 'ObsDate', 'Q', 'umag', 'e_umag']
    spobjid = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')
    parentid = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')
    flags = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')
    status = db.Column(db.Integer, nullable=True, default=-1)
    e_ra = db.Column(db.Float, nullable=False)
    e_dec = db.Column(db.Float, nullable=False)
    obsdate = db.Column(db.Float, nullable=False)
    quality = db.Column(db.Integer, nullable=True, default=-1)
    umag = db.Column(db.Float, nullable=False, index=True)
    e_umag = db.Column(db.Float, nullable=False)

    # 20: ['gmag', 'e_gmag', 'rmag', 'e_rmag', 'imag', 'e_imag', 'zmag', 'e_zmag', 'zsp', 'e_zsp']
    gmag = db.Column(db.Float, nullable=False, index=True)
    e_gmag = db.Column(db.Float, nullable=False)
    rmag = db.Column(db.Float, nullable=False, index=True)
    e_rmag = db.Column(db.Float, nullable=False)
    imag = db.Column(db.Float, nullable=False, index=True)
    e_imag = db.Column(db.Float, nullable=False)
    zmag = db.Column(db.Float, nullable=False, index=True)
    e_zmag = db.Column(db.Float, nullable=False)
    zsp = db.Column(db.Float, nullable=False, index=True)
    e_zsp = db.Column(db.Float, nullable=False)

    # 30: ['f_zsp', 'Vdisp', 'e_Vdisp', 'spInst', 'spType', 'spCl', 'subClass', 'spS/N', 'uFlags', 'us']
    f_zsp = db.Column(db.Integer, nullable=True, default=-1)
    vdisp = db.Column(db.Float, nullable=False)
    e_vdisp = db.Column(db.Float, nullable=False)
    spinst = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')
    sptype = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')
    spclass = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')
    spubclass = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')
    spsignal = db.Column(db.Float, nullable=False)
    u_flags = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')
    u_prob = db.Column(db.Integer, nullable=False)

    # 40: ['uc', 'uDate', "u'mag", "e_u'mag", 'upmag', 'e_upmag', 'uPmag', 'e_uPmag', 'uPrad', 'e_uPrad']
    u_photo = db.Column(db.Integer, nullable=False)
    u_date = db.Column(db.Float, nullable=False)
    u_prime_mag = db.Column(db.Float, nullable=False, index=True)
    e_u_prime_mag = db.Column(db.Float, nullable=False)
    u_pmag = db.Column(db.Float, nullable=False, index=True)
    e_u_pmag = db.Column(db.Float, nullable=False)
    u_upmag = db.Column(db.Float, nullable=False, index=True)
    e_u_upmag = db.Column(db.Float, nullable=False)
    u_prad = db.Column(db.Float, nullable=False)
    e_u_prad = db.Column(db.Float, nullable=False)

    # 50: ['uoRA', 'uoDE', 'udVrad', 'udVell', 'uPA', 'gFlags', 'gs', 'gc', 'gDate', "g'mag"]
    u_ora = db.Column(db.Float, nullable=False)
    u_odec = db.Column(db.Float, nullable=False)
    u_dvrad = db.Column(db.Float, nullable=False)
    u_dvell = db.Column(db.Float, nullable=False)
    u_pa = db.Column(db.Float, nullable=False)
    g_flags = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')
    g_prob = db.Column(db.Integer, nullable=False)
    g_photo = db.Column(db.Integer, nullable=False)
    g_date = db.Column(db.Float, nullable=False)
    g_prime_mag = db.Column(db.Float, nullable=False, index=True)

    # 60: ["e_g'mag", 'gpmag', 'e_gpmag', 'gPmag', 'e_gPmag', 'gPrad', 'e_gPrad', 'goRA', 'goDE', 'gdVrad']
    e_g_prime_mag = db.Column(db.Float, nullable=False, index=True)
    g_pmag = db.Column(db.Float, nullable=False)
    e_g_pmag = db.Column(db.Float, nullable=False)
    g_upmag = db.Column(db.Float, nullable=False, index=True)
    e_g_upmag = db.Column(db.Float, nullable=False)
    g_prad = db.Column(db.Float, nullable=False)
    e_g_prad = db.Column(db.Float, nullable=False)
    g_ora = db.Column(db.Float, nullable=False)
    g_odec = db.Column(db.Float, nullable=False)
    g_dvrad = db.Column(db.Float, nullable=False)

    # 70: ['gdVell', 'gPA', 'rFlags', 'rs', 'rc', 'rDate', "r'mag", "e_r'mag", 'rpmag', 'e_rpmag']
    g_dvell = db.Column(db.Float, nullable=False)
    g_pa = db.Column(db.Float, nullable=False)
    r_flags = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')
    r_prob = db.Column(db.Integer, nullable=False)
    r_photo = db.Column(db.Integer, nullable=False)
    r_date = db.Column(db.Float, nullable=False)
    r_prime_mag = db.Column(db.Float, nullable=False, index=True)
    e_r_prime_mag = db.Column(db.Float, nullable=False)
    r_pmag = db.Column(db.Float, nullable=False)
    e_r_pmag = db.Column(db.Float, nullable=False, index=True)

    # 80: ['rPmag', 'e_rPmag', 'rPrad', 'e_rPrad', 'roRA', 'roDE', 'rdVrad', 'rdVell', 'rPA', 'iFlags']
    r_upmag = db.Column(db.Float, nullable=False, index=True)
    e_r_upmag = db.Column(db.Float, nullable=False)
    r_prad = db.Column(db.Float, nullable=False)
    e_r_prad = db.Column(db.Float, nullable=False)
    r_ora = db.Column(db.Float, nullable=False)
    r_odec = db.Column(db.Float, nullable=False)
    r_dvrad = db.Column(db.Float, nullable=False)
    r_dvell = db.Column(db.Float, nullable=False)
    r_pa = db.Column(db.Float, nullable=False)
    i_flags = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')

    # 90: ['is', 'ic', 'iDate', "i'mag", "e_i'mag", 'ipmag', 'e_ipmag', 'iPmag', 'e_iPmag', 'iPrad']
    i_prob = db.Column(db.Integer, nullable=False)
    i_photo = db.Column(db.Integer, nullable=False)
    i_date = db.Column(db.Float, nullable=False)
    i_prime_mag = db.Column(db.Float, nullable=False, index=True)
    e_i_prime_mag = db.Column(db.Float, nullable=False)
    i_pmag = db.Column(db.Float, nullable=False, index=True)
    e_i_pmag = db.Column(db.Float, nullable=False)
    i_upmag = db.Column(db.Float, nullable=False, index=True)
    e_i_upmag = db.Column(db.Float, nullable=False)
    i_prad = db.Column(db.Float, nullable=False)

    # 100: ['e_iPrad', 'ioRA', 'ioDE', 'idVrad', 'idVell', 'iPA', 'zFlags', 'zs', 'zc', 'zDate']
    e_i_prad = db.Column(db.Float, nullable=False)
    i_ora = db.Column(db.Float, nullable=False)
    i_odec = db.Column(db.Float, nullable=False)
    i_dvrad = db.Column(db.Float, nullable=False)
    i_dvell = db.Column(db.Float, nullable=False)
    i_pa = db.Column(db.Float, nullable=False)
    z_flags = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')
    z_prob = db.Column(db.Integer, nullable=False)
    z_photo = db.Column(db.Integer, nullable=False)
    z_date = db.Column(db.Float, nullable=False)

    # 110: ["z'mag", "e_z'mag", 'zpmag', 'e_zpmag', 'zPmag', 'e_zPmag', 'zPrad', 'e_zPrad', 'zoRA', 'zoDE']
    z_prime_mag = db.Column(db.Float, nullable=False, index=True)
    e_z_prime_mag = db.Column(db.Float, nullable=False)
    z_pmag = db.Column(db.Float, nullable=False, index=True)
    e_z_pmag = db.Column(db.Float, nullable=False)
    z_upmag = db.Column(db.Float, nullable=False, index=True)
    e_z_upmag = db.Column(db.Float, nullable=False)
    z_prad = db.Column(db.Float, nullable=False)
    e_z_prad = db.Column(db.Float, nullable=False)
    z_ora = db.Column(db.Float, nullable=False)
    z_odec = db.Column(db.Float, nullable=False)

    # 120: ['zdVrad', 'zdVell', 'zPA', 'pmRA', 'e_pmRA', 'pmDE', 'e_pmDE', 'sigRA', 'sigDE', 'M']
    z_dvrad = db.Column(db.Float, nullable=False)
    z_dvell = db.Column(db.Float, nullable=False)
    z_pa = db.Column(db.Float, nullable=False)
    pmra = db.Column(db.Float, nullable=False)
    e_pmra = db.Column(db.Float, nullable=False)
    pmdec = db.Column(db.Float, nullable=False)
    e_pmdec = db.Column(db.Float, nullable=False)
    sigra = db.Column(db.Float, nullable=False)
    sigdec = db.Column(db.Float, nullable=False)
    m = db.Column(db.Integer, nullable=False)

    # 130: ['N', 'g(O)', 'r(E)', 'g(J)', 'r(F)', 'i(N)', 'photoz', 'e_photoz', 'nnAvgZ', 'chisq_photoz']
    n = db.Column(db.Integer, nullable=False)
    g_o_plate = db.Column(db.Float, nullable=False)
    r_e_plate = db.Column(db.Float, nullable=False)
    g_j_plate = db.Column(db.Float, nullable=False)
    r_f_plate = db.Column(db.Float, nullable=False)
    i_n_plate = db.Column(db.Float, nullable=False)
    zph = db.Column(db.Float, nullable=False, index=True)
    e_zph = db.Column(db.Float, nullable=False)
    ave_zph = db.Column(db.Float, nullable=False)
    chi2 = db.Column(db.Float, nullable=False)

    # 140: ['absMagU', 'absMagG', 'absMagR', 'absMagI', 'absMagZ']
    abs_u_mag = db.Column(db.Float, nullable=False, index=True)
    abs_g_mag = db.Column(db.Float, nullable=False, index=True)
    abs_r_mag = db.Column(db.Float, nullable=False, index=True)
    abs_i_mag = db.Column(db.Float, nullable=False, index=True)
    abs_z_mag = db.Column(db.Float, nullable=False, index=True)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'sid': self.sid,

            # 0:  ['RAdeg', 'DEdeg', 'mode', 'q_mode', 'cl', 'SDSS12', 'm_SDSS12', 'SDSS-ID', 'objID', 'Sp-ID']
            'ra': self.ra,
            'dec': self.dec,
            'mode': self.mode,
            'q_mode': self.q_mode,
            'classifier': self.classifier,
            'sdss12': self.sdss12,
            'm_sdss12': self.m_sdss12,
            'sdssid': self.sdssid,
            'objid': self.objid,
            'specid': self.specid,

            # 10: ['SpObjID', 'parentID', 'flags', 'Status', 'e_RAdeg', 'e_DEdeg', 'ObsDate', 'Q', 'umag', 'e_umag']
            'spobjid': self.spobjid,
            'parentid': self.parentid,
            'flags': self.flags,
            'status': self.status,
            'e_ra': self.e_ra,
            'e_dec': self.e_dec,
            'obsdate': self.obsdate,
            'quality': self.quality,
            'umag': self.umag,
            'e_umag': self.e_umag,

            # 20: ['gmag', 'e_gmag', 'rmag', 'e_rmag', 'imag', 'e_imag', 'zmag', 'e_zmag', 'zsp', 'e_zsp']
            'gmag': self.gmag,
            'e_gmag': self.e_gmag,
            'rmag': self.rmag,
            'e_rmag': self.e_rmag,
            'imag': self.imag,
            'e_imag': self.e_imag,
            'zmag': self.zmag,
            'e_zmag': self.e_zmag,
            'zsp': self.zsp,
            'e_zsp': self.e_zsp,

            # 30: ['f_zsp', 'Vdisp', 'e_Vdisp', 'spInst', 'spType', 'spCl', 'subClass', 'spS/N', 'uFlags', 'us']
            'f_zsp': self.f_zsp,
            'vdisp': self.vdisp,
            'e_vdisp': self.e_vdisp,
            'spinst': self.spinst,
            'sptype': self.sptype,
            'spclass': self.spclass,
            'spubclass': self.spubclass,
            'spsignal': self.spsignal,
            'u_flags': self.u_flags,
            'u_prob': self.u_prob,

            # 40: ['uc', 'uDate', "u'mag", "e_u'mag", 'upmag', 'e_upmag', 'uPmag', 'e_uPmag', 'uPrad', 'e_uPrad']
            'u_photo': self.u_photo,
            'u_date': self.u_date,
            'u_prime_mag': self.u_prime_mag,
            'e_u_prime_mag': self.e_u_prime_mag,
            'u_pmag': self.u_pmag,
            'e_u_pmag': self.e_u_pmag,
            'u_upmag': self.u_upmag,
            'e_u_upmag': self.e_u_upmag,
            'u_prad': self.u_prad,
            'e_u_prad': self.e_u_prad,

            # 50: ['uoRA', 'uoDE', 'udVrad', 'udVell', 'uPA', 'gFlags', 'gs', 'gc', 'gDate', "g'mag"]
            'u_ora': self.u_ora,
            'u_odec': self.u_odec,
            'u_dvrad': self.u_dvrad,
            'u_dvell': self.u_dvell,
            'u_pa': self.u_pa,
            'g_flags': self.g_flags,
            'g_prob': self.g_prob,
            'g_photo': self.g_photo,
            'g_date': self.g_date,
            'g_prime_mag': self.g_prime_mag,

            # 60: ["e_g'mag", 'gpmag', 'e_gpmag', 'gPmag', 'e_gPmag', 'gPrad', 'e_gPrad', 'goRA', 'goDE', 'gdVrad']
            'e_g_prime_mag': self.e_g_prime_mag,
            'g_pmag': self.g_pmag,
            'e_g_pmag': self.e_g_pmag,
            'g_upmag': self.g_upmag,
            'e_g_upmag': self.e_g_upmag,
            'g_prad': self.g_prad,
            'e_g_prad': self.e_g_prad,
            'g_ora': self.g_ora,
            'g_odec': self.g_odec,
            'g_dvrad': self.g_dvrad,

            # 70: ['gdVell', 'gPA', 'rFlags', 'rs', 'rc', 'rDate', "r'mag", "e_r'mag", 'rpmag', 'e_rpmag']
            'g_dvell': self.g_dvell,
            'g_pa': self.g_pa,
            'r_flags': self.r_flags,
            'r_prob': self.r_prob,
            'r_photo': self.r_photo,
            'r_date': self.r_date,
            'r_prime_mag': self.r_prime_mag,
            'e_r_prime_mag': self.e_r_prime_mag,
            'r_pmag': self.r_pmag,
            'e_r_pmag': self.e_r_pmag,

            # 80: ['rPmag', 'e_rPmag', 'rPrad', 'e_rPrad', 'roRA', 'roDE', 'rdVrad', 'rdVell', 'rPA', 'iFlags']
            'r_upmag': self.r_upmag,
            'e_r_upmag': self.e_r_upmag,
            'r_prad': self.r_prad,
            'e_r_prad': self.e_r_prad,
            'r_ora': self.r_ora,
            'r_odec': self.r_odec,
            'r_dvrad': self.r_dvrad,
            'r_dvell': self.r_dvell,
            'r_pa': self.r_pa,
            'i_flags': self.i_flags,

            # 90: ['is', 'ic', 'iDate', "i'mag", "e_i'mag", 'ipmag', 'e_ipmag', 'iPmag', 'e_iPmag', 'iPrad']
            'i_prob': self.i_prob,
            'i_photo': self.i_photo,
            'i_date': self.i_date,
            'i_prime_mag': self.i_prime_mag,
            'e_i_prime_mag': self.e_i_prime_mag,
            'i_pmag': self.i_pmag,
            'e_i_pmag': self.e_i_pmag,
            'i_upmag': self.i_upmag,
            'e_i_upmag': self.e_i_upmag,
            'i_prad': self.i_prad,

            # 100: ['e_iPrad', 'ioRA', 'ioDE', 'idVrad', 'idVell', 'iPA', 'zFlags', 'zs', 'zc', 'zDate']
            'e_i_prad': self.e_i_prad,
            'i_ora': self.i_ora,
            'i_odec': self.i_odec,
            'i_dvrad': self.i_dvrad,
            'i_dvell': self.i_dvell,
            'i_pa': self.i_pa,
            'z_flags': self.z_flags,
            'z_prob': self.z_prob,
            'z_photo': self.z_photo,
            'z_date': self.z_date,

            # 110: ["z'mag", "e_z'mag", 'zpmag', 'e_zpmag', 'zPmag', 'e_zPmag', 'zPrad', 'e_zPrad', 'zoRA', 'zoDE']
            'z_prime_mag': self.z_prime_mag,
            'e_z_prime_mag': self.e_z_prime_mag,
            'z_pmag': self.z_pmag,
            'e_z_pmag': self.e_z_pmag,
            'z_upmag': self.z_upmag,
            'e_z_upmag': self.e_z_upmag,
            'z_prad': self.z_prad,
            'e_z_prad': self.e_z_prad,
            'z_ora': self.z_ora,
            'z_odec': self.z_odec,

            # 120: ['zdVrad', 'zdVell', 'zPA', 'pmRA', 'e_pmRA', 'pmDE', 'e_pmDE', 'sigRA', 'sigDE', 'M']
            'z_dvrad': self.z_dvrad,
            'z_dvell': self.z_dvell,
            'z_pa': self.z_pa,
            'pmra': self.pmra,
            'e_pmra': self.e_pmra,
            'pmdec': self.pmdec,
            'e_pmdec': self.e_pmdec,
            'sigra': self.sigra,
            'sigdec': self.sigdec,
            'm': self.m,

            # 130: ['N', 'g(O)', 'r(E)', 'g(J)', 'r(F)', 'i(N)', 'photoz', 'e_photoz', 'nnAvgZ', 'chisq_photoz']
            'n': self.n,
            'g_o_plate': self.g_o_plate,
            'r_e_plate': self.r_e_plate,
            'g_j_plate': self.g_j_plate,
            'r_f_plate': self.r_f_plate,
            'i_n_plate': self.i_n_plate,
            'zph': self.zph,
            'e_zph': self.e_zph,
            'ave_zph': self.ave_zph,
            'chi2': self.chi2,

            # 140: ['absMagU', 'absMagG', 'absMagR', 'absMagI', 'absMagZ']
            'abs_u_mag': self.abs_u_mag,
            'abs_g_mag': self.abs_g_mag,
            'abs_r_mag': self.abs_r_mag,
            'abs_i_mag': self.abs_i_mag,
            'abs_z_mag': self.abs_z_mag
        }

    # +
    # (overload) method: __str__()
    # -
    def __str__(self):
        return self.sid

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(m_records):
        return [_a.serialized() for _a in m_records]
