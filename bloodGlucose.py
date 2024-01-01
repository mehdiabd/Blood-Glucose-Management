import scipy.stats as stats

def normal_distribution(mean, std):
    return stats.norm.rvs(mean, std)

def blood_glucose_level(mean, std):
    blood_glucose_level = normal_distribution(mean, std)
    return blood_glucose_level


def simulate(mean, std, sim_cnt, n_idle, n_high, n_low, n_emergency):
    
    for _ in range(sim_cnt):
        pr = blood_glucose_level(mean, std)
        if pr >= 35 and pr < 75:
            n_low += 1
        elif pr >= 75 and pr < 131:
            n_idle += 1
        elif pr >= 131 and pr < 401:
            n_high += 1
        else:
            n_emergency += 1
    return n_idle, n_high, n_low, n_emergency


if __name__ == '__main__':
    mean = 110
    std = 50
    
    sim_cnt = 10000000
    # sim_cnt = 288
    # sim_cnt = 1440

    count_idle = 0
    count_high = 0
    count_low = 0
    count_emergency = 0
    
    n_idle, n_high, n_low, n_emergency = simulate(mean, std, sim_cnt, count_idle, count_high, count_low, count_emergency)
    print(f'pr_idle= {n_idle / sim_cnt}\tpr_high= {n_high / sim_cnt}\tpr_low= {n_low / sim_cnt}'
          f'\tpr_emergency= {n_emergency / sim_cnt}')
