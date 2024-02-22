#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS desi_spec_q3c;
CREATE TABLE desi_spec_q3c (
  did serial PRIMARY KEY,
  targetid bigint,
  survey VARCHAR(7),
  program VARCHAR(6),
  healpix integer,
  spgrpval integer,
  z double precision,
  zerr double precision,
  zwarn bigint,
  chi2 double precision,
  coeff_0 double precision,
  coeff_1 double precision,
  coeff_2 double precision,
  coeff_3 double precision,
  coeff_4 double precision,
  coeff_5 double precision,
  coeff_6 double precision,
  coeff_7 double precision,
  coeff_8 double precision,
  coeff_9 double precision,
  npixels bigint,
  spectype VARCHAR(6),
  subtype VARCHAR(20),
  ncoeff bigint,
  deltachi2 double precision,
  coadd_fiberstatus integer,
  target_ra double precision,
  target_dec double precision,
  pmra double precision,
  pmdec double precision,
  ref_epoch double precision,
  fa_target bigint,
  fa_type integer,
  objtype VARCHAR(3),
  subpriority double precision,
  obsconditions integer,
  release integer,
  brickname VARCHAR(8),
  brickid integer,
  brick_objid integer,
  morphtype VARCHAR(4),
  ebv double precision,
  flux_g double precision,
  flux_r double precision,
  flux_z double precision,
  flux_w1 double precision,
  flux_w2 double precision,
  flux_ivar_g double precision,
  flux_ivar_r double precision,
  flux_ivar_z double precision,
  flux_ivar_w1 double precision,
  flux_ivar_w2 double precision,
  fiberflux_g double precision,
  fiberflux_r double precision,
  fiberflux_z double precision,
  fibertotflux_g double precision,
  fibertotflux_r double precision,
  fibertotflux_z double precision,
  maskbits integer,
  sersic double precision,
  shape_r double precision,
  shape_e1 double precision,
  shape_e2 double precision,
  ref_id bigint,
  ref_cat VARCHAR(2),
  gaia_phot_g_mean_mag double precision,
  gaia_phot_bp_mean_mag double precision,
  gaia_phot_rp_mean_mag double precision,
  parallax double precision,
  photsys VARCHAR(1),
  priority_init bigint,
  numobs_init bigint,
  cmx_target bigint,
  sv1_desi_target bigint,
  sv1_bgs_target bigint,
  sv1_mws_target bigint,
  sv1_scnd_target bigint,
  sv2_desi_target bigint,
  sv2_bgs_target bigint,
  sv2_mws_target bigint,
  sv2_scnd_target bigint,
  sv3_desi_target bigint,
  sv3_bgs_target bigint,
  sv3_mws_target bigint,
  sv3_scnd_target bigint,
  desi_target bigint,
  bgs_target bigint,
  mws_target bigint,
  scnd_target bigint,
  plate_ra double precision,
  plate_dec double precision,
  coadd_numexp integer,
  coadd_exptime double precision,
  coadd_numnight integer,
  coadd_numtile integer,
  mean_delta_x double precision,
  rms_delta_x double precision,
  mean_delta_y double precision,
  rms_delta_y double precision,
  mean_fiber_ra double precision,
  std_fiber_ra double precision,
  mean_fiber_dec double precision,
  std_fiber_dec double precision,
  mean_psf_to_fiber_specflux double precision,
  tsnr2_gpbdark_b double precision,
  tsnr2_elg_b double precision,
  tsnr2_gpbbright_b double precision,
  tsnr2_lya_b double precision,
  tsnr2_bgs_b double precision,
  tsnr2_gpbbackup_b double precision,
  tsnr2_qso_b double precision,
  tsnr2_lrg_b double precision,
  tsnr2_gpbdark_r double precision,
  tsnr2_elg_r double precision,
  tsnr2_gpbbright_r double precision,
  tsnr2_lya_r double precision,
  tsnr2_bgs_r double precision,
  tsnr2_gpbbackup_r double precision,
  tsnr2_qso_r double precision,
  tsnr2_lrg_r double precision,
  tsnr2_gpbdark_z double precision,
  tsnr2_elg_z double precision,
  tsnr2_gpbbright_z double precision,
  tsnr2_lya_z double precision,
  tsnr2_bgs_z double precision,
  tsnr2_gpbbackup_z double precision,
  tsnr2_qso_z double precision,
  tsnr2_lrg_z double precision,
  tsnr2_gpbdark double precision,
  tsnr2_elg double precision,
  tsnr2_gpbbright double precision,
  tsnr2_lya double precision,
  tsnr2_bgs double precision,
  tsnr2_gpbbackup double precision,
  tsnr2_qso double precision,
  tsnr2_lrg double precision,
  sv_nspec integer,
  sv_primary boolean,
  zcat_nspec integer,
  zcat_primary boolean
);
END_TABLE
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_Q3C
  CREATE INDEX idx_desi_spec_q3c_z ON desi_spec_q3c(z);
  CREATE INDEX ON desi_spec_q3c (q3c_ang2ipix(target_ra, target_dec));
  CLUSTER desi_spec_q3c_q3c_ang2ipix_idx ON desi_spec_q3c;
  ANALYZE VERBOSE desi_spec_q3c;
END_Q3C