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
from MytUtil import *

import os

import MytProj
import MytDisplay

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
   if (not os.path.exists(MYT_PROJLIST.FILE)):
      return False

   # Read in the file.
   fileContent: str
   file = open(MYT_PROJLIST.FILE, 'r')
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
      MytProjList._list.append(proj)

   # this should sort the list by name.
   MytProjList._list.sort()

   return True

###############################################################################
# Save the new project list.
###############################################################################
def FileStore() -> bool:

   # Open the file for writing
   file = open(MYT_PROJLIST.FILE, 'w')
   
   # For all projects...
   for proj in MytProjList._list:
   
      # Write the project information.
      file.write(str(proj))

   file.close()

   return True

###############################################################################
# Find a project given a project id.
###############################################################################
def FindById(id: int):

   # For all projects...
   for proj in MytProjList._list:

      # check if the ids match.
      if (id == proj.GetId()):
         return proj

   return None

###############################################################################
# Get the n'th project in the array
###############################################################################
def Get():
   return MytProjList._list

###############################################################################
# Get the n'th project in the array
###############################################################################
def GetAt(index: int):
   
   if (index < 0 or GetCount() <= index):
      return None

   return MytProjList._list[index]

###############################################################################
# Get the number of projects in the project list.
###############################################################################
def GetCount() -> int:
   return len(MytProjList._list)

###############################################################################
# Sort the list
###############################################################################
def Sort():
   
   MytProjList._list.sort()

###############################################################################
# Start the project list routines
###############################################################################
def Start() -> bool:
   return FileLoad()

