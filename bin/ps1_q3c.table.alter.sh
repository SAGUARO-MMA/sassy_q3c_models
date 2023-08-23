#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
CREATE INDEX idx_ps1_q3c_gmeanpsfmag ON ps1_q3c(gmeanpsfmag);
CREATE INDEX idx_ps1_q3c_imeanpsfmag ON ps1_q3c(imeanpsfmag);
CREATE INDEX idx_ps1_q3c_ymeanpsfmag ON ps1_q3c(ymeanpsfmag);
CREATE INDEX idx_ps1_q3c_zmeanpsfmag ON ps1_q3c(zmeanpsfmag);
END_TABLE

#PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
#ALTER TABLE ps1_q3c ADD objname VARCHAR(64);
#ALTER TABLE ps1_q3c ADD objinfoflag integer;
#ALTER TABLE ps1_q3c ADD qualityflag integer;
#ALTER TABLE ps1_q3c ADD nDetections integer;
#ALTER TABLE ps1_q3c ADD ramean double precision;
#ALTER TABLE ps1_q3c ADD rameanerr double precision;
#ALTER TABLE ps1_q3c ADD decmean double precision;
#ALTER TABLE ps1_q3c ADD decmeanerr double precision;
#ALTER TABLE ps1_q3c ADD gmeanpsfmag double precision;
#ALTER TABLE ps1_q3c ADD gmeanpsfmagerr double precision;
#ALTER TABLE ps1_q3c ADD rmeanpsfmag double precision;
#ALTER TABLE ps1_q3c ADD rmeanpsfmagerr double precision;
#ALTER TABLE ps1_q3c ADD imeanpsfmag double precision;
#ALTER TABLE ps1_q3c ADD imeanpsfmagerr double precision;
#ALTER TABLE ps1_q3c ADD zmeanpsfmag double precision;
#ALTER TABLE ps1_q3c ADD zmeanpsfmagerr double precision;
#ALTER TABLE ps1_q3c ADD ymeanpsfmag double precision;
#ALTER TABLE ps1_q3c ADD ymeanpsfmagerr double precision;
#ALTER TABLE ps1_q3c ALTER COLUMN objname SET DEFAULT '';
#ALTER TABLE ps1_q3c ALTER COLUMN objinfoflag SET DEFAULT -999;
#ALTER TABLE ps1_q3c ALTER COLUMN qualityflag SET DEFAULT -999;
#ALTER TABLE ps1_q3c ALTER COLUMN ndetections SET DEFAULT -999;
#ALTER TABLE ps1_q3c ALTER COLUMN ramean SET DEFAULT -999.0;
#ALTER TABLE ps1_q3c ALTER COLUMN rameanerr SET DEFAULT -999.0;
#ALTER TABLE ps1_q3c ALTER COLUMN decmean SET DEFAULT -999.0;
#ALTER TABLE ps1_q3c ALTER COLUMN decmeanerr SET DEFAULT -999.0;
#ALTER TABLE ps1_q3c ALTER COLUMN gmeanpsfmag SET DEFAULT -999.0;
#ALTER TABLE ps1_q3c ALTER COLUMN gmeanpsfmagerr SET DEFAULT -999.0;
#ALTER TABLE ps1_q3c ALTER COLUMN rmeanpsfmag SET DEFAULT -999.0;
#ALTER TABLE ps1_q3c ALTER COLUMN rmeanpsfmagerr SET DEFAULT -999.0;
#ALTER TABLE ps1_q3c ALTER COLUMN imeanpsfmag SET DEFAULT -999.0;
#ALTER TABLE ps1_q3c ALTER COLUMN imeanpsfmagerr SET DEFAULT -999.0;
#ALTER TABLE ps1_q3c ALTER COLUMN zmeanpsfmag SET DEFAULT -999.0;
#ALTER TABLE ps1_q3c ALTER COLUMN zmeanpsfmagerr SET DEFAULT -999.0;
#ALTER TABLE ps1_q3c ALTER COLUMN ymeanpsfmag SET DEFAULT -999.0;
#ALTER TABLE ps1_q3c ALTER COLUMN ymeanpsfmagerr SET DEFAULT -999.0;
#CREATE INDEX idx_ps1_q3c_psps_objid ON ps1_q3c(psps_objid);
#CREATE INDEX idx_ps1_q3c_rmeanpsfmag ON ps1_q3c(rmeanpsfmag);
#ANALYZE VERBOSE ps1_q3c;
#END_TABLE
# CREATE INDEX ON ps1_q3c (q3c_ang2ipix(ramean, decmean));
