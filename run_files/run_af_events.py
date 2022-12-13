from af_tokens import token_tezbol, id_andr_tezbol
from Appsflyer_api.af_events_data.ask_af_events import AF_events_data

""" Date """
from_date = '2022-12-13'
to_date = '2022-12-13'


""" Token and app ID"""
app_id = id_andr_tezbol
token = token_tezbol

# app_id = id_andr_kreditomat_kz
# token = token_kreditomat_kz



if __name__ == '__main__':
    print(AF_events_data(app_id, token, to_date, from_date).get_channels())