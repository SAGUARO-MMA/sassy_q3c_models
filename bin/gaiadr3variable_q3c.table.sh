#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

# Database definition: 
#    https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_variability_tables/ssec_dm_vari_summary.html
#    https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_variability_tables/ssec_dm_vari_classifier_result.html

PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_TABLE
DROP TABLE IF EXISTS gaiadr3variable_q3c;
CREATE TABLE gaiadr3variable_q3c (
  gid serial PRIMARY KEY,
  ra double precision,
  ra_error double precision,
  dec double precision,
  dec_error double precision,
  pmra double precision,
  pmra_error double precision,
  pmdec double precision,
  pmdec_error double precision,
  parallax double precision,
  parallax_error double precision,
  solution_id bigint,
  source_id bigint,
  classification VARCHAR(16),
  best_class_name VARCHAR(26),
  best_class_score double precision,
  num_selected_g_fov integer,
  mean_obs_time_g_fov double precision,
  time_duration_g_fov double precision,
  min_mag_g_fov double precision,
  max_mag_g_fov double precision,
  mean_mag_g_fov double precision,
  median_mag_g_fov double precision,
  range_mag_g_fov double precision,
  trimmed_range_mag_g_fov double precision,
  std_dev_mag_g_fov double precision,
  skewness_mag_g_fov double precision,
  kurtosis_mag_g_fov double precision,
  mad_mag_g_fov double precision,
  abbe_mag_g_fov double precision,
  iqr_mag_g_fov double precision,
  stetson_mag_g_fov double precision,
  std_dev_over_rms_err_mag_g_fov double precision,
  outlier_median_g_fov double precision,
  num_selected_bp integer,
  mean_obs_time_bp double precision,
  time_duration_bp double precision,
  min_mag_bp double precision,
  max_mag_bp double precision,
  mean_mag_bp double precision,
  median_mag_bp double precision,
  range_mag_bp double precision,
  trimmed_range_mag_bp double precision,
  std_dev_mag_bp double precision,
  skewness_mag_bp double precision,
  kurtosis_mag_bp double precision,
  mad_mag_bp double precision,
  abbe_mag_bp double precision,
  iqr_mag_bp double precision,
  stetson_mag_bp double precision,
  std_dev_over_rms_err_mag_bp double precision,
  outlier_median_bp double precision,
  num_selected_rp integer,
  mean_obs_time_rp double precision,
  time_duration_rp double precision,
  min_mag_rp double precision,
  max_mag_rp double precision,
  mean_mag_rp double precision,
  median_mag_rp double precision,
  range_mag_rp double precision,
  trimmed_range_mag_rp double precision,
  std_dev_mag_rp double precision,
  skewness_mag_rp double precision,
  kurtosis_mag_rp double precision,
  mad_mag_rp double precision,
  abbe_mag_rp double precision,
  iqr_mag_rp double precision,
  stetson_mag_rp double precision,
  std_dev_over_rms_err_mag_rp double precision,
  outlier_median_rp double precision,
  in_vari_classification_result boolean,
  in_vari_rrlyrae boolean,
  in_vari_cepheid boolean,
  in_vari_planetary_transit boolean,
  in_vari_short_timescale boolean,
  in_vari_long_period_variable boolean,
  in_vari_eclipsing_binary boolean,
  in_vari_rotation_modulation boolean,
  in_vari_ms_oscillator boolean,
  in_vari_agn boolean,
  in_vari_microlensing boolean,
  in_vari_compact_companion boolean
);
END_TABLE
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} << END_Q3C
  CREATE INDEX ON gaiadr3variable_q3c (q3c_ang2ipix(ra, dec));
  CREATE INDEX idx_gaiadr3variable_q3c_ra_error ON gaiadr3variable_q3c(ra_error);
  CREATE INDEX idx_gaiadr3variable_q3c_dec_error ON gaiadr3variable_q3c(dec_error);
  CREATE INDEX idx_gaiadr3variable_q3c_pmra ON gaiadr3variable_q3c(pmra);
  CREATE INDEX idx_gaiadr3variable_q3c_pmdec ON gaiadr3variable_q3c(pmdec);
  CREATE INDEX idx_gaiadr3variable_q3c_classification ON gaiadr3variable_q3c(classification);
  CREATE INDEX idx_gaiadr3variable_q3c_mean_mag_g_fov ON gaiadr3variable_q3c(mean_mag_g_fov);
  CREATE INDEX idx_gaiadr3variable_q3c_median_mag_g_fov ON gaiadr3variable_q3c(median_mag_g_fov);
  CREATE INDEX idx_gaiadr3variable_q3c_best_class_name ON gaiadr3variable_q3c(best_class_name);
  CREATE INDEX idx_gaiadr3variable_q3c_best_class_score ON gaiadr3variable_q3c(best_class_score);
  ANALYZE VERBOSE gaiadr3variable_q3c;
END_Q3C
