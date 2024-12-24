from matplotlib import pyplot as plt

from model import Model

DISTANCE = 1000
SHOTS = 40000
INC_ANGLE = 30
INC_ANGLE_DEV = 0.4
SPEED_DEV = 0.4

CHUNK = 100

TARGET_SIZE = 50

DENSITY_INTERVAL = 50
LEFT_INTERVAL = 400
RIGHT_INTERVAL = 1400

shots_list = Model.simulate_shots(distance=DISTANCE, inc_angle_exp_val=INC_ANGLE, inc_angle_std_dev=INC_ANGLE_DEV,
                                  speed_std_dev=SPEED_DEV,
                                  total_shots=SHOTS)

hit_probability = Model.calculate_hit_probability(shots_list=shots_list, distance=DISTANCE, total_shots=SHOTS,
                                                  target_size=TARGET_SIZE)
print(f"Target hit probability: {hit_probability}")

exp_vals = []
stat_disps = []
elem_chunks = []
Model.fill_lists_for_plot(shots_list=shots_list, total_shots=SHOTS, exp_vals=exp_vals, stat_disps=stat_disps,
                          elem_chunks=elem_chunks, chunk_size=CHUNK)

hit_density = Model.calculate_hit_density(shots_list=shots_list, total_shots=SHOTS,
                                          left_interval=LEFT_INTERVAL, right_interval=RIGHT_INTERVAL,
                                          interval_size=DENSITY_INTERVAL)

if len(elem_chunks) == len(exp_vals) == len(stat_disps):
    # plt.figure(figsize=(18, 8))

    # Expected val
    plt.figure(figsize=(12, 8))
    # plt.subplot(1, 3, 1)
    plt.plot(elem_chunks, exp_vals, marker='o', label='Expected Value', color='blue')
    plt.title('Expected Value vs Chunk Size')
    plt.xlabel('Chunk Size')
    plt.ylabel('Expected Value')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Statistical disp
    plt.figure(figsize=(12, 8))
    # plt.subplot(1, 3, 2)
    plt.plot(elem_chunks, stat_disps, marker='x', label='Statistical Dispersion', color='red')
    plt.title('Statistical Dispersion vs Chunk Size')
    plt.xlabel('Chunk Size')
    plt.ylabel('Statistical Dispersion')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Density histogram
    plt.figure(figsize=(12, 8))
    # plt.subplot(1, 3, 3)
    intervals = list(range(LEFT_INTERVAL, RIGHT_INTERVAL, DENSITY_INTERVAL))
    plt.bar(intervals, hit_density, width=DENSITY_INTERVAL, align='edge', edgecolor='black', alpha=0.7)
    plt.title('Hit Density Histogram')
    plt.xlabel('Intervals')
    plt.ylabel('Hit Density')
    plt.grid(True)

    plt.tight_layout()

    plt.show()
else:
    print("Error in arrs sizes")
