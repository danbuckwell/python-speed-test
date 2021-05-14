'''
Python Speed Test

A Python script to execute an internet speed test using speedtest.net.
Results are saved to a csv for future reference and analysis.
'''
import os
import ssl
import speedtest
import pandas as pd
import datetime as dt

# Output file
output_file = 'results.csv'

# Create HTTPS context to mitigate SSL issues
if (not os.environ.get(
    'PYTHONHTTPSVERIFY', '') and getattr(
        ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


def execute_test():
    # Execute speed test
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]


def main():

    print('\nRunning speedtest...')
    # Execute speed test, creating download, upload, and ping variables
    d, u, p = execute_test()

    # Print results to console, converting download and upload from b to Mb
    print('\nTest\n')
    print('Download: {:.2f} Mb/s\n'.format(d / (1024 * 1024)))
    print('Upload: {:.2f} Mb/s\n'.format(u / (1024 * 1024)))
    print('Ping: {}\n'.format(p))

    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    # Check that output_file exists
    if os.path.isfile(output_file):
        # If file exits, read contents to data frame
        df = pd.read_csv(output_file, skip_blank_lines=True)
    else:
        # If file does nont exist, create empty data frame to store new values
        df = pd.DataFrame({
            'Date': [],
            'Service': [],
            'Download': [],
            'Upload': [],
            'Ping': []
        })

    # Add new results to data frame
    df = df.append(
        pd.DataFrame({
            'Date': [dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S")],
            'Service': 'Speedtest.net',
            'Download': [round(d / (1024 * 1024), 2)],
            'Upload': [round(u / (1024 * 1024), 2)],
            'Ping': [p]
        })
    )

    # Write results to csv
    df.to_csv(
        output_file,
        index=False)


if __name__ == '__main__':
    main()
