#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.roma_bzcat_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 roma_bzcat_q3c_orm_cli.py --help """


# +
# constant(s)
# -
ARXIV_PDF_URL = ROMA_BZCAT_PDF_URL
ARXIV_PDF_FIL = ROMA_BZCAT_PDF_URL.split("/")[-1]
ARXIV_DAT_URL = ROMA_BZCAT_DAT_URL
ARXIV_DAT_FIL = ROMA_BZCAT_DAT_URL.split("/")[-1]


# +
# __text__
# -
__text__ = """

VII/274             The Roma BZCAT - 5th edition                (Massaro+, 2015)
================================================================================
The 5th edition of the Roma-BZCAT.
     Massaro E., Maselli A., Leto C., Marchegiani P., Perri M., Giommi P.,
     Piranomonte S.
     <Astrophys. Space Sci., 357, 75 (2015)>
     =2015Ap&SS.357...75M
     =2016yCat.7274....0M
================================================================================
ADC_Keywords: QSOs ; BL Lac objects ; Galaxy catalogs ; Redshifts ; Photometry
Keywords: BL Lacertae objects: general - galaxies: quasars: general - catalogs

Abstract:
    The Roma-BZCAT is now at the 5th Edition which contains coordinates
    and multi-frequency data of 3561 sources, about 30% more than in the
    1st edition, either confirmed blazars or exhibiting characteristics
    close to this type of sources. With respect to the previous editions,
    this new edition has relevant changes in the sources' classification
    and has a new format for the notes in the tables. We emphasize that
    all the sources in the Roma-BZCAT have a detection in the radio
    band. Moreover, a complete spectroscopic information is published
    and could be accessed by us for all of them, with the exception of BL
    Lac candidates. Consequently, peculiar sources as the so called
    "radio quiet BL Lacs", which are reported in some other
    catalogues, are not included here because of possible contamination
    with hot stars and other extragalactic objects.

Description:
    In the 5th Edition we use similar denomination of
    blazars adopted in the previous editions. Each blazar
    is identified by a code, with 5BZ for all blazars, a fourth
    letter that specifies the type (B, G, Q or U), followed by the
    truncated equatorial coordinates (J2000). We introduced the edition
    number before the letters BZ to avoid possible confusion due to the
    fact that several sources changed their old names because of the new
    adopted classification.

    The codes are defined in the "Note (G1)" below.

    The 5th edition contains 1151 BZB sources, 92 of which are reported as
    candidates because we could not find their optical spectra in the
    literature, 1909 BZQ sources, 274 BZG sources and 227 BZU objects

File Summary:
--------------------------------------------------------------------------------
 FileName      Lrecl  Records   Explanations
--------------------------------------------------------------------------------
ReadMe            80        .   This file
bzcat5.dat       133     3561   The Roma BZCAT - 5th edition
--------------------------------------------------------------------------------

See also:
 J/A+A/495/691 : Multifrequency catalogue of blazars, Roma-BZCAT (Massaro+ 2009)
 http://www.asdc.asi.it/bzcat : BZCAT Home Page

Byte-by-byte Description of file: bzcat5.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  4  I4    ---     Seq       Sequential number
   6- 20  A15   ---     Name      Source name (based on J2000 position),
                                   5BZA JHHMM+DDMM (G1)
  22- 23  I2    h       RAh       Right ascension (J2000.0)
  25- 26  I2    min     RAm       Right ascension (J2000.0)
  28- 32  F5.2  s       RAs       Right ascension (J2000.0)
      34  A1    ---     DE-       Declination sign (J2000.0)
  35- 36  I2    deg     DEd       Declination (J2000.0)
  38- 39  I2    arcmin  DEm       Declination (J2000.0)
  41- 45  F5.2  arcsec  DEs       Declination (J2000.0)
  47- 52  F6.2  deg     GLON      Galactic longitude
  54- 59  F6.2  deg     GLAT      Galactic latitude
  61- 65  F5.3  ---     z         Redshift
      66  A1    ---   u_z         [?] uncertainty flag on z
  68- 71  F4.1  mag     Rmag      ?=0 R magnitude
  73- 96  A24   ---     Class     Source classification
  98-105  F8.1  mJy     FR        ?=0 Flux density at 1.4/0.843GHz
 107-111  I5    mJy     F143      ?=0 Flux density at 143GHz
 113-118  F6.2  fW/m2   FX        ?=0 X-ray flux 0.1-2.4keV
 120-126  E7.3  cm2/s   FF        ?=0 Fermi flux1-100GeV (in ph/cm2/s)
 128-133  F6.3  ---     aro       Spectral index radio-optical
--------------------------------------------------------------------------------

Global Notes:
Note (G1): The classifications are:
    5BZB = BL Lac objects, used for AGNs with a featureless optical
      spectrum, or having only absorption lines of galaxian origin and weak
      and narrow emission lines;
    5BZG = sources, usually reported as BL Lac objects in the literature,
      but having a spectral energy distribution (SED) with a significant
      dominance of the galaxian emission over the nuclear one
    5BZQ = Flat Spectrum Radio Quasars, with an optical spectrum showing
      broad emission lines and dominant blazar characteristics;
    BZU  = blazars of Uncertain type, adopted for a small number of sources
      having peculiar characteristics but also exhibiting blazar activity:
      for instance, occasional presence/absence of broad spectral lines or
      other features, transition objects between a radio galaxy and a BL
      Lac, galaxies hosting a low luminosity blazar Nucleus, etc.
--------------------------------------------------------------------------------

History:
    Copied at http://www.asdc.asi.it/bzcat

================================================================================
(End)                                      Patricia Vannier [CDS]    11-Feb-2016
"""


# +
# function: roma_bzcat_q3c_orm_cli()
# -
# noinspection PyBroadException
def roma_bzcat_q3c_orm_cli(_args: Any = None):

    # check input(s)
    if _args is None:
        raise Exception('Invalid arguments')

    # if --catalog is present, download the catalog
    if _args.catalog:
        if _args.verbose:
            print(f"Downloading catalog from {ARXIV_DAT_URL} to {ARXIV_DAT_FIL}")
        get_data(_url=ARXIV_DAT_URL, _file=ARXIV_DAT_FIL)
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
    if _args.rid:
        request_args['rid'] = f'{_args.rid}'
    if _args.ra__gte:
        request_args['ra__gte'] = f'{_args.ra__gte}'
    if _args.ra__lte:
        request_args['ra__lte'] = f'{_args.ra__lte}'
    if _args.dec__gte:
        request_args['dec__gte'] = f'{_args.dec__gte}'
    if _args.dec__lte:
        request_args['dec__lte'] = f'{_args.dec__lte}'
    if _args.rmag__gte:
        request_args['rmag__gte'] = f'{_args.rmag__gte}'
    if _args.rmag__lte:
        request_args['rmag__lte'] = f'{_args.rmag__lte}'
    if _args.z__gte:
        request_args['z__gte'] = f'{_args.z__gte}'
    if _args.z__lte:
        request_args['z__lte'] = f'{_args.z__lte}'
    if _args.name:
        request_args['name'] = f'{_args.name}'
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
        query = session.query(RomaBzcatQ3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = roma_bzcat_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output alphabetically
    _keys = ROMA_BZCAT_KEYS[:-1]
    print(f"#{','.join(_ for _ in ROMA_BZCAT_KEYS)}")
    for _e in RomaBzcatQ3cRecord.serialize_list(query.all()):
        if verify_keys(_e, set(_keys)):
            print(f"{','.join(str(_e[_l]) for _l in _keys)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query ROMA_BZCAT Q3C database', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (de),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--rid', help=f'rid <int>')
    _p.add_argument(f'--ra__gte', help=f'RA >= <float>')
    _p.add_argument(f'--ra__lte', help=f'RA <= <float>')
    _p.add_argument(f'--dec__gte', help=f'Dec >= <float>')
    _p.add_argument(f'--dec__lte', help=f'Dec <= <float>')
    _p.add_argument(f'--rmag__gte', help=f'R magnitude >= <float>')
    _p.add_argument(f'--rmag__lte', help=f'R magnitude <= <float>')
    _p.add_argument(f'--z__gte', help=f'Redshift >= <float>')
    _p.add_argument(f'--z__lte', help=f'Redshift <= <float>')
    _p.add_argument(f'--name', help=f'name <str>')
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {ROMA_BZCAT_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {ROMA_BZCAT_SORT_VALUE}")

    # non-database query argument(s)ß
    _p.add_argument(f'--catalog', default=False, action='store_true', help=f'if present, download the catalog')
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        roma_bzcat_q3c_orm_cli(_args=_a)
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
