#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                                            Table "public.fermi_lat_q3c"
     Column     |         Type          | Collation | Nullable |                  Default                   | Storage  | Stats target | Description
----------------+-----------------------+-----------+----------+--------------------------------------------+----------+--------------+-------------
 fid            | integer               |           | not null | nextval('fermi_lat_q3c_fid_seq'::regclass) | plain    |              |
 name           | character varying(24) |           | not null |                                            | extended |              |
 b              | double precision      |           |          |                                            | plain    |              |
 l              | double precision      |           |          |                                            | plain    |              |
 lbllac         | double precision      |           |          |                                            | plain    |              |
 pbllac         | double precision      |           |          |                                            | plain    |              |
 pfsrq          | double precision      |           |          |                                            | plain    |              |
 classification | character varying(16) |           |          |                                            | extended |              |
 lbllaclit      | double precision      |           |          |                                            | plain    |              |
 classlit       | character varying(16) |           |          |                                            | extended |              |
 simbad         | character varying(8)  |           |          |                                            | extended |              |
 ra             | double precision      |           |          |                                            | plain    |              |
 dec            | double precision      |           |          |                                            | plain    |              |
Indexes:
    "fermi_lat_q3c_pkey" PRIMARY KEY, btree (fid)
    "fermi_lat_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(ra, "dec")) CLUSTER
    "idx_fermi_lat_q3c_b" btree (b)
    "idx_fermi_lat_q3c_l" btree (l)
Access method: heap
"""

# +
# constant(s)
# -
FERMI_LAT_DAT_URL = 'https://cdsarc.cds.unistra.fr/ftp/J/MNRAS/490/4770/table1.dat'
FERMI_LAT_PAG_URL = 'https://cdsarc.cds.unistra.fr/viz-bin/cat/J/MNRAS/490/4770'
FERMI_LAT_PDF_URL = 'https://arxiv.org/pdf/1911.02948.pdf'
FERMI_LAT_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
FERMI_LAT_SORT_VALUE = ['fid', 'name', 'ra', 'dec', 'l', 'b']
FERMI_LAT_HEADERS = ('fid', 'name', 'b', 'l', 'lbllac', 'pbllac', 'pfsrq', 'classification', 'lbllaclit', 'classlit', 'simbad', 'ra', 'dec')
FERMI_LAT_HTUPLES = (
    ("Name", "name"),
    ("GLAT", "b"),
    ("GLON", "l"),
    ("lBLLac", "lbllac"),
    ("PBLLac", "pbllac"),
    ("PFSRQ", "pfsrq"),
    ("Class", "classification"),
    ("lBLLacLit", "lbllaclit"),
    ("ClassLit", "classlit"),
    ("Simbad", "simbad"),
    ("RA", "ra"),
    ("Dec", "dec")
)
FERMI_LAT_HEADERS = [_v[0] for _v in FERMI_LAT_HTUPLES]
FERMI_LAT_KEYS = [_v[1] for _v in FERMI_LAT_HTUPLES]
FERMI_LAT_COLUMNS = len(FERMI_LAT_HEADERS)


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: FermiLatQ3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class FermiLatQ3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'fermi_lat_q3c'
    fid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(DB_VARCHAR_24), nullable=False, default='')
    b = db.Column(db.Float, nullable=False, index=True)
    l = db.Column(db.Float, nullable=False, index=True)
    lbllac = db.Column(db.Float, nullable=False)
    pbllac = db.Column(db.Float, nullable=False)
    pfsrq = db.Column(db.Float, nullable=False)
    classification = db.Column(db.String(DB_VARCHAR_16), nullable=False, default='')
    lbllaclit = db.Column(db.Float, nullable=False)
    classlit = db.Column(db.String(DB_VARCHAR_16), nullable=False, default='')
    simbad = db.Column(db.String(DB_VARCHAR_8), nullable=False, default='')
    ra = db.Column(db.Float, nullable=False, index=True)
    dec = db.Column(db.Float, nullable=False, index=True)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'fid': self.fid,
            'name': self.name,
            'b': self.b,
            'l': self.l,
            'lbllac': self.lbllac,
            'pbllac': self.pbllac,
            'pfsrq': self.pfsrq,
            'classification': self.classification,
            'lbllaclit': self.lbllaclit,
            'classlit': self.classlit,
            'simbad': self.simbad,
            'ra': self.ra,
            'dec': self.dec
        }

    # +
    # (overload) method: __str__()
    # -
    def __str__(self):
        return self.fid

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(m_records):
        return [_a.serialized() for _a in m_records]

