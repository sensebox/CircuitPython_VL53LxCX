# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2025 senseBox for senseBox
#
# SPDX-License-Identifier: MIT
"""
`vl53lxcx`
================================================================================

CircuitPython driver for VL53L5CX and VL53L8CX ToF sensors


* Author(s): senseBox

Implementation Notes
--------------------

**Hardware:**

* senseBox ToF Distance Sensor <https://sensebox.shop/product/time-of-flight-sensor>

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
* Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice

"""

# imports

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/sensebox/CircuitPython_VL53LxCX.git"


# Copyright (c) 2021 Mark Grosen <mark@grosen.org>
#
# SPDX-License-Identifier: MIT

from time import sleep

from adafruit_bus_device.i2c_device import I2CDevice

from src import VL53LxCX


class _VL53LxCX(VL53LxCX):
    def __init__(self, i2c, addr=0x29, lpn=None):
        """
        Initialize the sensor
        """
        self._buf = bytearray(3)
        self.dev = I2CDevice(i2c, addr)
        super().__init__(i2c, addr=addr, lpn=lpn)

    def _rd_byte(self, reg16):
        """
        Read a byte from the sensor
        """
        self._buf[0] = reg16 >> 8
        self._buf[1] = reg16 & 0xFF
        with self.dev:
            self.dev.write_then_readinto(self._buf, self._b1, out_start=0, out_end=2)

        return self._b1[0]

    def _rd_multi(self, reg16, size):
        """
        Read multiple bytes from the sensor
        """
        self._buf[0] = reg16 >> 8
        self._buf[1] = reg16 & 0xFF
        data = bytearray(size)
        with self.dev:
            self.dev.write_then_readinto(self._buf, data, out_start=0, out_end=2)

        return data

    def _wr_byte(self, reg16, val):
        """
        Write a byte to the sensor
        """
        self._buf[0] = reg16 >> 8
        self._buf[1] = reg16 & 0xFF
        self._buf[2] = val
        with self.dev:
            self.dev.write(self._buf)

    def _wr_multi(self, reg16, data):
        """
        Write multiple bytes to the sensor
        """
        buf = bytearray(2 + len(data))
        buf[0] = reg16 >> 8
        buf[1] = reg16 & 0xFF
        buf[2:] = data
        with self.dev:
            self.dev.write(buf)

    def reset(self):
        """
        Reset the sensor
        """
        if not self._lpn:
            raise ValueError("no LPN pin provided")

        self._lpn.value = False
        sleep(0.1)
        self._lpn.value = True
        sleep(0.1)


class VL53L5CX(_VL53LxCX):
    """
    CircuitPython driver for VL53L5CX ToF sensor
    """

    def __init__(self, i2c, addr=0x29, lpn=None):
        super().__init__(i2c, addr=addr, lpn=lpn)


class VL53L8CX(_VL53LxCX):
    """
    CircuitPython driver for VL53L8CX ToF sensor
    """

    def __init__(self, i2c, addr=0x29, lpn=None):
        super().__init__(i2c, addr=addr, lpn=lpn)
