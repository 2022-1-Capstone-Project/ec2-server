import sys

def to_sec(t):
    min, sec = t.rstrip().split(sep=":")
    return 60 * int(min) + int(sec)

def getStride(height : int):
    a = height * 0.37
    b = height - 100
    c = height * 0.45

    if a > c and c >= b : 
        max_stride = a
        min_stride = b

    elif a > b and b >= c : 
        max_stride = a
        min_stride = c

    elif b > c and c >= a : 
        max_stride = b
        min_stride = a

    elif b > a and a >= c : 
        max_stride = b
        min_stride = c
        
    elif c > b and b >= a : 
        max_stride = c
        min_stride = a

    elif c > a and a >= b : 
        max_stride = c
        min_stride = b
    # 평균 보폭
    return round((min_stride + max_stride)/2)

def getTargetPace(sex:str, age:int,workout_level:str, weight:int):
    '''
    1 : starter
    2 : beginner
    3 : novice
    4 : intermediate
    5 : advanced
    6 : elite
    '''
    if sex == 'm':
        if 10 <= age < 15:
            if workout_level   == '1' : target_pace = to_sec('08:00') 
            elif workout_level == '2' : target_pace = to_sec('07:00')
            elif workout_level == '3' : target_pace = to_sec('05:48')
            elif workout_level == '4' : target_pace = to_sec('04:55')
            elif workout_level == '5' : target_pace = to_sec('04:17')
            elif workout_level == '6' : target_pace = to_sec('03:49')

        elif 15 <= age < 20:
            if workout_level   == '1' : target_pace = to_sec('07:24') 
            elif workout_level == '2' : target_pace = to_sec('06:04')
            elif workout_level == '3' : target_pace = to_sec('05:01')
            elif workout_level == '4' : target_pace = to_sec('04:16')
            elif workout_level == '5' : target_pace = to_sec('03:43')
            elif workout_level == '6' : target_pace = to_sec('03:18')

        elif 20 <= age < 25:
            if workout_level   == '1' : target_pace = to_sec('07:00') 
            elif workout_level == '2' : target_pace = to_sec('05:51')
            elif workout_level == '3' : target_pace = to_sec('04:51')
            elif workout_level == '4' : target_pace = to_sec('04:07')
            elif workout_level == '5' : target_pace = to_sec('03:35')
            elif workout_level == '6' : target_pace = to_sec('03:12')

        elif 25 <= age < 30:
            if workout_level   == '1' : target_pace = to_sec('07:00') 
            elif workout_level == '2' : target_pace = to_sec('05:52')
            elif workout_level == '3' : target_pace = to_sec('04:51')
            elif workout_level == '4' : target_pace = to_sec('04:07')
            elif workout_level == '5' : target_pace = to_sec('03:35')
            elif workout_level == '6' : target_pace = to_sec('03:12')

        elif 30 <= age < 35:
            if workout_level   == '1' : target_pace = to_sec('07:00') 
            elif workout_level == '2' : target_pace = to_sec('05:51')
            elif workout_level == '3' : target_pace = to_sec('04:51')
            elif workout_level == '4' : target_pace = to_sec('04:07')
            elif workout_level == '5' : target_pace = to_sec('03:35')
            elif workout_level == '6' : target_pace = to_sec('03:12')

        elif 35 <= age < 40:
            if workout_level   == '1' : target_pace = to_sec('07:00') 
            elif workout_level == '2' : target_pace = to_sec('05:57')
            elif workout_level == '3' : target_pace = to_sec('04:56')
            elif workout_level == '4' : target_pace = to_sec('04:11')
            elif workout_level == '5' : target_pace = to_sec('03:39')
            elif workout_level == '6' : target_pace = to_sec('03:15')

        elif 40 <= age < 45:
            if workout_level   == '1' : target_pace = to_sec('07:20') 
            elif workout_level == '2' : target_pace = to_sec('06:10')
            elif workout_level == '3' : target_pace = to_sec('05:06')
            elif workout_level == '4' : target_pace = to_sec('04:20')
            elif workout_level == '5' : target_pace = to_sec('03:46')
            elif workout_level == '6' : target_pace = to_sec('03:22')
            
        elif 45 <= age < 50:
            if workout_level   == '1' : target_pace = to_sec('07:00') 
            elif workout_level == '2' : target_pace = to_sec('05:51')
            elif workout_level == '3' : target_pace = to_sec('04:51')
            elif workout_level == '4' : target_pace = to_sec('04:07')
            elif workout_level == '5' : target_pace = to_sec('03:35')
            elif workout_level == '6' : target_pace = to_sec('03:12')

        elif 50 <= age < 55:
            if workout_level   == '1' : target_pace = to_sec('07:46') 
            elif workout_level == '2' : target_pace = to_sec('06:39')
            elif workout_level == '3' : target_pace = to_sec('05:30')
            elif workout_level == '4' : target_pace = to_sec('04:40')
            elif workout_level == '5' : target_pace = to_sec('04:04')
            elif workout_level == '6' : target_pace = to_sec('03:37')

        elif 55 <= age < 60:
            if workout_level   == '1' : target_pace = to_sec('08:00') 
            elif workout_level == '2' : target_pace = to_sec('06:55')
            elif workout_level == '3' : target_pace = to_sec('05:44')
            elif workout_level == '4' : target_pace = to_sec('04:52')
            elif workout_level == '5' : target_pace = to_sec('04:14')
            elif workout_level == '6' : target_pace = to_sec('03:46')

        elif 60 <= age < 65:
            if workout_level   == '1' : target_pace = to_sec('08:24') 
            elif workout_level == '2' : target_pace = to_sec('07:13')
            elif workout_level == '3' : target_pace = to_sec('05:58')
            elif workout_level == '4' : target_pace = to_sec('05:04')
            elif workout_level == '5' : target_pace = to_sec('04:25')
            elif workout_level == '6' : target_pace = to_sec('03:56')

        elif 65 <= age < 70:
            if workout_level   == '1' : target_pace = to_sec('08:56') 
            elif workout_level == '2' : target_pace = to_sec('07:32')
            elif workout_level == '3' : target_pace = to_sec('06:14')
            elif workout_level == '4' : target_pace = to_sec('05:18')
            elif workout_level == '5' : target_pace = to_sec('04:36')
            elif workout_level == '6' : target_pace = to_sec('04:06')

        elif 70 <= age < 75:
            if workout_level   == '1' : target_pace = to_sec('09:00') 
            elif workout_level == '2' : target_pace = to_sec('07:54')
            elif workout_level == '3' : target_pace = to_sec('06:33')
            elif workout_level == '4' : target_pace = to_sec('05:34')
            elif workout_level == '5' : target_pace = to_sec('04:50')
            elif workout_level == '6' : target_pace = to_sec('04:19')

        elif 75 <= age < 80:
            if workout_level   == '1' : target_pace = to_sec('10:00') 
            elif workout_level == '2' : target_pace = to_sec('08:30')
            elif workout_level == '3' : target_pace = to_sec('07:02')
            elif workout_level == '4' : target_pace = to_sec('05:18')
            elif workout_level == '5' : target_pace = to_sec('05:12')
            elif workout_level == '6' : target_pace = to_sec('04:38')

        elif 80 <= age < 85:
            if workout_level   == '1' : target_pace = to_sec('11:30') 
            elif workout_level == '2' : target_pace = to_sec('09:24')
            elif workout_level == '3' : target_pace = to_sec('07:47')
            elif workout_level == '4' : target_pace = to_sec('06:37')
            elif workout_level == '5' : target_pace = to_sec('05:45')
            elif workout_level == '6' : target_pace = to_sec('05:08')

        elif 85 <= age < 90:
            if workout_level   == '1' : target_pace = to_sec('12:30') 
            elif workout_level == '2' : target_pace = to_sec('10:49')
            elif workout_level == '3' : target_pace = to_sec('08:58')
            elif workout_level == '4' : target_pace = to_sec('07:37')
            elif workout_level == '5' : target_pace = to_sec('06:37')
            elif workout_level == '6' : target_pace = to_sec('05:54')

        elif 90 <= age :
            if workout_level   == '1' : target_pace = to_sec('13:00') 
            elif workout_level == '2' : target_pace = to_sec('13:11')
            elif workout_level == '3' : target_pace = to_sec('10:55')
            elif workout_level == '4' : target_pace = to_sec('09:16')
            elif workout_level == '5' : target_pace = to_sec('08:04')
            elif workout_level == '6' : target_pace = to_sec('07:12')

    elif sex == 'f':
        if 10 <= age < 15:
            if workout_level   == '1' : target_pace = to_sec('09:00') 
            elif workout_level == '2' : target_pace = to_sec('07:45')
            elif workout_level == '3' : target_pace = to_sec('06:33')
            elif workout_level == '4' : target_pace = to_sec('05:38')
            elif workout_level == '5' : target_pace = to_sec('04:56')
            elif workout_level == '6' : target_pace = to_sec('04:26')

        elif 15 <= age < 20:
            if workout_level   == '1' : target_pace = to_sec('08:00') 
            elif workout_level == '2' : target_pace = to_sec('06:58')
            elif workout_level == '3' : target_pace = to_sec('05:53')
            elif workout_level == '4' : target_pace = to_sec('05:03')
            elif workout_level == '5' : target_pace = to_sec('04:26')
            elif workout_level == '6' : target_pace = to_sec('03:59')

        elif 20 <= age < 35:
            if workout_level   == '1' : target_pace = to_sec('07:40') 
            elif workout_level == '2' : target_pace = to_sec('06:38')
            elif workout_level == '3' : target_pace = to_sec('05:36')
            elif workout_level == '4' : target_pace = to_sec('04:49')
            elif workout_level == '5' : target_pace = to_sec('04:13')
            elif workout_level == '6' : target_pace = to_sec('03:47')

        elif 35 <= age < 40:
            if workout_level   == '1' : target_pace = to_sec('07:30') 
            elif workout_level == '2' : target_pace = to_sec('06:40')
            elif workout_level == '3' : target_pace = to_sec('05:38')
            elif workout_level == '4' : target_pace = to_sec('04:50')
            elif workout_level == '5' : target_pace = to_sec('04:15')
            elif workout_level == '6' : target_pace = to_sec('03:49')

        elif 40 <= age < 45:
            if workout_level   == '1' : target_pace = to_sec('07:20') 
            elif workout_level == '2' : target_pace = to_sec('05:45')
            elif workout_level == '3' : target_pace = to_sec('05:06')
            elif workout_level == '4' : target_pace = to_sec('04:56')
            elif workout_level == '5' : target_pace = to_sec('04:20')
            elif workout_level == '6' : target_pace = to_sec('03:53')
            
        elif 45 <= age < 50:
            if workout_level   == '1' : target_pace = to_sec('08:20') 
            elif workout_level == '2' : target_pace = to_sec('07:03')
            elif workout_level == '3' : target_pace = to_sec('05:57')
            elif workout_level == '4' : target_pace = to_sec('05:07')
            elif workout_level == '5' : target_pace = to_sec('04:30')
            elif workout_level == '6' : target_pace = to_sec('04:02')

        elif 50 <= age < 55:
            if workout_level   == '1' : target_pace = to_sec('08:36') 
            elif workout_level == '2' : target_pace = to_sec('07:25')
            elif workout_level == '3' : target_pace = to_sec('06:16')
            elif workout_level == '4' : target_pace = to_sec('05:23')
            elif workout_level == '5' : target_pace = to_sec('04:43')
            elif workout_level == '6' : target_pace = to_sec('04:14')

        elif 55 <= age < 60:
            if workout_level   == '1' : target_pace = to_sec('09:10') 
            elif workout_level == '2' : target_pace = to_sec('07:51')
            elif workout_level == '3' : target_pace = to_sec('06:37')
            elif workout_level == '4' : target_pace = to_sec('05:41')
            elif workout_level == '5' : target_pace = to_sec('05:00')
            elif workout_level == '6' : target_pace = to_sec('04:29')

        elif 60 <= age < 65:
            if workout_level   == '1' : target_pace = to_sec('09:40') 
            elif workout_level == '2' : target_pace = to_sec('08:19')
            elif workout_level == '3' : target_pace = to_sec('07:01')
            elif workout_level == '4' : target_pace = to_sec('06:02')
            elif workout_level == '5' : target_pace = to_sec('05:18')
            elif workout_level == '6' : target_pace = to_sec('04:45')

        elif 65 <= age < 70:
            if workout_level   == '1' : target_pace = to_sec('10:26') 
            elif workout_level == '2' : target_pace = to_sec('08:52')
            elif workout_level == '3' : target_pace = to_sec('07:29')
            elif workout_level == '4' : target_pace = to_sec('06:26')
            elif workout_level == '5' : target_pace = to_sec('05:39')
            elif workout_level == '6' : target_pace = to_sec('05:04')

        elif 70 <= age < 75:
            if workout_level   == '1' : target_pace = to_sec('11:00') 
            elif workout_level == '2' : target_pace = to_sec('09:29')
            elif workout_level == '3' : target_pace = to_sec('08:00')
            elif workout_level == '4' : target_pace = to_sec('06:53')
            elif workout_level == '5' : target_pace = to_sec('06:02')
            elif workout_level == '6' : target_pace = to_sec('05:25')

        elif 75 <= age < 80:
            if workout_level   == '1' : target_pace = to_sec('12:00') 
            elif workout_level == '2' : target_pace = to_sec('10:11')
            elif workout_level == '3' : target_pace = to_sec('08:36')
            elif workout_level == '4' : target_pace = to_sec('07:23')
            elif workout_level == '5' : target_pace = to_sec('06:29')
            elif workout_level == '6' : target_pace = to_sec('05:49')

        elif 80 <= age < 85:
            if workout_level   == '1' : target_pace = to_sec('13:30') 
            elif workout_level == '2' : target_pace = to_sec('11:01')
            elif workout_level == '3' : target_pace = to_sec('09:18')
            elif workout_level == '4' : target_pace = to_sec('08:00')
            elif workout_level == '5' : target_pace = to_sec('07:01')
            elif workout_level == '6' : target_pace = to_sec('06:18')

        elif 85 <= age < 90:
            if workout_level   == '1' : target_pace = to_sec('14:30') 
            elif workout_level == '2' : target_pace = to_sec('12:25')
            elif workout_level == '3' : target_pace = to_sec('10:29')
            elif workout_level == '4' : target_pace = to_sec('09:00')
            elif workout_level == '5' : target_pace = to_sec('07:54')
            elif workout_level == '6' : target_pace = to_sec('07:05')

        elif 90 <= age :
            if workout_level   == '1' : target_pace = to_sec('17:00') 
            elif workout_level == '2' : target_pace = to_sec('14:58')
            elif workout_level == '3' : target_pace = to_sec('12:37')
            elif workout_level == '4' : target_pace = to_sec('10:51')
            elif workout_level == '5' : target_pace = to_sec('09:32')
            elif workout_level == '6' : target_pace = to_sec('08:33')

    return target_pace

def rec_bpm(sex, age, height, weight,  workout_level, target_pace, stride):
    sex = sex
    age = int(age)
    height = int(height)
    weight = int(weight)
    if workout_level == '0' : workout_level = 1
    else: workout_level = workout_level
    if target_pace == '0' : target_pace = 0
    else: target_pace = to_sec(target_pace) # 이것도 '00:00' 꼴로 입력 
    stride = int(stride)

    if target_pace != 0 and stride == 0: # 타겟 페이스는 있는데 보폭을 모를 때
        stride = getStride(height)
        #print(stride)

    elif target_pace == 0 and stride != 0: # 타겟 페이스모름 보폭을 알 때
        target_pace = getTargetPace(sex,age,workout_level,weight)

    elif target_pace == 0 and stride == 0: # 둘 다 모를 때
        stride = getStride(height)
        target_pace = getTargetPace(sex,age,workout_level,weight)

    else: pass # 둘 다 알 때


    # kilo_per_hour = 3600/target_pace   # km/h
    footnum = int(100000/stride)+1 # 보폭으로 뛰었을 때 몇번 발걸음을 해야하는지

    recommend_bpm = footnum/(target_pace/60)
    bpm = int(recommend_bpm)
    
    print(f'{bpm-5} ~ {bpm+5}')
    return f'{bpm-5} ~ {bpm+5}'



if __name__ == '__main__':

    sex = sys.argv[1] # 성별, 'f' of 'm', type: str
    age = sys.argv[2] # 나이 , type:str
    height = sys.argv[3] # 키 , type:str
    weight = sys.argv[4] # '00', type:str

    workout_level = sys.argv[5] # 운동 강도 1~6 숫자가 클수록 고강도 , type:str
    target_pace = sys.argv[6] # "00:00" 형태. 타켓 페이스 , type:str
    stride = sys.argv[7] # 보폭  , type:str
    # workout_duration = sys.argv[8]

    rec_bpm(sex, age, height, weight, workout_level, target_pace, stride)
