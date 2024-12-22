from model import Model

SHOTS = 5000
CHUNK = 100

hits_list = Model.simulate_shots(distance=1000, inc_angle_exp_val=30, inc_angle_std_dev=1, speed_std_dev=1, shots_qnty=SHOTS)

exp_vals = []
std_devs = []
elem_chunks = []

next_elems_chunk = CHUNK
for i in range(SHOTS):
    exp_vals[i] =
