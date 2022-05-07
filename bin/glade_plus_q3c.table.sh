#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS glade_plus_q3c;
CREATE TABLE glade_plus_q3c (
  gid serial PRIMARY KEY,
  gn integer,
  pgc integer,
  gwgc VARCHAR(64),
  hyperleda VARCHAR(64),
  twomass VARCHAR(64),
  wise VARCHAR(64),
  sdss VARCHAR(64),
  o_flag VARCHAR(1),
  ra double precision,
  dec double precision,
  b double precision,
  b_err double precision,
  b_flag integer,
  b_abs double precision,
  j double precision,
  j_err double precision,
  h double precision,
  h_err double precision,
  k double precision,
  k_err double precision,
  w1 double precision,
  w1_err double precision,
  w2 double precision,
  w2_err double precision,
  w1_flag integer,
  b_j double precision,
  b_j_err double precision,
  z_helio double precision,
  z_cmb double precision,
  z_flag integer,
  v_err double precision,
  z_err double precision,
  d_l double precision,
  d_l_err double precision,
  dist_flag integer,
  mstar double precision,
  mstar_err double precision,
  mrate double precision,
  mrate_err double precision);
END_TABLE
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_Q3C
  CREATE INDEX ON glade_plus_q3c (q3c_ang2ipix(ra, dec));
  CLUSTER glade_plus_q3c_q3c_ang2ipix_idx ON glade_plus_q3c;
  ANALYZE VERBOSE glade_plus_q3c;
END_Q3C
