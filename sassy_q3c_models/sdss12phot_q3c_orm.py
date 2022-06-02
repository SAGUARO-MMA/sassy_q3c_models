#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """ 
   Column   |         Type          | Collation | Nullable |                   Default                   | Storage  | Stats target | Description
------------+-----------------------+-----------+----------+---------------------------------------------+----------+--------------+-------------
 sid        | integer               |           | not null | nextval('sdss12phot_q3c_sid_seq'::regclass) | plain    |              |
 ra         | double precision      |           |          |                                             | plain    |              |
 dec        | double precision      |           |          |                                             | plain    |              |
 mode       | integer               |           |          |                                             | plain    |              |
 q_mode     | character varying(1)  |           |          |                                             | extended |              |
 classifier | integer               |           |          |                                             | plain    |              |
 sdss12     | character varying(24) |           |          |                                             | extended |              |
 m_sdss12   | character varying(1)  |           |          |                                             | extended |              |
 obsdate    | double precision      |           |          |                                             | plain    |              |
 quality    | integer               |           |          |                                             | plain    |              |
 umag       | double precision      |           |          |                                             | plain    |              |
 e_umag     | double precision      |           |          |                                             | plain    |              |
 gmag       | double precision      |           |          |                                             | plain    |              |
 e_gmag     | double precision      |           |          |                                             | plain    |              |
 rmag       | double precision      |           |          |                                             | plain    |              |
 e_rmag     | double precision      |           |          |                                             | plain    |              |
 imag       | double precision      |           |          |                                             | plain    |              |
 e_imag     | double precision      |           |          |                                             | plain    |              |
 zmag       | double precision      |           |          |                                             | plain    |              |
 e_zmag     | double precision      |           |          |                                             | plain    |              |
 zsp        | double precision      |           |          |                                             | plain    |              |
 zsh        | double precision      |           |          |                                             | plain    |              |
 e_zsh      | double precision      |           |          |                                             | plain    |              |
 lastcol    | double precision      |           |          |                                             | plain    |              |
Indexes:
    "sdss12phot_q3c_pkey" PRIMARY KEY, btree (sid)
    "sdss12phot_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(ra, "dec")) CLUSTER
Access method: heap
"""


# +
# constant(s)
# -
SDSS12PHOT_COLUMNS = 23
SDSS12PHOT_DAT_URL = 'None'
SDSS12PHOT_PAG_URL = 'https://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=V/147'
SDSS12PHOT_PDF_URL = 'https://arxiv.org/pdf/1501.00963.pdf'
SDSS12PHOT_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
SDSS12PHOT_SORT_VALUE = ['sid', 'sdss12', 'ra', 'dec', 'obsdate', 'u', 'g', 'r', 'i', 'z', 'zsp']
SDSS12PHOT_HEADERS = ('sid', 'ra', 'dec', 'mode', 'q_mode', 'classifier', 'sdss12', 'm_sdss12', 'obsdate', 'quality', 'umag',
                      'e_umag', 'gmag', 'e_gmag', 'rmag', 'e_rmag', 'imag', 'e_imag', 'zmag', 'e_zmag', 'zsp', 'zsh', 'e_zsh', 'lastcol')


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: Sdss12PhotQ3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class Sdss12PhotQ3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'sdss12phot_q3c'
    sid = db.Column(db.Integer, primary_key=True)
    ra = db.Column(db.Float, nullable=False, index=True)
    dec = db.Column(db.Float, nullable=False, index=True)
    mode = db.Column(db.Integer, nullable=True, default=-1)
    q_mode = db.Column(db.String(DB_VARCHAR_1), nullable=False, default='')
    classifier = db.Column(db.Integer, nullable=True, default=-1)
    sdss12 = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')
    m_sdss12 = db.Column(db.String(DB_VARCHAR_1), nullable=False, default='')
    obsdate = db.Column(db.Float, nullable=True, default=math.nan)
    quality = db.Column(db.Integer, nullable=True, default=-1)
    umag = db.Column(db.Float, nullable=True, default=math.nan)
    e_umag = db.Column(db.Float, nullable=True, default=math.nan)
    gmag = db.Column(db.Float, nullable=True, default=math.nan)
    e_gmag = db.Column(db.Float, nullable=True, default=math.nan)
    rmag = db.Column(db.Float, nullable=True, default=math.nan)
    e_rmag = db.Column(db.Float, nullable=True, default=math.nan)
    imag = db.Column(db.Float, nullable=True, default=math.nan)
    e_imag = db.Column(db.Float, nullable=True, default=math.nan)
    zmag = db.Column(db.Float, nullable=True, default=math.nan)
    e_zmag = db.Column(db.Float, nullable=True, default=math.nan)
    zsp = db.Column(db.Float, nullable=True, default=math.nan)
    zph = db.Column(db.Float, nullable=True, default=math.nan)
    e_zph = db.Column(db.Float, nullable=True, default=math.nan)
    lastcol = db.Column(db.Float, nullable=True, default=math.nan)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'sid': self.sid,
            'ra': self.ra,
            'dec': self.dec,
            'mode': self.mode,
            'q_mode': self.q_mode,
            'classifier': self.classifier,
            'sdss12': self.sdss12,
            'm_sdss12': self.m_sdss12,
            'obsdate': self.obsdate,
            'quality': self.quality,
            'umag': self.umag,
            'e_umag': self.e_umag,
            'gmag': self.gmag,
            'e_gmag': self.e_gmag,
            'rmag': self.rmag,
            'e_rmag': self.e_rmag,
            'imag': self.imag,
            'e_imag': self.e_imag,
            'zmag': self.zmag,
            'e_zmag': self.e_zmag,
            'zsp': self.zsp,
            'zph': self.zph,
            'e_zph': self.e_zph,
            'lastcol': self.lastcol
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
