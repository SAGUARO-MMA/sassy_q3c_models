#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.glade_q3c_orm import *


# +
# function: glade_q3c_orm_filters()
# -
# noinspection PyBroadException
def glade_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records within astrocone search (API: ?astrocone=M51,5.0)
    if request_args.get('astrocone'):
        _nam, _rad = request_args['astrocone'].split(',')
        _val = get_astropy_coords(_nam.strip().upper())
        if _val is not None:
            query = query.filter(func.q3c_radial_query(GladeQ3cRecord.ra, GladeQ3cRecord.dec, _val[0], _val[1], _rad))

    # return records with b >= value (API: ?b__gte=12.5)
    if request_args.get('b__gte'):
        query = query.filter(GladeQ3cRecord.b >= float(request_args['b__gte']))

    # return records with b <= value (API: ?b__lte=12.5)
    if request_args.get('b__lte'):
        query = query.filter(GladeQ3cRecord.b <= float(request_args['b__lte']))

    # return records with b_abs >= value (API: ?b_abs__gte=12.5)
    if request_args.get('b_abs__gte'):
        query = query.filter(GladeQ3cRecord.b_abs >= float(request_args['b_abs__gte']))

    # return records with b_abs <= value (API: ?b_abs__lte=12.5)
    if request_args.get('b_abs__lte'):
        query = query.filter(GladeQ3cRecord.b_abs <= float(request_args['b_abs__lte']))

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        _ra, _dec, _rad = request_args['cone'].split(',')
        query = query.filter(func.q3c_radial_query(GladeQ3cRecord.ra, GladeQ3cRecord.dec, _ra, _dec, _rad))

    # return records with dec >= value (API: ?dec__gte=-90.0)
    if request_args.get('dec__gte'):
        query = query.filter(GladeQ3cRecord.dec >= float(request_args['dec__gte']))

    # return records with dec <= value (API: ?dec__lte=90.0)
    if request_args.get('dec__lte'):
        query = query.filter(GladeQ3cRecord.dec <= float(request_args['dec__lte']))

    # return records with dist >= value (API: ?dist__gte=0.0)
    if request_args.get('dist__gte'):
        query = query.filter(GladeQ3cRecord.dist >= float(request_args['dist__gte']))

    # return records with dist <= value (API: ?dist__lte=10.0)
    if request_args.get('dist__lte'):
        query = query.filter(GladeQ3cRecord.dist <= float(request_args['dist__lte']))

    # return records with disterr >= value (API: ?disterr__gte=0.5)
    if request_args.get('disterr__gte'):
        query = query.filter(GladeQ3cRecord.disterr >= float(request_args['disterr__gte']))

    # return records with disterr <= value (API: ?disterr__lte=0.5)
    if request_args.get('disterr__lte'):
        query = query.filter(GladeQ3cRecord.disterr <= float(request_args['disterr__lte']))

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
        query = query.filter(
            func.q3c_ellipse_query(GladeQ3cRecord.ra, GladeQ3cRecord.dec, _ra, _dec, _maj, _rat, _pos))

    # return records with flag1 like value (API: ?flag1=Q)
    if request_args.get('flag1'):
        query = query.filter(GladeQ3cRecord.flag1.ilike(f"%{request_args['flag1']}%"))

    # return records with flag2 >= value (API: ?flag2__gte=3)
    if request_args.get('flag2__gte'):
        query = query.filter(GladeQ3cRecord.flag2 >= int(request_args['flag2__gte']))

    # return records with flag2 <= value (API: ?flag2__lte=1)
    if request_args.get('flag2__lte'):
        query = query.filter(GladeQ3cRecord.flag2 <= int(request_args['flag2__lte']))

    # return records with flag3 >= value (API: ?flag3__gte=3)
    if request_args.get('flag3__gte'):
        query = query.filter(GladeQ3cRecord.flag3 >= int(request_args['flag3__gte']))

    # return records with flag3 <= value (API: ?flag3__lte=1)
    if request_args.get('flag3__lte'):
        query = query.filter(GladeQ3cRecord.flag3 <= int(request_args['flag3__lte']))

    # return records with gid = value (API: ?gid=20)
    if request_args.get('gid'):
        query = query.filter(GladeQ3cRecord.gid == int(request_args['gid']))

    # return records with gwgc name like value (API: ?gwgc=demo)
    if request_args.get('gwgc'):
        query = query.filter(GladeQ3cRecord.gwgc.ilike(f"%{request_args['gwgc']}%"))

    # return records with h >= value (API: ?h__gte=12.5)
    if request_args.get('h__gte'):
        query = query.filter(GladeQ3cRecord.h >= float(request_args['h__gte']))

    # return records with h <= value (API: ?h__lte=12.5)
    if request_args.get('h__lte'):
        query = query.filter(GladeQ3cRecord.h <= float(request_args['h__lte']))

    # return records with hyperleda name like value (API: ?hyperleda=demo)
    if request_args.get('hyperleda'):
        query = query.filter(GladeQ3cRecord.hyperleda.ilike(f"%{request_args['hyperleda']}%"))

    # return records with j >= value (API: ?j__gte=13.5)
    if request_args.get('j__gte'):
        query = query.filter(GladeQ3cRecord.j >= float(request_args['j__gte']))

    # return records with j <= value (API: ?j__lte=13.5)
    if request_args.get('j__lte'):
        query = query.filter(GladeQ3cRecord.j <= float(request_args['j__lte']))

    # return records with k >= value (API: ?k__gte=14.5)
    if request_args.get('k__gte'):
        query = query.filter(GladeQ3cRecord.k >= float(request_args['k__gte']))

    # return records with k <= value (API: ?k__lte=14.5)
    if request_args.get('k__lte'):
        query = query.filter(GladeQ3cRecord.k <= float(request_args['k__lte']))

    # return records with pgc = value (API: ?pgc=20)
    if request_args.get('pgc'):
        query = query.filter(GladeQ3cRecord.pgc == int(request_args['pgc']))

    # return records with ra >= value (API: ?ra__gte=0.0)
    if request_args.get('ra__gte'):
        query = query.filter(GladeQ3cRecord.ra >= float(request_args['ra__gte']))

    # return records with ra <= value (API: ?ra__lte=360.0)
    if request_args.get('ra__lte'):
        query = query.filter(GladeQ3cRecord.ra <= float(request_args['ra__lte']))

    # return records with sdss name like value (API: ?sdss=demo)
    if request_args.get('sdss'):
        query = query.filter(GladeQ3cRecord.sdss.ilike(f"%{request_args['sdss']}%"))

    # return records with twomass name like value (API: ?twomass=demo)
    if request_args.get('twomass'):
        query = query.filter(GladeQ3cRecord.twomass.ilike(f"%{request_args['twomass']}%"))

    # return records with z >= value (API: ?z__gte=0.5)
    if request_args.get('z__gte'):
        query = query.filter(GladeQ3cRecord.z >= float(request_args['z__gte']))

    # return records with z >= value (API: ?z__lte=3.5)
    if request_args.get('z__lte'):
        query = query.filter(GladeQ3cRecord.z <= float(request_args['z__lte']))

    # sort results
    sort_value = request_args.get('sort_value', GLADE_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', GLADE_SORT_ORDER[0]).lower()
    if sort_order in GLADE_SORT_ORDER:
        if sort_order.startswith(GLADE_SORT_ORDER[0]):
            query = query.order_by(getattr(GladeQ3cRecord, sort_value).asc())
        elif sort_order.startswith(GLADE_SORT_ORDER[1]):
            query = query.order_by(getattr(GladeQ3cRecord, sort_value).desc())

    # return query
    return query
