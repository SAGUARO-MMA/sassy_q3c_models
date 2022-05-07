#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.ztf_q3c_orm import *


# +
# function: ztf_q3c_orm_filters()
# -
# noinspection PyBroadException
def ztf_q3c_orm_filters(query: Any = None, request_args: dict = None):

    # return records within astrocone search (API: ?astrocone=M51,5.0)
    if request_args.get('astrocone'):
        try:
            _nam, _rad = request_args['astrocone'].split(',')
            _val = get_astropy_coords(_nam.strip().upper())
            if _val is not None:
                query = query.filter(func.q3c_radial_query(
                    ZtfQ3cRecord.ra, ZtfQ3cRecord.dec, float(_val[0]), float(_val[1]), float(_rad)))
        except:
            pass

    # return records within cone search (API: ?cone=23.5,29.2,5.0)
    if request_args.get('cone'):
        try:
            _ra, _dec, _rad = request_args['cone'].split(',')
            query = query.filter(func.q3c_radial_query(
                ZtfQ3cRecord.ra, ZtfQ3cRecord.dec, float(_ra), float(_dec), float(_rad)))
        except:
            pass

    # return records within ellipse search (API: ?ellipse=202.1,47.2,5.0,0.5,25.0)
    if request_args.get('ellipse'):
        try:
            _ra, _dec, _maj, _rat, _pos = request_args['ellipse'].split(',')
            query = query.filter(func.q3c_ellipse_query(
                ZtfQ3cRecord.ra, ZtfQ3cRecord.dec, float(_ra), float(_dec), float(_maj),
                float(_rat), float(_pos)))
        except:
            pass

    # return records with alert_candid (API: ?alert_candid=1354526412715010015)
    if request_args.get('alert_candid'):
        query = query.filter(ZtfQ3cRecord.alert_candid == request_args['alert_candid'])

    # return records with a star/galaxy score >= value (API: ?classtar__gte=0.4)
    if request_args.get('classtar__gte'):
        query = query.filter(ZtfQ3cRecord.classtar >= float(request_args['classtar__gte']))

    # return records with a star/galaxy score <= value (API: ?classtar__lte=0.4)
    if request_args.get('classtar__lte'):
        query = query.filter(ZtfQ3cRecord.classtar <= float(request_args['classtar__lte']))

    # return records with a Dec >= value in deg (API: ?dec__gte=20.0)
    if request_args.get('dec__gte'):
        query = query.filter(ZtfQ3cRecord.dec >= float(request_args['dec__gte']))

    # return records with a Dec <= value in deg (API: ?dec__lte=20.0)
    if request_args.get('dec__lte'):
        query = query.filter(ZtfQ3cRecord.dec <= float(request_args['dec__gte']))

    # return records with a magnitude difference >= abs value (API: ?deltamaglatest__gte=1.0)
    if request_args.get('deltamaglatest__gte'):
        query = query.filter(ZtfQ3cRecord.deltamaglatest >= float(request_args['deltamaglatest__gte']))

    # return records with a magnitude difference <= abs value (API: ?deltamaglatest__lte=1.0)
    if request_args.get('deltamaglatest__lte'):
        query = query.filter(ZtfQ3cRecord.deltamaglatest <= float(request_args['deltamaglatest__lte']))

    # return records with a mag diff on the reference image >= value (API: ?deltamagref__gte=1.0)
    if request_args.get('deltamagref__gte'):
        query = query.filter(ZtfQ3cRecord.deltamagref >= float(request_args['deltamagref__gte']))

    # return records with a mag diff on the reference image <= value (API: ?deltamagref__gte=1.0)
    if request_args.get('deltamagref__lte'):
        query = query.filter(ZtfQ3cRecord.deltamagref <= float(request_args['deltamagref__lte']))

    # return records where the distance to the nearest source >= value (API: ?distnr__gte=1.0)
    if request_args.get('distnr__gte'):
        query = query.filter(ZtfQ3cRecord.distnr >= float(request_args['distnr__gte']))

    # return records where the distance to the nearest source <= value (API: ?distnr__lte=1.0)
    if request_args.get('distnr__lte'):
        query = query.filter(ZtfQ3cRecord.distnr <= float(request_args['distnr__lte']))

    # return records where the deep-learning real-bogus score >= value (API: ?drb__gte=1.0)
    if request_args.get('drb__gte'):
        query = query.filter(ZtfQ3cRecord.drb >= float(request_args['drb__gte']))

    # return records where the deep-learning real-bogus score <= value (API: ?drb__lte=1.0)
    if request_args.get('drb__lte'):
        query = query.filter(ZtfQ3cRecord.drb <= float(request_args['drb__lte']))

    # return records with a given fid (API: ?fid=1)
    if request_args.get('fid'):
        query = query.filter(ZtfQ3cRecord.fid == int(request_args['fid']))

    # return records with a given filtername (API: ?filtername='g')
    if request_args.get('filtername'):
        query = query.filter(ZtfQ3cRecord.filtername.like(f"%{request_args['filtername']}%"))

    # return records with an iso time >= date (API: ?iso__gte=2018-07-17)
    if request_args.get('iso__gte'):
        a_time = Time(request_args['iso__gte'], format='isot')
        query = query.filter(ZtfQ3cRecord.jd >= a_time.jd)

    # return records with an iso time <= date (API: ?iso=2018-07-17)
    if request_args.get('iso__lte'):
        a_time = Time(request_args['iso__lte'], format='isot')
        query = query.filter(ZtfQ3cRecord.jd <= a_time.jd)

    # return records with a JD >= date (API: ?jd__gte=2458302.6906713)
    if request_args.get('jd__gte'):
        query = query.filter(ZtfQ3cRecord.jd >= request_args['jd__gte'])

    # return records with a JD <= date (API: ?jd__lte=2458302.6906713)
    if request_args.get('jd__lte'):
        query = query.filter(ZtfQ3cRecord.jd <= request_args['jd__lte'])

    # return records with a magap >= value (API: ?magap__gte=0.4)
    if request_args.get('magap__gte'):
        query = query.filter(ZtfQ3cRecord.magap >= float(request_args['magap__gte']))

    # return records with a magap <= value (API: ?magap__lte=0.4)
    if request_args.get('magap__lte'):
        query = query.filter(ZtfQ3cRecord.magap <= float(request_args['magap__lte']))

    # return records with a magpsf >= value (API: ?magpsf__gte=20.0)
    if request_args.get('magpsf__gte'):
        query = query.filter(ZtfQ3cRecord.magpsf >= float(request_args['magpsf__gte']))

    # return records with a magpsf <= value (API: ?magpsf__lte=20.0)
    if request_args.get('magpsf__lte'):
        query = query.filter(ZtfQ3cRecord.magpsf <= float(request_args['magpsf__lte']))

    # return records near a PS1 object ID (API: ?objectidps=178183210973037920)
    if request_args.get('objectidps'):
        psid = int(request_args['objectidps'])
        query = query.filter(
            (ZtfQ3cRecord.objectidps1 == psid) | (ZtfQ3cRecord.objectidps2 == psid) | (ZtfQ3cRecord.objectidps3 == psid))

    # return records with oid like value (API: ?oid=NGC1365)
    if request_args.get('oid'):
        query = query.filter(ZtfQ3cRecord.oid.ilike(f"%{request_args['oid']}%"))

    # return records with an RA >= value in deg (API: ?ra__gte=20.0)
    if request_args.get('ra__gte'):
        query = query.filter(ZtfQ3cRecord.ra >= float(request_args['ra__gte']))

    # return records with an RA <= value in deg (API: ?ra__lte=20.0)
    if request_args.get('ra__lte'):
        query = query.filter(ZtfQ3cRecord.ra <= float(request_args['ra__lte']))

    # return records with a real/bogus score >= value (API: ?rb__gte=0.3)
    if request_args.get('rb__gte'):
        query = query.filter(ZtfQ3cRecord.rb >= float(request_args['rb__gte']))

    # return records with a real/bogus score <= value (API: ?rb__lte=0.3)
    if request_args.get('rb__lte'):
        query = query.filter(ZtfQ3cRecord.rb <= float(request_args['rb__lte']))

    # return records with a sigmapsf >= value (API: ?sigmapsf__gte=0.4)
    if request_args.get('sigmapsf__gte'):
        query = query.filter(ZtfQ3cRecord.sigmapsf <= float(request_args['sigmapsf__gte']))

    # return records with a sigmapsf <= value (API: ?sigmapsf__lte=0.4)
    if request_args.get('sigmapsf__lte'):
        query = query.filter(ZtfQ3cRecord.sigmapsf <= float(request_args['sigmapsf__lte']))

    # return records with ssnamenr (API: ?ssnamenr=16495)
    if request_args.get('ssnamenr'):
        query = query.filter(ZtfQ3cRecord.ssnamenr.ilike(f"%{request_args['ssnamenr']}%"))

    # return records with zid = value (API: ?zid=20)
    if request_args.get('zid'):
        query = query.filter(ZtfQ3cRecord.zid == int(request_args['zid']))

    # sort results
    sort_by = request_args.get('sort_value', 'jd')
    sort_order = request_args.get('sort_order', 'desc')
    if sort_order == 'desc':
        query = query.order_by(getattr(ZtfQ3cRecord, sort_by).desc())
    elif sort_order == 'asc':
        query = query.order_by(getattr(ZtfQ3cRecord, sort_by).asc())

    # return query
    return query
