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
   CURR_PROJ_ID         : str = 'currProjId'
   IS_SHOWING_PROJ_LIST : str = 'isShowingProjList'
   IS_SHOWING_TASK_WORK : str = 'isShowingTaskWork'
   IS_SHOWING_TASK_TEST : str = 'isShowingTaskTest'
   IS_SHOWING_TASK_DOC  : str = 'isShowingTaskDoc'
   IS_SHOWING_TASK_REL  : str = 'isShowingTaskRel'
   IS_SHOWING_TASK_DONE : str = 'isShowingTaskDone'

###############################################################################
# variable
###############################################################################
class MytState:
   _currProjId          : int  = 0
   _currProjIndex       : int  = 0
   _isProjListVis       : bool = False
   _isTaskWorkVis       : bool = True
   _isTaskTestVis       : bool = True
   _isTaskDocVis        : bool = True
   _isTaskRelVis        : bool = True
   _isTaskDoneVis       : bool = True
   
   @classmethod
   def GetCurrProjId(   cls)              -> int:  return cls._currProjId

   @classmethod
   def GetCurrProjIndex(cls)              -> int:  return cls._currProjIndex

   @classmethod
   def IsProjListVis(   cls)              -> bool: return cls._isProjListVis

   @classmethod
   def IsTaskWorkVis(   cls)              -> bool: return cls._isTaskWorkVis

   @classmethod
   def IsTaskTestVis(   cls)              -> bool: return cls._isTaskTestVis

   @classmethod
   def IsTaskDocVis(    cls)              -> bool: return cls._isTaskDocVis

   @classmethod
   def IsTaskRelVis(    cls)              -> bool: return cls._isTaskRelVis

   @classmethod
   def IsTaskDoneVis(   cls)              -> bool: return cls._isTaskDoneVis

   @classmethod
   def SetCurrProjId(   cls, value: int)  -> None: cls._currProjId    = value

   @classmethod
   def SetCurrProjIndex(cls, value: int)  -> None: cls._currProjIndex = value

   @classmethod
   def SetIsProjListVis(cls, value: bool) -> None: cls._isProjListVis = value

   @classmethod
   def SetIsTaskWorkVis(cls, value: bool) -> None: cls._isTaskWorkVis = value

   @classmethod
   def SetIsTaskTestVis(cls, value: bool) -> None: cls._isTaskTestVis = value

   @classmethod
   def SetIsTaskDocVis( cls, value: bool) -> None: cls._isTaskDocVis  = value

   @classmethod
   def SetIsTaskRelVis( cls, value: bool) -> None: cls._isTaskRelVis  = value

   @classmethod
   def SetIsTaskDoneVis(cls, value: bool) -> None: cls._isTaskDoneVis = value

###############################################################################
# global 
# function
###############################################################################
###############################################################################
# Load in the data.
###############################################################################
def FileLoad() -> bool:
      
   # No project list yet.
   if (not os.path.exists(MYT_STATE.FILE)):
      return FileStore()

   # Read in the file.
   file = open(MYT_STATE.FILE, 'r')
   fileContent = file.read()
   file.close();

   # For all lines in the file.
   lines       = fileContent.split('\n')
   fileContent = None
   for line in lines:
      # Split the line
      part = line.split('\t')

      if   (part[0] == MYT_STATE.CURR_PROJ_ID):
         MytState.SetCurrProjId(IntFromStr(part[1]))

      elif (part[0] == MYT_STATE.IS_SHOWING_PROJ_LIST):
         MytState.SetIsProjListVis(BoolFromStr(part[1]))

      elif (part[0] == MYT_STATE.IS_SHOWING_TASK_WORK):
         MytState.SetIsTaskWorkVis(BoolFromStr(part[1]))

      elif (part[0] == MYT_STATE.IS_SHOWING_TASK_TEST):
         MytState.SetIsTaskTestVis(BoolFromStr(part[1]))

      elif (part[0] == MYT_STATE.IS_SHOWING_TASK_DOC):
         MytState.SetIsTaskDocVis(BoolFromStr(part[1]))

      elif (part[0] == MYT_STATE.IS_SHOWING_TASK_REL):
         MytState.SetIsTaskRelVis(BoolFromStr(part[1]))

      elif (part[0] == MYT_STATE.IS_SHOWING_TASK_DONE):
         MytState.SetIsTaskDoneVis(BoolFromStr(part[1]))
   
   return True

###############################################################################
# Store the state data
###############################################################################
def FileStore() -> bool:
   
   file = open(MYT_STATE.FILE, 'w')

   file.write(MYT_STATE.CURR_PROJ_ID         + '\t' + StrFromInt( MytState.GetCurrProjId()) + '\n')
   file.write(MYT_STATE.IS_SHOWING_PROJ_LIST + '\t' + StrFromBool(MytState.IsProjListVis()) + '\n')
   file.write(MYT_STATE.IS_SHOWING_TASK_WORK + '\t' + StrFromBool(MytState.IsTaskWorkVis()) + '\n')
   file.write(MYT_STATE.IS_SHOWING_TASK_TEST + '\t' + StrFromBool(MytState.IsTaskTestVis()) + '\n')
   file.write(MYT_STATE.IS_SHOWING_TASK_DOC  + '\t' + StrFromBool(MytState.IsTaskDocVis())  + '\n')
   file.write(MYT_STATE.IS_SHOWING_TASK_REL  + '\t' + StrFromBool(MytState.IsTaskRelVis())  + '\n')
   file.write(MYT_STATE.IS_SHOWING_TASK_DONE + '\t' + StrFromBool(MytState.IsTaskDoneVis()) + '\n')

   file.close()

   return True
   
###############################################################################
# get the current project id
###############################################################################
def GetCurrProjId() -> int:
   return MytState.GetCurrProjId()

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
# set the current proj id
###############################################################################
def SetCurrProjId(value: int) -> None:
   MytState.SetCurrProjId(value)

###############################################################################
# Start up the status routines.
###############################################################################
def Start() -> bool:
   return FileLoad()
