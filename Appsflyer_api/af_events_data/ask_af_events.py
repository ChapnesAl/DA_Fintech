from Appsflyer_api.af_events_data.reques_af_api_events import pull_af_all_events_non_org
from Appsflyer_api.af_extra_func import array_parsing
import pandas as pd


class AF_events_data:
    def __init__(self, app_id, token, from_date, to_date):

        self.app_id = app_id
        self.token = token
        self.from_date = from_date
        self.to_date = to_date

    def get_all_events(self):
        df = pull_af_all_events_non_org(self.app_id, self.token, self.from_date, self.to_date)
        # извлечение колонок из массива Event Value
        key_1 = 'ClientState'
        key_2 = 'loam_amount'
        key_3 = 'loan_period'
        df[key_1] = array_parsing(key_1, df)
        df[key_2] = array_parsing(key_2, df)
        df[key_3] = array_parsing(key_3, df)

        return df

    def get_loan_rejected_cuID(self):
        df = pull_af_all_events_non_org(self.app_id, self.token, self.from_date, self.to_date)
        event = df.loc[df['Event Name'] == 'loan_rejected']

        sorted = event.sort_values('Customer User ID', ascending=True)
        event = sorted.groupby('Customer User ID').first().reset_index()

        event = event.drop_duplicates(subset='Customer User ID')

        event['Customer User ID'].to_excel(r'C:/Users/PC/Desktop/DataAnalytics/Events/loan_rej_customerID.xlsx',
                                              index=False)

        return event['Customer User ID']


    def get_loan_accepted_cuID(self):
        df = pull_af_all_events_non_org(self.app_id, self.token, self.from_date, self.to_date)
        event = df.loc[df['Event Name'] == 'loan_accepted']

        sorted = event.sort_values('Customer User ID', ascending=True)
        event = sorted.groupby('Customer User ID').first().reset_index()

        event = event.drop_duplicates(subset='Customer User ID')

        event['Customer User ID'].to_excel(r'C:/Users/PC/Desktop/DataAnalytics/Events/loan_accep_customerID.xlsx',
                                              index=False)

        return event['Customer User ID']



    def get_sumbit_cuID(self):
        df = pull_af_all_events_non_org(self.app_id, self.token, self.from_date, self.to_date)
        event = df.loc[df['Event Name'] == 'submit_loan_application']

        sorted = event.sort_values('Customer User ID', ascending=True)
        event = sorted.groupby('Customer User ID').first().reset_index()

        event = event.drop_duplicates(subset='Customer User ID')

        event['Customer User ID'].to_excel(r'C:/Users/PC/Desktop/DataAnalytics/Events/sub_customerID.xlsx',
                                              index=False)

        return event['Customer User ID']

    def get_sumbit_cuID_events(self):
        df = pull_af_all_events_non_org(self.app_id, self.token, self.from_date, self.to_date)
        event = df.loc[df['Event Name'] == 'submit_loan_application']

        sorted = event.sort_values('Customer User ID', ascending=True)
        event = sorted.groupby('Customer User ID').first().reset_index()

        event = event.drop_duplicates(subset='Customer User ID')
        event[['Customer User ID', 'Event Time']].to_excel(r'C:/Users/PC/Desktop/DataAnalytics/Events/sub_customerID.xlsx',
                                              index=False)

        return event[['Customer User ID', 'Event Time']]

    def get_channels(self):
        df = pull_af_all_events_non_org(self.app_id, self.token, self.from_date, self.to_date)
        sources = list(df['Media Source'].unique())
        if 'restricted' in sources:
            ind = sources.index('restricted')
            sources[ind] = 'Facebook_Ads'
        else:
            pass

        return sources