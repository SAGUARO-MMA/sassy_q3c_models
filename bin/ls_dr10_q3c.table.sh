#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS ls_dr10_q3c;
CREATE TABLE ls_dr10_q3c (
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
    declination double precision,
    flux_g double precision,
    flux_r double precision,
    flux_i double precision,
    flux_z double precision,
    flux_ivar_g double precision,
    flux_ivar_r double precision,
    flux_ivar_i double precision,
    flux_ivar_z double precision,
    flux_w1 double precision,
    flux_w2 double precision,
    flux_w3 double precision,
    flux_w4 double precision,
    flux_ivar_w1 double precision,
    flux_ivar_w2 double precision,
    flux_ivar_w3 double precision,
    flux_ivar_w4 double precision,
    mtype VARCHAR(8),
    ref_cat VARCHAR(8),
    ref_id bigint,
    parallax double precision,
    parallax_ivar double precision,
    pmra double precision,
    pmra_ivar double precision,
    pmdec double precision,
    pmdec_ivar double precision,
    gaia_phot_variable_flag smallint
);
END_TABLE
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_Q3C
  CREATE INDEX ON ls_dr10_q3c (q3c_ang2ipix(ra, declination));
  CREATE INDEX idx_ls_dr10_q3c_objid ON public.ls_dr10_q3c USING btree (objid);
  CREATE INDEX idx_ls_dr10_q3c_z_phot_mean ON public.ls_dr10_q3c USING btree (z_phot_mean);
  CREATE INDEX idx_ls_dr10_q3c_z_phot_median ON public.ls_dr10_q3c USING btree (z_phot_median);
  CREATE INDEX idx_ls_dr10_q3c_z_phot_mean_i ON public.ls_dr10_q3c USING btree (z_phot_mean_i);
  CREATE INDEX idx_ls_dr10_q3c_z_phot_median_i ON public.ls_dr10_q3c USING btree (z_phot_median_i);
  CREATE INDEX idx_ls_dr10_q3c_z_spec ON public.ls_dr10_q3c USING btree (z_spec);
  CREATE INDEX idx_ls_dr10_q3c_flux_g ON public.ls_dr10_q3c USING btree (flux_g);
  CREATE INDEX idx_ls_dr10_q3c_flux_r ON public.ls_dr10_q3c USING btree (flux_r);
  CREATE INDEX idx_ls_dr10_q3c_flux_i ON public.ls_dr10_q3c USING btree (flux_i);
  CREATE INDEX idx_ls_dr10_q3c_flux_z ON public.ls_dr10_q3c USING btree (flux_z);
  CREATE INDEX idx_ls_dr10_q3c_flux_w1 ON public.ls_dr10_q3c USING btree (flux_w1);
  CREATE INDEX idx_ls_dr10_q3c_flux_w2 ON public.ls_dr10_q3c USING btree (flux_w2);
  CREATE INDEX idx_ls_dr10_q3c_flux_w3 ON public.ls_dr10_q3c USING btree (flux_w3);
  CREATE INDEX idx_ls_dr10_q3c_flux_w4 ON public.ls_dr10_q3c USING btree (flux_w4);
  CLUSTER ls_dr10_q3c_q3c_ang2ipix_idx ON ls_dr10_q3c;
  ANALYZE VERBOSE ls_dr10_q3c;
END_Q3C
