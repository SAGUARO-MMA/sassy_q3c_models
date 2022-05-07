#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """ 
                                     Table "public.glade_plus_q3c"
  Column   |         Type          | Collation | Nullable |                   Default                   
-----------+-----------------------+-----------+----------+---------------------------------------------
 gid       | integer               |           | not null | nextval('glade_plus_q3c_gid_seq'::regclass)
 gn        | integer               |           |          | 
 pgc       | integer               |           |          | 
 gwgc      | character varying(64) |           |          | 
 hyperleda | character varying(64) |           |          | 
 twomass   | character varying(64) |           |          | 
 wise      | character varying(64) |           |          | 
 sdss      | character varying(64) |           |          | 
 o_flag    | character varying(1)  |           |          | 
 ra        | double precision      |           |          | 
 dec       | double precision      |           |          | 
 b         | double precision      |           |          | 
 b_err     | double precision      |           |          | 
 b_flag    | integer               |           |          | 
 b_abs     | double precision      |           |          | 
 j         | double precision      |           |          | 
 j_err     | double precision      |           |          | 
 h         | double precision      |           |          | 
 h_err     | double precision      |           |          | 
 k         | double precision      |           |          | 
 k_err     | double precision      |           |          | 
 w1        | double precision      |           |          | 
 w1_err    | double precision      |           |          | 
 w2        | double precision      |           |          | 
 w2_err    | double precision      |           |          | 
 w1_flag   | integer               |           |          | 
 b_j       | double precision      |           |          | 
 b_j_err   | double precision      |           |          | 
 z_helio   | double precision      |           |          | 
 z_cmb     | double precision      |           |          | 
 z_flag    | integer               |           |          | 
 v_err     | double precision      |           |          | 
 z_err     | double precision      |           |          | 
 d_l       | double precision      |           |          | 
 d_l_err   | double precision      |           |          | 
 dist_flag | integer               |           |          | 
 mstar     | double precision      |           |          | 
 mstar_err | double precision      |           |          | 
 mrate     | double precision      |           |          | 
 mrate_err | double precision      |           |          | 
Indexes:
    "glade_plus_q3c_pkey" PRIMARY KEY, btree (gid)
    "glade_plus_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(ra, "dec")) CLUSTER
"""


# +
# constant(s)
# -
GLADE_PLUS_COLUMNS = 39
GLADE_PLUS_DAT_URL = 'http://elysium.elte.hu/~dalyag/GLADE+.txt'
GLADE_PLUS_PDF_URL = 'https://arXiv.org/pdf/2110.06184.pdf'
GLADE_PLUS_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
GLADE_PLUS_SORT_VALUE = ['gn', 'name', 'ra', 'dec', 'b', 'b_abs', 'j', 'h', 'k', 'w1', 'w2', 'b_j', 'z_helio', 'z_cmb',
                         'd_l']
GLADE_PLUS_HEADERS = ('gid', 'gn', 'pgc', 'gwgc', 'hyperleda', 'twomass', 'wise', 'sdss', 'o_flag',
                      'ra', 'dec', 'b', 'b_err', 'b_flag', 'b_abs', 'j', 'j_err', 'h', 'h_err', 'k',
                      'k_err', 'w1', 'w1_err', 'w2', 'w2_err', 'w1_flag', 'b_j', 'b_j_err', 'z_helio',
                      'z_cmb', 'z_flag', 'v_err', 'z_err', 'd_l', 'd_l_err', 'dist_flag', 'mstar',
                      'mstar_err', 'mrate', 'mrate_err')


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: GladePlusQ3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class GladePlusQ3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'glade_plus_q3c'
    gid = db.Column(db.Integer, primary_key=True)
    gn = db.Column(db.Integer)
    pgc = db.Column(db.Integer)
    gwgc = db.Column(db.String(DB_VARCHAR_64))
    hyperleda = db.Column(db.String(DB_VARCHAR_64))
    twomass = db.Column(db.String(DB_VARCHAR_64))
    wise = db.Column(db.String(DB_VARCHAR_64))
    sdss = db.Column(db.String(DB_VARCHAR_64))
    o_flag = db.Column(db.String(DB_VARCHAR_1))
    ra = db.Column(db.Float)
    dec = db.Column(db.Float)
    b = db.Column(db.Float)
    b_err = db.Column(db.Float)
    b_flag = db.Column(db.Integer)
    b_abs = db.Column(db.Float)
    j = db.Column(db.Float)
    j_err = db.Column(db.Float)
    h = db.Column(db.Float)
    h_err = db.Column(db.Float)
    k = db.Column(db.Float)
    k_err = db.Column(db.Float)
    w1 = db.Column(db.Float)
    w1_err = db.Column(db.Float)
    w2 = db.Column(db.Float)
    w2_err = db.Column(db.Float)
    w1_flag = db.Column(db.Integer)
    b_j = db.Column(db.Float)
    b_j_err = db.Column(db.Float)
    z_helio = db.Column(db.Float)
    z_cmb = db.Column(db.Float)
    z_flag = db.Column(db.Integer)
    v_err = db.Column(db.Float)
    z_err = db.Column(db.Float)
    d_l = db.Column(db.Float)
    d_l_err = db.Column(db.Float)
    dist_flag = db.Column(db.Integer)
    mstar = db.Column(db.Float)
    mstar_err = db.Column(db.Float)
    mrate = db.Column(db.Float)
    mrate_err = db.Column(db.Float)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'gid': self.gid,
            'gn': self.gn,
            'pgc': self.pgc,
            'gwgc': self.gwgc,
            'hyperleda': self.hyperleda,
            'twomass': self.twomass,
            'wise': self.wise,
            'sdss': self.sdss,
            'o_flag': self.o_flag,
            'ra': self.ra,
            'dec': self.dec,
            'b': self.b,
            'b_err': self.b_err,
            'b_flag': self.b_flag,
            'b_abs': self.b_abs,
            'j': self.j,
            'j_err': self.j_err,
            'h': self.h,
            'h_err': self.h_err,
            'k': self.k,
            'k_err': self.k_err,
            'w1': self.w1,
            'w1_err': self.w1_err,
            'w2': self.w2,
            'w2_err': self.w2_err,
            'w1_flag': self.w1_flag,
            'b_j': self.b_j,
            'b_j_err': self.b_j_err,
            'z_helio': self.z_helio,
            'z_cmb': self.z_cmb,
            'z_flag': self.z_flag,
            'v_err': self.v_err,
            'z_err': self.z_err,
            'd_l': self.d_l,
            'd_l_err': self.d_l_err,
            'dist_flag': self.dist_flag,
            'mstar': self.mstar,
            'mstar_err': self.mstar_err,
            'mrate': self.mrate,
            'mrate_err': self.mrate_err
        }

    # +
    # (overload) method: __str__()
    # -
    def __str__(self):
        return self.gid

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(m_records):
        return [_a.serialized() for _a in m_records]
