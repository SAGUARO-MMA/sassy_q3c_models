#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS fermi_lat_q3c;
CREATE TABLE fermi_lat_q3c (
  fid serial PRIMARY KEY,
  name VARCHAR(24) NOT NULL,
  b double precision,
  l double precision,
  lbllac double precision,
  pbllac double precision,
  pfsrq double precision,
  classification VARCHAR(16),
  lbllaclit double precision,
  classlit VARCHAR(16),
  simbad VARCHAR(8),
  ra double precision,
  dec double precision);
END_TABLE
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_Q3C
  CREATE INDEX idx_fermi_lat_q3c_b ON fermi_lat_q3c(b);
  CREATE INDEX idx_fermi_lat_q3c_l ON fermi_lat_q3c(l);
  CREATE INDEX ON fermi_lat_q3c (q3c_ang2ipix(ra, dec));
  CLUSTER fermi_lat_q3c_q3c_ang2ipix_idx ON fermi_lat_q3c;
  ANALYZE VERBOSE fermi_lat_q3c;
END_Q3C
