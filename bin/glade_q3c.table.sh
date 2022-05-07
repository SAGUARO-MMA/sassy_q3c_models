#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS glade_q3c;
CREATE TABLE glade_q3c (
  gid serial PRIMARY KEY,
  pgc integer,
  gwgc VARCHAR(128),
  hyperleda VARCHAR(128),
  twomass VARCHAR(128),
  sdss VARCHAR(128),
  flag1 VARCHAR(1),
  ra double precision,
  dec double precision,
  dist double precision,
  disterr double precision,
  z double precision,
  b double precision,
  b_err double precision,
  b_abs double precision,
  j double precision,
  j_err double precision,
  h double precision,
  h_err double precision,
  k double precision,
  k_err double precision,
  flag2 integer,
  flag3 integer);
END_TABLE
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_Q3C
  CREATE INDEX ON glade_q3c (q3c_ang2ipix(ra, dec));
  CLUSTER glade_q3c_q3c_ang2ipix_idx ON glade_q3c;
  ANALYZE VERBOSE glade_q3c;
END_Q3C

