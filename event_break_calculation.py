import random as rnd
import matplotlib.pyplot as plt


def calculate_T_be() -> float:
    # declaring steps
    # step_off = 0.0005  # mw
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

    return T_tr, P_tr, T_be


T_tr_vals = []
P_tr_vals = []
T_be_vals = []

more_than_2h = []
less_than_4h = []


def main(no_of_run) -> float:
    T_tr, P_tr, T_be = calculate_T_be()
    if T_be < 14400:
        T_tr_vals.append(T_tr)
        P_tr_vals.append(P_tr)
        T_be_vals.append(T_be)

    less_than_4h.append(T_be) if T_be < 14400 else None
    more_than_2h.append(T_be) if T_be > 7200 else None

    print("************************************************")
    print(f'the End of Run Number {no_of_run + 1}')
    print(f'=> Final Event Break: {T_be}')
    print("************************************************")


number_of_runs = int(input("Please enter the number of runs you need: "))

for i in range(number_of_runs):
    main(i)
print('Runtiems Less than 4 Hours: ', less_than_4h)

print(f'Number of transmissions lasted Less than 4 Hours: {len(less_than_4h)}'
      f' (out of {number_of_runs}) -> '
      f'{len(less_than_4h) / number_of_runs * 100}%')

print(f'Number of transmissions lasted More than 2 Hours: {len(more_than_2h)}'
      f' (out of {number_of_runs}) -> '
      f'{len(more_than_2h) / number_of_runs * 100}%')

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(T_tr_vals, P_tr_vals, T_be_vals, c='blue', marker='o')
ax.set_xlabel('T_tr(s)')
ax.set_ylabel('P_tr(mw)')
ax.set_zlabel('T_be(s)')
ax.set_title('3D Scatter Plot of T_be Based on T_tr, P_tr')
plt.show()
