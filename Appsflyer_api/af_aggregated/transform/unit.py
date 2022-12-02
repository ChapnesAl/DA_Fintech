from Appsflyer_api.af_aggregated.request_af_api import pull_af_agr_df
import pandas as pd
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def trunc(values, decs=0):
    return np.trunc(values * 10 ** decs) / (10 ** decs)


def clear_af_aggr(df):
    # Replace spaces on
    df['Media Source (pid)'] = df['Media Source (pid)'].str.replace(' ', '_')

    # Group sources in one type source
    dfx = df.groupby('Media Source (pid)').sum(numeric_only=True)

    df = dfx.copy()

    df = df.drop([
        'Impressions',
        'CTR',
        'Conversion Rate',
        'Total Revenue',
        'Total Cost',
        'af_login (Unique users)',
        'loan_accepted (Unique users)',
        'install_kreditomat (Event counter)',
        'ROI',
        'ARPU',
        'Loyal Users',
        'Loyal Users/Installs',
        'loan_rejected (Unique users)',
        'Average eCPI',
        'install_kreditomat (Unique users)',
        'af_complete_registration (Unique users)',
        'submit_loan_application (Unique users)',
        'af_complete_registration (Sales in USD)',
        'af_login (Sales in USD)',
        'install_kreditomat (Sales in USD)',
        'loan_accepted (Sales in USD)',
        'loan_rejected (Sales in USD)',
        'submit_loan_application (Sales in USD)'], axis=1)

    # transposition columns without BUDGET
    df = df[['Sessions', 'Installs', 'af_login (Event counter)', 'submit_loan_application (Event counter)',
             'loan_rejected (Event counter)', 'loan_accepted (Event counter)']]
    return df


def clarity_af_aggr(df):
    # transposition columns without BUDGET
    df = df[['Sessions', 'Installs', 'af_login (Event counter)', 'submit_loan_application (Event counter)',
             'loan_rejected (Event counter)', 'loan_accepted (Event counter)']]

    """ функция по сокращению символов во float """

    # получаем Installs_to_Login
    itlo = trunc(df[['af_login (Event counter)']].to_numpy() / (df[['Installs']].to_numpy() / 100), decs=1)
    df.insert(2, "Installs_to_Login %", itlo, True)

    # получаем Installs_to_Submit
    itsu = trunc(df[['submit_loan_application (Event counter)']].to_numpy() / (df[['Installs']].to_numpy() / 100),
                 decs=1)
    df.insert(4, "Installs_to_Submit %", itsu, True)

    # получаем Submit_to_Rejected
    stre = trunc(df[['loan_rejected (Event counter)']].to_numpy() / (
            df[['submit_loan_application (Event counter)']].to_numpy() / 100), decs=1)
    df.insert(6, "Submit_to_Rejected %", stre, True)

    # получаем Submit_to_Accepted
    stap = trunc(df[['loan_accepted (Event counter)']].to_numpy() / (
            df[['submit_loan_application (Event counter)']].to_numpy() / 100), decs=1)
    df.insert(8, "Submit_to_Accepted %", stap, True)

    # получаем Submit_to_Lost
    stl = (100 - (stre + stap))
    df.insert(10, "Submit_to_Lost %", stl, True)

    return df


def vanity_af_aggr(df, med_sour, sources):
    """ Добавляем данные в таблицу по бюджету, просмотрам и кликам """
    df_bvc = pd.DataFrame(index=['Budget', 'Views', 'Clicks'])

    for i in range(len(med_sour)):
        df_bvc.insert(0, f"{med_sour[i]}", sources[i], True)

    df_bvc = df_bvc.T

    """ Объединение таблиц """
    df = pd.concat([df_bvc, df], axis=1, join="inner")

    """ сортировка по установкам """

    df = df.sort_values(by='Installs', ascending=False)

    """ Считаем финанансовые метрики  """

    ''' AMOUNT PERCENT '''

    # получаем Clicks_to_Installs
    cti = df[['Installs']].to_numpy() / (df[['Clicks']].to_numpy() / 100)
    cti = trunc(cti, decs=1)
    df.insert(4, "Clicks_to_Installs %", cti, True)

    ''' FINANCIAL '''

    np.seterr(divide='ignore', invalid='ignore')

    # получаем CPAp
    cpap = df[['Budget']].to_numpy() / df[['loan_accepted (Event counter)']].to_numpy()
    cpap = trunc(cpap, decs=2)
    df.insert(3, "CPAp", cpap, True)

    # получаем CPSu
    cpsu = trunc(df[['Budget']].to_numpy() / df[['submit_loan_application (Event counter)']].to_numpy(), decs=2)
    df.insert(3, "CPSu", cpsu, True)

    # получаем CPI
    cpi = trunc(df[['Budget']].to_numpy() / df[['Installs']].to_numpy(), decs=2)
    df.insert(3, "CPI", cpi, True)

    # получаем CPC
    cpc = trunc(df[['Budget']].to_numpy() / df[['Clicks']].to_numpy(), decs=2)
    df.insert(3, "CPC", cpc, True)

    return df


def af_agr_correct_placement(df):
    df = df[['Budget',
             'Views',
             'Clicks',
             'CPC',
             'Clicks_to_Installs %',
             'Installs',
             'CPI',
             'Installs_to_Login %',
             'af_login (Event counter)',
             'Installs_to_Submit %',
             'submit_loan_application (Event counter)',
             'CPSu',
             'Submit_to_Rejected %',
             'loan_rejected (Event counter)',
             'Submit_to_Accepted %',
             'loan_accepted (Event counter)',
             'CPAp',
             'Submit_to_Lost %'
             ]]
    return df


from Appsflyer_api.af_aggregated.af_extra_func import retrieve_name
# from af_tokens import token_tezbol, id_andr_tezbol
# from Appsflyer_api.af_aggregated.af_extra_func import retrieve_name
#
# """ Date """
# from_date = '2022-11-22'
# to_date = '2022-11-30'
#
# """ Token and app ID"""
# app_id = id_andr_tezbol
# token = token_tezbol
#
# """ Sources - Budget, Views, Clicks"""
# Organic = [0, 0, 0]
# googleadwords_int = [1680, 646000, 14500]
# Facebook_Ads = [100, 6000, 1000]
#
# sources = [Organic, googleadwords_int, Facebook_Ads]
#
# # Вспомагательный для получения имен переменных
# media_source = [retrieve_name(x) for x in sources]

if __name__ == '__main__':
    print(vanity_af_aggr(clarity_af_aggr(clear_af_aggr(pull_af_agr_df()))))
    # print(clear_af_aggr(pull_af_agr_df(media_source, app_id, token, from_date, to_date)))
    # print(clarity_af_aggr(clear_af_aggr(pull_af_agr_df(media_source, app_id, token, from_date, to_date))))
    # print(vanity_af_aggr(clarity_af_aggr(clear_af_aggr(pull_af_agr_df(media_source, app_id, token, from_date, to_date))), media_source, sources))