#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.sassy_cron_q3c_orm import *


# +
# function: sassy_cron_q3c_orm_filters()
# -
# noinspection PyBroadException
def sassy_cron_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records within astrocone search (API: ?astrocone=M51,5.0)
    if request_args.get('astrocone'):
        try:
            _nam, _rad = request_args['astrocone'].split(',')
            _val = get_astropy_coords(_nam.strip().upper())
            if _val is not None:
                query = query.filter(func.q3c_radial_query(
                    SassyCronQ3cRecord.zra, SassyCronQ3cRecord.zdec, float(_val[0]), float(_val[1]), float(_rad)))
        except:
            pass

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        try:
            _ra, _dec, _rad = request_args['cone'].split(',')
            query = query.filter(func.q3c_radial_query(
                SassyCronQ3cRecord.zra, SassyCronQ3cRecord.zdec, float(_ra), float(_dec), float(_rad)))
        except:
            pass

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        try:
            _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
            query = query.filter(func.q3c_ellipse_query(
                SassyCronQ3cRecord.zra, SassyCronQ3cRecord.zdec, float(_ra), float(_dec), float(_maj),
                float(_rat), float(_pos)))
        except:
            pass

    # return records with sid = value (API: ?sid=20)
    if request_args.get('sid'):
        query = query.filter(SassyCronQ3cRecord.sid == int(request_args['sid']))

    # return records with class_name like value (API: ?class_name='SN')
    if request_args.get('class_name'):
        query = query.filter(SassyCronQ3cRecord.class_name.ilike(f"%{request_args['class_name']}%"))

    # return records with zoid like value (API: ?zoid=demo)
    if request_args.get('zoid'):
        query = query.filter(SassyCronQ3cRecord.zoid.ilike(f"%{request_args['zoid']}%"))

    # return records with zfid like value (API: ?zfid=1)
    if request_args.get('zfid'):
        query = query.filter(SassyCronQ3cRecord.zfid == int(request_args['zfid']))

    # return records with gdist >= value (API: ?gdist__gte=0.0)
    if request_args.get('gdist__gte'):
        query = query.filter(SassyCronQ3cRecord.gdist >= float(request_args['gdist__gte']))

    # return records with gdist <= value (API: ?gdist__lte=360.0)
    if request_args.get('gdist__lte'):
        query = query.filter(SassyCronQ3cRecord.gdist <= float(request_args['gdist__lte']))

    # return records with gsep >= value (API: ?gsep__gte=0.0)
    if request_args.get('gsep__gte'):
        query = query.filter(SassyCronQ3cRecord.gsep >= float(request_args['gsep__gte']))

    # return records with gsep <= value (API: ?gsep__lte=360.0)
    if request_args.get('gsep__lte'):
        query = query.filter(SassyCronQ3cRecord.gsep <= float(request_args['gsep__lte']))

    # return records with gz >= value (API: ?gz__gte=0.0)
    if request_args.get('gz__gte'):
        query = query.filter(SassyCronQ3cRecord.gz >= float(request_args['gz__gte']))

    # return records with gz <= value (API: ?gz__lte=360.0)
    if request_args.get('gz__lte'):
        query = query.filter(SassyCronQ3cRecord.gz <= float(request_args['gz__lte']))

    # return records with zra >= value (API: ?zra__gte=0.0)
    if request_args.get('zra__gte'):
        query = query.filter(SassyCronQ3cRecord.zra >= float(request_args['zra__gte']))

    # return records with zra <= value (API: ?zra__lte=360.0)
    if request_args.get('zra__lte'):
        query = query.filter(SassyCronQ3cRecord.zra <= float(request_args['zra__lte']))

    # return records with zdec >= value (API: ?zdec__gte=0.0)
    if request_args.get('zdec__gte'):
        query = query.filter(SassyCronQ3cRecord.zdec >= float(request_args['zdec__gte']))

    # return records with zdec <= value (API: ?zdec__lte=360.0)
    if request_args.get('zdec__lte'):
        query = query.filter(SassyCronQ3cRecord.zdec <= float(request_args['zdec__lte']))

    # sort results
    sort_value = request_args.get('sort_value', SASSY_CRON_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', SASSY_CRON_SORT_ORDER[0]).lower()
    if sort_order in SASSY_CRON_SORT_ORDER:
        if sort_order.startswith(SASSY_CRON_SORT_ORDER[0]):
            query = query.order_by(getattr(SassyCronQ3cRecord, sort_value).asc())
        elif sort_order.startswith(SASSY_CRON_SORT_ORDER[1]):
            query = query.order_by(getattr(SassyCronQ3cRecord, sort_value).desc())

    # return query
    return query
