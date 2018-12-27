
import os

def delpbms():
  file_list = []
  folder = ''
  try:
    folder = input('Enter a folder name. Leave blank for root.' +
                   '\nExample: animations/mario\n\n: ')
    file_list = os.listdir(folder)
  except:
    print('Directory not found...')
    
  for file in file_list:
    try:
      if '.pbm' in file:
        print('Deleting: ' + str(file))
        os.remove(str(folder)+'/'+str(file))
        print('Deleted: ' + str(file)) 
    except:
      print('Unable to delete file...')
 

