#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.fermi_lat_q3c_orm import *
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
__doc__ = """python3 fermi_lat_q3c_hammer.py --help"""


# +
# function: fermi_lat_q3c_hammer()
# -
def fermi_lat_q3c_hammer() -> None:

    # get data
    try:
        engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        get_session = sessionmaker(bind=engine)
        session = get_session()
        query = session.query(FermiLatQ3cRecord)
    except Exception as _e1:
        raise Exception(f"failed to connect to database, error='{_e1}'")

    # get co-oords
    _l, _b = [], []
    for _e in FermiLatQ3cRecord.serialize_list(query.all()):
        _l.append(_e['l'])
        _b.append(_e['b'])
    print(f"_l={_l}, len={len(_l)}")
    print(f"_b={_b}, len={len(_b)}")
    _l_np = np.array(_l)
    _b_np = np.array(_b)

    # massage all l data so that east is to the left
    _l_np = np.remainder(_l_np + 360.0 - ORIGIN, 360.0)
    _ind = _l_np > 180.0
    _l_np[_ind] -= 360.0
    # _l_np = -_l_np

    # set up plot
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="hammer", **{'facecolor': 'LightYellow'})

    # plot data
    try:
        ax.scatter(np.radians(_l_np), np.radians(_b_np), color='blue', s=2.5,
                   alpha=0.25, marker='D', label="FERMI_LAT")
    except Exception as _ep1:
        raise Exception(f"{_ep1}")

    # add label(s), legend, title, grid
    tick_labels = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210])
    # tick_labels = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210])
    tick_labels = np.remainder(tick_labels + 360.0 + ORIGIN, 360.0)
    # tick_labels = [f"\n{int(_v):d}{DEGREE}\n\n{int(_v/15.0):d}{UPPER_H}" for _v in tick_labels]
    ax.set_xticklabels(tick_labels, **{'va': 'center', 'color': 'black'})
    ax.set_xlabel(f'Galactic Longitude (l{DEGREE})')
    ax.set_ylabel(f'Galactic Latitude (b{DEGREE})')
    ax.grid(True)
    plt.title(f"Fermi LAT Coverage Map")

    # output(s)
    _png = os.path.abspath(os.path.expanduser(f"fermi_lat_q3c_hammer.png"))
    plt.savefig(fname=f"{_png}", format='png', dpi=100, bbox_inches='tight')


# +
# main()
# -
if __name__ == '__main__':

    # noinspection PyTypeChecker
    _p = argparse.ArgumentParser(description='Plot FERMI_LAT Molleweide', formatter_class=argparse.RawTextHelpFormatter)
    _a = _p.parse_args()

    # execute
    try:
        fermi_lat_q3c_hammer()
    except Exception as _:
        print(f"{_}\nUse: {__doc__}")
