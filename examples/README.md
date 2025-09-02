<!--
SPDX-FileCopyrightText: Copyright (c) 2025 senseBox for senseBox

SPDX-License-Identifier: MIT
-->

# VL53LxCX Examples

This folder contains example code for using the VL53LxCX CircuitPython library.

## Files

- `vl53lxcx_simpletest.py` - Basic example showing how to initialize and read data from VL53L5CX/VL53L8CX sensors

## Important Setup Requirements

Before running these examples, ensure you have:

1. **Installed the library**: Use `circup install vl53lxcx` or copy the library files manually
2. **Binary file requirement**: Copy the corresponding `.bin` file to the `/lib` folder on your CircuitPython device alongside the `.mpy` file. This binary file contains the required firmware for the sensors.

## Hardware Setup

The examples assume:

- I2C connection (SCL/SDA pins)
- LPN (Low Power) pin connected to D3 (configurable)
- VL53L5CX or VL53L8CX sensor properly wired

## Running the Examples

Simply copy the example file to your CircuitPython device and run it. The simple test example will:

- Initialize the sensor
- Set 8x8 resolution
- Start ranging measurements
- Display distance data in a grid format

Make sure your sensor is properly connected and the binary firmware file is in place before running the examples.
