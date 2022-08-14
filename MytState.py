###############################################################################
# file:       MYT_state
# author:     Robbert de Groot
# company:    [company]
# copyright:  2022, Robbert de Groot
#
# description:
# Program state information
###############################################################################

###############################################################################
# imports:
###############################################################################
from MytUtil import *

import os

###############################################################################
# local
# constant
###############################################################################
class MYT_STATE:
   FILE                 : str = 'MYT_state.dat'
   CURR_ID_PROJ         : str = 'currIdProj'
   NEXT_ID_PROJ         : str = 'nextIdProj'
   NEXT_ID_TASK         : str = 'nextIdTask'
   IS_PROJ_LIST_VIS     : str = 'isProjListVis'
   IS_TASK_WORK_VIS     : str = 'isTaskWorkVis'
   IS_TASK_TEST_VIS     : str = 'isTaskTestVis'
   IS_TASK_DOC_VIS      : str = 'isTaskDocVis'
   IS_TASK_REL_VIS      : str = 'isTaskRelVis'
   IS_TASK_DONE_VIS     : str = 'isTaskDoneVis'

###############################################################################
# variable
###############################################################################
class MytState:
   _currIdProj          : int  = 0
   _nextIdProj          : int  = 1
   _nextIdTask          : int  = 1
   _isProjListVis       : bool = False
   _isTaskWorkVis       : bool = True
   _isTaskTestVis       : bool = True
   _isTaskDocVis        : bool = True
   _isTaskRelVis        : bool = True
   _isTaskDoneVis       : bool = True

   @classmethod
   def GetCurrIdProj(cls) -> int:
      return cls._currIdProj

   @classmethod
   def GetNextIdProj(cls) -> int:
      id = cls._nextIdProj
      cls._nextIdProj = cls._nextIdProj + 1
      cls.FileStore()
      return id

   @classmethod
   def GetNextIdTask(cls) -> int:
      id = cls._nextIdTask
      cls._nextIdTask = cls._nextIdTask + 1
      cls.FileStore()
      return id


   @classmethod
   def IsProjListVis(cls) -> bool:
      return cls._isProjListVis

   @classmethod
   def IsTaskWorkVis(cls) -> bool:
      return cls._isTaskWorkVis

   @classmethod
   def IsTaskTestVis(cls) -> bool:
      return cls._isTaskTestVis

   @classmethod
   def IsTaskDocVis(cls) -> bool:
      return cls._isTaskDocVis

   @classmethod
   def IsTaskRelVis(cls) -> bool:
      return cls._isTaskRelVis

   @classmethod
   def IsTaskDoneVis(cls) -> bool:
      return cls._isTaskDoneVis


   @classmethod
   def SetCurrIdProj(cls, value: int)  -> None:
      cls._currIdProj = value
      cls.FileStore()

   @classmethod
   def SetNextIdProj(   cls, value: int)  -> None:
      # Ensure we have the highest values.
      if (value >= cls._nextIdProj):
         cls._nextIdProj = value + 1
         cls.FileStore()

   @classmethod
   def SetNextIdTask(   cls, value: int)  -> None:
      # Ensure we have the highest values.
      if (value >= cls._nextIdTask):
         cls._nextIdTask = value + 1
         cls.FileStore()

   @classmethod
   def SetCurrProjIndex(cls, value: int) -> None:
      cls._currProjIndex = value
      cls.FileStore()

   @classmethod
   def SetIsProjListVis(cls, value: bool) -> None:
      cls._isProjListVis = value
      cls.FileStore()

   @classmethod
   def SetIsTaskWorkVis(cls, value: bool) -> None:
      cls._isTaskWorkVis = value
      cls.FileStore()

   @classmethod
   def SetIsTaskTestVis(cls, value: bool) -> None:
      cls._isTaskTestVis = value
      cls.FileStore()

   @classmethod
   def SetIsTaskDocVis( cls, value: bool) -> None:
      cls._isTaskDocVis  = value
      cls.FileStore()

   @classmethod
   def SetIsTaskRelVis( cls, value: bool) -> None:
      cls._isTaskRelVis  = value
      cls.FileStore()

   @classmethod
   def SetIsTaskDoneVis(cls, value: bool) -> None:
      cls._isTaskDoneVis = value
      cls.FileStore()

   @classmethod
   def FileLoad(cls)                      -> bool:
      # No project list yet.
      if (not os.path.exists(MYT_STATE.FILE)):
         return cls.FileStore()

      # Read in the file.
      try:
         file = open(MYT_STATE.FILE, 'r')
      except IOError:
         return False

      fileContent = file.read()
      file.close();

      # For all lines in the file.
      lines       = fileContent.split('\n')
      fileContent = None
      for line in lines:
         # Split the line
         part = line.split('\t')

         if   (part[0] == MYT_STATE.CURR_ID_PROJ):
            cls._currIdProj = IntFromStr(part[1])

         elif (part[0] == MYT_STATE.NEXT_ID_PROJ):
            cls._nextIdProj = IntFromStr(part[1])

         elif (part[0] == MYT_STATE.NEXT_ID_TASK):
            cls._nextIdTask = IntFromStr(part[1])

         elif (part[0] == MYT_STATE.IS_PROJ_LIST_VIS):
            cls._isProjListVis = BoolFromStr(part[1])

         elif (part[0] == MYT_STATE.IS_TASK_WORK_VIS):
            cls._isTaskWorkVis = BoolFromStr(part[1])

         elif (part[0] == MYT_STATE.IS_TASK_TEST_VIS):
            cls._isTaskTestVis = BoolFromStr(part[1])

         elif (part[0] == MYT_STATE.IS_TASK_DOC_VIS):
            cls._isTaskDocVis = BoolFromStr(part[1])

         elif (part[0] == MYT_STATE.IS_TASK_REL_VIS):
            cls._isTaskRelVis = BoolFromStr(part[1])

         elif (part[0] == MYT_STATE.IS_TASK_DONE_VIS):
            cls._isTaskDoneVis = BoolFromStr(part[1])

      return True

   @classmethod
   def FileStore(cls) -> bool:

      try:
         file = open(MYT_STATE.FILE, 'w')
      except IOError:
         return False

      file.write(MYT_STATE.CURR_ID_PROJ     + '\t' + StrFromInt( cls._currIdProj)    + '\n')
      file.write(MYT_STATE.NEXT_ID_PROJ     + '\t' + StrFromInt( cls._nextIdProj)    + '\n')
      file.write(MYT_STATE.NEXT_ID_TASK     + '\t' + StrFromInt( cls._nextIdTask)    + '\n')
      file.write(MYT_STATE.IS_PROJ_LIST_VIS + '\t' + StrFromBool(cls._isProjListVis) + '\n')
      file.write(MYT_STATE.IS_TASK_WORK_VIS + '\t' + StrFromBool(cls._isTaskWorkVis) + '\n')
      file.write(MYT_STATE.IS_TASK_TEST_VIS + '\t' + StrFromBool(cls._isTaskTestVis) + '\n')
      file.write(MYT_STATE.IS_TASK_DOC_VIS  + '\t' + StrFromBool(cls._isTaskDocVis)  + '\n')
      file.write(MYT_STATE.IS_TASK_REL_VIS  + '\t' + StrFromBool(cls._isTaskRelVis)  + '\n')
      file.write(MYT_STATE.IS_TASK_DONE_VIS + '\t' + StrFromBool(cls._isTaskDoneVis) + '\n')

      file.close()

      return True

###############################################################################
# global
# function
###############################################################################
###############################################################################
# Load in the data.
###############################################################################
def FileLoad() -> bool:
   return MytState.FileLoad()

###############################################################################
# Store the state data
###############################################################################
def FileStore() -> bool:
   return MytState.FileStore()

###############################################################################
# get the current project id
###############################################################################
def GetCurrIdProj() -> int:
   return MytState.GetCurrIdProj()

###############################################################################
# get the next project id
###############################################################################
def GetNextIdProj() -> int:
   return MytState.GetNextIdProj()

###############################################################################
# get the next task id
###############################################################################
def GetNextIdTask() -> int:
   return MytState.GetNextIdTask()

###############################################################################
# is the display showing the project list
###############################################################################
def IsProjListVis() -> bool:
   return MytState.IsProjListVis()

###############################################################################
# IsTaskDoneVis
###############################################################################
def IsTaskDoneVis() -> bool:
   return MytState.IsTaskDoneVis()

###############################################################################
# IsTaskDocVis
###############################################################################
def IsTaskDocVis() -> bool:
   return MytState.IsTaskDocVis()

###############################################################################
# IsTaskRelVis
###############################################################################
def IsTaskRelVis() -> bool:
   return MytState.IsTaskRelVis()

###############################################################################
# IsTaskTestVis
###############################################################################
def IsTaskTestVis() -> bool:
   return MytState.IsTaskTestVis()

###############################################################################
# IsTaskWorkVis
###############################################################################
def IsTaskWorkVis() -> bool:
   return MytState.IsTaskWorkVis()

###############################################################################
# set the current proj id
###############################################################################
def SetCurrIdProj(value: int) -> None:
   MytState.SetCurrIdProj(value)

###############################################################################
# set the next proj id
###############################################################################
def SetNextIdProj(value: int) -> None:
   MytState.SetNextIdProj(value)

###############################################################################
# set the next task id
###############################################################################
def SetNextIdTask(value: int) -> None:
   MytState.SetNextIdTask(value)

###############################################################################
# set the display to show the project list
###############################################################################
def SetIsProjListVis(value: bool) -> None:
   MytState.SetIsProjListVis(value)

###############################################################################
# SetIsTaskDoneVis
###############################################################################
def SetIsTaskDoneVis(value: bool) -> None:
   MytState.SetIsTaskDoneVis(value)

###############################################################################
# SetIsTaskDocVis
###############################################################################
def SetIsTaskDocVis(value: bool) -> None:
   MytState.SetIsTaskDocVis(value)

###############################################################################
# SetIsTaskRelVis
###############################################################################
def SetIsTaskRelVis(value: bool) -> None:
   MytState.SetIsTaskRelVis(value)

###############################################################################
# SetIsTaskTestVis
###############################################################################
def SetIsTaskTestVis(value: bool) -> None:
   MytState.SetIsTaskTestVis(value)

###############################################################################
# SetIsTaskWorkVis
###############################################################################
def SetIsTaskWorkVis(value: bool) -> None:
   MytState.SetIsTaskWorkVis(value)

###############################################################################
# Start up the status routines.
###############################################################################
def Start() -> bool:
   return FileLoad()
