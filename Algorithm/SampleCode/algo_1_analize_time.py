#!usr/bin/env python

# 对于下表中的每一个函数f(n)和时间t，求出可以在时间t内被求解出来的问题的最大规模n
# (假设解决该问题的时间为f(n)微妙)

import math
time_1_s = 10 ** 6
time_1_min = time_1_s * 60
time_1_hour = time_1_min * 60
time_1_day = time_1_hour * 24
time_1_mouth = time_1_day * 30
time_1_year = time_1_mouth * 12
time_century = time_1_year * 50

def compute_n(time_func, result_time, range_func=None):
    result = None
    start_num = 1
    end_num = result_time
    if range_func:
        result =range_func(result_time)
    else:
        result = (start_num, end_num)
    while not isinstance(result, int):
        if isinstance(result, tuple):
            start_num, end_num = result
            result = bi_search(time_func, result_time, start_num, end_num)
            # print(result)
    return result

def bi_search(time_func, result, start, end):
    if start + 1 >= end:
        return start
    mid = (start + end) // 2
    time_func_result = time_func(mid)
    if time_func_result == result:
        return mid
    elif time_func_result > result:
        return start, mid
    else:
        return mid, end

def log_n_func(n):
    return math.log(n)

def sqrt_n_func(n):
    return math.sqrt(n)

def n_func(n):
    return n


def n_n_func(n):
    return n**2


def n_3_func(n):
    return n**3


def n_log_n(n):
    return math.log(n) * n


def n_recursion(n):
    # 斯特林公式：sqrt(2*pi*n)(n/e)^n
    # return math.sqrt(2*math.pi*n)*n_2_n(n, n/math.e)
    result = 1
    for i in range(1, n):
        result *= i
    return result

def n_2_n(n, a=None):
    # # 将n分解为1+2+4+...
    # list_2_n = {}
    # cnt_n = 0
    # i = 1
    # while(cnt_n < n):
    #     if cnt_n == 0:
    #         pass
    cnt = 0
    cnt_remainder_list = []
    tmp_n = n
    while tmp_n >= 2:
        tmp_remainder_n = tmp_n % 2
        tmp_n = tmp_n // 2
        cnt += 1
        cnt_remainder_list.append(tmp_remainder_n)
    cnt_remainder_list.reverse()

    if n == 1:
        return 2
    elif n == 2:
        return 4
    elif n == 3:
        return 8
    else:
        result = a if a else 2
        for idx, tmp_remainder in enumerate(cnt_remainder_list):
            if tmp_remainder:
                result = (result * result) * 2
            else:
                result = result * result
    return result
if __name__ == "__main__":
    for i in range(1, 20):
        print(n_recursion(i))
    func_dict = {
        'logn': log_n_func,
        'sqrt_n': sqrt_n_func,
        'n': n_func,
        'nlogn': n_log_n,
        'n^2': n_n_func,
        'n^3': n_3_func, 
        'n_recur': n_recursion,
        'n_2_n': n_2_n,
    }

    func_name_2_range_func_dict = {
        'logn': lambda n: (1, n*n + n),
        'sqrt_n': lambda n: (1, n*n + n * 100000),
        'n': lambda n: (1, n),
        'nlogn': lambda n: (1, n),
        'n^2': lambda n: (1, n),
        'n^3': lambda n: (1, n),
        'n_2_n': lambda n: (1, 100),
        'n_recur': lambda n: (1, 100),
    }

    time_result_dict = {
        'time_1_s': time_1_s,
        'time_1_min': time_1_min,
        'time_1_hour': time_1_hour,
        'time_1_day': time_1_day,
        'time_1_mouth': time_1_mouth,
        'time_1_year': time_1_year,
        'time_century': time_century,
    }


    for idx, name in enumerate(time_result_dict.keys()):
        if idx != 0:
            print('\t', end='')
        print(name, end='')
    print('\n', end='')
    for name, time_func in func_dict.items():
        result_n_list = []
        for time_check_name, time_result in time_result_dict.items():
            result_n = compute_n(time_func=time_func, result_time=time_result, range_func=func_name_2_range_func_dict[name])
            # print("compute: ", result_n)
            result_n_list.append(result_n)
        print('{0}: '.format(name), end='')
        # print('\t\t')
        for _idx, _name in enumerate(result_n_list):
            if _idx != 0:
                print('\t', end='')
            print(_name, end='')
        print('\n', end='')