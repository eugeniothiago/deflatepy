import pandas as pd
import ipeadatapy as ip
import datetime
import requests
import json

def main():
    series= "PRECOS_IPCAG"
    pos_fix = "('%s')" % series if series is not None else ""
    series_url = "http://www.ipeadata.gov.br/api/odata4/Metadados%s" % pos_fix + '/Valores'
    ipca = requests.get(series_url)
    ipca_df = pd.DataFrame(json.loads(ipca.text)['value'])
    ipca_df['VALDATA'] = pd.to_datetime(ipca_df['VALDATA'].apply(pd.to_datetime), utc=True)


if __name__=="__main__":
    main()