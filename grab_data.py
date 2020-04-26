import os
import wget

if not os.path.exists('data'):
    os.makedirs('data')

url_meta = {
    'confirmed': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
    'deaths': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv',
    'recovered': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
}

for key, value in url_meta.items():
    desti_path = os.path.join('data', value.split('/')[-1])
    if os.path.exists(desti_path):
        print(f'\n{key} data already exists at: {desti_path}. Re-downloading', end='')
        os.remove(desti_path)
    print(f'\nDownloading {key} data')
    wget.download(value, desti_path)