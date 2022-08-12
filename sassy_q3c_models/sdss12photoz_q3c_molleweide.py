#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.sdss12photoz_q3c_orm import *

import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt


# +
# initialize
# -
# noinspection PyBroadException
try:
    mpl.use('Agg')
except:
    pass


# +
# __doc__
# -
__doc__ = """ python3 sdss12photoz_q3c_molleweide.py --help """


# +
# function: sdss12photoz_q3c_molleweide()
# -
def sdss12photoz_q3c_molleweide(_verbose: bool = False):

    # get data
    try:
        engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        get_session = sessionmaker(bind=engine)
        session = get_session()
        query = session.query(Sdss12PhotozQ3cRecord)
    except Exception as _e1:
        raise Exception(f"failed to connect to database, error='{_e1}'")

    # get co-oords
    _dec, _ra = [], []
    for _e in Sdss12PhotozQ3cRecord.serialize_list(query.all()):
        if verify_keys(_e, set(SDSS12PHOTOZ_HEADERS)):
            _ra.append(_e['ra'])
            _dec.append(_e['dec'])
    if _verbose:
        print(f"_ra={_ra}, len={len(_ra)}")
        print(f"_dec={_dec}, len={len(_dec)}")
    _ra_np = np.array(_ra)
    _dec_np = np.array(_dec)

    # massage all RA data so that east is to the left
    _ra_np = np.remainder(_ra_np + 360.0 - ORIGIN, 360.0)
    _ind = _ra_np > 180.0
    _ra_np[_ind] -= 360.0
    _ra_np = -_ra_np

    # set up plot
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="mollweide", **{'facecolor': 'LightYellow'})

    # plot data
    try:
        ax.scatter(np.radians(_ra_np), np.radians(_dec_np), color='blue', s=2.5,
                   alpha=0.25, marker='D', label="SDSS12PHOTOZ")
    except Exception as _ep1:
        raise Exception(f"{_ep1}")

    # add label(s), legend, title, grid
    tick_labels = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210])
    tick_labels = np.remainder(tick_labels + 360.0 + ORIGIN, 360.0)
    tick_labels = [f"\n{int(_v):d}{DEGREE}\n\n{int(_v/15.0):d}{UPPER_H}" for _v in tick_labels]
    ax.set_xticklabels(tick_labels, **{'va': 'center', 'color': 'black'})
    ax.set_xlabel(f'Right Ascension (J2k{DEGREE})')
    ax.set_ylabel(f'Declination (J2k{DEGREE})')
    ax.grid(True)
    plt.title(f"SDSS12PHOTOZ Coverage Map")

    # output(s)
    _png = os.path.abspath(os.path.expanduser(f"sdss12photoz_q3c_molleweide.png"))
    plt.savefig(fname=f"{_png}", format='png', dpi=100, bbox_inches='tight')


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description='Plot SDSS12PHOTOZ Molleweide', formatter_class=argparse.RawTextHelpFormatter)
    _p.add_argument(f'--verbose', default=False, action='store_true', help='if present, produce more verbose output')
    _a = _p.parse_args()

    # execute
    try:
        sdss12photoz_q3c_molleweide(_verbose=bool(_a.verbose))
    except Exception as _:
        if bool(_a.verbose):
            print(f"'{_}'")
        print(f"Use: {__doc__}")
