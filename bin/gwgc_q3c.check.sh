#!/bin/sh

# +
# $1 = database host
# $2 = database port
# $3 = database name
# $4 = database username
# $5 = database password
# -

# +
# NB: the catalog has RA in "digital hours" not degrees so make sure you are comparing like with like!
# -
for galaxy in NGC7317 NGC7318A NGC7318B NGC7319 NGC7320 NGC7320C; do
  echo "Stephan's Quintet Galaxy: ${galaxy} begin >>>>>"
  grep "${galaxy}" gwgc.dat
  PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} --pset pager=off -c "SELECT * FROM gwgc_q3c WHERE name = '${galaxy}';"
  python3 -c "from sassy_q3c_models import *; _ra, _dec = get_astropy_coords(_oname='${galaxy}'); print(f'RAh={_ra/15.0}, RA={_ra}, Dec={_dec}')"
  python3 -c "from sassy_q3c_models import *; _ra, _dec = get_simbad2k_coords(_oname='${galaxy}'); print(f'RAh={_ra/15.0}, RA={_ra}, Dec={_dec}')"
  echo "Stephan's Quintet Galaxy: ${galaxy} end   >>>>>"
done

wc -l gwgc.dat
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} --pset pager=off -c "SELECT COUNT(*) FROM gwgc_q3c;"
PGPASSWORD=${5} psql --echo-all -h ${1} -p ${2} -U ${4} -d ${3} --pset pager=off -c "SELECT MAX(gid) FROM gwgc_q3c;"
