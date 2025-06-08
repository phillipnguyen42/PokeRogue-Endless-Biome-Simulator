# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 12:07:31 2025

@author: Phillip
Dictionary of biomes and which biome they link to.
Inner list integer represents reciprocal of chance to travel to that biome (e.g. 3 => 1/3 chance)
"""
biome_links = {
    "TOWN": ["PLAINS"],
    "ABYSS": ["CAVE", ["SPACE", 2], ["WASTELAND", 2]],
    "BADLANDS": ["DESERT", "MOUNTAIN"],
    "BEACH": ["SEA", ["ISLAND", 2]],
    "CAVE": ["BADLANDS", "LAKE", ["LABORATORY", 2]],
    "CONSTRUCTION_SITE": ["POWER_PLANT", ["DOJO", 2]],
    "DESERT": ["RUINS", ["CONSTRUCTION_SITE", 2]],
    "DOJO": ["PLAINS", ["JUNGLE", 2], ["TEMPLE", 2]],
    "FACTORY": ["PLAINS", ["LABORATORY", 2]],
    "FAIRY_CAVE": ["ICE_CAVE", ["SPACE", 2]],
    "FOREST": ["JUNGLE", "MEADOW"],
    "GRASS": ["TALL_GRASS"],
    "GRAVEYARD": ["ABYSS"],
    "ICE_CAVE": ["SNOWY_FOREST"],
    "ISLAND": ["SEA"],
    "JUNGLE": ["TEMPLE"],
    "LABORATORY": ["CONSTRUCTION_SITE"],
    "LAKE": ["BEACH", "SWAMP", "CONSTRUCTION_SITE"],
    "MEADOW": ["PLAINS", "FAIRY_CAVE"],
    "METROPOLIS": ["SLUM"],
    "MOUNTAIN": ["VOLCANO", ["WASTELAND", 2], ["SPACE", 3]],
    "PLAINS": ["GRASS", "METROPOLIS", "LAKE"],
    "POWER_PLANT": ["FACTORY"],
    "RUINS": ["MOUNTAIN", ["FOREST", 2]],
    "SEA": ["SEABED", "ICE_CAVE"],
    "SEABED": ["CAVE", ["VOLCANO", 3]],
    "SLUM": ["CONSTRUCTION_SITE", ["SWAMP", 2]],
    "SNOWY_FOREST": ["FOREST", ["MOUNTAIN", 2], ["LAKE", 2]],
    "SPACE": ["RUINS"],
    "SWAMP": ["GRAVEYARD", "TALL_GRASS"],
    "TALL_GRASS": ["FOREST", "CAVE"],
    "TEMPLE": ["DESERT", ["SWAMP", 2], ["RUINS", 2]],
    "VOLCANO": ["BEACH", ["ICE_CAVE", 3]],
    "WASTELAND": ["BADLANDS"]
}
