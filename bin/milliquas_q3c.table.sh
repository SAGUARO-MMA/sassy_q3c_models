#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS milliquas_q3c;
CREATE TABLE milliquas_q3c (
  mid serial PRIMARY KEY,
  ra double precision,
  dec double precision,
  name VARCHAR(32),
  objtype VARCHAR(8),
  rmag double precision,
  bmag double precision,
  comment VARCHAR(8),
  rpsf VARCHAR(1),
  bpsf VARCHAR(1),
  z double precision,
  namecit VARCHAR(8),
  zcit VARCHAR(8),
  qpct integer,
  xname VARCHAR(32),
  rname VARCHAR(32),
  lobe1 VARCHAR(32),
  lobe2 VARCHAR(32));
END_TABLE
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_Q3C
  CREATE INDEX ON milliquas_q3c (q3c_ang2ipix(ra, dec));
  CLUSTER milliquas_q3c_q3c_ang2ipix_idx ON milliquas_q3c;
  ANALYZE VERBOSE milliquas_q3c;
END_Q3C
