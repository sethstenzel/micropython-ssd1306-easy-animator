from machine import I2C, Pin
import ssd1306
import framebuf
import utime

def setup_display(hw_pin_scl, hw_pin_sda):
  i2c = I2C(scl=Pin(hw_pin_scl), sda=Pin(hw_pin_sda), freq=400000)
  lcd = ssd1306.SSD1306_I2C(128,64,i2c)
  return i2c, lcd
  
   
def display_animation(lcd, dir, inverted, disptime, framecount, duration, startframe):
  """Displays and animation.

    Args:
        lcd: SSD1306_I2C        The ssd1306 lcd object.
        dir: str                Directory on the device animation files are in.
        inverted: bool          Inverts the black/white pbm file.
        disptime: int           How long each frame should display in ms.
        framecount: int         How many individual .pbm frames are in the directory.
        duration: int           How long the animation should play for.
        startframe: int         Frame to start the animation on.
    """

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

      
def display_image(lcd, dir, file, inverted, disptime):
  """Displays a Single Image.

  Args:
      lcd: SSD1306_I2C        The ssd1306 lcd object.
      dir: str                Directory on the device animation files are in.
      file: str               File to display.
      inverted: bool          Inverts the black/white pbm file.
      disptime: int           How long each frame should display in ms.
  """
  framebuf_type = framebuf.MONO_HLSB
  with open(str(dir) + '/' + file, 'rb') as f:
    header_split = f.read().split(b'128 64\r')
    if len(header_split) < 2:
      header_split = header_split[0].split(b'128 64\n')
    data = bytearray(header_split[1])
  fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf_type)
  lcd.invert(inverted)
  lcd.blit(fbuf, 0, 0)
  lcd.show()
  utime.sleep_ms(disptime)


  
def display_slide_show(lcd, dir, files, inverted, disptime, loops):
  """Displays a slide show of images.

  Args:
      lcd: SSD1306_I2C        The ssd1306 lcd object.
      dir: str                Directory on the device animation files are in.
      files: str              List of file names in the directory to show through.
      inverted: bool          Inverts the black/white pbm file.
      disptime: int           How long each slide should display in ms.
      loops: int              How many times the slideshow should loop. Set to -1 to loop forever.
  """
  counter = 0
  while loops < 0 or counter <= loops:
    for file in files:
      display_image(lcd, dir, file, inverted)
      utime.sleep_ms(disptime)
    if loops != -1:
      counter +=1








