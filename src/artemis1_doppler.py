import datetime as dt
from astropy import time
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# http://maia.usno.navy.mil/ser7/tai-utc.dat
constant_offset = 2430000
infile_CAN = "./gmd/DSN_CAN_range_and_doppler_measurements.gmd"
infile_GDS = "./gmd/DSN_GDS_range_and_doppler_measurements.gmd"
infile_MAD = "./gmd/DSN_MAD_range_and_doppler_measurements.gmd"

# electromagnetic waves in vacuum [km/s]
c = 299792.458
# frequency
f_X = 7.16e+09  # X-band [Hz]
# f_X = 8.4 * 1.0e+09
# transponder turn around ratio 探査機トランスポンダ周波数変換比
M2_S = 240/221
M2_X = 880/749

time_CAN = []
doppler_CAN = []
time_GDS = []
doppler_GDS = []
time_MAD = []
doppler_MAD = []

with open(infile_CAN) as f:
    datalist = f.readlines()
    for data in datalist:
        data = data.split()
        if len(data) == 8:
            # print(data)
            epoch = time.Time(float(data[0]) + constant_offset, format='jd', scale='tai')
            dtobj = dt.datetime.strptime(epoch.utc.fits, "%Y-%m-%dT%H:%M:%S.%f")
            # doppler
            doppler = float(data[7])
            time_CAN.append(dtobj)
            doppler_CAN.append(doppler)
# with open read end

with open(infile_GDS) as f:
    datalist = f.readlines()
    for data in datalist:
        data = data.split()
        if len(data) == 8:
            # print(data)
            epoch = time.Time(float(data[0]) + constant_offset, format='jd', scale='tai')
            dtobj = dt.datetime.strptime(epoch.utc.fits, "%Y-%m-%dT%H:%M:%S.%f")
            # doppler
            doppler = float(data[7])
            time_GDS.append(dtobj)
            doppler_GDS.append(doppler)
# with open read end

with open(infile_MAD) as f:
    datalist = f.readlines()
    for data in datalist:
        data = data.split()
        if len(data) == 8:
            # print(data)
            epoch = time.Time(float(data[0]) + constant_offset, format='jd', scale='tai')
            dtobj = dt.datetime.strptime(epoch.utc.fits, "%Y-%m-%dT%H:%M:%S.%f")
            # doppler
            doppler = float(data[7])
            time_MAD.append(dtobj)
            doppler_MAD.append(doppler)
# with open read end

# figure
fig = plt.figure(figsize=(10,5),tight_layout=True)
ax1 = fig.add_subplot(111)
ax1.scatter(time_CAN,doppler_CAN,c="r",s=10,marker=".",label="CAN")
ax1.scatter(time_GDS,doppler_GDS,c="g",s=10,marker=".",label="GDS")
ax1.scatter(time_MAD,doppler_MAD,c="b",s=10,marker=".",label="MAD")
ax1.set_title('doppler CAN, GDS, MAD')
ax1.set_xlabel('date [UTC]')
ax1.set_ylabel('doppler observation [Hz]')
ax1.legend()
ax1.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M:%S'))
ax1.set_xlim([time_CAN[0],time_CAN[-1]])
ax1.tick_params(axis='x', rotation=45)
plt.show()