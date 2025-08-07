# LED Control with On/Off Buttons (MicroPython)

This project controls an LED using two push buttons connected to a microcontroller (tested on ESP32) with pull-up resistors.

## Features
- Separate ON and OFF buttons
- Debouncing with small delay
- Uses MicroPython `machine` module

## Requirements
- ESP32 or similar board
- MicroPython firmware
- Two push buttons
- One LED + resistor

## Wiring
- Pin 23: ON button
- Pin 22: OFF button
- Pin 25: LED

## Run
Upload `main.py` to your board using Thonny or ampy.
