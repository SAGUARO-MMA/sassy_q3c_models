#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                                            Table "public.roma_bzcat_q3c"
     Column     |         Type          | Collation | Nullable |                   Default                   | Storage  | Stats target | Description
----------------+-----------------------+-----------+----------+---------------------------------------------+----------+--------------+-------------
 rid            | integer               |           | not null | nextval('roma_bzcat_q3c_rid_seq'::regclass) | plain    |              |
 name           | character varying(16) |           | not null |                                             | extended |              |
 ra             | double precision      |           |          |                                             | plain    |              |
 dec            | double precision      |           |          |                                             | plain    |              |
 l              | double precision      |           |          |                                             | plain    |              |
 b              | double precision      |           |          |                                             | plain    |              |
 z              | double precision      |           |          |                                             | plain    |              |
 z_err          | double precision      |           |          |                                             | plain    |              |
 rmag           | double precision      |           |          |                                             | plain    |              |
 classification | character varying(64) |           |          |                                             | extended |              |
 flux           | double precision      |           |          |                                             | plain    |              |
 flux_143       | double precision      |           |          |                                             | plain    |              |
 flux_xray      | double precision      |           |          |                                             | plain    |              |
 flux_fermi     | double precision      |           |          |                                             | plain    |              |
 aro            | double precision      |           |          |                                             | plain    |              |
Indexes:
    "roma_bzcat_q3c_pkey" PRIMARY KEY, btree (rid)
    "idx_roma_bzcat_q3c_rmag" btree (rmag)
    "idx_roma_bzcat_q3c_z" btree (z)
    "roma_bzcat_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(ra, "dec")) CLUSTER
Access method: heap
"""


# +
# constant(s)
# -
ROMA_BZCAT_DAT_URL = 'https://cdsarc.cds.unistra.fr/ftp/VII/274/bzcat5.dat'
ROMA_BZCAT_PAG_URL = 'http://vizier.cds.unistra.fr/viz-bin/VizieR?-source=VII/274'
ROMA_BZCAT_PDF_URL = 'https://link.springer.com/content/pdf/10.1007/s10509-015-2254-2.pdf'
ROMA_BZCAT_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
ROMA_BZCAT_SORT_VALUE = ['rid', 'name', 'ra', 'dec', 'z', 'rmag']
ROMA_BZCAT_HEADERS = ('rid', 'name', 'ra', 'dec', 'l', 'b', 'z', 'z_err', 'rmag', 'classification',
                      'flux', 'flux_143', 'flux_xray', 'flux_fermi', 'aro', 'simbad')
ROMA_BZCAT_HTUPLES = (
    ("Seq", "rid"),
    ("Name", "name"),
    ("RAJ2000", "ra"),
    ("DEJ2000", "dec"),
    ("GLON", "l"),
    ("GLAT", "b"),
    ("z", "z"),
    ("u_z", "z_err"),
    ("Rmag", "rmag"),
    ("Class", "classification"),
    ("FR", "flux"),
    ("F143", "flux_143"),
    ("FX", "flux_xray"),
    ("FF", "flux_fermi"),
    ("aro", "aro"),
    ("Simbad", "simbad")
)
ROMA_BZCAT_HEADERS = [_v[0] for _v in ROMA_BZCAT_HTUPLES]
ROMA_BZCAT_KEYS = [_v[1] for _v in ROMA_BZCAT_HTUPLES]
ROMA_BZCAT_COLUMNS = len(ROMA_BZCAT_HEADERS)


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: RomaBzcatQ3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class RomaBzcatQ3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'roma_bzcat_q3c'
    rid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(DB_VARCHAR_16), nullable=False, default='')
    ra = db.Column(db.Float, nullable=False, index=True)
    dec = db.Column(db.Float, nullable=False, index=True)
    l = db.Column(db.Float, nullable=False, index=True)
    b = db.Column(db.Float, nullable=False, index=True)
    z = db.Column(db.Float, nullable=False, index=True)
    z_err = db.Column(db.Float, nullable=False, index=True)
    rmag = db.Column(db.Float, nullable=False, index=True)
    classification = db.Column(db.String(DB_VARCHAR_64), nullable=False, default='')
    flux = db.Column(db.Float, nullable=False, index=True)
    flux_143 = db.Column(db.Float, nullable=False, index=True)
    flux_xray = db.Column(db.Float, nullable=False, index=True)
    flux_fermi = db.Column(db.Float, nullable=False, index=True)
    aro = db.Column(db.Float, nullable=False, index=True)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'rid': self.rid,
            'name': self.name,
            'ra': self.ra,
            'dec': self.dec,
            'l': self.l,
            'b': self.b,
            'z': self.z,
            'z_err': self.z_err,
            'rmag': self.rmag,
            'classification': self.classification,
            'flux': self.flux,
            'flux_143': self.flux_143,
            'flux_xray': self.flux_xray,
            'flux_fermi': self.flux_fermi,
            'aro': self.aro,
        }

    # +
    # (overload) method: __str__()
    # -
    def __str__(self):
        return self.rid

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(m_records):
        return [_a.serialized() for _a in m_records]

