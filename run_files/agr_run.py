# import pandas as pd
# import numpy as np
from af_aggregated.af_extra_func import retrieve_name
from af_tokens import token_creditomat_md, token_tezbol, token_kreditomat_kz, id_andr_creditomat_md, id_andr_tezbol, id_andr_kreditomat_kz, id_ios_kreditomat_kz
from af_aggregated.request_af_api import get_af_agr_df


""" Date """
from_date = '2022-11-22'
to_date = '2022-11-30'


""" Token and app ID"""
app_id = id_andr_tezbol
token = token_tezbol


""" Sources - Budget, Views, Clicks"""
Organic = [0, 0, 0]
googleadwords_int = [1680, 646000, 14500]
Facebook_Ads = [100, 6000, 1000]


sources = [Organic, googleadwords_int, Facebook_Ads]


# Вспомогательный для получения имен переменных
media_source = [retrieve_name(x) for x in sources]

if __name__ == '__main__':
    print(get_af_agr_df(media_source, app_id, token, from_date, to_date))


