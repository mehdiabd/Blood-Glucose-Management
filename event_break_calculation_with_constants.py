"""_summary_
    This very Python code is identic to the other one, named 'event_break_calculation.py', except for the approach
    of looping over the code. Here instead of running the whole script for N times, every time we suppose that 
    all variables are constants except for one of them. So if we have 5 variables, we should do this job for 5 times.
Returns:
    _time(s)_: Returns a number of each variable which is the time lasted during the whole transmission process.
"""

import numpy as np

# declaring powers as variables (mw)
P_on: float = 0.30
# P_off: float = 0.0
P_off: np.array = np.arange(.0001, .229, .0005)
P_off2on: np.array = np.arange(.1, 120, .05)
P_on2off: np.array = np.arange(.1, 100, .05)

# declaring times (s)
T_off2on: np.array = np.arange(30, 91, .5)
T_on2off: np.array = np.arange(15, 61, .5)


def by_P_off_calculate_T_be(P_on, P_off, P_on2off, P_off2on, T_on2off, T_off2on):
    for i in P_off:
        # power and time consumed in each transmission
        T_tr = T_on2off + T_off2on
        P_tr = ((T_on2off * P_on2off) + (T_off2on * P_off2on)) / T_tr

        T_be: float = (
            T_tr + T_tr * ((P_tr - P_on) / (P_on - i)) if P_tr > P_on
            else T_tr
        )

        # print everything
        print(f"* POWER consumed when OFF: {i} mw")
        print(f"* POWER consumed when SWITCHING ON: {P_off2on} mw")
        print(f"* POWER consumed when SWITCHING OFF: {P_on2off} mw")
        print(f"* TIME passed when SWITCHING ON: {T_off2on} s")
        print(f"* TIME passed when SWITCHING OFF: {T_on2off} s")
        print(f"* TIME passed while transmitting: {T_tr} s")
        print(f"* POWER consumed while transmitting: {P_tr} mw")
        print(f'=> Final Event Break: {T_be}')
        print("************************************************")

    return T_be


def by_P_on2off_calculate_T_be(P_on, P_off, P_on2off, P_off2on, T_on2off, T_off2on):
    for i in P_on2off:
        # power and time consumed in each transmission
        T_tr = T_on2off + T_off2on
        P_tr = ((T_on2off * i) + (T_off2on * P_off2on)) / T_tr

        T_be: float = (
            T_tr + T_tr * ((P_tr - P_on) / (P_on - P_off)) if P_tr > P_on else T_tr
        )

        # print everything
        print(f"* POWER consumed when OFF: {P_off} mw")
        print(f"* POWER consumed when SWITCHING ON: {P_off2on} mw")
        print(f"* POWER consumed when SWITCHING OFF: {i} mw")
        print(f"* TIME passed when SWITCHING ON: {T_off2on} s")
        print(f"* TIME passed when SWITCHING OFF: {T_on2off} s")
        print(f"* TIME passed while transmitting: {T_tr} s")
        print(f"* POWER consumed while transmitting: {P_tr} mw")
        print(f'=> Final Event Break: {T_be}')
        print("************************************************")

    return T_be


def by_P_off2on_calculate_T_be(P_on, P_off, P_on2off, P_off2on, T_on2off, T_off2on):
    for i in P_off2on:
        # power and time consumed in each transmission
        T_tr = T_on2off + T_off2on
        P_tr = ((T_on2off * P_on2off) + (T_off2on * i)) / T_tr

        T_be: float = (
            T_tr + T_tr * ((P_tr - P_on) / (P_on - P_off)) if P_tr > P_on
            else T_tr
        )

        # print everything
        print(f"* POWER consumed when OFF: {P_off} mw")
        print(f"* POWER consumed when SWITCHING ON: {i} mw")
        print(f"* POWER consumed when SWITCHING OFF: {P_on2off} mw")
        print(f"* TIME passed when SWITCHING ON: {T_off2on} s")
        print(f"* TIME passed when SWITCHING OFF: {T_on2off} s")
        print(f"* TIME passed while transmitting: {T_tr} s")
        print(f"* POWER consumed while transmitting: {P_tr} mw")
        print(f'=> Final Event Break: {T_be}')
        print("************************************************")

    return T_be


def by_T_on2off_calculate_T_be(P_on, P_off, P_on2off, P_off2on, T_on2off, T_off2on):
    for i in T_on2off:
        # power and time consumed in each transmission
        T_tr = i + T_off2on
        P_tr = ((i * P_on2off) + (T_off2on * P_off2on)) / T_tr

        T_be: float = (
            T_tr + T_tr * ((P_tr - P_on) / (P_on - P_off)) if P_tr > P_on
            else T_tr
        )

        # print everything
        print(f"* POWER consumed when OFF: {P_off} mw")
        print(f"* POWER consumed when SWITCHING ON: {P_off2on} mw")
        print(f"* POWER consumed when SWITCHING OFF: {P_on2off} mw")
        print(f"* TIME passed when SWITCHING ON: {T_off2on} s")
        print(f"* TIME passed when SWITCHING OFF: {i} s")
        print(f"* TIME passed while transmitting: {T_tr} s")
        print(f"* POWER consumed while transmitting: {P_tr} mw")
        print(f'=> Final Event Break: {T_be}')
        print("************************************************")

    return T_be


def by_T_off2on_calculate_T_be(P_on, P_off, P_on2off, P_off2on, T_on2off, T_off2on):
    for i in T_off2on:
        # power and time consumed in each transmission
        T_tr = T_on2off + i
        P_tr = ((T_on2off * P_on2off) + (i * P_off2on)) / T_tr

        T_be: float = (
            T_tr + T_tr * ((P_tr - P_on) / (P_on - P_off)) if P_tr > P_on
            else T_tr
        )

        # print everything
        print(f"* POWER consumed when OFF: {P_off} mw")
        print(f"* POWER consumed when SWITCHING ON: {P_off2on} mw")
        print(f"* POWER consumed when SWITCHING OFF: {P_on2off} mw")
        print(f"* TIME passed when SWITCHING ON: {i} s")
        print(f"* TIME passed when SWITCHING OFF: {T_on2off} s")
        print(f"* TIME passed while transmitting: {T_tr} s")
        print(f"* POWER consumed while transmitting: {P_tr} mw")
        print(f'=> Final Event Break: {T_be}')
        print("************************************************")

    return T_be


def main():
    T_be_P_off = by_P_off_calculate_T_be(P_on, P_off, P_on2off[0], P_off2on[0],
                                         T_on2off[0], T_off2on[0])

    T_be_P_on2off = by_P_on2off_calculate_T_be(P_on, 0, P_on2off, P_off2on[0],
                                               T_on2off[0], T_off2on[0])

    T_be_P_off2on = by_P_off2on_calculate_T_be(P_on, 0, P_on2off[0], P_off2on,
                                               T_on2off[0], T_off2on[0])

    T_be_T_on2off = by_T_on2off_calculate_T_be(P_on, 0, P_on2off[0], P_off2on[0],
                                               T_on2off, T_off2on[0])

    T_be_T_off2on = by_T_off2on_calculate_T_be(P_on, 0, P_on2off[0], P_off2on[0],
                                               T_on2off[0], T_off2on)


main()
