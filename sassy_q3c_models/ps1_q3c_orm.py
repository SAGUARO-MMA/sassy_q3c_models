#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
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
    'z_zero', 'extra_photoz', 'celld_photoz', 'cellid_photoz', 'ps_score')
PS1_HEADERS = ('pid', 'objid', 'psps_objid', 'ra', 'dec', 'l',
    'b', 'obj_class', 'prob_galaxy', 'prob_star', 'prob_qso',
    'extra_class', 'celld_class', 'cellid_class', 'z_phot', 'z_err',
    'z_zero', 'extra_photoz', 'celld_photoz', 'cellid_photoz', 'ps_score')


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
    l = db.Column(db.Float, nullable=False)
    b = db.Column(db.Float, nullable=False)
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
    ps_score = db.Column(db.Float)

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
            'ps_score': self.ps_score
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
