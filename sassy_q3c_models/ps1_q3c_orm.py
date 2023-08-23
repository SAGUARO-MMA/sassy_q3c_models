#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                        Table "public.ps1_q3c"
     Column     |         Type          | Collation | Nullable |               Default
----------------+-----------------------+-----------+----------+--------------------------------------
 pid            | bigint                |           | not null | nextval('ps1_q3c_pid_seq'::regclass)
 objid          | bigint                |           |          |
 psps_objid     | bigint                |           |          |
 ra             | double precision      |           | not null |
 dec            | double precision      |           | not null |
 l              | double precision      |           |          |
 b              | double precision      |           |          |
 obj_class      | character varying(8)  |           |          |
 prob_galaxy    | double precision      |           |          |
 prob_star      | double precision      |           |          |
 prob_qso       | double precision      |           |          |
 extra_class    | double precision      |           |          |
 celld_class    | double precision      |           |          |
 cellid_class   | integer               |           |          |
 z_phot         | double precision      |           |          |
 z_err          | double precision      |           |          |
 z_zero         | double precision      |           |          |
 extra_photoz   | integer               |           |          |
 celld_photoz   | double precision      |           |          |
 cellid_photoz  | integer               |           |          |
 ps_score       | double precision      |           |          |
 objname        | character varying(64) |           |          | ''::character varying
 objinfoflag    | integer               |           |          | '-999'::integer
 qualityflag    | integer               |           |          | '-999'::integer
 ndetections    | integer               |           |          | '-999'::integer
 ramean         | double precision      |           |          | '-999.0'::numeric
 rameanerr      | double precision      |           |          | '-999.0'::numeric
 decmean        | double precision      |           |          | '-999.0'::numeric
 decmeanerr     | double precision      |           |          | '-999.0'::numeric
 gmeanpsfmag    | double precision      |           |          | '-999.0'::numeric
 gmeanpsfmagerr | double precision      |           |          | '-999.0'::numeric
 rmeanpsfmag    | double precision      |           |          | '-999.0'::numeric
 rmeanpsfmagerr | double precision      |           |          | '-999.0'::numeric
 imeanpsfmag    | double precision      |           |          | '-999.0'::numeric
 imeanpsfmagerr | double precision      |           |          | '-999.0'::numeric
 zmeanpsfmag    | double precision      |           |          | '-999.0'::numeric
 zmeanpsfmagerr | double precision      |           |          | '-999.0'::numeric
 ymeanpsfmag    | double precision      |           |          | '-999.0'::numeric
 ymeanpsfmagerr | double precision      |           |          | '-999.0'::numeric
Indexes:
    "ps1_q3c_pkey" PRIMARY KEY, btree (pid)
    "idx_ps1_q3c_gmeanpsfmag" btree (gmeanpsfmag)
    "idx_ps1_q3c_imeanpsfmag" btree (imeanpsfmag)
    "idx_ps1_q3c_objid" btree (objid)
    "idx_ps1_q3c_ps_score" btree (ps_score)
    "idx_ps1_q3c_psps_objid" btree (psps_objid)
    "idx_ps1_q3c_rmeanpsfmag" btree (rmeanpsfmag)
    "idx_ps1_q3c_ymeanpsfmag" btree (ymeanpsfmag)
    "idx_ps1_q3c_zmeanpsfmag" btree (zmeanpsfmag)
    "ps1_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(ra, "dec")) CLUSTER
"""


# +
# constant(s)
# -
PS1_DAT_URL = 'https://archive.stsci.edu/hlsp/ps1-strm#section-ea0203ae-9960-44b9-bf7e-51fc095c0cb1'
PS1_PAG_URL = 'https://archive.stsci.edu/hlsp/ps1-strm'
PS1_PDF_URL = ''
PS1_SORT_ORDER = ('asc', 'desc', 'ascending', 'descending')
PS1_SORT_VALUE = ('pid', 'objid', 'psps_objid', 'ra', 'dec', 'l',
    'b', 'obj_class', 'prob_galaxy', 'prob_star', 'prob_qso',
    'extra_class', 'celld_class', 'cellid_class', 'z_phot', 'z_err',
    'z_zero', 'extra_photoz', 'celld_photoz', 'cellid_photoz', 'ps_score',
    'objname', 'objinfoflag', 'qualityflag', 'ndetections', 'ramean', 'rameanerr',
    'decmean', 'decmeanerr', 'gmeanpsfmag', 'gmeanpsfmagerr', 'rmeanpsfmag', 'rmeanpsfmagerr',
    'imeanpsfmag', 'imeanpsfmagerr', 'zmeanpsfmag', 'zmeanpsfmagerr', 'ymeanpsfmag', 'ymeanpsfmagerr')
PS1_HEADERS = ('pid', 'objid', 'psps_objid', 'ra', 'dec', 'l',
    'b', 'obj_class', 'prob_galaxy', 'prob_star', 'prob_qso',
    'extra_class', 'celld_class', 'cellid_class', 'z_phot', 'z_err',
    'z_zero', 'extra_photoz', 'celld_photoz', 'cellid_photoz', 'ps_score',
    'objname', 'objinfoflag', 'qualityflag', 'ndetections', 'ramean', 'rameanerr',
    'decmean', 'decmeanerr', 'gmeanpsfmag', 'gmeanpsfmagerr', 'rmeanpsfmag', 'rmeanpsfmagerr',
    'imeanpsfmag', 'imeanpsfmagerr', 'zmeanpsfmag', 'zmeanpsfmagerr', 'ymeanpsfmag', 'ymeanpsfmagerr')


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: Ps1Q3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class Ps1Q3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'ps1_q3c'
    pid = db.Column(db.BigInteger, primary_key=True)
    objid = db.Column(db.BigInteger, nullable=True, default=-1, index=True)
    psps_objid = db.Column(db.BigInteger, nullable=False, default=-1)
    ra = db.Column(db.Float, nullable=False, index=True)
    dec = db.Column(db.Float, nullable=False, index=True)
    l = db.Column(db.Float)
    b = db.Column(db.Float)
    obj_class = db.Column(db.String(DB_VARCHAR_8))
    prob_galaxy = db.Column(db.Float)
    prob_star = db.Column(db.Float)
    prob_qso = db.Column(db.Float)
    extra_class = db.Column(db.Float)
    celld_class = db.Column(db.Float)
    cellid_class = db.Column(db.Integer)
    z_phot = db.Column(db.Float)
    z_err = db.Column(db.Float)
    z_zero = db.Column(db.Float)
    extra_photoz = db.Column(db.Integer)
    celld_photoz = db.Column(db.Float)
    cellid_photoz = db.Column(db.Integer)
    ps_score = db.Column(db.Float, index=True)

    # added 20230731
    objname = db.Column(db.String(DB_VARCHAR_64))
    objinfoflag = db.Column(db.Integer)
    qualityflag = db.Column(db.Integer)
    ndetections = db.Column(db.Integer)
    ramean = db.Column(db.Float)
    rameanerr = db.Column(db.Float)
    decmean = db.Column(db.Float)
    decmeanerr = db.Column(db.Float)
    gmeanpsfmag = db.Column(db.Float)
    gmeanpsfmagerr = db.Column(db.Float)
    rmeanpsfmag = db.Column(db.Float)
    rmeanpsfmagerr = db.Column(db.Float)
    imeanpsfmag = db.Column(db.Float)
    imeanpsfmagerr = db.Column(db.Float)
    zmeanpsfmag = db.Column(db.Float)
    zmeanpsfmagerr = db.Column(db.Float)
    ymeanpsfmag = db.Column(db.Float)
    ymeanpsfmagerr = db.Column(db.Float)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'pid': self.pid,
            'objid': self.objid,
            'psps_objid': self.psps_objid,
            'ra': self.ra,
            'dec': self.dec,
            'l': self.l,
            'b': self.b,
            'obj_class': self.obj_class,
            'prob_galaxy': self.prob_galaxy,
            'prob_star': self.prob_star,
            'prob_qso': self.prob_qso,
            'extra_class': self.extra_class,
            'celld_class': self.celld_class,
            'cellid_class': self.cellid_class,
            'z_phot': self.z_phot,
            'z_err': self.z_err,
            'z_zero': self.z_zero,
            'extra_photoz': self.extra_photoz,
            'celld_photoz': self.celld_photoz,
            'cellid_photoz': self.cellid_photoz,
            'ps_score': self.ps_score,
            'objname': self.objname,
            'objinfoflag': self.objinfoflag,
            'qualityflag': self.qualityflag,
            'ndetections': self.ndetections,
            'ramean': self.ramean,
            'rameanerr': self.rameanerr,
            'decmean': self.decmean,
            'decmeanerr': self.decmeanerr,
            'gmeanpsfmag': self.gmeanpsfmag,
            'gmeanpsfmagerr': self.gmeanpsfmagerr,
            'rmeanpsfmag': self.rmeanpsfmag,
            'rmeanpsfmagerr': self.rmeanpsfmagerr,
            'imeanpsfmag': self.imeanpsfmag,
            'imeanpsfmagerr': self.imeanpsfmagerr,
            'zmeanpsfmag': self.zmeanpsfmag,
            'zmeanpsfmagerr': self.zmeanpsfmagerr,
            'ymeanpsfmag': self.ymeanpsfmag,
            'ymeanpsfmagerr': self.ymeanpsfmagerr
        }

    # +
    # (overload) method: __str__()
    # -
    def __str__(self):
        return self.pid

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(p_records):
        return [_a.serialized() for _a in p_records]
