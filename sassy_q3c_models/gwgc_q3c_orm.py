#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                      Table "public.gwgc_q3c"
  Column   |          Type          | Collation | Nullable |                Default                
-----------+------------------------+-----------+----------+---------------------------------------
 gid       | integer                |           | not null | nextval('gwgc_q3c_gid_seq'::regclass)
 pgc       | integer                |           |          | 
 name      | character varying(128) |           | not null | 
 rah       | double precision       |           |          | 
 ra        | double precision       |           |          | 
 dec       | double precision       |           |          | 
 tt        | double precision       |           |          | 
 b_app     | double precision       |           |          | 
 a         | double precision       |           |          | 
 e_a       | double precision       |           |          | 
 b         | double precision       |           |          | 
 e_b       | double precision       |           |          | 
 b_div_a   | double precision       |           |          | 
 e_b_div_a | double precision       |           |          | 
 pa        | double precision       |           |          | 
 b_abs     | double precision       |           |          | 
 dist      | double precision       |           |          | 
 e_dist    | double precision       |           |          | 
 e_b_app   | double precision       |           |          | 
 e_b_abs   | double precision       |           |          | 
Indexes:
    "gwgc_q3c_pkey" PRIMARY KEY, btree (gid)
    "gwgc_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(ra, "dec"))
"""


# +
# constant(s)
# -
GWGC_DAT_URL = 'https://cdsarc.u-strasbg.fr/ftp/VII/267/gwgc.dat.gz'
GWGC_PAG_URL = 'None'
GWGC_PDF_URL = 'https://arXiv.org/pdf/1103.0695.pdf'
GWGC_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
GWGC_SORT_VALUE = ['gid', 'pgc', 'name', 'ra', 'dec', 'tt', 'b_app', 'a', 'b', 'b_div_a', 'pa', 'b_abs', 'dist']
GWGC_HEADERS = ('gid', 'pgc', 'name', 'ra', 'dec', 'tt', 'b_app', 'a', 'e_a',
                'b', 'e_b', 'b_div_a', 'e_b_div_a', 'pa', 'b_abs', 'dist', 'e_dist', 'e_b_app', 'e_b_abs')


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: GwgcQ3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class GwgcQ3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'gwgc_q3c'
    gid = db.Column(db.Integer, primary_key=True)
    pgc = db.Column(db.Integer, nullable=True, default=None)
    name = db.Column(db.String(DB_VARCHAR_128), nullable=False, default='')
    rah = db.Column(db.Float, nullable=True)
    ra = db.Column(db.Float, nullable=False, index=True)
    dec = db.Column(db.Float, nullable=False, index=True)
    tt = db.Column(db.Float, nullable=True, default=None)
    b_app = db.Column(db.Float, nullable=True, default=None, index=True)
    a = db.Column(db.Float, nullable=True, default=None)
    e_a = db.Column(db.Float, nullable=True, default=None)
    b = db.Column(db.Float, nullable=True, default=None)
    e_b = db.Column(db.Float, nullable=True, default=None)
    b_div_a = db.Column(db.Float, nullable=True, default=None)
    e_b_div_a = db.Column(db.Float, nullable=True, default=None)
    pa = db.Column(db.Float, nullable=True, default=None)
    b_abs = db.Column(db.Float, nullable=True, default=None, index=True)
    dist = db.Column(db.Float, nullable=True, default=None)
    e_dist = db.Column(db.Float, nullable=True, default=None)
    e_b_app = db.Column(db.Float, nullable=True, default=None)
    e_b_abs = db.Column(db.Float, nullable=True, default=None)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'gid': self.gid,
            'pgc': self.pgc,
            'name': self.name,
            'rah': self.rah,
            'ra': self.ra,
            'dec': self.dec,
            'tt': self.tt,
            'b_app': self.b_app,
            'a': self.a,
            'e_a': self.e_a,
            'b': self.b,
            'e_b': self.e_b,
            'b_div_a': self.b_div_a,
            'e_b_div_a': self.e_b_div_a,
            'pa': self.pa,
            'b_abs': self.b_abs,
            'dist': self.dist,
            'e_dist': self.e_dist,
            'e_b_app': self.e_b_app,
            'e_b_abs': self.e_b_abs
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

