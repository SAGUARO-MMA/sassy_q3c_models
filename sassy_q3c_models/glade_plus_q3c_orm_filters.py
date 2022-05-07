#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.glade_plus_q3c_orm import *


# +
# function: glade_plus_q3c_orm_filters()
# -
# noinspection PyBroadException
def glade_plus_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records within astrocone search (API: ?astrocone=M51,5.0)
    if request_args.get('astrocone'):
        try:
            _nam, _rad = request_args['astrocone'].split(',')
            _val = get_astropy_coords(_nam.strip().upper())
            if _val is not None:
                query = query.filter(func.q3c_radial_query(
                    GladePlusQ3cRecord.ra, GladePlusQ3cRecord.dec, float(_val[0]), float(_val[1]), float(_rad)))
        except:
            pass

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        try:
            _ra, _dec, _rad = request_args['cone'].split(',')
            query = query.filter(func.q3c_radial_query(
                GladePlusQ3cRecord.ra, GladePlusQ3cRecord.dec, float(_ra), float(_dec), float(_rad)))
        except:
            pass

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        try:
            _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
            query = query.filter(func.q3c_ellipse_query(
                GladePlusQ3cRecord.ra, GladePlusQ3cRecord.dec, float(_ra), float(_dec), float(_maj),
                float(_rat), float(_pos)))
        except:
            pass

    # return records with gid = value (API: ?gid=20)
    if request_args.get('gid'):
        query = query.filter(GladePlusQ3cRecord.gid == int(request_args['gid']))

    # return records with gn = value (API: ?gn=20)
    if request_args.get('gn'):
        query = query.filter(GladePlusQ3cRecord.gn == int(request_args['gn']))

    # return records with name like value (API: ?name=demo)
    if request_args.get('name'):
        query = query.filter(or_(
            GladePlusQ3cRecord.gwgc.ilike(f"%{request_args['name']}%"),
            GladePlusQ3cRecord.hyperleda.ilike(f"%{request_args['name']}%"),
            GladePlusQ3cRecord.twomass.ilike(f"%{request_args['name']}%"),
            GladePlusQ3cRecord.wise.ilike(f"%{request_args['name']}%"),
            GladePlusQ3cRecord.sdss.ilike(f"%{request_args['name']}%")))

    # return records with ra >= value (API: ?ra__gte=0.0)
    if request_args.get('ra__gte'):
        query = query.filter(GladePlusQ3cRecord.ra >= float(request_args['ra__gte']))

    # return records with ra <= value (API: ?ra__lte=360.0)
    if request_args.get('ra__lte'):
        query = query.filter(GladePlusQ3cRecord.ra <= float(request_args['ra__lte']))

    # return records with dec >= value (API: ?dec__gte=-90.0)
    if request_args.get('dec__gte'):
        query = query.filter(GladePlusQ3cRecord.dec >= float(request_args['dec__gte']))

    # return records with dec <= value (API: ?dec__lte=90.0)
    if request_args.get('dec__lte'):
        query = query.filter(GladePlusQ3cRecord.dec <= float(request_args['dec__lte']))

    # return records with b >= value (API: ?b__gte=12.5)
    if request_args.get('b__gte'):
        query = query.filter(GladePlusQ3cRecord.b >= float(request_args['b__gte']))

    # return records with b <= value (API: ?b__lte=12.5)
    if request_args.get('b__lte'):
        query = query.filter(GladePlusQ3cRecord.b <= float(request_args['b__lte']))

    # return records with b_abs >= value (API: ?b_abs__gte=12.5)
    if request_args.get('b_abs__gte'):
        query = query.filter(GladePlusQ3cRecord.b_abs >= float(request_args['b_abs__gte']))

    # return records with b_abs <= value (API: ?b_abs__lte=12.5)
    if request_args.get('b_abs__lte'):
        query = query.filter(GladePlusQ3cRecord.b_abs <= float(request_args['b_abs__lte']))

    # return records with j >= value (API: ?j__gte=13.5)
    if request_args.get('j__gte'):
        query = query.filter(GladePlusQ3cRecord.j >= float(request_args['j__gte']))

    # return records with j <= value (API: ?j__lte=13.5)
    if request_args.get('j__lte'):
        query = query.filter(GladePlusQ3cRecord.j <= float(request_args['j__lte']))

    # return records with h >= value (API: ?h__gte=12.5)
    if request_args.get('h__gte'):
        query = query.filter(GladePlusQ3cRecord.h >= float(request_args['h__gte']))

    # return records with h <= value (API: ?h__lte=12.5)
    if request_args.get('h__lte'):
        query = query.filter(GladePlusQ3cRecord.h <= float(request_args['h__lte']))

    # return records with k >= value (API: ?k__gte=14.5)
    if request_args.get('k__gte'):
        query = query.filter(GladePlusQ3cRecord.k >= float(request_args['k__gte']))

    # return records with k <= value (API: ?k__lte=14.5)
    if request_args.get('k__lte'):
        query = query.filter(GladePlusQ3cRecord.k <= float(request_args['k__lte']))

    # return records with w1 >= value (API: ?w1__gte=14.5)
    if request_args.get('w1__gte'):
        query = query.filter(GladePlusQ3cRecord.w1 >= float(request_args['w1__gte']))

    # return records with w1 <= value (API: ?w1__lte=14.5)
    if request_args.get('w1__lte'):
        query = query.filter(GladePlusQ3cRecord.w1 <= float(request_args['w1__lte']))

    # return records with w2 >= value (API: ?w2__gte=24.5)
    if request_args.get('w2__gte'):
        query = query.filter(GladePlusQ3cRecord.w2 >= float(request_args['w2__gte']))

    # return records with w2 <= value (API: ?w2__lte=24.5)
    if request_args.get('w2__lte'):
        query = query.filter(GladePlusQ3cRecord.w2 <= float(request_args['w2__lte']))

    # return records with b_j >= value (API: ?b_j__gte=12.5)
    if request_args.get('b_j__gte'):
        query = query.filter(GladePlusQ3cRecord.b_j >= float(request_args['b_j__gte']))

    # return records with b_j <= value (API: ?b_j__lte=12.5)
    if request_args.get('b_j__lte'):
        query = query.filter(GladePlusQ3cRecord.b_j <= float(request_args['b_j__lte']))

    # return records with zhelio >= value (API: ?zhelio__gte=0.5)
    if request_args.get('zhelio__gte'):
        query = query.filter(GladePlusQ3cRecord.z_helio >= float(request_args['zhelio__gte']))

    # return records with zhelio >= value (API: ?zhelio__lte=3.5)
    if request_args.get('zhelio__lte'):
        query = query.filter(GladePlusQ3cRecord.z_helio <= float(request_args['zhelio__lte']))

    # return records with zcmb >= value (API: ?zcmb__gte=0.5)
    if request_args.get('zcmb__gte'):
        query = query.filter(GladePlusQ3cRecord.z_cmb >= float(request_args['zcmb__gte']))

    # return records with z >= value (API: ?z__lte=3.5)
    if request_args.get('z__lte'):
        query = query.filter(GladePlusQ3cRecord.z_cmb <= float(request_args['z__lte']))

    # return records with d_l >= value (API: ?d_l__gte=12.5)
    if request_args.get('d_l__gte'):
        query = query.filter(GladePlusQ3cRecord.d_l >= float(request_args['d_l__gte']))

    # return records with d_l <= value (API: ?d_l__lte=12.5)
    if request_args.get('d_l__lte'):
        query = query.filter(GladePlusQ3cRecord.d_l <= float(request_args['d_l__lte']))

    # sort results
    sort_value = request_args.get('sort_value', GLADE_PLUS_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', GLADE_PLUS_SORT_ORDER[0]).lower()
    if sort_order in GLADE_PLUS_SORT_ORDER:
        if sort_order.startswith(GLADE_PLUS_SORT_ORDER[0]):
            query = query.order_by(getattr(GladePlusQ3cRecord, sort_value).asc())
        elif sort_order.startswith(GLADE_PLUS_SORT_ORDER[1]):
            query = query.order_by(getattr(GladePlusQ3cRecord, sort_value).desc())

    # return query
    return query
