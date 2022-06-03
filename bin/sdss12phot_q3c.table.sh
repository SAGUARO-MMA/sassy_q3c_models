#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS sdss12phot_q3c;
CREATE TABLE sdss12phot_q3c (
  sid serial PRIMARY KEY,
  ra double precision,
  dec double precision,
  mode integer,
  q_mode VARCHAR(1),
  classifier integer,
  sdss12 VARCHAR(24),
  m_sdss12 VARCHAR(1),
  obsdate double precision,
  quality integer,
  umag  double precision,
  e_umag  double precision,
  gmag  double precision,
  e_gmag  double precision,
  rmag  double precision,
  e_rmag  double precision,
  imag  double precision,
  e_imag  double precision,
  zmag  double precision,
  e_zmag  double precision,
  zsp  double precision,
  zph  double precision,
  e_zph  double precision,
  nnzph double precision);
END_TABLE
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_Q3C
  CREATE INDEX ON sdss12phot_q3c (q3c_ang2ipix(ra, dec));
  CLUSTER sdss12phot_q3c_q3c_ang2ipix_idx ON sdss12phot_q3c;
  ANALYZE VERBOSE sdss12phot_q3c;
END_Q3C
