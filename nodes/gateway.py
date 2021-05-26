#!/usr/bin/env python3
"""
Polyglot v3 node server Rainforest Eagle 200 gateway
Copyright (C) 2021 Robert Paauwe
"""

import udi_interface
import sys
import time
import eagle200-reader

LOGGER = udi_interface.LOGGER
Custom = udi_interface.Custom

class Controller(udi_interface.Node):
    id = 'controller'
    def __init__(self, polyglot, primary, address, name):
        super(Controller, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.name = name
        self.address = address
        self.primary = primary
        self.configured = False
        self.force = True
        self.eagle = None
        self.deviceList = []

        self.Parameters = Custom(polyglot, 'customparams')
        self.Notices = Custom(polyglot, 'notices')

        self.poly.subscribe(self.poly.CUSTOMPARAMS, self.parameterHandler)
        self.poly.subscribe(self.poly.START, self.start, self.address)
        self.poly.subscribe(self.poly.POLL, self.poll)

        self.poly.ready()
        self.poly.addNode(self)

    def query(self):
        if not self.configured:
            return

        i_demand = self.eagle.instantanous_demand()
        t_delivered = self.eagle.summation_delivered()
        t_received = self.eagle.summation_received()
        t_net = self.eagle.summation_total()

        LOGGER.info('data: {} {} {} {}'.format(i_demand, t_delviered, t_received, t_net))

        self.setDriver('TPW', i_demand, True, False)
        self.setDriver('GV1', t_net, True, True)


    # Process changes to customParameters
    def parameterHandler(self, params):
        self.configured = False
        self.Parameters.load(params)

        valid_i = False
        valid_u = False
        valid_p = False

        # How to detect that self.Parameters is empty?
        if len(self.Parameters) == 0:
            self.Notices['cfg'] = 'Enter username and password'
            return

        # Check for username and password
        self.Notices.clear()
        for p in self.Parameters:
            self.configured = True
            if p == 'IP Address' and self.Parameters[p] != '': 
                valid_i = True
            if p == 'Cloud ID' and self.Parameters[p] != '': 
                valid_u = True
            if p == 'Install Code' and self.Parameters[p] != '': 
                valid_p = True

        if not valid_i:
            self.configured = False
            self.Notices['cfg_i'] = 'Please enter a valid IP Address'

        if not valid_u:
            self.configured = False
            self.Notices['cfg_u'] = 'Please enter a valid Cloud ID'

        if not valid_p:
            self.configured = False
            self.Notices['cfg_p'] = 'Please enter a valid Install Code'

        if self.configured:
            self.eagle = eagle200-reader.EagleReader(
                    self.Parameters['IP Address'],
                    self.Parameters['Cloud ID'],
                    self.Parameters['Install Code'])

    def start(self):
        LOGGER.info('Starting node server')
        self.poly.updateProfile()
        self.poly.setCustomParamsDoc()

        if len(self.Parameters) == 0:
            self.Notices['cfg'] = 'Enter username and password'

        LOGGER.info('Node server started')

        if self.configured:
            self.query()
            self.query_day()

    def poll(self, poll):
        if poll == 'shortPoll':
            self.query()

    def delete(self):
        LOGGER.info('Removing node server')

    def stop(self):
        LOGGER.info('Stopping node server')

    commands = {
            'QUERY': query,
            }

    drivers = [
            {'driver': 'ST', 'value': 1, 'uom': 2},    # node server status
            {'driver': 'TPW', 'value': 0, 'uom': 33},  # power
            {'driver': 'GV1', 'value': 0, 'uom': 33},  # power
            ]

    
