###############################################################################
# file:       MytTask
# author:     Robbert de Groot
# company:    Zekaric
# copyright:  2022, Zekaric
# 
# description:
# Item handling
###############################################################################

###############################################################################
# import
###############################################################################
import os

import MytProj
import MytProjList

###############################################################################
# global
# class
###############################################################################
###############################################################################
# Task Class
###############################################################################
class MytTask:

   _clsIdMax: int = 0

   def __init__(self, id: int, projId: int, state: str, priority: str, effort: str, desc: str):
      self._id        = id
      self._projId    = projId
      self._projName  = ""
      self._state     = state
      self._priority  = priority
      self._effort    = effort
      self._desc      = desc

      if id < 0:
         self._id = MytTask._clsIdMax
         MytTask._clsIdMax += 1

      else:
         if MytTask._clsIdMax < id:
            MytTask._clsIdMax = id + 1

      # for convenience get the project name.
      proj = MytProjList.FindById(projId)
      if proj != None:
         self._projName = proj.GetName()


   def __eq__(self, other):
      return self.id == other.id

   def __ge__(self, other):
      if self._projName != other._projName:
         return self._projName >= other._projName
      return self.id >= other.id

   def __gt__(self, other):
      if self._projName != other._projName:
         return self._projName > other._projName
      return self.id > other.id

   def __le__(self, other):
      if self._projName != other._projName:
         return self._projName <= other._projName
      return self.id <= other.id

   def __lt__(self, other):
      if self._projName != other._projName:
         return self._projName < other._projName
      return self.id < other.id

   def __ne__(self, other):
      return self.id != other.id

   def __str__(self):
      return f'{self._id}\t{item._projId}\t{item._state}\t{item._priority}\t{item._effort}\t{item._desc}\n'


   def GetId(self):
      return self._id

   def GetProjId(self):
      return self._projId

   def GetProjName(self):
      return self._projName

   def GetState(self):
      return self._state

   def GetPriority(self):
      return self._priority

   def GetEffort(self):
      return self._effort

   def GetDesc(self):
      return self._desc

   def SetProjId(self, value: int):
      self._projId = value

      # for convenience get the project name.
      proj = MytProjList.FindById(projId)
      if proj != None:
         self._projName = proj.GetName()

   def SetState(self, value: str):
      self._state = value

   def SetPriority(self, value: str):
      self._priority = value

   def SetEffort(self, value: str):
      self._effort = value

   def SetDesc(self, value: str):
      self._desc = value

###############################################################################
# global
# function
###############################################################################
###############################################################################
# Create a task from values
###############################################################################
def Create(id: int, projId: int, state: str, priority: str, effort: str, desc: str) -> MytTask:
   return MytTask(id, projId, state, priority, effort, desc)

###############################################################################
# Create a Task from a string definition
###############################################################################
def CreateFromStr(line: str) -> MytTask:

   # Split the line
   part = line.split('\t')

   # not enough parts, something wrong.
   if len(part) < 6:
      return None

   # Get the values.
   id       = int(part[0])
   projId   = int(part[1])
   state    =     part[2]
   priority =     part[3]
   effort   =     part[4]
   desc     =     part[5]

   return Create(id, projId, state, priority, effort, desc)
