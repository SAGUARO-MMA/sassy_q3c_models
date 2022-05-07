#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS ztf_q3c;
CREATE TABLE ztf_q3c (
  aimage double precision,
  aimagerat double precision,
  alert_candid bigint,
  avro VARCHAR(256) NOT NULL,
  bimage double precision,
  bimagerat double precision,
  candid bigint,
  chinr double precision,
  chipsf double precision,
  classtar double precision,
  clrcoeff double precision,
  clrcounc double precision,
  clrmed double precision,
  clrrms double precision,
  cutoutdifference VARCHAR(192),
  cutoutscience VARCHAR(192),
  cutouttemplate VARCHAR(192),
  dec double precision NOT NULL,
  decnr double precision NOT NULL,
  deltamaglatest double precision,
  deltamagref double precision,
  diffmaglim double precision,
  distpsnr1 double precision,
  distpsnr2 double precision,
  distpsnr3 double precision,
  distnr double precision,
  drb double precision,
  drbversion VARCHAR(64),
  dsnrms double precision,
  dsdiff double precision,
  elong double precision,
  exptime double precision,
  fid integer NOT NULL,
  filtername VARCHAR(1) NOT NULL,
  field integer,
  fwhm double precision,
  gal_b double precision NOT NULL,
  gal_l double precision NOT NULL,
  isdiffpos VARCHAR(1) NOT NULL,
  iso VARCHAR(32) NOT NULL,
  jd double precision NOT NULL,
  jdendhist double precision,
  jdendref double precision NOT NULL,
  jdstarthist double precision,
  jdstartref double precision NOT NULL,
  magap double precision,
  magapbig double precision,
  magdiff double precision,
  magfromlim double precision,
  maggaia double precision,
  maggaiabright double precision,
  magnr double precision,
  magpsf double precision NOT NULL,
  magzpsci double precision,
  magzpscirms double precision,
  magzpsciunc double precision,
  mindtoedge double precision,
  nbad integer,
  ncovhist integer NOT NULL,
  ndethist integer NOT NULL,
  neargaia double precision,
  neargaiabright double precision,
  nframesref integer NOT NULL,
  nid integer,
  nmatches integer,
  nmtchps integer NOT NULL,
  nneg integer,
  objectidps1 bigint,
  objectidps2 bigint,
  objectidps3 bigint,
  oid VARCHAR(64) NOT NULL,
  pdiffimfilename VARCHAR(256),
  pid bigint NOT NULL,
  programid integer NOT NULL,
  programpi VARCHAR(128),
  publisher VARCHAR(128) NOT NULL,
  ra double precision NOT NULL,
  ranr double precision NOT NULL,
  rb double precision,
  rbversion VARCHAR(64) NOT NULL,
  rcid integer,
  rfid bigint NOT NULL,
  scorr double precision,
  seeratio double precision,
  sgmag1 double precision,
  sgmag2 double precision,
  sgmag3 double precision,
  sgscore1 double precision,
  sgscore2 double precision,
  sgscore3 double precision,
  sharpnr double precision,
  sigmagap double precision,
  sigmagapbig double precision,
  sigmagnr double precision,
  sigmapsf double precision NOT NULL,
  simag1 double precision,
  simag2 double precision,
  simag3 double precision,
  sky double precision,
  srmag1 double precision,
  srmag2 double precision,
  srmag3 double precision,
  ssdistnr double precision,
  ssmagnr double precision,
  ssnamenr VARCHAR(128) NOT NULL,
  ssnrms double precision,
  sumrat double precision,
  szmag1 double precision,
  szmag2 double precision,
  szmag3 double precision,
  tblid bigint,
  tooflag smallint NOT NULL,
  xpos double precision,
  ypos double precision,
  zid serial PRIMARY KEY,
  zpclrcov double precision,
  zpmed double precision);
END_TABLE
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_Q3C
  CREATE INDEX idx_ztf_q3c_oid ON ztf_q3c(oid);
  CREATE INDEX idx_ztf_q3c_alert_candid ON ztf_q3c(alert_candid);
  CREATE INDEX idx_ztf_q3c_ra ON ztf_q3c(ra);
  CREATE INDEX idx_ztf_q3c_dec ON ztf_q3c(dec);
  CREATE INDEX idx_ztf_q3c_jd ON ztf_q3c(jd);
  CREATE INDEX idx_ztf_q3c_magpsf ON ztf_q3c(magpsf);
  CREATE INDEX idx_ztf_q3c_sigmapsf ON ztf_q3c(sigmapsf);
  CREATE INDEX idx_ztf_q3c_deltamaglatest ON ztf_q3c(deltamaglatest);
  CREATE INDEX idx_ztf_q3c_deltamagref ON ztf_q3c(deltamagref);
  CREATE INDEX idx_ztf_q3c_magap ON ztf_q3c(magap);
  CREATE INDEX idx_ztf_q3c_fwhm ON ztf_q3c(fwhm);
  CREATE INDEX idx_ztf_q3c_classtar ON ztf_q3c(classtar);
  CREATE INDEX idx_ztf_q3c_elong ON ztf_q3c(elong);
  CREATE INDEX idx_ztf_q3c_nbad ON ztf_q3c(nbad);
  CREATE INDEX idx_ztf_q3c_rb ON ztf_q3c(rb);
  CREATE INDEX idx_ztf_q3c_drb ON ztf_q3c(drb);
  CREATE INDEX idx_ztf_q3c_ssdistnr ON ztf_q3c(ssdistnr);
  CREATE INDEX idx_ztf_q3c_gal_l ON ztf_q3c(gal_l);
  CREATE INDEX idx_ztf_q3c_gal_b ON ztf_q3c(gal_b);
  CREATE INDEX idx_ztf_q3c_objectisps1 ON ztf_q3c(objectisps1);
  CREATE INDEX idx_ztf_q3c_objectisps2 ON ztf_q3c(objectisps2);
  CREATE INDEX idx_ztf_q3c_objectisps3 ON ztf_q3c(objectisps3);
  CREATE INDEX ON ztf_q3c (q3c_ang2ipix(ra, dec));
  CLUSTER ztf_q3c_q3c_ang2ipix_idx ON ztf_q3c;
  ANALYZE VERBOSE ztf_q3c;
END_Q3C
