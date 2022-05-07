#!/usr/bin/env python3


# +
# import(s)
# -
from sassy_q3c_models.non_detections_orm import *


# +
# function: non_detections_orm_filters() alphabetically
# -
# noinspection PyBroadException
def non_detections_orm_filters(query: Any = None, request_args: dict = None):

    # return records with nid = value (API: ?nid=20)
    if request_args.get('nid'):
        query = query.filter(NonDetectionsRecord.nid == int(request_args['nid']))

    # return records with oid equal to value (API: ?oid=NGC1365)
    if request_args.get('oid'):
        query = query.filter(NonDetectionsRecord.oid == request_args['oid'])

    # return records with diffmaglim >= value (API: ?diffmaglim__gte=0.3)
    if request_args.get('diffmaglim__gte'):
        query = query.filter(NonDetectionsRecord.diffmaglim >= float(request_args['diffmaglim__gte']))

    # return records with diffmaglim <= value (API: ?diffmaglim__lte=0.3)
    if request_args.get('diffmaglim__lte'):
        query = query.filter(NonDetectionsRecord.diffmaglim <= float(request_args['diffmaglim__lte']))

    # return records with jd >= value (API: ?jd__gte=0.3)
    if request_args.get('jd__gte'):
        query = query.filter(NonDetectionsRecord.jd >= float(request_args['jd__gte']))

    # return records with jd <= value (API: ?jd__lte=0.3)
    if request_args.get('jd__lte'):
        query = query.filter(NonDetectionsRecord.jd <= float(request_args['jd__lte']))

    # return records with fid = value (API: ?fid=20)
    if request_args.get('fid'):
        query = query.filter(NonDetectionsRecord.fid == int(request_args['fid']))

    # sort results
    sort_value = request_args.get('sort_value', NON_DETECTIONS_SORT_VALUE[0]).lower()
    sort_order = request_args.get('sort_order', NON_DETECTIONS_SORT_ORDER[0]).lower()
    if sort_order in NON_DETECTIONS_SORT_ORDER:
        if sort_order.startswith(NON_DETECTIONS_SORT_ORDER[0]):
            query = query.order_by(getattr(NonDetectionsRecord, sort_value).asc())
        elif sort_order.startswith(NON_DETECTIONS_SORT_ORDER[1]):
            query = query.order_by(getattr(NonDetectionsRecord, sort_value).desc())

    # return query
    return query
