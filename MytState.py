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
import os
from enum        import Enum, auto

from dataclasses import dataclass

###############################################################################
# local
# constant
###############################################################################
@dataclass
class MYT_STATE:
   FILE                 : str = 'MYT_state.dat'
   CURR_ITEM            : str = 'currItem'
   CURR_PROJECT         : str = 'currProj'
   IS_SHOWING_PROJ_LIST : str = 'isShowingProjList'
   IS_SHOWING_TASK_WORK : str = 'isShowingTaskWork'
   IS_SHOWING_TASK_TEST : str = 'isShowingTaskTest'
   IS_SHOWING_TASK_DOC  : str = 'isShowingTaskDoc'
   IS_SHOWING_TASK_REL  : str = 'isShowingTaskRel'
   IS_SHOWING_TASK_ARC  : str = 'isShowingTaskArc'

###############################################################################
# variable
###############################################################################
@dataclass
class MytState:
   _currProjId          : int  = 0
   _currProjIndex       : int  = 0
   _currItemId          : int  = 0
   _currItemIndex       : int  = 0
   _isShowingProjList   : bool = False
   _isShowingTaskWork   : bool = True
   _isShowingTaskTest   : bool = True
   _isShowingTaskDoc    : bool = True
   _isShowingTaskRel    : bool = True
   _isShowingTaskArc    : bool = True

###############################################################################
# global 
# function
###############################################################################
###############################################################################
# Load in the data.
###############################################################################
def FileLoad() -> bool:
      
   # No project list yet.
   if not os.path.exists(MYT_STATE.FILE):
      return False

   # Read in the file.
   fileContent: str
   with open(MYT_STATE.FILE, 'r') as file:
      fileContent = file.read()

   # For all lines in the file.
   for line in fileContent:
      # Split the line
      part = line.split('\t')

      pindex = 0

      if   part[0] == MYT_STATE.CURR_ITEM_ID:
         MytState._currItemId          = int( part[1])
         
      elif part[0] == MYT_STATE.CURR_PROJ_ID:
         MytState._currProjId          = int( part[1])

      elif part[0] == MYT_STATE.IS_SHOWING_PROJ_LIST:
         MytState._isShowingProjList   = bool(part[1])

      elif part[0] == MYT_STATE.IS_SHOWING_TASK_WORK:
         MytState._isShowingTaskWork   = bool(part[1])

      elif part[0] == MYT_STATE.IS_SHOWING_TASK_TEST:
         MytState._isShowingTaskTest   = bool(part[1])

      elif part[0] == MYT_STATE.IS_SHOWING_TASK_DOC:
         MytState._isShowingTaskDoc    = bool(part[1])

      elif part[0] == MYT_STATE.IS_SHOWING_TASK_REL:
         MytState._isShowingTaskRel    = bool(part[1])

      elif part[0] == MYT_STATE.IS_SHOWING_TASK_ARC:
         MytState._isShowingTaskArc    = bool(part[1])
   
   return True

###############################################################################
# Store the state data
###############################################################################
def FileStore() -> bool:
   
   result = False
   
   # Open the file for writing
   with open(MYT_STATE.FILE, 'w') as file:

      file.write(MYT_STATE.CURR_ITEM_ID         + '\t' + MytState._currItemId        + '\n')
      file.write(MYT_STATE.CURR_PROJ_ID         + '\t' + MytState._currProjId        + '\n')
      file.write(MYT_STATE.IS_SHOWING_PROJ_LIST + '\t' + MytState._isShowingProjList + '\n')
      file.write(MYT_STATE.IS_SHOWING_TASK_WORK + '\t' + MytState._isShowingTaskWork + '\n')
      file.write(MYT_STATE.IS_SHOWING_TASK_TEST + '\t' + MytState._isShowingTaskTest + '\n')
      file.write(MYT_STATE.IS_SHOWING_TASK_DOC  + '\t' + MytState._isShowingTaskDoc  + '\n')
      file.write(MYT_STATE.IS_SHOWING_TASK_REL  + '\t' + MytState._isShowingTaskRel  + '\n')
      file.write(MYT_STATE.IS_SHOWING_TASK_ARC  + '\t' + MytState._isShowingTaskArc  + '\n')

      result = True

   return result
   
###############################################################################
# Get curr item id
###############################################################################
def GetCurrentItemId() -> int:
   return MytState._currItemId
   
###############################################################################
# get the current project id
###############################################################################
def GetCurrentProjId() -> int:
   return MytState._currProjId

###############################################################################
# is the display showing the project list
###############################################################################
def IsShowingProjList() -> bool:
   return MytState._isShowingProjList

###############################################################################
# IsShowingTaskArc
###############################################################################
def IsShowingTaskArc() -> bool:
   return MytState._isShowingTaskArc

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
# SetIsShowingTaskArc
###############################################################################
def SetIsShowingTaskArc(value: bool):
   MytState._isShowingTaskArc = value

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
# set the current item id
###############################################################################
def SetCurrentItemId(value: int):
   MytState._currItemId = value

###############################################################################
# set the current proj id
###############################################################################
def SetCurrentProjId(value: int):
   MytState._currProjId = value

###############################################################################
# Start up the status routines.
###############################################################################
def Start() -> bool:
   FileLoad();
   
