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
  pid bigserial PRIMARY KEY,
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
  ps_score double precision,
  objname VARCHAR(64),
  objinfoflag integer,
  qualityflag integer,
  ndetections integer,
  ramean double precision,
  rameanerr double precision,
  decmean double precision,
  decmeanerr double precision,
  gmeanpsfmag double precision,
  gmeanpsfmagerr double precision,
  rmeanpsfmag double precision,
  rmeanpsfmagerr double precision,
  imeanpsfmag double precision,
  imeanpsfmagerr double precision,
  zmeanpsfmag double precision,
  zmeanpsfmagerr double precision,
  ymeanpsfmag double precision,
  ymeanpsfmagerr double precision
);
 objname        | character varying(64) |           |          | ''::character varying                | extended |              |
 objinfoflag    | integer               |           |          | '-999'::integer                      | plain    |              |
 qualityflag    | integer               |           |          | '-999'::integer                      | plain    |              |
 ndetections    | integer               |           |          | '-999'::integer                      | plain    |              |
 ramean         | double precision      |           |          | '-999.0'::numeric                    | plain    |              |
 rameanerr      | double precision      |           |          | '-999.0'::numeric                    | plain    |              |
 decmean        | double precision      |           |          | '-999.0'::numeric                    | plain    |              |
 decmeanerr     | double precision      |           |          | '-999.0'::numeric                    | plain    |              |
 gmeanpsfmag    | double precision      |           |          | '-999.0'::numeric                    | plain    |              |
 gmeanpsfmagerr | double precision      |           |          | '-999.0'::numeric                    | plain    |              |
 rmeanpsfmag    | double precision      |           |          | '-999.0'::numeric                    | plain    |              |
 rmeanpsfmagerr | double precision      |           |          | '-999.0'::numeric                    | plain    |              |
 imeanpsfmag    | double precision      |           |          | '-999.0'::numeric                    | plain    |              |
 imeanpsfmagerr | double precision      |           |          | '-999.0'::numeric                    | plain    |              |
 zmeanpsfmag    | double precision      |           |          | '-999.0'::numeric                    | plain    |              |
 zmeanpsfmagerr | double precision      |           |          | '-999.0'::numeric                    | plain    |              |
 ymeanpsfmag    | double precision      |           |          | '-999.0'::numeric                    | plain    |              |
 ymeanpsfmagerr | double precision      |           |          | '-999.0'::numeric                    | plain    |              |
CREATE INDEX idx_ps1_q3c_objid ON ps1_q3c(objid);
CREATE INDEX idx_ps1_q3c_ps_score ON ps1_q3c(ps_score);
CREATE INDEX ON ps1_q3c (q3c_ang2ipix(ra, dec));
CREATE INDEX idx_ps1_q3c_gmeanpsfmag ON ps1_q3c(gmeanpsfmag);
CREATE INDEX idx_ps1_q3c_imeanpsfmag ON ps1_q3c(imeanpsfmag);
CREATE INDEX idx_ps1_q3c_ymeanpsfmag ON ps1_q3c(ymeanpsfmag);
CREATE INDEX idx_ps1_q3c_zmeanpsfmag ON ps1_q3c(zmeanpsfmag);
CLUSTER ps1_q3c_q3c_ang2ipix_idx ON ps1_q3c;
ANALYZE VERBOSE ps1_q3c;
END_TABLE
