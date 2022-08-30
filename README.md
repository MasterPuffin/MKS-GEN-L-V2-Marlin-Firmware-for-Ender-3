# MKS GEN L V2 Marlin Firmware for Ender 3
Marlin Firmware for Creality Ender 3 Printers with MKS GEN L V2.0 Board and TMC2209 Stepper Motors

The following guide is for use without a BLTouch. For more information about using one, please see [Using a BLTouch](#using-a-bltouch)

# Known issues
## :warning: Step miscount when using Octoprint
There is currently an issue when using Octoprint with the PSU Control plugin / supplying power to the stepper motors after boot. See the corresponding ticket at https://github.com/MarlinFirmware/Marlin/issues/17671.

## "Error EEPROM Ver." Message
Fix: Connect to the printer using [Printrun](https://www.pronterface.com/), [Octoprint](https://octoprint.org/) or similar. Send a `M502`, followed by an `M500` GCODE command via console to the printer to do a factory reset. This will get rid of the error message. Keep in mind that you have to reapply all previous settings such as Z-Offset, if you had any.

# Content
The Marlin folder contains a current fork of the Marlin branch, the changes from the original Ender 3 template and my changes to the files to make them work with the MKS GEN L V2.0 Board and TMC2209 Stepper Motors. If you want to make the changes yourself, see my changes listed below. 

Please copy the correct configuration file from the config folder (normal or for use with a BLTouch and ABL). There is also file with the [modified startup GCODE](https://github.com/MasterPuffin/MKS-GEN-L-V2-Marlin-Firmware-for-Ender-3/blob/BLTouch/cura_abl_settings.txt) for Cura.

# Wiring
Use the schematic below to wire up your printer
![Schematic](https://github.com/MasterPuffin/MKS-GEN-L-V2-Marlin-Firmware-for-Ender-3/blob/master/Schematic.png?raw=true)

Place a jumper on the outlined pins to enable UART.

Connect the ribbon cable to EXT3 on your display. As you have to plug the plug in reverse, you have to sand down the notch on the outside of the plug.

Place the cables from the endstops on the top and the bottom pin of each plug, so that the switch is connected to the 5V and D pin in [this schematic](https://github.com/makerbase-mks/MKS-GEN_L/blob/master/hardware/MKS%20Gen_L%20V2.0_001/MKS%20Gen_L%20V2.0_001%20PIN.pdf). You must use either jumper cables or resolder the plugs.

I made some adapter cables so that I could easily undo the changes in the future. In terms of plugs you are looking for JST connectors, 2.5mm XH 3-Pin. This is what my adapter looks like:
![Adapter](https://github.com/MasterPuffin/MKS-GEN-L-V2-Marlin-Firmware-for-Ender-3/blob/master/adapter_cable.jpg?raw=true)

# Configuration changes
Make sure you copy the Ender-3 config files first (https://github.com/MarlinFirmware/Configurations/tree/import-2.0.x/config/examples/Creality/Ender-3/CrealityV1) and then apply my changes

## Configuration.h

`//#define SHOW_CUSTOM_BOOTSCREEN`  
and  
`// #define CUSTOM_STATUS_SCREEN_IMAGE`

*(optional) Removes the custom boot logo and logo on the status page*

---
`#define MOTHERBOARD BOARD_MKS_GEN_L_V2`

*Defines the correct board*

---
```
#define X_MIN_ENDSTOP_INVERTING true
#define Y_MIN_ENDSTOP_INVERTING true
#define Z_MIN_ENDSTOP_INVERTING true
```

*Inverts the logic of the endstops*

---
```
#define X_DRIVER_TYPE  TMC2209
#define Y_DRIVER_TYPE  TMC2209
#define Z_DRIVER_TYPE  TMC2209
```  
and  
`#define E0_DRIVER_TYPE TMC2209`

*Enables support for TMC2209 in UART mode. Requires that UART jumper is set correctly. Set drivers to `TMC2209_STANDALONE` otherwise*


## Configuration_adv.h
`#define E0_AUTO_FAN_PIN 7`

*Sets the correct output for the fan, which will automatically enable when the hotend reaches 50° or more*

---
`#define HOMING_BUMP_MM      { 5, 5, 2 } `

*Only when using an older config file. Replaces `X_HOME_BUMP_MM`, `Y_HOME_BUMP_MM` and `Z_HOME_BUMP_MM` as Marlin changed the variable name*

# Using a BLTouch
## Mounting
Use [this thing](https://www.thingiverse.com/thing:3003725) from Thingiverse, it works great!

## Wiring
The metioned pins correspond to [this schematic](https://github.com/makerbase-mks/MKS-GEN_L/blob/master/hardware/MKS%20Gen_L%20V2.0_001/MKS%20Gen_L%20V2.0_001%20PIN.pdf).

The 3 wire plug goes on the D11 pin, orientate it in a way that the yellow cable is on the leftmost pin.

The 2 wire black and white cable goes to the green Z-min header, however unlike the normal endstops, the black cable goes on the middle plug (GND) and the white one on the lowermost one (D18).

## Firmware
Change the following parameters in addition to the changes above

### Configuration.h 

`#define BLTOUCH`

---

`#define NOZZLE_TO_PROBE_OFFSET { -41, -10, 0 }`

---

`#define PROBING_MARGIN 30`

---

`#define AUTO_BED_LEVELING_BILINEAR`

---

`#define Z_SAFE_HOMING`

---

`#define NUM_SERVOS 1`
