import random as rnd


def calculate_T_be() -> float:
    # declaring steps
    step_off = 0.0005  # mw
    step_P_tr = 0.05  # mw
    step_T_tr = 0.5  # s

    # declaring powers as variables
    P_on = 0.30
    # P_off = round(rnd.uniform(0.0001, 0.229) / step_off) * step_off
    P_off = 0
    P_off2on = round(rnd.uniform(0.1, 120) / step_P_tr) * step_P_tr
    P_on2off = round(rnd.uniform(0.1, 100) / step_P_tr) * step_P_tr

    # declaring times
    T_off2on = round(rnd.randint(30, 91) / step_T_tr) * step_T_tr
    T_on2off = round(rnd.randint(15, 61) / step_T_tr) * step_T_tr

    # power and time consumed in each transmission
    T_tr = T_on2off + T_off2on
    P_tr = ((T_on2off * P_on2off) + (T_off2on * P_off2on)) / T_tr

    T_be: float = (
        T_tr + T_tr * ((P_tr - P_on) / (P_on - P_off)) if P_tr > P_on else T_tr
    )

    # print everything
    print(f"* POWER consumed when OFF: {P_off} mw")
    print(f"* POWER consumed when SWITCHING ON: {P_off2on} mw")
    print(f"* POWER consumed when SWITCHING OFF: {P_on2off} mw")
    print(f"* TIME passed when SWITCHING ON: {T_off2on} s")
    print(f"* TIME passed when SWITCHING OFF: {T_on2off} s")
    print(f"* TIME passed while transmitting: {T_tr} s")
    print(f"* POWER consumed while transmitting: {P_tr} mw")

    return T_be

list_of_t = []

def main(no_of_run) -> float:
    T_be: float = calculate_T_be()
    list_of_t.append(T_be) if T_be > 7200 else None
    print("************************************************")
    print(f'the End of Run Number {no_of_run + 1}')
    print(f'=> Final Event Break: {T_be}')
    print("************************************************")


number_of_runs = int(input("Please enter the number of runs you need: "))

for i in range(number_of_runs):
    main(i)
print(list_of_t)
print(f'Number of transmissions lasted more than 7200 secs: {len(list_of_t)} '
      f'(out of {number_of_runs})')
