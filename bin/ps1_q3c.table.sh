#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS ps1_q3c;
CREATE TABLE ps1_q3c (
  pid serial PRIMARY KEY,
  objid bigint,
  psps_objid bigint,
  ra double precision NOT NULL,
  dec double precision NOT NULL,
  l double precision,
  b double precision,
  obj_class VARCHAR(8),
  prob_galaxy double precision,
  prob_star double precision,
  prob_qso double precision,
  extra_class double precision,
  celld_class double precision,
  cellid_class integer,
  z_phot double precision,
  z_err double precision,
  z_zero double precision,
  extra_photoz integer,
  celld_photoz double precision,
  cellid_photoz integer,
  ps_score double precision
);
ALTER SEQUENCE ps1_q3c_pid_seq AS bigint;
ALTER SEQUENCE ps1_q3c_pid_seq MAXVALUE 9223372036854775807;
ALTER TABLE ps1 ALTER COLUMN pid TYPE bigint;
CREATE INDEX idx_ps1_q3c_objid ON ps1(objid);
CREATE INDEX ON ps1_q3c (q3c_ang2ipix(ra, dec));
CLUSTER ps1_q3c_q3c_ang2ipix_idx ON ps1_q3c;
ANALYZE VERBOSE ps1_q3c;
END_TABLE
