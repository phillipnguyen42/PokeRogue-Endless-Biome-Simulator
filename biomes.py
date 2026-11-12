# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:01:56 2026

@author: Phillip
Dictionary of PokeRogue biomes and their connection probabilities.
Inner tuple represents name-probability pair.
Accurate as of v1.12.2.6
"""

biome_chance = {
    "TOWN": [("PLAINS", 1)],
    "ABYSS": [("CAVE", 0.58), ("SPACE", 0.21), ("WASTELAND", 0.21)],
    "BADLANDS": [("DESERT", 0.5), ("MOUNTAIN", 0.5)],
    "BEACH": [("SEA", 0.75), ("ISLAND", 0.25)],
    "CAVE": [("BADLANDS", 0.42), ("LAKE", 0.42), ("LABORATORY", 0.17)],
    "CONSTRUCTION_SITE": [("POWER_PLANT", 0.75), ("DOJO", 0.25)],
    "DESERT": [("ANCIENT_RUINS", 0.75), ("CONSTRUCTION_SITE", 0.25)],
    "DOJO": [("PLAINS", 0.58), ("JUNGLE", 0.21), ("TEMPLE", 0.21)],
    "FACTORY": [("PLAINS", 0.75), ("LABORATORY", 0.25)],
    "FAIRY_CAVE": [("ICE_CAVE", 0.75), ("SPACE", 0.25)],
    "FOREST": [("JUNGLE", 0.5), ("MEADOW", 0.5)],
    "GRASSY_FIELD": [("TALL_GRASS", 1)],
    "GRAVEYARD": [("ABYSS", 1)],
    "ICE_CAVE": [("SNOWY_FOREST", 1)],
    "ISLAND": [("SEA", 1)],
    "JUNGLE": [("TEMPLE", 1)],
    "LABORATORY": [("CONSTRUCTION_SITE", 0.5), ("ISLAND", 0.5)],
    "LAKE": [("BEACH", 0.33), ("SWAMP", 0.33), ("CONSTRUCTION_SITE", 0.33)],
    "MEADOW": [("PLAINS", 0.5), ("FAIRY_CAVE", 0.5)],
    "METROPOLIS": [("SLUM", 1)],
    "MOUNTAIN": [("VOLCANO", 0.64), ("WASTELAND", 0.22), ("SPACE", 0.14)],
    "PLAINS": [("GRASSY_FIELD", 0.33), ("METROPOLIS", 0.33), ("LAKE", 0.33)],
    "POWER_PLANT": [("FACTORY", 1)],
    "ANCIENT_RUINS": [("MOUNTAIN", 0.75), ("FOREST", 0.25)],
    "SEA": [("SEABED", 0.5), ("ICE_CAVE", 0.5)],
    "SEABED": [("CAVE", 0.83), ("VOLCANO", 0.17)],
    "SLUM": [("CONSTRUCTION_SITE", 0.75), ("SWAMP", 0.25)],
    "SNOWY_FOREST": [("FOREST", 0.58), ("MOUNTAIN", 0.21), ("LAKE", 0.21)],
    "SPACE": [("ANCIENT_RUINS", 1)],
    "SWAMP": [("GRAVEYARD", 0.5), ("TALL_GRASS", 0.5)],
    "TALL_GRASS": [("FOREST", 0.5), ("CAVE", 0.5)],
    "TEMPLE": [("DESERT", 0.58), ("SWAMP", 0.21), ("ANCIENT_RUINS", 0.21)],
    "VOLCANO": [("BEACH", 0.83), ("ICE_CAVE", 0.17)],
    "WASTELAND": [("BADLANDS", 1)],
}
