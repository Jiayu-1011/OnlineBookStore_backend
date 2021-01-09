
import time

def generateBookId(name, date):
    temp = date.split('-')
    year = temp[0]
    month = temp[1]
    day = temp[2]

    return name + year + month + day

# 根据当前时间计算订单编号
# 如2021-01-08 18:24:30 -> 20210108182430
def generateOrderId():
    year = str(time.localtime().tm_year)

    if time.localtime().tm_mon < 10:
        month = '0' + str(time.localtime().tm_mon)
    else:
        month = str(time.localtime().tm_mon)

    if time.localtime().tm_mday < 10:
        day = '0' + str(time.localtime().tm_mday)
    else:
        day = str(time.localtime().tm_mday)

    if time.localtime().tm_hour < 10:
        hour = '0' + str(time.localtime().tm_hour)
    else:
        hour = str(time.localtime().tm_hour)

    if time.localtime().tm_min < 10:
        minute = '0' + str(time.localtime().tm_min)
    else:
        minute = str(time.localtime().tm_min)

    if time.localtime().tm_sec < 10:
        second = '0' + str(time.localtime().tm_sec)
    else:
        second = str(time.localtime().tm_sec)


    return year + month + day + hour + minute + second

# print(generateOrderId())

def generateFormatTime():
    year = str(time.localtime().tm_year)

    if time.localtime().tm_mon < 10:
        month = '0' + str(time.localtime().tm_mon)
    else:
        month = str(time.localtime().tm_mon)

    if time.localtime().tm_mday < 10:
        day = '0' + str(time.localtime().tm_mday)
    else:
        day = str(time.localtime().tm_mday)

    if time.localtime().tm_hour < 10:
        hour = '0' + str(time.localtime().tm_hour)
    else:
        hour = str(time.localtime().tm_hour)

    if time.localtime().tm_min < 10:
        minute = '0' + str(time.localtime().tm_min)
    else:
        minute = str(time.localtime().tm_min)

    if time.localtime().tm_sec < 10:
        second = '0' + str(time.localtime().tm_sec)
    else:
        second = str(time.localtime().tm_sec)


    return year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second

print(generateFormatTime())

