#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS gwgc_q3c;
CREATE TABLE gwgc_q3c (
  gid serial PRIMARY KEY,
  pgc integer,
  name VARCHAR(128) NOT NULL,
  rah double precision,
  ra double precision,
  dec double precision,
  tt double precision,
  b_app double precision,
  a double precision,
  e_a double precision,
  b double precision,
  e_b double precision,
  b_div_a double precision,
  e_b_div_a double precision,
  pa double precision,
  b_abs double precision,
  dist double precision,
  e_dist double precision,
  e_b_app double precision,
  e_b_abs double precision);
END_TABLE
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_Q3C
  CREATE INDEX ON gwgc_q3c (q3c_ang2ipix(ra, dec));
  CLUSTER gwgc_q3c_q3c_ang2ipix_idx ON gwgc_q3c;
  ANALYZE VERBOSE gwgc_q3c;
END_Q3C
