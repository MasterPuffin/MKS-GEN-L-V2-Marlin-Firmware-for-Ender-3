# MKS GEN L V2 Marlin Firmware for Ender 3
Marlin Firmware for Creality Ender 3 Printers with MKS GEN L V2.0 Board and TMC2209 Stepper Motors

# Content
The Marlin folder contains a current fork of the Marlin development branch, the changes from the original Ender 3 template and my changes to the files to make them work with the MKS GEN L V2.0 Board and TMC2209 Stepper Motors. If you want to make the changes yourself, see my changes listed below.

# Wiring
Use the schematic below to wire up your printer
![Schematic](https://github.com/MasterPuffin/MKS-GEN-L-V2-Marlin-Firmware-for-Ender-3/blob/master/Schematic.png?raw=true)

Place a jumper on the outlined pins to enable UART.

Connect the ribbon cable to EXT3 on your display. As you have to plug the put in reverse, you have to sand down the notch on the outside of the plug.

Place the cables from the endstops on the top and the bottom pin of each plug, so that the switch is connected to the 5V and D pin in [this schematic](https://github.com/makerbase-mks/MKS-GEN_L/blob/master/hardware/MKS%20Gen_L%20V2.0_001/MKS%20Gen_L%20V2.0_001%20PIN.pdf). You must use either jumper cables or resolder the plugs.

# Configuration changes
Make sure you copy first the Ender 3 Config Files (https://github.com/MarlinFirmware/Configurations) and then apply my changes

## Configuration.h

`//#define SHOW_CUSTOM_BOOTSCREEN`  
and  
`// #define CUSTOM_STATUS_SCREEN_IMAGE`

*(optional) Removes the custom boot logo and Logo on the status page*

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

---
`//#define EEPROM_SETTINGS`

*(optional) Disables the EEPROM as enabling it currently always shows an error message on the screen*

## Configuration_adv.h
`#define E0_AUTO_FAN_PIN 7`

*Sets the correct output for the fan, with will automatically enable when the hotend reaches 50° or more*

---
`#define HOMING_BUMP_MM      { 5, 5, 2 } `

*Replaces `X_HOME_BUMP_MM`, `Y_HOME_BUMP_MM` and `Z_HOME_BUMP_MM` as Marlin changed the variable name*
