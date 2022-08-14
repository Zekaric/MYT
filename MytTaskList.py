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
from io import TextIOWrapper
import os

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
   _list: list[MytTask.MytTask] = []

   @classmethod
   def Append(cls, task: MytTask.MytTask) -> None:
      cls._list.append(task)

   @classmethod
   def GetAt(cls, index: int) -> MytTask.MytTask:
      return cls._list[index]

   @classmethod
   def GetCount(cls) -> int:
      return len(cls._list)

   @classmethod
   def Sort(cls) -> None:
      cls._list.sort()

   @classmethod
   def FileLoad(cls) -> bool:
      # No project list yet.
      if (not os.path.exists(MYT_TASKLIST.FILE)):
         return False

      # Read in the file.
      file: TextIOWrapper
      try:
         file = open(MYT_TASKLIST.FILE, 'r')
      except OSError:
         return False;

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
         cls._list.append(task)

      cls._list.sort()

      return True

   @classmethod
   def FileStore(cls) -> bool:
      # Open the file for writing
      file = None
      try:
         file = open(MYT_TASKLIST.FILE, 'w')
      except OSError:
         return False

      # For all tasks...
      for task in cls._list:

         # Write the project information.
         file.write(str(task))

      # clean up
      file.close()

      return True

   @classmethod
   def FindById(cls, id: int) -> MytTask.MytTask | None:
      
      # For all tasks...
      for task in cls._list:

         if (task.GetId() == id):
            return task
      
      return None

###############################################################################
# global
# function
###############################################################################
###############################################################################
# Add a new task
###############################################################################
def Add(task: MytTask.MytTask) -> None:
   MytTaskList.Append(task)
   MytTaskList.Sort()

###############################################################################
# Load in the tasks
###############################################################################
def FileLoad() -> bool:
   return MytTaskList.FileLoad()

###############################################################################
# Save the items
###############################################################################
def FileStore() -> bool:
   return MytTaskList.FileStore()

###############################################################################
# Find a task by its id
###############################################################################
def FindById(id: int) -> MytTask.MytTask | None:
   return MytTaskList.FindById(id)

###############################################################################
# Get the n'th task
###############################################################################
def GetAt(index: int) -> MytTask.MytTask:
   return MytTaskList.GetAt(index)

###############################################################################
# Get the size of the list.
###############################################################################
def GetCount() -> int:
   return MytTaskList.GetCount()

###############################################################################
# Start
###############################################################################
def Sort() -> None:
   MytTaskList.Sort()

###############################################################################
# Start
###############################################################################
def Start() -> bool:
   return MytTaskList.FileLoad()
