#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.gwgc_q3c_orm import *


# +
# function: gwgc_q3c_orm_filters() alphabetically
# -
# noinspection PyBroadException
def gwgc_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records with major axis >= value (API: ?a__gte=0.3)
    if request_args.get('a__gte'):
        query = query.filter(GwgcQ3cRecord.a >= float(request_args['a__gte']))

    # return records with major axis <= value (API: ?a__lte=0.3)
    if request_args.get('a__lte'):
        query = query.filter(GwgcQ3cRecord.a <= float(request_args['a__lte']))

    # return records within astrocone search (API: ?astrocone=NGC1365,5.0)
    if request_args.get('astrocone'):
        _nam, _rad = request_args['astrocone'].split(',')
        _val = get_astropy_coords(_nam.strip().upper())
        if _val is not None:
            query = query.filter(func.q3c_radial_query(GwgcQ3cRecord.ra, GwgcQ3cRecord.dec, _val[0], _val[1], _rad))

    # return records with absolute B magnitude >= value (API: ?b_abs__gte=15.0)
    if request_args.get('b_abs__gte'):
        query = query.filter(GwgcQ3cRecord.b_abs >= float(request_args['b_abs__gte']))

    # return records with absolute B magnitude <= value (API: ?b_abs__lte=15.0)
    if request_args.get('b_abs__lte'):
        query = query.filter(GwgcQ3cRecord.b_abs <= float(request_args['b_abs__lte']))

    # return records with apparent B magnitude >= value (API: ?b_app__gte=15.0)
    if request_args.get('b_app__gte'):
        query = query.filter(GwgcQ3cRecord.b_app >= float(request_args['b_app__gte']))

    # return records with apparent B magnitude <= value (API: ?b_app__lte=15.0)
    if request_args.get('b_app__lte'):
        query = query.filter(GwgcQ3cRecord.b_app <= float(request_args['b_app__lte']))

    # return records with minor axis >= value (API: ?b__gte=0.3)
    if request_args.get('b__gte'):
        query = query.filter(GwgcQ3cRecord.b >= float(request_args['b__gte']))

    # return records with minor axis <= value (API: ?b__lte=0.3)
    if request_args.get('b__lte'):
        query = query.filter(GwgcQ3cRecord.b <= float(request_args['b__lte']))

    # return records with axis ratio >= value (API: ?b_div_a__gte=0.3)
    if request_args.get('b_div_a__gte'):
        query = query.filter(GwgcQ3cRecord.b_div_a >= float(request_args['b_div_a__gte']))

    # return records with an axis ratio <= value (API: ?b_div_a__lte=0.3)
    if request_args.get('b_div_a__lte'):
        query = query.filter(GwgcQ3cRecord.b_div_a <= float(request_args['b_div_a__lte']))

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        _ra, _dec, _rad = request_args['cone'].split(',')
        query = query.filter(func.q3c_radial_query(GwgcQ3cRecord.ra, GwgcQ3cRecord.dec, _ra, _dec, _rad))

    # return records with an Dec >= value in deg (API: ?dec__gte=20.0)
    if request_args.get('dec__gte'):
        query = query.filter(GwgcQ3cRecord.dec >= float(request_args['dec__gte']))

    # return records with a Dec <= value in deg (API: ?dec__lte=20.0)
    if request_args.get('dec__lte'):
        query = query.filter(GwgcQ3cRecord.dec <= float(request_args['dec__lte']))

    # return records where the distance to the nearest source >= value (API: ?dist__gte=1.0)
    if request_args.get('dist__gte'):
        query = query.filter(GwgcQ3cRecord.dist >= float(request_args['dist__gte']))

    # return records where the distance to the nearest source <= value (API: ?dist__lte=1.0)
    if request_args.get('dist__lte'):
        query = query.filter(GwgcQ3cRecord.dist <= float(request_args['dist__lte']))

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
        query = query.filter(
            func.q3c_ellipse_query(GwgcQ3cRecord.ra, GwgcQ3cRecord.dec, _ra, _dec, _maj, _rat, _pos))

    # return records with gid = value (API: ?gid=20)
    if request_args.get('gid'):
        query = query.filter(GwgcQ3cRecord.gid == int(request_args['gid']))

    # return records with name like value (API: ?name=NGC1365)
    if request_args.get('name'):
        query = query.filter(GwgcQ3cRecord.name.ilike(f"%{request_args['name']}%"))

    # return records with a position angle >= value (API: ?pa__gte=1.0)
    if request_args.get('pa__gte'):
        query = query.filter(GwgcQ3cRecord.pa >= float(request_args['pa__gte']))

    # return records with a position angle <= value (API: ?pa__lte=1.0)
    if request_args.get('pa__lte'):
        query = query.filter(GwgcQ3cRecord.pa <= float(request_args['pa__lte']))

    # return records with pgc = value (API: ?pgc=20)
    if request_args.get('pgc'):
        query = query.filter(GwgcQ3cRecord.pgc == int(request_args['pgc']))

    # return records with an RA >= value in deg (API: ?ra__gte=12.0)
    if request_args.get('ra__gte'):
        query = query.filter(GwgcQ3cRecord.ra >= float(request_args['ra__gte']))

    # return records with an RA <= value in deg (API: ?ra__lte=12.0)
    if request_args.get('ra__lte'):
        query = query.filter(GwgcQ3cRecord.ra <= float(request_args['ra__lte']))

    # return records with morphological type >= value (API: ?tt__gte=1.0)
    if request_args.get('tt__gte'):
        query = query.filter(GwgcQ3cRecord.tt >= float(request_args['tt__gte']))

    # return records with morphological type <= value (API: ?tt__lte=1.0)
    if request_args.get('tt__lte'):
        query = query.filter(GwgcQ3cRecord.tt <= float(request_args['tt__lte']))

    # sort results
    sort_value = request_args.get('sort_value', GWGC_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', GWGC_SORT_ORDER[0]).lower()
    if sort_order in GWGC_SORT_ORDER:
        if sort_order.startswith(GWGC_SORT_ORDER[0]):
            query = query.order_by(getattr(GwgcQ3cRecord, sort_value).asc())
        elif sort_order.startswith(GWGC_SORT_ORDER[1]):
            query = query.order_by(getattr(GwgcQ3cRecord, sort_value).desc())

    # return query
    return query
