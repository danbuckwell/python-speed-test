# Python Speed Test

A Python script to execute an internet speed test using [speedtest.net](https://www.speedtest.net). Results are saved to a csv for future reference and analysis.

## Prerequisites

This script depends on `pandas` and `speedtest-cli` in order to run. Both can be install via `pip`:

```basic
pip install pandas
pip install speedtest-cli
```

## Output

Speed test results will be written to `results.csv` unless otherwise specified using `output_file` in `speed_test.py`.

### Format

| Field    | Format                         | Description          |
| :------- | :----------------------------- | :------------------- |
| Date     | Datetime (`%Y/%m/%d %H:%M:%S`) | Datetime of test     |
| Service  | String                         | Speed test provider  |
| Download | Decimal                        | Download speed in Mb |
| Upload   | Decimal                        | Upload speed in Mb   |
| Ping     | Decimal                        | Ping in seconds      |
