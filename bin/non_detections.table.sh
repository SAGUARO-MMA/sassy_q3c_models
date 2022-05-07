#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS non_detections;
CREATE TABLE non_detections (
  nid serial PRIMARY KEY,
  oid VARCHAR(64) NOT NULL,
  diffmaglim double precision NOT NULL,
  jd double precision NOT NULL,
  fid integer NOT NULL);
ALTER SEQUENCE non_detections_nid_seq AS bigint;
ALTER SEQUENCE non_detections_nid_seq MAXVALUE 9223372036854775807;
ALTER TABLE non_detections ALTER COLUMN nid TYPE bigint;
CREATE INDEX idx_non_detections_jd ON non_detections(jd);
CREATE INDEX idx_non_detections_oid ON non_detections(oid);
ANALYZE VERBOSE non_detections;
END_TABLE
