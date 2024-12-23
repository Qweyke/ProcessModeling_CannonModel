from matplotlib import pyplot as plt

from model import Model

SHOTS = 50000
CHUNK = 100

hits_list = Model.simulate_shots(distance=1000, inc_angle_exp_val=45, inc_angle_std_dev=1, speed_std_dev=1,
                                 shots_qnty=SHOTS)
exp_vals = []
stat_disps = []
elem_chunks = []

next_elems_chunk = CHUNK
while next_elems_chunk <= SHOTS:
    exp_vals.append(Model.calculate_exp_val(hits_list[:next_elems_chunk], next_elems_chunk))
    stat_disps.append(Model.calculate_stat_disp(hits_list[:next_elems_chunk], next_elems_chunk))
    elem_chunks.append(next_elems_chunk)
    next_elems_chunk += CHUNK

if len(elem_chunks) == len(exp_vals) == len(stat_disps):

    plt.figure(figsize=(12, 6))  # window size

    plt.subplot(1, 2, 1)
    plt.plot(elem_chunks, exp_vals, marker='o', label='Expected Value', color='blue')
    plt.title('Expected Value vs Chunk Size')
    plt.xlabel('Chunk Size')
    plt.ylabel('Expected Value')
    plt.grid(True)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(elem_chunks, stat_disps, marker='x', label='Statistical Dispersion', color='red')
    plt.title('Statistical Dispersion vs Chunk Size')
    plt.xlabel('Chunk Size')
    plt.ylabel('Statistical Dispersion')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()
else:
    print("Error in arrs sizes")
