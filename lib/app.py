#!/usr/bin/python

#---------------------------------------------------------------------#
# app.py                                                              #
#---------------------------------------------------------------------#
# stores application global classes, vars and functions               #
#---------------------------------------------------------------------#


#-------------------------------IMPORT--------------------------------#
import os

class <#PREFIX#>_app(object):

  def __init__(self):
  
    # calculate path to app
    self.pth = os.path.dirname(os.path.dirname(__file__))

    # append var
    self.var = os.path.join(self.pth,'var')

    # make sure we are not referencing empty path
    if not os.path.exists(self.var):
      os.makedirs(self.var)

    self.csv = os.path.join(self.var,'csv')

    # make sure we are not referencing empty path
    if not os.path.exists(self.csv):
      os.makedirs(self.csv)


#--------------------------------MAIN---------------------------------#
def main():
  a = <#PREFIX#>_app()
  print '<#PREFIX#> application path: {}'.format(a.pth)


#-------------------------RUN AS EXECUTABLE---------------------------#
if __name__ == '__main__':
  main()


#-------------------------------EXPORT--------------------------------#
__all__ = ['<#PREFIX#>_app']
