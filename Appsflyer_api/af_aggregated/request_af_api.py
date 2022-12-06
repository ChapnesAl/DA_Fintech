import requests
import pandas as pd
import io
import time

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def pull_af_agr_df(med_sour, app_id, token, from_date, to_date):

    def pull_request(med_sour, app_id, token, from_date, to_date):
        if med_sour == 'Facebook_Ads':
            url = f"https://hq1.appsflyer.com/api/agg-data/export/app/{app_id}/partners_report/v5?from={from_date}&to={to_date}&media_source={med_sour}&category=facebook"
        else:
            url = f"https://hq1.appsflyer.com/api/agg-data/export/app/{app_id}/partners_report/v5?from={from_date}&to={to_date}&media_source={med_sour}&category=standard"

        headers = {
            "accept": "text/csv",
            "authorization": token
        }

        urlData = requests.get(url, headers=headers).content
        rawData = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
        return rawData

    df_agre = None
    if type(med_sour) == list:
        for i in range(len(med_sour)):
            if str(type(df_agre)) == "<class 'NoneType'>":
                df_agre = pull_request(med_sour[i], app_id, token, from_date, to_date)
            else:
                time.sleep(60)
                df_agre = pd.concat([df_agre, pull_request(med_sour[i], app_id, token, from_date, to_date)])
    else:
        print('Проблема в запросе API Appsflyer')

    return df_agre


if __name__ == '__main__':
    print(1)
