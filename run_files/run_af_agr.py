from Appsflyer_api.af_aggregated.af_extra_func import retrieve_name
from af_tokens import token_tezbol, id_andr_tezbol, id_andr_kreditomat_kz, id_ios_kreditomat_kz, id_andr_creditomat_md, token_kreditomat_kz, token_creditomat_md
from Appsflyer_api.af_aggregated.af_extra_func import retrieve_name
from Appsflyer_api.af_shorts_asks import af_unit_short, af_unit_short_kzt



""" Date """
from_date = '2022-10-01'
to_date = '2022-10-31'


""" Token and app ID"""
# app_id = id_andr_tezbol
# token = token_tezbol

app_id = id_andr_kreditomat_kz
token = token_kreditomat_kz


""" Sources - Budget, Views, Clicks"""
Organic = [0, 0, 0]
googleadwords_int = [7431, 2715423, 54379]
Facebook_Ads = [100, 6000, 1000]


# sources = [Organic, googleadwords_int, Facebook_Ads]
sources = [Organic, googleadwords_int]


# Вспомагательный для получения имен переменных
media_source = [retrieve_name(x) for x in sources]

if __name__ == '__main__':
    # print(af_unit_short(media_source, app_id, token, from_date, to_date, sources))
    # print(af_unit_short_kzt(media_source, app_id, token, from_date, to_date, sources))
    x = af_unit_short_kzt(media_source, app_id, token, from_date, to_date, sources)
    print(x)
    x.to_excel(r'C:\Users\PC\Desktop\DataAnalytics\Parser\result.xlsx', index=False)

