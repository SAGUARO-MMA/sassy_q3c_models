#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                                          Table "public.ls_dr10_photo_z_q3c"
     Column      |       Type       | Collation | Nullable |                     Default                      | Storage  | Stats target | Description 
-----------------+------------------+-----------+----------+--------------------------------------------------+----------+--------------+-------------
 lid             | bigint           |           | not null | nextval('ls_dr10_photo_z_q3c_lid_seq'::regclass) | plain    |              | 
 brickid         | integer          |           |          |                                                  | plain    |              | 
 objid           | integer          |           |          |                                                  | plain    |              | 
 z_phot_mean     | real             |           |          |                                                  | plain    |              | 
 z_phot_median   | real             |           |          |                                                  | plain    |              | 
 z_phot_std      | real             |           |          |                                                  | plain    |              | 
 z_phot_l68      | real             |           |          |                                                  | plain    |              | 
 z_phot_u68      | real             |           |          |                                                  | plain    |              | 
 z_phot_l95      | real             |           |          |                                                  | plain    |              | 
 z_phot_u95      | real             |           |          |                                                  | plain    |              | 
 z_phot_mean_i   | real             |           |          |                                                  | plain    |              | 
 z_phot_median_i | real             |           |          |                                                  | plain    |              | 
 z_phot_std_i    | real             |           |          |                                                  | plain    |              | 
 z_phot_l68_i    | real             |           |          |                                                  | plain    |              | 
 z_phot_u68_i    | real             |           |          |                                                  | plain    |              | 
 z_phot_l95_i    | real             |           |          |                                                  | plain    |              | 
 z_phot_u95_i    | real             |           |          |                                                  | plain    |              | 
 z_spec          | real             |           |          |                                                  | plain    |              | 
 release         | smallint         |           |          |                                                  | plain    |              | 
 training        | boolean          |           |          |                                                  | plain    |              | 
 training_i      | boolean          |           |          |                                                  | plain    |              | 
 survey          | text             |           |          |                                                  | extended |              | 
 kfold           | integer          |           |          |                                                  | plain    |              | 
 kfold_i         | integer          |           |          |                                                  | plain    |              | 
 ra              | double precision |           |          |                                                  | plain    |              | 
 declination     | double precision |           |          |                                                  | plain    |              | 
 flux_r          | double precision |           |          |                                                  | plain    |              | 
 flux_z          | double precision |           |          |                                                  | plain    |              | 
Indexes:
    "ls_dr10_photo_z_q3c_pkey" PRIMARY KEY, btree (lid)
    "idx_ls_dr10_photo_z_q3c_objid" btree (objid)
    "idx_ls_dr10_photo_z_q3c_z_phot_mean" btree (z_phot_mean)
    "idx_ls_dr10_photo_z_q3c_z_phot_mean_i" btree (z_phot_mean_i)
    "idx_ls_dr10_photo_z_q3c_z_phot_median" btree (z_phot_median)
    "idx_ls_dr10_photo_z_q3c_z_phot_median_i" btree (z_phot_median_i)
    "idx_ls_dr10_photo_z_q3c_z_spec" btree (z_spec)
    "idx_ls_dr10_photo_z_q3c_flux_r" btree (flux_r)
    "ls_dr10_photo_z_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(ra, declination)) CLUSTER
Access method: heap
"""


# +
# constant(s)
# -
LSDR10_PHOTOZ_DAT_URL = 'https://datalab.noirlab.edu/ls/dataAccess.php'
LSDR10_PHOTOZ_PAG_URL = 'https://datalab.noirlab.edu/ls/ls.php'
LSDR10_PHOTOZ_PDF_URL = 'https://arxiv.org/abs/1804.08657.pdf'
LSDR10_PHOTOZ_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
LSDR10_PHOTOZ_SORT_VALUE = ['lid', 'objid', 'ra', 'declination', 'z_phot_mean', 'z_phot_median', 'z_phot_mean_i', 'z_phot_median_i', 'z_spec']
LSDR10_PHOTOZ_HEADERS = ('lid', 'brickid', 'objid', 'z_phot_mean', 'z_phot_median', 'z_phot_std', 'z_phot_l68', 'z_phot_u68', 
                         'z_phot_l95', 'z_phot_u95', 'z_phot_mean_i', 'z_phot_median_i', 'z_phot_std_i', 'z_phot_l68_i', 
                         'z_phot_u68_i', 'z_phot_l95_i', 'z_phot_u95_i', 'z_spec', 'release', 'training', 'training_i', 
                         'survey', 'kfold', 'kfold_i', 'ra', 'declination', 'flux_r', 'flux_z')


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: LsDr10PhotoZQ3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class LsDr10PhotoZQ3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'ls_dr10_photo_z_q3c'
    lid = db.Column(db.Integer, primary_key=True)
    brickid = db.Column(db.Integer)
    objid = db.Column(db.Integer, index=True)
    z_phot_mean = db.Column(db.Float, index=True)
    z_phot_median = db.Column(db.Float, index=True)
    z_phot_std = db.Column(db.Float)
    z_phot_l68 = db.Column(db.Float)
    z_phot_u68 = db.Column(db.Float)
    z_phot_l95 = db.Column(db.Float)
    z_phot_u95 = db.Column(db.Float)
    z_phot_mean_i = db.Column(db.Float, index=True)
    z_phot_median_i = db.Column(db.Float, index=True)
    z_phot_std_i = db.Column(db.Float)
    z_phot_l68_i = db.Column(db.Float)
    z_phot_u68_i = db.Column(db.Float)
    z_phot_l95_i = db.Column(db.Float)
    z_phot_u95_i = db.Column(db.Float)
    z_spec = db.Column(db.Float)
    release = db.Column(db.SmallInteger)
    survey = db.Column(db.Text)
    training = db.Column(db.Boolean)
    training_i = db.Column(db.Boolean)
    kfold = db.Column(db.Integer)
    kfold_i = db.Column(db.Integer)
    ra = db.Column(db.Float, nullable=False, index=True)
    declination = db.Column(db.Float, nullable=False, index=True)
    flux_r = db.Column(db.Float, index=True)
    flux_z = db.Column(db.Float)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'lid': self.lid,
            'brickid': self.brickid,
            'objid': self.objid,
            'z_phot_mean': self.z_phot_mean,
            'z_phot_median': self.z_phot_median,
            'z_phot_std': self.z_phot_std,
            'z_phot_l68': self.z_phot_l68,
            'z_phot_u68': self.z_phot_u68,
            'z_phot_l95': self.z_phot_l95,
            'z_phot_u95': self.z_phot_u95,
            'z_phot_mean_i': self.z_phot_mean_i,
            'z_phot_median_i': self.z_phot_median_i,
            'z_phot_std_i': self.z_phot_std_i,
            'z_phot_l68_i': self.z_phot_l68_i,
            'z_phot_u68_i': self.z_phot_u68_i,
            'z_phot_l95_i': self.z_phot_l95_i,
            'z_phot_u95_i': self.z_phot_u95_i,
            'z_spec': self.z_spec,
            'release': self.release,
            'survey': self.survey,
            'training': self.training,
            'training_i': self.training_i,
            'kfold': self.kfold,
            'kfold_i': self.kfold_i,
            'ra': self.ra,
            'declination': self.declination,
            'flux_r': self.flux_r,
            'flux_z': self.flux_z
        }

    # +
    # (overload) method: __str__()
    # -
    def __str__(self):
        return self.lid

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(m_records):
        return [_a.serialized() for _a in m_records]
