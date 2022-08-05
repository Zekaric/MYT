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
import cgi, cgitb

import MytProjList
import MytTaskList
import MytState
import MytCommand

###############################################################################
# The main program
###############################################################################
def Start():

   # ensure errors are shown to the web page.
   cgitb.enable()
   #cgitb.enable(display = 0, logdir = "/PythonScript.log")

   # create the classes.
   MytProjList.Start();
   MytTaskList.Start();
   MytState.Start();

   # Process the command 
   MytCommand.Process(cgi.FieldStorage())

   # Display the page
   #DisplayProcess()

   print("Content-Type: text/html\n\n")

   #print("<strong>Environment</strong></br>\n\n")
   #for param in os.environ.keys() :
   #   print("<strong>" + param + "</strong> : " + os.environ[param] + "</br>\n\n")
   
   # Form handing GET and POST
   #print("Getting Field Info </br>\n")
   #flist = cgi.FieldStorage();
   #
   #print("Getting Field Values </br>\n")
   #fname = flist.getvalue('fname')
   #lname = flist.getvalue('lname')
   #
   #print("First Name: " + fname + "</br>Last Name: " + lname + "\n")
