#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.roma_bzcat_q3c_orm import *


# +
# function: roma_bzcat_q3c_orm_filters() alphabetically
# -
# noinspection PyBroadException
def roma_bzcat_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records within astrocone search (API: ?astrocone=NGC1365,5.0)
    if request_args.get('astrocone'):
        _nam, _rad = request_args['astrocone'].split(',')
        _val = get_astropy_coords(_nam.strip().upper())
        if _val is not None:
            query = query.filter(func.q3c_radial_query(RomaBzcatQ3cRecord.ra, RomaBzcatQ3cRecord.dec, _val[0], _val[1], _rad))

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        _ra, _dec, _rad = request_args['cone'].split(',')
        query = query.filter(func.q3c_radial_query(RomaBzcatQ3cRecord.ra, RomaBzcatQ3cRecord.dec, _ra, _dec, _rad))

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
        query = query.filter(
            func.q3c_ellipse_query(RomaBzcatQ3cRecord.ra, RomaBzcatQ3cRecord.dec, _ra, _dec, _maj, _rat, _pos))

    # return records with rid = value (API: ?rid=20)
    if request_args.get('rid'):
        query = query.filter(RomaBzcatQ3cRecord.rid == int(request_args['rid']))

    # return records with an RA >= value in deg (API: ?ra__gte=12.0)
    if request_args.get('ra__gte'):
        query = query.filter(RomaBzcatQ3cRecord.ra >= float(request_args['ra__gte']))

    # return records with an RA <= value in deg (API: ?ra__lte=12.0)
    if request_args.get('ra__lte'):
        query = query.filter(RomaBzcatQ3cRecord.ra <= float(request_args['ra__lte']))

    # return records with an Dec >= value in deg (API: ?dec__gte=20.0)
    if request_args.get('dec__gte'):
        query = query.filter(RomaBzcatQ3cRecord.dec >= float(request_args['dec__gte']))

    # return records with a Dec <= value in deg (API: ?dec__lte=20.0)
    if request_args.get('dec__lte'):
        query = query.filter(RomaBzcatQ3cRecord.dec <= float(request_args['dec__lte']))

    # return records where redshift >= value (API: ?z__gte=1.0)
    if request_args.get('z__gte'):
        query = query.filter(RomaBzcatQ3cRecord.z >= float(request_args['z__gte']))

    # return records where redshift <= value (API: ?z__lte=1.0)
    if request_args.get('z__lte'):
        query = query.filter(RomaBzcatQ3cRecord.z <= float(request_args['z__lte']))

    # return records where rmag >= value (API: ?rmag__gte=1.0)
    if request_args.get('rmag__gte'):
        query = query.filter(RomaBzcatQ3cRecord.rmag >= float(request_args['rmag__gte']))

    # return records where rmag <= value (API: ?rmag__lte=1.0)
    if request_args.get('rmag__lte'):
        query = query.filter(RomaBzcatQ3cRecord.rmag <= float(request_args['rmag__lte']))

    # return records with name like value (API: ?name=NGC1365)
    if request_args.get('name'):
        query = query.filter(RomaBzcatQ3cRecord.name.ilike(f"%{request_args['name']}%"))

    # sort results
    sort_value = request_args.get('sort_value', ROMA_BZCAT_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', ROMA_BZCAT_SORT_ORDER[0]).lower()
    if sort_order in ROMA_BZCAT_SORT_ORDER:
        if sort_order.startswith(ROMA_BZCAT_SORT_ORDER[0]):
            query = query.order_by(getattr(RomaBzcatQ3cRecord, sort_value).asc())
        elif sort_order.startswith(ROMA_BZCAT_SORT_ORDER[1]):
            query = query.order_by(getattr(RomaBzcatQ3cRecord, sort_value).desc())

    # return query
    return query
