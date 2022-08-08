###############################################################################
# file:       MytCommand
# author:     Robbert de Groot
# company:    Zekaric
# copyright:  2022, Zekaric
# 
# description:
# Web site commands.
#
# l             - switch from displaying the item list or the project list.
#     
# dw            - toggle work visibility
# dt            - toggle test visibility
# dd            - toggle doc  visibility
# dr            - toggle rel  visibility
# dx            - toggle done visibility
#
# pv[ID]        - toggle visibility
# p0            - hide all project items.
# p1            - show all project items.
# pa[ID] [Name] - add a new project.
# pn[ID] [Name] - rename a project.
# pd[ID] [Desc] - add a description for the project.
#
# ta[ID] [Desc] - add a new item to the current project.
# td[ID] [Desc] - edit a description.
# tP[ID]        - set the project id.
# tp[ID] [VAL]  - set the priority VAL = 1, 2, 3, 4, 5, 6 
# te[ID] [VAL]  - set the effort   VAL = 1, 2, 3, 4, 5, 6, i
# ts[ID] [VAL]  - set the state    VAL = wt, wp, tt, tp, dt, dp, rt, rp, dn
# tS[ID] +      - progress the item state.
# tS[ID] -      - regress  the item state.
###############################################################################

###############################################################################
# imports:
###############################################################################
from MytUtil import *

import cgi

import MytProj
import MytProjList
import MytTask
import MytTaskList
import MytState
import MytDisplay

###############################################################################
# local
# constants
###############################################################################
class MYT_COMMAND:
   CMD             : str = 'cmd'
   ID              : str = 'id'
   VALUE           : str = 'val'

   CMD_LIST        : str = 'l'
   CMD_PROJECT     : str = 'p'
   CMD_ITEM        : str = 'i'
   
   SET             : str = '='
   PROGRESS        : str = '+'
   REGRESS         : str = '-'
   SHOW            : str = '+'
   HIDE            : str = '-'
   SHOW_ALL        : str = '1'
   HIDE_ALL        : str = '0'
   ADD             : str = 'a'
   PROJECT_ID      : str = 'P'
   PRIORITY        : str = 'p'
   EFFORT          : str = 'e'
   DESC            : str = 'd'
   STATE           : str = 's'
   
   VAL1            : str = '1'
   VAL2            : str = '2'
   VAL3            : str = '3'
   VAL4            : str = '4'
   VAL5            : str = '5'
   VALI            : str = 'i'
   
   STATE_WORK_TODO : str = 'wt'
   STATE_WORK_PROG : str = 'wp'
   STATE_TEST_TODO : str = 'tt'
   STATE_TEST_PROG : str = 'tp'
   STATE_DOC_TODO  : str = 'dt'
   STATE_DOC_PROG  : str = 'dp'
   STATE_REL_TODO  : str = 'rt'
   STATE_REL_PROG  : str = 'rp'
   STATE_ARCHIVE   : str = 'a'

###############################################################################
# global
# function
###############################################################################
###############################################################################
# process the command.
###############################################################################
def Process(form) -> bool:

   command = ""
   id      = 0
   value   = ""
   if (False):
      command = "l"
      id      = 0
      value   = ""

   if (MYT_COMMAND.CMD in form):
      command = form.getvalue(MYT_COMMAND.CMD)

   if (MYT_COMMAND.ID in form):
      id = IntFromStr(form.getvalue(MYT_COMMAND.ID))

   if (MYT_COMMAND.VALUE in form):
      value = form.getvalue(MYT_COMMAND.VALUE)

   return _Process(command, id, value)

###############################################################################
# local 
# function
###############################################################################
###############################################################################
# Process the command string.
###############################################################################
def _Process(line: str, id: int, value: str) -> bool:

   command = line[0:1]
   rest    = line[1:]

   if   (command == 'l'):
      return _ProcessList(rest, id, value)

   elif (command == 't'):
      return _ProcessTask(rest, id, value)

   elif (command == 'p'):
      return _ProcessProj(rest, id, value)

   # Unknown command
   return False

###############################################################################
# process the list command
###############################################################################
def _ProcessList(line: str, id: int, value: str) -> bool:

   MytState.SetIsShowingProjList(not MytState.IsShowingProjList())

   return MytState.FileStore();

###############################################################################
# Process the project command
###############################################################################
def _ProcessProj(line: str, id: int, value: str) -> bool:

   command = line[0:1]
   rest    = line[1:]

   # add a new project
   if   (command == 'a'):
      return _ProcessProjAdd(rest, id, value)

   elif (command == 'n'):
      return _ProcessProjName(rest, id, value)

   elif (command == 'd'):
      return _ProcessProjDesc(rest, id, value)

   elif (command == 'v'):
      return _ProcessProjVis(command, id, value)

   elif (command == '0' or
         command == '1'):
      return _ProcessProjVisAll(command, id, value)

   # Unknow command
   return False

###############################################################################
def _ProcessProjAdd(line: str, id: int, value: str) -> bool:

   # Create the new project.
   proj = MytProj.Create(-1, True, value, "")
   if (proj is None):
      return False

   # Set the current project to be this new project.
   MytState.SetCurrentProjId(proj.GetId())

   # Append the new project to the project list.
   MytProjList.Add(proj)

   # Store the new changes.
   MytProjList.FileStore()
   MytState.FileStore()

   return True

###############################################################################
def _ProcessProjName(line: str, id: int, value: str) -> bool:

   # Find the current project.
   proj = MytProjList.FindById(id)
   if (proj is None):
      return False

   # Set the project description.
   proj.SetName(value)

   # Sort the list.
   MytProjList.Sort()

   # Store the new changes.
   MytProjList.FileStore()

   return True

###############################################################################
def _ProcessProjDesc(line: str, id: int, value: str) -> bool:

   # Find the current project.
   proj = MytProjList.FindById(id)
   if (proj is None):
      return False

   # Set the project description.
   proj.SetDesc(value)

   # Store the new changes.
   MytProjList.FileStore()

   return True

###############################################################################
def _ProcessProjVis(command: str, id: int, value: str) -> bool:

   # Get the project if there exists a project with that id
   proj = MytProjList.FindById(id)
   if (proj is None):
      return False

   # turn on/off the project's visibility
   proj.SetIsVis(not proj.IsVis())

   # Save the changes
   return MytProjList.FileStore()

###############################################################################
def _ProcessProjVisAll(command: str, id: int, value: str) -> bool:

   count = MytProjList.GetCount()

   # for all projects...
   for index in range(count):
      
      # Get the project.
      proj = MytProjList.GetAt(index)

      # Set the visibility
      proj.SetIsVis(command == '1')

   # Save the changes
   return MytProjList.FileStore()

###############################################################################
# Process the task command
###############################################################################
def _ProcessTask(line: str, id: int, value: str) -> bool:

   command = line[0:1]
   rest    = line[1:]
   
   if   (command == 'a'):
      return _ProcessTaskAdd(rest, id, value)

   elif (command == 'd'):
      return _ProcessTaskDesc(rest, id, value)

   elif (command == 'P'):
      return _ProcessTaskProjId(rest, id, value)

   elif (command == 'p' or
         command == 'e' or
         command == 's'):
      return _ProcessTaskAttribute(command, id, value)

   elif (command == 'S'):
      return _ProcessTaskState(rest, id, value)

   return False

###############################################################################
def _ProcessTaskAdd(line: str, id: int, value: str) -> bool:

   # Get the current project
   proj = MytProjList.FindById(id)
   if (proj is None):
      return False

   # Get the new task.
   task = MytTask.Create(
      -1, 
      proj.GetId(), 
      MYT_COMMAND.STATE_WORK_TODO, 
      MYT_COMMAND.VAL1,
      MYT_COMMAND.VAL1,
      value)
   if (task is None):
      return False

   # Add the task to the task list
   MytTaskList.Add(task)

   # Store the task list
   return MytTaskList.FileStore()

###############################################################################
def _ProcessTaskDesc(line: str, id: int, value: str) -> bool:

   # Get the current task
   task = MytTaskList.FindById(id)
   if (task is None):
      return False

   # Change the description
   task.SetDesc(value)

   # Save the changes
   return MytTaskList.FileStore()

###############################################################################
def _ProcessTaskProjId(line: str, id: int, value: str) -> bool:

   # Get the project if it exits.
   proj = MytProjList.FindById(int(value))
   if (proj is None):
      return False

   # Get the current task
   task = MytTaskList.FindById(id)
   if (task is None):
      return False

   # Make the Change
   task.SetProjId(id)

   # Save the changes
   return MytTaskList.FileStore()

###############################################################################
def _ProcessTaskAttribute(command: str, id: int, value: str) -> bool:

   # Get the current task
   task = MytTaskList.FindById(id)
   if (task is None):
      return False

   # Make the change
   if   (command == 'p'):
      task.SetPriority(value)
   elif (command == 'e'):
      task.SetEffort(value)
   elif (command == 's'):
      task.SetState(value)

   # Save the changes
   return MytTaskList.FileStore()

###############################################################################
def _ProcessTaskState(line: str, id: int, value: str) -> bool:

   # Get the current task
   task = MytTaskList.FindById(id)
   if (task is None):
      return False

   # Make the change
   if   (line == 'p'):
      task.SetState(line)
   elif (line == 'n'):
      task.SetState(line)

   # Save the changes
   return MytTaskList.FileStore()
