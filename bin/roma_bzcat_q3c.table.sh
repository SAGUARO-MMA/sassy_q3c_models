#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -


PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS roma_bzcat_q3c;
CREATE TABLE roma_bzcat_q3c (
  rid serial PRIMARY KEY,
  name VARCHAR(16) NOT NULL,
  ra double precision,
  dec double precision,
  l double precision,
  b double precision,
  z double precision,
  z_err double precision,
  rmag double precision,
  classification VARCHAR(64),
  flux double precision,
  flux_143 double precision,
  flux_xray double precision,
  flux_fermi double precision,
  aro double precision);
END_TABLE
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_Q3C
  CREATE INDEX idx_roma_bzcat_q3c_rmag ON roma_bzcat_q3c(rmag);
  CREATE INDEX idx_roma_bzcat_q3c_z ON roma_bzcat_q3c(z);
  CREATE INDEX ON roma_bzcat_q3c (q3c_ang2ipix(ra, dec));
  CLUSTER roma_bzcat_q3c_q3c_ang2ipix_idx ON roma_bzcat_q3c;
  ANALYZE VERBOSE roma_bzcat_q3c;
END_Q3C
