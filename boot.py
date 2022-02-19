from machine import Pin, I2C
import python_lcd
import time

i2c = I2C(0)
i2c = I2C(1, scl=Pin(22), sda=Pin(21), freq=400000)

LCD_DISPLAY = python_lcd.I2cLcd()

for i in range(5):
    LCD_DISPLAY.hal_backlight_off()

    time.sleep(2.5)

    LCD_DISPLAY.hal_backlight_on()
