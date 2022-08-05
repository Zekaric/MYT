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
import os

from dataclasses import dataclass

import MytProj

###############################################################################
# local
# constant
###############################################################################
@dataclass
class MYT_PROJLIST:
   FILE: str = 'MYT_projlist.dat'

###############################################################################
# variable
###############################################################################
@dataclass 
class MytProjList:
   # array of MytProj.MytProj
   _list = []

###############################################################################
# global
# class
###############################################################################
###############################################################################
# Add a new project
###############################################################################
def Add(proj: MytProj.MytProj):
   
   MytProjList._list.append(proj)
   MytProjList._list.sort()

###############################################################################
# Load in the project list.
###############################################################################
def FileLoad() -> bool:
   
   # No project list yet.
   if not os.path.exists(MYT_PROJLIST.FILE):
      return False

   # Read in the file.
   fileContent: str
   with open(MYT_PROJLIST.FILE, 'r') as file:
      fileContent = file.read()

   # For all lines in the file.
   for line in fileContent:

      # Append the project to the list.
      MytProjList._list.append(MytProj.CreateFromStr(line))

   # this should sort the list by name.
   MytProjList._list.sort()

   return True

###############################################################################
# Save the new project list.
###############################################################################
def FileStore() -> bool:

   result = False

   # Open the file for writing
   with open(MYT_PROJLIST.FILE, 'w') as file:
   
      # For all projects...
      for proj in MytProjList._list:
   
         # Write the project information.
         file.write(str(proj))

      result = True

   return result

###############################################################################
# Find a project given a project id.
###############################################################################
def FindById(id: int):

   # For all projects...
   for proj in MytProjList._list:

      # check if the ids match.
      if id == proj.GetId():
         return proj

   return None

###############################################################################
# Get the n'th project in the array
###############################################################################
def GetAt(index: int):
   
   if index < 0 or GetCount() <= index:
      return None

   return MytProjList._list[index]

###############################################################################
# Get the number of projects in the project list.
###############################################################################
def GetCount() -> int:
   return len(MytProjList._list)

###############################################################################
# Start the project list routines
###############################################################################
def Start() -> bool:
   return FileLoad()

