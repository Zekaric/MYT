###############################################################################
# file:       MytProjList
# author:     Robbert de Groot
# company:    Zekaric
# copyright:  2022, Zekaric
# 
# description:
# Project list handling.
###############################################################################

###############################################################################
# import
###############################################################################
from io import TextIOWrapper
from MytUtil import *

import os

import MytProj

###############################################################################
# local
# constant
###############################################################################
class MYT_PROJLIST:
   FILE: str = 'MYT_projlist.dat'

###############################################################################
# variable
###############################################################################
class MytProjList:
   _list: list[MytProj.MytProj] = []

   @classmethod
   def Append(cls, value: MytProj.MytProj) -> None:
      cls._list.append(value)

   @classmethod
   def GetAt(cls, index: int) -> MytProj.MytProj:
      return cls._list[index]

   @classmethod
   def GetCount(cls) -> int:
      return len(cls._list)

   @classmethod
   def FileLoad(cls) -> bool:
      # No project list yet.
      if (not os.path.exists(MYT_PROJLIST.FILE)):
         return False

      # Read in the file.
      file: TextIOWrapper
      try:
         file = open(MYT_PROJLIST.FILE, 'r')
      except OSError:
         return False

      fileContent = file.read()
      file.close()

      # For all lines in the file.
      lines       = fileContent.split('\n')
      fileContent = None
      for line in lines:

         # Convert the line into a project.
         proj = MytProj.CreateFromStr(line)
         if (proj is None):
            continue

         # Append the project to the list.
         cls._list.append(proj)

      # this should sort the list by name.
      cls._list.sort()

      return True

   @classmethod
   def FileStore(cls) -> bool:
      # Open the file for writing
      file: TextIOWrapper
      try:
         file = open(MYT_PROJLIST.FILE, 'w')
      except OSError:
         return False
      
      # For all projects...
      for proj in cls._list:

         # Write the project information.
         file.write(str(proj))

      file.close()

      return True

   @classmethod
   def FindById(cls, id: int) -> MytProj.MytProj | None:
      # For all projects...
      for proj in cls._list:

         # check if the ids match.
         if (id == proj.GetId()):
            return proj

      return None

   @classmethod
   def Sort(cls) -> None:
      return cls._list.sort()

###############################################################################
# global
# class
###############################################################################
###############################################################################
# Add a new project
###############################################################################
def Add(proj: MytProj.MytProj) -> None:
   
   MytProjList.Append(proj)
   MytProjList.Sort()

###############################################################################
# Load in the project list.
###############################################################################
def FileLoad() -> bool:
   return MytProjList.FileLoad()

###############################################################################
# Save the new project list.
###############################################################################
def FileStore() -> bool:
   return MytProjList.FileStore()

###############################################################################
# Find a project given a project id.
###############################################################################
def FindById(id: int) -> MytProj.MytProj | None:
   return MytProjList.FindById(id)

###############################################################################
# Get the n'th project in the array
###############################################################################
def GetAt(index: int) -> MytProj.MytProj:
   return MytProjList.GetAt(index)   

###############################################################################
# Get the number of projects in the project list.
###############################################################################
def GetCount() -> int:
   return MytProjList.GetCount()

###############################################################################
# Sort the list
###############################################################################
def Sort():
   return MytProjList.Sort()

###############################################################################
# Start the project list routines
###############################################################################
def Start() -> bool:
   return MytProjList.FileLoad()
