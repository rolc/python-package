#!/usr/bin/python

#---------------------------------------------------------------------#
# test.py                                                             #
#---------------------------------------------------------------------#
# test package functionality                                          #
#---------------------------------------------------------------------#


#-------------------------------IMPORT--------------------------------#
import os
import sys

pkg_pth = os.path.dirname(os.path.dirname(__file__))
sys.path.append(pkg_pth)

from lib import *


#--------------------------------MAIN---------------------------------#
def main():

  a = <#PREFIX#>_app()
  print a.__dict__

  x = <#PREFIX#>_index()
  print x.__dict__


#-------------------------RUN AS EXECUTABLE---------------------------#
if __name__ == '__main__':
  main()



