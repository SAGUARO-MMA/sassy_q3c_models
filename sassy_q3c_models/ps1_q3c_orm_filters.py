#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.ps1_q3c_orm import *


# +
# function: ps1_q3c_orm_filters() alphabetically
# -
# noinspection PyBroadException
def ps1_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records within astrocone search (API: ?astrocone=M51,5.0)
    if request_args.get('astrocone'):
        try:
            _nam, _rad = request_args['astrocone'].split(',')
            _val = get_astropy_coords(_nam.strip().upper())
            if _val is not None:
                query = query.filter(func.q3c_radial_query(
                    Ps1Q3cRecord.ra, Ps1Q3cRecord.dec, float(_val[0]), float(_val[1]), float(_rad)))
                # query = query.filter(func.q3c_radial_query(
                #     Ps1Q3cRecord.ramean, Ps1Q3cRecord.decmean, float(_val[0]), float(_val[1]), float(_rad)))
        except:
            pass

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        try:
            _ra, _dec, _rad = request_args['cone'].split(',')
            query = query.filter(func.q3c_radial_query(
                Ps1Q3cRecord.ra, Ps1Q3cRecord.dec, float(_ra), float(_dec), float(_rad)))
            # query = query.filter(func.q3c_radial_query(
            #     Ps1Q3cRecord.ramean, Ps1Q3cRecord.decmean, float(_ra), float(_dec), float(_rad)))
        except:
            pass

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        try:
            _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
            query = query.filter(func.q3c_ellipse_query(
                Ps1Q3cRecord.ra, Ps1Q3cRecord.dec, float(_ra), float(_dec), float(_maj),
                float(_rat), float(_pos)))
            # query = query.filter(func.q3c_ellipse_query(
            #     Ps1Q3cRecord.ramean, Ps1Q3cRecord.decmean, float(_ra), float(_dec), float(_maj),
            #     float(_rat), float(_pos)))
        except:
            pass

    # return records with pid = value (API: ?pid=20)
    if request_args.get('pid'):
        query = query.filter(Ps1Q3cRecord.pid == int(request_args['pid']))

    # return records with objid equal to value (API: ?objid=1365)
    if request_args.get('objid'):
        query = query.filter(Ps1Q3cRecord.objid == request_args['objid'])

    # return records with objname equal to value (API: ?objid=NGC1365)
    if request_args.get('objname'):
        query = query.filter(Ps1Q3cRecord.objname.ilike(f"%{request_args['objname']}%"))

    # return records with psps_objid equal to value (API: ?psps_objid=NGC1365)
    if request_args.get('psps_objid'):
        query = query.filter(Ps1Q3cRecord.psps_objid == request_args['psps_objid'])

    # return records with ra >= value (API: ?ra__gte=0.3)
    if request_args.get('ra__gte'):
        query = query.filter(Ps1Q3cRecord.ra >= float(request_args['ra__gte']))

    # return records with ra <= value (API: ?ra__lte=0.3)
    if request_args.get('ra__lte'):
        query = query.filter(Ps1Q3cRecord.ra <= float(request_args['ra__lte']))

    # return records with dec >= value (API: ?dec__gte=0.3)
    if request_args.get('dec__gte'):
        query = query.filter(Ps1Q3cRecord.dec >= float(request_args['dec__gte']))

    # return records with dec <= value (API: ?dec__lte=0.3)
    if request_args.get('dec__lte'):
        query = query.filter(Ps1Q3cRecord.dec <= float(request_args['dec__lte']))

    # return records with gmag >= value (API: ?gmag__gte=0.3)
    if request_args.get('gmag__gte'):
        query = query.filter(Ps1Q3cRecord.gmeanpsfmag >= float(request_args['gmag__gte']))

    # return records with gmag <= value (API: ?gmag__lte=0.3)
    if request_args.get('gmag__lte'):
        query = query.filter(Ps1Q3cRecord.gmeanpsfmag <= float(request_args['gmag__lte']))

    # return records with rmag >= value (API: ?rmag__gte=0.3)
    if request_args.get('rmag__gte'):
        query = query.filter(Ps1Q3cRecord.rmeanpsfmag >= float(request_args['rmag__gte']))

    # return records with rmag <= value (API: ?rmag__lte=0.3)
    if request_args.get('rmag__lte'):
        query = query.filter(Ps1Q3cRecord.rmeanpsfmag <= float(request_args['rmag__lte']))

    # return records with imag >= value (API: ?imag__gte=0.3)
    if request_args.get('imag__gte'):
        query = query.filter(Ps1Q3cRecord.imeanpsfmag >= float(request_args['imag__gte']))

    # return records with imag <= value (API: ?imag__lte=0.3)
    if request_args.get('imag__lte'):
        query = query.filter(Ps1Q3cRecord.imeanpsfmag <= float(request_args['imag__lte']))

    # return records with zmag >= value (API: ?zmag__gte=0.3)
    if request_args.get('zmag__gte'):
        query = query.filter(Ps1Q3cRecord.zmeanpsfmag >= float(request_args['zmag__gte']))

    # return records with zmag <= value (API: ?zmag__lte=0.3)
    if request_args.get('zmag__lte'):
        query = query.filter(Ps1Q3cRecord.zmeanpsfmag <= float(request_args['zmag__lte']))

    # return records with ymag >= value (API: ?ymag__gte=0.3)
    if request_args.get('ymag__gte'):
        query = query.filter(Ps1Q3cRecord.ymeanpsfmag >= float(request_args['ymag__gte']))

    # return records with ymag <= value (API: ?ymag__lte=0.3)
    if request_args.get('ymag__lte'):
        query = query.filter(Ps1Q3cRecord.ymeanpsfmag <= float(request_args['ymag__lte']))

    # return records with ps_score >= value (API: ?ps_score__gte=0.3)
    if request_args.get('ps_score__gte'):
        query = query.filter(Ps1Q3cRecord.ps_score >= float(request_args['ps_score__gte']))

    # return records with ps_score <= value (API: ?ps_score__lte=0.3)
    if request_args.get('ps_score__lte'):
        query = query.filter(Ps1Q3cRecord.ps_score <= float(request_args['ps_score__lte']))

    # sort results
    sort_value = request_args.get('sort_value', PS1_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', PS1_SORT_ORDER[0]).lower()
    if sort_order in PS1_SORT_ORDER:
        if sort_order.startswith(PS1_SORT_ORDER[0]):
            query = query.order_by(getattr(Ps1Q3cRecord, sort_value).asc())
        elif sort_order.startswith(PS1_SORT_ORDER[1]):
            query = query.order_by(getattr(Ps1Q3cRecord, sort_value).desc())

    # return query
    return query
