# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 11:59:04 2025

@author: Phillip
Purpose of this script is to simulate and record PokeRogue Endless
biome frequencies.
"""

import random
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from biomes import biome_chance


def generate_next_biome(input_biome):
    """Return the name of the next biome given input of biome name."""
    biome_list = []
    chance_list = []
    for possible_biome, prob in biome_chance[input_biome]:
        biome_list.append(possible_biome)
        chance_list.append(prob)

    normalize_chance = [val / sum(chance_list) for val in chance_list]
    next_biome = np.random.choice(biome_list, p=normalize_chance)
    return next_biome


def generate_random_biome():
    """Return name of a random biome, not including TOWN."""
    possible_biomes = list(biome_chance.keys())
    possible_biomes.remove("TOWN")
    next_biome = possible_biomes[random.randrange(len(possible_biomes))]

    return next_biome


def simulate_biome_travel(num_biomes=1170, chart_bool=False):
    """
    Simulate traveling between biomes in Endless mode and record biomes.

    Steps through biomes and chooses next biome based on biome links and random
    chance. Every 10 biomes travels to a random biome. Writes biomes to a text
    log file. If chart_bool is true, creates and exports a chart based on the
    number of occurrences in text log file. Returns a sorted dictionary of
    biome counts. Current endless mode has 5850 waves or 1170 biomes.
    """
    with open("biome_log.txt", "w", encoding="utf8") as biome_log:
        current_biome = "TOWN"
        for biome_count in range(1, num_biomes + 1):
            biome_log.write(current_biome + "\n")
            if biome_count == 0:
                current_biome = generate_next_biome(current_biome)
            elif biome_count % 10 == 0:
                current_biome = generate_random_biome()
            else:
                current_biome = generate_next_biome(current_biome)

    with open("biome_log.txt", "r", encoding="utf8") as biome_log:
        biome_counter = Counter(biome_log.read().splitlines())
        sorted_biome_counter = dict(
            sorted(biome_counter.items(), key=lambda item: item[1])
        )

    if chart_bool:
        fig, ax = plt.subplots()
        y_pos = np.arange(len(list(sorted_biome_counter.keys())))
        ax.barh(y_pos, list(sorted_biome_counter.values()))
        ax.set_yticks(
            np.arange(len(list(sorted_biome_counter.keys()))),
            labels=sorted_biome_counter.keys(),
        )
        plt.yticks(fontsize=6)
        fig.savefig("Biomes.pdf", bbox_inches="tight")
        plt.show()

    return sorted_biome_counter


def calc_metropolis_percent():
    """
    Calculate percentage of biomes in the construction site loop.

    Calculates the percentage of biomes that are either Metropolis, Slum,
    Construction Site, Power Plant, Factory, and Laboratory compared to the
    total number of biomes in the biome_log.txt file.
    """
    with open("biome_log.txt", "r", encoding="utf8") as biome_log:
        biome_counter = Counter(biome_log.read().splitlines())

    metro_biomes = (
        biome_counter["METROPOLIS"]
        + biome_counter["SLUM"]
        + biome_counter["CONSTRUCTION_SITE"]
        + biome_counter["POWER_PLANT"]
        + biome_counter["FACTORY"]
        + biome_counter["LABORATORY"]
    )

    metro_percent = metro_biomes / sum(biome_counter.values())
    return metro_percent


def count_natural_spawns(target_biome, prior_biome_list=None):
    """
    Count the number of natural spawns of the target biome.

    Counts the number of times target_biome appears in the biome_log.txt and
    calculates how many of these occurrences are naturally chosen and how many
    are randomly selected. Optional input to look only for target_biome that
    naturally spawns after biomes in prior_biome_list.
    """
    with open("biome_log.txt", "r", encoding="utf8") as biome_txt:
        biome_log = biome_txt.read().splitlines()

    # Validates prior_biome_list
    if prior_biome_list:
        if not isinstance(prior_biome_list, list):
            return print("prior_biome_list not of type list.")

        for prior_biome in prior_biome_list:
            if not any(target_biome in sl for sl in biome_chance[prior_biome]):
                return print(
                    f"{prior_biome} not a valid prior biome of "
                    f"{target_biome}."
                )

    total_count = 0
    natural_count = 0
    for idx, biome in enumerate(biome_log):
        if biome == target_biome:
            total_count += 1
            if not idx % 10 == 0:  # checks if prior biome is a floor 50
                if prior_biome_list:
                    if biome_log[idx - 1] in prior_biome_list:
                        natural_count += 1
                else:
                    natural_count += 1

    if prior_biome_list:
        return print(
            f"{target_biome} appeared {total_count} times out of "
            f"{len(biome_log)} biomes. Of these, {natural_count} were"
            f" naturally occurring and directly followed the "
            f"{'biome' if len(prior_biome_list) == 1 else 'biomes'} "
            f" {prior_biome_list}."
        )

    return print(
        f"{target_biome} appeared {total_count} times out of "
        f"{len(biome_log)} biomes. Of these, {natural_count} were "
        f"naturally occurring."
    )


def identify_prior_biomes(target_biome):
    """Return a list of biomes that directly precede the target biome."""
    if target_biome not in biome_chance:
        return print(f"{target_biome} is not a valid biome.")

    prior_biomes = []
    for key, value in biome_chance.items():
        if any(target_biome in sl for sl in value):
            prior_biomes.append(key)

    return prior_biomes
