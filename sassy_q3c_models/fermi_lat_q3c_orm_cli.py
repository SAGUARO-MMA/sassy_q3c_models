#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.fermi_lat_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 fermi_lat_q3c_orm_cli.py --help """


# +
# constant(s)
# -
ARXIV_PDF_URL = FERMI_LAT_PDF_URL
ARXIV_PDF_FIL = FERMI_LAT_PDF_URL.split("/")[-1]
ARXIV_DAT_URL = FERMI_LAT_DAT_URL
ARXIV_DAT_FIL = FERMI_LAT_DAT_URL.split("/")[-1]


# +
# __text__
# -
__text__ = """
J/MNRAS/490/4770    Classifying Fermi-LAT gamma-ray sources   (Kovacevic+, 2019)
================================================================================
Optimizing neural network techniques in classifying Fermi-LAT gamma-ray sources.
    Kovacevic M., Chiaro G., Cutini S., Tosti G.
   <Mon. Not. R. Astron. Soc., 490, 4770-4777 (2019)>
   =2019MNRAS.490.4770K    (SIMBAD/NED BibCode)
================================================================================
ADC_Keywords: Active gal. nuclei ; BL Lac objects ; Gamma rays ;
              X-ray sources ; Radio sources
Keywords: methods: statistical - galaxies: active -
          BL Lacertae objects: general - gamma-rays: galaxies

Abstract:
    Machine learning is an automatic technique that is revolutionizing
    scientific research, with innovative applications and wide use in
    astrophysics. The aim of this study was to develop an optimized
    version of an Artificial Neural Network machine learning method for
    classifying blazar candidates of uncertain type detected by the Fermi
    Large Area Telescope {gamma}-ray instrument. The final result of this
    study increased the classification performance by about 80 per cent
    with respect to previous method, leaving only 15 unclassified blazars
    out of 573 blazar candidates of uncertain type listed in the LAT
    4-year Source Catalog.

Description:
    In this study, we explored the possibilities to increase the
    performance of a neural network method previously used for the
    classification of uncertain blazars in Chiaro et al.
    (2016MNRAS.462.3180C, Cat. J/MNRAS/462/3180). We developed an
    optimized version of the original algorithm improving the selecting
    performance of about 80 per cent. The final result of this study
    left 15 uncertain blazar sources instead of 77 in Chiaro et al.
    (2016MNRAS.462.3180C, Cat. J/MNRAS/462/3180).

    Looking beyond {gamma}-ray features of blazars, interesting
    information can be obtained from a multiwavelength study of the
    sources and particularly from X-ray and radio flux. In this study we
    tested the possibility to use those two parameters to improve the
    performance of the network. We did not consider any optical
    spectroscopy data because when considering uncertain sources, optical
    spectra are very often not available or not sufficiently descriptive
    of the nature of the source.

    The {gamma}-ray flux was obtained by adding five time-integrated
    fluxes in five bands (0.1-0.3, 0.3-1, 1-3, 3-10, 10-100 GeV) from the
    3FGL catalogue (Acero et al. 2015ApJS..218...23A, Cat. J/ApJS/218/23).
    Radio and X-ray data were obtained from the Fermi-LAT 4-year AGN
    Catalog 3LAC (Ackermann et al. 2015ApJ...810...14A, Cat.
    J/ApJ/810/14). Radio fluxes used were measured at frequencies of 1.4
    and 0.8GHz; the X-ray fluxes were measured in the 0.1-2.4keV range.

    The complete list of 567 classified BCUs is presented in Table 1 in
    which sources are sorted by increasing likelihood of a source being a
    BL Lac.

File Summary:
--------------------------------------------------------------------------------
 FileName      Lrecl  Records   Explanations
--------------------------------------------------------------------------------
ReadMe            80        .   This file
table1.dat        72      567   Properties of 567 BCUs used for classification
                                in this work
--------------------------------------------------------------------------------

See also:
 J/MNRAS/462/3180 : 3FGL Blazar of Unknown Type classification (Chiaro+, 2016)
    J/ApJS/218/23 : Fermi LAT third source catalog (3FGL) (Acero+, 2015)
     J/ApJ/810/14 : Third catalog of LAT-detected AGNs (3LAC) (Ackermann+, 2015)

Byte-by-byte Description of file: table1.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1- 18  A18   ---     Name      Blazar name (3FGL JHHMM.m+DDMMe)
  20- 26  F7.3  deg     GLAT      Galactic latitude
  28- 34  F7.3  deg     GLON      Galactic longitude
  36- 40  F5.3  ---     lBLLac    BL Lac likelihood from this work
  42- 46  F5.3  ---     PBLLac    ? BL Lac precision from this work
  48- 52  F5.3  ---     PFSRQ     ? FSRQ precision from this work
  54- 59  A6    ---     Class     BCU classification from this work (1)
  61- 65  F5.3  ---     lBLLaclit BL Lac likelihood according to
                                   Chiaro et al. (2016MNRAS.462.3180C,
                                   Cat. J/MNRAS/462/3180)
  67- 72  A6    ---     Classlit  BCU classification according to
                                   Chiaro et al. (2016MNRAS.462.3180C,
                                   Cat. J/MNRAS/462/3180) (2)
--------------------------------------------------------------------------------
Note (1): Classification as follows:
       BCU = Blazar candidates of uncertain type (15/567)
    BL Lac = BL Lacertae (378/567)
      FSRQ = Flat Spectrum Radio Quasar (174/567)
Note (2): Classification as follows:
       BCU = Blazar candidates of uncertain type (75/567)
    BL Lac = BL Lacertae (341/567)
      FSRQ = Flat Spectrum Radio Quasar (151/567)
--------------------------------------------------------------------------------

History:
    From electronic version of the journal

================================================================================
(End)                                           Ana Fiallos [CDS]    03-Feb-2023
"""


# +
# function: fermi_lat_q3c_orm_cli()
# -
# noinspection PyBroadException
def fermi_lat_q3c_orm_cli(_args: Any = None):

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
    if _args.fid:
        request_args['fid'] = f'{_args.fid}'
    if _args.b__gte:
        request_args['b__gte'] = f'{_args.b__gte}'
    if _args.b__lte:
        request_args['b__lte'] = f'{_args.b__lte}'
    if _args.l__gte:
        request_args['l__gte'] = f'{_args.l__gte}'
    if _args.l__lte:
        request_args['l__lte'] = f'{_args.l__lte}'
    if _args.ra__gte:
        request_args['ra__gte'] = f'{_args.ra__gte}'
    if _args.ra__lte:
        request_args['ra__lte'] = f'{_args.ra__lte}'
    if _args.dec__gte:
        request_args['dec__gte'] = f'{_args.dec__gte}'
    if _args.dec__lte:
        request_args['dec__lte'] = f'{_args.dec__lte}'
    if _args.lbllac__gte:
        request_args['lbllac__gte'] = f'{_args.lbllac__gte}'
    if _args.lbllac__lte:
        request_args['lbllac__lte'] = f'{_args.lbllac__lte}'
    if _args.name:
        request_args['name'] = f'{_args.name}'
    if _args.classification:
        request_args['classification'] = f'{_args.classification}'
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
        query = session.query(FermiLatQ3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = fermi_lat_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output alphabetically
    print(f"#{','.join(_ for _ in FERMI_LAT_KEYS)}")
    for _e in FermiLatQ3cRecord.serialize_list(query.all()):
        if verify_keys(_e, set(FERMI_LAT_KEYS)):
            print(f"{','.join(str(_e[_l]) for _l in FERMI_LAT_KEYS)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query FERMI_LAT Q3C database', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (de),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--fid', help=f'fid <int>')
    _p.add_argument(f'--b__gte', help=f'Galactic Latitude >= <float>')
    _p.add_argument(f'--b__lte', help=f'Galactic Latitude <= <float>')
    _p.add_argument(f'--l__gte', help=f'Galactic Longitude >= <float>')
    _p.add_argument(f'--l__lte', help=f'Galactic Longitude <= <float>')
    _p.add_argument(f'--ra__gte', help=f'RA >= <float>')
    _p.add_argument(f'--ra__lte', help=f'RA <= <float>')
    _p.add_argument(f'--dec__gte', help=f'Dec >= <float>')
    _p.add_argument(f'--dec__lte', help=f'Dec <= <float>')
    _p.add_argument(f'--lbllac__gte', help=f'BLLac Likeliehood >= <float>')
    _p.add_argument(f'--lbllac__lte', help=f'BLLac Likeliehood <= <float>')
    _p.add_argument(f'--name', help=f'name <str>')
    _p.add_argument(f'--classification', help=f'Classification <str>')
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {FERMI_LAT_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {FERMI_LAT_SORT_VALUE}")

    # non-database query argument(s)ß
    _p.add_argument(f'--catalog', default=False, action='store_true', help=f'if present, download the catalog')
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    #try:
    fermi_lat_q3c_orm_cli(_args=_a)
    #except Exception as _:
    #    if bool(_a.verbose):
    #        print(f"{_}")
    #    print(f"Use: {__doc__}")
