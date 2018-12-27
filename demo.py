from machine import I2C, Pin
import ssd1306
import framebuf
import utime

def setup_display(hw_pin_scl, hw_pin_sda):
  i2c = I2C(scl=Pin(hw_pin_scl), sda=Pin(hw_pin_sda), freq=400000)
  lcd = ssd1306.SSD1306_I2C(128,64,i2c)
  return i2c, lcd
  
   
def display_animation(i2c, lcd, dir, inverted, disptime, framecount, duration, startframe):

  while startframe <= duration or duration < 0:
    for frame in range(1,framecount+1):
      framebuf_type = framebuf.MONO_HLSB
      with open(str(dir) + '/' + str(frame)+'.pbm', 'rb') as f:
        header_split = f.read().split(b'128 64\r')
        if len(header_split) < 2:
          header_split = header_split[0].split(b'128 64\n')
        data = bytearray(header_split[1])
      fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf_type)
      lcd.invert(inverted)
      lcd.blit(fbuf, 0, 0)
      lcd.show()
      utime.sleep_ms(disptime)
      startframe+=1
      
def display_image(i2c, lcd, directory, file, inverted):
  framebuf_type = framebuf.MONO_HLSB
  with open(str(directory) + '/' + file, 'rb') as f:
    header_split = f.read().split(b'128 64\r')
    if len(header_split) < 2:
      header_split = header_split[0].split(b'128 64\n')
    data = bytearray(header_split[1])
  fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf_type)
  lcd.invert(inverted)
  lcd.blit(fbuf, 0, 0)
  lcd.show()
  
def display_slide_show(i2c, lcd, dir, files, inverted, disptime, loops):
  counter = 0
  while loops < 0 or counter <= loops:
    for file in files:
      display_image(i2c, lcd, dir, file, inverted)
      utime.sleep_ms(disptime)
    if loops != -1:
      counter +=1








