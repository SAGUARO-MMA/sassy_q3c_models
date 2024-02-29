#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models import *


# +
# __doc__ string
# -
__doc__ = """
                                                                  Table "public.desi_spec_q3c"
           Column           |         Type          | Collation | Nullable |                  Default                   | Storage  | Stats target | Description
----------------------------+-----------------------+-----------+----------+--------------------------------------------+----------+--------------+-------------
 did                        | integer               |           | not null | nextval('desi_spec_q3c_did_seq'::regclass) | plain    |              |
 targetid                   | bigint                |           |          |                                            | plain    |              |
 survey                     | character varying(7)  |           |          |                                            | extended |              |
 program                    | character varying(6)  |           |          |                                            | extended |              |
 healpix                    | integer               |           |          |                                            | plain    |              |
 spgrpval                   | integer               |           |          |                                            | plain    |              |
 z                          | double precision      |           |          |                                            | plain    |              |:
 zerr                       | double precision      |           |          |                                            | plain    |              |
 zwarn                      | bigint                |           |          |                                            | plain    |              |
 chi2                       | double precision      |           |          |                                            | plain    |              |
 coeff_0                    | double precision      |           |          |                                            | plain    |              |
 coeff_1                    | double precision      |           |          |                                            | plain    |              |
 coeff_2                    | double precision      |           |          |                                            | plain    |              |
 coeff_3                    | double precision      |           |          |                                            | plain    |              |
 coeff_4                    | double precision      |           |          |                                            | plain    |              |
 coeff_5                    | double precision      |           |          |                                            | plain    |              |
 coeff_6                    | double precision      |           |          |                                            | plain    |              |
 coeff_7                    | double precision      |           |          |                                            | plain    |              |
 coeff_8                    | double precision      |           |          |                                            | plain    |              |
 coeff_9                    | double precision      |           |          |                                            | plain    |              |
 npixels                    | bigint                |           |          |                                            | plain    |              |
 spectype                   | character varying(6)  |           |          |                                            | extended |              |
 subtype                    | character varying(20) |           |          |                                            | extended |              |
 ncoeff                     | bigint                |           |          |                                            | plain    |              |
 deltachi2                  | double precision      |           |          |                                            | plain    |              |
 coadd_fiberstatus          | integer               |           |          |                                            | plain    |              |
 target_ra                  | double precision      |           |          |                                            | plain    |              |
 target_dec                 | double precision      |           |          |                                            | plain    |              |
 pmra                       | double precision      |           |          |                                            | plain    |              |
 pmdec                      | double precision      |           |          |                                            | plain    |              |
 ref_epoch                  | double precision      |           |          |                                            | plain    |              |
 fa_target                  | bigint                |           |          |                                            | plain    |              |
 fa_type                    | integer               |           |          |                                            | plain    |              |
 objtype                    | character varying(3)  |           |          |                                            | extended |              |
 subpriority                | double precision      |           |          |                                            | plain    |              |
 obsconditions              | integer               |           |          |                                            | plain    |              |
 release                    | integer               |           |          |                                            | plain    |              |
 brickname                  | character varying(8)  |           |          |                                            | extended |              |
 brickid                    | integer               |           |          |                                            | plain    |              |
 brick_objid                | integer               |           |          |                                            | plain    |              |
 morphtype                  | character varying(4)  |           |          |                                            | extended |              |
 ebv                        | double precision      |           |          |                                            | plain    |              |
 flux_g                     | double precision      |           |          |                                            | plain    |              |
 flux_r                     | double precision      |           |          |                                            | plain    |              |
 flux_z                     | double precision      |           |          |                                            | plain    |              |
 flux_w1                    | double precision      |           |          |                                            | plain    |              |
 flux_w2                    | double precision      |           |          |                                            | plain    |              |
 flux_ivar_g                | double precision      |           |          |                                            | plain    |              |
 flux_ivar_r                | double precision      |           |          |                                            | plain    |              |
 flux_ivar_z                | double precision      |           |          |                                            | plain    |              |
 flux_ivar_w1               | double precision      |           |          |                                            | plain    |              |
 flux_ivar_w2               | double precision      |           |          |                                            | plain    |              |
 fiberflux_g                | double precision      |           |          |                                            | plain    |              |
 fiberflux_r                | double precision      |           |          |                                            | plain    |              |
 fiberflux_z                | double precision      |           |          |                                            | plain    |              |
 fibertotflux_g             | double precision      |           |          |                                            | plain    |              |
 fibertotflux_r             | double precision      |           |          |                                            | plain    |              |
 fibertotflux_z             | double precision      |           |          |                                            | plain    |              |
 maskbits                   | integer               |           |          |                                            | plain    |              |
 sersic                     | double precision      |           |          |                                            | plain    |              |
 shape_r                    | double precision      |           |          |                                            | plain    |              |
 shape_e1                   | double precision      |           |          |                                            | plain    |              |
 shape_e2                   | double precision      |           |          |                                            | plain    |              |
 ref_id                     | bigint                |           |          |                                            | plain    |              |
 ref_cat                    | character varying(2)  |           |          |                                            | extended |              |
 gaia_phot_g_mean_mag       | double precision      |           |          |                                            | plain    |              |
 gaia_phot_bp_mean_mag      | double precision      |           |          |                                            | plain    |              |
 gaia_phot_rp_mean_mag      | double precision      |           |          |                                            | plain    |              |
 parallax                   | double precision      |           |          |                                            | plain    |              |
 photsys                    | character varying(1)  |           |          |                                            | extended |              |
 priority_init              | bigint                |           |          |                                            | plain    |              |
 numobs_init                | bigint                |           |          |                                            | plain    |              |
 cmx_target                 | bigint                |           |          |                                            | plain    |              |
 sv1_desi_target            | bigint                |           |          |                                            | plain    |              |
 sv1_bgs_target             | bigint                |           |          |                                            | plain    |              |
 sv1_mws_target             | bigint                |           |          |                                            | plain    |              |
 sv1_scnd_target            | bigint                |           |          |                                            | plain    |              |
 sv2_desi_target            | bigint                |           |          |                                            | plain    |              |
 sv2_bgs_target             | bigint                |           |          |                                            | plain    |              |
 sv2_mws_target             | bigint                |           |          |                                            | plain    |              |
 sv2_scnd_target            | bigint                |           |          |                                            | plain    |              |
 sv3_desi_target            | bigint                |           |          |                                            | plain    |              |
 sv3_bgs_target             | bigint                |           |          |                                            | plain    |              |
 sv3_mws_target             | bigint                |           |          |                                            | plain    |              |
 sv3_scnd_target            | bigint                |           |          |                                            | plain    |              |
 desi_target                | bigint                |           |          |                                            | plain    |              |
 bgs_target                 | bigint                |           |          |                                            | plain    |              |
 mws_target                 | bigint                |           |          |                                            | plain    |              |
 scnd_target                | bigint                |           |          |                                            | plain    |              |
 plate_ra                   | double precision      |           |          |                                            | plain    |              |
 plate_dec                  | double precision      |           |          |                                            | plain    |              |
 coadd_numexp               | integer               |           |          |                                            | plain    |              |
 coadd_exptime              | double precision      |           |          |                                            | plain    |              |
 coadd_numnight             | integer               |           |          |                                            | plain    |              |
 coadd_numtile              | integer               |           |          |                                            | plain    |              |
 mean_delta_x               | double precision      |           |          |                                            | plain    |              |
 rms_delta_x                | double precision      |           |          |                                            | plain    |              |
 mean_delta_y               | double precision      |           |          |                                            | plain    |              |
 rms_delta_y                | double precision      |           |          |                                            | plain    |              |
 mean_fiber_ra              | double precision      |           |          |                                            | plain    |              |
 std_fiber_ra               | double precision      |           |          |                                            | plain    |              |
 mean_fiber_dec             | double precision      |           |          |                                            | plain    |              |
 std_fiber_dec              | double precision      |           |          |                                            | plain    |              |
 mean_psf_to_fiber_specflux | double precision      |           |          |                                            | plain    |              |
 tsnr2_gpbdark_b            | double precision      |           |          |                                            | plain    |              |
 tsnr2_elg_b                | double precision      |           |          |                                            | plain    |              |
 tsnr2_gpbbright_b          | double precision      |           |          |                                            | plain    |              |
 tsnr2_lya_b                | double precision      |           |          |                                            | plain    |              |
 tsnr2_bgs_b                | double precision      |           |          |                                            | plain    |              |
 tsnr2_gpbbackup_b          | double precision      |           |          |                                            | plain    |              |
 tsnr2_qso_b                | double precision      |           |          |                                            | plain    |              |
 tsnr2_lrg_b                | double precision      |           |          |                                            | plain    |              |
 tsnr2_gpbdark_r            | double precision      |           |          |                                            | plain    |              |
 tsnr2_elg_r                | double precision      |           |          |                                            | plain    |              |
 tsnr2_gpbbright_r          | double precision      |           |          |                                            | plain    |              |
 tsnr2_lya_r                | double precision      |           |          |                                            | plain    |              |
 tsnr2_bgs_r                | double precision      |           |          |                                            | plain    |              |
 tsnr2_gpbbackup_r          | double precision      |           |          |                                            | plain    |              |
 tsnr2_qso_r                | double precision      |           |          |                                            | plain    |              |
 tsnr2_lrg_r                | double precision      |           |          |                                            | plain    |              |
 tsnr2_gpbdark_z            | double precision      |           |          |                                            | plain    |              |
 tsnr2_elg_z                | double precision      |           |          |                                            | plain    |              |
 tsnr2_gpbbright_z          | double precision      |           |          |                                            | plain    |              |
 tsnr2_lya_z                | double precision      |           |          |                                            | plain    |              |
 tsnr2_bgs_z                | double precision      |           |          |                                            | plain    |              |
 tsnr2_gpbbackup_z          | double precision      |           |          |                                            | plain    |              |
 tsnr2_qso_z                | double precision      |           |          |                                            | plain    |              |
 tsnr2_lrg_z                | double precision      |           |          |                                            | plain    |              |
 tsnr2_gpbdark              | double precision      |           |          |                                            | plain    |              |
 tsnr2_elg                  | double precision      |           |          |                                            | plain    |              |
 tsnr2_gpbbright            | double precision      |           |          |                                            | plain    |              |
 tsnr2_lya                  | double precision      |           |          |                                            | plain    |              |
 tsnr2_bgs                  | double precision      |           |          |                                            | plain    |              |
 tsnr2_gpbbackup            | double precision      |           |          |                                            | plain    |              |
 tsnr2_qso                  | double precision      |           |          |                                            | plain    |              |
 tsnr2_lrg                  | double precision      |           |          |                                            | plain    |              |
 sv_nspec                   | integer               |           |          |                                            | plain    |              |
 sv_primary                 | boolean               |           |          |                                            | plain    |              |
 zcat_nspec                 | integer               |           |          |                                            | plain    |              |
 zcat_primary               | boolean               |           |          |                                            | plain    |              |
Indexes:
    "desi_spec_q3c_pkey" PRIMARY KEY, btree (did)
    "desi_spec_q3c_q3c_ang2ipix_idx" btree (q3c_ang2ipix(target_ra, target_dec)) CLUSTER
    "idx_desi_spec_q3c_z" btree (z)
Access method: heap
"""


# +
# constant(s)
# -
DESI_SPEC_DAT_URL = ''
DESI_SPEC_PAG_URL = ''
DESI_SPEC_PDF_URL = ''
DESI_SPEC_SORT_ORDER = ['asc', 'desc', 'ascending', 'descending']
DESI_SPEC_SORT_VALUE = ['did', 'spectype', 'objtype', 'brickname', 'target_ra', 'target_dec', 'z']
DESI_SPEC_HEADERS = (
    'did', 'targetid', 'survey', 'program', 'healpix', 'spgrpval', 'z', 'zerr', 'zwarn', 'chi2',
    'coeff_0', 'coeff_1', 'coeff_2', 'coeff_3', 'coeff_4', 'coeff_5', 'coeff_6', 'coeff_7', 'coeff_8', 'coeff_9',
    'npixels', 'spectype', 'subtype', 'ncoeff', 'deltachi2', 'coadd_fiberstatus', 'target_ra', 'target_dec', 'pmra', 'pmdec',
    'ref_epoch', 'fa_target', 'fa_type', 'objtype', 'subpriority', 'obsconditions', 'release', 'brickname', 'brickid', 'brick_objid',
    'morphtype', 'ebv', 'flux_g', 'flux_r', 'flux_z', 'flux_w1', 'flux_w2', 'flux_ivar_g', 'flux_ivar_r', 'flux_ivar_z',
    'flux_ivar_w1', 'flux_ivar_w2', 'fiberflux_g', 'fiberflux_r', 'fiberflux_z', 'fibertotflux_g', 'fibertotflux_r', 'fibertotflux_z', 
    'maskbits', 'sersic', 'shape_r', 'shape_e1', 'shape_e2', 'ref_id', 'ref_cat', 'gaia_phot_g_mean_mag', 'gaia_phot_bp_mean_mag', 
    'gaia_phot_rp_mean_mag', 'parallax', 'photsys', 'priority_init', 'numobs_init', 'cmx_target', 'sv1_desi_target', 'sv1_bgs_target', 
    'sv1_mws_target', 'sv1_scnd_target', 'sv2_desi_target', 'sv2_bgs_target', 'sv2_mws_target', 'sv2_scnd_target', 'sv3_desi_target', 
    'sv3_bgs_target', 'sv3_mws_target', 'sv3_scnd_target', 'desi_target', 'bgs_target', 'mws_target', 'scnd_target', 'plate_ra', 
    'plate_dec', 'coadd_numexp', 'coadd_exptime', 'coadd_numnight', 'coadd_numtile', 'mean_delta_x', 'rms_delta_x', 'mean_delta_y', 
    'rms_delta_y', 'mean_fiber_ra', 'std_fiber_ra', 'mean_fiber_dec', 'std_fiber_dec', 'mean_psf_to_fiber_specflux', 'tsnr2_gpbdark_b', 
    'tsnr2_elg_b', 'tsnr2_gpbbright_b', 'tsnr2_lya_b', 'tsnr2_bgs_b', 'tsnr2_gpbbackup_b', 'tsnr2_qso_b', 'tsnr2_lrg_b', 
    'tsnr2_gpbdark_r', 'tsnr2_elg_r', 'tsnr2_gpbbright_r', 'tsnr2_lya_r', 'tsnr2_bgs_r', 'tsnr2_gpbbackup_r', 'tsnr2_qso_r', 
    'tsnr2_lrg_r', 'tsnr2_gpbdark_z', 'tsnr2_elg_z', 'tsnr2_gpbbright_z', 'tsnr2_lya_z', 'tsnr2_bgs_z', 'tsnr2_gpbbackup_z',
    'tsnr2_qso_z', 'tsnr2_lrg_z', 'tsnr2_gpbdark', 'tsnr2_elg', 'tsnr2_gpbbright', 'tsnr2_lya', 'tsnr2_bgs', 'tsnr2_gpbbackup', 
    'tsnr2_qso', 'tsnr2_lrg', 'sv_nspec', 'sv_primary', 'zcat_nspec', 'zcat_primary')


# +
# initialize sqlalchemy (deferred)
# -
db = SQLAlchemy()


# +
# class: DesiSpecQ3cRecord(), inherits from db.Model
# -
# noinspection PyUnresolvedReferences
class DesiSpecQ3cRecord(db.Model):

    # +
    # define table
    # -
    __tablename__ = 'desi_spec_q3c'
    did = db.Column(db.Integer, primary_key=True)
    targetid = db.Column(db.BigInteger)
    survey = db.Column(db.String(7), default='')
    program = db.Column(db.String(6), default='')
    healpix = db.Column(db.Integer)
    spgrpval = db.Column(db.Integer)
    z = db.Column(db.Float, index=True)
    zerr = db.Column(db.Float)
    zwarn = db.Column(db.BigInteger)
    chi2 = db.Column(db.Float)
    coeff_0 = db.Column(db.Float)
    coeff_1 = db.Column(db.Float)
    coeff_2 = db.Column(db.Float)
    coeff_3 = db.Column(db.Float)
    coeff_4 = db.Column(db.Float)
    coeff_5 = db.Column(db.Float)
    coeff_6 = db.Column(db.Float)
    coeff_7 = db.Column(db.Float)
    coeff_8 = db.Column(db.Float)
    coeff_9 = db.Column(db.Float)
    npixels = db.Column(db.BigInteger)
    spectype = db.Column(db.String(6), default='')
    subtype = db.Column(db.String(20), default='')
    ncoeff = db.Column(db.BigInteger)
    deltachi2 = db.Column(db.Float)
    spgrpval = db.Column(db.Integer)
    coadd_fiberstatus = db.Column(db.Integer)
    target_ra = db.Column(db.Float, index=True)
    target_dec = db.Column(db.Float, index=True)
    pmra = db.Column(db.Float)
    pmdec = db.Column(db.Float)
    ref_epoch = db.Column(db.Float)
    fa_target = db.Column(db.BigInteger)
    fa_type = db.Column(db.Integer)
    objtype = db.Column(db.String(3), default='')
    subpriority = db.Column(db.Float)
    obsconditions = db.Column(db.Integer)
    release = db.Column(db.Integer)
    brickname = db.Column(db.String(8), default='')
    brickid = db.Column(db.Integer)
    brick_objid = db.Column(db.Integer)
    morphtype = db.Column(db.String(4), default='')
    ebv = db.Column(db.Float)
    flux_g = db.Column(db.Float)
    flux_r = db.Column(db.Float)
    flux_z = db.Column(db.Float)
    flux_w1 = db.Column(db.Float)
    flux_w2 = db.Column(db.Float)
    flux_ivar_g = db.Column(db.Float)
    flux_ivar_r = db.Column(db.Float)
    flux_ivar_z = db.Column(db.Float)
    flux_ivar_w1 = db.Column(db.Float)
    flux_ivar_w2 = db.Column(db.Float)
    fiberflux_g = db.Column(db.Float)
    fiberflux_r = db.Column(db.Float)
    fiberflux_z = db.Column(db.Float)
    fibertotflux_g = db.Column(db.Float)
    fibertotflux_r = db.Column(db.Float)
    fibertotflux_z = db.Column(db.Float)
    maskbits = db.Column(db.Integer)
    sersic = db.Column(db.Float)
    shape_r = db.Column(db.Float)
    shape_e1 = db.Column(db.Float)
    shape_e2 = db.Column(db.Float)
    ref_id = db.Column(db.BigInteger)
    ref_cat = db.Column(db.String(2), default='')
    gaia_phot_g_mean_mag = db.Column(db.Float)
    gaia_phot_bp_mean_mag = db.Column(db.Float)
    gaia_phot_rp_mean_mag = db.Column(db.Float)
    parallax = db.Column(db.Float)
    photsys = db.Column(db.String(1), default='')
    priority_init = db.Column(db.BigInteger)
    numobs_init = db.Column(db.BigInteger)
    cmx_target = db.Column(db.BigInteger)
    sv1_desi_target = db.Column(db.BigInteger)
    sv1_bgs_target = db.Column(db.BigInteger)
    sv1_mws_target = db.Column(db.BigInteger)
    sv1_scnd_target = db.Column(db.BigInteger)
    sv2_desi_target = db.Column(db.BigInteger)
    sv2_bgs_target = db.Column(db.BigInteger)
    sv2_mws_target = db.Column(db.BigInteger)
    sv2_scnd_target = db.Column(db.BigInteger)
    sv3_desi_target = db.Column(db.BigInteger)
    sv3_bgs_target = db.Column(db.BigInteger)
    sv3_mws_target = db.Column(db.BigInteger)
    sv3_scnd_target = db.Column(db.BigInteger)
    desi_target = db.Column(db.BigInteger)
    bgs_target = db.Column(db.BigInteger)
    mws_target = db.Column(db.BigInteger)
    scnd_target = db.Column(db.BigInteger)
    plate_ra = db.Column(db.Float)
    plate_dec = db.Column(db.Float)
    coadd_numexp = db.Column(db.Integer)
    coadd_exptime = db.Column(db.Float)
    coadd_numnight = db.Column(db.Integer)
    coadd_numtile = db.Column(db.Integer)
    mean_delta_x = db.Column(db.Float)
    rms_delta_x = db.Column(db.Float)
    mean_delta_y = db.Column(db.Float)
    rms_delta_y = db.Column(db.Float)
    mean_fiber_ra = db.Column(db.Float)
    std_fiber_ra = db.Column(db.Float)
    mean_fiber_dec = db.Column(db.Float)
    std_fiber_dec = db.Column(db.Float)
    mean_psf_to_fiber_specflux = db.Column(db.Float)
    tsnr2_gpbdark_b = db.Column(db.Float)
    tsnr2_elg_b = db.Column(db.Float)
    tsnr2_gpbbright_b = db.Column(db.Float)
    tsnr2_lya_b = db.Column(db.Float)
    tsnr2_bgs_b = db.Column(db.Float)
    tsnr2_gpbbackup_b = db.Column(db.Float)
    tsnr2_qso_b = db.Column(db.Float)
    tsnr2_lrg_b = db.Column(db.Float)
    tsnr2_gpbdark_r = db.Column(db.Float)
    tsnr2_elg_r = db.Column(db.Float)
    tsnr2_gpbbright_r = db.Column(db.Float)
    tsnr2_lya_r = db.Column(db.Float)
    tsnr2_bgs_r = db.Column(db.Float)
    tsnr2_gpbbackup_r = db.Column(db.Float)
    tsnr2_qso_r = db.Column(db.Float)
    tsnr2_lrg_r = db.Column(db.Float)
    tsnr2_gpbdark_z = db.Column(db.Float)
    tsnr2_elg_z = db.Column(db.Float)
    tsnr2_gpbbright_z = db.Column(db.Float)
    tsnr2_lya_z = db.Column(db.Float)
    tsnr2_bgs_z = db.Column(db.Float)
    tsnr2_gpbbackup_z = db.Column(db.Float)
    tsnr2_qso_z = db.Column(db.Float)
    tsnr2_lrg_z = db.Column(db.Float)
    tsnr2_gpbdark = db.Column(db.Float)
    tsnr2_elg = db.Column(db.Float)
    tsnr2_gpbbright = db.Column(db.Float)
    tsnr2_lya = db.Column(db.Float)
    tsnr2_bgs = db.Column(db.Float)
    tsnr2_gpbbackup = db.Column(db.Float)
    tsnr2_qso = db.Column(db.Float)
    tsnr2_lrg = db.Column(db.Float)
    sv_nspec = db.Column(db.Integer)
    sv_primary = db.Column(db.Boolean)
    zcat_nspec = db.Column(db.Integer)
    zcat_primary = db.Column(db.Boolean)

    # +
    # method: serialized()
    # -
    def serialized(self):
        return {
            'did': self.did,
            'targetid': self.targetid,
            'survey': self.survey,
            'program': self.program,
            'healpix': self.healpix,
            'spgrpval': self.spgrpval,
            'z': self.z,
            'zerr': self.zerr,
            'zwarn': self.zwarn,
            'chi2': self.chi2,
            'coeff_0': self.coeff_0,
            'coeff_1': self.coeff_1,
            'coeff_2': self.coeff_2,
            'coeff_3': self.coeff_3,
            'coeff_4': self.coeff_4,
            'coeff_5': self.coeff_5,
            'coeff_6': self.coeff_6,
            'coeff_7': self.coeff_7,
            'coeff_8': self.coeff_8,
            'coeff_9': self.coeff_9,
            'npixels': self.npixels,
            'spectype': self.spectype,
            'subtype': self.subtype,
            'ncoeff': self.ncoeff,
            'deltachi2': self.deltachi2,
            'coadd_fiberstatus': self.coadd_fiberstatus,
            'target_ra': self.target_ra,
            'target_dec': self.target_dec,
            'pmra': self.pmra,
            'pmdec': self.pmdec,
            'ref_epoch': self.ref_epoch,
            'fa_target': self.fa_target,
            'fa_type': self.fa_type,
            'objtype': self.objtype,
            'subpriority': self.subpriority,
            'obsconditions': self.obsconditions,
            'release': self.release,
            'brickname': self.brickname,
            'brickid': self.brickid,
            'brick_objid': self.brick_objid,
            'morphtype': self.morphtype,
            'ebv': self.ebv,
            'flux_g': self.flux_g,
            'flux_r': self.flux_r,
            'flux_z': self.flux_z,
            'flux_w1': self.flux_w1,
            'flux_w2': self.flux_w2,
            'flux_ivar_g': self.flux_ivar_g,
            'flux_ivar_r': self.flux_ivar_r,
            'flux_ivar_z': self.flux_ivar_z,
            'flux_ivar_w1': self.flux_ivar_w1,
            'flux_ivar_w2': self.flux_ivar_w2,
            'fiberflux_g': self.fiberflux_g,
            'fiberflux_r': self.fiberflux_r,
            'fiberflux_z': self.fiberflux_z,
            'fibertotflux_g': self.fibertotflux_g,
            'fibertotflux_r': self.fibertotflux_r,
            'fibertotflux_z': self.fibertotflux_z,
            'maskbits': self.maskbits,
            'sersic': self.sersic,
            'shape_r': self.shape_r,
            'shape_e1': self.shape_e1,
            'shape_e2': self.shape_e2,
            'ref_id': self.ref_id,
            'ref_cat': self.ref_cat,
            'gaia_phot_g_mean_mag': self.gaia_phot_g_mean_mag,
            'gaia_phot_bp_mean_mag': self.gaia_phot_bp_mean_mag,
            'gaia_phot_rp_mean_mag': self.gaia_phot_rp_mean_mag,
            'parallax': self.parallax,
            'photsys': self.photsys,
            'priority_init': self.priority_init,
            'numobs_init': self.numobs_init,
            'cmx_target': self.cmx_target,
            'sv1_desi_target': self.sv1_desi_target,
            'sv1_bgs_target': self.sv1_bgs_target,
            'sv1_mws_target': self.sv1_mws_target,
            'sv1_scnd_target': self.sv1_scnd_target,
            'sv2_desi_target': self.sv2_desi_target,
            'sv2_bgs_target': self.sv2_bgs_target,
            'sv2_mws_target': self.sv2_mws_target,
            'sv2_scnd_target': self.sv2_scnd_target,
            'sv3_desi_target': self.sv3_desi_target,
            'sv3_bgs_target': self.sv3_bgs_target,
            'sv3_mws_target': self.sv3_mws_target,
            'sv3_scnd_target': self.sv3_scnd_target,
            'desi_target': self.desi_target,
            'bgs_target': self.bgs_target,
            'mws_target': self.mws_target,
            'scnd_target': self.scnd_target,
            'plate_ra': self.plate_ra,
            'plate_dec': self.plate_dec,
            'coadd_numexp': self.coadd_numexp,
            'coadd_exptime': self.coadd_exptime,
            'coadd_numnight': self.coadd_numnight,
            'coadd_numtile': self.coadd_numtile,
            'mean_delta_x': self.mean_delta_x,
            'rms_delta_x': self.rms_delta_x,
            'mean_delta_y': self.mean_delta_y,
            'rms_delta_y': self.rms_delta_y,
            'mean_fiber_ra': self.mean_fiber_ra,
            'std_fiber_ra': self.std_fiber_ra,
            'mean_fiber_dec': self.mean_fiber_dec,
            'std_fiber_dec': self.std_fiber_dec,
            'mean_psf_to_fiber_specflux': self.mean_psf_to_fiber_specflux,
            'tsnr2_gpbdark_b': self.tsnr2_gpbdark_b,
            'tsnr2_elg_b': self.tsnr2_elg_b,
            'tsnr2_gpbbright_b': self.tsnr2_gpbbright_b,
            'tsnr2_lya_b': self.tsnr2_lya_b,
            'tsnr2_bgs_b': self.tsnr2_bgs_b,
            'tsnr2_gpbbackup_b': self.tsnr2_gpbbackup_b,
            'tsnr2_qso_b': self.tsnr2_qso_b,
            'tsnr2_lrg_b': self.tsnr2_lrg_b,
            'tsnr2_gpbdark_r': self.tsnr2_gpbdark_r,
            'tsnr2_elg_r': self.tsnr2_elg_r,
            'tsnr2_gpbbright_r': self.tsnr2_gpbbright_r,
            'tsnr2_lya_r': self.tsnr2_lya_r,
            'tsnr2_bgs_r': self.tsnr2_bgs_r,
            'tsnr2_gpbbackup_r': self.tsnr2_gpbbackup_r,
            'tsnr2_qso_r': self.tsnr2_qso_r,
            'tsnr2_lrg_r': self.tsnr2_lrg_r,
            'tsnr2_gpbdark_z': self.tsnr2_gpbdark_z,
            'tsnr2_elg_z': self.tsnr2_elg_z,
            'tsnr2_gpbbright_z': self.tsnr2_gpbbright_z,
            'tsnr2_lya_z': self.tsnr2_lya_z,
            'tsnr2_bgs_z': self.tsnr2_bgs_z,
            'tsnr2_gpbbackup_z': self.tsnr2_gpbbackup_z,
            'tsnr2_qso_z': self.tsnr2_qso_z,
            'tsnr2_lrg_z': self.tsnr2_lrg_z,
            'tsnr2_gpbdark': self.tsnr2_gpbdark,
            'tsnr2_elg': self.tsnr2_elg,
            'tsnr2_gpbbright': self.tsnr2_gpbbright,
            'tsnr2_lya': self.tsnr2_lya,
            'tsnr2_bgs': self.tsnr2_bgs,
            'tsnr2_gpbbackup': self.tsnr2_gpbbackup,
            'tsnr2_qso': self.tsnr2_qso,
            'tsnr2_lrg': self.tsnr2_lrg,
            'sv_nspec': self.sv_nspec,
            'sv_primary': self.sv_primary,
            'zcat_nspec': self.zcat_nspec,
            'zcat_primary': self.zcat_primary
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
