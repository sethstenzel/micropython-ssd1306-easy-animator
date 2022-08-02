from display_pbm import *
import time

hw_pin_scl, hw_pin_sda = (4 , 5)
i2c, lcd = setup_display(hw_pin_scl, hw_pin_sda)

# SINGLE IMAGE DEMO
display_image(lcd, "./img", "ash-pikachu.pbm", True, 3000)

# SLIDE SHOW DEMO
display_slide_show(lcd, "./img", ["mario-kart.pbm", "pokemon.pbm", "tetris.pbm", "three-starters.pbm"], True, 2000, 1)

# ANIMATION DEMO
display_animation(lcd, "./ani/mario_dance", True, 66, 23, 6, 1)
display_animation(lcd, "./ani/streetf", True, 33, 38, 15, 1)
display_animation(lcd, "./ani/yoshi_walk", True, 99,  5, 10, 1)


