from Appsflyer_api.af_events_data.reques_af_api_events import pull_af_all_events_non_org
import numpy as np
import pandas as pd
from af_tokens import token_tezbol, id_andr_tezbol
from Appsflyer_api.af_events_data.ask_af_events import AF_events_data

""" Date """
from_date = '2022-12-13'
to_date = '2022-12-13'

""" Token and app ID"""
app_id = id_andr_tezbol
token = token_tezbol

df = pull_af_all_events_non_org(app_id, token, from_date, to_date)

sources = list(df['Media Source'].unique())
if 'restricted' in sources:
    ind = sources.index('restricted')
    sources[ind] = 'Facebook_Ads'
else:
    pass

if 'Facebook Ads' in sources:
    x = sources.index('Facebook Ads')
    sources[x] = 'Facebook_Ads'
else:
    pass

"""получаем уникальные значения"""


def unique(list1):
    x = np.array(list1)
    return np.unique(x)


channels = list(unique(sources))


def create_chan_dict(list_of_channels):
    for i in range(len(list_of_channels)):
        if i == 0:
            x = int(input(f'Добавьте бюджет канала {list_of_channels[i]}:'))
            y = int(input(f'Добавьте просмотры канала {list_of_channels[i]}:'))
            z = int(input(f'Добавьте клики канала {list_of_channels[i]}:'))
            dict_channels = {list_of_channels[0]: [x, y, z]}
        else:
            x = int(input(f'Добавьте бюджет канала {list_of_channels[i]}:'))
            y = int(input(f'Добавьте просмотры канала {list_of_channels[i]}:'))
            z = int(input(f'Добавьте клики канала {list_of_channels[i]}:'))
            dict_channels[list_of_channels[i]] = [x, y, z]
    return dict_channels


dict_channels = create_chan_dict(channels)

if __name__ == '__main__':
    print(channels)
