# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2025 senseBox for senseBox
#
# SPDX-License-Identifier: Unlicense

import board
import busio
from digitalio import DigitalInOut, Direction

from vl53lxcx import (
    DATA_DISTANCE_MM,
    DATA_TARGET_STATUS,
    RESOLUTION_8X8,
    STATUS_VALID,
    VL53L8CX,
)

lpn_pin = board.D3
i2c = busio.I2C(board.SCL, board.SDA, frequency=1_000_000)

lpn = DigitalInOut(lpn_pin)
lpn.direction = Direction.OUTPUT
lpn.value = True

tof = VL53L8CX(i2c, lpn=lpn)


def main():
    tof.reset()

    if not tof.is_alive():
        raise ValueError("VL53L8CX not detected")

    tof.init()

    tof.resolution = RESOLUTION_8X8
    grid = 7

    tof.ranging_freq = 2

    tof.start_ranging({DATA_DISTANCE_MM, DATA_TARGET_STATUS})

    while True:
        if tof.check_data_ready():
            results = tof.get_ranging_data()
            distance = results.distance_mm
            status = results.target_status

            for i, d in enumerate(distance):
                if status[i] == STATUS_VALID:
                    print(f"{d:4}", end=" ")
                else:
                    print("xxxx", end=" ")

                if (i & grid) == grid:
                    print("")

            print("")


main()
