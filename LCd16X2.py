import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

lcd_columns, lcd_lines = 16, 2

pin_numbers = [
    board.D26,
    board.D19,
    board.D25,
    board.D24,
    board.D22,
    board.D27,
    board.D4,
]

pins = [digitalio.DigitalInOut(pin) for pin in pin_numbers]

lcd = characterlcd.Character_LCD_Mono(*pins, lcd_columns, lcd_lines)

lcd.message = "Hello world"
time.sleep(5)
lcd.clear()
