#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS asassn_q3c;
CREATE TABLE asassn_q3c (
  aid serial PRIMARY KEY,
  asassn_id VARCHAR(40),
  source_id VARCHAR(20),
  asassn_name VARCHAR(30),
  other_names VARCHAR(32),
  ra double precision,
  dec double precision,
  l double precision,
  b double precision,
  mean_vmag double precision,
  amplitude double precision,
  period double precision,
  variable_type VARCHAR(10),
  class_probability double precision,
  lksl_statistic double precision,
  rfr_score double precision,
  epoch_hjd double precision,
  gdr2_id bigint,
  phot_g_mean_mag double precision,
  e_phot_g_mean_mag double precision,
  phot_bp_mean_mag double precision,
  e_phot_bp_mean_mag double precision,
  phot_rp_mean_mag double precision,
  e_phot_rp_mean_mag double precision,
  bp_rp double precision,
  parallax double precision,
  parallax_error double precision,
  parallax_over_error double precision,
  pmra double precision,
  pmra_error double precision,
  pmdec double precision,
  pmdec_error double precision,
  vt double precision,
  dist double precision,
  allwise_id VARCHAR(20),
  j_mag double precision,
  e_j_mag double precision,
  h_mag double precision,
  e_h_mag double precision,
  k_mag double precision,
  e_k_mag double precision,
  w1_mag double precision,
  e_w1_mag double precision,
  w2_mag double precision,
  e_w2_mag double precision,
  w3_mag double precision,
  e_w3_mag double precision,
  w4_mag double precision,
  e_w4_mag double precision,
  j_k double precision,
  w1_w2 double precision,
  w3_w4 double precision,
  apass_dr9_id bigint,
  apass_vmag double precision,
  e_apass_vmag double precision,
  apass_bmag double precision,
  e_apass_bmag double precision,
  apass_gpmag double precision,
  e_apass_gpmag double precision,
  apass_rpmag double precision,
  e_apass_rpmag double precision,
  apass_ipmag double precision,
  e_apass_ipmag double precision,
  b_v double precision,
  e_b_v double precision,
  vector_x double precision,
  vector_y double precision,
  vector_z double precision,
  reference VARCHAR(45),
  periodic boolean,
  classified boolean,
  asassn_discovery boolean,
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  edr3_source_id VARCHAR(25),
  galex_id VARCHAR(25),
  fuvmag double precision,
  e_fuvmag double precision,
  nuvmag double precision,
  e_nuvmag double precision,
  tic_id VARCHAR(16),
  pm double precision,
  ruwe double precision);
END_TABLE
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_Q3C
  CREATE INDEX ON asassn_q3c (q3c_ang2ipix(ra, dec));
  CLUSTER asassn_q3c_q3c_ang2ipix_idx ON asassn_q3c;
  ANALYZE VERBOSE asassn_q3c;
END_Q3C


