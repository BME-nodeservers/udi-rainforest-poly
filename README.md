
# Rainforest gateway

This is a node server to pull energy meter data from a Rainforest Eagle 200 gateway and make it
available to a [Universal Devices ISY994i](https://www.universal-devices.com/residential/ISY)
[Polyglot interface](http://www.universal-devices.com/developers/polyglot/docs/) with 
Polyglot V3 running on a [Polisy](https://www.universal-devices.com/product/polisy/)

(c) 2021 Robert Paauwe

## Installation

1. Backup Your ISY in case of problems!
   * Really, do the backup, please
2. Go to the Polyglot Store in the UI and install.
3. From the Polyglot dashboard, select the Rainforest Eagle 200 node server and configure (see configuration options below).
4. Once configured, the Rainforest Eagle 200 node server should update the ISY with the proper nodes and begin filling in the node data.
5. Restart the Admin Console so that it can properly display the new node server nodes.

### Node Settings
The settings for this node are:

#### Short Poll
   * How often to poll for current energy data (in seconds)
#### Long Poll
   * Not used
#### Custom Parameters
	* IP Address - IP address of Eagle 200 gateway
	* Cloud ID - Eagle 200 cloud id
	* Install Code - Eagle 200 install code

## Node substitution variables
### Controller node
 * sys.node.[address].ST      (Node sever online)
 * sys.node.[address].TWP     (Instetaneous power)
 * sys.node.[address].GV1     (Net power)



## Requirements
1. Polyglot V3.
2. ISY firmware 5.3.x or later

# Release Notes

- 1.0.0 05/26/2021
   - Initial version.
