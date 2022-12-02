from Appsflyer_api.af_aggregated.af_extra_func import retrieve_name
from af_tokens import token_tezbol, id_andr_tezbol
from Appsflyer_api.af_shorts_asks import af_aggregated_short
from Appsflyer_api.af_aggregated.af_extra_func import retrieve_name


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


# Вспомагательный для получения имен переменных
media_source = [retrieve_name(x) for x in sources]

if __name__ == '__main__':
    print(af_aggregated_short(media_source, app_id, token, from_date, to_date, sources))

