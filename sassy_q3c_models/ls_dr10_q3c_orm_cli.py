#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.ls_dr10_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 ls_dr10_q3c_orm_cli.py --help """


# +
# constant(s)
# -
ARXIV_PDF_URL = LSDR10_PDF_URL
ARXIV_PDF_FIL = LSDR10_PDF_URL.split("/")[-1]
ARXIV_DAT_URL = LSDR10_DAT_URL
ARXIV_DAT_FIL = LSDR10_DAT_URL.split("/")[-1]


# +
# __text__
# -
__text__ = """
Table: ls_dr10_q3c

Column           Type     Description
--------------------------------------------------------------------------------
lid                       bigint   Unique LS object ID
brickid                   int      Brick ID [1,662174]
objid                     int      Catalog object number within this brick
                                     - a unique identifier hash is release,brickid,objid
                                     - objid spans [0,N-1] and is contiguously enumerated within each brick
z_phot_mean               double   photo-z derived from the mean of the photo-z PDF
z_phot_median             double   photo-z derived from the median of the photo-z PDF
z_phot_std                double   Standard deviation of the photo-zs derived from the photo-z PDF
z_phot_l68                double   Lower 68% confidence region, derived from the photo-z PDF
z_phot_u68                double   Upper 68% confidence region, derived from the photo-z PDF
z_phot_l95                double   Lower 95% confidence region, derived from the photo-z PDF
z_phot_u95                double   Upper 95% confidence region, derived from the photo-z PDF
z_phot_mean_i             double   photo-z derived from the mean of the photo-z PDF (inc i band)
z_phot_median_i           double   photo-z derived from the median of the photo-z PDF (inc i band)
z_phot_std_i              double   Standard deviation of the photo-zs derived from the photo-z PDF (inc i band)
z_phot_l68_i              double   Lower 68% confidence region, derived from the photo-z PDF (inc i band)
z_phot_u68_i              double   Upper 68% confidence region, derived from the photo-z PDF (inc i band)
z_phot_l95_i              double   Lower 95% confidence region, derived from the photo-z PDF (inc i band)
z_phot_u95_i              double   Upper 95% confidence region, derived from the photo-z PDF (inc i band)
z_spec                    double   Spectroscopic Z
release                   smallint Unique integer denoting the camera and filter set
training                  bool     True if spectroscopic Z is used in photometric Z training
training_i                bool     True if spectroscopic Z is used in photometric Z training (inc i band)
survey                    text     Source of the spectroscopic Z
kfold                     int      Index of the subset in the 10-fold cross-validation
kfold_i                   int      Index of the subset in the 10-fold cross-validation (inc i band)
ra                        double   RA (J2000)
declination               double   Dec (J2000)
flux_g                    double   G-band Flux
flux_r                    double   R-band Flux
flux_i                    double   I-band Flux
flux_z                    double   Z-band Flux
flux_ivar_g               double   G-band Flux Variance
flux_ivar_r               double   R-band Flux Variance
flux_ivar_i               double   I-band Flux Variance
flux_ivar_z               double   Z-band Flux Variance
flux_w1                   double   W1-band Flux
flux_w2                   double   W2-band Flux
flux_w3                   double   W3-band Flux
flux_w4                   double   W4-band Flux
flux_ivar_w1              double   W1-band Flux Variance
flux_ivar_w2              double   W2-band Flux Variance
flux_ivar_w3              double   W3-band Flux Variance
flux_ivar_w4              double   W4-band Flux Variance
mtype                     text     Morphological type
ref_cat                   text     Reference Catalog
ref_id                    integer  Reference Catalog Identifier
parallax                  double   Parallax
parallax_ivar             double   Parallax Variance
pmra                      double   RA Proper Motion
pmra_ivar                 double   RA Proper Motion Variance
pmdec                     double   Dec Proper Motion
pmdec_ivar                double   Dec Proper Motion Variance
gaia_phot_variable_flag   boolean  GAIA phot variable flag
"""


# +
# function: ls_dr10_q3c_orm_cli()
# -
# noinspection PyBroadException
def ls_dr10_q3c_orm_cli(_args: Any = None):

    # check input(s)
    if _args is None:
        raise Exception('Invalid arguments')

    # if --paper is present, download the science paper
    if _args.paper:
        if _args.verbose:
            print(f"Downloading science paper from {ARXIV_PDF_URL} to {ARXIV_PDF_FIL}")
        get_data(_url=ARXIV_PDF_URL, _file=ARXIV_PDF_FIL)
        return

    # if --text is present, describe of the catalog
    if _args.text:
        return print(__text__)

    # get input(s)
    request_args = {}
    if _args.astrocone:
        request_args['astrocone'] = f'{_args.astrocone}'
    if _args.cone:
        request_args['cone'] = f'{_args.cone}'
    if _args.ellipse:
        request_args['ellipse'] = f'{_args.ellipse}'
    if _args.lid:
        request_args['lid'] = f'{_args.lid}'
    if _args.ra__gte:
        request_args['ra__gte'] = f'{_args.ra__gte}'
    if _args.ra__lte:
        request_args['ra__lte'] = f'{_args.ra__lte}'
    if _args.dec__gte:
        request_args['dec__gte'] = f'{_args.dec__gte}'
    if _args.dec__lte:
        request_args['dec__lte'] = f'{_args.dec__lte}'
    if _args.z_mean__gte:
        request_args['z_mean__gte'] = f'{_args.z_mean__gte}'
    if _args.z_mean__lte:
        request_args['z_mean__lte'] = f'{_args.z_mean__lte}'
    if _args.z_median__gte:
        request_args['z_median__gte'] = f'{_args.z_median__gte}'
    if _args.z_median__lte:
        request_args['z_median__lte'] = f'{_args.z_median__lte}'
    if _args.iz_mean__gte:
        request_args['iz_mean__gte'] = f'{_args.iz_mean__gte}'
    if _args.iz_mean__lte:
        request_args['iz_mean__lte'] = f'{_args.iz_mean__lte}'
    if _args.iz_median__gte:
        request_args['iz_median__gte'] = f'{_args.iz_median__gte}'
    if _args.iz_median__lte:
        request_args['iz_median__lte'] = f'{_args.iz_median__lte}'
    if _args.z_spec__gte:
        request_args['z_spec__gte'] = f'{_args.z_spec__gte}'
    if _args.z_spec__lte:
        request_args['z_spec__lte'] = f'{_args.z_spec__lte}'
    if _args.r_flux__gte:
        request_args['r_flux__gte'] = f'{_args.r_flux__gte}'
    if _args.r_flux__lte:
        request_args['r_flux__lte'] = f'{_args.r_flux__lte}'
    if _args.sort_order:
        request_args['sort_order'] = f'{_args.sort_order}'
    if _args.sort_value:
        request_args['sort_value'] = f'{_args.sort_value}'

    # set up access to database
    try:
        if _args.verbose:
            print(f'connecting via postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        if _args.verbose:
            print(f'engine = {engine}')
        get_session = sessionmaker(bind=engine)
        if _args.verbose:
            print(f'Session = {get_session}')
        session = get_session()
        if _args.verbose:
            print(f'session = {session}')
    except Exception as _e1:
        raise Exception(f"failed to connect to database, error='{_e1}'")

    # execute query
    try:
        if _args.verbose:
            print(f'executing query')
        query = session.query(LsDr10Q3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = ls_dr10_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output alphabetically
    print(f"#{','.join(_ for _ in LSDR10_HEADERS)}")
    for _e in LsDr10Q3cRecord.serialize_list(query.all()):
        if verify_keys(_e, set(LSDR10_HEADERS)):
            print(f"{','.join(str(_e[_l]) for _l in LSDR10_HEADERS)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query LSDR10_Q3C database', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),declination (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),declination (de),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--lid', help=f'lid <int>')
    _p.add_argument(f'--ra__gte', help=f'RA >= <float>')
    _p.add_argument(f'--ra__lte', help=f'RA <= <float>')
    _p.add_argument(f'--dec__gte', help=f'Dec >= <float>')
    _p.add_argument(f'--dec__lte', help=f'Dec <= <float>')
    _p.add_argument(f'--z_mean__gte', help=f'Z mean >= <float>')
    _p.add_argument(f'--z_mean__lte', help=f'Z mean <= <float>')
    _p.add_argument(f'--z_median__gte', help=f'Z median >= <float>')
    _p.add_argument(f'--z_median__lte', help=f'Z median <= <float>')
    _p.add_argument(f'--iz_mean__gte', help=f'Z i mean >= <float>')
    _p.add_argument(f'--iz_mean__lte', help=f'Z i mean <= <float>')
    _p.add_argument(f'--iz_median__gte', help=f'Z i median >= <float>')
    _p.add_argument(f'--iz_median__lte', help=f'Z i median <= <float>')
    _p.add_argument(f'--z_spec__gte', help=f'Z spec >= <float>')
    _p.add_argument(f'--z_spec__lte', help=f'Z spec <= <float>')
    _p.add_argument(f'--g_flux__gte', help=f'G flux >= <float>')
    _p.add_argument(f'--g_flux__lte', help=f'G flux <= <float>')
    _p.add_argument(f'--r_flux__gte', help=f'R flux >= <float>')
    _p.add_argument(f'--r_flux__lte', help=f'R flux <= <float>')
    _p.add_argument(f'--i_flux__gte', help=f'I flux >= <float>')
    _p.add_argument(f'--i_flux__lte', help=f'I flux <= <float>')
    _p.add_argument(f'--z_flux__gte', help=f'Z flux >= <float>')
    _p.add_argument(f'--z_flux__lte', help=f'Z flux <= <float>')
    _p.add_argument(f'--w1_flux__gte', help=f'W1 flux >= <float>')
    _p.add_argument(f'--w2_flux__lte', help=f'W2 flux <= <float>')
    _p.add_argument(f'--w3_flux__gte', help=f'W3 flux >= <float>')
    _p.add_argument(f'--w4_flux__lte', help=f'W4 flux <= <float>')
    _p.add_argument(f'--w1_flux__gte', help=f'W1 flux >= <float>')
    _p.add_argument(f'--w2_flux__lte', help=f'W2 flux <= <float>')
    _p.add_argument(f'--w3_flux__gte', help=f'W3 flux >= <float>')
    _p.add_argument(f'--w4_flux__lte', help=f'W4 flux <= <float>')
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {LSDR10_SORT_ORDER}")
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {LSDR10_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {LSDR10_SORT_VALUE}")

    # non-database query argument(s)
    _p.add_argument(f'--paper', default=False, action='store_true', help=f'if present, download the science paper')
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        ls_dr10_q3c_orm_cli(_args=_a)
    except Exception as _:
        print(f"{_}\n{__doc__}")
