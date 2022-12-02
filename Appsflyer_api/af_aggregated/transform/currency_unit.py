from kzt_exchangerates import Rates
import pandas as pd



"""  USD to KZT converter """

def af_unit_usd_to_kzt(df):

    rates = Rates()

    KZTUSD = rates.get_exchange_rate("USD", from_kzt=True)

    # create copy of table with KZT
    df_kzt = df.copy()
    financial_metrics = ['Budget', 'CPC', 'CPI', 'CPSu', 'CPAp']
    df_kzt[financial_metrics] = df_kzt[financial_metrics] * KZTUSD

    return df_kzt