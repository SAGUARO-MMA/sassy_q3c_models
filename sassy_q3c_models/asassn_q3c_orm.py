#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                             Table "public.asassn_q3c"
       Column        |            Type             | Collation | Nullable |                 Default                 
---------------------+-----------------------------+-----------+----------+-----------------------------------------
 aid                 | integer                     |           | not null | nextval('asassn_q3c_aid_seq'::regclass)
 asassn_id           | character varying(40)       |           |          | 
 source_id           | character varying(20)       |           |          | 
 asassn_name         | character varying(30)       |           |          | 
 other_names         | character varying(32)       |           |          | 
 ra                  | double precision            |           |          | 
 dec                 | double precision            |           |          | 
 l                   | double precision            |           |          | 
 b                   | double precision            |           |          | 
 mean_vmag           | double precision            |           |          | 
 amplitude           | double precision            |           |          | 
 period              | double precision            |           |          | 
 variable_type       | character varying(10)       |           |          | 
 class_probability   | double precision            |           |          | 
 lksl_statistic      | double precision            |           |          | 
 rfr_score           | double precision            |           |          | 
 epoch_hjd           | double precision            |           |          | 
 gdr2_id             | bigint                      |           |          | 
 phot_g_mean_mag     | double precision            |           |          | 
 e_phot_g_mean_mag   | double precision            |           |          | 
 phot_bp_mean_mag    | double precision            |           |          | 
 e_phot_bp_mean_mag  | double precision            |           |          | 
 phot_rp_mean_mag    | double precision            |           |          | 
 e_phot_rp_mean_mag  | double precision            |           |          | 
 bp_rp               | double precision            |           |          | 
 parallax            | double precision            |           |          | 
 parallax_error      | double precision            |           |          | 
 parallax_over_error | double precision            |           |          | 
 pmra                | double precision            |           |          | 
 pmra_error          | double precision            |           |          | 
 pmdec               | double precision            |           |          | 
 pmdec_error         | double precision            |           |          | 
 vt                  | double precision            |           |          | 
 dist                | double precision            |           |          | 
 allwise_id          | character varying(20)       |           |          | 
 j_mag               | double precision            |           |          | 
 e_j_mag             | double precision            |           |          | 
 h_mag               | double precision            |           |          | 
 e_h_mag             | double precision            |           |          | 
 k_mag               | double precision            |           |          | 
 e_k_mag             | double precision            |           |          | 
 w1_mag              | double precision            |           |          | 
 e_w1_mag            | double precision            |           |          | 
 w2_mag              | double precision            |           |          | 
 e_w2_mag            | double precision            |           |          | 
 w3_mag              | double precision            |           |          | 
 e_w3_mag            | double precision            |           |          | 
 w4_mag              | double precision            |           |          | 
 e_w4_mag            | double precision            |           |          | 
 j_k                 | double precision            |           |          | 
 w1_w2               | double precision            |           |          | 
 w3_w4               | double precision            |           |          | 
 apass_dr9_id        | bigint                      |           |          | 
 apass_vmag          | double precision            |           |          | 
 e_apass_vmag        | double precision            |           |          | 
 apass_bmag          | double precision            |           |          | 
 e_apass_bmag        | double precision            |           |          | 
 apass_gpmag         | double precision            |           |          | 
 e_apass_gpmag       | double precision            |           |          | 
 apass_rpmag         | double precision            |           |          | 
 e_apass_rpmag       | double precision            |           |          | 
 apass_ipmag         | double precision            |           |          | 
 e_apass_ipmag       | double precision            |           |          | 
 b_v                 | double precision            |           |          | 
 e_b_v               | double precision            |           |          | 
 vector_x            | double precision            |           |          | 
 vector_y            | double precision            |           |          | 
 vector_z            | double precision            |           |          | 
 reference           | character varying(45)       |           |          | 
 periodic            | boolean                     |           |          | 
 classified          | boolean                     |           |          | 
 asassn_discovery    | boolean                     |           |          | 
 created_at          | timestamp without time zone |           |          | 
 updated_at          | timestamp without time zone |           |          | 
 edr3_source_id      | character varying(25)       |           |          | 
 galex_id            | character varying(25)       |           |          | 
 fuvmag              | double precision            |           |          | 
 e_fuvmag            | double precision            |           |          | 
 nuvmag              | double precision            |           |          | 
 e_nuvmag            | double precision            |           |          | 
 tic_id              | character varying(16)       |           |          | 
 pm                  | double precision            |           |          | 
 ruwe                | double precision            |           |          | 
Indexes:
    "asassn_q3c_pkey" PRIMARY KEY, btree (aid)
    "asassn_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(ra, "dec")) CLUSTER
"""


# +
# constant(s)
# -
ASASSN_COLUMNS = 82
ASASSN_DAT_URL = 'https://drive.google.com/file/d/1oDeWKuIIvMscd5DNNcLWb1rbSaAQ-LHr/view?usp=sharing'
ASASSN_PDF_URL = 'https://arXiv.org/pdf/2006.10057.pdf'
ASASSN_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
ASASSN_SORT_VALUE = ['ra', 'dec', 'vmag', 'amplitude', 'period', 'lksl', 'parallax', 'class_probability',
                     'variable_type']
ASASSN_HEADERS = ('aid', 'asassn_id', 'source_id', 'asassn_name', 'other_names', 'ra', 'dec', 'l', 'b', 'mean_vmag',
                  'amplitude', 'period', 'variable_type', 'class_probability', 'lksl_statistic', 'rfr_score',
                  'epoch_hjd', 'gdr2_id', 'phot_g_mean_mag', 'e_phot_g_mean_mag', 'phot_bp_mean_mag',
                  'e_phot_bp_mean_mag', 'phot_rp_mean_mag', 'e_phot_rp_mean_mag', 'bp_rp', 'parallax',
                  'parallax_error', 'parallax_over_error', 'pmra', 'pmra_error', 'pmdec', 'pmdec_error', 'vt', 'dist',
                  'allwise_id', 'j_mag', 'e_j_mag', 'h_mag', 'e_h_mag', 'k_mag', 'e_k_mag', 'w1_mag', 'e_w1_mag',
                  'w2_mag', 'e_w2_mag', 'w3_mag', 'e_w3_mag', 'w4_mag', 'e_w4_mag', 'j_k', 'w1_w2', 'w3_w4',
                  'apass_dr9_id', 'apass_vmag', 'e_apass_vmag', 'apass_bmag', 'e_apass_bmag', 'apass_gpmag',
                  'e_apass_gpmag', 'apass_rpmag', 'e_apass_rpmag', 'apass_ipmag', 'e_apass_ipmag', 'b_v', 'e_b_v',
                  'vector_x', 'vector_y', 'vector_z', 'reference', 'periodic', 'classified', 'asassn_discovery',
                  'created_at', 'updated_at', 'edr3_source_id', 'galex_id', 'fuvmag', 'e_fuvmag', 'nuvmag',
                  'e_nuvmag', 'tic_id', 'pm', 'ruwe')


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: AsAssnQ3cRecord(): inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class AsAssnQ3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'asassn_q3c'
    aid = db.Column(db.Integer, primary_key=True)
    asassn_id = db.Column(db.String(DB_VARCHAR_40))
    source_id = db.Column(db.String(DB_VARCHAR_20))
    asassn_name = db.Column(db.String(DB_VARCHAR_30))
    other_names = db.Column(db.String(DB_VARCHAR_32))
    ra = db.Column(db.Float)
    dec = db.Column(db.Float)
    l = db.Column(db.Float)
    b = db.Column(db.Float)
    mean_vmag = db.Column(db.Float)
    amplitude = db.Column(db.Float)
    period = db.Column(db.Float)
    variable_type = db.Column(db.String(DB_VARCHAR_10))
    class_probability = db.Column(db.Float)
    lksl_statistic = db.Column(db.Float)
    rfr_score = db.Column(db.Float)
    epoch_hjd = db.Column(db.Float)
    gdr2_id = db.Column(db.BigInteger)
    phot_g_mean_mag = db.Column(db.Float)
    e_phot_g_mean_mag = db.Column(db.Float)
    phot_bp_mean_mag = db.Column(db.Float)
    e_phot_bp_mean_mag = db.Column(db.Float)
    phot_rp_mean_mag = db.Column(db.Float)
    e_phot_rp_mean_mag = db.Column(db.Float)
    bp_rp = db.Column(db.Float)
    parallax = db.Column(db.Float)
    parallax_error = db.Column(db.Float)
    parallax_over_error = db.Column(db.Float)
    pmra = db.Column(db.Float)
    pmra_error = db.Column(db.Float)
    pmdec = db.Column(db.Float)
    pmdec_error = db.Column(db.Float)
    vt = db.Column(db.Float)
    dist = db.Column(db.Float)
    allwise_id = db.Column(db.String(DB_VARCHAR_20))
    j_mag = db.Column(db.Float)
    e_j_mag = db.Column(db.Float)
    h_mag = db.Column(db.Float)
    e_h_mag = db.Column(db.Float)
    k_mag = db.Column(db.Float)
    e_k_mag = db.Column(db.Float)
    w1_mag = db.Column(db.Float)
    e_w1_mag = db.Column(db.Float)
    w2_mag = db.Column(db.Float)
    e_w2_mag = db.Column(db.Float)
    w3_mag = db.Column(db.Float)
    e_w3_mag = db.Column(db.Float)
    w4_mag = db.Column(db.Float)
    e_w4_mag = db.Column(db.Float)
    j_k = db.Column(db.Float)
    w1_w2 = db.Column(db.Float)
    w3_w4 = db.Column(db.Float)
    apass_dr9_id = db.Column(db.BigInteger)
    apass_vmag = db.Column(db.Float)
    e_apass_vmag = db.Column(db.Float)
    apass_bmag = db.Column(db.Float)
    e_apass_bmag = db.Column(db.Float)
    apass_gpmag = db.Column(db.Float)
    e_apass_gpmag = db.Column(db.Float)
    apass_rpmag = db.Column(db.Float)
    e_apass_rpmag = db.Column(db.Float)
    apass_ipmag = db.Column(db.Float)
    e_apass_ipmag = db.Column(db.Float)
    b_v = db.Column(db.Float)
    e_b_v = db.Column(db.Float)
    vector_x = db.Column(db.Float)
    vector_y = db.Column(db.Float)
    vector_z = db.Column(db.Float)
    reference = db.Column(db.String(DB_VARCHAR_45))
    periodic = db.Column(db.Boolean)
    classified = db.Column(db.Boolean)
    asassn_discovery = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    edr3_source_id = db.Column(db.String(DB_VARCHAR_25))
    galex_id = db.Column(db.String(DB_VARCHAR_25))
    fuvmag = db.Column(db.Float)
    e_fuvmag = db.Column(db.Float)
    nuvmag = db.Column(db.Float)
    e_nuvmag = db.Column(db.Float)
    tic_id = db.Column(db.String(DB_VARCHAR_16))
    pm = db.Column(db.Float)
    ruwe = db.Column(db.Float)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'aid': self.aid,
            'asassn_id': self.asassn_id,
            'source_id': self.source_id,
            'asassn_name': self.asassn_name,
            'other_names': self.other_names,
            'ra': self.ra,
            'dec': self.dec,
            'l': self.l,
            'b': self.b,
            'mean_vmag': self.mean_vmag,
            'amplitude': self.amplitude,
            'period': self.period,
            'variable_type': self.variable_type,
            'class_probability': self.class_probability,
            'lksl_statistic': self.lksl_statistic,
            'rfr_score': self.rfr_score,
            'epoch_hjd': self.epoch_hjd,
            'gdr2_id':  self.gdr2_id,
            'phot_g_mean_mag': self.phot_g_mean_mag,
            'e_phot_g_mean_mag': self.e_phot_g_mean_mag,
            'phot_bp_mean_mag': self.phot_bp_mean_mag,
            'e_phot_bp_mean_mag': self.e_phot_bp_mean_mag,
            'phot_rp_mean_mag': self.phot_rp_mean_mag,
            'e_phot_rp_mean_mag': self.e_phot_rp_mean_mag,
            'bp_rp': self.bp_rp,
            'parallax': self.parallax,
            'parallax_error': self.parallax_error,
            'parallax_over_error': self.parallax_over_error,
            'pmra': self.pmra,
            'pmra_error': self.pmra_error,
            'pmdec': self.pmdec,
            'pmdec_error': self.pmdec_error,
            'vt': self.vt,
            'dist': self.dist,
            'allwise_id': self.allwise_id,
            'j_mag': self.j_mag,
            'e_j_mag': self.e_j_mag,
            'h_mag': self.h_mag,
            'e_h_mag': self.e_j_mag,
            'k_mag': self.k_mag,
            'e_k_mag': self.e_k_mag,
            'w1_mag': self.w1_mag,
            'e_w1_mag': self.e_w1_mag,
            'w2_mag': self.w2_mag,
            'e_w2_mag': self.e_w2_mag,
            'w3_mag': self.w3_mag,
            'e_w3_mag': self.e_w3_mag,
            'w4_mag': self.w4_mag,
            'e_w4_mag': self.e_w4_mag,
            'j_k': self.j_k,
            'w1_w2': self.w1_w2,
            'w3_w4': self.w3_w4,
            'apass_dr9_id':  self.apass_dr9_id,
            'apass_vmag': self.apass_vmag,
            'e_apass_vmag': self.e_apass_vmag,
            'apass_bmag': self.apass_bmag,
            'e_apass_bmag': self.e_apass_bmag,
            'apass_gpmag': self.apass_gpmag,
            'e_apass_gpmag': self.e_apass_gpmag,
            'apass_rpmag': self.apass_rpmag,
            'e_apass_rpmag': self.e_apass_rpmag,
            'apass_ipmag': self.apass_ipmag,
            'e_apass_ipmag': self.e_apass_ipmag,
            'b_v': self.b_v,
            'e_b_v': self.e_b_v,
            'vector_x': self.vector_x,
            'vector_y': self.vector_y,
            'vector_z': self.vector_z,
            'reference': self.reference,
            'periodic':  self.periodic,
            'classified':  self.classified,
            'asassn_discovery': self.asassn_discovery,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'edr3_source_id': self.edr3_source_id,
            'galex_id': self.galex_id,
            'fuvmag': self.fuvmag,
            'e_fuvmag': self.e_fuvmag,
            'nuvmag': self.nuvmag,
            'e_nuvmag': self.e_nuvmag,
            'tic_id': self.tic_id,
            'pm': self.pm,
            'ruwe': self.ruwe
        }

    # +
    # (overload) method: __str__()
    # -
    def __str__(self):
        return self.aid

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(m_records):
        return [_a.serialized() for _a in m_records]
