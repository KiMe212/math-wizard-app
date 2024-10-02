import random

from app.config import config


def get_random_multiplier() -> int:
    return random.randint(*config.random_multiplier_range)


def get_random_delay() -> int:
    return random.randint(*config.random_delay_range)
