from Appsflyer_api.af_events_data.reques_af_api_events import pull_af_all_events_non_org
import pandas as pd


class AF_events_data:
    def __init__(self, app_id, token, from_date, to_date):

        self.app_id = app_id
        self.token = token
        self.from_date = from_date
        self.to_date = to_date

    def get_all_events(self):
        return pull_af_all_events_non_org(self.app_id, self.token, self.from_date, self.to_date)

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