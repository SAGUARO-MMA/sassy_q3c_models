#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.milliquas_q3c_orm_filters import *


# +
# __doc__ string
# -
__doc__ = """ python3 milliquas_q3c_orm_cli.py --help """


# +
# constant(s)
# -
ARXIV_PDF_URL = MILLIQUAS_PDF_URL
ARXIV_PDF_FIL = MILLIQUAS_PDF_URL.split("/")[-1]
ARXIV_DAT_URL = MILLIQUAS_DAT_URL
ARXIV_DAT_FIL = MILLIQUAS_DAT_URL.split("/")[-1]


# +
# __text__
# -
__text__ = """
VII/290    The Million Quasars (Milliquas) catalogue, version 7.2 (Flesch, 2021)
================================================================================
The Million Quasars (MILLIQUAS) catalogue, version 7.2.
   Flesch E.W.
   <Pub. Astron. Soc. Australia 32, 10 (2015)>
   =2015PASA...32...10F
   =2021yCat.7290....0F
================================================================================
ADC_Keywords: QSOs ; Active gal. nuclei ; Redshifts ; Magnitudes
Keywords: catalogs - quasars: general

Description:
    This is a compendium of 829666 type-I QSOs and AGN, largely complete
    from the literature to 30 April 2021 including SDSS-DR16 quasars and
    VLASS radio. Also included are 703348 candidates which are calculated
    as 60%-100% likely to be quasars, including 225051 which are
    radio/X-ray associated. Type-II and Bl Lac objects are also included,
    bringing the total count to 1573824. Gaia-DR2 astrometry is used
    where available, amounting to ~66% of all objects.

    Changes from version 7.1 are:
    (1) Quasars added from publications to 30 April 2021.
    (2) The VLASS Quick Look radio catalog is included, which adds 34189
        new radio core associations and 6793 probable double radio lobe
        associations.
    (3) Ongoing audits of SDSS & LAMOST quasars have led to a few
         additions & drops. Some WISEA-supported SDSS/LAMOST pipeline
         quasars are now accepted which were otherwise marginal. Also
         some likely galaxies removed.

    Low-confidence/quality or questionable objects (so deemed by their
    researchers) are not included in Milliquas. Additional quality cuts
    can apply as detailed in the HMQ paper (Flesch, 2015PASA...32...10F).
    Full QSO/AGN classification is via spectral lines, thus hidden /
    occluded objects may be absent from Milliquas. Two NIQs offset
    <2-arcsecs can be reported as a single object if within the same host.
    The aim here is to present one unique reliable object per each data
    row.

    The catalog format is simple, each object is shown as one line bearing
    the J2000 coordinates, its original name, object class, red and blue
    optical magnitudes, PSF class, redshift, the citations for the name
    and redshift, plus up to four radio/X-ray identifiers where
    applicable.

    Please cite as Milliquas v7.2, Flesch, E.W. 2021, arXiv:2105.12985 or
    as Milliquas v7.2 (2021) update, Flesch, E.W. 2015PASA...32...10F.

    Questions/comments/praise/complaints may be directed to me at
    eric(at)flesch.org.

File Summary:
--------------------------------------------------------------------------------
 FileName      Lrecl  Records   Explanations
--------------------------------------------------------------------------------
ReadMe            80        .   This file
catalog.dat      192  1573824   The catalogue (v7.2), 30-April-2021
refs.dat         162     2171   References (for numerical references)
--------------------------------------------------------------------------------

See also:
  VII/273 : The Half Million Quasars (HMQ) catalogue (Flesch, 2015)
  VII/277 : The Million Quasars (Milliquas) catalogue (V4.8) (Flesch, 2016)
  VII/280 : The Million Quasars (Milliquas) catalogue (V5.2) (Flesch, 2017)
  VII/283 : The Million Quasars (Milliquas) catalogue (V6.3) (Flesch, 2019)

Byte-by-byte Description of file: catalog.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label    Explanations
--------------------------------------------------------------------------------
   1- 11  F11.7 deg     RAdeg    Right ascension J2000 (deg) (1)
  13- 23  F11.7 deg     DEdeg    Declination J2000 (deg) (1)
  26- 50  A25   ---     Name     ID from the literature, or J2000 (2)
  52- 55  A4    ---     Type     Classification of object, and associations (3)
  57- 61  F5.2  mag     Rmag     ?=0 Red optical magnitude (4)
  63- 67  F5.2  mag     Bmag     ?=0 Blue optical magnitude (4)
  69- 71  A3    ---     Comment  Comment on optical object (5)
      73  A1    ---     R        Red Optical PSF class (6)
      75  A1    ---     B        Blue Optical PSF class (6)
  77- 82  F6.3  ---     z        ? Redshift from the literature or estimated (7)
  84- 89  A6    ---     rName    Citation for name (8)
  91- 96  A6    ---     rz       Citation for redshift (8)
  98-100  I3    pct     Qpct     ? Probability that this object is a QSO (9)
 102-123  A22   ---     XName    X-ray ID, if any (10)
 125-146  A22   ---     RName    Radio ID, if any (10)
 148-169  A22   ---     Lobe1    Radio lobe ID or extra R/X ID, if any (10)
 171-192  A22   ---     Lobe2    Radio lobe ID or extra R/X ID, if any (10)
--------------------------------------------------------------------------------
Note (1): These are to 7 decimals which suits Gaia-DR2 astrometry.

Note (2): Nameless radio/X-ray associated objects here show the J2000 position
     in HHMMSS.SS+DDMMSS.S for the convenience of the user.  If needing a name
     for it, just preface the J2000 with "MQ", e.g., MQ J000001.89+443053.8 .

Note (3): Legend of type/class:
     Q = QSO, type-I broad-line core-dominated, 790776 of these.
     A = AGN, type-I Seyferts/host-dominated, 38890 of these.
     B = BL Lac object, 2704 of these.
     L = lensed quasar extra image, only 64 of these in this optical data.
     K = NLQSO, type-II narrow-line core-dominated, 5316 of these.
     N = NLAGN, type-II Seyferts/host-dominated, 32726 of these.  Includes an
                unquantified residue of legacy NELGs/ELGs/LINERs.
     q = quasar candidate of the displayed QSO likelihood, 559424 of these.
     R = radio association displayed.
     X = X-ray association displayed.
     2 = double radio lobes displayed (declared by data-driven algorithm).

Note (4): Optical data is mostly from the ASP optical catalog 
     (Flesch, 2017PASA...34...25F) which presents data from the APM 
     (http://www.ast.cam.ac.uk/~mike/apmcat), USNO-A & USNO-B 
     (http://www.nofs.navy.mil), and the SDSS (http://sdss.org).
     APM/USNO-A magnitudes were recalibrated as documented in
     2004A&A...427..387F, so such USNO-A magnitudes are often used in
     preference to USNO-B. APM/USNO-B galaxies < mag 17 are usually shown
     too bright due to PSF modelling. Integer magnitudes (e.g., 22.00) are
     estimates if both bands are integer or one band empty. Note: many SDSS
     magnitudes are "extinction-corrected" ~0.3 mag brighter than observed.

Note (5): Legend as follows:
     p = optical magnitudes are POSS-I O (violet 4050A) and E (red 6400A).
          These are preferred because O is well-offset from E, and those plates
          were always taken on the same night, thus the red-blue color is
          correct even for variable objects.  Epoch is 1950's.
     j = optical magnitudes are SERC J (Bj 4850A) and R (red 6400A) from the
          POSS-II or UKST surveys.  Red-blue color is less reliable because the
          red & blue plates were taken in different epochs, i.e., years apart.
     b = blue magnitude is Vega 4400A (Johnson), red is 6400A (Cousins).
     g = blue magnitude is SDSS-type green 4900A, red is r 6200A.
     u = blue magnitude is SDSS ultraviolet 3850A.
     v = red magnitude is visual., i.e., white, 5500A midpoint.
     i = red magnitude is infrared 7500A.
     z = red magnitude is infrared z 8600A.
     r = red magnitude is r 6200A.
     (blank) =  Pan-STARRS r 6200A & g 4900A, but red alone is 6400A (Cousins).
     G = Gaia-DR2 astrometry shown, precessed to J2000 by CDS.  If 'G' is alone
          then the magnitudes are Gaia RP & BP, or Gaia G if red band only.
     + = variability nominally detected in both red/blue over multi-epoch data.
     m = proper motion nominally detected, from USNO-B.
     % = swap of two "unplugged" SDSS spectra which crossed wires (7 of these).
     a = object is host-dominated with faint nuclear activity, such as an SDSS
          pipeline galaxy with an AGN subclass or AGN-classed elsewhere, see its
          citation.  Milliquas class is 'A' if BROADLINE, else 'N'. (see note 2)

Note (6): The APM, USNO-B, and SDSS provide PSF class, albeit using different
     criteria. These are shown here as:
     - = point source / stellar PSF (APM notation: -1, here truncated)
     1 = fuzzy / galaxy shape       (APM notation: 1 and some 2)
     n = no PSF available, whether borderline or too faint to tell, etc.
     x = not seen in this band (fainter than plate depth, or confused, etc.)

Note (7):  Spectroscopic/grism redshifts are required for objects classified as
     Q/A/K/N/L and is optional for B (BL Lac type).  Photometric redshifts
     rounded to 0.1z can be displayed for B/R/X/2 objects, and are either taken
     from the cited catalogue or calculated here using the four-colour method of
     Flesch 2015PASA...32...10F, Appendix 2, using 4 colours from SDSS ugriz,
     Pan-STARRS grizy, or, for WISEA, the 4 colours B-R, R-W1, W1-W2, and W2-W3.

Note (8): Legend (with counts of name and redshift) and references:
  (for numerical reference code, see refs.dat file):

  2dF (357,211)         : 2dF galaxy survey, Colless M. et al.,
                           2001MNRAS.328.1039C, Cat. VII/250

  2QZ (27520,24157)     : Croom S.M. et al., 2004MNRAS.349.1397C, Cat. VII/241

  2SLAQ (10353,8679)    : Croom S.M. et al., 2009, Cat. J/MNRAS/392/19

  3FGL (16,11)          : Fermi cleanups, Paiano S. et al.,  2017ApJ...851..135P

  3FGL2 (21,19)         : Fermi cleanups II, Paiano S. et al.,
                           2019ApJ...871..162P

  3HSP (819,999)        : 3HSP blazars, Chang Y.-L. et al.,
                           2019A&A...632A..77C, Cat. J/A+A/632/A77

  3XLSS (25,25)         : The XXL Survey, Pierre M. et al.,
                           2016A&A...592A...1P, Cat, IX/49

  4FGL1 (15,3)          : Fermi cleanups, de Menezes R. et al.,
                           2019A&A...630A..55D

  4FGL2 (18,22)         : Fermi cleanups X, de Menezes R. et al.,
                           2020Ap&SS.365..12D

  4LAC (367,349)        : Fermi AGN v4 + LL, Fermi-LAT collab.,
                           2020ApJ...892..105A

  6dF (315,223)         : 6dF galaxy survey, Jones D.H. et al.,
                           2009MNRAS.399..683J, Cat. VII/259

  AAOz (1491,1498)      : AAOmega XXL-South: Lidman C. et al.,
                           2016PASA...33....1L

  AGES (2046,2046)      : AGES survey, Kochanek C.S. et al.,
                           2012, Cat. J/ApJS/200/8

  AGNELL (2,3)          : DES lenses, Agnello A. et al., 2015MNRAS.454.1260A

  AGNELA (4,4)          : SDSS J1433+6007 4-lens, Agnello A. et al.,
                           2018MNRAS.474.3391A

  AGNEL2 (13,13)        : VST-Gaia QSO pairs, Agnello A. et al.,
                           2018MNRAS.475.2086A

  AKARI (1,1)           : overlooked luminous quasar, Aoki K. et al.,
                           2011PASJ...63S.457A

  ALMA (4,4)            : ALMA hi-z, Roberto Decarli R. et al.,
                           2018ApJ...854...97D

  ANDIKA (2,2)          : Hi-z starbursts: Andika I.T. et al.,
                           2020ApJ...903...34A

  ANGUIT (1,1)          : COSMOS lens, Anguita T. et al., 2009A&A...507...35A

  ATel (5,5)            : Astronomers Telegraph posts,
                           http://www.astronomerstelegram.org

  ATHENS (86,108)       : VIPERS AGN SEDs, Pouliasis E. et al.,
                           2020MNRAS.495.1853P, Cat. J/MNRAS/495/1853

  ATLAS (229,269)       : Mao M.Y. et al., 2012, Cat. J/MNRAS/426/3334

  BAHM (24,24)          : dust-reddened QSOs, Banerji M. et al.,
                           2015MNRAS.447.3368B

  BASS (16,113)         : Swift-BAT AGN, Koss M. et al., 2017, Cat. J/ApJ/850/74

  BERGHE (1,1)          : Pan-STARRS lens, Berghea C.T. et al.,
                           2017ApJ...844...90B

  BGGFC (4,4)           : COSMOS hi-z, Boutsia K. et al., 2018ApJ...869...20B

  BLAZZ (0,8)           : Blazar redshifts, Goldini P. et al.,
                           2020,arXiv:2012.05176

  BMCGCS (1,1)          : Belladitta S. et al., 2019A&A...629A..68B

  BMCS (1,1)            : Blazar at z>6, Belladitta S. et al.,
                           2020A&A...635L...7B

  BQLS (16,16)          : BOSS QSO lenses & pairs, More A. et al.,
                           2016MNRAS.456.1595M

  BZCAT (4,3)           : Blazars catalog, Massaro E. et al.,
                           http://www.asdc.asi.it/bzcat

  C-COSM (180,180)      : Chandra COSMOS IDs, Marchesi S. et al.,
                           2016ApJ...817...34M

  ChaMP (191,187)       : Trichas M. et al., 2012ApJS..200...17T

  DABAST (1,1)          : Diaz-Santos T. et al., 2018Sci...362.1034D

  Dart (26,25)          : Heavily Obscured QSOs, Hviding R. et al.,
                           2018MNRAS.474.1955H

  DDC2 (14,14)          : variable AGN, De Cicco D. et al., 2019,
                           Cat. J/A+A/627/A33

  DEEP (143,139)        : DEEP2, Newman J. et al., 2013ApJS..208....5N;
                           deep.ps.uci.edu/DR4

  DES (1,1)             : Dark Energy hi-z, Reed S.L. et al.,
                           2015MNRAS.454.3952R

  DESQQ (26,26)         : STRIDES lenses, Anguita T. et al., 2018MNRAS.480.5017A

  DESQQ2 (12,12)        : STRIDES lenses, Treu T. et al., 2018MNRAS.481.1041T

  DPeake (683,656)      : Double-peaked NELGs, Ge J.-Q. et al., 2012,
                           Cat. J/ApJS/201/31

  DR12 (6,6)            : Alam S. et al., 2015ApJS..219...12A,
                           https://sdss.org/dr12

  DR12Q (244,15)        : SDSS-DR12Q, Paris I. et al., 2017A&A...597A..79P,
                           Cat. VII/279

  DR14 (12,44)          : Abolfathi B. et al., 2018ApJS..235...42A, pipeline,
                           data at
                           https://data.sdss.org/sas/dr14/sdss/spectro/redux

  DR14Q (1527,1538)     : SDSS-DR14Q, Paris I. et al., 2018A&A...613A..51P
                           data at
                           https://data.sdss.org/sas/dr14/eboss/qso/DR14Q

  DR16 (41065,374519)   : Ahumada R. et al., 2020ApJS..249....3A, pipeline,
                           data at
                           https://data.sdss.org/sas/dr16/sdss/spectro/redux

  DR16Q (715827,395233) : SDSS-DR16Q, Lyke B. et al., 2020ApJS..250....8L
                           2 files, data at
                           https://data.sdss.org/sas/dr16/eboss/qso/DR16Q

  DR16QN (0,2132)       : same as above, using the QuasarNET redshift supplied.

  DR7 (2,26)            : SDSS DR7, Abazajian K.N. et al., 2009ApJS..182..543A
                           files at
               http://classic.sdss.org/dr7/products/spectra/getspectra.html

  DR7Q (1967,200)       : SDSS Quasar DR7, Schneider D. et al.,
                           2010AJ....139.2360S, Cat. VII/26 data
               http://classic.sdss.org/dr7/products/value_added/qsocat_dr7.html

  DUALQ (1,1)           : Dual QSOs HSC, Silverman J.D. et al.,
                           2020ApJ...899..154S

  DUHIZ (2,2)           : DECaLS-UKIRT hi-z, Wang F. et al.,
                           2017ApJ...839...27W

  Dusty (11,11)         : Dusty Starbursts, Rodighiero G. et al.,
                           2019ApJ...877...38H

  DUz6 (18,18)          : DESI & UKIRT hi-z, Wang F. et al., 2019ApJ...884...30W

  eHAQ (82,80)          : Extended High AV, Krogager J.-K., 2016ApJ...832...49K

  ELQ-PS (216,215)      : ELQS on PS1, Schindler J.-T. et al.,
                           2019, Cat. J/ApJS/243/5

  ELQS-N (38,38)        : ELQS in NGC, Schindler J.-T. et al.,
                           2018ApJ...863..144S

  ELQS-S (126,126)      : ELQS in SGC, Schindler J.-T. et al.,
                           2019ApJ...871..258S

  FISCBA (1,1)          : HST lens, Fischer/Schade/Barrientos,
                           1998ApJ...503L.127F

  FLES40 (40,0)         : Salvaged QSOs, Flesch E.W., 2021MNRAS.504..621F

  FYNBO (1,1)           : LiBAL QSO, Fynbo J.P.U. et al., 2020A&A...634A..11D

  GAIA1 (21,21)         : Gaia DR1, Gaia Collaboration et al.,
                           2016A&A...595A...1G, Cat. I/337

  GAIA2 (236,232)       : Gaia DR2, Gaia Collaboration et al.,
                           2018A&A...616A...1G, Cat. I/345 (GAIA data as
                           presented by SIMBAD,
                           http://simbad.u-strasbg.fr/simbad)

  GEIER (1,1)           : Geier S.J. et al., 2019A&A...625L...9G

  GGLS (3,4)            : Gaia GraL, Krone-Martins A. et al.,
                           2019, arXiv:1912.08977

  GLDD (1,1)            : Lensed QSO data-driven, Ostrovski F. et al.,
                           2017MNRAS.465.4325O

  GLIKMA (28,28)        : red WISE QSOs, Glikman E. et al.,
                           2018, Cat. J/ApJ/861/37

  GLOH (1,1)            : Grav Lensed Objs HSC, Jaelani A.T. et al.,
                           2020,arXiv:2006.16584

  GLRED (1,1)           : lensed red QSO, Glikman E. et al.,
                           2018,arXiv:1807.05434

  GQ (2,2)              : serendipitous binary, Altamura E. et al.,
                           2020AJ....159..122A

  GRAL4 (10,10)         : Gaia Grav Lens quads, Stern D. et al.,
                           2020,arXiv:2012.10051

  GUTI (1,1)            : not a ULX, Gutierrez C.M., 2013A&A...549A..81G

  GZPM (23,23)          : Gaia zero pm, Heintz K.E. et al.,
                           2020, Cat. J/A+A/644/A17

  H-DOGs (16,16)        : Herschel DOGs, Riguccini L.A. et al.,
                           2019A&A...625A...9D

  HAQ (2,2)             : High AV serendipitous, Heintz K.E. et al.,
                           2016AJ....152...13H

  HAQC (1,1)            : High AV in COSMOS, Heintz K.E. et al.,
                           2016A&A...595A..13H

  HE2QS (103,103)       : HeII quasar survey, Schmidt T.M. et al.,
                           2017, Cat. J/ApJ/847/81

  HE2QS2 (5,5)          : HeII HST/COS quasars, Worseck G. et al.,
                           2019ApJ...875..111W

  HEINTZ (1,1)          : dusty absorbed QSO, Heintz K.E. et al.,
                           2018A&A...615A..43H

  HIZ7.5 (1,1)          : QSO z=7.5, Banados E. et al., 2018Natur.553..473B

  HSC (3,3)             : Low-luminosity QSOs, Niida M. et al.,
                           2020ApJ...904...89N

  HSTvar (42,42)        : variable AGN, Pouliasis E. et al.,
                           2019, Cat. J/MNRAS/487/4285

  ICECUB (9,12)         : IceCube spectra, Paiano S. et al.,
                           2021,arXiv:2104.05290

  IGMCP (10,10)         : IGM close pairs, Rorai A. et al., 2017Sci...356..418R

  IKEDA (1,1)           : Ikeda H. et al., 2017ApJ...846...57I

  IMDS (3,3)            : IR medium-deep hi-z VII, Shin S. et al.,
                           2020ApJ...893...45S

  IMS (1,1)             : IR medium-deep hi-z, Kim Y. et al.,
                           2015ApJ...813...35H

  IMS2 (10,11)          : IR medium-deep hi-z, Kim Y. et al.,
                           2019ApJ...870...86K

  INAF (1,1)            : UV bright hi-z, Grazian A. et al., 2020ApJ...897...94G

  JERAM (1,1)           : extremely bright, Jeram S. et al., 2020ApJ...899...76J

  JPLUS (24,24)         : luminous Ly, Spinoso D. et al.,
                           2020, Cat. J/A+A/643/A149

  K4K (2,2)             : K4000 bz, Uwitonze/Nkundabakura/Mutabazi,
                           2020, arXiv:2004.03154

  KHOR1 (7,6)           : 3XMM hi-z, Khorunzhev G.A. et al., 2017,AstL,43,135

  KHOR2 (11,11)         : 3XMM hi-z, Khorunzhev G.A. et al., 2019AstL...45..411K

  KHOR3 (1,1)           : X-ray luminous, Khorunzhev G.A. et al.,
                           2021, arXiv:2104.05142

  KODQ3 (4,4)           : KODIAQ DR3, O'Meara J.M. et al., 2020,arXiv:2010.09061

  KOVACS (1,1)          : bright QSO behind Milky Way, Kovacs T. et al.,
                           2019, RNAAS, 3, 3

  LAMDR6 (2966,3341)    : LAMOST-DR6, pipeline, http://dr6.lamost.org

  LAMQ1 (684,625)       : LAMOST QUASAR DR1, Ai Y.L. et al.,
                           2016, Cat. J/AJ/151/24

  LAMQ3 (6698,6587)     : LAMOST QUASAR DR3/DR2, Dong X.Y. et al.,
                           2018, Cat. J/AJ/155/189
  LAMQ5 (7938,7937)     : LAMOST QUASAR DR5/DR4, Yao S. et al.,
                           2019ApJS..240....6Y

  LEMON (40,40)         : 24 Gaia lenses, Lemon C. et al., 2018MNRAS.479.5060L

  LEMON2 (30,30)        : 22 Gaia lenses, Lemon/Auger/McMahon,
                           2019MNRAS.483.4242L

  LEMON3 (53,52)        : STRIDES lenses etc, Lemon C. et al.,
                           2020MNRAS.494.3491L

  LGGS (11,11)          : M31/M33 area, Massey/Neugent/Levesque,
                           2019AJ....157..227M

  LIDMAN (1,1)          : SN Host Galaxy redshifts, Lidman C. et al.,
                           2013PASA...30....1L

  LIN (1,1)             : DES lens, Lin H. et al., 2017ApJ...838...15L

  LIRAS (169,154)       : LoCuSS IR AGNs, Xu, L. et al.,
                           2015, Cat. J/ApJS/219/18

  LOZAGN (38,10997)     : Low-redshift AGN, Liu H.-Y. et al.,
                           2019, Cat. J/ApJS/243/21

  LSSA (2,1)            : 2 lenses, Lucey/Schechter/Smith/Anguita,
                           2018MNRAS.476..927L

  LUMIz5 (66,66)        : Luminous hi-z, Yang J. et al., 2019ApJ...871..199Y

  M31UV (1,1)           : UV flare QSO on M31, Meusinger H. et al.,
                           2010A&A...512A...1M

  MALS-N (69,68)        : MEERKAT QSOs, Krogager J.-K. et al.,
                           2018ApJS..235...10K

  MFJC (52,51)          : McGreer I.D., Fan X., Jiang L. & Cai Z.,
                           2018, Cat. J/AJ/155/131

  MQ (143925,539324)    : MILLIQUAS, original data in this catalog, Flesch E.,
                           2021

  NBCKDE (2559,2656)    : Richards G.T. et al., 2009, Cat. J/ApJS/180/67

  NBCKv3 (13224,67795)  : NBCKDE v3, Richards G.T. et al.,
                           2015, Cat. J/ApJS/219/39

  NED (5,6)             : NASA/IPAC Extragalactic Database,
                           https://ned.ipac.caltech.edu

  OGLE2 (2,2)           : OGLE quasars, Kozlowski S. et al., 2019ApJ...878..115K

  OVRLAP (5,5)          : SDSS overlap hi-z QSOs, Jiang L. et al.,
                           2015AJ....149..188J

  OzDES (608,435)       : Dark Energy SN QSOs, Tie S.S. et al.,
                           2017AJ....153..107T

  OzDES2 (751,921)      : DESN QSOs, Lidman C. et al., 2020MNRAS.496...19L

  P352-1 (1,1)          : P352-15, Banados E. et al., 2018ApJ...861L..14B

  PETERS (245,268)      : photo special., Peters C.M. et al, 2015ApJ...811...95P

  PFTS (2,11)           : blazar spectroscopy, Paiano S. et al.,
                           2020MNRAS.497...94P

  PGC (12914,8)         : Principal Galaxy Catalog, Paturel G. et al.,
                           2003A&A...412...45P, Cat. VII/237

  PHILLI (1,0)          : MERLIN lens, Phillips P.M. et al., 2000MNRAS.319L...7P

  PS1 (63,63)           : PAN-STARRS1 hi-z, Banados E. et al.,
                           2016, Cat. J/ApJS/227/11

  PS1hiz (1,1)          : Tang, Ji-Jia et al., 2017MNRAS.466.4568T

  PS1MAZ (6,6)          : Mazzucchelli C. et al., 2017ApJ...849...91M

  PSO (3,3)             : PAN-STARRS z-dropouts, Venemans B.P. et al.,
                           2015ApJ...801L..11V

  QLSV (21,20)          : QUEST-La Silla, Sanchez-Saez P. et al.,
                           2019ApJS..242...10S

  QPQ10 (70,70)         : Quasar pair DB, Findlay J.R. et al.,
                           2018ApJS..236...44F

  QUBRIC (91,91)        : QUBRICS I, Calderone G. et al., 2019ApJ...887....2Y

  QUBRIX (249,252)      : QUBRICS II, Boutsia K. et al., 2020ApJS..250...26B

  RBS (3,3)             : Laporte N. et al., 2017ApJ...851...40L

  Redden (25,25)        : Reddened QSOs, Temple M.J. et al., 2019MNRAS.487.2594R

  REQ4 (6,6)            : Reionization-Era quasars, Yang J. et al.,
                           2019AJ....157..236Y

  REQ7 (1,1)            : Reionization-Era QSO z=7.5,Yang J. et al.,
                           2020ApJ...897...14C

  RLQ (4,3)             : Tuccillo D./Gonzalez-Serrano J.I./Benn C.R.,
                           2015, Cat. J/MNRAS/449/2818

  RSG (1,1)             : Dorn-Wallenstein T.Z. & Levesque E.,
                           2017, IAUS, 329, 376

  S82X (71,75)          : Stripe 82 AGN, LaMassa S.M. et al.,
                           2019ApJ...876...50L

  S82XRQ (8,8)          : Red Quasars, LaMassa S.M. et al., 2017ApJ...847..100L

  SAGE1 (1,1)           : SAGE IR AGN, Hony S. et al., 2011A&A...531A.137H

  SCULPT (2,3)          : Sculptor X-ray, Arnason R. M. et al.,
                           2019MNRAS.485.2259A

  SDLENS (3,3)          : SDSS Lenses, Williams P.R. et al., 2018MNRAS.477L..70W

  SDSSHI (6,6)          : SDSS hi-z, Jiang L. et al., 2016ApJ...833..222J

  SELMAN (1,1)          : serendipitous, Selman F.J. et al., 2020AN...341...26S

  SFM201 (1,1)          : Schulze S. et al., 2012A&A...546A..20S

  SHELLQ (33,33)        : Subaru hi-z, Matsuoka Y. et al., 2018PASJ...70S..35M

  SHELQ3 (28,28)        : Subaru hi-z, Matsuoka Y. et al., 2019ApJ...883..183M

  SHELQS (30,30)        : SHELLQS hi-z, Matsuoka Y. et al., 2018ApJS..237....5M

  SHELz7 (1,1)          : SHELLQS z=7, Matsuoka Y. et al., 2019ApJ...872L...2M

  SMSSQ (2,2)           : SkyMapper hi-z, Zefeng Li Z. et al.,
                           2018,arXiv:1805.03429

  SOLARZ (13,13)        : AllWISE anomalies, Solarz A. et al.,
                           2020A&A...642A.103S

  SPIN18 (1,1)          : KiDS-SQuaD lens, Spiniello C. et al.,
                           2018MNRAS.480.1163S

  SPIN19 (2,2)          : 2 lensed quasars, Spiniello C. et al.,
                           2019MNRAS.485.5086S

  SQLS (60,51)          : SDSS DR7 QSO Lens Search, Inada N. et al.,
                           2012, Cat. J/AJ/143/119

  SQUAD (13,13)         : UVES DB DR1, Murphy M.T. et al., 2019MNRAS.482.3458M

  SSLENS (3,3)          : South sky lenses, Spiniello C. et al.,
                           2019MNRAS.483.3888S

  SUV (22,22)           : SDSS-ULAS/VHS QSOs, Yang J. et al.,
                           2017AJ....153..184Y

  SXDF (39,39)          : Subaru-XMMDF redshifts, Simpson C. et al.,
                           2012, Cat. J/MNRAS/421/3060

  SXDS (307,306)        : Subaru-XMMDF spectra, Akiyama M. et al.,
                           2015PASJ...67...82A

  ULTRA (1,1)           : Ultraluminous hi-z, Wu, X.-B. et al.,
                           2015Natur.518..512W

  UVQS (435,503)        : UV QSOs, Monroe T.R. et al., 2016, Cat. J/AJ/152/25

  VAHIZ (2,2)           : VST ATLAS hi-z, Carnall A.C. et al.,
                           2015MNRAS.451L..16C

  VAHIZ2 (1,1)          : bright z>6 QSOs, Chehade B. et al.,
                           2018MNRAS.478.1649C

  VAHIZ3 (1,1)          : VST-ATLAS lens, Schechter P.L. et al.,
                           2018, RNAAS, 2b, 21

  VAQL (11,11)          : VST-ATLAS quasar systems,Schechter P.L. et al.,
                           2017AJ....153..219S

  VDES (8,8)            : VISTA Dark Energy QSOs, Reed S.L. et al.,
                           2017MNRAS.468.4702R

  VDES2 (2,2)           : more VHS-DES quasars, Reed S.L. et al.,
                           2019MNRAS.487.1874R

  VIKING (4,4)          : VIKING IR, Venemans, G.A. et al., 2015MNRAS.453.2259V

  VIPERS (241,283)      : VIPERS PDR-2, Scodeggio M. et al., 2018A&A...609A..84S

  VMC (34,34)           : Magellanic IR QSOs, Ivanov V.D. et al.,
                           2016A&A...588A..93I

  WARSAW (3,3)          : OGLE lens, Kostrzewa-Rutkowska Z. et al.,
                           2018MNRAS.476..663K

  WERTZ (1,1)           : Gaia GraL lens, Wertz O. et al., 2019A&A...628A..17W

  WGD (2,2)             : DES/Gaia lenses; Agnello A. et al.,
                           2018MNRAS.479.4345A

  WILLIG (1,1)          : Williger, G., 2020, p comm., data on LJMU Robotic
                           Telescope

  WISEA (522905,0)      : AllWISE QSO candidates, Secrest N. et al.,
                           2015, Cat. J/ApJS/221/12

  WISEHI (72,70)        : Hi-z QSOs from WISE, Wang F. et al.,
                           2016, Cat. J/ApJ/819/24

  WOLF1 (1,0)           : most ultraluminous QSO, Wolf C. et al.,
                           2018PASA...35...24W

  WOLF2 (16,16)         : hi-z ultraluminous QSOs, Wolf C. et al.,
                           2020MNRAS.491.1970W

  WYFH (1,1)            : z=7.642 quasar, Wang F. et al., 2021,arXiv:2101.03179

  XDQSO (20119,0)       : SDSS-XDQSO, Bovy J. et al., 2011ApJ...729..141B

  XLSS (306,118)        : Stalin C.S. et al., 2010, Cat. J/MNRAS/401/294

  XMM2 (12,12)          : 2XMM-Newton cross-search, Combi J.A. et al.,
                           2011Ap&SS.331...53C, Cat. V/138

  XMMSMC (6,6)          : SMC quasars, Maitral C. et al., 2019A&A...622A..29M

  XMSS (182,148)        : Barcons X. et al., 2007, Cat. J/A+A/476/1191

  XWAS (490,449)        : Esquej P. et al., 2013, Cat. J/A+A/557/A123

  YQLF (25,25)          : deep CFHT QSOs, Yang J. et al.,
                           2018, Cat. J/AJ/155/110

  YSZ (0,414)           : Type 2 QSOs IDd, Yuan/Strauss/Zakamska,
                           2016,arXiv:1606.04976

  z6.51 (1,1)           : lensed quasar z=6.51, Fan X. et al.,
                           2019ApJ...870L..11F

  z6.82 (1,1)           : radio-loud z=6.82, Banados E. et al.,
                           2021,arXiv:2103.03295

  z7.02 (1,1)           : lensed quasar z=7.02, Wang F. et al.,
                           2018ApJ...869L...9W

  4-digit numeric citations are indexed in the HMQ (2015PASA...32...10F)
  references list. The citation for the classification (e.g., that the
  object is a quasar) is from either the name or redshift citation.

Note (9): For QSO candidates (class starting with q/R/X/2) this shows its pQSO
  (percent chance that it is a QSO) based on radio/X-ray association and/or
  photometric analysis. Radio/X-ray based likelihoods are calculated as
  described in Flesch & Hardcastle, 2004A&A...427..387F. WISEA photometric
  pQSOs are calibrated all-sky via the colours B-R, R-W1, W1-W2, and W2-W3,
  using the method of Flesch 2015PASA...32...10F, Appendix 2.  SDSS-based
  candidates from NBCKDE/NBCKv3/XDQSO/Peters (see Note 7 for citations)
  photometric catalogs can also have photometric-based pQSOs which are here
  calibrated against SDSS-DR16Q classified objects using 4-colour matching.

  The calibrated photometric pQSO (P1) and radio/X-ray derived pQSO (P2),
  if both present, are combined into a single pQSO as
    pQSO = 1/(1+((1-P1)*(1-P2))/(P1*P2)).

  For a fully classified object (class starting with Q/A/B/K/N/L), this
  shows the percent chance that a shown radio/X-ray detection(s) is truly
  associated to it. If no radio/X-ray detection, value is blank.

Note (10): Four columns of Radio/X-ray detections are presented:
   * 1st column: best X-ray detection (i.e. highest probability association).
   * 2nd column: best core Radio detection.
   * 3rd column: a radio lobe if the description (see note 2) shows a "2",
                 otherwise this is an additional radio or X-ray detection.
   * 4th column: a radio lobe if the description (see note 2) shows a "2",
                 otherwise this is an additional radio or X-ray detection.

   Legend of Radio/X-ray detection prefixes and catalog home pages:

   FIRST: VLA FIRST survey, 13Jun05 version, http://sundog.stsci.edu
   VL0 (abbrev of VLASS1QLCIR): VLASS Quick Look, https://cirada.ca/catalogues
   NVSS: NRAO VLA sky survey, http://www.cv.nrao.edu/nvss
   SUMSS: Sydney U. Molonglo, http://www.astrop.physics.usyd.edu.au/sumsscat/
   MGPS: Molonglo galactic plane, www.astrop.physics.usyd.edu.au/mgpscat/
   ROSAT catalogs available from http://cdsarc.u-strasbg.fr/cats/IX.htx are:
    - IX/28A is 1RXH: ROSAT HRI (high resolution imager)
    - IX/30 is 2RXP: ROSAT PSPC (position sensitive proportional counter)
    - IX/10A & IX/29 are 1RXS: ROSAT RASS (all-sky survey, bright & faint)
   2RXF: https://heasarc.gsfc.nasa.gov/W3Browse/rosat/rospspcftot.html
   2RXS: 2nd RASS source catalog, http://www.mpe.mpg.de/ROSAT
   1WGA: White, Giommi & Angelini, wgacat.gsfc.nasa.gov/wgacat/wgacat.html
   CXOG: Chandra ACIS source catalog, Wang S. et al., 2016,ApJS,224,40
   CXO:  Chandra Source Catalog v1.1, http://cxc.harvard.edu/csc
   2CXO: Chandra Source Catalog v2, http://cxc.harvard.edu/csc
   CXOX: XAssist Chandra source list, http://xassist.pha.jhu.edu/
   2XMM/2XMMi: XMM-Newton DR3, http://cdsarc.u-strasbg.fr/cats/IX.htx IX/39&40
   4XMM: XMM-Newton DR10, https://www.cosmos.esa.int/web/xmm-newton/xsa
   XMMSL: XMM-Newton Slew Survey Release 2.0, same attribution as 4XMM
   XMMX: XAssist XMM-Newton source list, http://xassist.pha.jhu.edu/
   2SXPS: Swift X-ray Point Source catalog, http://www.swift.ac.uk/2SXPS

   Optical field solutions are calculated from the raw source positions of all
   these catalogs (except 2CXO) as described in my MORX paper,
   Flesch, 2016PASA...33...52F.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: refs.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  4  I04   ---     Ref       Reference number
   6- 11  I6    ----    N1        ? Number of this reference for Name
  13- 18  I6    ---     N2        ? Number of this reference for redshift
  21- 39  A19   ---     Bibcode   BibCode
  41- 71  A31   ---     Aut       Author's name
  73-162  A90   ---     Com       Comments
--------------------------------------------------------------------------------

Acknowledgements:
    If using this catalogue in published research, please cite as
    Milliquas v7.2, Flesch, E.W. 2021, arXiv:2105.12985 , or as
    Milliquas v7.2 (2021) update, Flesch, E.W. 2015PASA...32...10F.


    The confirmed quasars of this catalog (to Jan 2015) were published as
    the Half Million Quasars (HMQ) catalog: Flesch E., 2015PASA...32...10F.
    Note however that Milliquas uses optical sky data from ASP
    (2017PASA...34...25F) whereas the HMQ used optical sky data from QORG
    (2004A&A...427..387F, Cat. J/A+A/427/387) Appendix A.

    This research has made use of the NASA/IPAC Extragalactic Database
    (NED) which is operated by the Jet Propulsion Laboratory,California
    Institute of Technology, under contract with the National Aeronautics
    and Space Administration.

    This research has made use of the SIMBAD database and CDS cross-match
    service (to obtain Gaia DR2 data) provided by CDS, Strasbourg, France.

History:
    From Eric Flesch, eric(at)flesch.org

================================================================================
(End)                                      Patricia Vannier [CDS]    03-May-2021
"""


# +
# __refs__
# -
__refs__ = """
   1             6  2005AJ....130...23A Aars C.E. et al.                
   2    125   1491  2003AJ....126.2081A Abazajian K.N. et al.           (SDSS DR1)
   3    133      1  2004AJ....128..502A Abazajian K.N. et al.           (SDSS DR2)
   4   2597   1927  2005AJ....129.1755A Abazajian K.N. et al.           (SDSS DR3)
   5   1759   2507  2009ApJS..182..543A Abazajian K.N. et al.           (SDSS DR7)
   6             1  2011MNRAS.417.1891A Abdalla F.B. et al.             (MegaZ-LRG)
   7      1         1990Ap.....32...14A Abramian G.V. et al.            
   8      1         1990Ap.....33..418A Abramian G.V. et al.            
   9      1         1990Ap.....33..493A Abramian G.V. et al.            
  10             1  1991A&AS...87..499A Acker A. et al.                 
  11    315     97  2011ApJ...743..171A Ackermann M. et al.             
  12      1         1977AJ.....82..857A Adams M.T., Rudnick L.          
  13    855   1237  2006ApJS..162...38A Adelman-McCarthy J.K. et al.    (SDSS DR4)
  14    823   1308  2007ApJS..172..634A Adelman-McCarthy J.K. et al.    (SDSS DR5)
  15   1043   1487  2008ApJS..175..297A Adelman-McCarthy J.K. et al.    (SDSS DR6)
  16      1         1975MNRAS.170p..31A Adgie R.L. et al.               
  17      1      1  1979AN....300...31A Afanasjev V.L. et al.           
  18      2      1  1979AN....300...77A Afanasjev V.L. et al.           (Tautenburg Objective Prism Survey)
  19                1979Ap.....16..119A Afanasjev V.L. et al.           
  20      1      1  ................... Afanasjev V.L. et al.           1989, SvAL, 15, 83
  21             1  ................... Afanasjev V.L. et al.           1990, BSAO, 1, 32
  22      2      2  2003ARep...47..458A Afanasjev V.L. et al.           
  23      6      6  2006ARep...50..255A Afanasjev V.L. et al.           
  24      3      1  2009ARep...53..287A Afanasjev V.L. et al.           
  25      1      1  2007A&A...476L..17A Agudo I. et al.                 (NRAO 150)
  26             2  1996PASP..108.1117A Aguero E.L. et al.              
  27   2952   2770  2012ApJS..203...21A Ahn C.P. et al.                 (SDSS DR9 http://sdss3.org/dr9)
  28   2591   2300  2014ApJS..211...17A Ahn C.P. et al.                 (SDSS DR10 http://sdss3.org/dr10)
  29   3417   1762  2011ApJS..193...29A Aihara H. et al.                (SDSS DR8)
  30     14     11  2000ApJ...532..700A Akiyama M. et al.               
  31     48     37  2003ApJS..148..275A Akiyama M. et al.               
  32             1  1997Ap.....40..114A Akopian S. et al.               
  33      2         1989A&AS...80..215A Akujor C.E. et al.              
  34   4261   5781  ................... Alam S. et al.                  2015, ArXiv 1501, 963 (SDSS DR12  http://sdss.org/dr12)
  35             9  1994ApJS...93....1A Aldcroft T.L. et al.            
  36      4      4  2001ApJ...554...18A Alexander D.M. et al.           
  37      2      5  1991MNRAS.248..528A Allen D.A. et al.               
  38                1992MNRAS.259...67A Allen S.W. et al.               
  39      7         1982MNRAS.201..331A Allington-Smith J.R. et al.     
  40      1         1985MNRAS.213..243A Allington-Smith J.R. et al.     
  41                1988MNRAS.234.1091A Allington-Smith J.R. et al.     
  42      1      2  1991MNRAS.253..287A Allington-Smith J.R. et al.     
  43                1992A&A...266..117A Alloin D. et al.                
  44                2000ApJ...528L..81A Alloin D. et al.                
  45      1      1  1993ARep...37..466A Amirkhanyan V.R. et al.         
  46      8      8  2004AstL...30..834A Amirkhanyan V.R. et al.         (Zelenchuk radio)
  47      1      1  2006Ap.....49..184A Amirkhanyan V.R. et al.         (Z0254+43)
  48      5      2  2009SerAJ.179....7A Anderson M. et al.              (KEYFIELD)
  49     59      5  ................... Anderson S.F. et al.             1985, Ph.D. thesis University of Washington
  50      1     39  1987ApJ...314..111A Anderson S.F. et al.            
  51      1      1  1987Natur.327..125A Anderson S.F. et al.            
  52      3      2  2001AJ....122..503A Anderson S.F. et al.            
  53     17      2  2003AJ....126.2209A Anderson S.F. et al.            
  54     81      8  2007AJ....133..313A Anderson S.F. et al.            
  55                1994A&AS..107...23A Andreasian N. et al.            
  56      3      3  1994A&A...291..411A Angonin-Willaime M.C. et al.    
  57      5         1977AJ.....82..102A Anguita A.C. et al.             
  58      3         1979AJ.....84..718A Anguita A.C. et al.             
  59             1  1985ApJ...297..621A Antonucci R.R.J. et al.         
  60             1  1987AJ.....93..785A Antonucci R.R.J. et al.         
  61             1  1994Natur.371..313A Antonucci R.R.J. et al.         
  62      1         1978Natur.273..450A Apparao K.V. et al.             
  63    175    143  1998ApJS..117..319A Appenzeller I. et al.           
  64             1  2000A&A...364..443A Appenzeller I. et al.           
  65      5         1996MNRAS.281..945A Aragon-Salamanca A. et al.      
  66      1         1975SoByu..47....3A Arakelian M.A. et al.           
  67      5         1980MNRAS.192..779A Argue A.N. et al.               
  68             1  1989ApJ...347..727A Armus L. et al.                 
  69      4      1  ................... Arnaud K.A. et al.              1984 'An optically selected sample of X-ray-quiet QSOs'
  70      1         1985MNRAS.217..105A Arnaud K.A. et al.              
  71      3         1966ApJS...14....1A Arp H. et al.                   
  72      2      1  1975ApJ...198L...3A Arp H. et al.                   
  73      1      1  ................... Arp H. et al.                   1977 Colloq. Int. N263 (Paris CNRS) 1, 377
  74      1      6  1979A&A....77...86A Arp H. et al.                   
  75      8      5  1979ApJ...229..489A Arp H. et al.                   
  76      2      3  1979ApJ...229..496A Arp H. et al.                   
  77     10      5  1980ApJ...236...63A Arp H. et al.                   
  78      3      2  1980ApJ...240..415A Arp H. et al.                   
  79      9      2  1980ApJ...240..726A Arp H. et al.                   
  80      3      2  ................... Arp H. et al.                   1980 Proc. 9th Texas Symp. Ann. New-York Acad. Sci. 336, 94
  81     14      7  1981ApJ...250...31A Arp H. et al.                   
  82     13      6  1982A&A...109..101A Arp H. et al.                   
  83      3      4  1983ApJ...271..479A Arp H. et al.                   
  84      1      2  1984A&A...138..179A Arp H. et al.                   
  85      1      1  1984A&A...139..240A Arp H. et al.                   
  86     25     26  1984ApJ...285...44A Arp H. et al.                   
  87      7     12  1984ApJ...285..547A Arp H. et al.                   
  88     10     10  1985PASP...97.1149A Arp H. et al.                   
  89      1         ................... Arp H. et al.                   1987 'Quasars redshifts and controversies'  Interstellar media
  90      4      2  2001ApJ...553L..11A Arp H.C. et al.                 
  91      2         2004A&A...418..877A Arp H. et al.                   
  92                1992AJ....104..980A Ashby M. et al.                 
  93             1  1994A&AS..104..259A Augarde R. et al.               
  94             1  1985Msngr..39...12A Azzopardi M. et al.             
  95             1  1988A&A...189...34A Azzopardi M. et al.             
  96      1         1954ApJ...119..215B Baade W. et al.                 
  97      1         1998ApJ...509..633B Baan W.A. et al.                
  98      2     15  2008A&A...488..887B Bachev R. et al.                
  99             2  1994A&A...286..381B Bade N. et al.                  
 100     74     84  1995A&AS..110..469B Bade N. et al.                  
 101      1     13  1998A&A...334..459B Bade N. et al.                  
 102    123         1998A&AS..127..145B Bade N. et al.                  
 103      7      5  1973ApJ...183..777B Bahcall N.A. et al.             
 104      2         1968MNRAS.138...51B Bailey J. et al.                
 105      2     85  1999ApJS..122...29B Baker J.C. et al.               
 106     21         1973ApJ...185..739B Baldwin J.A. et al.             
 107             2  1975ApJ...201...26B Baldwin J.A. et al.             
 108      3         1976ApJ...206L..83B Baldwin J.A. et al.             
 109             1  1978Natur.273..431B Baldwin J.A. et al.             
 110             3  1981ApJ...243...76B Baldwin J.A. et al.             
 111      3      1  1988ApJ...327..103B Baldwin J.A. et al.             
 112             3  1989ApJ...338..630B Baldwin J.A. et al.             
 113      1      1  1996ApJ...461..664B Baldwin J.A. et al.             
 114      8      8  2014AJ....148...14B Banados E. et al.               (Pan-Starrs hi-z)
 115      6      6  2012MNRAS.427.2275B Banerji M. et al.               (UKIDSS red QSOs)
 116      2      2  2013MNRAS.429L..55B Banerji M. et al.               (VISTA-WISE Hyperluminous)
 117      8         1968POPad.143....1B Barbieri C. et al.              
 118      1         1974A&AS...13..269B Barbieri C. et al.              
 119                1975MmSAI..46..461B Barbieri C. et al.              
 120      2         1985A&AS...61..163B Barbieri C. et al.              
 121     15     10  1986A&AS...63....1B Barbieri C. et al.              
 122             2  1987A&AS...67..551B Barbieri C. et al.              
 123      1      1  1998MNRAS.301L..25B Barcons X. et al.               
 124     23     25  2002A&A...382..522B Barcons X. et al.               
 125    160    130  2007A&A...476.1191B Barcons X. et al.               (XMSS)
 126      8     10  2001AJ....122.2177B Barger A.J. et al.              
 127     26     20  2002AJ....124.1839B Barger A.J. et al.              
 128      6      6  2003AJ....126..632B Barger A.J. et al.              
 129      1      1  2008MNRAS.389..792B Barrio F.E. et al.              
 130      1      1  2012ApJ...744....7B Barrows R.S. et al.             (dual AGN)
 131                1984ApJ...279..112B Bartel N. et al.                
 132                1999AJ....118.1609B Barth A.J. et al.               
 133             1  2004ApJ...607...90B Barth A.J. et al.               
 134                2008AJ....136.1179B Barth A.J. et al.               
 135                2008ApJ...683L.119B Barth A.J. et al.               
 136             1  1990A&AS...82..339B Barthel P.D. et al.             
 137      3      2  2002MNRAS.331..417B Basilakos S. et al.             
 138      1         1975A&A....40..217B Battistini P. et al.            
 139    282     95  2000ApJS..129..547B Bauer F.E. et al.               
 140      1      2  2008ATel.1429....1B Baumgartner W.H. et al.         
 141      1         1976ApJ...203L...5B Beaver E.A. et al.              
 142      2         1983ApJ...265...26B Bechtold J. et al.              
 143      1         1992AJ....104..531B Becker R.H. et al.              
 144             1  2001AJ....122.2850B Becker R.H. et al.              
 145     94     60  2001ApJS..135..227B Becker R.H. et al.              
 146             1  1999A&A...352..395B Beckmann V. et al.              
 147     10      8  2003A&A...401..927B Beckmann V. et al.              
 148                1999PASA...16..134B Beer S.H. et al.                
 149                1985ApJ...293..148B Beichman C.A. et al.            
 150      1      1  1998PASP..110..367B Beichman C.A. et al.            
 151             1  2003MNRAS.344L..80B Bellany M.J. et al.             
 152             1  1993MNRAS.263...98B Benn C.R. et al.                
 153      9      5  2002MNRAS.329..221B Benn C.R. et al.                
 154      1         2005MNRAS.360.1455B Benn C.R. et al.                
 155      2         2004AJ....127..576B Bentz M.C. et al.               
 156      1         1980A&A....85L..11B Bergeron J. et al.              
 157             1  1983MNRAS.202..125B Bergeron J. et al.              
 158      2      6  1984MNRAS.207..263B Bergeron J. et al.              
 159      3         1991A&A...243..344B Bergeron J. et al.              
 160      1         1999A&A...343L..40B Bergeron J. et al.              
 161      1         1966ApJ...144..866V van den Bergh S.                
 162                1986A&A...166...92B Bergvall N. et al.              
 163      3      2  1998ApJ...496..103B Bershady M.A. et al.            
 164      7      7  2007A&A...467..565B Berta S. et al.                 
 165     10     12  1999MNRAS.310..223B Best P.N. et al.                
 166      6         2003MNRAS.346..627B Best P.N. et al.                
 167     11     12  1999A&A...347...47B Beuermann K. et al.             
 168      1      1  1998MNRAS.299L..25B Bhatnagar S. et al.             
 169      3         2005MNRAS.364..187B Bian W. et al.                  
 170                2008MNRAS.385..195B Bianchi S. et al.               
 171      1      1  2010MNRAS.405.2737B Bibby J.L. et al.               (Wolf-Rayet QSO)
 172      2      2  2010A&A...523...66B Bielby R.M. et al.              (WIRCAM deep IR clusters)
 173     17     17  2013MNRAS.430..425B Bielby R. et al.                (VLT LBG Redshift Survey)
 174      4      3  2006AstL...32..221B Bikmaev I.F. et al.             
 175      2      2  2008AstL...34..653B Bikmaev I.F. et al.             
 176      2         1985AJ.....90.2508B Biretta J.A. et al.             
 177      1         2008AJ....135..374B Blackburne J.A. et al.          
 178             1  1981MNRAS.194..669B Blades J.C. et al.              
 179      1      1  1980MNRAS.191...61B Blades J. . et al.              
 180      6         1970ApL.....6..201B Blake G.M. et al.               
 181      1      1  1986PASP...98..635B Blanco V.M. et al.              
 182      1      1  2000ApJ...531..118B Blanton E.L. et al.             
 183      2         2001AJ....121.2915B Blanton E.L. et al.             
 184             1  1982ApJ...257..499B Blumenthal G.R. et al.          
 185      4      2  2008MNRAS.390.1229B Blustin A.J. et al.             
 186      1      1  2000ApJS..129..435B Bohringer H. et al.             
 187     15      2  1979ApJ...231..653B Bohuski T.J. et al.             
 188             1  1988A&A...192....1B Boisse P. et al.                
 189             1  1992A&A...262..401B Boisse P. et al.                
 190             1  1976MNRAS.177p..43B Boksenberg A. et al.            
 191      2      2  1989AN....310..187B Boller T. et al.                
 192     13         1998A&AS..129...87B Boller T. et al.                
 193                2003A&A...397..557B Boller T. et al.                
 194      3         1965ApJ...142.1289B Bolton J.G. et al.              
 195      7         1965AuJPh..18..627B Bolton J.G. et al.              
 196      9         1966ApJ...144.1229B Bolton J.G. et al.              
 197      7         1966ApJ...145..951B Bolton J.G. et al.              
 198      3         1966AuJPh..19..275B Bolton J.G. et al.              
 199      3         1966AuJPh..19..471B Bolton J.G. et al.              
 200     12         1966AuJPh..19..559B Bolton J.G. et al.              
 201      3         1966AuJPh..19..713B Bolton J.G. et al.              
 202      9         1967AuJPh..20..109B Bolton J.G. et al.              
 203      6      1  1968ApJ...154L.105B Bolton J.G. et al.              
 204     11         1968AuJPh..21...81B Bolton J.G. et al.              
 205      1         1969ApL.....3..177B Bolton J.G. et al.              
 206     50      2  1970AuJPh..23..789B Bolton J.G. et al.              
 207      7         1971AuJPh..24..889B Bolton J.G. et al.              
 208      2         1973AuJPA..30....1B Bolton J.G. et al.              
 209     50         1975AuJPA..34....1B Bolton J.G. et al.              
 210             2  1976ApJ...210L...1B Bolton J.G. et al.              
 211     13         1977AuJPA..41...25B Bolton J.G. et al.              
 212     13         1977AuJPA..44...21B Bolton J.G. et al.              
 213     23         1981AuJPh..34..445B Bolton J.G. et al.              
 214      1         1977ApJ...213....1B Bond H.E. et al.                
 215      1         1993A&A...280L...7B Bonnet H. et al.                
 216      7      7  2012ApJS..203...15B Bonzini M. et al.               (E-CDFS radio)
 217                2007MNRAS.378..551B Bornancini C.G. et al.          
 218             1  1987PASP...99..809B Boroson T.A. et al.             
 219      1      2  1992ApJ...397..442B Boroson T.A. et al.             
 220            21  1992ApJS...80..109B Boroson T.A. et al.             
 221     31     33  1989AJ.....97..344B Borra E.F. et al.               
 222     66     42  1996AJ....111.1456B Borra E.F. et al.               
 223             3  2004AJ....127.3168B Botte V. et al.                 
 224      7      6  2009A&A...497...81B Boutsia K. et al.               
 225  23135         2011ApJ...729..141B Bovy J. et al.                  (SDSS-XDQSO)
 226    115         1994AJ....107..461B Bowen D.V. et al.               
 227      7         1997MNRAS.284..599B Bowen D.V. et al.               
 228                2000ApJ...534..189B Bower G.A. et al.               
 229      8      8  1996MNRAS.281...59B Bower R.G. et al.               
 230      8      2  1985MNRAS.216..623B Boyle B.J. et al.               
 231    372    331  1990MNRAS.243....1B Boyle B.J. et al.               
 232     58     51  1991MNRAS.251..482B Boyle B.J. et al.               
 233      2         1993MNRAS.265..501B Boyle B.J. et al.               
 234      1      2  1995MNRAS.276..315B Boyle B.J. et al.               
 235     56     36  1997MNRAS.285..511B Boyle B.J. et al.               
 236      2      2  1998MNRAS.296....1B Boyle B.J. et al.               
 237      1         1998MNRAS.297L..53B Boyle B.J. et al.               
 238      5         1979AJ.....84..910B Bozyan E.P. et al.              
 239     44         1992ApJS...82....1B Bozyan E.P. et al.              
 240      8      1  1968ApJ...152L.105B Braccesi A. et al.              
 241      3      2  1970A&A.....5..264B Braccesi A. et al.              
 242      7      7  2007ApJ...663..204B Brand K. et al.                 
 243             1  1994MNRAS.271..958B Brandt W.N. et al.              
 244      1      1  2000AJ....119.2349B Brandt W.N. et al.              
 245      2      1  1985MNRAS.216.1043B Branduardi-Raymont G. et al.    
 246                1998ApJ...497..133B Bransford M.A. et al.           
 247      1      1  2005A&A...441..981B Bresolin F. et al.              (VLT HII)
 248             2  1994A&A...281..355B Brinkmann W. et al.             
 249      1      1  1995A&AS..109..147B Brinkmann W. et al.             
 250      1         1997A&A...319..413B Brinkmann W. et al.             
 251     40     11  2000A&A...356..445B Brinkmann W. et al.             
 252      1      1  2007A&A...476..759B Britzen S. et al.               (CJF AGN X-ray)
 253                2007MNRAS.375.1059B Broderick J.W. et al.           
 254      6         2006MNRAS.366.1265B Brookes M.H. et al.             
 255      2     15  2008MNRAS.385.1297B Brookes M.H. et al.             
 256      1      1  2000MNRAS.313..641B Brosch N. et al.                
 257            10  1996ApJS..102....1B Brotherton M.S. et al.          
 258      2      1  1999ApJ...514L..61B Brotherton M.S. et al.          
 259             1  1999ApJ...520L..87B Brotherton M.S. et al.          
 260      1      1  2001ApJ...546..134B Brotherton M.S. et al.          
 261      2         1971Natur.231..515B Browne I.W.A. et al.            
 262      3         1972Natur.239..101B Browne I.W.A. et al.            
 263      1         1973MNRAS.162p..21B Browne I.W.A. et al.            
 264     10         1973Natur.244..146B Browne I.W.A. et al.            
 265      1         1974Natur.252..209B Browne I.W.A. et al.            
 266             3  1975MNRAS.173p..87B Browne I.W.A. et al.            
 267      4      6  1977MNRAS.179p..65B Browne I.W.A. et al.            
 268      3      3  2003AJ....126...53B Brunner R.J. et al.             
 269     43     41  2002A&A...390..879B Brunzendorf J. et al.           
 270      5      5  2003A&A...409...65B Brusa M. et al.                 
 271      9      7  2009ApJ...693....8B Brusa M. et al.                 
 272    105    122  2010ApJ...716..348B Brusa M. et al.                 (http://www2011.mpe.mpg.de/XMMCosmos/xmm53_release)
 273             1  1989A&A...226L..13D de Bruyn A.G. et al.            
 274                2000ApJ...545..216B Bryant J.J. et al.              
 275      8      8  2009MNRAS.395.1099B Bryant J.J. et al.              
 276      3      2  1998ApJ...494..503B Buchalter A. et al.             
 277            18  2006AJ....132...27B Buchanan C.L. et al.            
 278      3         1993AstL...19....5B Bugaenko O.I. et al.            
 279             3  1999MNRAS.309..875B Bunker A.I. et al.              
 280             1  1966ApJ...143..612B Burbidge E.M. et al.            
 281             2  1966ApJ...145..654B Burbidge E.M. et al.            
 282      9      3  1968ApJ...154L.109B Burbidge E.M. et al.            
 283      3      4  1970ApJ...160L..33B Burbidge E.M. et al.            
 284             4  1972ApJ...174L..57B Burbidge E.M. et al.            
 285      3      2  1980ApJ...242L..55B Burbidge E.M. et al.            
 286     20      8  1985ApJ...288...82B Burbidge E.M. et al.            
 287      1         1996AJ....112.2533B Burbidge E.M. et al.            
 288      1         1997ApJ...484L..99B Burbidge E.M. et al.            
 289      3         1999ApJ...511L...9B Burbidge E.M. et al.            
 290      3      2  2002PASP..114..253B Burbidge E.M. et al.            
 291      3      2  2003ApJ...591..690B Burbidge E.M. et al.            
 292      4      4  ................... Burbidge E.M. et al.            2003 unpublished (October 2003 Keck-I LRIS)
 293      1      1  2004ApJS..153..159B Burbidge E.M. et al.            
 294      1      1  2006PASP..118..124B Burbidge E.M. et al.            
 295      2      1  1977ApJS...33..113B Burbidge G.R. et al.            
 296      4         ................... Burbidge G.R. et al.            1988, Mercury 7, 136
 297      6      2  2008AstL...34..367B Burenin R.A. et al.             
 298      6      9  2006AJ....131..114B Burgess A.M. et al.             
 299      1         1998ApJ...501L...5B Burud I. et al.                 
 300      1         2002A&A...391..481B Burud I. et al.                 
 301      1         2002ApJS..138....1B Bushouse H.A. et al.            
 302             1  1990MNRAS.245..470B Busko I.C. et al.               
 303      1      2  2009ApJ...698..502B Butler S.C. et al.              
 304      1      9  2009A&A...495.1033B Buttiglione S. et al.           
 305     64         2003PASP..115..837C Cabanela J.E. et al.            
 306     11     13  2004A&A...416..901C Caccianaga A. et al.            
 307     42     40  2000A&AS..144..247C Caccianiga A. et al.            
 308     16     20  2002ApJ...566..181C Caccianiga A. et al.            
 309     21     22  2002MNRAS.329..877C Caccianiga A. et al.            
 310      8      9  2007A&A...470..557C Caccianiga A. et al.            
 311    141    133  2008A&A...477..735C Caccianiga A. et al.            (XBSS)
 312      1         1977A&A....55...73C Callahan P.S. et al.            
 313      1         1999ApJ...511L...1C Campos A. et al.                
 314             1  ................... Campusano L.E. et al.           1978, OANCC Santiago Dep. Astron. Publ. 3, 315
 315     60         1983AJ.....88.1304C Campusano L.E. et al.           
 316            27  1991AJ....102..502C Campusano L.E. et al.           
 317      1      1  1998AJ....115..890C Canalizo G. et al.              
 318      1         2000AJ....119...59C Canalizo G. et al.              
 319             3  1999A&AS..135..243C Cao L. et al.                   
 320                1999ApJ...519..117C Cappellari M. et al.            
 321      1      3  2003A&A...412..651C Carangelo N. et al.             
 322             1  1995AJ....109.1531C Carballo R. et al.              
 323      4      1  1995MNRAS.277.1312C Carballo R. et al.              
 324      5         2006MNRAS.370.1034C Carballo R. et al.              (FIRST-APM-SDSS hi-z survey)
 325      7      7  2008MNRAS.391..369C Carballo R. et al.              
 326      1         1976PASP...88..334C Carney B.W. et al.              
 327      1      1  1997AJ....113.1527C Carrasco L. et al.              
 328      1      1  1998AJ....115.1717C Carrasco L. et al.              
 329             2  2004A&A...420..163C Carrera F.J. et al.             
 330                1983MNRAS.203p..49C Carter D. et al.                
 331             1  1988MNRAS.235..813C Carter D. et al.                
 332      3      2  2012ApJ...761..139C Casey C.M. et al.               (Herschel-SPIRE)
 333      1      1  2003AJ....125.1689C Castander F.J. et al.           
 334     62     75  1991AJ....102..461C Chaffee F.H. et al.             
 335      1      1  1996ApJS..106..215C Chambers K.C. et al.            
 336     10      2  1981ApJ...243L...5C Chanan G.A. et al.              
 337      2         1982ApJ...261L..31C Chanan G.A. et al.              
 338                1990MNRAS.244..281C Chapman J.M. et al.             
 339      1      1  2004ApJ...614..671C Chapman S.C. et al.             
 340      6         1959BOTT....2r...3C Chavira E. et al.               
 341             1  1997A&A...318L..67C Chavushyan V.H. et al.          
 342             2  2000AstL...26..339C Chavushyan V.H. et al.          
 343      3      2  2001ARep...45...79C Chavushyan V.H. et al.          
 344      3      1  ................... Chavushyan V.H. et al.          2001, ASP Conf. Ser. 232, 102
 345      4      4  2002ARep...46..697C Chavushyan V. et al.            
 346     17     15  1984A&A...134..306C Chen J.-S. et al.               
 347      5     11  1985ChA&A...9..343C Chen J.-S. et al.               
 348      7      2  2002AJ....123..578C Chen Y. et al.                  
 349      3      3  2009ApJS..181..548C Cheung C.C. et al.              
 350      8      8  2005AJ....130...13C Chiu K. et al.                  
 351             1  1982ApJ...253L..13C Christian C.A. et al.           
 352      1         1985ChA&A...9..246C Chu Y. et al.                   
 353             1  1986ChA&A..10..196C Chu Y. et al.                   
 354      1      4  1998ApJ...500..596C Chu Y. et al.                   
 355             1  1999AJ....117.2573C Churchill C.W. et al.           
 356             2  2004MNRAS.355..273C Cid-Fernandes R. et al.         
 357             3  1994AJ....108..970C Ciliegi P. et al.               
 358      1      1  1993MNRAS.263..236C Cimatti A. et al.               
 359             1  1996ApJ...465..145C Cimatti A. et al.               
 360             1  1997ApJ...476..677C Cimatti A. et al.               
 361      1      1  1996A&A...305L...9C Claeskens J.-F. et al.          
 362      1      1  2005ApJ...631L.109C Clark D.M. et al.               
 363      7         1966AuJPh..19..375C Clarke M. et al.                
 364      2      2  1999MNRAS.302..391C Clements D.L. et al.            
 365      1      2  1979MNRAS.189..175C Clowes R.G. et al.              
 366      4         1980MNRAS.193..415C Clowes R.G. et al.              
 367     74     22  1983MNRAS.204..365C Clowes R.G. et al.              
 368     21     12  1991MNRAS.249..218C Clowes R.G. et al.              
 369             1  1991MNRAS.250..597C Clowes R.G. et al.              
 370     54      1  1994MNRAS.266..317C Clowes R.G. et al.              
 371                1995MNRAS.275..819C Clowes R.G. et al.              
 372     57     24  1999MNRAS.309...48C Clowes R.G. et al.              
 373     38     32  2007A&A...466...31C Cocchia F. et al.               
 374     52         1977MmRAS..84....1C Cohen A.M. et al.               
 375      3      2  1999ApJS..120..171C Cohen J.G. et al.               
 376             1  2003ApJ...583...67C Cohen J.G. et al.               
 377                1992AJ....103.1734C Cohen M. et al.                 
 378                1997ApJ...484..193C Cohen M.H. et al.               
 379             3  1999AJ....118.1963C Cohen M.H. et al.               
 380             1  1987ApJ...318..577C Cohen R.D. et al.               
 381      1      1  2000A&AS..144..187C Colafrancesco S. et al.         
 382      4         1985AJ.....90.1437C Coleman P.H. et al.             
 383             1  1991ApJ...382L..63C Colina L. et al.                
 384      2      2  1991MNRAS.253..686C Colless M. et al.               
 385     90     13  2001MNRAS.328.1039C Colless M. et al.               (2dF GRS)
 386    138     37  2005AJ....129.2542C Collinge M.J. et al.            
 387             1  1998A&A...333...31C Comastri A. et al.              
 388     11         1975AJ.....80..887C Condon J.J. et al.              
 389      8         1976AJ.....81..913C Condon J.J. et al.              
 390     37         1977AJ.....82..692C Condon J.J. et al.              
 391     12         1978AJ.....83.1036C Condon J.J. et al.              
 392      1         1978ApJ...221..456C Condon J.J. et al.              
 393     18         1979AJ.....84..149C Condon J.J. et al.              
 394     15         1982AJ.....87..219C Condon J.J. et al.              
 395     13         1983AJ.....88...20C Condon J.J. et al.              
 396      1         1984AJ.....89..610C Condon J.J. et al.              
 397             6  ................... Condon J.J. et al.              1986, private communication to HB
 398      1         1995AJ....109.2318C Condon J.J. et al.              
 399     12      2  1998AJ....116.2682C Condon J.J. et al.              
 400             1  1998AJ....115...37C Conner S.R. et al.              
 401     11     17  2002ApJ...565...50C Constantin A. et al.            
 402             1  1974MNRAS.168..137C Conway R.G. et al.              
 403      3      3  2006AJ....132..823C Cool R.J. et al.                
 404                2003ApJ...583..670C Corbett E.A. et al.             
 405             2  1991ApJ...375..503C Corbin M.R. et al.              
 406             6  1997ApJS..113..245C Corbin M.R. et al.              
 407      1         1998A&AS..131..259C Costa E. et al.                 
 408                1977ApJ...211..675C Costero R. et al.               
 409      1         1996MNRAS.281.1081C Cotter G. et al.                
 410             4  1999ApJS..125..409C Cotton W.D. et al.              (UGC Galaxies)
 411      1      1  1987MNRAS.229..423C Couch W.J. et al.               
 412      1         2002A&A...394..863C Courbin F. et al.               
 413      1      1  1994ApJ...432L..83C Cowie L.L. et al.               
 414             2  1984ApJ...286..196C Cowley A.P. et al.              
 415      3      1  1987AJ.....94...16C Cowley A.P. et al.              
 416             1  1997AJ....113.1548C Coziol R. et al.                
 417                1998ApJS..119..239C Coziol R. et al.                
 418      4      3  1997AJ....114.1356C Craig N. et al.                 
 419      3      3  1982PASP...94..440C Crampton D. et al.              
 420     31     23  1985AJ.....90..987C Crampton D. et al.              
 421    133     83  1987ApJ...314..129C Crampton D. et al.              
 422    100     57  1988AJ.....96..816C Crampton D. et al.              
 423      2         1988ApJ...330..184C Crampton D. et al.              
 424     52     31  1989ApJ...345...59C Crampton D. et al.              
 425     52     26  1990AJ....100...47C Crampton D. et al.              
 426     11      5  1991AJ....101.1183C Crampton D. et al.              
 427      5      1  1992AJ....104.1706C Crampton D. et al.              
 428      1      1  1996A&A...307L..53C Crampton D. et al.              
 429     29     26  1997AJ....114.2353C Crampton D. et al.              
 430      2      2  2002MNRAS.333..809C Crawford C.S. et al.            
 431                1996ApJ...460..225C Crawford T. et al.              
 432      2         2003AJ....126.1690C Crenshaw D.M. et al.            
 433    168     93  2011MNRAS.414...28C Crighton N.H.M. et al.          
 434             1  1984A&A...132..351C Cristiani S. et al.             
 435      1      1  1984A&A...135..122C Cristiani S. et al.             
 436             4  1987A&AS...68..339C Cristiani S. et al.             
 437      3      1  1987MNRAS.227..639C Cristiani S. et al.             
 438     64     15  1989A&AS...77..161C Cristiani S. et al.             
 439     22     25  1990MNRAS.245..493C Cristiani S. et al.             
 440      1      6  1991MNRAS.250..531C Cristiani S. et al.             
 441      2      2  1993A&A...268...86C Cristiani S. et al.             
 442    118    137  1995A&AS..112..347C Cristiani S. et al.             
 443     33     13  1996A&A...306..395C Cristiani S. et al.             
 444      1      1  2000A&A...359..489C Cristiani S. et al.             
 445      6      6  2005AJ....130..867C Croft S. et al.                 
 446     81    395  2001MNRAS.322L..29C Croom S.M. et al.               
 447  23036  19692  2004MNRAS.349.1397C Croom S.M. et al.               (2QZ/6QZ)
 448   7722   6556  2009MNRAS.392...19C Croom S.M. et al.               (2SLAQ)
 449             1  1989ApJ...336..550C Crotts A.P.S. et al.            
 450      1         1998ApJ...502...16C Crotts A.P.S. et al.            
 451      1      1  2006MNRAS.373.1531C Cruz M.J. et al.                
 452                1984AJ.....89..441C Cruz-Gonzalez I. et al.         
 453             3  1994ApJS...94...47C Cruz-Gonzalez I. et al.         
 454     15         ................... Cruz-Gonzalez I. et al.         2004, mas conf 303 (A+A, submitted)
 455      1      1  2008A&A...484..303D D'Elia V. et al.                
 456      1      1  2013A&A...559...86D Dadina M. et al.                
 457                1985ApJS...57..643D Dahari O. et al.                
 458             3  1988ApJS...67..249D Dahari O. et al.                
 459      1      1  2013ApJ...773..146D Dahle H. et al.                 (Giant Arcs sextuple)
 460                1979MNRAS.186...93D Danziger I.J. et al.            
 461                1983MNRAS.202..703D Danziger I.J. et al.            
 462                1984MNRAS.208..589D Danziger I.J. et al.            
 463      4     11  1997A&A...323...47D Danziger I.J. et al.            
 464             4  1994AJ....108.2025D Darling G.W. et al.             
 465            16  1996AJ....111..865D Darling G.W. et al.             
 466      1         2006AJ....132.2596D Darling J. et al.               
 467      1         1980PASP...91..817D Davidson K. et al.              
 468      1      1  1991A&A...252...69D Davoust E. et al.               
 469                1995A&AS..110...19D Davoust E. et al.               
 470      1      1  1998AJ....116...13D de Breuck C. et al.             
 471      4      4  2001AJ....121.1241D de Breuck C. et al.             
 472                2002AJ....123..637D de Breuck C. et al.             
 473      3      3  2006MNRAS.366...58D de Breuck C. et al.             
 474             1  2002A&A...381L..57D de Bruijne J.H.J. et al.        
 475      1         2007PASP..119...50D de Diego J.A. et al.            
 476      1      1  1999ApJ...514..148D De Grandi S. et al.             (ROSAT South)
 477                1985Natur.314..240D de Grijp M.H.K. et al.          
 478     27         1987A&AS...70...95D de Grijp M.H.K. et al.          
 479            11  1992A&AS...96..389D de Grijp M.H.K. et al.          
 480                1986ApJ...301...98D de Robertis M.M. et al.         
 481      7         1998ApJS..115..163D de Robertis M.M. et al.         
 482      1      3  2007A&A...464..879D de Vries N. et al.              
 483      1      1  1995A&AS..114..259D de Vries W.H. et al.            
 484                2000A&AS..143..181D de Vries W.H. et al.            
 485      2      1  2009MNRAS.396L..31D Decarli R. et al.               
 486      1      1  2010A&A..511A...27D Decarli R. et al.               
 487      1      1  2009A&A...493..445D Del Moro A. et al.              
 488             1  1991A&A...245...27D del Olmo et al.                 
 489                2000A&A...355..121D Della Ceca R. et al.            
 490                2005A&A...440....5D Dennefeld M. et al.             
 491      1      1  2000ApJ...529L..65D Dennett-Thorpes J. et al.       
 492      1         2000A&A...360..107D Dewangan G.C. et al.            
 493             1  2001MNRAS.325.1616D Dewangan G.C. et al.            
 494     22      6  2002MNRAS.337..693D Dewangan G.C. et al.            
 495                1994AJ....107.1977D Dey A. et al.                   
 496      1         1996ApJ...459..133D Dey A. et al.                   
 497             1  1994ApJ...431..123D Di Serego Alighieri S. et al.   
 498      2      5  1994MNRAS.269..998D Di Serego Alighieri S. et al.   
 499      1         2009ApJ...699..782D Diamond-Stanic A.M. et al.      
 500                1988A&A...195...53D Diaz A.I. et al.                
 501      2      2  1999A&A...352L...1D Dietrich M. et al.              
 502      1      3  2000A&A...354...17D Dietrich M. et al.              
 503      2      8  2003A&A...398..891D Dietrich M. et al.              
 504             2  1994ApJ...437L..87D Dinshaw N. et al.               
 505      1      1  1996ApJ...458...73D Dinshaw N. et al.               
 506      1         1973ApJ...181L..55D Disney M.J. et al.              
 507      1         1987ApJ...321L..17D Djorgovski S. et al.            
 508             1  1990PASP..102..113D Djorgovski S. et al.            
 509      3      3  1995ApJS..101..255D Djorgovski S. et al.            
 510     51     28  ................... Djorgovski S. et al.            2001 http://www.astro.caltech.edu/~george/z4.qsos
 511      1      1  2003ApJ...596...67D Djorgovski S.G. et al.          
 512      1         1999A&A...349L..29D Dobrzycki A. et al.             
 513      4      2  2002ApJ...569L..15D Dobrzycki A. et al.             
 514      3      2  2003AJ....125.1330D Dobrzycki A. et al.             
 515      5      4  2003AJ....126..734D Dobrzycki A. et al.             
 516      8      5  2005A&A...442..495D Dobrzycki A. et al.             
 517      3      3  1999ARep...43..275D Dodonov S.N. et al.             
 518      1         1978PASP...90...24D Donivan F.F. et al.             
 519      1         2002AJ....124.1308D Donley J.L. et al.              
 520      1      1  1987ApJ...321...94D Donnelly R.H. et al.            
 521                2000AJ....120..189D Donzelli C.J. et al.            
 522                2007MNRAS.376.1393D Douglas L.S. et al.             
 523      9         1986MNRAS.218...31D Downes A.J.B. et al.            
 524             1  1999ApJ...513L...1D Downes D. et al.                
 525      1         1996PASP..108..134D Downes R.A. et al.              
 526     10         2003AJ....126.2237D Drake C.L. et al.               
 527      1         1983ApJ...270....7D Dressler A. et al.              
 528      1      2  1985ApJ...288..481D Dressler A. et al.              
 529      2      1  1992ApJS...78....1D Dressler A. et al.              
 530    517    539  ................... Drinkwater M.J. et al.          1987, Ph.D. thesis 'Quasar clustering on large scale' Cambridge
 531     34     49  1997MNRAS.284...85D Drinkwater M.J. et al.          
 532      2      2  ................... Drinkwater M. et al.            2001 private communication to NED (Fornax cluster survey)
 533      1      1  1997A&AS..124..533D Duc P.-A. et al.                
 534      1      1  2002A&A...389L..47D Duc P.-A. et al.                
 535      1         1986Natur.319..564D Dunlop J.S. et al.              
 536      2     12  1989MNRAS.238.1171D Dunlop J.S. et al.              
 537                1993A&AS...98..365D Durret F. et al.                
 538                1994A&AS..105...57D Durret F. et al.                
 539             3  1986A&A...168...17E Eckart A. et al.                
 540    189    174  2006ApJS..165...19E Eckart M.E. et al.              
 541             1  1995MNRAS.272L...5E Economou F. et al.              
 542     12     16  2012ApJ...751...52E Edelson R. et al.               (WISE-2MASS-RASS)
 543             1  1982MNRAS.198.1089E Edmunds M.G. et al.             
 544      5         1975AJ.....80.1005E Edwards T. et al.               
 545      1         1970AuJPh..23..217E Ekers R.D. et al.               
 546     21         1991ApJS...76..455E Ellingson E. et al.             
 547      2      1  ................... Ellis R. et al.                 1985, Gemini 15, 1
 548     14     25  2008MNRAS.388.1349E Ellison S.L. et al.             
 549      2      1  1995ApJ...440..458E Elowitz R.M. et al.             
 550                1969MNRAS.146..361E Elsmore B. et al.               
 551                1985ApJ...296..106E Elston R. et al.                
 552                2006A&A...454..125E Emonts B.H.C. et al.            
 553     88     46  1998A&AS..128..507E Engels D. et al.                
 554            18  1994ApJS...90....1E Eracleous M. et al.             
 555            18  2004ApJS..150..181E Eracleous M. et al.             
 556             1  1989AN....310...97E Erculiani-Abati L. et al.       
 557             1  1997A&A...323..707E Erkens U. et al.                
 558             1  1994ApJ...434..484E Espey B.R. et al.               
 559    399    369  2013A&A...557..123E Esquej P. et al.                (XWAS)
 560                1998ApJ...506..205E Evans A.S. et al.               
 561             6  1995PASP..107.1059E Everett M.E. et al.             
 562             1  2002A&A...383..838F Fadda D. et al.                 
 563      1         1968PASP...80..235F Fairall A.P. et al.             
 564      1         1978MNSSA..37...41F Fairall A.P. et al.             
 565      1         1981MNRAS.196..417F Fairall A.P. et al.             
 566                1983MNRAS.203...47F Fairall A.P. et al.             
 567             1  1984MNRAS.210...69F Fairall A.P. et al.             
 568             1  1985Obs...105..129F Fairall A.P. et al.             
 569                1986MNRAS.218..453F Fairall A.P. et al.             
 570                1988MNRAS.230...69F Fairall A.P. et al.             
 571             5  1988MNRAS.233..691F Fairall A.P. et al.             
 572                1998A&AS..127..463F Fairall A.P. et al.             
 573      7      4  ................... Faisse S. et al.                1998, Ph.D. Paris
 574     68     51  1998ApJ...494...47F Falco E.E. et al.               
 575      4      5  1999PASP..111..438F Falco E.E. et al.               (the Updated Zwicky Catalog)
 576             1  1991AJ....101..821F Falomo R. et al.                
 577             5  1994ApJS...93..125F Falomo R. et al.                
 578      1         1995ApJ...438L...9F Falomo R. et al.                
 579      1      1  2000A&A...357...91F Falomo R. et al.                
 580      1         2008ApJ...673..694F Falomo R. et al.                
 581             1  1994ApJS...94...17F Fan X.-M. et al.                
 582      1      1  1999AJ....118....1F Fan X. et al.                   
 583             1  1999ApJ...526L..57F Fan X. et al.                   
 584      3      2  2000AJ....119....1F Fan X. et al.                   
 585      1         2000AJ....120.1167F Fan X. et al.                   
 586      9      8  2001AJ....121...31F Fan X. et al.                   
 587      3         2001AJ....122.2833F Fan X. et al.                   
 588      2      2  2003AJ....125.1649F Fan X. et al.                   
 589      4      4  2004AJ....128..515F Fan X. et al.                   
 590      7      7  2006AJ....131.1203F Fan X. et al.                   
 591                1972MNRAS.157...41F Fanaroff B.L. et al.            
 592     21         1975A&AS...19..143F Fanti C. et al.                 
 593      1         1981A&A....97..251F Fanti C. et al.                 
 594      2         1977A&AS...29..263F Fanti R. et al.                 
 595      2      2  2013MNRAS.431.1019F Farina E.P. et al.              (QQQ Triplet)
 596                2005ApJ...626...70F Farrah B. et al.                
 597      1      1  1996ApJ...460L.103F Fassnacht C.D. et al.           (1608+656)
 598      2      2  1998AJ....115..377F Fassnacht C.D. et al.           
 599      1      1  1999AJ....117..658F Fassnacht C.D. et al.           
 600             1  1999ApJ...510..167F Feldmeier J.J. et al.           
 601    115    115  2008A&A...488..417F Feruglio C. et al.              
 602             4  1985ApJS...57..503F Filippenko A.V. et al.          
 603      1      1  1991IAUC.5328....1F Filippenko A.V. et al.          
 604      2      1  1993IAUC.5829....1F Filippenko A.V. et al.          
 605             1  2008A&A...477..513F Finke J.D. et al.               
 606      1      1  2009ApJ...703L.162F Finkelstein S.L. et al.         
 607      3      4  1999MNRAS.306L..55F Fiore F. et al.                 
 608      3      4  2000NewA....5..143F Fiore F. et al.                 
 609     55     55  2003A&A...409...79F Fiore F. et al.                 
 610     12     31  1998AN....319..347F Fischer J.-U. et al.            
 611         10815  ................... Flesch E.W. et al.              2015, this catalog, (Half Million Quasars)
 612      1         1970ApL.....7...15F Folsom G.H. et al.              
 613      1         1971ApJ...169L.131F Folsom G.H. et al.              
 614      1         1983PASP...95..117F Foltz C.B. et al.               
 615      9      2  1987AJ.....94.1423F Foltz C.B. et al.               
 616      1      3  1989AJ.....98.1959F Foltz C.B. et al.               
 617     32     32  1993AJ....105...22F Foltz C.B. et al.               
 618      1      1  2007A&A...461...39F Fontanot F. et al.              
 619             1  1983ApJ...266..451F Ford H. et al.                  
 620                1982MNRAS.201..991F Fosbury R.A.E. et al.           
 621                1987MNRAS.225..761F Fosbury R.A.E. et al.           
 622      1      1  2002A&A...396..787F Foschini L. et al.              
 623      1      1  2007A&A...473..791F Fox A.J. et al.                 
 624             3  2000PASA...17...56F Francis P.J. et al.             
 625      7      5  2004AJ....127..646F Francis P.J. et al.             
 626      5      5  2004ApJ...614...75F Francis P.J. et al.             
 627      1         2004ApJ...602L..77F Francis P.J. et al.             
 628             1  2000ApJ...532..867F Fraquelli H.A. et al.           
 629             3  1983A&A...117...60F Fricke K.J. et al.              
 630      1         1989ApJ...343..672F Frogel J.A. et al.              
 631             1  1991ApJ...380L..13F Fruscione A. et al.             
 632      1      1  ................... Fu H. et al.                    2014, ArXiv 1411, 685 (Radio-selected binary AGN)
 633      4         1988A&AS...75..173F Fugmann W. et al.               
 634             1  1988A&AS...76..145F Fugmann W. et al.               
 635             2  2004ApJ...603L..65F Fukugita M. et al.              
 636      1         2000A&A...353..457F Fynbo J.U. et al.               
 637     22     16  2013ApJS..204....6F Fynbo J.P.U. et al.             (Red QSOs)
 638      1         2002PASP..114..587G Gal-Yam A. et al.               
 639                2005A&A...430..927G Galbiatti E. et al.             
 640      1      1  2005ApJ...620...88G Galianni P. et al.              
 641             1  1994A&A...290..705G Gallego J. et al.               
 642             3  1996A&AS..120..323G Gallego J. et al.               
 643      1      1  2002MNRAS.337..781G Gandhi P. et al.                
 644                2006MNRAS.369.1566G Gandhi P. et al.                
 645      1         1992AJ....104.1290G Garilli B. et al.               
 646    297    237  2014A&A...562...23G Garilli B. et al.               (VIPERS v1)
 647      1      1  1996IAUC.6358....1G Garnavich P. et al.             
 648     64     15  1983ApJ...272..411G Gaston B. et al.                
 649             1  ................... Gaston B. et al.                1983, Ph.D. thesis 'Luminosity function of high redshift quasars'
 650    114     92  2006A&A...457...79G Gavignaud I. et al.             
 651      2    566  2012ApJS..201...31G Ge J.-Q. et al.                 (Double-Peaked NELGs)
 652      2         1972AJ.....77..557G Gearhart M.R. et al.            
 653     47     30  2003AJ....125....1G Geha M. et al.                  
 654      3         2009MNRAS.397..172G Gelbord J.M. et al.             
 655             6  1994ApJS...91..491G Gelderman R. et al.             
 656     10     10  1999MNRAS.306..708G Georgakakis A. et al.           
 657     10      5  2006MNRAS.371..221G Georgakakis A. et al.           
 658      1      1  1997MNRAS.291..203G Georgantopoulos I. et al.       
 659      1      1  1999MNRAS.305..125G Georgantopoulos I. et al.       
 660             1  2004ApJ...614..634G Georgantopoulos I. et al.       
 661      9      4  2004MNRAS.352...91G Georgantopoulos I. et al.       
 662                2007ApJ...660L..23G Gerke B.F. et al.               
 663      3      1  1977ApJS...35..359G Ghigo F.D. et al.               
 664             1  1982AJ.....87.1438G Ghigo F.D. et al.               
 665      4      1  1979ApJ...234L...1G Giacconi R. et al.              
 666                2002ApJS..139..369G Giacconi R. et al.              
 667             1  1984MNRAS.211p..25G Gilmore G. et al.               
 668             1  1986A&A...168...62G Gilmozzi R. et al.              
 669             1  1983ApJ...271..524G Gioia I.M. et al.               
 670      7     11  1984ApJ...283..495G Gioia I.M. et al.               
 671      2         1994ApJS...94..583G Gioia I.M. et al.               
 672    169    175  2003ApJS..149...29G Gioia I.M. et al.               
 673     11     11  1991ApJ...378...77G Giommi P. et al.                
 674      2      2  2004A&A...414....7G Giommi P. et al.                (Blazars in CMB)
 675      1         1979A&A....76..109G Gisler G.R. et al.              
 676      1         1997MNRAS.284...27G Gladders M.D. et al.            
 677      1      1  1995MNRAS.273..157G Glazebrook K. et al.            
 678      2      2  2006AJ....131.2383G Glazebrook K. et al.            
 679      8      5  2004ApJ...607...60G Glikman E. et al.               
 680     34     28  2007ApJ...667..673G Glikman E. et al.               
 681      2      2  2007ApJ...663L..73G Glikman E. et al.               
 682     21     20  2010ApJ...710.1498G Glikman E. et al.               (Faint End of QLF)
 683     20     21  2012ApJ...757...51G Glikman E. et al.               (FIRST-2MASS red quasars)
 684      6      6  2013ApJ...778..127G Glikman E. et al.               (UKIDSS-FIRST)
 685      5      3  1992MNRAS.256p..65G Goldschmidt P. et al.           
 686     37     18  1999ApJ...511..612G Goldschmidt P. et al.           
 687             6  1998A&AS..127..107G Goncalves A.C. et al.           
 688                2008ATel.1623....1G Goncalves T.S. et al.           
 689             1  1994MNRAS.268..973G Gondhalekar P.M. et al.         
 690      2         1997ApJS..108..155G Gonzalez Delgado R.M. et al.    
 691      2         2001AJ....122.2055G Gonzalez-Perez J.N. et al.      
 692             1  1989ApJ...340..190G Goodrich R.W. et al.            
 693             1  1994ApJ...422..521G Goodrich R.W. et al.            
 694             1  1994ApJ...434...82G Goodrich R.W. et al.            
 695             1  2001ApJ...561L..23G Goodrich R.W. et al.            
 696      2      2  2005A&A...436..457G Gopal-Krishna G. et al.         
 697             1  2000AJ....119.1677G Gorham P.W. et al.              
 698      1         1998A&A...339..719G Gorosabel J. et al.             
 699      1      1  1993AstL...19...55G Gorshkov A.G. et al.            
 700      4      6  2003ARep...47..903G Gorshkov A.G. et al.            
 701     36     14  1997A&AS..123..529G Gosset E. et al.                
 702      1      1  2006MNRAS.371..769G Goto T. et al.                  
 703      1      1  1996MNRAS.279.1349G Graham M.J. et al.              
 704     18     18  2014MNRAS.439..703G Graham M.J. et al.              (CRTS Slepian)
 705      1      1  2004A&A...418..907G Grandi P. et al.                
 706             1  1978ApJ...220..783G Grandi S.A. et al.              
 707                1983MNRAS.204..691G Grandi S.A. et al.              
 708      3      8  2000AJ....119.2540G Grazian A. et al.               
 709     14     39  2002AJ....124.2955G Grazian A. et al.               
 710             1  1989ApJ...339...93G Green P.J. et al.               
 711     45     37  2004ApJS..150...43G Green P.J. et al.               
 712     13     10  2009ApJ...690..644G Green P.J. et al.               
 713      1         2010ApJ...710.1578G Green P.J. et al.               erratum ApJ 712, 762
 714      1      1  2011ApJ...743...81G Green P.J. et al.               (Chandra binaries)
 715      3         1976PASP...88..665G Green R.F. et al.               
 716      3         1980ApJ...239..483G Green R.F. et al.               
 717      4         1986ApJS...61..305G Green R.F. et al.               
 718      3      3  2007ApJ...667..131G Greene J.E. et al.              
 719      1         1964ApJ...140....1G Greenstein J. et al.            
 720      1      1  1996AJ....112..407G Gregg M.D. et al.               
 721      1      1  2000AJ....119.2535G Gregg M.D. et al.               
 722      2         2002ApJ...564..133G Gregg M.D. et al.               
 723             1  1991AJ....102.1977G Gregory S.A. et al.             
 724                2000AJ....119..545G Gregory S.A. et al.             
 725      3         1996A&A...310..384G Greiner J. et al.               
 726      1         1963AJ.....68..421G Griffin R. et al.               
 727      1         1979ApJ...230L..21G Griffiths R.E. et al.           
 728      9      1  1983ApJ...269..375G Griffiths R.E. et al.           
 729      1         1989MNRAS.240...33G Griffiths R.E. et al.           
 730     16     16  1995MNRAS.275...77G Griffiths R.E. et al.           
 731             4  1996MNRAS.281...71G Griffiths R.E. et al.           
 732                2005MNRAS.359.1345G Grimes J.A. et al.              
 733      3         1980ApJ...239L..43G Grindlay J.E. et al.            
 734      1      1  1993A&AS...97..113G Grindlay J.E. et al.            
 735                2004AJ....127.1943G Gronwall C. et al.              
 736                2004AJ....128..644G Gronwall C. et al.              
 737      1      2  1989A&A...223L...1G Groote D. et al.                
 738     16         1972A&AS....6....1G Grueff G. et al.                
 739             1  1995A&A...300L..21G Grupe D. et al.                 
 740     13     40  1999A&A...350..805G Grupe D. et al.                 
 741      1         2000A&A...356...11G Grupe D. et al.                 
 742      1         2001A&A...369..450G Grupe D. et al.                 
 743     10     26  2004AJ....127..156G Grupe D. et al.                 
 744      4      1  1999MNRAS.304..199G Gruppioni C. et al.             
 745                1997A&A...319...92G Gu Q.-S. et al.                 
 746      2         1981MNRAS.194..111G Gunn J.E. et al.                
 747      1      2  1999A&A...342..378G Gurvits L.I. et al.             
 748      7      5  2005ApJ...622L..89G Gutierrez C.M. et al.           
 749      2      1  2006ApJ...640L..17G Gutierrez C.M.                  
 750      4      2  2007A&A...472...87G Gutierrez C.M. et al.           
 751      1      1  2004A&A...419L..49H Haas M. et al.                  
 752      1         1992A&A...253L...5H Hagen H.J. et al.               
 753      2         1996A&A...308L..25H Hagen H.J. et al.               
 754    196    127  1999A&AS..134..483H Hagen H.J. et al.               
 755      1         2000A&A...357L..29H Hagen H.J. et al.               
 756     10     10  2012ApJ...754...97H Haines C.P. et al.              (LOCUSS)
 757      2      2  2014ApJ...795..124H Hainline K.N. et al.            (WISE-selected obscured quasars)
 758                2004Ap.....47..378H Hakopian S.A. et al.            
 759     35     33  1996ApJ...462..614H Hall P.B. et al.                
 760     37     28  2000AJ....120.2220H Hall P.B. et al.                
 761      3      3  2002ApJS..141..267H Hall P.B. et al.                
 762             2  1987ApJ...312...91H Halpern J.P. et al.             
 763             1  1991AJ....101..818H Halpern J.P. et al.             
 764      1      1  1997AJ....114.1736H Halpern J.P. et al.             
 765      1         1998ApJ...494..194H Halpern J.P. et al.             
 766             1  1998ApJ...501..103H Halpern J.P. et al.             
 767             1  1999MNRAS.307L..47H Halpern J.P. et al.             
 768      1         2001ApJ...551.1016H Halpern J.P. et al.             
 769     10      7  2003AJ....125..572H Halpern J.P. et al.             
 770      4         2005AJ....129.1783H Hao L. et al.                   
 771      1         1960BOTT....2s..17H Haro G. et al.                  
 772             1  1982A&A...111..299H Harris D.E. et al.              
 773      2      2  1983ApJ...270...39H Harris D.E. et al.              
 774     10      8  1992AJ....104...53H Harris H.C. et al.              
 775     14     14  ................... Harris K.A.                     2012, PhDT 15, (Ph.D. thesis, arXiv 1201.5746)
 776                2002Msngr.108...11H Hasinger G. et al.              
 777             1  1983MNRAS.202..571H Hawkins M.R.S. et al.           
 778      4      4  1985MNRAS.214..241H Hawkins M.R.S. et al.           
 779     29      2  1986MNRAS.219..417H Hawkins M.R.S. et al.           
 780      2         1991A&A...248..421H Hawkins M.R.S. et al.           
 781     68     71  1993MNRAS.260..202H Hawkins M.R.S. et al.           
 782      2         1993Msngr..74...27H Hawkins M.R.S. et al.           
 783     97     99  1995MNRAS.275.1102H Hawkins M.R.S. et al.           
 784      1      1  1996MNRAS.281..348H Hawkins M.R.S. et al.           
 785      2         1996MNRAS.280L...1H Hawkins M.R.S. et al.           
 786      1      1  1997MNRAS.291..811H Hawkins M.R.S. et al.           
 787    129    130  2000A&AS..143..465H Hawkins M.R.S. et al.           
 788      1         1967ApJ...148..669H Hazard C. et al.                
 789      1         1968ApJ...154..413H Hazard C. et al.                
 790      1         1973Natur.246..205H Hazard C. et al.                
 791      6         1977AuJPA..42....1H Hazard C. et al.                
 792      5      1  1979Natur.282..271H Hazard C. et al.                
 793      9         1984ApJ...282...33H Hazard C. et al.                
 794      1         1984MNRAS.211p..45H Hazard C. et al.                
 795      1      1  1985Natur.314..238H Hazard C. et al.                
 796     41      2  1986MNRAS.223...87H Hazard C. et al.                
 797      1         1986Natur.322...38H Hazard C. et al.                
 798      2         1987MNRAS.229..371H Hazard C. et al.                
 799     24      5  ................... Hazard C. et al.                1992, private communication to HB
 800     92     69  ................... Hazard C. et al.                2013, in preparation
 801     10         1993Ap&SS.200..279H He R. et al.                    
 802     13         1984MNRAS.211..443H He X.-T. et al.                 
 803     11      2  2001AJ....121.1863H He X.-T. et al.                 
 804    311    323  2008ApJS..175...97H Healey S.E. et al.              
 805      1         1994ApJ...428...65H Heckman T.M. et al.             
 806      1         1999A&A...348..113H Heidt J. et al.                 
 807      1      1  2003A&A...406..565H Heidt J. et al.                 
 808             1  2004A&A...418..813H Heidt J. et al.                 
 809             1  1997Natur.385..700H Heisler C.A. et al.             
 810      3         2001AJ....121.1872H Helfand D.J. et al.             
 811    137    109  2006AJ....131....1H Hennawi J.F. et al.             
 812      2      2  2006ApJ...651...61H Hennawi J.F. et al.             
 813     26     18  2010ApJ...719.1672H Hennawi J.F. et al.             (hi-z binary quasars)
 814      2         1985AJ.....90.1425H Henry J.P. et al.               
 815      1         1994AJ....107.1270H Henry J.P. et al.               
 816     25     28  1997MNRAS.290..380H Henstock B.R. et al.            
 817             1  1992ApJS...81...83H Herbig T. et al.                
 818      7      7  2009MNRAS.395.1695H Hernan-Caballero A. et al.      
 819      1      1  1984ApJ...278..137H Hertz P. et al.                 
 820      2      2  1988AJ.....96..233H Hertz P. et al.                 
 821                1996A&A...313..423H Hes R. et al.                   
 822     42     30  1991AJ....101.1121H Hewett P.C. et al.              
 823      1      1  1994AJ....108.1534H Hewett P.C. et al.              
 824    114    122  1995AJ....109.1498H Hewett P.C. et al.              (LBQS)
 825      1      1  1998AJ....115..383H Hewett P.C. et al.              
 826      6      6  2001AJ....122..518H Hewett P.C. et al.              
 827      1      1  1980ApJS...43...57H Hewitt A. et al.                
 828     24      5  1987ApJS...63....1H Hewitt A. et al.                
 829      9     10  1993ApJS...87..451H Hewitt A. et al.                
 830      2      2  1987ApJ...321..706H Hewitt J.N. et al.              
 831      1         1992AJ....104..968H Hewitt J.N. et al.              
 832      6      1  2007MNRAS.381.1093H Heywood I. et al.               
 833      1      1  2002ApJ...581..205H Hicks E.K.S. et al.             
 834      1      1  1988AJ.....95.1031H Hill G.J. et al.                
 835             1  1996ApJ...462..163H Hill G.J. et al.                
 836      1      1  1991A&A...244...37H Hiltner P.R. et al.             
 837      2      2  2010ApJ...718..133H Hilton M. et al.                (XMM Cluster survey)
 838             1  2001ApJ...563..512H Hines D.C. et al.               
 839      7         1983AJ.....88..709H Hintzen P. et al.               
 840      1         1989A&A...216...11H Hippelein H.H. et al.           
 841     13     11  2012ApJ...758...49H Hiroi K. et al.                 (Subaru-XMM Deep)
 842                1993ApJ...417...63H Ho L.C. et al.                  
 843             2  1995ApJS...98..477H Ho L.C. et al.                  
 844             2  1997ApJS..112..315H Ho L.C. et al.                  
 845      1      5  1997ApJS..112..391H Ho L.C. et al.                  
 846      2     30  2009ApJS..184..398H Ho L.C. et al.                  
 847      2         1976PASP...88..860H Hoag A.A. et al.                
 848     69      2  1977ApJ...217..362H Hoag A.A. et al.                
 849     34     21  1982ApJ...263...23H Hoag A.A. et al.                
 850      5      6  1986IAUS..119...47H Hoag A.A. et al.                
 851             1  1977A&AS...27..295H Holmberg E.B. et al.            
 852      6         2004MNRAS.348..857H Holt J. et al.                  
 853      7     10  1994MNRAS.268..305H Hook I.M. et al.                
 854     32     22  1996MNRAS.282.1274H Hook I.M. et al.                
 855     18      4  1998MNRAS.297.1115H Hook I.M. et al.                
 856      2      1  1998MNRAS.294L...7H Hook I.M. et al.                
 857     12     11  2002A&A...391..509H Hook I.M. et al.                
 858           142  2003A&A...399..469H Hook I.M. et al.                
 859      4         2000A&AS..142..417H Hopp U. et al.                  
 860     13     11  2001ApJ...554..742H Hornschemeier A.E. et al.       
 861      7         1972AuJPh..25..559H Hoskins D.G. et al.             
 862     11         1974MNRAS.166..235H Hoskins D.G. et al.             
 863      1      1  1993PASP..105..383H Howell S.B. et al.              
 864      1         1997PASP..109.1149H Howell S.B. et al.              
 865      1         1991ApJ...368...28H Hu E.M. et al.                  
 866     85         1984ApJS...56..393H Huang K.-L. et al.              
 867      3         1986Ap&SS.125...85H Huang K.-L. et al.              
 868             1  1982AJ.....87.1628H Huchra J.P. et al.              
 869                ................... Huchra J.P. et al.              1984, private communication to HB
 870             1  1985AJ.....90..691H Huchra J.P. et al.              
 871                1991ApJ...370..495H Huchra J.P. et al.              
 872      1      1  1991ApJS...75..297H Huchra J.P. et al.              (private comm to Hewitt & Burbidge)
 873             4  1999ApJS..121..287H Huchra J.P. et al.              http://www.cfa.harvard.edu/~huchra/zcat
 874      5      3  2012ApJS..199...26H Huchra J.P. et al.              http://tdc-www.harvard.edu/2mrs/
 875      1      1  2008MNRAS.383...11H Humphrey A. et al.              
 876      1         1970MNRAS.149...91H Hunstead R.W. et al.            
 877      2         1971AuJPh..24..601H Hunstead R.W. et al.            
 878      2         1971MNRAS.152..277H Hunstead R.W. et al.            
 879     11      8  1978MNRAS.185..149H Hunstead R.W. et al.            
 880             1  1980MNRAS.192p..31H Hunstead R.W. et al.            
 881             1  1984MNRAS.207...55H Hunstead R.W. et al.            
 882             1  1993ApJ...409..134H Hunter S.D. et al.              
 883    519    455  2013AJ....145..159H Huo Z.-Y. et al.                (LAMOST Andromeda pilot)
 884      1         1988ApJS...66..361H Hutchings J.B. et al.           
 885      1         1995AJ....109..928H Hutchings J.B. et al.           
 886      1         1997AJ....113.1514H Hutchings J.B. et al.           
 887            36  2003AJ....126...63H Hutchings J.B. et al.           
 888      5      5  2008AJ....135.2470H Huynh M.T. et al.               
 889     34     37  2007ApJ...664...64I Im M. et al.                    
 890             1  1986MNRAS.221..897I Impey C.D. et al.               
 891      1         2002ApJ...574..623I Impey C.D. et al.               
 892      3      3  2003Natur.426..810I Inada N. et al.                 
 893      1      1  2006ApJ...653L..97I Inada N. et al.                 (SDSS doubles)
 894     14     14  2008AJ....135..496I Inada N. et al.                 
 895     28     27  2012AJ....143..119I Inada N. et al.                 (SDSS Lens Search)
 896      5      5  2003ApJ...588...90I Infante L. et al.               
 897   1140   1141  1996A&AS..119..265I Iovino A. et al.                
 898      4         1957BOTT....2p...3I Iriarte B. et al.               
 899      1         1998ApJ...505..529I Irwin M.J. et al.               
 900                1998MNRAS.298..583I Ivison R.J. et al.              
 901    107      3  2002A&A...386...97J Jackson C.A. et al.             
 902            11  1991MNRAS.250..414J Jackson N. et al.               
 903             3  1995MNRAS.276.1409J Jackson N. et al.               
 904             1  1995MNRAS.274L..25J Jackson N. et al.               
 905      1      1  1998A&A...334L..33J Jackson N. et al.               (Lensing galaxies)
 906      1         1975A&AS...21..137J Jaffe W.J. et al.               
 907      1         1974ArA.....5..345J Jaidee S. et al.                
 908             1  1988ApJ...326..710J Jakobsen P. et al.              
 909             9  1992ApJ...392..432J Jakobsen P. et al.              
 910      2      1  2003A&A...397..891J Jakobsen P. et al.              
 911      2         2005AJ....130..496J Jangren A. et al.               
 912      1      1  1993ApJ...404..100J Jannuzi B.T. et al.             
 913      1      9  2000A&A...359..429J Jansen R.A. et al.              
 914      3      3  2001MNRAS.326.1563J Jarvis M.J. et al.              
 915                2005MNRAS.358L..11J Jarvis M.J. et al.              
 916      3         1970ApL.....7....1J Jauncey D.L. et al.             
 917            12  1978ApJ...219L...1J Jauncey D.L. et al.             
 918     18      5  1982AJ.....87..763J Jauncey D.L. et al.             
 919      1     25  1984ApJ...286..498J Jauncey D.L. et al.             
 920     14      1  1989AJ.....98...54J Jauncey D.L. et al.             
 921     20     13  1995A&A...300..323J Jaunsen A.O. et al.             
 922      1         1997A&A...317L..39J Jaunsen A.O. et al.             
 923    160    176  2006AJ....131.2788J Jiang L. et al.                 
 924      4      5  2008AJ....135.1057J Jiang L. et al.                 
 925      6      6  2009AJ....138..305J Jiang L. et al.                 
 926      2      2  2000A&A...362..263J Jiang X.J. et al.               
 927             1  2000MNRAS.317..907J Jimenez-Benito L. et al.        
 928                1988A&A...191...29J Johansson L. et al.             
 929                1988A&AS...73..335J Johansson L. et al.             
 930                1990A&AS...86..167J Johansson L. et al.             
 931     11         1974AJ.....79.1006J Johnson K.H. et al.             
 932             2  1995AJ....110..880J Johnston K.J. et al.            
 933    195    208  2009MNRAS.399..683J Jones D.H. et al.               (6dF Galaxy Survey)
 934      1      1  1992ApJS...80..137J Jones P.A. et al.               
 935      2      1  2006ApJ...646..730J Jorgenson R.A. et al.           
 936      2         ................... Joshi M.N. et al.               1980, Mem. Astron. Soc. India 1, 49
 937             1  1984PASP...96..539J Junkkarinen V.T. et al.         
 938      1      1  1993BAAS...25.1445J Junkkarinen V.T. et al.         
 939             1  2001ApJ...549L.155J Junkkarinen V. et al.           
 940      1         1973AJ.....78..673K Kapahi V.K. et al.              
 941      1         1973ApL....14...31K Kapahi V.K. et al.              
 942      2         1979A&A....74L..11K Kapahi V.K. et al.              
 943      2         1981A&AS...43..381K Kapahi V.K. et al.              
 944     56         1998ApJS..118..327K Kapahi V.K. et al.              
 945      1      1  ................... Kashikawa N. et al.             2014, ArXiv 1410, 7401 (Subaru hi-z)
 946      2         1978A&AS...31..409K Katgert J.K. et al.             
 947      1         1979A&AS...36..213K Katgert P. et al.               
 948             1  1983ApJ...275....1K Katgert P. et al.               
 949      1         1980A&AS...40...91K Katgert-Merkelijn J. et al.     
 950             2  1999ApJ...518..219K Kay L.E. et al.                 
 951      1         1979Ap.....15....1K Kazarian M.A. et al.            
 952      1         1980Ap.....16....7K Kazarian M.A. et al.            
 953                1987Ap.....26....1K Kazarian M.A. et al.            
 954                1988Ap.....27..569K Kazarian M.A. et al.            
 955                1994Ap.....37..329K Kazarian M.A. et al.            
 956                1983ApJS...52..229K Keel W.C. et al.                
 957             1  1984ApJ...282...75K Keel W.C. et al.                
 958      1         1988A&A...203..250K Keel W.C. et al.                
 959     14         1996AJ....111..696K Keel W.C. et al.                
 960      2      2  2002AJ....123.3041K Keel W.C. et al.                
 961      2      3  2005ApJS..158..139K Keel W.C. et al.                
 962             1  1998AJ....115.1295K Kellermann K.I. et al.          
 963             1  2007ApJS..168....1K Kelly C.B. et al.               
 964      5         1995AJ....110...78K Kennefick J.D. et al.           
 965      4         1995AJ....110.2553K Kennefick J.D. et al.           
 966      4      1  1996AJ....111.1816K Kennefick J.D. et al.           
 967      2      3  1997AJ....114.2269K Kennefick J.D. et al.           
 968                1984ApJ...279L...5K Kennicutt R.C. et al.           
 969                1989AJ.....97.1022K Kennicutt R.C. et al.           
 970                2000ApJ...530..704K Kewley L.J. et al.              
 971             1  2001ApJS..132...37K Kewley L.J. et al.              
 972      1         1998ApJ...508..627K Kim D.-C. et al.                
 973      3      2  1999ApJ...516....9K Kim D.-W. et al.                
 974      7      7  2013ApJ...768L...9K Kim M. et al.                   
 975      1         1966ApJ...144.1232K Kinman T. et al.                
 976      6         1967ApJ...147..848K Kinman T. et al.                
 977             2  1990AJ.....99.1722K Kirhakos S.D. et al.            
 978             1  2001ApJ...547..667K Kishimoto M. et al.             
 979                1991A&AS...90...33K Klaas U. et al.                 
 980                1993A&A...280...76K Klaas U. et al.                 
 981                1993A&AS...99...71K Klaas U. et al.                 
 982      2         1987AJ.....94..501K Klemola A.R. et al.             (NPM1) Cat. I/200
 983     14      4  1998AJ....115.1737K Knezek P.M. et al.              
 984      6      1  2001A&A...366..771K Kniazev A.Y. et al.             
 985      1      1  2003A&A...411..343K Knudsen K.K. et al.             
 986      1         1997ApJ...479..678K Kochanek C.S. et al.            
 987    848    848  2012ApJS..200....8K Kochanek C.S. et al.            (AGES survey)
 988      9      4  1996A&A...307..745K Kock A. et al.                  
 989      1         1998A&A...329...68K Koenig M. et al.                
 990      3      3  2001A&A...379..215K Koester D. et al.               (ESO WD candidates)
 991             1  1983A&A...125..276K Kollatschny W. et al.           
 992                1987A&A...183....9K Kollatschny W. et al.           
 993             7  2006A&A...454..459K Kollatschny W. et al.           
 994      9     17  2008A&A...484..897K Kollatschny W. et al.           
 995             3  1995ApJ...449...61K Kollgaard R.I. et al.           
 996    107         1984AnTok..20..130K Kondo M. et al.                 
 997      1         1981ApJ...251L..75K Koo D.C. et al.                 
 998     28      4  1986PASP...98..285K Koo D.C. et al.                 
 999             2  1988ApJ...325...92K Koo D.C. et al.                 
1000      1      1  2000A&A...361..815K Koopmans L.V.E. et al.          
1001     18      5  2004A&A...421..455K Kopylov A.I. et al.             
1002      4      7  1993ApJS...88..357K Korista K.T. et al.             
1003                1978ApJ...223...56K Koski A.T. et al.               
1004     31     31  2011ApJS..194...22K Kozlowski S. et al.             (SMC Magellanic)
1005    142    136  2012ApJ...746...27K Kozlowski S. et al.             (LMC Magellanic)
1006    543    574  2013ApJ...775...92K Kozlowski S. et al.             (Magellanic Quasars)
1007             1  1995A&A...297..617K Kraan-Korteweg R.C. et al.      
1008     13      1  1982ApJ...261...51K Kriss G.A. et al.               
1009             1  1985ApJ...297..177K Kriss G.A. et al.               
1010      3         1970ApJ...162..391K Kristian J. et al.              
1011      3         1974ApJ...191...43K Kristian J. et al.              
1012      1         1978ApJ...219..803K Kristian J. et al.              
1013    113    101  ................... Krogager J.-K. et al.           2014, ArXiv 1410, 7783, (High AV Quasar survey)
1014             1  1996ApJ...463L..55K Kroker H. et al.                
1015      9      8  1983A&A...127...29K Kron R.G. et al.                
1016             5  1985A&A...146...38K Kron R.G. et al.                
1017             1  1977ApJ...218....8K Kronberg P.P. et al.            
1018      2         2001AJ....121..702K Krongold Y. et al.              
1019     43     60  2007A&A...466...41K Krumpe M. et al.                
1020      2         2007A&A...470..497K Krumpe M. et al.                
1021                2008A&A...483..415K Krumpe M. et al.                
1022      4      4  2005A&A...439..497K Kuhlbrodt B. et al.             
1023     35         1977A&AS...29..139K Kuhr H. et al.                  
1024      1         ................... Kuhr H. et al.                  1980, Ph.D. Bonn
1025      1         1983ApJ...275L..33K Kuhr H. et al.                  
1026     37      5  1987A&AS...71..493K Kuhr H. et al.                  
1027      1         1985A&AS...61....1K Kulkarni V.K. et al.            
1028             1  1979A&A....76...50K Kunth D. et al.                 
1029                1979A&AS...36..259K Kunth D. et al.                 
1030     23     19  1981A&AS...44..229K Kunth D. et al.                 
1031     66     47  1986AJ.....91..761K Kunth D. et al.                 
1032     25      6  1992AJ....103.1062L La Franca F. et al.             
1033    216    228  1999A&AS..140..351L La Franca F. et al.             
1034     13     13  2002ApJ...570..100L La Franca F. et al.             
1035     21     21  2004AJ....127.3075L La Franca F. et al.             
1036      1      1  2007A&A...463...97L Labiano A. et al.               
1037      6      3  1993MNRAS.263..707L Lacy M. et al.                  
1038                1999MNRAS.307..420L Lacy M. et al.                  
1039      7      7  1999MNRAS.308.1096L Lacy M. et al.                  
1040      1         2002AJ....123.2925L Lacy M. et al.                  
1041     22     13  2007AJ....133..186L Lacy M. et al.                  
1042     90     85  2013ApJS..208...24L Lacy M. et al.                  (Spitzer mid-IR survey)
1043     13      5  1991A&AS...88..525L Lahulla J.F. et al.             
1044      2         1978MNRAS.183..547L Laing R.A. et al.               
1045      1         1983MNRAS.204..151L Laing R.A. et al.               (3CRR)
1046     15     15  2012AJ....143....7L Lake S.E. et al.                
1047     33     30  1997A&A...327..467L Lamer G. et al.                 
1048     22      9  2000AJ....119..241L Lamontagne R. et al.            
1049      1      3  2007ApJ...669..109L Landi R. et al.                 
1050      1      1  2013AJ....145..114L Landoni M. et al.               
1051     74     65  2001MNRAS.323..757L Landt H. et al.                 
1052      6      6  2004MNRAS.351...83L Landt H. et al.                 (Blazar classification)
1053      1      1  1989AJ.....97.1283L Langston G.I. et al.            
1054     11     14  1991ApJS...77....1L Lanzetta K.M. et al.            
1055                2009A&A...498...67L Lanzuisi G. et al.              
1056      2      1  2001A&A...378..826L Lara L. et al.                  
1057             1  2000ApJ...533L..61L Larkin J.E. et al.              
1058     57     62  1998ApJS..118..127L Laurent-Muehleisen S.A. et al.  
1059      7      4  1999ApJ...525..127L Laurent-Muehleisen S.A. et al.  
1060                1988AJ.....96..470L Laurikainen E. et al.           
1061      2      4  1999MNRAS.308..897L Lawrence A. et al.              
1062      2      1  1984Sci...223...46L Lawrence C.R. et al.            
1063     38      2  1986ApJS...61..105L Lawrence C.R. et al.            
1064             1  1995AJ....110.2570L Lawrence C.R. et al.            
1065      2     15  1996ApJS..107..541L Lawrence C.R. et al.            
1066      1      1  1990A&A...229L..13L Le Borgne J.F. et al.           
1067      1         1998A&A...340..381L Le Brun V. et al.               
1068      1         1976ApJ...206L..87L Leacock R.J. et al.             
1069      4      2  1999A&AS..138..109L Ledoux C. et al.                
1070      7      4  2008ApJS..175..116L Lee I. et al.                   
1071      1         1994MNRAS.267..253L Leech K.J. et al.               
1072      2      1  2001ApJ...547...60L Lehar J. et al.                 
1073     38     30  2000A&A...354...35L Lehmann I. et al.               
1074     26     24  2001A&A...371..833L Lehmann I. et al.               
1075      1      1  2009ApJ...694..734L Lehner N. et al.                
1076      1      1  2001AJ....121.2889L Leighly K. et al.               
1077     12     10  2005A&A...440L...5L Leipski C. et al.               
1078                2007A&A...464..895L Leipski C. et al.               
1079      1      1  2007A&A...473..121L Leipski C. et al.               
1080      1         1987A&AS...67..169L Lequeux J. et al.               
1081      1         2004A&A...424..455L Letawe G. et al.                
1082      1         2009MNRAS.396...78L Letawe G. et al.                
1083                1998ApJ...504...64L Levine D.A. et al.              
1084            14  1979ApJ...233..787L Lewis D.W. et al.               
1085                2003ApJ...593..115L Lewis K.T. et al.               
1086      1      1  2003MNRAS.340..632L Liang E.W. et al.               
1087      1      1  2004A&A...423..867L Liang Y.C. et al.               
1088      1      1  1999ApJ...514L..57L Lidman C. et al.                
1089             1  1991ApJ...366L..65L Lipari S. et al.                
1090             1  1991MNRAS.253...19L Lipari S. et al.                
1091             2  1992ApJ...387..522L Lipari S. et al.                
1092             1  1992ApJ...397..126L Lipari S. et al.                
1093             1  1993ApJ...406..451L Lipari S. et al.                
1094                1997ApJS..111..369L Lipari S. et al.                
1095                1989Ap.....31..665L Lipovetski V.A. et al.          
1096             3  1990SvA....33..585L Lipovetski V.A. et al.          
1097      1      1  2007MNRAS.382.1552L Lira P. et al.                  
1098     14      4  1999AJ....118.1912L Liu C.T. et al.                 
1099             1  1999ApJS..122..257L Liu W. et al.                   
1100      2      2  2002MNRAS.334..941L Londish D. et al.               
1101      1      1  ................... Londish D.                      2003, Ph.D. thesis U of Sydney 'Properties of BL Lac objects from the 2dF redshift survey'
1102     12     14  2007MNRAS.374..556L Londish D. et al.               
1103      2         1975MNRAS.170..121L Longair M.S. et al.             
1104      2      9  2001A&A...366..387L Lopez S. et al.                 
1105      6      6  2008A&A...480...61L Lopez-Corredoira M. et al.      
1106      1         1978ApL....19..117L Lorenz H. et al.                
1107             1  1979AN....300...81L Lorenz H. et al.                
1108      2         1993ApJS...84....1L Lu L. et al.                    
1109      2         1970AJ.....75.1161L Lu P.K. et al.                  
1110      1      1  1996IAUC.6526....1L Luginbuhl C. et al.             
1111             1  2001MNRAS.327..459L Lumsden S.L. et al.             
1112             2  2004MNRAS.348.1451L Lumsden S.L. et al.             
1113      1      1  2009ApJ...695.1227L Luo B. et al.                   
1114      1      1  2012AstL...38..281L Lutovinov A.A. et al.           (BTA SWIFT Hard)
1115             2  1967ApJ...147..837L Lynds C.R. et al.               
1116      2         1968ApJ...153L..23L Lynds C.R. et al.               
1117     14      1  1977ApJS...34...95M MacAlpine G.M. et al.           
1118     23      1  1977ApJS...35..197M MacAlpine G.M. et al.           
1119     32      1  1977ApJS...35..203M MacAlpine G.M. et al.           
1120     16         1978ApJS...36..587M MacAlpine G.M. et al.           
1121     35      1  1981ApJS...45..113M MacAlpine G.M. et al.           
1122     30     19  1982ApJ...261..412M MacAlpine G.M. et al.           
1123    251      4  1994ApL....29..267M Maccacaro T. et al.             
1124      1         1990AJ....100.1461M Maccagni D. et al.              
1125      1         1982AJ.....87.1150M Machalski J. et al.             
1126      1         1983AJ.....88..143M Machalski J. et al.             
1127     11         1983AJ.....88.1591M Machalski J. et al.             
1128      1         1985AJ.....90....5M Machalski J. et al.             
1129             2  1991AcA....41...39M Machalski J. et al.             
1130      2         1993A&AS..102..315M Machalski J. et al.             
1131                1999ApJS..123...41M Machalski J. et al.             
1132                2001A&A...371..445M Machalski J. et al.             
1133      2      2  2006A&A...454...85M Machalski J. et al.             
1134     77     57  2008MNRAS.386.1605M Maddox N. et al.                
1135    274    157  2012MNRAS.424.2876M Maddox N. et al.                (KX quasars)
1136     25     43  2002MNRAS.334..209M Madgwick D.S. et al.            
1137             1  2005Natur.437..381M Magain P. et al.                
1138      3         2000MNRAS.318.1047M Magliocchetti M. et al.         
1139      1      1  2005ApJ...634L...9M Mahabal A. et al.               
1140      2      1  2008ATel.1520....1M Mahabal A. et al.               
1141             2  1987AJ.....93..546M Maia M.A.G. et al.              
1142             3  1996A&AS..117..487M Maia M.A.G. et al.              
1143      1      3  2003AJ....126.1750M Maia M.A.G. et al.              
1144             1  2004A&A...420..889M Maiolino R. et al.              
1145      1      1  2006A&A...445..457M Maiolino R. et al.              
1146                2000A&A...359..509M Malizia A. et al.               
1147     11     11  2012MNRAS.426.1750M Malizia A. et al.               (INTEGRAL/IBIS AGN)
1148      1         1963ApJ...137..153M Maltby P. et al.                
1149      1      1  2002MNRAS.330..390M Manners J. et al.               
1150      2      1  2007A&A...468..807M Mannucci F. et al.              
1151             1  1992MNRAS.257..353M Mantovani F. et al.             
1152     68     69  2012MNRAS.426.3334M Mao M.Y. et al.                 
1153      1         1992ApJ...394...51M Maoz D. et al.                  
1154      1      1  1996A&A...308..511M Maoz D. et al.                  
1155      1     15  2003ApJ...590..707M Marble A.R. et al.              
1156      8     47  2013MNRAS.430.2464M March M.J.M. et al.             (CLASS Bl Lacs)
1157             3  1996MNRAS.281..425M Marcha M.J.M. et al.            
1158                1994Msngr..78...20M Marconi A. et al.               
1159      1         1981Natur.290..480M Margon B. et al.                
1160             1  1983Natur.301..221M Margon B. et al.                
1161     16     20  1985ApJS...59...23M Margon B. et al.                
1162      2      1  1986PASP...98.1129M Margon B. et al.                
1163      1         1997PASP..109..673M Margon B. et al.                
1164      1         1999PASP..111...45M Margon B. et al.                
1165      2         1967Ap......3...24M Markarian B.E. et al.           
1166      5         1969Ap......5..206M Markarian B.E. et al.           
1167      1         1969Ap......5..286M Markarian B.E. et al.           
1168      1         1971Ap......7..299M Markarian B.E. et al.           
1169      3         1972Ap......8...89M Markarian B.E. et al.           
1170      6         1973Ap......9..283M Markarian B.E. et al.           
1171      2         1974Ap.....10..185M Markarian B.E. et al.           
1172      3         1976Ap.....12..241M Markarian B.E. et al.           
1173      7         1976Ap.....12..429M Markarian B.E. et al.           
1174      3         1977Ap.....13..116M Markarian B.E. et al.           
1175                1977Ap.....13..215M Markarian B.E. et al.           
1176      3         1979Ap.....15..130M Markarian B.E. et al.           
1177      3         1979Ap.....15..235M Markarian B.E. et al.           
1178      2         1979Ap.....15..363M Markarian B.E. et al.           
1179      3         1981Ap.....17..321M Markarian B.E. et al.           
1180      8         1983Ap.....19...14M Markarian B.E. et al.           
1181     17         1983Ap.....19..354M Markarian B.E. et al.           
1182     13      1  1984Ap.....20...10M Markarian B.E. et al.           
1183      3         1984Ap.....20..278M Markarian B.E. et al.           
1184     21         1986Ap.....23..623M Markarian B.E. et al.           
1185     12         1986Afz....25..345M Markarian B.E. et al.           
1186             1  1987Ap.....26....7M Markarian B.E. et al.           
1187      1      1  1987IAUS..121...25M Markarian B.E. et al.           
1188             1  1988Ap.....28...14M Markarian B.E. et al.           
1189     25     26  2000AJ....119.2629M Marlow D.R. et al.              
1190      9      9  1984ApJ...283...50M Marshall H.L. et al.            
1191             1  1994AJ....107.1283M Martel A. et al.                
1192      1      1  1998A&A...330...72M Marti J. et al.                 
1193      7      7  2006MNRAS.370.1479M Martinez-Sansigre A. et al.     
1194      7      7  2008ApJ...674..676M Martinez-Sansigre A. et al.     
1195      1      1  2002ApJ...576L.109M Martini P. et al.               
1196      2      2  2006ApJ...644..116M Martini P. et al.               
1197     72     72  2007ApJ...664..761M Martini P. et al.               
1198      2      2  2009ApJ...701...66M Martini P. et al.               
1199             2  1996ApJS..104...37M Marziani P. et al.              
1200                1999AJ....117.2736M Marziani P. et al.              
1201     20     25  2009A&A...495...83M Marziani P. et al.              
1202    119    123  2010PASA...27..302M Masci F.J. et al.               (Southern 2MASS AGN using 6dF)
1203      1      2  2006A&A...455...11M Masetti M. et al.               
1204      4      6  2006A&A...459...21M Masetti M. et al.               
1205      2      2  2004A&A...426L..41M Masetti N. et al.               
1206             1  2006A&A...448..547M Masetti N. et al.               
1207      1      2  2006A&A...449.1139M Masetti N. et al.               
1208                2006NewA...11..411M Masetti N. et al.               
1209                2006ATel..941....1M Masetti N. et al.               
1210                2007ATel.1033....1M Masetti N. et al.               
1211             1  2008A&A...480..715M Masetti N. et al.               
1212      8     13  2008A&A...482..113M Masetti N. et al.               
1213      6      5  2009A&A...495..121M Masetti N. et al.               
1214      7      8  2012A&A...538..123M Masetti N. et al.               (Integral IX)
1215     11     11  2013A&A...556..120M Masetti N. et al.               (Integral X)
1216      2         1993AJ....105...30M Maslowski J. et al.             
1217      2         1995MNRAS.274.1194M Mason K.O. et al.               
1218    183     92  2000MNRAS.311..456M Mason K.O. et al.               
1219      2      2  2008MNRAS.384..775M Massardi M. et al.              (AT20G)
1220    106    175  2009A&A...495..691M Massaro E. et al.               BZCAT v4.1.1
1221     23     22  2012ApJ...755..169M Masters D. et al.               (COSMOS hi-z)
1222      1      1  1999IAUC.7228R...1M Matheson T. et al.              
1223      3         1963ApJ...138...30M Matthews T.A. et al.            
1224      1      1  2013A&A...557...78M Matute I. et al.                
1225     60    187  2007MNRAS.375..931M Mauch T. et al.                 
1226             2  1995PASP..107..566M Maxfield L. et al.              
1227      5         1989ApJS...69..349M Maza J. et al.                  
1228            24  1989ApJS...69..353M Maza J. et al.                  
1229      7         1992RMxAA..24..147M Maza J. et al.                  
1230    198         1993RMxAA..25...51M Maza J. et al.                  
1231     10    171  1994RMxAA..28..187M Maza J. et al.                  
1232     96     87  1995RMxAA..31..119M Maza J. et al.                  
1233     95         1995RMxAA..31..159M Maza J. et al.                  
1234            87  1995RMxAA..31..159M Maza J. et al.                  
1235     94     83  1996RMxAA..32...35M Maza J. et al.                  
1236                2007A&A...463..445M Mazzalay X. et al.              
1237      7         1993ApJS...85...27M Mazzarella J.M. et al.          
1238      1         1990AJ....100.1014M McCarthy P.J. et al.            
1239      1      1  1991AJ....102..518M McCarthy P.J. et al.            
1240      2      2  1991AJ....102..522M McCarthy P.J. et al.            
1241      9      9  1993ApJ...411..650M McCausland R.J.H. et al.        (M31 halo stars)
1242     11         1975MmRAS..80....1M McEwan N.J. et al.              
1243             1  2006ApJ...652..157M McGreer I.D. et al.             
1244     13     10  2009AJ....138.1925M McGreer I. et al.               (SDSS Radio)
1245     56     56  2013ApJ...768..105M McGreer I.D. et al.             (High Redshift Stripe 82)
1246     12     17  1998MNRAS.295..641M McHardy I.M. et al.             
1247      1     13  1999ApJ...514...40M McIntosh D.H. et al.            
1248     58     44  2004AJ....128..544M McIntosh D.H. et al.            
1249      1      1  2011MNRAS.412..900M McKean J.P. et al.              
1250             1  2001MNRAS.327..199M McLure R.J. et al.              
1251      1      1  ................... McMahon R.G. et al.             private comm to Warren et al., 1991ApJS...76...23M
1252             1  2005A&A...433...79M Mediavilla E. et al.            
1253      1         2009RAA.....9..269M Mei L. et al.                   
1254      1         1975MitVS...7....1M Meinunger L. et al.             
1255      4         1983A&AS...51...41M Meisenheimer K. et al.          
1256      2      1  2004AJ....127..686M Melbourne J. et al.             
1257      1         1990A&A...231L..19M Melnick J. et al.               
1258      1         2007A&A...465..759M Memola E. et al.                
1259      1      1  1989AJ.....97.1576M Menzies J.W. et al.             
1260                1991A&AS...89..225M Merighi R. et al.               
1261      6         1968AuJPh..21..523M Merkelijn J. et al.             
1262      3         1968AuJPh..21..903M Merkelijn J. et al.             
1263     10         1969AuJPh..22..237M Merkelijn J. et al.             
1264      1         1970AuJPh..23..575M Merkelijn J. et al.             
1265      2         1972AuJPh..25..451M Merkelijn J. et al.             
1266      1      1  2009ATel.2132....1M Mescheryakov A. et al.          
1267     61     60  2001A&A...374..878M Meusinger H. et al.             
1268                2001A&A...379..845M Meusinger H. et al.             
1269     76     31  2002A&A...392..851M Meusinger H. et al.             
1270     33     30  2003AN....324..474M Meusinger H. et al.             
1271      2      2  2005A&A...433L..25M Meusinger H. et al.             
1272      4      4  2011A&A...525...37M Meusinger H. et al.             (Spectral variablility of SDSS Stripe82 QSOs)
1273     65     69  2001MNRAS.324..343M Meyer M.J. et al.               
1274      1      1  1999Ap.....42....1M Mickaelian A.M. et al.          
1275      3      2  2001Ap.....44...14M Mickaelian A.M. et al.          
1276                2004Ap.....47..361M Mickaelian A.M. et al.          
1277      4      4  2002A&A...383..823M Mieske S. et al.                
1278             2  2002ApJ...569..134M Miller E.D. et al.              
1279             2  1990ApJ...355..456M Miller J.S. et al.              
1280             2  2004MNRAS.348..395M Miller L. et al.                
1281      1      1  1982MNRAS.200.1007M Mills B.Y. et al.               
1282      1         1958PASP...70..143M Minkowski R. et al.             
1283      1      1  2000MNRAS.315..839M Minns A.R. et al.               
1284     10     10  2000ApJ...541..180M Mirabal N. et al.               
1285      1      1  2009ApJ...701L.129M Mirabal N. et al.               
1286      2         2006AJ....131...34M Misawa T. et al.                
1287      1         1985AJ.....90.1957M Mitchell K.J. et al.            
1288             3  2004ApJS..153..119M Mitchell K.J. et al.            
1289      3      1  1990MNRAS.244....1M Mitchell P.S. et al.            
1290      2      3  1977MNRAS.179..569M Mitton S. et al.                
1291      6      3  2004AJ....127.3180M Miyaji T. et al.                
1292      1      1  1983ApJ...271L..45M Moffat A.F.J. et al.            
1293             1  1994A&A...287..719M Moller P. et al.                
1294     28      5  1997A&AS..126..509M Molthagen K. et al.             
1295      1         1998A&A...331..925M Molthagen K. et al.             
1296      1         2000A&A...361..444M Molthagen K. et al.             
1297      2      2  2002AJ....124.2971M Monier E.M. et al.              
1298      5      4  1986MNRAS.222..787M Monk A.S. et al.                
1299     40     50  1988MNRAS.234..193M Monk A.S. et al.                
1300                1999Msngr..95....1M Moorwood A. et al.              
1301      1         1992AJ....104..990M Moran E.C. et al.               
1302             6  1994ApJ...433L..65M Moran E.C. et al.               
1303     15     18  1996ApJ...461..127M Moran E.C. et al.               
1304      1     37  1996ApJS..106..341M Moran E.C. et al.               
1305             4  2000ApJ...540L..73M Moran E.C. et al.               
1306      1      1  2007ApJ...668L..31M Moran E.C. et al.               
1307      1      1  2001MNRAS.327.1187M Morel T. et al.                 
1308      1      1  2006ATel..785....1M Morelli L. et al.               
1309      1         1999AJ....118.1444M Morgan N.D. et al.              
1310      1      1  2000AJ....119.1083M Morgan N.D. et al.              
1311             1  2003AJ....126..696M Morgan N.D. et al.              
1312      2      2  2004AJ....127.2617M Morgan N.D. et al.              
1313      1      1  2012AJ....143..142M Morganson E. et al.             (Pan-Starrs hi-z)
1314             1  1992MNRAS.256p...1M Morganti R. et al.              
1315      1      4  1988MNRAS.230..639M Morris S.L. et al.              
1316     97    147  1991AJ....102.1627M Morris S.L. et al.              
1317      1      1  2009A&A...505...97M Mortlock D.J. et al.            
1318      1      1  2011Natur.474..616M Mortlock D. et al.              (ULAS hi-z)
1319      1      1  1978MNRAS.185..735M Morton D.C. et al.              
1320      4      1  1982MNRAS.198..669M Morton D.C. et al.              
1321      2         1970AJ.....75.1015M Moseley G.F. et al.             
1322      1      1  1991A&A...246L..24M Motch C. et al.                 
1323      9     14  1998A&AS..132..341M Motch C. et al.                 
1324      1      1  1990AJ.....99.1823M Mould J.R. et al.               
1325      4      3  ................... Mujica R. et al.                2004, private communication to VCV
1326      2      1  ................... Mujica R. et al.                2004, private communication to VCV
1327      2      2  1998ApJ...492L...9M Munoz J.A. et al.               
1328      1         2001ApJ...546..769M Munoz J.A. et al.               
1329     19     12  2003ApJ...594..684M Munoz J.A. et al.               
1330      1         1974Natur.248..491M Murdoch H.S. et al.             
1331     13     14  1984PASAu...5..341M Murdoch H.S. et al.             
1332             1  2000AJ....120.1675M Murphy T.W. et al.              
1333      1      1  2005ApJS..161....1M Murray S.S. et al.              (NDWFS X-ray)
1334      3      3  2011ApJ...743...12M Mushotzky R.F. et al.           (Kepler quasars)
1335     37     30  2008ApJ...678..635M Myers A. et al.                 
1336      2      1  1999AJ....117.2565M Myers S.T. et al.               
1337             1  2004AJ....128..109N Nagao T. et al.                 
1338      1         2000AJ....120.2859N Najita J. et al.                
1339             1  1991ApJ...373..452N Nakajima T. et al.              
1340     19      9  2009A&A...494..579N Nakos T. et al.                 
1341      3      1  2004MNRAS.347L..41N Nandra K. et al.                
1342      1      9  1996A&A...309..419N Nass P. et al.                  
1343      2      1  1992ApJS...82..447N Nelson B.O. et al.              
1344      1         2007AJ....133..965N Nesci R. et al.                 
1345      2      2  2011ApJ...733..123N Neugent K. et al.               (Wolf-Rayet QSOs)
1346      3      3  2012ApJ...759...11N Neugent K. et al.               (Wolf-Rayet QSOs)
1347   1437   1400  2013ApJS..208....5N Newman J.A. et al.              (DEEP2 Redshifts http://deep.ps.uci.edu/DR4/home.html)
1348      1         1999PASP..111.1223N Nilsson K. et al.               
1349      8      8  2004A&A...418..885N Noll S. et al.                  
1350                2002ApJ...571..218N Norman C. et al.                
1351      1      1  2008MNRAS.385...40N Norris M.A. et al.              (NGC 3923 GCs)
1352      1      1  1971AN....293..221N Notni P. et al.                 
1353      2         1975AN....296..197N Notni P. et al.                 
1354     11         1980AN....301...51N Notni P. et al.                 
1355      1         1990A&AS...82..261O O'Dea C.P. et al.               
1356             1  1991ApJ...380...66O O'Dea C.P. et al.               
1357             6  1999ApJS..125....1O Ogle P.M. et al.                
1358      6      2  2003ApJ...598..210O Ohta K. et al.                  
1359             1  1978ApJ...219L..97O Oke J.B. et al.                 
1360                1998A&A...329L..21O Oliva E. et al.                 
1361     36         1970AJ.....75..764O Olsen E.T. et al.               
1362      1         1995ApJ...445..624O Oren A.L. et al.                
1363      1      1  2006A&A...450..959O Orienti M. et al.               
1364             1  2001ApJ...558..578O Oshlack A.Y.K.N. et al.         
1365             7  1976ApJ...210..267O Osmer P.S. et al.               
1366     26     14  1977ApJ...213..607O Osmer P.S. et al.               
1367      6      1  1977ApJ...215L..47O Osmer P.S. et al.               
1368      2         1977ApJ...217L..73O Osmer P.S. et al.               
1369            12  1977ApJ...218L..89O Osmer P.S. et al.               
1370     78     82  1980ApJS...42..333O Osmer P.S. et al.               
1371            46  1980ApJS...42..523O Osmer P.S. et al.               
1372      6      5  1982ApJ...253...28O Osmer P.S. et al.               
1373    139    142  1991ApJS...75..273O Osmer P.S. et al.               
1374      1     22  1994ApJ...436..678O Osmer P.S. et al.               
1375      1      1  1998ApJS..119..189O Osmer P.S. et al.               
1376             1  1976ApJ...206..898O Osterbrock D.E. et al.          
1377             7  1977ApJ...215..733O Osterbrock D.E. et al.          
1378             1  1977PASP...89..251O Osterbrock D.E. et al.          
1379             1  1979ApJ...228L..59O Osterbrock D.E. et al.          
1380             1  1981ApJ...249..462O Osterbrock D.E. et al.          
1381             1  1982ApJS...49..149O Osterbrock D.E. et al.          
1382            15  1983ApJ...273..478O Osterbrock D.E. et al.          
1383                1984ApJ...280L..43O Osterbrock D.E. et al.          
1384             1  1985ApJ...297..166O Osterbrock D.E. et al.          
1385             4  1985PASP...97.1129O Osterbrock D.E. et al.          
1386             1  1987ApJ...323..108O Osterbrock D.E. et al.          
1387             9  1993ApJ...414..552O Osterbrock D.E. et al.          
1388      2         1976ApJ...203..307O Owen F.N. et al.                
1389      1         1977AJ.....82..677O Owen F.N. et al.                
1390      1         1977AJ.....82..776O Owen F.N. et al.                
1391             1  1978AJ.....83.1009O Owen F.N. et al.                
1392      1         1980ApJ...235L..57O Owen F.N. et al.                
1393      3         1992ApJS...80..501O Owen F.N. et al.                
1394      2         1993ApJS...87..135O Owen F.N. et al.                
1395      1      4  1995AJ....109...14O Owen F.N. et al.                
1396      1      1  1995AJ....109..486O Owen F.N. et al.                
1397      1         1977A&AS...27..171P Padrielli L. et al.             
1398      2         1981A&AS...46..473P Padrielli L. et al.             
1399             1  2000MNRAS.312..207P Page M.J. et al.                
1400     17     17  2001MNRAS.325..575P Page M.J. et al.                
1401      8      3  2007MNRAS.378.1335P Page M.J. et al.                (XMMSSC
1402      1      1  2014AJ....147..112P Paggi A. et al.                 
1403    381     89  2013A&A...551...29P Palanque-Delabrouille N. et al. (MMT-BOSS)
1404      1      1  ................... Palumbo G.G.C. et al.           1983, A catalogue of radial velocities of galaxies (Gordon and Breach NY)
1405      1      1  2009MNRAS.398.1951P Panessa F. et al.               
1406    110    110  2006AJ....132..231P Papovich C. et al.              
1407      2         2009A&A...499..395P Paraficz D. et al.              
1408      7      7  2010ARep...54..675P Parijskij Yu.N. et al.          
1409  62478    218  2012A&A...548...66P Paris I. et al.                 (SDSS DR9Q manual)
1410  58006    808  2014A&A...563...54P Paris I. et al.                 (SDSS DR10Q manual)
1411 154958 298959  ................... Paris I. et al.                 2015, paper in preparation (SDSS DR12Q manual  http://sdss.org/dr12)
1412     14     28  2014A&A...561...67P Parisi P. et al.                (Palermo Swift/BAT)
1413      1         1966Natur.210...22P Parker E. et al.                
1414      1         1973MNRAS.162..117P Parkes A.G. et al.              
1415             1  ................... Pasanen N. et al.               2003, ASP Conf. Ser. 299, 309
1416      2      2  1998A&A...336..902P Pasquini L. et al.              
1417             1  1992MNRAS.259p...1P Patnaik A.R. et al.             
1418      2      2  2003A&A...412..349P Patris J. et al.                
1419   4254      5  2003A&A...412...45P Paturel G. et al.               (Principal Galaxy Catalogue)
1420      1         1973A&A....27..475P Pauliny-Toth I.I.K. et al.      
1421      3         1981MNRAS.194..601P Peacock J.A. et al.             
1422             1  1988ApJ...328..114P Pearson T.J. et al.             
1423      1         2000ApJ...534..104P Peck A.B. et al.                
1424             1  1990A&A...232..331P Pecontal E. et al.              
1425      1      1  1983ApJ...270L..43P Pedersen H. et al.              
1426      1      1  2002AJ....123.1971P Pedreros M.H. et al.            (Q0459-6427 Field)
1427             2  2004A&A...415..487P Peng B. et al.                  
1428      6      6  2004ApJS..150..367P Peng E.W. et al.                (NGC 5128 GCs)
1429      1         1971ApJ...170..395P Penston M.V. et al.             
1430                1977MNRAS.180...19P Penston M.V. et al.             
1431      1      1  2002A&A...396..109P Pentericci L. et al.            
1432      1         1989A&A...215..262P Perez E. et al.                 
1433             1  1989MNRAS.239...55P Perez E. et al.                 
1434                1990A&A...227..407P Perez E. et al.                 
1435     33     17  1996ApJS..104..251P Perlman E.S. et al.             
1436     50     63  1998AJ....115.1253P Perlman E.S. et al.             
1437     22     38  2001AJ....121.1799P Peroux C. et al.                
1438      1      2  1985MNRAS.216..641P Perryman  .A.C. et al.          
1439      1         1979MNRAS.187..223P Perryman M.A.C. et al.          
1440             1  ................... Persic M. et al.                1986 in: "Structure of Active Galactic Nuclei"
1441             1  1995AJ....110.1554P Pesce J.E. et al.               
1442     22         1983ApJS...51..171P Pesch P. et al.                 
1443     14         1986ApJS...60..543P Pesch P. et al.                 
1444     25         1988ApJS...66..297P Pesch P. et al.                 
1445     16         1989ApJS...70..163P Pesch P. et al.                 
1446     22         1991ApJS...76.1043P Pesch P. et al.                 (Case low-dispersion survey 1983-1995)
1447     10         1995ApJS...98...41P Pesch P. et al.                 
1448             2  1972ApJ...173L..19P Peterson B.A. et al.            
1449     14         1972ApL....10..105P Peterson B.A. et al.            
1450     30         1973ApL....13..187P Peterson B.A. et al.            
1451     31         1973ApL....15..109P Peterson B.A. et al.            
1452      1      8  1976ApJ...207L...5P Peterson B.A. et al.            
1453      6         1976ApL....17..137P Peterson B.A. et al.            
1454      1      1  1978PASP...90..386P Peterson B.M. et al.            
1455            10  1979ApJ...232..400P Peterson B.A. et al.            
1456      1         1986Ap&SS.124..407P Petrov G.T. et al.              
1457             1  2003ApJ...594..695P Pettini M. et al.               
1458      1      1  1997ApJ...489..543P Phillips A.C. et al.            
1459                1983ApJ...266..485P Phillips M.M. et al.            
1460      2      2  2005AJ....130...95P Piatek S. et al.                
1461      1         2006A&A...453..839P Piconcelli E. et al.            
1462      1      1  2001A&A...372L..45P Pierre M. et al.                
1463      2         1994A&A...284..386P Pietsch W. et al.               
1464      5     17  1998A&A...333...48P Pietsch W. et al.               
1465     49     51  2007A&A...470..787P Piranomonte S. et al.           
1466    134     28  2008AJ....135.2453P Plotkin R.M. et al.             
1467     12      3  2010AJ....139..390P Plotkin R.M. et al.             (SDSS-DR7 Bl Lac candidates)
1468      1      4  1984MNRAS.210..373P Pocock A.S. et al.              
1469             1  ................... Pogrebenko S. et al.            1994 Proc. 2nd EVN/JIVE Symp. 1, 33
1470             1  1995ApJS...98....1P Poladitis A.G. et al.           
1471      9      2  2007ApJ...663...81P Poletta M. et al.               
1472      5      4  2006ApJ...642..673P Polletta M. et al.              
1473      2      2  2008A&A...492...81P Polletta M. et al.              
1474      8      8  2008ApJ...675..960P Polletta M. et al.              (Obscuration)
1475      3         1997ApJ...486..179P Polomski E. et al.              
1476      1      1  2013MNRAS.428..226P Polsterer K. et al.             
1477      4      4  1996A&AS..116...43P Popescu C.C. et al.             
1478      1         1974MNRAS.167p..41P Porcas R.W. et al.              
1479     14         1980MNRAS.191..607P Porcas R.W. et al.              
1480      2      2  2003MNRAS.343.1348P Pozzi F. et al.                 
1481      1      2  2001A&A...369..787P Prandoni I. et al.              
1482      4      4  1984ApJ...281..570P Pravdo S.H. et al.              
1483     69     68  2006ApJ...644..100P Prescott M.K.M. et al.          
1484      5         1983MNRAS.204..355P Prestage R.M. et al.            
1485                1986A&A...168..253P Prieto A. et al.                
1486      5      2  1991ApJ...374..440P Primini F.A. et al.             
1487      1         2002AJ....123.2206P Prochaska J.X. et al.           
1488      3      2  2003ApJS..148..317P Prochaska J.X. et al.           
1489      2      1  2008ApJ...675.1002P Prochaska J.X. et al.           
1490     54     47  2013ApJ...776..136P Prochaska J.X. et al.           (QPQ6)
1491             1  1995A&AS..114..565P Proust D. et al.                
1492     14     10  1992MNRAS.256..589P Puchnarewicz E.M. et al.        
1493             9  1998MNRAS.293..243P Puchnarewicz E.M. et al.        
1494      1      1  1995AJ....109.1555P Punsly B. et al.                
1495                2008ApJ...687..162P Punsly B. et al.                
1496     61     61  2013ApJ...767...14P Pursimo T. et al.               (MASIV)
1497      6      1  1999A&AS..137..299P Pustilnik S.A. et al.           
1498      5      1  2005A&A...442..109P Pustilnik S.A. et al.           
1499      1         1995Ap&SS.229..317G Gu et al.                       
1500      5         1998A&AS..129..445R Rabbette M. et al.              
1501                1990AJ.....99...53R Rafanelli P. et al.             
1502             3  1991AN....312..167R Rafanelli P. et al.             
1503      8      8  2013MNRAS.432..866R Rao S.M. et al.                 (HST-COS)
1504             1  1998MNRAS.300..417R Ratcliffe A. et al.             
1505      5      5  2007A&A...465.1099R Ravikumar C.D. et al.           
1506      1      1  2001MNRAS.322..523R Rawlings S. et al.              
1507      1      1  1998A&A...336..855R Read A.M. et al.                erratum A&A 339, 310
1508      1         1998A&A...335..121R Read M.A. et al.                
1509      2      2  1987A&A...177..337R Reboul H. et al.                
1510             1  1999ApJ...516..145R Rector T.A. et al.              
1511      2     26  2000AJ....120.1626R Rector T.A. et al.              
1512             5  2001AJ....122..565R Rector T.A. et al.              
1513      1         2003AJ....126...47R Rector T.A. et al.              
1514      2      1  2006ApJ...653.1004R Reddy Y.N.A. et al.             
1515                1994A&A...281..348R Rego M. et al.                  
1516      4      5  1982ApJ...260..437R Reichert G.A. et al.            
1517      2      2  1995A&A...293L..21R Reimers D. et al.               
1518    109    147  1996A&AS..115..235R Reimers D. et al.               
1519             1  1997A&A...327..890R Reimers D. et al.               
1520      3      1  1998A&A...334...96R Reimers D. et al.               
1521             1  1998A&A...329L..25R Reimers D. et al.               
1522      1         2002A&A...382L..26R Reimers D. et al.               
1523             1  2005A&A...435...17R Reimers D. et al.               
1524             5  1986ApJ...301..742R Remillard R.A. et al.           
1525     10      9  1993AJ....105.2079R Remillard R.A. et al.           
1526      1         1993A&A...278L..19R Remy M. et al.                  
1527      5      2  2004ApJ...606..741R Rengstorf A.W. et al.           
1528             1  2003MNRAS.343..192R Reunamem J. et al.              
1529             1  2002MNRAS.331..154R Reunanen J. et al.              
1530                2006A&A...448L..49R Revnitsev M. et al.             
1531     19      3  2008AJ....136.2373R Reyes R. et al.                 
1532             1  1997MNRAS.291..403R Reynolds C.S. et al.            
1533                1996ApJ...463L...5R Riberio A.L.B. et al.           
1534      4     10  2001AJ....121.2308R Richards G.T. et al.            
1535      4      2  2001ApJS..133...53R Richards G.T. et al.            
1536      1         2002ApJ...567L..13R Richards G.T. et al.            
1537      3      3  2006AJ....131...49R Richards G.T. et al.            (ARC HST hi-z)
1538   1878  14205  2009ApJS..180...67R Richards G.T. et al.            (NBCKDE)
1539      1      2  1980PASP...92..573R Richer H.B. et al.              
1540     12         1968MiTau..38....1R Richter L. et al.               
1541      3         1965MiTau..24....5R Richter N. et al.               
1542      1         1978Natur.271...35R Ricker G.R. et al.              
1543      2         1979ApJ...232L.151R Rieke G.H. et al.               
1544      1         1975MmRAS..80..105R Riley J.M. et al.               
1545      2         1975MNRAS.170...53R Riley J.M. et al.               
1546      2         1980MNRAS.192..233R Riley J.M. et al.               
1547             1  1989MNRAS.236p..13R Riley J.M. et al.               
1548      1         2007ApJ...670...15R Rix S.A. et al.                 
1549             1  1978ApJ...224..344R Roberts D.H. et al.             
1550      3         1986MNRAS.219..403R Robertson J.G. et al.           
1551      1      1  2002MNRAS.330..307R Roche N.D. et al.               
1552             1  1978ApJ...225..768R Rodgers A.W. et al.             
1553             1  1996ApJ...463..522R Rodriguez-Ardila A. et al.      
1554             2  1998ApJ...494..202R Rodriguez-Ardila A. et al.      
1555             9  2000ApJS..126...63R Rodriguez-Ardila A. et al.      
1556     26     26  2006ApJS..163..160R Rogel A.B. et al.               
1557      1      1  2004ApJ...610L...9R Romani R.W. et al.              
1558      3         1999A&AS..135..477R Romero G.E. et al.              
1559    170    168  2012ApJS..199....3R Ross N.P. et al.                (MMT-BOSS pilot)
1560      1      3  1999A&A...350..379R Rossa J. et al.                 
1561             1  1996MNRAS.282.1033R Rottgering H.J.A. et al.        
1562      3      4  1997A&A...326..505R Rottgering H.J.A. et al.        
1563      1         1991Natur.351..719R Rowan-Robinson M. et al.        
1564      2      1  2000MNRAS.316..885R Rowan-Robinson M. et al.        
1565      6      6  2004MNRAS.351.1290R Rowan-Robinson M. et al.        
1566    116     80  2013MNRAS.428.1958R Rowan-Robinson M. et al.        (SWIRE)
1567                1997MNRAS.289..824R Roy A.L. et al.                 
1568     12     12  2008AJ....135.2163R Rubin K.H.R. et al.             
1569      5         1967AJ.....72...59R Rubin V.C. et al.               
1570                1974ApJ...191..645R Rubin V.C. et al.               
1571             1  1987ApJ...316L..67R Rubin V.C. et al.               
1572     13         1977A&AS...28..211D de Ruiter H.R. et al.           
1573      1         1996IAUS..175..271R Ruscica C. et al.               
1574      2         1964ApJ...139..419R Ryle M. et al.                  
1575             1  1989ApJ...347L...5S Sabbadin F. et al.              
1576     12      4  2001ApJ...548..585S Sabbey C.N. et al.              
1577                2002MNRAS.329..227S Sadler E.M. et al.              
1578      1      1  2008MNRAS.385.1656S Sadler E.M. et al.              
1579      1      1  1987MNRAS.229..495S Saikia D.J. et al.              
1580      1      1  1993AJ....105.1658S Saikia D.J. et al.              (1222+216)
1581             1  1989ApJS...70..447S Salzer J.J. et al.              
1582                2001AJ....121...66S Salzer J.J. et al.              
1583      4         2005AJ....130.2584S Salzer J.J. et al.              
1584      3      5  2009MNRAS.395.1087S Sameshima H. et al.             
1585      1         2002AstL...28..174S Samus N.N. et al.               (GCVS)
1586      1         ................... Sandage A. et al.               1961 'The Hubble atlas of galaxies' Carnegie IoW publ. 1, 618
1587      5         1965ApJ...141..328S Sandage A. et al.               
1588     11         1965ApJ...142.1307S Sandage A. et al.               
1589      1         1966ApJ...144.1234S Sandage A. et al.               
1590      1      2  1967ApJ...148..767S Sandage A. et al.               
1591      1         1978AJ.....83..904S Sandage A. et al.               
1592     36         ................... Sandage A. et al.               1994 'The Carnegie atlas of galaxies' Carnegie IoW publ. 1, 638
1593      2         2003AJ....126.1607S Sanders D.B. et al.             
1594      1         1982ApJ...258L..11S Sanduleak N. et al.             
1595     37         1984ApJS...55..517S Sanduleak N. et al.             
1596     39         1989ApJS...70..173S Sanduleak N. et al.             
1597      2         1989PASP..101.1081S Sanduleak N. et al.             
1598      2         1990ApJS...72..291S Sanduleak N. et al.             
1599      2      2  1999ApJS..121..417S Sarajadini V.L. et al.          
1600      6      4  2006ApJS..166...69S Sarajedini V.L. et al.          
1601                1970ApJ...160..405S Sargent W.L.W. et al.           
1602             1  1977ApJ...212L.105S Sargent W.L.W. et al.           
1603             1  1986Natur.322...40S Sargent W.L.W. et al.           
1604             6  1987ApJ...322..142S Sargent W.L.W. et al.           
1605      6      5  1988ApJS...68..539S Sargent W.L.W. et al.           
1606      1      8  1989ApJS...69..703S Sargent W.L.W. et al.           
1607      2      3  2005AJ....130..896S Saripalli L. et al.             
1608                2007ApJ...663L...9S Satyopal S. et al.              
1609     38         1976AuJPA..39...39S Savage A. et al.                
1610      6         1976MNRAS.174..259S Savage A. et al.                
1611      5         1976MNRAS.175..517S Savage A. et al.                
1612             9  1976MNRAS.177..77PS Savage A. et al.                
1613     10         1977MNRAS.179..135S Savage A. et al.                
1614     21     15  1978MNRAS.183..473S Savage A. et al.                
1615      8         1979AuJPA..46...19S Savage A. et al.                
1616    161    125  1979MNRAS.188..599S Savage A. et al.                
1617      8      5  1981MNRAS.196..927S Savage A. et al.                
1618      5      1  1982AuJPh..35..207S Savage A. et al.                
1619      2      1  1982MNRAS.200.1135S Savage A. et al.                
1620      3      1  1984MNRAS.206..745S Savage A. et al.                
1621    233    195  1984MNRAS.207..393S Savage A. et al.                
1622     12     51  1985MNRAS.213..485S Savage A. et al.                
1623             2  1990AuJPh..43..241S Savage A. et al.                
1624                2005A&A...444L..37S Sazonov S. et al.               
1625             9  2005AJ....129..559S Sbarufatti B. et al.            
1626             7  2006A&A...457...35S Sbarufatti B. et al.            
1627      1     16  2006AJ....132....1S Sbarufatti B. et al.            
1628      4     13  2009AJ....137..337S Sbarufatti B. et al.            
1629     12     12  2013MNRAS.428.2207S Scaringi S. et al.              (Kepler blue H excess)
1630             1  1996A&AS..116..295S Scarpa R. et al.                
1631            11  1997A&A...325..109S Scarpa R. et al.                
1632      1      1  1999ApJ...521..134S Scarpa R. et al.                
1633             6  1993ApJ...412..541S Schachter J.F. et al.           
1634      4      4  1991AJ....102..869S Schade D. et al.                
1635      6      3  1996MNRAS.278...95S Schade D. et al.                
1636      6         1966ApJ...143..274S Scheuer P. et al.               
1637      1         1975MmRAS..79...75S Schilizzi R.T. et al.           
1638             2  1999ApJ...512..125S Schmidt G.D. et al.             
1639      1         2002ApJ...578L..99S Schmidt G.D. et al.             
1640      1      1  2007ApJ...666..784S Schmidt G.D. et al.             
1641             2  1966ApJ...144..443S Schmidt M. et al.               
1642             5  1974ApJ...193..505S Schmidt M. et al.               
1643     15     10  1974ApJ...193..509S Schmidt M. et al.               
1644             9  1977ApJ...217..358S Schmidt M. et al.               
1645     43         1983ApJ...269..352S Schmidt M. et al.               
1646     13      3  1986ApJ...306..411S Schmidt M. et al.               
1647     10      2  1986ApJ...310..518S Schmidt M. et al.               
1648             2  1987ApJ...316L...1S Schmidt M. et al.               
1649      1         1987ApJ...321L...7S Schmidt M. et al.               
1650      1      2  1998A&A...329..495S Schmidt M. et al.               
1651      2         1994PASP..106..843S Schmidtke P.C. et al.           
1652      1         1968Natur.218..663S Schmitt J.L. et al.             
1653      1      6  ................... Schmitz M. et al.               2014 NED (NED http://ned.ipac.caltech.edu)
1654      6         1989AJ.....98.1507S Schneider D.P. et al.           
1655      1         1989AJ.....98.1951S Schneider D.P. et al.           
1656      5      5  1991AJ....101.2004S Schneider D.P. et al.           
1657      1      1  1991AJ....102..837S Schneider D.P. et al.           
1658      1         1992AJ....103.1047S Schneider D.P. et al.           
1659     58         1992PASP..104..678S Schneider D.P. et al.           
1660      1         1994AJ....107..880S Schneider D.P. et al.           
1661    270     78  1994AJ....107.1245S Schneider D.P. et al.           
1662      4      3  1997AJ....114...36S Schneider D.P. et al.           
1663      1      1  1998AJ....115.1230S Schneider D.P. et al.           
1664     37     23  1999AJ....117...40S Schneider D.P. et al.           
1665      2         2000AJ....120.2183S Schneider D.P. et al.           
1666      4      4  2001AJ....121.1232S Schneider D.P. et al.           
1667  39247      9  2005AJ....130..367S Schneider D.P. et al.           (SDSS DR3Q manual)
1668  28259     73  2007AJ....134..102S Schneider D.P. et al.           (SDSS DR5Q manual)
1669  26301  80222  2010AJ....139.2360S Schneider D.P. et al.           (SDSS DR7Q manual)
1670             1  1998A&A...336..455S Schoenmakers A.P. et al.        
1671                2000MNRAS.315..395S Schoenmakers A.P. et al.        
1672      1         2001A&A...374..861S Schoenmakers A.P. et al.        
1673      3      5  2008A&A...478..311S Schramm M. et al.               
1674      2      6  2001ApJ...560..127S Schreier E.J. et al.            
1675      1         1979ApJ...229L..53S Schwartz D.A. et al.            
1676      1         2004ApJ...605L.105S Schwartz D.A. et al.            
1677     75    133  2000AN....321....1S Schwope A. et al.               
1678      1         1995ASPC...84..522S Sealey K.M. et al.              
1679             1  1998ApJ...499L.135S Sealey K.M. et al.              
1680      1         1968ApJ...154L.101S Searle L. et al.                
1681             1  1992MNRAS.255..581S Sekiguchi K. et al.             
1682             1  1993MNRAS.263..349S Sekiguchi K. et al.             
1683                2008ApJ...678..116S Seth A. et al.                  
1684      1      1  2006A&A...451..859S Severgnini P. et al.            
1685      3         1978AJ.....83..209S Shaffer D.B. et al.             
1686      1         1983Natur.303..156S Shanks T. et al.                
1687     20     22  1991Natur.353..315S Shanks T. et al.                
1688      3      3  2001MNRAS.326L..45S Sharp R.G. et al.               
1689     22     13  2002MNRAS.337.1153S Sharp R.G. et al.               
1690             2  1983ApJ...268L..57S Shaver P.A. et al.              
1691             1  1985MNRAS.212p..15S Shaver P.A. et al.              
1692      1         1996MNRAS.278L..11S Shaver P.A. et al.              
1693             4  1995MNRAS.275..703S Shaw M. et al.                  
1694     10     10  2009ApJ...704..477S Shaw M.S. et al.                
1695      7     23  2013ApJ...764..135S Shaw M.S. et al.                (Gamma-ray Bl Lacs)
1696      1         2007AJ....133.2222S Shen Y. et al.                  
1697      2      1  1989PASP..101..351S Shields J.C. et al.             
1698                1996A&A...311..393S Shields J.C. et al.             
1699      1         1968ApL.....1..167S Shimmins A.J. et al.            
1700     11         1971ApL.....8..139S Shimmins A.J. et al.            
1701             1  1972AuJPA..23....1S Shimmins A.J. et al.            
1702     33         1975AuJPA..34...63S Shimmins A.J. et al.            
1703                1981ApJ...250...55S Shuder J.M. et al.              
1704             1  1999A&A...348..678S Siebert J. et al.               
1705             1  1998A&A...335..443S Silverman J.D. et al.           
1706      1      1  2002ApJ...569L...1S Silverman J.D. et al.           
1707     77     71  2005ApJ...618..123S Silverman J.D. et al.           
1708     15     15  2010ApJS..191..124S Silverman J.D. et al.           (ECDF South)
1709             3  1997ApJ...489..615S Simcoe R. et al.                
1710                1980ApJ...237..404S Simkin S.M. et al.              
1711                1996MNRAS.281..509S Simpson C. et al.               
1712      1      1  1999MNRAS.303L..23S Simpson C. et al.               
1713      9      4  2006MNRAS.372..741S Simpson C. et al.               
1714      1         ................... Singal A.K. et al.              1979, Mem. R. Astron. Soc. India 1, 14
1715      1         2003A&A...406L..43S Sluse D. et al.                 
1716             1  2007A&A...468..885S Sluse D. et al.                 
1717      2         1998PASA...15..267S Smail I. et al.                 
1718     17      7  2008MNRAS.389..407S Smail I. et al.                 
1719      6      2  1997ApJS..111....1S Small T.A. et al.               
1720             1  ................... Smette A. et al.                1991, private communication to HB
1721      1      1  1976ApJ...206..345S Smith H.E. et al.               
1722             1  1976PASP...88..621S Smith H.E. et al.               
1723      4     15  1977ApJ...215..427S Smith H.E. et al.               
1724      1         1989ApJ...347...87S Smith H.E. et al.               
1725      2         1994AJ....107...24S Smith J.D. et al.               
1726      4         1994AJ....108.1147S Smith J.D. et al.               
1727             2  2002MNRAS.335..773S Smith J.E. et al.               
1728             2  2004MNRAS.350..140S Smith J.E. et al.               
1729      1         1975ApJ...202..591S Smith M.G. et al.               
1730      9         1976ApJ...206L.125S Smith M.G. et al.               
1731                1976ApJS...32..217S Smith M.G. et al.               
1732             4  1980MNRAS.191..871S Smith M.G. et al.               
1733      3         1981MNRAS.195..437S Smith M.G. et al.               
1734     29         1991ApJS...77...67S Smith P.S. et al.               
1735      1         2000ApJ...545L..19S Smith P.S. et al.               
1736     24     13  2002ApJ...569...23S Smith P.S. et al.               
1737     12      8  2003ApJ...593..676S Smith P.S. et al.               
1738      2      1  2007ApJ...663..118S Smith P.S. et al.               
1739                1985MNRAS.212..809S Smith R.M. et al.               
1740      1         1986ApJ...308...36S Smith R.M. et al.               
1741     12     12  1999MNRAS.307..149S Snellen I.A.C. et al.           
1742      2         2001MNRAS.325.1167S Snellen I.A.G. et al.           
1743      1         2002MNRAS.329..700S Snellen I.A.G. et al.           
1744      3         2002MNRAS.337..981S Snellen I.A.G. et al.           
1745                1994ApJ...433L..69S Soifer B.T. et al.              
1746             1  2007IBVS.5775....1S Southworth J. et al.            
1747     20     23  2003ApJ...590..109S Sowards-Emmerd D. et al.        
1748     22     20  2004ApJ...609..564S Sowards-Emmerd D. et al.        
1749    131    118  2005ApJ...626...95S Sowards-Emmerd D. et al.        
1750             1  1989MNRAS.240..657S Spencer R.E. et al.             
1751                1976ApJ...206L..79S Spinrad H. et al.               
1752             1  1976PASP...88..565S Spinrad H. et al.               
1753      2         1979ApJS...41..701S Spinrad H. et al.               
1754      1      3  1985PASP...97..932S Spinrad H. et al.               
1755                1995AJ....109..558S Sprayberry D. et al.            
1756     87     18  1978ApJ...221..468S Sramek R.A. et al.              
1757            32  1980ApJ...238..435S Sramek R.A. et al.              
1758    223     98  2010MNRAS.401..294S Stalin C.S. et al.              (XMM-LSS sources)
1759      8      2  2011MNRAS.413.1013S Stalin C.S. et al.              
1760             1  1977MNRAS.179..719S Stannard D. et al.              
1761             1  1982ApJ...262...66S Stauffer J.R. et al.            
1762    102     88  2004AJ....128.1483S Steffen A.T. et al.             
1763             1  1990ApJS...72....1S Steidel C.C. et al.             
1764             1  1991AJ....102.1610S Steidel C.C. et al.             
1765            20  1991ApJ...382..433S Steidel C.C. et al.             
1766      1         1995AJ....110.2519S Steidel C.C. et al.             
1767      3      3  2003ApJ...592..728S Steidel C.C. et al.             
1768                1982ApJ...259..482S Steiner J.E. et al.             
1769     19         1988Afz....29..247S Stepanian J.A. et al.           
1770      1         1990Ap.....32..252S Stepanian J.A. et al.           
1771             1  1990Ap.....33..344S Stepanian J.A. et al.           
1772             1  1990Ap.....33..501S Stepanian J.A. et al.           
1773     17         1991Ap.....34....1S Stepanian J.A. et al.           
1774     16      1  1991Ap.....34..163S Stepanian J.A. et al.           
1775      2      1  1993BSAO...35...15S Stepanian J.A. et al.           
1776      1      1  1993BSAO...35...24S Stepanian J.A. et al.           
1777     34      5  1993BSAO...36....5S Stepanian J.A. et al.           
1778     15      2  1999PASP..111.1099S Stepanian J.A. et al.           
1779     42      4  2001AJ....122.3361S Stepanian J.A. et al.           
1780             1  2002AJ....124.1283S Stepanian J.A. et al.           
1781      7      1  2003ApJ...588..746S Stepanian J.A. et al.           
1782      1     22  1989AJ.....97...10S Stephens S.A. et al.            
1783      9         1992ApJS...82..471S Stephenson C.B. et al.          
1784      2      1  1999AJ....117.1122S Stern D. et al.                 
1785      3      2  2000AJ....119.1526S Stern D. et al.                 
1786      1      1  2000ApJ...533L..75S Stern D. et al.                 
1787      2      2  2002AJ....123.2223S Stern D. et al.                 
1788                2002ApJ...568...71S Stern D. et al.                 
1789      1         2007ApJ...663..677S Stern D. et al.                 
1790      1      1  2010ApJS..188..280S Stern D. et al.                 
1791      3      3  2012ApJ...753...30S Stern D. et al.                 (WISE-selected)
1792      1         2004ApJ...604L..17S Stevens J.A. et al.             
1793      3      3  2005MNRAS.360..610S Stevens J.A. et al.             
1794      5      1  2002AJ....124.3465S Stevenson S.L. et al.           
1795            11  1989A&AS...80..103S Stickel M. et al.               
1796             1  1992A&A...264...68S Stickel M. et al.               
1797            19  1993A&AS...97..483S Stickel M. et al.               
1798             8  1993A&AS...98..393S Stickel M. et al.               
1799      1      7  1993A&AS..100..395S Stickel M. et al.               
1800      4      8  1993A&AS..101..521S Stickel M. et al.               
1801      5     13  1994A&AS..103..349S Stickel M. et al.               
1802             7  1994A&AS..105...67S Stickel M. et al.               
1803             3  1994A&AS..105..211S Stickel M. et al.               
1804                1996A&A...306...49S Stickel M. et al.               
1805             4  1996A&AS..115....1S Stickel M. et al.               
1806      7      2  1996A&AS..115...11S Stickel M. et al.               
1807             4  1990A&AS...85.1049S Stirpe G.M. et al.              
1808             1  1997MNRAS.287..848S Stobie R.S. et al.              
1809      1      2  1978ApJ...219..367S Stocke J.T. et al.              
1810     19     11  1983ApJ...273..458S Stocke J.T. et al.              
1811      1         1984ApJ...277...43S Stocke J.T. et al.              
1812      2      2  1984ApJ...280..476S Stocke J.T. et al.              
1813      7      1  1987ApJ...315L..11S Stocke J.T. et al.              
1814      3    158  1991ApJS...76..813S Stocke J.T. et al.              
1815             1  1992ApJ...400L..17S Stocke J.T. et al.              
1816             2  1997ApJ...489L..17S Stocke J.T. et al.              
1817      1         1969ApJ...155L.141S Stockton A.N. et al.            
1818             1  1972Natur.238...37S Stockton A.N. et al.            
1819             2  1990MNRAS.245..749S Storchi-Bergmann T. et al.      
1820      7     12  1996ApJ...468..121S Storrie-Lombardi L.J. et al.    
1821      6     14  2000ApJ...543..552S Storrie-Lombardi L.J. et al.    
1822     34      8  2001MNRAS.322..933S Storrie-Lombardi L.J. et al.    
1823      1      1  2003AJ....126.1720S Strateva I.V. et al.            
1824             1  1988ApJ...332L..45S Strauss M.A. et al.             
1825      1         1973ApJ...183..767S Strittmatter P.A. et al.        
1826             1  1974ApJ...190..509S Strittmatter P.A. et al.        
1827                2006ApJ...642...81S Sturm E. et al.                 
1828      9      7  2000MNRAS.312..442S Sullivan M. et al.              
1829      5      2  1982A&A...114..182S Surdej J. et al.                
1830      3         ................... Surdej J. et al.                1983, Proc. 24th Liege Int. AP Colloq. 1, 355
1831      2         1986A&A...161..209S Surdej J. et al.                
1832             1  1997A&A...327L...1S Surdej J. et al.                
1833      8      8  2004ApJ...617...64S Swinbank A.M. et al.            
1834     33     20  2004ApJS..155..271S Szokoly G.P. et al.             
1835            15  1993MNRAS.263..999T Tadhunter C.N. et al.           
1836             4  1998MNRAS.298.1035T Tadhunter C.N. et al.           
1837                1985AnTok..20..335T Takas  B. et al.                
1838      2         1984AnTok..19..595T Takase B. et al.                
1839      3         1985AnTok..20..237T Takase B. et al.                
1840      2         1986AnTok..21..127T Takase B. et al.                
1841      3         1986AnTok..21..181T Takase B. et al.                
1842             1  1987AnTok..21..251T Takase B. et al.                
1843      1         1988AnTok..22...41T Takase B. et al.                
1844      1         1989PNAOJ...1...11T Takase B. et al.                
1845      1         1989PNAOJ...1...97T Takase B. et al.                
1846      1         1993PNAOJ...3...21T Takase B. et al.                
1847      1      1  1994PASJ...46..343T Takata T. et al.                
1848      6      6  2006ApJ...651..713T Takata T. et al.                
1849      2         1977ApJ...215L..71T Tapia S. et al.                 
1850      1      1  2000ApJ...537L..17T Taylor G.B. et al.              
1851      1         2003ApJS..146..209T Teplitz H.I. et al.             
1852             2  1991A&AS...91..285T Terlevich R. et al.             
1853      3      3  2000MNRAS.313..377T Tesch F. et al.                 
1854      1         1994A&A...285..785T Thimm G.J. et al.               
1855      6      3  1998A&A...335..467T Thomas H.-C. et al.             
1856             1  1989PASP..101.1065T Thompson D.J. et al.            
1857      1      4  1990PASP..102..959T Thompson D.J. et al.            
1858      2      5  1990PASP..102.1235T Thompson D.J. et al.            
1859      1      3  1992ApJS...81....1T Thompson D.J. et al.            
1860      2      2  1996AJ....110..982T Thompson D.J. et al.            
1861      2         1995MNRAS.277..609T Tinney C.G. et al.              
1862     24     27  1997MNRAS.285..111T Tinney C.G. et al.              
1863     30     30  1999MNRAS.303..565T Tinney C.G. et al.              
1864     33     35  2011AJ....142..165T Titov O. et al.                 (ICRF South)
1865      3      3  2013AJ....146...10T Titov O. et al.                 
1866      1      1  1999AJ....117.2034T Tonry J.L. et al.               
1867             1  1992AJ....104.2072T Tran H.D. et al.                
1868             2  1995ApJ...440..578T Tran H.D. et al.                
1869             2  1998ApJ...500..660T Tran H.D. et al.                
1870             1  1999ApJ...516...85T Tran H.D. et al.                
1871      1      9  2001ApJ...554L..19T Tran H.D. et al.                
1872      1         2004ApJ...603...36T Treister E. et al.              
1873     37     37  2005ApJ...621..104T Treister E. et al.              
1874     57     64  2009ApJ...693.1713T Treister E. et al.              
1875      1      4  1994ApJ...433..494T Trevese D. et al.               
1876      3     10  2007A&A...469.1211T Trevese D. et al.               
1877      4      3  2008A&A...477..473T Trevese D. et al.               
1878     10      1  1982MNRAS.200..785T Trew A.S. et al.                
1879             1  1998MNRAS.300..303T Treyer M.A. et al.              
1880     97     97  2012ApJS..200...17T Trichas M. et al.               (ChaMP AGN)
1881                2008AJ....135.2048T Trippe M.L. et al.              
1882    125    113  2008ApJS..179....1T Trouille L. et al.              
1883      3      2  2009ApJ...703.2160T Trouille L. et al.              
1884     11         2006ApJS..165....1T Trump J.R. et al.               
1885     77     66  2007ApJS..172..383T Trump J.R. et al.               
1886    180    161  2009ApJ...696.1195T Trump J.R. et al.               
1887      1         1995ApJS..101..287T Tsvetanov Z.I. et al.           
1888      1         1995ApJ...444..532T Tucker W.H. et al.              
1889      1      1  1989MNRAS.240..833T Turner T.J. et al.              
1890      1         1999ApJ...510..178T Turner T.J. et al.              
1891             1  1984ApJ...277...51T Turnshek D.A. et al.            
1892                1985AJ.....90.1676T Tytler D. et al.                
1893             1  1987ApJS...64..667T Tytler D. et al.                
1894      5     69  1992ApJS...79....1T Tytler D. et al.                
1895             6  1993AJ....106..426T Tytler D. et al.                
1896      1      4  2004AJ....128.1058T Tytler D. et al.                
1897      2      1  1999A&AS..135..511U Ugryumov A.V. et al.            
1898      5      2  2001A&A...374..907U Ugryumov A.V. et al.            
1899      1         2003A&A...397..463U Ugryumov A.V. et al.            (HSS-LM)
1900      1         1983ApJ...270L...1U Ulmer M.P. et al.               
1901      1         1973ApL....14...89U Ulrich M.-H. et al.             
1902             1  1978ApJ...222L...3U Ulrich M.-H. et al.             
1903             3  1989A&A...220...71U Ulrich M.-H. et al.             
1904     31     27  2009ApJ...698.1095U Urrutia T. et al.               
1905     14         1978ApJ...222...40U Usher P.D. et al.               
1906      9         1978ApJ...223....1U Usher P.D. et al.               
1907     36         1981ApJS...46..117U Usher P.D. et al.               
1908     47         1982ApJS...48...51U Usher P.D. et al.               
1909     18         1982ApJS...49...27U Usher P.D. et al.               
1910             1  1983ApJ...269...73U Usher P.D. et al.               
1911      5         1988ApJS...66....1U Usher P.D. et al.               
1912             2  2000AJ....120.1683U Usher P.D. et al.               
1913      1         1987AJ.....94..847V Vader J.P. et al.               
1914      1         1987Natur.327..304V Vader J.P. et al.               
1915                1993AJ....106.1743V Vader J.P. et al.               
1916      1         1977A&AS...28..333V Valentijn E.A. et al.           
1917      1      1  2002A&A...392..795V Valtchanov I. et al.            
1918      2      4  1991A&AS...91...61v van den Broek A.C. et al.       
1919      1      1  1999A&A...342..665v van den Werf P.P. et al.        
1920     10      4  2000AJ....119.2571V Vanden Berk D.E. et al.         
1921             1  1991A&A...251...43V Vanderriest C. et al.           
1922      2      4  2008MNRAS.387..505V Vardoulaki E. et al.            
1923      5      5  2010MNRAS.401.1709V Vardoulaki E. et al.            
1924             6  1982ApJ...261...18V Vaucher B.G. et al.             
1925      4      2  2001MNRAS.327..673V Vaughan S. et al.               
1926                1987ApJS...63..295V Veilleux S. et al.              
1927                1995ApJS...98..171V Veilleux S. et al.              
1928             2  1997ApJ...484...92V Veilleux S. et al.              
1929                1999ApJ...522..113V Veilleux S. et al.              
1930             1  1999ApJ...522..139V Veilleux S. et al.              
1931      1      1  2007A&A...461..823V Venemans B.P. et al.            
1932      1         2007MNRAS.376L..76V Venemans B.P. et al.            
1933      3      3  2013ApJ...779...24V Venemans B.P. et al.            (VIKING hi-z)
1934      6      6  1999ApJ...525..995V Vennes S. et al.                
1935      2      2  2012MNRAS.426.1235V Verbeek K. et al.               (UVEX survey)
1936      1      1  2003ARep...47..119V Verkhodanov O.V. et al.         (IRAS-Texas)
1937     20     25  1995AJ....109.1983V Vermeulen R.C. et al.           
1938             1  1995ApJ...452L...5V Vermeulen R.C. et al.           
1939      8     13  1996AJ....111.1013V Vermeulen R.C. et al.           
1940                2001A&A...380..409V Vernet J. et al.                
1941      9         1971A&A....11....1V Veron M.-P. et al.              
1942      3         1976A&A....47..401V Veron M.-P. et al.              
1943      1         1977A&AS...29..149V Veron M.-P. et al.              
1944                1981A&A....98...34V Veron M.-P. et al.              
1945                1981A&A...100...12V Veron M.-P. et al.              
1946      1      1  ................... Veron M.-P. et al.              1984 unpublished
1947      1         1966ApJ...144..861V Veron P. et al.                 
1948                1981A&A....97...71V Veron P. et al.                 
1949      3     15  1990A&AS...86..543V Veron P. et al.                 
1950             1  1994A&A...283..802V Veron P. et al.                 
1951     89     92  1995A&A...296..665V Veron P. et al.                 
1952      1         1996A&A...310..381V Veron P. et al.                 
1953             6  1997A&A...319...52V Veron P. et al.                 
1954      6      4  ................... Veron P. et al.                 1999 unpublished
1955      1      4  1986A&AS...65..241V Veron-Cetty M.-P. et al.        
1956             2  1986A&AS...66..335V Veron-Cetty M.-P. et al.        
1957             5  1988A&AS...76..489V Veron-Cetty M.-P. et al.        
1958             3  1993A&AS..100..521V Veron-Cetty M.-P. et al.        
1959                2000A&A...362..426V Veron-Cetty M.-P. et al.        
1960     29     13  2004A&A...414..487V Veron-Cetty M.-P. et al.        
1961                ................... Veron-Cetty M.-P. et al.        2005 unpublished
1962      1      1  1998A&AS..130..323V Vettolani G. et al.             
1963     13      1  1990A&AS...83..205V Vigotti M. et al.               
1964     54     33  1997A&AS..123..219V Vigotti M. et al.               
1965             1  1998A&A...332..479V Villar-Martin M. et al.         
1966      1         1998A&AS..130..305V Villata M. et al.               
1967     14     15  2012MNRAS.426..360V Villforth C. et al.             (GOODS-SOUTH)
1968                1993A&AS...98..193V Vogel S. et al.                 
1969      3      3  1999A&A...342..101V Vogler A. et al.                
1970      2      2  2006A&A...448..823V Voss H. et al.                  
1971      1         1979AJ.....84..470V Vrba F.J. et al.                
1972      1      1  1994ApJ...424...68V Vrba F.J. et al.                
1973      1      1  2000MNRAS.317..801W Waddington I. et al.            
1974      1      1  1987ApJ...315L..23W Wakamatsu K. et al.             
1975      2         1971AuJPA..20....1W Wall J.V. et al.                
1976      6         1973AuJPA..31....1W Wall J.V. et al.                
1977      1      1  2002ApJ...569...36W Wallace P.M. et al.             
1978      1      5  1979MNRAS.189..667W Walsh D. et al.                 
1979      2         1979Natur.279..381W Walsh D. et al.                 
1980             6  1982MNRAS.200..191W Walsh D. et al.                 
1981             9  1984MNRAS.211..105W Walsh D. et al.                 
1982             1  2008AJ....136.1677W Walsh J.L. et al.               
1983      2         1980A&A....86....1W Walter H.G. et al.              
1984      1         1982A&A...111..357W Walter H.G. et al.              
1985      1         1973Natur.246..203W Wampler E.J. et al.             
1986             1  1984ApJ...276..403W Wampler E.J. et al.             
1987             1  1985ApJ...298..448W Wampler E.J. et al.             
1988                1985A&AS...62..255W Wamsteker W. et al.             
1989             1  2003ApJ...590L..87W Wang J. et al.                  
1990      1      1  1991ApJ...374..475W Wang Q. et al.                  
1991      2      2  2008ApJ...687..848W Wang R. et al.                  (MAMBO hi-z)
1992             1  1977A&A....59L..19W Ward M.J. et al.                
1993      4      1  1975PASP...87..103W Warner J.W. et al.              
1994      1         1987Natur.325..131W Warren S.J. et al.              
1995      2         1987Natur.330..453W Warren S.J. et al.              
1996    106    115  1991ApJS...76...23W Warren S.J. et al.              
1997      1      1  1994ApJ...421..412W Warren S.J. et al.              
1998      5      5  ................... Warren S.J. et al.              2015 in preparation
1999      2         1983ApJ...272...68W Wasilewski A.J. et al.          
2000      2      1  2002PASJ...54..683W Watanabe S. et al.              
2001             1  2004A&A...418..459W Watson D. et al.                
2002                1969Ap......5...51W Weedman D.W. et al.             
2003      1         1971ApL.....9...49W Weedman D.W. et al.             
2004    181     63  1985ApJS...57..523W Weedman D.W. et al.             
2005      2      2  2006ApJ...653..101W Weedman D. et al.               (SWIRE hiz)
2006            15  ................... Weedman D.W. et al.             2014 private communication
2007             1  1987AJ.....94.1271W Wegner G. et al.                
2008             1  1988AJ.....96.1933W Wegner G. et al.                
2009             1  1990AJ.....99..330W Wegner G. et al.                
2010             8  1990AJ....100.1274W Wegner G. et al.                
2011             3  1993AJ....105..660W Wegner G. et al.                
2012      3         2003AJ....125.2373W Wegner G. et al.                
2013      8      2  1995AcApS..15..390W Wei J.-Y. et al.                
2014     25     24  1997ChA&A..21..146W Wei J.-Y. et al.                
2015      5      2  1998A&A...329..511W Wei J.-Y. et al.                
2016     43     62  1999A&AS..139..575W Wei J.Y. et al.                 
2017      1      1  2006ApJ...637..682W Weisskopf M.C. et al.           
2018      3         1973A&A....23..215W Weistrop D. et al.              
2019                1991AJ....102.1680W Weistrop D. et al.              
2020                1976A&A....46..327W West R.M. et al.                
2021                1966AuJPh..19..181W Westerlund B.E. et al.          
2022     11      5  2006AJ....131.1948W Whalen D.J. et al.              
2023     14     10  1980MNRAS.192..545W White G.L. et al.               
2024      2      2  1987MNRAS.227..607W White G.L. et al.               
2025      5         1987MNRAS.227..705W White G.L. et al.               
2026     11     26  1988ApJ...327..561W White G.L. et al.               
2027      2         1991MNRAS.248..398W White G.L. et al.               
2028      1      1  1981ApJ...245L...1W White R.A. et al.               
2029      4      4  1993ApJ...407..456W White R.L. et al.               
2030    148     79  2000ApJS..126..133W White R.L. et al.               
2031     32     16  2003AJ....126..706W White R.L. et al.               
2032      4      2  ................... White S.V. et al.               2014, ArXiv 1410, 3892 (VIDEO radio-quiet QSOs)
2033             1  1985MNRAS.216..817W Whittle M. et al.               
2034                1992ApJS...79...49W Whittle M. et al.               
2035             8  1983PASAu...5....2W Wilkes B.J. et al.              
2036      1      1  1984MNRAS.207...73W Wilkes B.J. et al.              
2037            24  1986MNRAS.218..331W Wilkes B.J. et al.              
2038      9      8  1994ApJS...92...53W Wilkes B.J. et al.              
2039      1     18  1999ApJ...513...76W Wilkes B.J. et al.              
2040      3      3  2007AJ....133.1490W Williams K.A. et al.            
2041      7         2002AJ....124.3042W Williams R.J. et al.            
2042     12     12  1996ApJS..104..145W Williger G.M. et al.            
2043      1      1  2002ApJ...578..708W Williger G.M. et al.            
2044      4         1977A&AS...29..103W Willis A.G. et al.              
2045      1         1979A&AS...37..397W Willis A.G. et al.              
2046     18     19  1998MNRAS.300..625W Willott C.J. et al.             
2047      1      1  2003MNRAS.339..397W Willott C.J. et al.             
2048      6      6  2004ApJ...610..140W Willott C.J. et al.             
2049      4      4  2007AJ....134.2435W Willott C.J. et al.             
2050      6      6  2009AJ....137.3541W Willott C.J. et al.             
2051      9      9  2010AJ....139..906W Willott C.J. et al.             
2052      1      1  2010AJ....140..546W Willott C.J. et al.             (hiz6)
2053     10      1  1973AJ.....78..521W Wills B.J. et al.               
2054     19         1976AJ.....81.1031W Wills B.J. et al.               
2055     20     12  1979ApJS...41..689W Wills B.J. et al.               
2056      1      1  1980ApJ...237..319W Wills B.J. et al.               
2057      1      3  1986ApJ...302...56W Wills B.J. et al.               
2058      3         1966Obs....86..245W Wills D. et al.                 
2059      4         1967MNRAS.135..339W Wills D. et al.                 
2060      3         1968ApL.....2..247W Wills D. et al.                 
2061     38         1969AuJPh..22..775W Wills D. et al.                 
2062     16      3  1974ApJ...190..271W Wills D. et al.                 
2063     15     20  1976ApJS...31..143W Wills D. et al.                 
2064      1     14  1978ApJS...36..317W Wills D. et al.                 
2065     24     32  ................... Wills D. et al.                 1985 private communication to HB
2066      2         1972MNRAS.156....7W Willson M.A.G. et al.           
2067                1998MNRAS.300L...7W Wilman R.J. et al.              
2068      1         1981AJ.....86.1289W Wilson A.S. et al.              
2069             2  1990ApJS...74..731W Wilson A.S. et al.              
2070      9         1984A&AS...58...39W Windhorst R.A. et al.           
2071                1991ApJ...380..362W Windhorst R.A. et al.           
2072      2      1  1995Natur.375..471W Windhorst R.A. et al.           
2073      1         1969MNRAS.146..265W Windram M. et al.               
2074                1988MNRAS.234..703W Winkler H. et al.               
2075             3  1992A&AS...94..103W Winkler H. et al.               
2076            18  1992MNRAS.257..677W Winkler H. et al.               
2077             2  1997MNRAS.292..273W Winkler H. et al.               
2078      1      1  1997ApJ...486L.137W Winkler P.F. et al.             
2079      1      1  2005ApJ...624..189W Winkler P.F. et al.             
2080      1      1  2000AJ....120.2868W Winn J.N. et al.                
2081      1      1  2002AJ....123...10W Winn J.N. et al.                
2082      1         1993A&A...278L..15W Wisotzki L. et al.              
2083      1      1  1996A&A...315L.405W Wisotzki L. et al.              
2084             1  1997A&A...320..395W Wisotzki L. et al.              
2085      1      1  1999A&A...348L..41W Wisotzki L. et al.              
2086    163    200  2000A&A...358...77W Wisotzki L. et al.              
2087      1      1  2002A&A...395...17W Wisotzki L. et al.              
2088      1      1  2004A&A...419L..31W Wisotzki L. et al.              
2089      1         1971A&A....11..142W Wlerick G. et al.               
2090      5      2  2000MNRAS.316..267W Wold M. et al.                  
2091     21      9  1999A&A...343..399W Wolf C. et al.                  
2092      6      2  1986ApJS...61..249W Wolfe A.M. et al.               
2093      5      3  1983MNRAS.205...67W Wolstencroft R.D. et al.        
2094      2      3  2000MNRAS.311..541W Wolstencroft R.D. et al.        
2095      5      1  1997MNRAS.284..225W Wolter A. et al.                
2096     13     10  1998MNRAS.299.1047W Wolter A. et al.                
2097      1      1  2005A&A...444..165W Wolter A. et al.                
2098      1         1990AJ....100.1785W Womble D.S. et al.              
2099      1         1992ApJ...388...55W Womble D.S. et al.              
2100             1  2008PASP..120..266W Wong D.S. et al.                
2101      7     11  2008AJ....135.1849W Woo J.-H. et al.                
2102             1  1999ApJ...516..163W Worrall D.M. et al.             
2103      1         2006A&A...450..495W Worseck G. et al.               
2104      4      4  2007A&A...473..805W Worseck G. et al.               
2105     79     77  2008A&A...487..539W Worseck G. et al.               
2106             1  1998A&A...338....8W Woudt P.A. et al.               
2107                ................... Wray J.D. et al.                1988 The color atlas of galaxies - Cambridge University Press
2108             7  1977ApJ...211L.115W Wright A.E. et al.              
2109      1         1977AuJPA..41....1W Wright A.E. et al.              
2110            15  1979ApJ...229...73W Wright A.E. et al.              
2111            12  1983MNRAS.205..793W Wright A.E. et al.              
2112             6  ................... Wright A.E. et al.              1990 PKSCAT90 - The southern radiosource database, Cat. VIII/15/
2113             1  1995AcASn..36..428W Wu H. et al.                    
2114                1998A&AS..127..521W Wu H. et al.                    
2115      1      1  2001A&A...379..860W Wu J.-H. et al.                 
2116      3      3  2003ChJAA...3..423W Wu J.-H. et al.                 
2117      5      3  1999A&A...347...63W Wu X.-B. et al.                 
2118      4         1999ChA&A..23....1W Wu X.-B. et al.                 
2119      8      8  2010RAA....10..745W Wu X.-B. et al.                 (LAMOST commissioning)
2120             1  2011AJ....142...78W Wu X-.B. et al.                 
2121      5      4  2012RAA....12.1185W Wu X.-B. et al.                 (YFOSC hi-z)
2122     22     11  2013AJ....146..100W Wu X.-B. et al.                 (BFOSC bright QSOs)
2123      1      1  2009ApJ...706..885W Wuyts S. et al.                 
2124      3         1965AJ.....70..384W Wyndham J. et al.               
2125     24         1966ApJ...144..459W Wyndham J. et al.               
2126                1999ApJ...524..746X Xia X.-Y. et al.                
2127      2      3  1996AcApS..16..327X Xie G.-Z. et al.                
2128      1      1  1997AcApS..17..437X Xie G.-Z. et al.                
2129      3         1999A&AS..134..365X Xu D.W. et al.                  
2130      7      8  1999ApJ...517..622X Xu D.W. et al.                  
2131     16     11  2001ChJAA...1...46X Xu D.W. et al.                  
2132             6  1994AJ....108..395X Xu W. et al.                    
2133             1  2001A&A...367...51Y Yamada T. et al.                
2134      1      2  2004AJ....127.1274Y Yan L. et al.                   
2135     16     11  2011ApJ...728...38Y Yan R. et al.                   (AEGIS)
2136                1986Afz....25..425Y Yegiazarian A.A. et al.         
2137      1      1  ................... Yi W.-M. et al.                 2014, ArXiv 1410, 2689 (radio-loud hi-z)
2138             4  1996MNRAS.281.1206Y Young S. et al.                 
2139      3         2008ApJ...685..801Y Yuan W. et al.                  
2140      2         2003AJ....126.2125Z Zakamska N.L. et al.            
2141     29      6  1999A&A...346..731Z Zamorani G. et al.              
2142             1  1992AJ....104.1000Z Zamorano J. et al.              
2143      2         1994ApJS...95..387Z Zamorano J. et al.              
2144      1      1  2011ApJ...736...57Z Zeimann G.R. et al.             
2145      1      2  2002AJ....124..662Z Zensus J.A. et al.              
2146     25     12  1987ChA&A..11..191Z Zhan Y. et al.                  
2147     16     11  1987ChA&A..11..299Z Zhan Y. et al.                  
2148     23         1989AcApS...9...37Z Zhan Y. et al.                  
2149            17  1989ChA&A..13..139Z Zhan Y. et al.                  
2150     23     11  1989ChA&A..13..321Z Zhan Y. et al.                  
2151      4         1989PASP..101..631Z Zhan Y. et al.                  
2152      5         2004AJ....127.2579Z Zhang H. et al.                 
2153      3      3  1998AcApS..18..453Z Zhang X.-Z. et al.              
2154      2         2007RMxAA..43..101Z Zhang X.-G. et al.              
2155      1         1994AcApS..14..385Z Zhao Y.-H. et al.               
2156      3      3  2000AcApS..20..109Z Zhao Y.-H. et al.               
2157      4      4  2000AJ....120.1607Z Zheng W. et al.                 
2158      1      1  2004ApJS..155...73Z Zheng W. et al.                 (CDFS X-ray)
2159      1      3  2002AJ....124...18Z Zheng X.Z. et al.               
2160      2      1  1999A&A...349..735Z Zheng Z. et al.                 
2161      1      1  2002ApJ...581...96Z Zhou H.-Y. et al.               
2162     40         2006ApJS..166..128Z Zhou H. et al.                  
2163             1  2007ApJ...658L..13Z Zhou H. et al.                  
2164      1         1997A&A...323L..21Z Zickgraf F.-J. et al.           
2165      2      1  1997A&AS..123..103Z Zickgraf F.-J. et al.           
2166      1      1  ................... Zinnecker H. et al.             1994, in ESO/OHP workshop on dwarf galaxies ESO Garching 1, 231
2167     34     44  1992MNRAS.256..349Z Zitelli V. et al.               
2168             1  1979ApJ...229L...5Z Zotov N. et al.                 
2169             1  1995A&A...304..369Z Zou Z.-L. et al.                
2170      1      1  2009A&A...502..787Z Zurita Heras J.A. et al.        
2171      1         1970PASP...82...93Z Zwicky F. et al.
"""


# +
# function: milliquas_q3c_orm_cli()
# -
# noinspection PyBroadException
def milliquas_q3c_orm_cli(_args: Any = None):

    # check input(s)
    if _args is None:
        raise Exception('Invalid arguments')

    # if --catalog is present, download the catalog
    if _args.catalog:
        if _args.verbose:
            print(f"Downloading catalog from {ARXIV_DAT_URL} to {ARXIV_DAT_FIL}")
        get_data(_url=ARXIV_DAT_URL, _file=ARXIV_DAT_FIL)
        return

    # if --paper is present, download the science paper
    if _args.paper:
        if _args.verbose:
            print(f"Downloading science paper from {ARXIV_PDF_URL} to {ARXIV_PDF_FIL}")
        get_data(_url=ARXIV_PDF_URL, _file=ARXIV_PDF_FIL)
        return

    # if --refs is present, describe of the catalog
    if _args.refs:
        return print(__refs__)

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
    if _args.mid:
        request_args['mid'] = f'{_args.mid}'
    if _args.name:
        request_args['name'] = f'{_args.name}'
    if _args.type:
        request_args['type'] = f'{_args.type}'
    if _args.ra__gte:
        request_args['ra__gte'] = f'{_args.ra__gte}'
    if _args.ra__lte:
        request_args['ra__lte'] = f'{_args.ra__lte}'
    if _args.dec__gte:
        request_args['dec__gte'] = f'{_args.dec__gte}'
    if _args.dec__lte:
        request_args['dec__lte'] = f'{_args.dec__lte}'
    if _args.r__gte:
        request_args['r__gte'] = f'{_args.r__gte}'
    if _args.r__lte:
        request_args['r__lte'] = f'{_args.r__lte}'
    if _args.b__gte:
        request_args['b__gte'] = f'{_args.b__gte}'
    if _args.b__lte:
        request_args['b__lte'] = f'{_args.b__lte}'
    if _args.q__gte:
        request_args['q__gte'] = f'{_args.q__gte}'
    if _args.q__lte:
        request_args['q__lte'] = f'{_args.q__lte}'
    if _args.z__gte:
        request_args['z__gte'] = f'{_args.z__gte}'
    if _args.z__lte:
        request_args['z__lte'] = f'{_args.z__lte}'
    if _args.sort_order:
        request_args['sort_order'] = f'{_args.sort_order}'
    if _args.sort_value:
        request_args['sort_value'] = f'{_args.sort_value}'

    # set up access to database
    try:
        if _args.verbose:
            print(f'connection string = postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
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
        query = session.query(MilliQuasQ3cRecord)
        if _args.verbose:
            print(f'query = {query}')
        query = milliquas_q3c_orm_filters(query, request_args)
        if _args.verbose:
            print(f'query = {query}')
    except Exception as _e2:
        raise Exception(f"failed to execute query, error='{_e2}'")

    # report output
    print(f"#{','.join(_ for _ in MILLIQUAS_HEADERS)}")
    for _e in MilliQuasQ3cRecord.serialize_list(query.all()):
        if verify_keys(_e, set(MILLIQUAS_HEADERS)):
            print(f"{','.join(str(_e[_l]) for _l in MILLIQUAS_HEADERS)}")


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description=f'Query MILLIQUAS Q3C', formatter_class=argparse.RawTextHelpFormatter)

    # database query argument(s)
    _p.add_argument(f'--astrocone', help=f'Astrocone search [name,radius (deg)]')
    _p.add_argument(f'--cone', help=f'Cone search [ra (deg),dec (deg),radius (deg)]')
    _p.add_argument(f'--ellipse', help=f'Ellipse search [ra (deg),dec (deg),major_axis,axis_ratio,pos_angle (deg)]')
    _p.add_argument(f'--mid', help=f'mid <int>')
    _p.add_argument(f'--name', help=f'name like <str>')
    _p.add_argument(f'--type', help=f'type like <str>')
    _p.add_argument(f'--ra__gte', help=f'RA (deg) >= <float>')
    _p.add_argument(f'--ra__lte', help=f'RA (deg) <= <float>')
    _p.add_argument(f'--dec__gte', help=f'Dec (deg) >= <float>')
    _p.add_argument(f'--dec__lte', help=f'Dec (deg) <= <float>')
    _p.add_argument(f'--r__gte', help=f'R magnitude >= <float>')
    _p.add_argument(f'--r__lte', help=f'R magnitude <= <float>')
    _p.add_argument(f'--b__gte', help=f'B magnitude >= <float>')
    _p.add_argument(f'--b__lte', help=f'B magnitude <= <float>')
    _p.add_argument(f'--q__gte', help=f'Quasar probability >= <int>')
    _p.add_argument(f'--q__lte', help=f'Quasar probability <= <int>')
    _p.add_argument(f'--z__gte', help=f'Redshift >= <float>')
    _p.add_argument(f'--z__lte', help=f'Redshift <= <float>')
    _p.add_argument(f'--sort_order', help=f"Sort order, one of {MILLIQUAS_SORT_ORDER}")
    _p.add_argument(f'--sort_value', help=f"Sort value, one of {MILLIQUAS_SORT_VALUE}")

    # non-database query argument(s)
    _p.add_argument(f'--catalog', default=False, action='store_true', help=f'if present, download the catalog')
    _p.add_argument(f'--paper', default=False, action='store_true', help=f'if present, download the science paper')
    _p.add_argument(f'--refs', default=False, action='store_true', help=f'if present, describe the references')
    _p.add_argument(f'--text', default=False, action='store_true', help=f'if present, describe the catalog')
    _p.add_argument(f'--verbose', default=False, action='store_true', help=f'if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        milliquas_q3c_orm_cli(_args=_a)
    except Exception as _:
        if bool(_a.verbose):
            print(f"{_}")
        print(f"Use: {__doc__}")
