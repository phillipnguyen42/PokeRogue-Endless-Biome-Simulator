# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 17:06:28 2026

@author: Phillip
Purpose of these functions is to calculate probability of travelling to a
 target biome for each possible biome.
"""

from biomes import biome_chance
import pandas as pd


def travel_chance(
    start_biome, target_biome, current_prob, current_step, max_step_count
):
    """Returns the probability of going to a target biome given a starting
    biome and a number of steps to take."""
    running_sum = 0
    if start_biome == target_biome:
        return current_prob
    if current_step > max_step_count:
        return 0
    current_step += 1

    for possible_biome, next_prob in biome_chance[start_biome]:
        cumulative_prob = current_prob * next_prob
        running_sum += travel_chance(
            start_biome=possible_biome,
            target_biome=target_biome,
            current_prob=cumulative_prob,
            current_step=current_step,
            max_step_count=max_step_count,
        )
    return running_sum


def calc_all_biome_chance(target, max_step):
    """Returns the probability of going to a target biome starting from all
    possible biomes given a max_step_count."""
    biome_dict = {}
    for biome in biome_chance:
        prob = travel_chance(
            start_biome=biome,
            target_biome=target,
            current_prob=1,
            current_step=0,
            max_step_count=max_step,
        )
        biome_dict[biome] = round(prob, 3)

    df = pd.DataFrame(list(biome_dict.items()))
    return df


# calc_all_biome_chance("LAKE", 9)
