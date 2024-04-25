#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS ls_dr10_photo_z_q3c;
CREATE TABLE ls_dr10_photo_z_q3c (
    lid serial PRIMARY KEY,
    brickid integer,
    objid integer,
    z_phot_mean double precision,
    z_phot_median double precision,
    z_phot_std double precision,
    z_phot_l68 double precision,
    z_phot_u68 double precision,
    z_phot_l95 double precision,
    z_phot_u95 double precision,
    z_phot_mean_i double precision,
    z_phot_median_i double precision,
    z_phot_std_i double precision,
    z_phot_l68_i double precision,
    z_phot_u68_i double precision,
    z_phot_l95_i double precision,
    z_phot_u95_i double precision,
    z_spec double precision,
    release smallint,
    training boolean,
    training_i boolean,
    survey VARCHAR(16),
    kfold integer,
    kfold_i integer,
    ra double precision,
    declination double precision
);
END_TABLE
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_Q3C
  CREATE INDEX idx_ls_dr10_photo_z_q3c_objid ON ls_dr10_photo_z_q3c(objid);
  CREATE INDEX idx_ls_dr10_photo_z_q3c_z_phot_mean ON ls_dr10_photo_z_q3c(z_phot_mean);
  CREATE INDEX idx_ls_dr10_photo_z_q3c_z_phot_median ON ls_dr10_photo_z_q3c(z_phot_median);
  CREATE INDEX idx_ls_dr10_photo_z_q3c_z_phot_mean_i ON ls_dr10_photo_z_q3c(z_phot_mean_i);
  CREATE INDEX idx_ls_dr10_photo_z_q3c_z_phot_median_i ON ls_dr10_photo_z_q3c(z_phot_median_i);
  CREATE INDEX idx_ls_dr10_photo_z_q3c_z_spec ON ls_dr10_photo_z_q3c(z_spec);
  CREATE INDEX ON ls_dr10_photo_z_q3c (q3c_ang2ipix(ra, declination));
  CLUSTER ls_dr10_photo_z_q3c_q3c_ang2ipix_idx ON ls_dr10_photo_z_q3c;
  ANALYZE VERBOSE ls_dr10_photo_z_q3c;
END_Q3C
