###############################################################################
# file:       MYT_main
# author:     Robbert de Groot
# company:    Zekaric
# copyright:  2022, Zekaric
#
# description:
#
###############################################################################

###############################################################################
# imports:
###############################################################################
from MytUtil import *

import cgi, cgitb

import MytState
import MytProjList
import MytTaskList
import MytCommand
import MytDisplay

###############################################################################
# The main program
###############################################################################
def Start():

   # ensure errors are shown to the web page.
   cgitb.enable()
   #cgitb.enable(display = 0, logdir = "/PythonScript.log")

   # create the classes.
   MytState.Start()
   MytProjList.Start()
   MytTaskList.Start()

   # Process the command
   MytCommand.Process(cgi.FieldStorage())

   # Display the page
   MytDisplay.Process()
