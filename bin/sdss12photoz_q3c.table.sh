#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS sdss12photoz_q3c;
CREATE TABLE sdss12photoz_q3c (
  sid serial PRIMARY KEY,
  ra double precision,
  dec double precision,
  mode integer,
  q_mode VARCHAR(1),
  classifier integer,
  sdss12 VARCHAR(24),
  m_sdss12 VARCHAR(1),
  sdssid VARCHAR(32),
  objid VARCHAR(24),
  specid VARCHAR(32),
  spobjid VARCHAR(24),
  parentid VARCHAR(24),
  flags VARCHAR(24),
  status integer,
  e_ra double precision,
  e_dec double precision,
  obsdate double precision,
  quality integer,
  umag double precision,
  e_umag double precision,
  gmag double precision,
  e_gmag double precision,
  rmag double precision,
  e_rmag double precision,
  imag double precision,
  e_imag double precision,
  zmag double precision,
  e_zmag double precision,
  zsp double precision,
  e_zsp double precision,
  f_zsp integer,
  vdisp double precision,
  e_vdisp double precision,
  spinst VARCHAR(24),
  sptype VARCHAR(24),
  spclass VARCHAR(24),
  spubclass VARCHAR(24),
  spsignal double precision,
  u_flags VARCHAR(24),
  u_prob integer,
  u_photo integer,
  u_date double precision,
  u_prime_mag double precision,
  e_u_prime_mag double precision,
  u_pmag double precision,
  e_u_pmag double precision,
  u_upmag double precision,
  e_u_upmag double precision,
  u_prad double precision,
  e_u_prad double precision,
  u_ora double precision,
  u_odec double precision,
  u_dvrad double precision,
  u_dvell double precision,
  u_pa double precision,
  g_flags VARCHAR(24),
  g_prob integer,
  g_photo integer,
  g_date double precision,
  g_prime_mag double precision,
  e_g_prime_mag double precision,
  g_pmag double precision,
  e_g_pmag double precision,
  g_upmag double precision,
  e_g_upmag double precision,
  g_prad double precision,
  e_g_prad double precision,
  g_ora double precision,
  g_odec double precision,
  g_dvrad double precision,
  g_dvell double precision,
  g_pa double precision,
  r_flags VARCHAR(24),
  r_prob integer,
  r_photo integer,
  r_date double precision,
  r_prime_mag double precision,
  e_r_prime_mag double precision,
  r_pmag double precision,
  e_r_pmag double precision,
  r_upmag double precision,
  e_r_upmag double precision,
  r_prad double precision,
  e_r_prad double precision,
  r_ora double precision,
  r_odec double precision,
  r_dvrad double precision,
  r_dvell double precision,
  r_pa double precision,
  i_flags VARCHAR(24),
  i_prob integer,
  i_photo integer,
  i_date double precision,
  i_prime_mag double precision,
  e_i_prime_mag double precision,
  i_pmag double precision,
  e_i_pmag double precision,
  i_upmag double precision,
  e_i_upmag double precision,
  i_prad double precision,
  e_i_prad double precision,
  i_ora double precision,
  i_odec double precision,
  i_dvrad double precision,
  i_dvell double precision,
  i_pa double precision,
  z_flags VARCHAR(24),
  z_prob integer,
  z_photo integer,
  z_date double precision,
  z_prime_mag double precision,
  e_z_prime_mag double precision,
  z_pmag double precision,
  e_z_pmag double precision,
  z_upmag double precision,
  e_z_upmag double precision,
  z_prad double precision,
  e_z_prad double precision,
  z_ora double precision,
  z_odec double precision,
  z_dvrad double precision,
  z_dvell double precision,
  z_pa double precision,
  pmra double precision,
  e_pmra double precision,
  pmdec double precision,
  e_pmdec double precision,
  sigra double precision,
  sigdec double precision,
  m integer,
  n integer,
  g_o_plate double precision,
  r_e_plate double precision,
  g_j_plate double precision,
  r_f_plate double precision,
  i_n_plate double precision,
  zph double precision,
  e_zph double precision,
  ave_zph double precision,
  chi2 double precision,
  abs_u_mag double precision,
  abs_g_mag double precision,
  abs_r_mag double precision,
  abs_i_mag double precision,
  abs_z_mag double precision);
END_TABLE
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_Q3C
  CREATE INDEX ON sdss12photoz_q3c (q3c_ang2ipix(ra, dec));
  CLUSTER sdss12photoz_q3c_q3c_ang2ipix_idx ON sdss12photoz_q3c;
  CREATE INDEX idx_sdss12photoz_q3c_umag ON sdss12photoz_q3c(umag);
  CREATE INDEX idx_sdss12photoz_q3c_u_prime_mag ON sdss12photoz_q3c(u_prime_mag);
  CREATE INDEX idx_sdss12photoz_q3c_u_pmag ON sdss12photoz_q3c(u_pmag);
  CREATE INDEX idx_sdss12photoz_q3c_u_upmag ON sdss12photoz_q3c(u_upmag);
  CREATE INDEX idx_sdss12photoz_q3c_abs_u_mag ON sdss12photoz_q3c(abs_u_mag);
  CREATE INDEX idx_sdss12photoz_q3c_gmag ON sdss12photoz_q3c(gmag);
  CREATE INDEX idx_sdss12photoz_q3c_g_prime_mag ON sdss12photoz_q3c(g_prime_mag);
  CREATE INDEX idx_sdss12photoz_q3c_g_pmag ON sdss12photoz_q3c(g_pmag);
  CREATE INDEX idx_sdss12photoz_q3c_g_upmag ON sdss12photoz_q3c(g_upmag);
  CREATE INDEX idx_sdss12photoz_q3c_abs_g_mag ON sdss12photoz_q3c(abs_g_mag);
  CREATE INDEX idx_sdss12photoz_q3c_rmag ON sdss12photoz_q3c(rmag);
  CREATE INDEX idx_sdss12photoz_q3c_r_prime_mag ON sdss12photoz_q3c(r_prime_mag);
  CREATE INDEX idx_sdss12photoz_q3c_r_pmag ON sdss12photoz_q3c(r_pmag);
  CREATE INDEX idx_sdss12photoz_q3c_r_upmag ON sdss12photoz_q3c(r_upmag);
  CREATE INDEX idx_sdss12photoz_q3c_abs_r_mag ON sdss12photoz_q3c(abs_r_mag);
  CREATE INDEX idx_sdss12photoz_q3c_imag ON sdss12photoz_q3c(imag);
  CREATE INDEX idx_sdss12photoz_q3c_i_prime_mag ON sdss12photoz_q3c(i_prime_mag);
  CREATE INDEX idx_sdss12photoz_q3c_i_pmag ON sdss12photoz_q3c(i_pmag);
  CREATE INDEX idx_sdss12photoz_q3c_i_upmag ON sdss12photoz_q3c(i_upmag);
  CREATE INDEX idx_sdss12photoz_q3c_abs_i_mag ON sdss12photoz_q3c(abs_i_mag);
  CREATE INDEX idx_sdss12photoz_q3c_zmag ON sdss12photoz_q3c(zmag);
  CREATE INDEX idx_sdss12photoz_q3c_z_prime_mag ON sdss12photoz_q3c(z_prime_mag);
  CREATE INDEX idx_sdss12photoz_q3c_z_pmag ON sdss12photoz_q3c(z_pmag);
  CREATE INDEX idx_sdss12photoz_q3c_z_upmag ON sdss12photoz_q3c(z_upmag);
  CREATE INDEX idx_sdss12photoz_q3c_abs_z_mag ON sdss12photoz_q3c(abs_z_mag);
  CREATE INDEX idx_sdss12photoz_q3c_zsp ON sdss12photoz_q3c(zsp);
  CREATE INDEX idx_sdss12photoz_q3c_zph ON sdss12photoz_q3c(zph);
  CREATE INDEX idx_sdss12photoz_q3c_ave_zph ON sdss12photoz_q3c(ave_zph);
  ANALYZE VERBOSE sdss12photoz_q3c;
END_Q3C
