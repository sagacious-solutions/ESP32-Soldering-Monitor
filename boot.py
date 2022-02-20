from machine import Pin, I2C
import lcd.python_lcd as python_lcd
import time

LCD_ADDRESS_FROM_SCAN = 39

i2c = I2C(1, scl=Pin(22), sda=Pin(21), freq=400000)

print(f"i2c addresses are {i2c.scan()}")


LCD_DISPLAY = python_lcd.I2cLcd(
    i2c=i2c, i2c_addr=LCD_ADDRESS_FROM_SCAN, num_lines=4, num_columns=20
)

for i in range(100):
    LCD_DISPLAY.clear()
    LCD_DISPLAY.putstr(f"Hello World : {i}")
    time.sleep(1)


# for i in range(5):
#     LCD_DISPLAY.hal_backlight_off()

#     time.sleep(2.5)

#     LCD_DISPLAY.hal_backlight_on()

#     time.sleep(2.5)
