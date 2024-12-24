from math import sqrt, sin, radians
from random import random

G_FORCE = 9.8
MAGIC_FOR_RANDN = 12
MAGIC2_FOR_RANDN = 6


class Model:

    @staticmethod
    def __generate_rand(expected_value: float, standard_deviation: float) -> float:
        norm_rand = 0
        for i in range(MAGIC_FOR_RANDN):
            norm_rand += random()
        norm_rand -= MAGIC2_FOR_RANDN

        return expected_value + standard_deviation * norm_rand

    @staticmethod
    def single_shot(inc_angle_exp_val: float, distance: float, inc_angle_std_dev: float,
                    speed_std_dev: float, do_print: bool) -> float:
        speed_exp_value = sqrt((distance * G_FORCE) / sin(2 * radians(inc_angle_exp_val)))
        speed = Model.__generate_rand(speed_exp_value, speed_std_dev)

        angle = Model.__generate_rand(inc_angle_exp_val, inc_angle_std_dev)
        if do_print:
            print(f"Current angle = {angle}")
        angle = radians(angle)
        if do_print:
            print(f"Current angle in radians = {angle}")
            print(f"Current speed = {speed}")

        return pow(speed, 2) * sin(2 * angle) / G_FORCE

    @staticmethod
    def simulate_shots(inc_angle_exp_val: float, distance: float, inc_angle_std_dev: float,
                       speed_std_dev: float, total_shots: int) -> list:
        shots_list = []
        for shots in range(total_shots):
            shots_list.append(
                Model.single_shot(distance=distance, inc_angle_exp_val=inc_angle_exp_val,
                                  inc_angle_std_dev=inc_angle_std_dev, speed_std_dev=speed_std_dev,
                                  do_print=False))
        return shots_list

    @staticmethod
    def calculate_hit_probability(shots_list: list, total_shots: int, distance: float, target_size: float):
        left_target_interval = distance - target_size / 2
        right_target_interval = distance + target_size / 2
        hit_count = len([hit for hit in shots_list if left_target_interval <= hit <= right_target_interval])
        return hit_count / total_shots

    @staticmethod
    def calculate_exp_val(shots_list_chunk: list, total_shots_in_chunk: int):
        return sum(shots_list_chunk) / total_shots_in_chunk

    @staticmethod
    def calculate_stat_disp(shots_list_chunk: list, total_shots_in_chunk: int):

        exp_val = Model.calculate_exp_val(shots_list_chunk, total_shots_in_chunk)
        sqr_dif_sum = sum((x - exp_val) ** 2 for x in shots_list_chunk)
        return sqr_dif_sum / (total_shots_in_chunk - 1)

    @staticmethod
    def fill_lists_for_plot(shots_list: list, total_shots: int, exp_vals: list, stat_disps: list, elem_chunks: list,
                            chunk_size: int):
        next_elems_chunk = chunk_size
        while next_elems_chunk <= total_shots:
            exp_vals.append(Model.calculate_exp_val(shots_list[:next_elems_chunk], next_elems_chunk))
            stat_disps.append(Model.calculate_stat_disp(shots_list[:next_elems_chunk], next_elems_chunk))
            elem_chunks.append(next_elems_chunk)
            next_elems_chunk += chunk_size

    @staticmethod
    def calculate_hit_density(shots_list: list, total_shots: int, left_interval: int, right_interval: int,
                              interval_size: int) -> list:
        hits_in_intervals = []
        next_point = left_interval
        while next_point < right_interval:
            hits_in_intervals.append(
                len([hit for hit in shots_list if next_point <= hit < next_point + interval_size]) / total_shots)
            next_point += interval_size

        return hits_in_intervals
