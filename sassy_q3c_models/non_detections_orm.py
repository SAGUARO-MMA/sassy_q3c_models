#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                      Table "public.non_detections"
   Column   |         Type          | Collation | Nullable |                   Default                   
------------+-----------------------+-----------+----------+---------------------------------------------
 nid        | bigint                |           | not null | nextval('non_detections_nid_seq'::regclass)
 oid        | character varying(50) |           |          | 
 diffmaglim | double precision      |           | not null | 
 jd         | double precision      |           | not null | 
 fid        | integer               |           | not null | 
Indexes:
    "non_detections_pkey" PRIMARY KEY, btree (nid)
    "idx_non_detections_jd" btree (jd)
    "idx_non_detections_oid" btree (oid)
"""


# +
# constant(s)
# -
NON_DETECTIONS_DAT_URL = 'None'
NON_DETECTIONS_PAG_URL = 'None'
NON_DETECTIONS_PDF_URL = 'None'
NON_DETECTIONS_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
NON_DETECTIONS_SORT_VALUE = ['nid', 'oid', 'diffmaglim', 'jd', 'fid']
NON_DETECTIONS_HEADERS = ('nid', 'oid', 'diffmaglim', 'jd', 'fid')


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: NonDetectionsRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class NonDetectionsRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'non_detections'
    nid = db.Column(db.BigInteger, primary_key=True)
    oid = db.Column(db.String(DB_VARCHAR_64), nullable=False, index=True)
    diffmaglim = db.Column(db.Float, nullable=False)
    jd = db.Column(db.Float, nullable=False, index=True)
    fid = db.Column(db.Integer, nullable=False)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'candidate': {
                'nid': self.nid,
                'oid': self.oid,
                'diffmaglim': self.diffmaglim,
                'jd': self.jd,
                'fid': self.fid
            }
        }

    # +
    # (overload) method: __str__()
    # -
    def __str__(self):
        return self.nid

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(n_records):
        return [_a.serialized() for _a in n_records]
