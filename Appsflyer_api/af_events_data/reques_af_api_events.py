import requests
import pandas as pd
import numpy as np
import csv
import io

def pull_af_all_events_non_org(app_id, token, from_date, to_date):
    url = f"https://hq1.appsflyer.com/api/raw-data/export/app/{app_id}/in_app_events_report/v5?from={from_date}&to={to_date}&event_name=&reattr=false&additional_fields=blocked_reason_rule,store_reinstall,impressions,conversion_type,gp_click_time,match_type,mediation_network,oaid,deeplink_url,gp_install_begin,campaign_type,custom_data,device_download_time,device_model,monetization_network,segment,store_product_page,device_category"

    headers = {
        "accept": "text/csv",
        "authorization": token}

    urlData = requests.get(url, headers=headers).content
    df = pd.read_csv(io.StringIO(urlData.decode('utf-8')), low_memory=False)
    return df


