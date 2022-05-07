#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                    Table "public.milliquas_q3c"
 Column  |         Type          | Collation | Nullable |                  Default                   
---------+-----------------------+-----------+----------+--------------------------------------------
 mid     | integer               |           | not null | nextval('milliquas_q3c_mid_seq'::regclass)
 ra      | double precision      |           |          | 
 dec     | double precision      |           |          | 
 name    | character varying(32) |           |          | 
 objtype | character varying(8)  |           |          | 
 rmag    | double precision      |           |          | 
 bmag    | double precision      |           |          | 
 comment | character varying(8)  |           |          | 
 rpsf    | character varying(1)  |           |          | 
 bpsf    | character varying(1)  |           |          | 
 z       | double precision      |           |          | 
 namecit | character varying(8)  |           |          | 
 zcit    | character varying(8)  |           |          | 
 qpct    | integer               |           |          | 
 xname   | character varying(32) |           |          | 
 rname   | character varying(32) |           |          | 
 lobe1   | character varying(32) |           |          | 
 lobe2   | character varying(32) |           |          | 
Indexes:
    "milliquas_q3c_pkey" PRIMARY KEY, btree (mid)
    "milliquas_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(ra, "dec")) CLUSTER
"""


# +
# constant(s)
# -
MILLIQUAS_COLUMNS = 17
MILLIQUAS_DAT_URL = 'https://cdsarc.cds.unistra.fr/viz-bin/nph-Cat/tar.gz?VII/290'
MILLIQUAS_PDF_URL = 'https://arxiv.org/pdf/2105.12985.pdf'
MILLIQUAS_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
MILLIQUAS_SORT_VALUE = ['mid', 'ra', 'dec', 'name', 'objtype', 'rmag', 'bmag', 'z', 'qpct']
MILLIQUAS_HEADERS = ('mid', 'ra', 'dec', 'name', 'objtype', 'rmag', 'bmag', 'comment', 'rpsf', 'bpsf', 'z', 'namecit',
                     'zcit', 'qpct', 'xname', 'rname', 'lobe1', 'lobe2')


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: MilliQuasQ3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class MilliQuasQ3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'milliquas_q3c'
    mid = db.Column(db.Integer, primary_key=True)
    ra = db.Column(db.Float)
    dec = db.Column(db.Float)
    name = db.Column(db.String(DB_VARCHAR_32))
    objtype = db.Column(db.String(DB_VARCHAR_8))
    rmag = db.Column(db.Float)
    bmag = db.Column(db.Float)
    comment = db.Column(db.String(DB_VARCHAR_8))
    rpsf = db.Column(db.String(DB_VARCHAR_1))
    bpsf = db.Column(db.String(DB_VARCHAR_1))
    z = db.Column(db.Float)
    namecit = db.Column(db.String(DB_VARCHAR_8))
    zcit = db.Column(db.String(DB_VARCHAR_8))
    qpct = db.Column(db.Integer)
    xname = db.Column(db.String(DB_VARCHAR_32))
    rname = db.Column(db.String(DB_VARCHAR_32))
    lobe1 = db.Column(db.String(DB_VARCHAR_32))
    lobe2 = db.Column(db.String(DB_VARCHAR_32))

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'mid': self.mid,
            'ra': self.ra,
            'dec': self.dec,
            'name': self.name,
            'objtype': self.objtype,
            'rmag': self.rmag,
            'bmag': self.bmag,
            'comment': self.comment,
            'rpsf': self.rpsf,
            'bpsf': self.bpsf,
            'z': self.z,
            'namecit': self.namecit,
            'zcit': self.zcit,
            'qpct': self.qpct,
            'xname': self.xname,
            'rname': self.rname,
            'lobe1': self.lobe1,
            'lobe2': self.lobe2
        }

    # +
    # (overload) method: __str__()
    # -
    def __str__(self):
        return self.mid

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(m_records):
        return [_a.serialized() for _a in m_records]
