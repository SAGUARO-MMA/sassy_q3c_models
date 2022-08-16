#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.sdss12photoz_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 sdss12photoz_q3c_orm_cli.py --help """


# +
# constant(s)
# -
URL = "https://vizier.u-strasbg.fr/viz-bin/VizieR?-source=+SDSS-DR12"
ARXIV_PDF_URL = SDSS12PHOTOZ_PDF_URL
ARXIV_PDF_FIL = SDSS12PHOTOZ_PDF_URL.split("/")[-1]
ARXIV_DAT_URL = SDSS12PHOTOZ_DAT_URL
ARXIV_DAT_FIL = SDSS12PHOTOZ_DAT_URL.split("/")[-1]


# +
# __text__
# -
__text__ = f"""
#NAME          UNIT          TYPE           DESCRIPTION
-------------------------------------------------------
ra             J2k{DEGREE}          float          Right Ascension of the object (ICRS)
dec            J2k{DEGREE}          float          Declination of the object (ICRS)
mode                         int            1: Primary (469,053,874 sources), 2: Secondary (324,960,094 sources) (qualified to =1 by default)
q_mode                       char           Indicates clean photometry (310,190,812 sources with mode 1+)
classifier                   int            Type of object (3=galaxy, 6=star)
sdss12                       char*24        SDSS-DR12 name, based on J2000 position
m_sdss12                     char*1         The asterisk indicates that 2 different SDSS objects share the same SDSS12 name
sdssid                       char*32        SDSS object identifier
objid                        char*24        SDSS unique object identifier
specid                       char*32        Spectroscopic Plate-MJD-Fiber identifier
spobjid                      char*24        Pointer to the spectrum of object, or 0
parentid                     char*24        Pointer to parent (if object de-blended)
flags                        char*24        Photo object attribute flags
status                       int            Hexadecimal status
e_ra           {ARCSEC}             float          Mean error on RA
e_dec          {ARCSEC}             float          Mean error on Dec
obsdate        yr            float          Mean Observation date
quality                      int            Quality of the observation: 1=bad 2=acceptable 3=good
umag           mag           float          Model magnitude in u filter, AB scale
e_umag         mag           float          Mean error on umag
gmag           mag           float          Model magnitude in g filter, AB scale
e_gmag         mag           float          Mean error on gmag
rmag           mag           float          Model magnitude in r filter, AB scale
e_rmag         mag           float          Mean error on rmag
imag           mag           float          Model magnitude in i filter, AB scale
e_imag         mag           float          Mean error on imag
zmag           mag           float          Model magnitude in z filter, AB scale
e_zmag         mag           float          Mean error on zmag
zsp                          float          Spectroscopic redshift (when SpObjID>0)
e_zsp                        float          Mean error on zsp (negative for bad fit)
f_zsp                        int            z warning flag
vdisp          km/s          float          Velocity dispersion
e_vdisp        km/s          float          Mean error on Vdisp
spinst                       char*24        Spectral instrument used (SDSS or BOSS)
sptype                       char*24        Source type
spclass                      char*24        Spectroscopic class: GALAXY, QSO, STAR
subclass                     char*24        Spectroscopic subclass
spsignal                     float          Median signal-to-noise over all good pixels
u_flags                      char*24        Detection flags, u band
u_prob                       int            Probability 0=notStar, 1=Star in u band
u_photo                      int            Phototype in u band, 6=Star
u_date         yr            float          Date of observation in u band
u_prime_mag    mag           float          Model magnitude in u{ARCMIN} filter
e_u_prime_mag  mag           float          Mean error on u{ARCMIN} filter
u_pmag         mag           float          PSF magnitude in u band
e_u_pmag       mag           float          Mean error on u_pmag
u_upmag        mag           float          Petrosian magnitude in u band
e_u_upmag      mag           float          Mean error on u_upmag
u_prad         {ARCSEC}             float          Petrosian radius in u band
e_u_urad       {ARCSEC}             float          Mean error in u_prad
u_ora          {ARCSEC}             float          Offset of u position along RA
u_odec         {ARCSEC}             float          Offset of u position along Dec
u_dvrad        {ARCSEC}             float          de Vaucouleurs fit radius, u band
u_dvell        {ARCSEC}             float          de Vaucouleurs fit ellipticity, u band
u_pa           {DEGREE}             float          Position angle of dVrad in u band
g_flags                      char*24        Detection flags, g band
g_prob                       int            Probability 0=notStar, 1=Star in g band
g_photo                      int            Phototype in g band, 6=Star
g_date         yr            float          Date of observation in g band
g_prime_mag    mag           float          Model magnitude in g{ARCMIN} filter
e_g_prime_mag  mag           float          Mean error on g{ARCMIN} filter
g_pmag         mag           float          PSF magnitude in g band
e_g_pmag       mag           float          Mean error on g_pmag
g_upmag        mag           float          Petrosian magnitude in g band
e_g_upmag      mag           float          Mean error on g_upmag
g_prad         {ARCSEC}             float          Petrosian radius in g band
e_g_prad       {ARCSEC}             float          Mean error in g_prad
g_ora          {ARCSEC}             float          Offset of g position along RA
g_odec         {ARCSEC}             float          Offset of g position along Dec
g_dvrad        {ARCSEC}             float          de Vaucouleurs fit radius, g band
g_dvell        {ARCSEC}             float          de Vaucouleurs fit ellipticity, g band
g_pa           {DEGREE}             float          Position angle of dVrad in g band
r_flags                      char*24        Detection flags, r band
r_prob                       int            Probability 0=notStar, 1=Star in r band
r_photo                      int            Phototype in r band, 6=Star
r_date         yr            float          Date of observation in r band
r_prime_mag    mag           float          Model magnitude in r{ARCMIN} filter
e_r_prime_mag  mag           float          Mean error on r{ARCMIN} filter
r_pmag         mag           float          PSF magnitude in r band
e_r_pmag       mag           float          Mean error on r_pmag
r_upmag        mag           float          Petrosian magnitude in r band
e_r_upmag      mag           float          Mean error on r_upmag
r_prad         {ARCSEC}             float          Petrosian radius in r band
e_r_urad       {ARCSEC}             float          Mean error in r_prad
r_ora          {ARCSEC}             float          Offset of u position along RA
r_odec         {ARCSEC}             float          Offset of r position along Dec
r_dvrad        {ARCSEC}             float          de Vaucouleurs fit radius, r band
r_dvell        {ARCSEC}             float          de Vaucouleurs fit ellipticity, r band
r_pa           {DEGREE}             float          Position angle of dVrad in r band
i_flags                      char*24        Detection flags, i band
i_prob                       int            Probability 0=notStar, 1=Star in i band
i_photo                      int            Phototype in i band, 6=Star
i_date         yr            float          Date of observation in i band
i_prime_mag    mag           float          Model magnitude in i{ARCMIN} filter
e_i_prime_mag  mag           float          Mean error on i{ARCMIN} filter
i_pmag         mag           float          PSF magnitude in i band
e_i_pmag       mag           float          Mean error on i_pmag
i_upmag        mag           float          Petrosian magnitude in i band
e_i_upmag      mag           float          Mean error on i_upmag
i_prad         {ARCSEC}             float          Petrosian radius in i band
e_i_urad       {ARCSEC}             float          Mean error in i_prad
i_ora          {ARCSEC}             float          Offset of i position along RA
i_odec         {ARCSEC}             float          Offset of i position along Dec
i_dvrad        {ARCSEC}             float          de Vaucouleurs fit radius, i band
i_dvell        {ARCSEC}             float          de Vaucouleurs fit ellipticity, i band
i_pa           {DEGREE}             float          Position angle of dVrad in i band
z_flags                      char*24        Detection flags, z band
z_prob                       int            Probability 0=notStar, 1=Star in z band
z_photo                      int            Phototype in z band, 6=Star
z_date         yr            float          Date of observation in z band
z_prime_mag    mag           float          Model magnitude in z{ARCMIN} filter
e_z_prime_mag  mag           float          Mean error on z{ARCMIN} filter
z_pmag         mag           float          PSF magnitude in z band
e_z_pmag       mag           float          Mean error on z_pmag
z_upmag        mag           float          Petrosian magnitude in z band
e_z_upmag      mag           float          Mean error on z_upmag
z_prad         {ARCSEC}             float          Petrosian radius in z band
e_z_urad       {ARCSEC}             float          Mean error in z_prad
z_ora          {ARCSEC}             float          Offset of z position along RA
z_odec         {ARCSEC}             float          Offset of z position along Dec
z_dvrad        {ARCSEC}             float          de Vaucouleurs fit radius, z band
z_dvell        {ARCSEC}             float          de Vaucouleurs fit ellipticity, z band
z_pa           {DEGREE}             float          Position angle of dVrad in z band
pmra           mas/yr        float          Proper motion along RA
e_pmra         mas/yr        float          Mean error on pmRA
pmdec          mas/yr        float          Proper motion along Dec
e_pmdEC        mas/yr        float          Mean error on pmDE
sigra          mas           float          RMS residual of proper motion fit in RA
sigdec         mas           float          RMS residual of proper motion fit in Dec
m                            int            Number of USNO-B objects matched within 1{ARCSEC}
n                            int            Number of detections used in the pm fit, including SDSS
g_o_plate                    float          Magnitude from O plate recalibrated to g
r_e_plate                    float          Magnitude from E plate recalibrated to r
g_j_plate                    float          Magnitude from J plate recalibrated to g
r_f_plate                    float          Magnitude from F plate recalibrated to r
i_n_plate                    float          Magnitude from N plate recalibrated to i
zph                          float          Photometric redshift; estimated by robust fit to nearest neighbors in a reference set
e_zph                        float          Estimated error of the photometric redshift
ave_zph                      float          Average redshift of the nearest neighbors
                                              if significantly different from zph this might be a better estimate than zph
chi2                         float          Chi-square value for the minimum chi-square template fit
u_prime_mag     mag          float          Rest frame u{ARCMIN} absolute magnitude
g_prime_mag     mag          float          Rest frame g{ARCMIN} absolute magnitude
r_prime_mag     mag          float          Rest frame r{ARCMIN} absolute magnitude
i_prime_mag     mag          float          Rest frame i{ARCMIN} absolute magnitude
z_prime_mag     mag          float          Rest frame z{ARCMIN} absolute magnitude
"""


# +
# function: sdss12photoz_q3c_orm_cli()
# -
# noinspection PyBroadException
def sdss12photoz_q3c_orm_cli(_args: Any = None):

    # check input(s)
    if _args is None:
        raise Exception('Invalid arguments')

    # if --catalog is present, download the catalog
    # if _args.catalog:
    #     if _args.verbose:
    #         print(f"Downloading catalog from {ARXIV_DAT_URL} to {ARXIV_DAT_FIL}")
    #     get_gzip(_url=ARXIV_DAT_URL, _file=ARXIV_DAT_FIL)
    #     return

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
    if _args.ra__gte:
        request_args['ra__gte'] = f'{_args.ra__gte}'
    if _args.ra__lte:
        request_args['ra__lte'] = f'{_args.ra__lte}'
    if _args.dec__gte:
        request_args['dec__gte'] = f'{_args.dec__gte}'
    if _args.dec__lte:
        request_args['dec__lte'] = f'{_args.dec__lte}'
    if _args.sid:
        request_args['sid'] = f'{_args.sid}'
    if _args.classifier:
        request_args['classifier'] = f'{_args.classifier}'
    if _args.quality:
        request_args['quality'] = f'{_args.quality}'
    if _args.name:
        request_args['name'] = f'{_args.name}'
    if _args.obsdate__gte:
        request_args['obsdate__gte'] = f'{_args.obsdate__gte}'
    if _args.obsdate__lte:
        request_args['obsdate__lte'] = f'{_args.obsdate__lte}'
    if _args.u__gte:
        request_args['u__gte'] = f'{_args.u__gte}'
    if _args.u__lte:
        request_args['u__lte'] = f'{_args.u__lte}'
    if _args.g__gte:
        request_args['g__gte'] = f'{_args.g__gte}'
    if _args.g__lte:
        request_args['g__lte'] = f'{_args.g__lte}'
    if _args.r__gte:
        request_args['r__gte'] = f'{_args.r__gte}'
    if _args.r__lte:
        request_args['r__lte'] = f'{_args.r__lte}'
    if _args.i__gte:
        request_args['i__gte'] = f'{_args.i__gte}'
    if _args.i__lte:
        request_args['i__lte'] = f'{_args.i__lte}'
    if _args.z__gte:
        request_args['z__gte'] = f'{_args.z__gte}'
    if _args.z__lte:
        request_args['z__lte'] = f'{_args.z__lte}'
    if _args.zsp__gte:
        request_args['zsp__gte'] = f'{_args.zsp__gte}'
    if _args.zsp__lte:
        request_args['zsp__lte'] = f'{_args.zsp__lte}'
    if _args.zph__gte:
        request_args['zph__gte'] = f'{_args.zph__gte}'
    if _args.zph__lte:
        request_args['zph__lte'] = f'{_args.zph__lte}'
    if _args.ave_zph__gte:
        request_args['ave_zph__gte'] = f'{_args.ave_zph__gte}'
    if _args.ave_zph__lte:
        request_args['ave_zph__lte'] = f'{_args.ave_zph__lte}'

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
        query = session.query(Sdss12PhotoZQ3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = sdss12photoz_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output alphabetically
    print(f"#{','.join(_ for _ in SDSS12PHOTOZ_HEADERS)}")
    for _e in Sdss12PhotoZQ3cRecord.serialize_list(query.all()):
        if verify_keys(_e, set(SDSS12PHOTOZ_HEADERS)):
            print(f"{','.join(str(_e[_l]) for _l in SDSS12PHOTOZ_HEADERS)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query SDSS12PHOTOZ Q3C database', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (de),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--ra__gte', help=f'RA >= <float>')
    _p.add_argument(f'--ra__lte', help=f'RA <= <float>')
    _p.add_argument(f'--dec__gte', help=f'Dec >= <float>')
    _p.add_argument(f'--dec__lte', help=f'Dec <= <float>')
    _p.add_argument(f'--sid', help=f'sid <int>')
    _p.add_argument(f'--classifier', help=f'Classifier <int>')
    _p.add_argument(f'--quality', help=f'Quality <int>')
    _p.add_argument(f'--name', help=f'Name <str>')
    _p.add_argument(f'--obsdate__gte', help=f'Observation date >= <float>')
    _p.add_argument(f'--obsdate__lte', help=f'Observation date <= <float>')
    _p.add_argument(f'--u__gte', help=f'u mag >= <float>')
    _p.add_argument(f'--u__lte', help=f'u mag <= <float>')
    _p.add_argument(f'--g__gte', help=f'g mag >= <float>')
    _p.add_argument(f'--g__lte', help=f'g mag <= <float>')
    _p.add_argument(f'--r__gte', help=f'r mag >= <float>')
    _p.add_argument(f'--r__lte', help=f'r mag <= <float>')
    _p.add_argument(f'--i__gte', help=f'i mag >= <float>')
    _p.add_argument(f'--i__lte', help=f'i mag <= <float>')
    _p.add_argument(f'--z__gte', help=f'z mag >= <float>')
    _p.add_argument(f'--z__lte', help=f'z mag <= <float>')
    _p.add_argument(f'--zsp__gte', help=f'Redshift (spectroscopic) >= <float>')
    _p.add_argument(f'--zsp__lte', help=f'Redshift (spectroscopic) <= <float>')
    _p.add_argument(f'--zph__gte', help=f'Redshift (photometric) >= <float>')
    _p.add_argument(f'--zph__lte', help=f'Redshift (photometric) <= <float>')
    _p.add_argument(f'--ave_zph__gte', help=f'Nearest-Neighbor Redshift (photometric) >= <float>')
    _p.add_argument(f'--ave_zph__lte', help=f'Nearest-Neighbor Redshift (photometric) <= <float>')

    _p.add_argument(f'--sort_order', help=f"Sort order, one of {SDSS12PHOTOZ_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {SDSS12PHOTOZ_SORT_VALUE}")

    # non-database query argument(s)ß
    # _p.add_argument(f'--catalog', default=False, action='store_true', help=f'if present, download the catalog')
    _p.add_argument(f'--paper', default=False, action='store_true', help=f'if present, download the science paper')
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        sdss12photoz_q3c_orm_cli(_args=_a)
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
