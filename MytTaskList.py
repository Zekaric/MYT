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
import os

from dataclasses import dataclass

import MytProj
import MytProjList
import MytTask

###############################################################################
# local
# constant
###############################################################################
@dataclass
class MYT_TASKLIST:
   FILE: str = 'MYT_tasklist.dat'

###############################################################################
# variable
###############################################################################
@dataclass
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
   if not os.path.exists(MYT_TASKLIST.FILE):
      return False

   # Read in the file.
   fileContent: str
   with open(MYT_TASKLIST.FILE, 'r') as file:
      fileContent = file.read()

   # For all lines in the file.
   for line in fileContent:

      # Append the task to the list.
      MytItemList._list.append(MytTask.CreateFromStr(line))

   MytItemList._list.sort()

   return True

###############################################################################
# Save the items
###############################################################################
def FileStore() -> bool:

   result = False

   # Open the file for writing
   with open(MYT_TASKLIST.FILE, 'w') as file:

      # For all projects...
      for task in MytTaskList._list:

         # Write the project information.
         file.write(str(task))

      result = True

   return result

###############################################################################
# Get the n'th task
###############################################################################
def GetAt(index: int):
   
   if index < 0 or GetCount() <= index:
      return None

   return MytItemList._list[index]

###############################################################################
# Get the size of the list.
###############################################################################
def GetCount() -> int:
   return len(MytItemList._list)

###############################################################################
# Start
###############################################################################
def Start() -> bool:
   return FileLoad()
