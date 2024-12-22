from math import sqrt, sin, radians
from random import random

G_FORCE = 9.8
MAGIC_FOR_RANDN = 12
MAGIC2_FOR_RANDN = 6


class Model:

    @staticmethod
    def __simulate_shot_distance(speed: float, angle: float) -> float:
        return pow(speed, 2) * sin(2 * angle) / G_FORCE

    @staticmethod
    def __generate_rand(expected_value: float, standard_deviation: float) -> float:
        norm_rand = 0
        for i in range(MAGIC_FOR_RANDN):
            norm_rand += random()
        norm_rand -= MAGIC2_FOR_RANDN

        return expected_value + standard_deviation * norm_rand

    @staticmethod
    def simulate_shot(inc_angle_exp_val: float, distance: float, inc_angle_std_dev: float,
                      speed_std_dev: float, do_print: bool) -> float:
        speed_exp_value = sqrt((distance * G_FORCE) / sin(2 * radians(inc_angle_exp_val)))
        speed = Model.__generate_rand(speed_exp_value, speed_std_dev)
        if do_print:
            print(f"Current speed = {speed}")

        angle = Model.__generate_rand(inc_angle_exp_val, inc_angle_std_dev)
        if do_print:
            print(f"Current angle = {angle}")
        angle = radians(angle)
        if do_print:
            print(f"Current angle in radians = {angle}")

        return Model.__simulate_shot_distance(speed, angle)

    @staticmethod
    def simulate_shots(inc_angle_exp_val: float, distance: float, inc_angle_std_dev: float,
                       speed_std_dev: float, shots_qnty: int) -> list:
        hits_list = []
        for shots in range(shots_qnty):
            hits_list.append(
                Model.simulate_shot(distance=distance, inc_angle_exp_val=inc_angle_exp_val,
                                    inc_angle_std_dev=inc_angle_std_dev, speed_std_dev=speed_std_dev,
                                    do_print=False))
        return hits_list

    @staticmethod
    def calculate_exp_val(hits_list: list, hits_qnty: int):
        return sum(hits_list) / hits_qnty

    @staticmethod
    def calculate_stat_disp(hits_list: list, hits_qnty: int):

        exp_val = Model.calculate_exp_val(hits_list, hits_qnty)
        sqr_dif_sum = sum((x - exp_val) ** 2 for x in hits_list)
        return sqr_dif_sum / (hits_qnty - 1)
