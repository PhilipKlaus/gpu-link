from __future__ import annotations

from enum import Enum


class TemperatureThreshold(Enum):
    TEMPERATURE_THRESHOLD_SHUTDOWN = 0
    TEMPERATURE_THRESHOLD_SLOWDOWN = 1
    TEMPERATURE_THRESHOLD_MEM_MAX = 2
    TEMPERATURE_THRESHOLD_GPU_MAX = 3
    TEMPERATURE_THRESHOLD_ACOUSTIC_MIN = 4
    TEMPERATURE_THRESHOLD_ACOUSTIC_CURR = 5
    TEMPERATURE_THRESHOLD_ACOUSTIC_MAX = 6
    TEMPERATURE_THRESHOLD_COUNT = 7


class ClockId(Enum):
    CLOCK_ID_CURRENT = 0
    CLOCK_ID_APP_CLOCK_TARGET = 1
    CLOCK_ID_APP_CLOCK_DEFAULT = 2
    CLOCK_ID_CUSTOMER_BOOST_MAX = 3


class ClockType(Enum):
    CLOCK_GRAPHICS = 0
    CLOCK_SM = 1
    CLOCK_MEM = 2
    CLOCK_VIDEO = 3


class TemperatureSensorType(Enum):
    GPU = 0