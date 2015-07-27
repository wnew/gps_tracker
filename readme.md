#Open GPS Tracker

##Description

Arduino based GPS vehicle tracker with python software to run on a server
for logging and display on google maps.

##Planned Features

1. TCP connection between server and tracker
2. GSM location estimation for when GPS not available
3. Interface the server to google maps and plot the position of the vehicle
4. Battery Backup

##Project State

Early days  
Design Phase almost complete  
about 10% complete  



#Requirements
##Hardware Requirements

1. Arduino Pro Mini, ideally 3v3 version, although any Arduino should do. (<$3 for the pro mini)
<p align="left">
<img src="https://cdn.sparkfun.com/assets/f/4/e/2/7/51eeb8f9ce395f0778000000.png" alt="alt text" width="150"height="150">
</p>
2. SIM800/SIM900/SIM908 GPRS Module/Shield (<$9 for the SIM800L)
<p align="left">
<img src="http://img.dxcdn.com/productimages/sku_382445_1.jpg" alt="alt text" width="150"height="150">
</p>
3. GPS Module, anything based on the UBlox NEO 6M ($12)
<p align="left">
<img src="http://www.digibay.in/image/cache/data/se/432-a-ublox-neo-6m-gps-module-with-active-antenna-600x600.jpg" alt="alt text" width="150"height="150">
</p>
4. 12v - 5v Buck Converter, at least 1Amp ($6)
<p align="left">
<img src="http://i01.i.aliimg.com/wsphoto/v0/500383839/DC-Buck-Converter-12V-24V-to-5V-8A-Step-Down-Car-Power-Supply-Waterproof-Module-090592.jpg" alt="alt text" width="150"height="150">
</p>
5. TP4056 Lithium Charger Module (<$3 for 10)
<p align="left">
<img src="http://i1235.photobucket.com/albums/ff428/sixty545/0TP4056board_zpsdb9ae434.jpg" alt="alt text" width="150"height="150">
</p>
6. 18650 3v7 Battery (<$4 or free from old laptop battery packs)
<p align="left">
<img src="http://i01.i.aliimg.com/photo/v0/344889611/Vector_Optics_18650_Rechargeable_Lithium_Battery.jpg" alt="alt text" width="200"height="150">
</p>
7. Single 18650 Battery holder(<$2 for 5)
<p align="left">
<img src="http://img.fasttechcdn.com/119/1191501/1191501-1.jpg" alt="alt text" width="250"height="150">
</p>
8. Sim Card
<p align="left">
<img src="http://www.diygadget.com/media/catalog/product/cache/3/image/9df78eab33525d08d6e5fb8d27136e95/i/p/iphone-activation-card-600.jpg" alt="alt text" width="150"height="150">
</p>
9. Server - with static IP

##Device Hardware

The arduino controls the device, it is connected via serial to both the GPS and GPRS modules. It reads the GPS data off the GPS module and sends it to the server via the GPRS connection.

##Power Supply

Power supply, must be able to supply 500mA at 3v7. It is recommended to use a 18650 Lithium Ion battery.
The battery can be charged with a TP4056 which has in input voltage of up to 8v. So a buck convert from 12-5v is recommended.


##Device Firmware

Control and configure GPS
Interface with server over GPRS TCP connection
Store a configuration which can be changed from the server-side.


##Server-Side Device Management Software

Connect to device
Receive data from the device
Send configuration to the device
Log all activity to files
Store a configuration file per device
Manage multiple devices


##Server-Side Mapping Software

Take the log file from the Device Manager and map it onto a map framework
A user must be able to browse to a particular address and see his device locations


##Interfaces

###Device to Server

- The server will listen for a TCP connection from the device.
- The device will send periodically send the location data to the server as it is configured.
- The server will store a configuration file and if requested to do so can send it to the device.


###Server Software to Mapping Software

This interface consists of a location log file produced by the server-side software managing the device. The mapping software takes this file, parses it and overlays it onto a mapping framework.











