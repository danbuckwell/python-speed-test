'''
Python Speed Test

An automatable Python script that can be used to
execute a network speed test and log the results
'''
import os
import ssl
import speedtest
import pandas as pd
import datetime as dt

if (not os.environ.get(
    'PYTHONHTTPSVERIFY', '') and getattr(
        ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


def execute_test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]


def main():

    print('\nRunning speedtest...')
    d, u, p = execute_test()

    print('\nTest\n')
    print('Download: {:.2f} Mb/s\n'.format(d / (1024 * 1024)))
    print('Upload: {:.2f} Mb/s\n'.format(u / (1024 * 1024)))
    print('Ping: {}\n'.format(p))

    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    if os.path.isfile('results.csv'):
        df = pd.read_csv('results.csv', skip_blank_lines=True)
    else:
        df = pd.DataFrame({
            'Date': [],
            'Service': [],
            'Download': [],
            'Upload': [],
            'Ping': []
        })

    df = df.append(
        pd.DataFrame({
            'Date': [dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S")],
            'Service': 'Speedtest.net',
            'Download': [round(d / (1024 * 1024), 2)],
            'Upload': [round(u / (1024 * 1024), 2)],
            'Ping': [p]
        })
    )

    df.to_csv(
        'results.csv',
        index=False)


if __name__ == '__main__':
    main()
