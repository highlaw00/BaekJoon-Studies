import math

def get_diff_time(t1, t2):
    # t1 > t2
    h1, m1 = map(int, t1.split(':'))
    h2, m2 = map(int, t2.split(':'))
    diff = (h1 - h2) * 60 + (m1 - m2)
    return diff

def solution(fees, records):
    default_time, default_fee, unit_time, unit_price = fees
    car_acc_times = dict()
    parking_lot = dict()
    for record in records:
        time, car_num, in_out = record.split()
        if in_out == 'IN':
            parking_lot[car_num] = time
        else:
            in_time = parking_lot[car_num]
            # 출차의 경우 누적 시간을 더한다. 출차 기록이 없는 경우 23:59에 출차한것으로 간주한다.
            car_acc_times[car_num] = car_acc_times.get(car_num, 0) + get_diff_time(time, in_time)
            del parking_lot[car_num]
    
    for car_num, in_time in parking_lot.items():
        car_acc_times[car_num] = car_acc_times.get(car_num, 0) + get_diff_time('23:59', in_time)
    
    final_fees = []
    # 주차 요금 계산
    for car_num, acc_times in car_acc_times.items():
        # 기본 시간 이하라면 기본 요금만 청구
        if default_time >= acc_times:
            final_fees.append({'car_num': car_num, 'fee': default_fee})
            continue
        # 기본 요금 + 초과 시간에 대한 단위 요금 부과
        fee = default_fee + math.ceil((acc_times - default_time) / unit_time) * unit_price
        final_fees.append({'car_num': car_num, 'fee': fee})
    
    final_fees.sort(key=lambda x: x['car_num'])
    for i, elem in enumerate(final_fees):
        fee = elem['fee']
        final_fees[i] = fee
        
    return final_fees