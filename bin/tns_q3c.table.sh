#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS tns_q3c;
CREATE TABLE tns_q3c (
  tid serial PRIMARY KEY,
  objid integer,
  name_prefix VARCHAR(4),
  name VARCHAR(32),
  ra double precision,
  declination double precision,
  redshift double precision,
  typeid integer,
  objtype VARCHAR(32),
  reporting_groupid integer,
  reporting_group VARCHAR(32),
  source_groupid integer,
  source_group VARCHAR(32),
  discoverydate TIMESTAMP,
  discoverymag double precision,
  discmagfilter integer,
  filtername VARCHAR(24),
  reporters VARCHAR(2048),
  time_received TIMESTAMP,
  internal_names VARCHAR(256),
  creationdate TIMESTAMP,
  lastmodified TIMESTAMP);
END_TABLE
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_Q3C
  CREATE INDEX ON tns_q3c (q3c_ang2ipix(ra, declination));
  CLUSTER tns_q3c_q3c_ang2ipix_idx ON tns_q3c;
  ANALYZE VERBOSE tns_q3c;
END_Q3C
