import math
def parking_fee(time):
    time_sum = time / 60
    return (math.ceil(time_sum)-1) * 30

def parking_time(time):
    h = time // 60
    m = time% 60
    print("เวลาที่จอดรถ : ", h ," ชั่วโมง", m ," นาที")

hour = int(input("ชั่วโมง : "))
minute = int(input("นาที : "))
timeSum = (hour*60)+minute

if(timeSum <= 60):
    parking_time(timeSum)
    print("ค่าจอดรถฟรี!")
else:
    parking_time(timeSum)
    print("ค่าจอดรถทั้งหมด : ", parking_fee(timeSum)," บาท")
