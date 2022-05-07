#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                       Table "public.hecate_q3c"
    Column    |         Type          | Collation | Nullable |                 Default                 
--------------+-----------------------+-----------+----------+-----------------------------------------
 hid          | integer               |           | not null | nextval('hecate_q3c_hid_seq'::regclass)
 pgc          | integer               |           |          | 
 objname      | character varying(64) |           |          | 
 id_ned       | character varying(64) |           |          | 
 id_nedd      | character varying(64) |           |          | 
 id_iras      | character varying(64) |           |          | 
 id_2mass     | character varying(64) |           |          | 
 sdss_photid  | character varying(64) |           |          | 
 sdss_specid  | character varying(64) |           |          | 
 ra           | double precision      |           |          | 
 dec          | double precision      |           |          | 
 f_astrom     | integer               |           |          | 
 r1           | double precision      |           |          | 
 r2           | double precision      |           |          | 
 pa           | double precision      |           |          | 
 rsource      | character varying(1)  |           |          | 
 rflag        | integer               |           |          | 
 t            | double precision      |           |          | 
 e_t          | double precision      |           |          | 
 incl         | double precision      |           |          | 
 v            | double precision      |           |          | 
 e_v          | double precision      |           |          | 
 v_vir        | double precision      |           |          | 
 e_v_vir      | double precision      |           |          | 
 ndist        | integer               |           |          | 
 edist        | boolean               |           |          | 
 d            | double precision      |           |          | 
 e_d          | double precision      |           |          | 
 d_lo68       | double precision      |           |          | 
 d_hi68       | double precision      |           |          | 
 d_lo95       | double precision      |           |          | 
 d_hi95       | double precision      |           |          | 
 dmethod      | character varying(2)  |           |          | 
 ut           | double precision      |           |          | 
 bt           | double precision      |           |          | 
 vt           | double precision      |           |          | 
 it           | double precision      |           |          | 
 e_ut         | double precision      |           |          | 
 e_bt         | double precision      |           |          | 
 e_vt         | double precision      |           |          | 
 e_it         | double precision      |           |          | 
 ag           | double precision      |           |          | 
 ai           | double precision      |           |          | 
 s12          | double precision      |           |          | 
 s25          | double precision      |           |          | 
 s60          | double precision      |           |          | 
 s100         | double precision      |           |          | 
 q12          | double precision      |           |          | 
 q25          | double precision      |           |          | 
 q60          | double precision      |           |          | 
 q100         | double precision      |           |          | 
 wf1          | double precision      |           |          | 
 wf2          | double precision      |           |          | 
 wf3          | double precision      |           |          | 
 wf4          | double precision      |           |          | 
 e_wf1        | double precision      |           |          | 
 e_wf2        | double precision      |           |          | 
 e_wf3        | double precision      |           |          | 
 e_wf4        | double precision      |           |          | 
 wfpoint      | boolean               |           |          | 
 wftreat      | boolean               |           |          | 
 j            | double precision      |           |          | 
 h            | double precision      |           |          | 
 k            | double precision      |           |          | 
 e_j          | double precision      |           |          | 
 e_h          | double precision      |           |          | 
 e_k          | double precision      |           |          | 
 flag_2mass   | integer               |           |          | 
 u            | double precision      |           |          | 
 g            | double precision      |           |          | 
 r            | double precision      |           |          | 
 i            | double precision      |           |          | 
 z            | double precision      |           |          | 
 e_u          | double precision      |           |          | 
 e_g          | double precision      |           |          | 
 e_r          | double precision      |           |          | 
 e_i          | double precision      |           |          | 
 e_z          | double precision      |           |          | 
 logl_tir     | double precision      |           |          | 
 logl_fir     | double precision      |           |          | 
 logl_60u     | double precision      |           |          | 
 logl_12u     | double precision      |           |          | 
 logl_22u     | double precision      |           |          | 
 logl_k       | double precision      |           |          | 
 ml_ratio     | double precision      |           |          | 
 logsfr_tir   | double precision      |           |          | 
 logsfr_fir   | double precision      |           |          | 
 logsfr_60u   | double precision      |           |          | 
 logsfr_12u   | double precision      |           |          | 
 logsfr_22u   | double precision      |           |          | 
 logsfr_hec   | double precision      |           |          | 
 sfr_hec_flag | character varying(2)  |           |          | 
 logm_hec     | double precision      |           |          | 
 logsfr_gsw   | double precision      |           |          | 
 logm_gsw     | double precision      |           |          | 
 min_snr      | double precision      |           |          | 
 metal        | double precision      |           |          | 
 flag_metal   | integer               |           |          | 
 class_sp     | integer               |           |          | 
 agn_s17      | character varying(1)  |           |          | 
 agn_hec      | character varying(1)  |           |          | 
Indexes:
    "hecate_q3c_pkey" PRIMARY KEY, btree (hid)
    "hecate_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(ra, "dec")) CLUSTER
"""


# +
# constant(s)
# -
HECATE_COLUMNS = 100
HECATE_DAT_URL = 'http://hecate.ia.forth.gr/HECATE_v1.1.csv'
HECATE_PDF_URL = 'https://arXiv.org/pdf/2106.12101.pdf'
HECATE_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
HECATE_SORT_VALUE = ['hid', 'name', 'ra', 'dec', 'd', 'ut', 'bt', 'vt', 'it', 'j', 'h', 'k', 'u', 'g', 'r', 'i', 'z']
HECATE_HEADERS = ('hid', 'pgc', 'objname', 'id_ned', 'id_nedd', 'id_iras', 'id_2mass', 'sdss_photid', 'sdss_specid',
                  'ra', 'dec', 'f_astrom', 'r1', 'r2', 'pa', 'rsource', 'rflag', 't', 'e_t', 'incl', 'v', 'e_v',
                  'v_vir', 'e_v_vir', 'ndist', 'edist', 'd', 'e_d', 'd_lo68', 'd_hi68', 'd_lo95', 'd_hi95', 'dmethod',
                  'ut', 'bt', 'vt', 'it', 'e_ut', 'e_bt', 'e_vt', 'e_it', 'ag', 'ai', 's12', 's25', 's60', 's100',
                  'q12', 'q25', 'q60', 'q100', 'wf1', 'wf2', 'wf3', 'wf4', 'e_wf1', 'e_wf2', 'e_wf3', 'e_wf4',
                  'wfpoint', 'wftreat', 'j', 'h', 'k', 'e_j', 'e_h', 'e_k', 'flag_2mass', 'u', 'g', 'r', 'i', 'z',
                  'e_u', 'e_g', 'e_r', 'e_i', 'e_z', 'logl_tir', 'logl_fir', 'logl_60u', 'logl_12u', 'logl_22u',
                  'logl_k', 'ml_ratio', 'logsfr_tir', 'logsfr_fir', 'logsfr_60u', 'logsfr_12u', 'logsfr_22u',
                  'logsfr_hec', 'sfr_hec_flag', 'logm_hec', 'logsfr_gsw', 'logm_gsw', 'min_snr', 'metal',
                  'flag_metal', 'class_sp', 'agn_s17', 'agn_hec')


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: HecateQ3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class HecateQ3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'hecate_q3c'
    hid = db.Column(db.Integer, primary_key=True)
    pgc = db.Column(db.Integer)
    objname = db.Column(db.String(DB_VARCHAR_64))
    id_ned = db.Column(db.String(DB_VARCHAR_64))
    id_nedd = db.Column(db.String(DB_VARCHAR_64))
    id_iras = db.Column(db.String(DB_VARCHAR_64))
    id_2mass = db.Column(db.String(DB_VARCHAR_64))
    sdss_photid = db.Column(db.String(DB_VARCHAR_64))
    sdss_specid = db.Column(db.String(DB_VARCHAR_64))
    ra = db.Column(db.Float)
    dec = db.Column(db.Float)
    f_astrom = db.Column(db.Integer)
    r1 = db.Column(db.Float)
    r2 = db.Column(db.Float)
    pa = db.Column(db.Float)
    rsource = db.Column(db.String(DB_VARCHAR_1))
    rflag = db.Column(db.Integer)
    t = db.Column(db.Float)
    e_t = db.Column(db.Float)
    incl = db.Column(db.Float)
    v = db.Column(db.Float)
    e_v = db.Column(db.Float)
    v_vir = db.Column(db.Float)
    e_v_vir = db.Column(db.Float)
    ndist = db.Column(db.Integer)
    edist = db.Column(db.Boolean)
    d = db.Column(db.Float)
    e_d = db.Column(db.Float)
    d_lo68 = db.Column(db.Float)
    d_hi68 = db.Column(db.Float)
    d_lo95 = db.Column(db.Float)
    d_hi95 = db.Column(db.Float)
    dmethod = db.Column(db.String(DB_VARCHAR_2))
    ut = db.Column(db.Float)
    bt = db.Column(db.Float)
    vt = db.Column(db.Float)
    it = db.Column(db.Float)
    e_ut = db.Column(db.Float)
    e_bt = db.Column(db.Float)
    e_vt = db.Column(db.Float)
    e_it = db.Column(db.Float)
    ag = db.Column(db.Float)
    ai = db.Column(db.Float)
    s12 = db.Column(db.Float)
    s25 = db.Column(db.Float)
    s60 = db.Column(db.Float)
    s100 = db.Column(db.Float)
    q12 = db.Column(db.Float)
    q25 = db.Column(db.Float)
    q60 = db.Column(db.Float)
    q100 = db.Column(db.Float)
    wf1 = db.Column(db.Float)
    wf2 = db.Column(db.Float)
    wf3 = db.Column(db.Float)
    wf4 = db.Column(db.Float)
    e_wf1 = db.Column(db.Float)
    e_wf2 = db.Column(db.Float)
    e_wf3 = db.Column(db.Float)
    e_wf4 = db.Column(db.Float)
    wfpoint = db.Column(db.Boolean)
    wftreat = db.Column(db.Boolean)
    j = db.Column(db.Float)
    h = db.Column(db.Float)
    k = db.Column(db.Float)
    e_j = db.Column(db.Float)
    e_h = db.Column(db.Float)
    e_k = db.Column(db.Float)
    flag_2mass = db.Column(db.Integer)
    u = db.Column(db.Float)
    g = db.Column(db.Float)
    r = db.Column(db.Float)
    i = db.Column(db.Float)
    z = db.Column(db.Float)
    e_u = db.Column(db.Float)
    e_g = db.Column(db.Float)
    e_r = db.Column(db.Float)
    e_i = db.Column(db.Float)
    e_z = db.Column(db.Float)
    logl_tir = db.Column(db.Float)
    logl_fir = db.Column(db.Float)
    logl_60u = db.Column(db.Float)
    logl_12u = db.Column(db.Float)
    logl_22u = db.Column(db.Float)
    logl_k = db.Column(db.Float)
    ml_ratio = db.Column(db.Float)
    logsfr_tir = db.Column(db.Float)
    logsfr_fir = db.Column(db.Float)
    logsfr_60u = db.Column(db.Float)
    logsfr_12u = db.Column(db.Float)
    logsfr_22u = db.Column(db.Float)
    logsfr_hec = db.Column(db.Float)
    sfr_hec_flag = db.Column(db.String(2))
    logm_hec = db.Column(db.Float)
    logsfr_gsw = db.Column(db.Float)
    logm_gsw = db.Column(db.Float)
    min_snr = db.Column(db.Float)
    metal = db.Column(db.Float)
    flag_metal = db.Column(db.Integer)
    class_sp = db.Column(db.Integer)
    agn_s17 = db.Column(db.String(1))
    agn_hec = db.Column(db.String(1))

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'hid': self.hid,
            'pgc': self.pgc,
            'objname': self.objname,
            'id_ned': self.id_ned,
            'id_nedd': self.id_nedd,
            'id_iras': self.id_iras,
            'id_2mass': self.id_2mass,
            'sdss_photid': self.sdss_photid,
            'sdss_specid': self.sdss_specid,
            'ra': self.ra,
            'dec': self.dec,
            'f_astrom': self.f_astrom,
            'r1': self.r1,
            'r2': self.r2,
            'pa': self.pa,
            'rsource': self.rsource,
            'rflag': self.rflag,
            't': self.t,
            'e_t': self.e_t,
            'incl': self.incl,
            'v': self.v,
            'e_v': self.e_v,
            'v_vir': self.v_vir,
            'e_v_vir': self.e_v_vir,
            'ndist': self.ndist,
            'edist': self.edist,
            'd': self.d,
            'e_d': self.e_d,
            'd_lo68': self.d_lo68,
            'd_hi68': self.d_hi68,
            'd_lo95': self.d_lo95,
            'd_hi95': self.d_hi95,
            'dmethod': self.dmethod,
            'ut': self.ut,
            'bt': self.bt,
            'vt': self.vt,
            'it': self.it,
            'e_ut': self.e_ut,
            'e_bt': self.e_bt,
            'e_vt': self.e_vt,
            'e_it': self.e_it,
            'ag': self.ag,
            'ai': self.ai,
            's12': self.s12,
            's25': self.s25,
            's60': self.s60,
            's100': self.s100,
            'q12': self.q12,
            'q25': self.q25,
            'q60': self.q60,
            'q100': self.q100,
            'wf1': self.wf1,
            'wf2': self.wf2,
            'wf3': self.wf3,
            'wf4': self.wf4,
            'e_wf1': self.e_wf1,
            'e_wf2': self.e_wf2,
            'e_wf3': self.e_wf3,
            'e_wf4': self.e_wf4,
            'wfpoint': self.wfpoint,
            'wftreat': self.wftreat,
            'j': self.j,
            'h': self.h,
            'k': self.k,
            'e_j': self.e_j,
            'e_h': self.e_h,
            'e_k': self.e_k,
            'flag_2mass': self.flag_2mass,
            'u': self.u,
            'g': self.g,
            'r': self.r,
            'i': self.i,
            'z': self.z,
            'e_u': self.e_u,
            'e_g': self.e_g,
            'e_r': self.e_r,
            'e_i': self.e_i,
            'e_z': self.e_z,
            'logl_tir': self.logl_tir,
            'logl_fir': self.logl_fir,
            'logl_60u': self.logl_60u,
            'logl_12u': self.logl_12u,
            'logl_22u': self.logl_22u,
            'logl_k': self.logl_k,
            'ml_ratio': self.ml_ratio,
            'logsfr_tir': self.logsfr_tir,
            'logsfr_fir': self.logsfr_fir,
            'logsfr_60u': self.logsfr_60u,
            'logsfr_12u': self.logsfr_12u,
            'logsfr_22u': self.logsfr_22u,
            'logsfr_hec': self.logsfr_hec,
            'sfr_hec_flag': self.sfr_hec_flag,
            'logm_hec': self.logm_hec,
            'logsfr_gsw': self.logsfr_gsw,
            'logm_gsw': self.logm_gsw,
            'min_snr': self.min_snr,
            'metal': self.metal,
            'flag_metal': self.flag_metal,
            'class_sp': self.class_sp,
            'agn_s17': self.agn_s17,
            'agn_hec': self.agn_hec
        }

    # +
    # (overload) method: __str__()
    # -
    def __str__(self):
        return self.hid

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(m_records):
        return [_a.serialized() for _a in m_records]
