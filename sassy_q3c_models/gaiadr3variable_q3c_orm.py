#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                       Table "public.gaiadr3variable_q3c"
    Column                      |         Type          | Collation | Nullable |                    Default                    
--------------------------------+-----------------------+-----------+----------+-----------------------------------------------
 gid                            | integer               |           | not null | nextval('gaiadr3variable_q3c_gid_seq'::regclass)
 ra                             | double precision      |           |          | 
 ra_error                       | double precision      |           |          | 
 dec                            | double precision      |           |          | 
 dec_error                      | double precision      |           |          | 
 pmra                           | double precision      |           |          | 
 pmra_error                     | double precision      |           |          | 
 pmdec                          | double precision      |           |          | 
 pmdec_error                    | double precision      |           |          | 
 parallax                       | double precision      |           |          | 
 parallax_error                 | double precision      |           |          | 
 solution_id                    | bigint                |           |          | 
 source_id                      | bigint                |           |          | 
 classification                 | character varying(16) |           |          | 
 best_class_name                | character varying (26)|           |          | 
 best_class_score               | double precision      |           |          | 
 num_selected_g_fov             | integer               |           |          | 
 mean_obs_time_g_fov            | double precision      |           |          | 
 time_duration_g_fov            | double precision      |           |          | 
 min_mag_g_fov                  | double precision      |           |          | 
 max_mag_g_fov                  | double precision      |           |          | 
 mean_mag_g_fov                 | double precision      |           |          | 
 median_mag_g_fov               | double precision      |           |          | 
 range_mag_g_fov                | double precision      |           |          | 
 trimmed_range_mag_g_fov        | double precision      |           |          | 
 std_dev_mag_g_fov              | double precision      |           |          | 
 skewness_mag_g_fov             | double precision      |           |          | 
 kurtosis_mag_g_fov             | double precision      |           |          | 
 mad_mag_g_fov                  | double precision      |           |          | 
 abbe_mag_g_fov                 | double precision      |           |          | 
 iqr_mag_g_fov                  | double precision      |           |          | 
 stetson_mag_g_fov              | double precision      |           |          | 
 std_dev_over_rms_err_mag_g_fov | double precision      |           |          | 
 outlier_median_g_fov           | double precision      |           |          | 
 num_selected_bp                | integer               |           |          | 
 mean_obs_time_bp               | double precision      |           |          | 
 time_duration_bp               | double precision      |           |          | 
 min_mag_bp                     | double precision      |           |          | 
 max_mag_bp                     | double precision      |           |          | 
 mean_mag_bp                    | double precision      |           |          | 
 median_mag_bp                  | double precision      |           |          | 
 range_mag_bp                   | double precision      |           |          | 
 trimmed_range_mag_bp           | double precision      |           |          | 
 std_dev_mag_bp                 | double precision      |           |          | 
 skewness_mag_bp                | double precision      |           |          | 
 kurtosis_mag_bp                | double precision      |           |          | 
 mad_mag_bp                     | double precision      |           |          | 
 abbe_mag_bp                    | double precision      |           |          | 
 iqr_mag_bp                     | double precision      |           |          | 
 stetson_mag_bp                 | double precision      |           |          | 
 std_dev_over_rms_err_mag_bp    | double precision      |           |          | 
 outlier_median_bp              | double precision      |           |          | 
 num_selected_rp                | integer               |           |          | 
 mean_obs_time_rp               | double precision      |           |          | 
 time_duration_rp               | double precision      |           |          | 
 min_mag_rp                     | double precision      |           |          | 
 max_mag_rp                     | double precision      |           |          | 
 mean_mag_rp                    | double precision      |           |          | 
 median_mag_rp                  | double precision      |           |          | 
 range_mag_rp                   | double precision      |           |          | 
 trimmed_range_mag_rp           | double precision      |           |          | 
 std_dev_mag_rp                 | double precision      |           |          | 
 skewness_mag_rp                | double precision      |           |          | 
 kurtosis_mag_rp                | double precision      |           |          | 
 mad_mag_rp                     | double precision      |           |          | 
 abbe_mag_rp                    | double precision      |           |          | 
 iqr_mag_rp                     | double precision      |           |          | 
 stetson_mag_rp                 | double precision      |           |          | 
 std_dev_over_rms_err_mag_rp    | double precision      |           |          | 
 outlier_median_rp              | double precision      |           |          | 
 in_vari_classification_result  | boolean               |           |          | 
 in_vari_rrlyrae                | boolean               |           |          | 
 in_vari_cepheid                | boolean               |           |          | 
 in_vari_planetary_transit      | boolean               |           |          | 
 in_vari_short_timescale        | boolean               |           |          | 
 in_vari_long_period_variable   | boolean               |           |          | 
 in_vari_eclipsing_binary       | boolean               |           |          | 
 in_vari_rotation_modulation    | boolean               |           |          | 
 in_vari_ms_oscillator          | boolean               |           |          | 
 in_vari_agn                    | boolean               |           |          | 
 in_vari_microlensing           | boolean               |           |          | 
 in_vari_compact_companion      | boolean               |           |          | 
Indexes:
    "gaiadr3variable_q3c_pkey" PRIMARY KEY, btree (gid)
    "idx_gaiadr3variable_q3c_ra" btree (ra)
    "idx_gaiadr3variable_q3c_dec" btree (dec)
    "idx_gaiadr3variable_q3c_ra_error" btree (ra_error)
    "idx_gaiadr3variable_q3c_dec_error" btree (dec_error)
    "idx_gaiadr3variable_q3c_pmra" btree (pmra)
    "idx_gaiadr3variable_q3c_pmdec" btree (pmdec)
    "idx_gaiadr3variable_q3c_classification" btree (classification)
    "idx_gaiadr3variable_q3c_mean_g_mag_fov" btree (mean_g_mag_fov)
    "idx_gaiadr3variable_q3c_median_g_mag_fov" btree (median_g_mag_fov)
    "idx_gaiadr3variable_q3c_best_class_name" btree (best_class_name)
    "idx_gaiadr3variable_q3c_best_class_score" btree (best_class_score)
"""


# +
# constant(s)
# -
GAIADR3VARIABLE_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
GAIADR3VARIABLE_SORT_VALUE = ['gid', 'ra', 'dec', 'ra_error', 'dec_error', 'pmra', 'pmdec', 'mean_g_mag_fov', 'median_g_mag_fov', 'best_class_name', 'best_class_score']
GAIADR3VARIABLE_HTUPLES = (
    # 0: 
    ("ra", "ra"),
    ("ra_error", "ra_error"),
    ("dec", "dec"),
    ("dec_error", "dec_error"),
    ("pmra", "pmra"),
    ("pmra_error", "pmra_error"),
    ("pmdec", "pmdec"),
    ("pmdec_error", "pmdec_error"),
    ("parallax", "parallax"),
    ("parallax_error", "parallax_error"),
    ("solution_id", "solution_id"),
    ("source_id", "source_id"),
    ("classification", "classification"),
    ("best_class_name", "best_class_name"),
    ("best_class_score", "best_class_score"),
    ("num_selected_g_fov", "num_selected_g_fov"),
    ("mean_obs_time_g_fov", "mean_obs_time_g_fov"),
    ("time_duration_g_fov", "time_duration_g_fov"),
    # 10: 
    ("min_mag_g_fov", "min_mag_g_fov"),
    ("max_mag_g_fov", "max_mag_g_fov"),
    ("mean_mag_g_fov", "mean_mag_g_fov"),
    ("median_mag_g_fov", "median_mag_g_fov"),
    ("range_mag_g_fov", "range_mag_g_fov"),
    ("trimmed_range_mag_g_fov", "trimmed_range_mag_g_fov"),
    ("std_dev_mag_g_fov", "std_dev_mag_g_fov"),
    ("skewness_mag_g_fov", "skewness_mag_g_fov"),
    ("kurtosis_mag_g_fov", "kurtosis_mag_g_fov"),
    ("mad_mag_g_fov", "mad_mag_g_fov"),
    # 20: 
    ("abbe_mag_g_fov", "abbe_mag_g_fov"),
    ("iqr_mag_g_fov", "iqr_mag_g_fov"),
    ("stetson_mag_g_fov", "stetson_mag_g_fov"),
    ("std_dev_over_rms_err_mag_g_fov", "std_dev_over_rms_err_mag_g_fov"),
    ("outlier_median_g_fov", "outlier_median_g_fov"),
    ("num_selected_bp", "num_selected_bp"),
    ("mean_obs_time_bp", "mean_obs_time_bp"),
    ("time_duration_bp", "time_duration_bp"),
    ("min_mag_bp", "min_mag_bp"),
    ("max_mag_bp", "max_mag_bp"),
    # 30: 
    ("mean_mag_bp", "mean_mag_bp"),
    ("median_mag_bp", "median_mag_bp"),
    ("range_mag_bp", "range_mag_bp"),
    ("trimmed_range_mag_bp", "trimmed_range_mag_bp"),
    ("std_dev_mag_bp", "std_dev_mag_bp"),
    ("skewness_mag_bp", "spcskewness_mag_bp"),
    ("kurtosis_mag_bp", "kurtosis_mag_bp"),
    ("mad_mag_bp", "mad_mag_bp"),
    ("abbe_mag_bp", "abbe_mag_bp"),
    ("iqr_mag_bp", "iqr_mag_bp"),
    # 40: 
    ("stetson_mag_bp", "stetson_mag_bp"),
    ("std_dev_over_rms_err_mag_bp", "std_dev_over_rms_err_mag_bp"),
    ("outlier_median_bp", "outlier_median_bp"),
    ("num_selected_rp", "num_selected_rp"),
    ("mean_obs_time_rp", "mean_obs_time_rp"),
    ("time_duration_rp", "time_duration_rp"),
    ("min_mag_rp", "min_mag_rp"),
    ("max_mag_rp", "max_mag_rp"),
    ("mean_mag_rp", "mean_mag_rp"),
    ("median_mag_rp", "median_mag_rp"),
    # 50: 
    ("range_mag_rp", "range_mag_rp"),
    ("trimmed_range_mag_rp", "trimmed_range_mag_rp"),
    ("std_dev_mag_rp", "std_dev_mag_rp"),
    ("skewness_mag_rp", "skewness_mag_rp"),
    ("kurtosis_mag_rp", "kurtosis_mag_rp"),
    ("mad_mag_rp", "mad_mag_rp"),
    ("abbe_mag_rp", "abbe_mag_rp"),
    ("iqr_mag_rp", "iqr_mag_rp"),
    ("stetson_mag_rp", "stetson_mag_rp"),
    ("std_dev_over_rms_err_mag_rp", "std_dev_over_rms_err_mag_rp"),
    # 60: 
    ("outlier_median_rp", "outlier_median_rp"),
    ("in_vari_classification_result", "in_vari_classification_result"),
    ("in_vari_rrlyrae", "in_vari_rrlyrae"),
    ("in_vari_cepheid", "in_vari_cepheid"),
    ("in_vari_planetary_transit", "in_vari_planetary_transit"),
    ("in_vari_short_timescale", "in_vari_short_timescale"),
    ("in_vari_long_period_variable", "in_vari_long_period_variable"),
    ("in_vari_eclipsing_binary", "in_vari_eclipsing_binary"),
    ("in_vari_rotation_modulation", "in_vari_rotation_modulation"),
    ("in_vari_ms_oscillator", "in_vari_ms_oscillator"),
    # 70: 
    ("in_vari_agn", "in_vari_agn"),
    ("in_vari_microlensing", "in_vari_microlensing"),
    ("in_vari_compact_companion", "in_vari_compact_companion"),
    ("source_id_2", "source_id_2")
)
GAIADR3VARIABLE_HEADERS = [_v[0] for _v in GAIADR3VARIABLE_HTUPLES]
GAIADR3VARIABLE_KEYS = [_v[1] for _v in GAIADR3VARIABLE_HTUPLES]
GAIADR3VARIABLE_COLUMNS = len(GAIADR3VARIABLE_HEADERS)


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: GaiaDR3VariableQ3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class GaiaDR3VariableQ3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'gaiadr3variable_q3c'
    gid = db.Column(db.Integer, primary_key=True)

    # 0:
    ra = db.Column(db.Float, nullable=False, index=True)
    ra_error = db.Column(db.Float, nullable=False)
    dec = db.Column(db.Float, nullable=False, index=True)
    dec_error = db.Column(db.Float, nullable=False)
    pmra = db.Column(db.Float, nullable=False, index=True)
    pmra_error = db.Column(db.Float, nullable=False)
    pmdec = db.Column(db.Float, nullable=False, index=True)
    pmdec_error = db.Column(db.Float, nullable=False)
    parallax = db.Column(db.Float, nullable=False)
    parallax_error = db.Column(db.Float, nullable=False)
    solution_id = db.Column(db.BigInteger, nullable=True, default=-1)
    source_id = db.Column(db.BigInteger, nullable=True, default=-1)
    classification = db.Column(db.String(DB_VARCHAR_16), nullable=False, default='', index=True)
    best_class_name = db.Column(db.String(DB_VARCHAR_26), nullable=False, default='', index=True)
    best_class_score = db.Column(db.Float, nullable=False, index=True)
    num_selected_g_fov = db.Column(db.Integer, nullable=False, default=-1)
    mean_obs_time_g_fov = db.Column(db.Float, nullable=False)
    time_duration_g_fov = db.Column(db.Float, nullable=False)

    # 10: 
    min_mag_g_fov = db.Column(db.Float, nullable=False)
    max_mag_g_fov = db.Column(db.Float, nullable=False)
    mean_mag_g_fov = db.Column(db.Float, nullable=False, index=True)
    median_mag_g_fov = db.Column(db.Float, nullable=False, index=True)
    range_mag_g_fov = db.Column(db.Float, nullable=False)
    trimmed_range_mag_g_fov = db.Column(db.Float, nullable=False)
    std_dev_mag_g_fov = db.Column(db.Float, nullable=False)
    skewness_mag_g_fov = db.Column(db.Float, nullable=False)
    kurtosis_mag_g_fov = db.Column(db.Float, nullable=False)
    mad_mag_g_fov = db.Column(db.Float, nullable=False)

    # 20: 
    abbe_mag_g_fov = db.Column(db.Float, nullable=False)
    iqr_mag_g_fov = db.Column(db.Float, nullable=False)
    stetson_mag_g_fov = db.Column(db.Float, nullable=False)
    std_dev_over_rms_err_mag_g_fov = db.Column(db.Float, nullable=False)
    outlier_median_g_fov = db.Column(db.Float, nullable=False)
    num_selected_bp = db.Column(db.Integer, nullable=False, default=-1)
    mean_obs_time_bp = db.Column(db.Float, nullable=False)
    time_duration_bp = db.Column(db.Float, nullable=False)
    min_mag_bp = db.Column(db.Float, nullable=False)
    max_mag_bp = db.Column(db.Float, nullable=False)

    # 30: 
    mean_mag_bp = db.Column(db.Float, nullable=False)
    median_mag_bp = db.Column(db.Float, nullable=False)
    range_mag_bp = db.Column(db.Float, nullable=False)
    trimmed_range_mag_bp = db.Column(db.Float, nullable=False)
    std_dev_mag_bp = db.Column(db.Float, nullable=False)
    skewness_mag_bp = db.Column(db.Float, nullable=False)
    kurtosis_mag_bp = db.Column(db.Float, nullable=False)
    mad_mag_bp = db.Column(db.Float, nullable=False)
    abbe_mag_bp = db.Column(db.Float, nullable=False)
    iqr_mag_bp = db.Column(db.Float, nullable=False)

    # 40: 
    stetson_mag_bp = db.Column(db.Integer, nullable=False)
    std_dev_over_rms_err_mag_bp = db.Column(db.Float, nullable=False)
    outlier_median_bp = db.Column(db.Float, nullable=False)
    num_selected_rp = db.Column(db.Integer, nullable=False, default=-1)
    mean_obs_time_rp = db.Column(db.Float, nullable=False)
    time_duration_rp = db.Column(db.Float, nullable=False)
    min_mag_rp = db.Column(db.Float, nullable=False)
    max_mag_rp = db.Column(db.Float, nullable=False)
    mean_mag_rp = db.Column(db.Float, nullable=False)
    median_mag_rp = db.Column(db.Float, nullable=False)

    # 50: 
    range_mag_rp = db.Column(db.Float, nullable=False)
    trimmed_range_mag_rp = db.Column(db.Float, nullable=False)
    std_dev_mag_rp = db.Column(db.Float, nullable=False)
    skewness_mag_rp = db.Column(db.Float, nullable=False)
    kurtosis_mag_rp = db.Column(db.Float, nullable=False)
    mad_mag_rp = db.Column(db.Float, nullable=False)
    abbe_mag_rp = db.Column(db.Float, nullable=False)
    iqr_mag_rp = db.Column(db.Float, nullable=False)
    stetson_mag_rp = db.Column(db.Float, nullable=False)
    std_dev_over_rms_err_mag_rp = db.Column(db.Float, nullable=False)

    # 60: 
    outlier_median_rp = db.Column(db.Float, nullable=False)
    in_vari_classification_result = db.Column(db.Boolean, nullable=False)
    in_vari_rrlyrae = db.Column(db.Boolean, nullable=False)
    in_vari_cepheid = db.Column(db.Boolean, nullable=False)
    in_vari_planetary_transit = db.Column(db.Boolean, nullable=False)
    in_vari_short_timescale = db.Column(db.Boolean, nullable=False)
    in_vari_long_period_variable = db.Column(db.Boolean, nullable=False)
    in_vari_eclipsing_binary = db.Column(db.Boolean, nullable=False)
    in_vari_rotation_modulation = db.Column(db.Boolean, nullable=False)
    in_vari_ms_oscillator = db.Column(db.Boolean, nullable=False)

    # 70: ['gdVell', 'gPA', 'rFlags', 'rs', 'rc', 'rDate', "r'mag", "e_r'mag", 'rpmag', 'e_rpmag']
    in_vari_agn = db.Column(db.Boolean, nullable=False)
    in_vari_microlensing = db.Column(db.Boolean, nullable=False)
    in_vari_compact_companion = db.Column(db.Boolean, nullable=False)


    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'gid': self.gid,

            # 0:  
            'ra': self.ra,
            'ra_error': self.ra_error,
            'dec': self.dec,
            'dec_error': self.dec_error,
            'pmra': self.pmra,
            'pmra_error': self.pmra_error,
            'pmdec': self.pmdec,
            'pmdec_error': self.pmdec_error,
            'parallax': self.parallax,
            'parallax_error': self.parallax_error,
            'solution_id': self.solution_id,
            'source_id': self.source_id,
            'classification': self.classification,
            'best_class_name': self.best_class_name,
            'best_class_score': self.best_class_score,
            'num_selected_g_fov': self.num_selected_g_fov,
            'mean_obs_time_g_fov': self.mean_obs_time_g_fov,

            # 10: 
            'time_duration_g_fov': self.time_duration_g_fov,
            'min_mag_g_fov': self.min_mag_g_fov,
            'max_mag_g_fov': self.max_mag_g_fov,
            'mean_mag_g_fov': self.mean_mag_g_fov,
            'median_mag_g_fov': self.median_mag_g_fov,
            'range_mag_g_fov': self.range_mag_g_fov,
            'trimmed_range_mag_g_fov': self.trimmed_range_mag_g_fov,
            'std_dev_mag_g_fov': self.std_dev_mag_g_fov,
            'skewness_mag_g_fov': self.skewness_mag_g_fov,
            'kurtosis_mag_g_fov': self.kurtosis_mag_g_fov,

            # 20: 
            'mad_mag_g_fov': self.mad_mag_g_fov,
            'abbe_mag_g_fov': self.abbe_mag_g_fov,
            'iqr_mag_g_fov': self.iqr_mag_g_fov,
            'stetson_mag_g_fov': self.stetson_mag_g_fov,
            'std_dev_over_rms_err_mag_g_fov': self.std_dev_over_rms_err_mag_g_fov,
            'outlier_median_g_fov': self.outlier_median_g_fov,
            'num_selected_bp': self.num_selected_bp,
            'mean_obs_time_bp': self.mean_obs_time_bp,
            'time_duration_bp': self.time_duration_bp,
            'min_mag_bp': self.min_mag_bp,

            # 30: 
            'max_mag_bp': self.max_mag_bp,
            'mean_mag_bp': self.mean_mag_bp,
            'median_mag_bp': self.median_mag_bp,
            'range_mag_bp': self.range_mag_bp,
            'trimmed_range_mag_bp': self.trimmed_range_mag_bp,
            'std_dev_mag_bp': self.std_dev_mag_bp,
            'skewness_mag_bp': self.skewness_mag_bp,
            'kurtosis_mag_bp': self.kurtosis_mag_bp,
            'mad_mag_bp': self.mad_mag_bp,
            'abbe_mag_bp': self.abbe_mag_bp,

            # 40: 
            'iqr_mag_bp': self.iqr_mag_bp,
            'stetson_mag_bp': self.stetson_mag_bp,
            'std_dev_over_rms_err_mag_bp': self.std_dev_over_rms_err_mag_bp,
            'outlier_median_bp': self.outlier_median_bp,
            'num_selected_rp': self.num_selected_rp,
            'mean_obs_time_rp': self.mean_obs_time_rp,
            'time_duration_rp': self.time_duration_rp,
            'min_mag_rp': self.min_mag_rp,
            'max_mag_rp': self.max_mag_rp,
            'mean_mag_rp': self.mean_mag_rp,

            # 50: 
            'median_mag_rp': self.median_mag_rp,
            'range_mag_rp': self.range_mag_rp,
            'trimmed_range_mag_rp': self.trimmed_range_mag_rp,
            'std_dev_mag_rp': self.std_dev_mag_rp,
            'skewness_mag_rp': self.skewness_mag_rp,
            'kurtosis_mag_rp': self.kurtosis_mag_rp,
            'mad_mag_rp': self.mad_mag_rp,
            'abbe_mag_rp': self.abbe_mag_rp,
            'iqr_mag_rp': self.iqr_mag_rp,
            'stetson_mag_rp': self.stetson_mag_rp,

            # 60: 
            'std_dev_over_rms_err_mag_rp': self.std_dev_over_rms_err_mag_rp,
            'outlier_median_rp': self.outlier_median_rp,
            'in_vari_classification_result': self.in_vari_classification_result,
            'in_vari_rrlyrae': self.in_vari_rrlyrae,
            'in_vari_cepheid': self.in_vari_cepheid,
            'in_vari_planetary_transit': self.in_vari_planetary_transit,
            'in_vari_short_timescale': self.in_vari_short_timescale,
            'in_vari_long_period_variable': self.in_vari_long_period_variable,
            'in_vari_eclipsing_binary': self.in_vari_eclipsing_binary,
            'in_vari_rotation_modulation': self.in_vari_rotation_modulation,

            # 70: 
            'in_vari_ms_oscillator': self.in_vari_ms_oscillator,
            'in_vari_agn': self.in_vari_agn,
            'in_vari_microlensing': self.in_vari_microlensing,
            'in_vari_compact_companion': self.in_vari_compact_companion,
        }

    # +
    # (overload) method: __str__()
    # -
    def __str__(self):
        return self.gid

    # +
    # (static) method: serialize_list()
    # -
    @staticmethod
    def serialize_list(m_records):
        return [_a.serialized() for _a in m_records]
