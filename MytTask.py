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
from MytUtil import *

import MytProj
import MytProjList

###############################################################################
# global
# class
###############################################################################
###############################################################################
# Constants
###############################################################################
class PRI:
   VAL1: str = "1"
   VAL2: str = "2"
   VAL3: str = "3"
   VAL4: str = "4"
   VAL5: str = "5"

class EFF:
   VAL1: str = "1"
   VAL2: str = "2"
   VAL3: str = "3"
   VAL4: str = "4"
   VAL5: str = "5"
   VALI: str = "i"

class STATE:
   WORK_TODO: str = "wt"
   WORK_PROG: str = "wp"
   TEST_TODO: str = "tt"
   TEST_PROG: str = "tp"
   DOC_TODO:  str = "dt"
   DOC_PROG:  str = "dp"
   REL_TODO:  str = "rt"
   REL_PROG:  str = "rp"
   DONE:      str = "xx"

   _list: list[str] = [ 
      WORK_TODO,
      WORK_PROG,
      TEST_TODO,
      TEST_PROG,
      DOC_TODO,
      DOC_PROG,
      REL_TODO,
      REL_PROG,
      DONE
   ]

   _listNice: list[str] = [
      "Work Todo",
      "Work In Progress",
      "Test Todo",
      "Test In Progress",
      "Doc Todo",
      "Doc In Progress",
      "Release Todo",
      "Release In Progress",
      "Done"
   ]

   @classmethod
   def IsLE(cls, vala: str, valb: str):
      return (STATE.IntFromSTATE(vala) <= STATE.IntFromSTATE(valb))

   @classmethod
   def IsLT(cls, vala: str, valb: str):
      return (STATE.IntFromSTATE(vala) < STATE.IntFromSTATE(valb))

   @classmethod
   def IntFromSTATE(cls, val: str):
      for index in range(len(cls._list)):
         if (val == cls._list[index]): return index
      return 0

   @classmethod
   def GetNiceName(cls, value: str) -> str:
      index = STATE.IntFromSTATE(value)
      return cls._listNice[index]

   @classmethod
   def GetNextState(cls, value: str) -> str:
      index = min(STATE.IntFromSTATE(value) + 1, len(cls._list) - 1)
      return cls._list[index]

   @classmethod
   def GetPrevState(cls, value: str) -> str:
      index = max(STATE.IntFromSTATE(value) - 1, 0)
      return cls._list[index]

###############################################################################
# Task Class
###############################################################################
class MytTask:

   _clsIdMax: int = 0

   def __init__(self, id: int, projId: int, state: str, priority: str, effort: str, desc: str):
      self._id:         int               = id
      self._projId:     int               = projId
      self._proj:       MytProj.MytProj   = MytProj.MytProj()
      self._state:      str               = state
      self._priority:   str               = priority
      self._effort:     str               = effort
      self._desc:       str               = desc

      if (id < 0):
         self._id = MytTask._clsIdMax
         MytTask._clsIdMax += 1

      else:
         if (MytTask._clsIdMax < id):
            MytTask._clsIdMax = id + 1

      # for convenience get the project name.
      proj = MytProjList.FindById(projId)
      if (proj is not None):
         self._proj = proj


   def __eq__(self, other: object) -> bool:
      if isinstance(other, MytTask):
         return self._id == other._id
      return NotImplemented

   def __ge__(self, other: object) -> bool:
      if isinstance(other, MytTask):
         
         return not (self < other)

      return NotImplemented

   def __gt__(self, other: object) -> bool:
      if isinstance(other, MytTask):

         return not (self <= other)

      return NotImplemented

   def __le__(self, other: object) -> bool:
      if isinstance(other, MytTask):

         if (self._projId != other._projId):
            return self._proj.GetName() <= other._proj.GetName()

         if (self._state != other._state):
            return STATE.IsLE(self._state, other._state)

         if (self._priority != other._priority):
            return self._priority > other._priority
         if (self._effort != other._effort):
            return self._effort > other._effort
         
         return self._id <= other._id

      return NotImplemented

   def __lt__(self, other: object) -> bool:
      if isinstance(other, MytTask):

         if (self._projId != other._projId):
            return self._proj.GetName() < other._proj.GetName()

         if (self._state != other._state):
            return STATE.IsLT(self._state, other._state)

         if (self._priority != other._priority):
            return self._priority >= other._priority
         if (self._effort != other._effort):
            return self._effort >= other._effort
         
         return self._id < other._id

      return NotImplemented

   def __ne__(self, other: object) -> bool:
      if isinstance(other, MytTask):

         return not (self == other)

      return NotImplemented

   def __str__(self) -> str:
      return "{id}\t{projId}\t{state}\t{pri}\t{eff}\t{desc}\n".format(
         id     = StrFromInt(self._id),
         projId = StrFromInt(self._projId),
         state  =            self._state,
         pri    =            self._priority,
         eff    =            self._effort,
         desc   =            self._desc)


   def GetId(self) -> int:
      return self._id

   def GetProjId(self) -> int:
      return self._projId

   def GetProj(self) -> MytProj.MytProj:
      return self._proj

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
      self._proj   = MytProj.MytProj()

      # for convenience get the project name.
      proj = MytProjList.FindById(value)
      if (proj is not None):
         self._proj = proj

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
def CreateFromStr(line: str) -> MytTask | None:

   # Split the line
   part = line.split('\t')

   # not enough parts, something wrong.
   if (len(part) < 6):
      return None

   # Get the values.
   id       = IntFromStr(part[0])
   projId   = IntFromStr(part[1])
   state    =            part[2]
   priority =            part[3]
   effort   =            part[4]
   desc     =            part[5]

   return Create(id, projId, state, priority, effort, desc)
