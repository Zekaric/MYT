###############################################################################
# file:       MytTaskList
# author:     Robbert de Groot
# company:    Zekaric
# copyright:  2022, Zekaric
# 
# description:
# Task list handling
###############################################################################

###############################################################################
# import
###############################################################################
from MytUtil import *

import os

import MytProj
import MytProjList
import MytTask

###############################################################################
# local
# constant
###############################################################################
class MYT_TASKLIST:
   FILE: str = 'MYT_tasklist.dat'

###############################################################################
# variable
###############################################################################
class MytTaskList:
   _list = []

###############################################################################
# global
# function
###############################################################################
###############################################################################
# Add a new task
###############################################################################
def Add(task: MytTask.MytTask):
   
   MytTaskList._list.append(task)

###############################################################################
# Load in the tasks
###############################################################################
def FileLoad() -> bool:

   # No project list yet.
   if (not os.path.exists(MYT_TASKLIST.FILE)):
      return False

   # Read in the file.
   fileContent: str
   file = open(MYT_TASKLIST.FILE, 'r')
   fileContent = file.read()
   file.close()

   # For all lines in the file.
   lines       = fileContent.split('\n')
   fileContent = None
   for line in lines:

      # Create the task from the line
      task = MytTask.CreateFromStr(line)
      if (task is None):
         continue

      # Append the task to the list.
      MytTaskList._list.append(task)

   MytTaskList._list.sort()

   return True

###############################################################################
# Save the items
###############################################################################
def FileStore() -> bool:

   # Open the file for writing
   file = open(MYT_TASKLIST.FILE, 'w')

   # For all projects...
   for task in MytTaskList._list:

      # Write the project information.
      file.write(str(task))

   file.close()

   return True

###############################################################################
# Get the n'th task
###############################################################################
def GetAt(index: int):
   
   if (index < 0 or GetCount() <= index):
      return None

   return MytTaskList._list[index]

###############################################################################
# Get the size of the list.
###############################################################################
def GetCount() -> int:
   return len(MytTaskList._list)

###############################################################################
# Start
###############################################################################
def Start() -> bool:
   return FileLoad()
