#!/usr/bin/python

#---------------------------------------------------------------------#
# index.py                                                            #
#---------------------------------------------------------------------#
# indexes app model                                                   #
#---------------------------------------------------------------------#


#-------------------------------IMPORT--------------------------------#
import os
from app import *

class <#PREFIX#>_type(object):

  # Constructor
  def __init__(self):

    self.rows = []

    app = <#PREFIX#>_app()

    # calculate path to csv
    self.pth = os.path.join(app.csv,'index.csv')

    file = open(self.pth)

    lines = file.read().split('\n')

    file.close()

    for line in lines:

      if len(line) > 1:

        cells = line.split(',')

        cdecd = []

        for cell in cells:

          if '' in cell:
            cdecd.append(cell.replace('&#44;',','))
          else:
            cdecd.append(cell)

        self.rows.append(cdecd)


  # Save rows to disk
  def save(self):

    out = ''

    for row in rows:

      c = 1

      x = len(row)

      for cell in row:

        if ',' in cell:
          out += cell.replace(',','&#44;')
        else:
          out += cell

        if c < x:
          out += ','

        c += 1

      out += '\n'

    file = open(self.pth,'w')

    file.write(out)

    file.close()


#--------------------------------MAIN---------------------------------#
def main():
  x = <#PREFIX#>_index()


#-------------------------RUN AS EXECUTABLE---------------------------#
if __name__ == '__main__':
  main()


#-------------------------------EXPORT--------------------------------#
__all__ = ['<#PREFIX#>_index']
