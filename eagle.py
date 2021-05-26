#!/usr/bin/env python3
"""
Polyglot v3 node server Rainforest Eagle 200 gateway
Copyright (C) 2021 Robert Paauwe
"""

import udi_interface
import sys
import time
from nodes import gateway

LOGGER = udi_interface.LOGGER

if __name__ == "__main__":
    try:
        polyglot = udi_interface.Interface([gateway.Controller])
        polyglot.start()
        control = gateway.Controller(polyglot, "controller", "controller", "Eagle 200")
        polyglot.runForever()
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
        

