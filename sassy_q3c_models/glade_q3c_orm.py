#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                     Table "public.glade_q3c"
  Column   |          Type          | Collation | Nullable |                Default                
-----------+------------------------+-----------+----------+---------------------------------------
 id        | integer                |           | not null | nextval('glade_q3c_id_seq'::regclass)
 pgc       | integer                |           |          | 
 gwgc      | character varying(128) |           |          | 
 hyperleda | character varying(128) |           |          | 
 twomass   | character varying(128) |           |          | 
 sdss      | character varying(128) |           |          | 
 flag1     | character varying(1)   |           |          | 
 ra        | double precision       |           |          | 
 dec       | double precision       |           |          | 
 dist      | double precision       |           |          | 
 disterr   | double precision       |           |          | 
 z         | double precision       |           |          | 
 b         | double precision       |           |          | 
 b_err     | double precision       |           |          | 
 b_abs     | double precision       |           |          | 
 j         | double precision       |           |          | 
 j_err     | double precision       |           |          | 
 h         | double precision       |           |          | 
 h_err     | double precision       |           |          | 
 k         | double precision       |           |          | 
 k_err     | double precision       |           |          | 
 flag2     | integer                |           |          | 
 flag3     | integer                |           |          | 
Indexes:
    "glade_q3c_pkey" PRIMARY KEY, btree (id)
    "glade_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(ra, "dec")) CLUSTER
"""


# +
# constant(s)
# -
GLADE_DAT_URL = 'https://glade.elte.hu/GLADE_2.4.txt'
GLADE_PAG_URL = 'https://glade.elte.hu'
GLADE_PDF_URL = 'https://arxiv.org/pdf/1804.05709.pdf'
GLADE_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
GLADE_SORT_VALUE = ['gid', 'pgc', 'gwgc', 'hyperleda', 'twomass', 'sdss', 'ra', 'dec', 'dist', 'z', 'b', 'b_abs', 'j',
                    'h', 'k']
GLADE_HEADERS = ('gid', 'pgc', 'gwgc', 'hyperleda', 'twomass', 'sdss', 'flag1',
                 'ra', 'dec', 'dist', 'disterr', 'z', 'b', 'b_err', 'b_abs', 'j',
                 'j_err', 'h', 'h_err', 'k', 'k_err', 'flag2', 'flag3')


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: GladeQ3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class GladeQ3cRecord(db.Model):

    # +
    # define table
    # -

    __tablename__ = 'glade_q3c'
    gid = db.Column(db.Integer, primary_key=True)
    pgc = db.Column(db.Integer)
    gwgc = db.Column(db.String(DB_VARCHAR_128))
    hyperleda = db.Column(db.String(DB_VARCHAR_128))
    twomass = db.Column(db.String(DB_VARCHAR_128))
    sdss = db.Column(db.String(DB_VARCHAR_128))
    flag1 = db.Column(db.String(DB_VARCHAR_1))
    ra = db.Column(db.Float)
    dec = db.Column(db.Float)
    dist = db.Column(db.Float)
    disterr = db.Column(db.Float)
    z = db.Column(db.Float)
    b = db.Column(db.Float)
    b_err = db.Column(db.Float)
    b_abs = db.Column(db.Float)
    j = db.Column(db.Float)
    j_err = db.Column(db.Float)
    h = db.Column(db.Float)
    h_err = db.Column(db.Float)
    k = db.Column(db.Float)
    k_err = db.Column(db.Float)
    flag2 = db.Column(db.Integer)
    flag3 = db.Column(db.Integer)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'gid': self.gid,
            'pgc': self.pgc,
            'gwgc': self.gwgc,
            'hyperleda': self.hyperleda,
            'twomass': self.twomass,
            'sdss': self.sdss,
            'flag1': self.flag1,
            'ra': self.ra,
            'dec': self.dec,
            'dist': self.dist,
            'disterr': self.disterr,
            'z': self.z,
            'b': self.b,
            'b_err': self.b_err,
            'b_abs': self.b_abs,
            'j': self.j,
            'j_err': self.j_err,
            'h': self.h,
            'h_err': self.h_err,
            'k': self.k,
            'k_err': self.k_err,
            'flag2': self.flag2,
            'flag3': self.flag3
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
