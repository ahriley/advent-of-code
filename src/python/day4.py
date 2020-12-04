import numpy as np

# read and sort the data by time
with open('data/day4.txt') as f:
    lines = f.readlines()
    datetimes = [np.datetime64(line[1:11]+'T'+line[12:17]) for line in lines]
    log = [line for _,line in sorted(zip(datetimes,lines))]
datetimes = np.sort(datetimes)
dates = datetimes.astype('datetime64[D]')
dates = np.arange(dates[1], dates[-1] + np.timedelta64(2, 'D'))
dates
