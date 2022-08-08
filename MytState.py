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
   CURR_TASK_ID         : str = 'currTaskId'
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
   _currTaskId          : int  = 0
   _currTaskIndex       : int  = 0
   _isShowingProjList   : bool = False
   _isShowingTaskWork   : bool = True
   _isShowingTaskTest   : bool = True
   _isShowingTaskDoc    : bool = True
   _isShowingTaskRel    : bool = True
   _isShowingTaskDone   : bool = True

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

      pindex = 0

      if   (part[0] == MYT_STATE.CURR_TASK_ID):
         MytState._currTaskId          = IntFromStr( part[1])
         
      elif (part[0] == MYT_STATE.CURR_PROJ_ID):
         MytState._currProjId          = IntFromStr( part[1])

      elif (part[0] == MYT_STATE.IS_SHOWING_PROJ_LIST):
         MytState._isShowingProjList   = BoolFromStr(part[1])

      elif (part[0] == MYT_STATE.IS_SHOWING_TASK_WORK):
         MytState._isShowingTaskWork   = BoolFromStr(part[1])

      elif (part[0] == MYT_STATE.IS_SHOWING_TASK_TEST):
         MytState._isShowingTaskTest   = BoolFromStr(part[1])

      elif (part[0] == MYT_STATE.IS_SHOWING_TASK_DOC):
         MytState._isShowingTaskDoc    = BoolFromStr(part[1])

      elif (part[0] == MYT_STATE.IS_SHOWING_TASK_REL):
         MytState._isShowingTaskRel    = BoolFromStr(part[1])

      elif (part[0] == MYT_STATE.IS_SHOWING_TASK_DONE):
         MytState._isShowingTaskDone   = BoolFromStr(part[1])
   
   return True

###############################################################################
# Store the state data
###############################################################################
def FileStore() -> bool:
   
   file = open(MYT_STATE.FILE, 'w')

   file.write(MYT_STATE.CURR_TASK_ID         + '\t' + StrFromInt( MytState._currTaskId)        + '\n')
   file.write(MYT_STATE.CURR_PROJ_ID         + '\t' + StrFromInt( MytState._currProjId)        + '\n')
   file.write(MYT_STATE.IS_SHOWING_PROJ_LIST + '\t' + StrFromBool(MytState._isShowingProjList) + '\n')
   file.write(MYT_STATE.IS_SHOWING_TASK_WORK + '\t' + StrFromBool(MytState._isShowingTaskWork) + '\n')
   file.write(MYT_STATE.IS_SHOWING_TASK_TEST + '\t' + StrFromBool(MytState._isShowingTaskTest) + '\n')
   file.write(MYT_STATE.IS_SHOWING_TASK_DOC  + '\t' + StrFromBool(MytState._isShowingTaskDoc)  + '\n')
   file.write(MYT_STATE.IS_SHOWING_TASK_REL  + '\t' + StrFromBool(MytState._isShowingTaskRel)  + '\n')
   file.write(MYT_STATE.IS_SHOWING_TASK_DONE + '\t' + StrFromBool(MytState._isShowingTaskDone) + '\n')

   file.close()

   return True
   
###############################################################################
# get the current project id
###############################################################################
def GetCurrentProjId() -> int:
   return MytState._currProjId

###############################################################################
# Get current task id
###############################################################################
def GetCurrentTaskId() -> int:
   return MytState._currTaskId
   
###############################################################################
# is the display showing the project list
###############################################################################
def IsShowingProjList() -> bool:
   return MytState._isShowingProjList

###############################################################################
# IsShowingTaskDone
###############################################################################
def IsShowingTaskDone() -> bool:
   return MytState._isShowingTaskDone

###############################################################################
# IsShowingTaskDoc
###############################################################################
def IsShowingTaskDoc() -> bool:
   return MytState._isShowingTaskDoc

###############################################################################
# IsShowingTaskRel
###############################################################################
def IsShowingTaskRel() -> bool:
   return MytState._isShowingTaskRel

###############################################################################
# IsShowingTaskTest
###############################################################################
def IsShowingTaskTest() -> bool:
   return MytState._isShowingTaskTest

###############################################################################
# IsShowingTaskWork
###############################################################################
def IsShowingTaskWork() -> bool:
   return MytState._isShowingTaskWork

###############################################################################
# set the display to show the project list
###############################################################################
def SetIsShowingProjList(value: bool):
   MytState._isShowingProjList = value

###############################################################################
# SetIsShowingTaskDone
###############################################################################
def SetIsShowingTaskDone(value: bool):
   MytState._isShowingTaskDone = value

###############################################################################
# SetIsShowingTaskDoc
###############################################################################
def SetIsShowingTaskDoc(value: bool):
   MytState._isShowingTaskDoc = value

###############################################################################
# SetIsShowingTaskRel
###############################################################################
def SetIsShowingTaskRel(value: bool):
   MytState._isShowingTaskRel = value

###############################################################################
# SetIsShowingTaskTest
###############################################################################
def SetIsShowingTaskTest(value: bool):
   MytState._isShowingTaskTest = value

###############################################################################
# SetIsShowingTaskWork
###############################################################################
def SetIsShowingTaskWork(value: bool):
   MytState._isShowingTaskWork = value

###############################################################################
# set the current proj id
###############################################################################
def SetCurrentProjId(value: int):
   MytState._currProjId = value

###############################################################################
# set the current Task id
###############################################################################
def SetCurrentTaskId(value: int):
   MytState._currTaskId = value

###############################################################################
# Start up the status routines.
###############################################################################
def Start() -> bool:
   FileLoad()
