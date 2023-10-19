#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -


PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS ztf_fp_q3c;
CREATE TABLE ztf_fp_q3c (
  fpid serial PRIMARY KEY,
  field integer,
  rcid integer,
  fid integer NOT NULL,
  pid bigint NOT NULL,
  rfid bigint NOT NULL,
  sciinpseeing double precision,
  scibckgnd double precision,
  scisigpix double precision,
  magzpsci double precision,
  magzpsciunc double precision,
  magzpscirms double precision,
  clrcoeff double precision,
  clrcounc double precision,
  exptime double precision,
  adpctdif1 double precision,
  adpctdif2 double precision,
  diffmaglim double precision,
  programid integer NOT NULL,
  jd double precision NOT NULL,
  forcediffimflux double precision,
  forcediffimfluxunc double precision,
  procstatus VARCHAR(16),
  distnr double precision,
  ranr double precision NOT NULL,
  decnr double precision NOT NULL,
  magnr double precision,
  sigmagnr double precision,
  chinr double precision,
  sharpnr double precision
);
ALTER SEQUENCE ztf_fp_q3c_fpid_seq AS bigint;
ALTER SEQUENCE ztf_fp_q3c_fpid_seq MAXVALUE 9223372036854775807;
ALTER TABLE ztf_fp_q3c ALTER COLUMN fpid TYPE bigint;
CREATE INDEX idx_ztf_fp_q3c_jd ON ztf_fp_q3c(jd);
CREATE INDEX ON ztf_fp_q3c (q3c_ang2ipix(ranr, decnr));
CLUSTER ztf_fp_q3c_q3c_ang2ipix_idx ON ztf_fp_q3c;
ANALYZE VERBOSE ztf_fp_q3c;
END_TABLE
