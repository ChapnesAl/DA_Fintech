from Appsflyer_api.af_aggregated.request_af_api import pull_af_agr_df
from Appsflyer_api.af_aggregated.transform.unit import clarity_af_aggr, clear_af_aggr, af_agr_correct_placement, \
    vanity_af_aggr


def af_aggregated_short(med_sour, app_id, token, from_date, to_date, sources):
    return (af_agr_correct_placement(
        vanity_af_aggr(clarity_af_aggr(clear_af_aggr(pull_af_agr_df(med_sour, app_id, token, from_date, to_date))),
                       med_sour, sources)))
