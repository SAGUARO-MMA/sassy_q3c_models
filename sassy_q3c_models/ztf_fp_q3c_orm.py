#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                                              Table "public.ztf_fp_q3c"
       Column       |         Type          | Collation | Nullable |                 Default                  | Storage  | Stats target | Description
--------------------+-----------------------+-----------+----------+------------------------------------------+----------+--------------+-------------
 fpid               | bigint                |           | not null | nextval('ztf_fp_q3c_fpid_seq'::regclass) | plain    |              |
 candid             | bigint                |           | not null |                                          | plain    |              |
 oid                | character varying(64) |           |          |                                          | extended |              |
 fpid               | bigint                |           | not null | nextval('ztf_fp_q3c_fpid_seq'::regclass) | plain    |              |
 field              | integer               |           |          |                                          | plain    |              |
 rcid               | integer               |           |          |                                          | plain    |              |
 fid                | integer               |           | not null |                                          | plain    |              |
 pid                | bigint                |           | not null |                                          | plain    |              |
 rfid               | bigint                |           | not null |                                          | plain    |              |
 sciinpseeing       | double precision      |           |          |                                          | plain    |              |
 scibckgnd          | double precision      |           |          |                                          | plain    |              |
 scisigpix          | double precision      |           |          |                                          | plain    |              |
 magzpsci           | double precision      |           |          |                                          | plain    |              |
 magzpsciunc        | double precision      |           |          |                                          | plain    |              |
 magzpscirms        | double precision      |           |          |                                          | plain    |              |
 clrcoeff           | double precision      |           |          |                                          | plain    |              |
 clrcounc           | double precision      |           |          |                                          | plain    |              |
 exptime            | double precision      |           |          |                                          | plain    |              |
 adpctdif1          | double precision      |           |          |                                          | plain    |              |
 adpctdif2          | double precision      |           |          |                                          | plain    |              |
 diffmaglim         | double precision      |           |          |                                          | plain    |              |
 programid          | integer               |           | not null |                                          | plain    |              |
 jd                 | double precision      |           | not null |                                          | plain    |              |
 forcediffimflux    | double precision      |           |          |                                          | plain    |              |
 forcediffimfluxunc | double precision      |           |          |                                          | plain    |              |
 procstatus         | character varying(16) |           |          |                                          | extended |              |
 distnr             | double precision      |           |          |                                          | plain    |              |
 ranr               | double precision      |           | not null |                                          | plain    |              |
 decnr              | double precision      |           | not null |                                          | plain    |              |
 magnr              | double precision      |           |          |                                          | plain    |              |
 sigmagnr           | double precision      |           |          |                                          | plain    |              |
 chinr              | double precision      |           |          |                                          | plain    |              |
 sharpnr            | double precision      |           |          |                                          | plain    |              |
Indexes:
    "ztf_fp_q3c_pkey" PRIMARY KEY, btree (fpid)
    "idx_ztf_fp_q3c_jd" btree (jd)
    "ztf_fp_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(ranr, decnr)) CLUSTER
Access method: heap
"""


# +
# constant(s)
# -
ZTF_FP_Q3C_DAT_URL = ''
ZTF_FP_Q3C_PAG_URL = ''
ZTF_FP_Q3C_PDF_URL = ''
ZTF_FP_Q3C_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
ZTF_FP_Q3C_SORT_VALUE = ['fpid', 'field', 'ranr', 'decnr', 'jd', 'fid', 'candid', 'oid']
ZTF_FP_Q3C_HEADERS = ('fpid', 'candid', 'oid', 'field', 'rcid', 'fid', 'pid', 'rfid', 'sciinpseeing', 'scibckgnd', 
                      'scisigpix', 'magzpsci', 'magzpsciunc', 'magzpscirms', 'clrcoeff', 'clrcounc', 'exptime', 'adpctdif1', 'adpctdif2', 'diffmaglim', 
                      'programid', 'jd', 'forcediffimflux', 'forcediffimfluxunc', 'procstatus', 'distnr', 'ranr', 'decnr', 'magnr', 'sigmagnr', 
                      'chinr', 'sharpnr')


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: ZtfFpQ3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class ZtfFpQ3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'ztf_fp_q3c'
    fpid = db.Column(db.BigInteger, primary_key=True)
    candid = db.Column(db.BigInteger, nullable=False)
    oid = db.Column(db.String(DB_VARCHAR_64), nullable=False)
    field = db.Column(db.Integer)
    rcid = db.Column(db.Integer)
    fid = db.Column(db.Integer, nullable=False)
    pid = db.Column(db.BigInteger, nullable=False)
    rfid = db.Column(db.BigInteger, nullable=False)
    sciinpseeing = db.Column(db.Float)
    scibckgnd = db.Column(db.Float)
    scisigpix = db.Column(db.Float)
    magzpsci = db.Column(db.Float)
    magzpsciunc = db.Column(db.Float)
    magzpscirms = db.Column(db.Float)
    clrcoeff = db.Column(db.Float)
    clrcounc = db.Column(db.Float)
    exptime = db.Column(db.Float)
    adpctdif1 = db.Column(db.Float)
    adpctdif2 = db.Column(db.Float)
    diffmaglim = db.Column(db.Float)
    programid = db.Column(db.Integer, nullable=False)
    jd = db.Column(db.Float, nullable=False, index=True)
    forcediffimflux = db.Column(db.Float)
    forcediffimfluxunc = db.Column(db.Float)
    procstatus = db.Column(db.String(DB_VARCHAR_16), default='')
    distnr = db.Column(db.Float)
    ranr = db.Column(db.Float, nullable=False)
    decnr = db.Column(db.Float, nullable=False)
    magnr = db.Column(db.Float)
    sigmagnr = db.Column(db.Float)
    chinr = db.Column(db.Float)
    sharpnr = db.Column(db.Float)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'fpid': self.fpid,
            'candid': self.candid,
            'oid': self.oid,
            'field': self.field,
            'rcid': self.rcid,
            'fid': self.fid,
            'pid': self.pid,
            'rfid': self.rfid,
            'sciinpseeing': self.sciinpseeing,
            'scibckgnd': self.scibckgnd,
            'scisigpix': self.scisigpix,
            'magzpsci': self.magzpsci,
            'magzpsciunc': self.magzpsciunc,
            'magzpscirms': self.magzpscirms,
            'clrcoeff': self.clrcoeff,
            'clrcounc': self.clrcounc,
            'exptime': self.exptime,
            'adpctdif1': self.adpctdif1,
            'adpctdif2': self.adpctdif2,
            'diffmaglim': self.diffmaglim,
            'programid': self.programid,
            'jd': self.jd,
            'forcediffimflux': self.forcediffimflux, 
            'forcediffimfluxunc': self.forcediffimfluxunc,
            'procstatus': self.procstatus,
            'distnr': self.distnr,
            'ranr': self.ranr,
            'decnr': self.decnr,
            'magnr': self.magnr,
            'sigmagnr': self.sigmagnr,
            'chinr': self.chinr,
            'sharpnr': self.sharpnr
        }

    # +
    # (overload) method: __str__()
    # -
    def __str__(self):
        return self.fpid

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(n_records):
        return [_a.serialized() for _a in n_records]
