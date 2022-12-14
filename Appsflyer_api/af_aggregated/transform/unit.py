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

    try:
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
            'submit_loan_application (Event counter)'], axis=1)


    except:
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
            'submit_loan_application (Event counter)'], axis=1)

    try:
        if 'af_login (Sales in KZT)' in df.columns:
            df = df.drop([
                'af_complete_registration (Sales in KZT)',
                'af_login (Sales in KZT)',
                'install_kreditomat (Sales in KZT)',
                'loan_accepted (Sales in KZT)',
                'loan_rejected (Sales in KZT)',
                'submit_loan_application (Sales in KZT)'], axis=1)
        else:
            df = df.drop([
                'af_complete_registration (Sales in USD)',
                'af_login (Sales in USD)',
                'install_kreditomat (Sales in USD)',
                'loan_accepted (Sales in USD)',
                'loan_rejected (Sales in USD)',
                'submit_loan_application (Sales in USD)'], axis=1)
    except:
        if 'af_login (Sales in KZT)' in df.columns:
            df = df.drop([
                'af_login (Sales in KZT)',
                'install_kreditomat (Sales in KZT)',
                'loan_accepted (Sales in KZT)',
                'loan_rejected (Sales in KZT)',
                'submit_loan_application (Sales in KZT)'], axis=1)
        else:
            df = df.drop([
                'af_login (Sales in USD)',
                'install_kreditomat (Sales in USD)',
                'loan_accepted (Sales in USD)',
                'loan_rejected (Sales in USD)',
                'submit_loan_application (Sales in USD)'], axis=1)

    # transposition columns without BUDGET
    df = df[['Sessions', 'Installs', 'af_login (Event counter)', 'submit_loan_application (Unique users)',
             'loan_rejected (Event counter)', 'loan_accepted (Event counter)']]
    return df


def clarity_af_aggr(df):
    # transposition columns without BUDGET
    df = df[['Sessions', 'Installs', 'af_login (Event counter)', 'submit_loan_application (Unique users)',
             'loan_rejected (Event counter)', 'loan_accepted (Event counter)']]

    """ ?????????????? ???? ???????????????????? ???????????????? ???? float """

    # ???????????????? Installs_to_Login
    itlo = trunc(df[['af_login (Event counter)']].to_numpy() / (df[['Installs']].to_numpy() / 100), decs=1)
    df.insert(2, "Installs_to_Login %", itlo, True)

    # ???????????????? Installs_to_Submit
    itsu = trunc(df[['submit_loan_application (Unique users)']].to_numpy() / (df[['Installs']].to_numpy() / 100),
                 decs=1)
    df.insert(4, "Installs_to_Submit %", itsu, True)

    # ???????????????? Installs_to_Accepted
    itap = trunc(df[['loan_accepted (Event counter)']].to_numpy() / (df[['Installs']].to_numpy() / 100),
                 decs=1)
    df.insert(4, "Installs_to_Accepted %", itap, True)

    # # ???????????????? Submit_to_Rejected
    # stre = trunc(df[['loan_rejected (Event counter)']].to_numpy() / (
    #         df[['submit_loan_application (Unique users)']].to_numpy() / 100), decs=1)
    # df.insert(6, "Submit_to_Rejected %", stre, True)

    # # ???????????????? Submit_to_Accepted
    # stap = trunc(df[['loan_accepted (Event counter)']].to_numpy() / (
    #         df[['submit_loan_application (Unique users)']].to_numpy() / 100), decs=1)
    # df.insert(8, "Submit_to_Accepted %", stap, True)

    # # ???????????????? Submit_to_Lost
    # stl = (100 - (stre + stap))
    # df.insert(10, "Submit_to_Lost %", stl, True)

    return df


def vanity_af_aggr(df, med_sour, sources):
    """ ?????????????????? ???????????? ?? ?????????????? ???? ??????????????, ???????????????????? ?? ???????????? """
    df_bvc = pd.DataFrame(index=['Budget', 'Views', 'Clicks'])

    for i in range(len(med_sour)):
        df_bvc.insert(0, f"{med_sour[i]}", sources[i], True)

    df_bvc = df_bvc.T

    """ ?????????????????????? ???????????? """
    df = pd.concat([df_bvc, df], axis=1, join="inner")

    """ ???????????????????? ???? ???????????????????? """

    df = df.sort_values(by='Installs', ascending=False)

    """ ?????????????? ???????????????????????? ??????????????  """

    ''' AMOUNT PERCENT '''

    # ???????????????? Clicks_to_Installs
    cti = df[['Installs']].to_numpy() / (df[['Clicks']].to_numpy() / 100)
    cti = trunc(cti, decs=1)
    df.insert(4, "Clicks_to_Installs %", cti, True)

    ''' FINANCIAL '''

    np.seterr(divide='ignore', invalid='ignore')

    # ???????????????? CPAp
    cpap = df[['Budget']].to_numpy() / df[['loan_accepted (Event counter)']].to_numpy()
    cpap = trunc(cpap, decs=2)
    df.insert(3, "CPAp", cpap, True)

    # ???????????????? CPSu
    cpsu = trunc(df[['Budget']].to_numpy() / df[['submit_loan_application (Unique users)']].to_numpy(), decs=2)
    df.insert(3, "CPSu", cpsu, True)

    # ???????????????? CPI
    cpi = trunc(df[['Budget']].to_numpy() / df[['Installs']].to_numpy(), decs=2)
    df.insert(3, "CPI", cpi, True)

    # ???????????????? CPC
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
             'submit_loan_application (Unique users)',
             'CPSu',
             # 'Submit_to_Rejected %',
             'loan_rejected (Event counter)',
             # 'Submit_to_Accepted %',
             'Installs_to_Accepted %',
             'loan_accepted (Event counter)',
             'CPAp',
             # 'Submit_to_Lost %'
             ]]
    return df



if __name__ == '__main__':
    print(vanity_af_aggr(clarity_af_aggr(clear_af_aggr(pull_af_agr_df()))))
    # print(clear_af_aggr(pull_af_agr_df(media_source, app_id, token, from_date, to_date)))
    # print(clarity_af_aggr(clear_af_aggr(pull_af_agr_df(media_source, app_id, token, from_date, to_date))))
    # print(vanity_af_aggr(clarity_af_aggr(clear_af_aggr(pull_af_agr_df(media_source, app_id, token, from_date, to_date))), media_source, sources))
