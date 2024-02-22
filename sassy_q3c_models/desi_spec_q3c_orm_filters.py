#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.desi_spec_q3c_orm import *


# +
# function: desi_spec_q3c_orm_filters() alphabetically
# -
# noinspection PyBroadException
def desi_spec_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records within astrocone search (API: ?astrocone=NGC1365,5.0)
    if request_args.get('astrocone'):
        _nam, _rad = request_args['astrocone'].split(',')
        _val = get_astropy_coords(_nam.strip().upper())
        if _val is not None:
            query = query.filter(func.q3c_radial_query(DesiSpecQ3cRecord.target_ra, DesiSpecQ3cRecord.target_dec, _val[0], _val[1], _rad))

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        _ra, _dec, _rad = request_args['cone'].split(',')
        query = query.filter(func.q3c_radial_query(DesiSpecQ3cRecord.target_ra, DesiSpecQ3cRecord.target_dec, _ra, _dec, _rad))

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
        query = query.filter(
            func.q3c_ellipse_query(DesiSpecQ3cRecord.target_ra, DesiSpecQ3cRecord.target_dec, _ra, _dec, _maj, _rat, _pos))

    # return records with did = value (API: ?did=20)
    if request_args.get('did'):
        query = query.filter(DesiSpecQ3cRecord.did == int(request_args['did']))

    # return records with spectype like value (API: ?spectype=NGC1365)
    if request_args.get('spectype'):
        query = query.filter(DesiSpecQ3cRecord.spectype.ilike(f"%{request_args['spectype']}%"))

    # return records with objtype like value (API: ?objtype=NGC1365)
    if request_args.get('objtype'):
        query = query.filter(DesiSpecQ3cRecord.objtype.ilike(f"%{request_args['objtype']}%"))

    # return records with brickname like value (API: ?brickname=NGC1365)
    if request_args.get('brickname'):
        query = query.filter(DesiSpecQ3cRecord.brickname.ilike(f"%{request_args['brickname']}%"))

    # return records with an RA >= value in deg (API: ?ra__gte=12.0)
    if request_args.get('ra__gte'):
        query = query.filter(DesiSpecQ3cRecord.target_ra >= float(request_args['ra__gte']))

    # return records with an RA <= value in deg (API: ?ra__lte=12.0)
    if request_args.get('ra__lte'):
        query = query.filter(DesiSpecQ3cRecord.target_ra <= float(request_args['ra__lte']))

    # return records with an Dec >= value in deg (API: ?dec__gte=20.0)
    if request_args.get('dec__gte'):
        query = query.filter(DesiSpecQ3cRecord.target_dec >= float(request_args['dec__gte']))

    # return records with a Dec <= value in deg (API: ?dec__lte=20.0)
    if request_args.get('dec__lte'):
        query = query.filter(DesiSpecQ3cRecord.target_dec <= float(request_args['dec__lte']))

    # return records where z >= value (API: ?z__gte=1.0)
    if request_args.get('z__gte'):
        query = query.filter(DesiSpecQ3cRecord.z >= float(request_args['z__gte']))

    # return records where z <= value (API: ?z__lte=1.0)
    if request_args.get('z__lte'):
        query = query.filter(DesiSpecQ3cRecord.z <= float(request_args['z__lte']))

    # sort results
    sort_value = request_args.get('sort_value', DESI_SPEC_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', DESI_SPEC_SORT_ORDER[0]).lower()
    if sort_order in DESI_SPEC_SORT_ORDER:
        if sort_order.startswith(DESI_SPEC_SORT_ORDER[0]):
            query = query.order_by(getattr(DesiSpecQ3cRecord, sort_value).asc())
        elif sort_order.startswith(DESI_SPEC_SORT_ORDER[1]):
            query = query.order_by(getattr(DesiSpecQ3cRecord, sort_value).desc())

    # return query
    return query
