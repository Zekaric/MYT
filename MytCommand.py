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
# pc[ID]        - set the project to be current project.
#
# ta[ID] [Desc] - add a new item to the current project.
# td[ID] [Desc] - edit a description.
# tP[ID]        - set the project id.
# tp[ID] [VAL]  - set the priority VAL = 1, 2, 3, 4, 5, 6 
# te[ID] [VAL]  - set the effort   VAL = 1, 2, 3, 4, 5, 6, i
# ts[ID] [VAL]  - set the state    VAL = wt, wp, tt, tp, dt, dp, rt, rp, xx, n, p
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

###############################################################################
# local
# constants
###############################################################################
class COMMAND:
   CMD               : str = 'cmd'
   ID                : str = 'id'
   VALUE             : str = 'val'

   SEC_LIST          : str = 'l'
   SEC_PROJECT       : str = 'p'
   SEC_TASK          : str = 't'
   SEC_TASKTYPE      : str = 'd'

   PROJ_ADD          : str = 'a'
   PROJ_VIS          : str = 'v'
   PROJ_NAME         : str = 'n'
   PROJ_DESC         : str = 'd'
   PROJ_CURR         : str = 'c'
   PROJ_ALL_OFF      : str = '0'
   PROJ_ALL_ON       : str = '1'

   TASK_ADD          : str = 'a'
   TASK_DESC         : str = 'd'
   TASK_EFFORT       : str = 'e'
   TASK_PRIORITY     : str = 'p'
   TASK_PROJID       : str = 'P'
   TASK_STATE        : str = 's'

   TASK_STATE_NEXT   : str = 'n'
   TASK_STATE_PREV   : str = 'p'

   TYPE_WORK         : str = 'w'
   TYPE_TEST         : str = 't'
   TYPE_DOC          : str = 'd'
   TYPE_REL          : str = 'r'
   TYPE_DONE         : str = 'x'
   TYPE_ALL_OFF      : str = '0'
   TYPE_ALL_ON       : str = '1'

###############################################################################
# global
# function
###############################################################################
###############################################################################
# process the command.
###############################################################################
def Process(form: cgi.FieldStorage) -> bool:

   command = ""
   id      = 0
   value   = ""
   if (False):
      command = "tp"
      id      = 44
      value   = "5"

   if (COMMAND.CMD in form):
      command = form.getvalue(COMMAND.CMD)

   if (COMMAND.ID in form):
      id = IntFromStr(form.getvalue(COMMAND.ID))

   if (COMMAND.VALUE in form):
      value = form.getvalue(COMMAND.VALUE)

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

   if (command == COMMAND.SEC_LIST):
      return _ProcessList(rest, id, value)

   if (command == COMMAND.SEC_TASK):
      return _ProcessTask(rest, id, value)

   if (command == COMMAND.SEC_PROJECT):
      return _ProcessProj(rest, id, value)

   if (command == COMMAND.SEC_TASKTYPE):
      return _ProcessTaskType(rest)

   # Unknown command
   return False

###############################################################################
# process the list command
###############################################################################
def _ProcessList(line: str, id: int, value: str) -> bool:

   MytState.SetIsProjListVis(not MytState.IsProjListVis())

   return MytState.FileStore();

###############################################################################
# Process the project command
###############################################################################
def _ProcessProj(line: str, id: int, value: str) -> bool:

   command = line[0:1]
   rest    = line[1:]

   # add a new project
   if (command == COMMAND.PROJ_ADD):
      return _ProcessProjAdd(value)

   if (command == COMMAND.PROJ_NAME):
      return _ProcessProjName(id, value)

   if (command == COMMAND.PROJ_DESC):
      return _ProcessProjDesc(id, value)

   if (command == COMMAND.PROJ_CURR):
      return _ProcessProjCurr(id)

   if (command == COMMAND.PROJ_VIS):
      return _ProcessProjVis(id)

   if (command == COMMAND.PROJ_ALL_OFF):
      return _ProcessProjVisAll(False)
   
   if (command == COMMAND.PROJ_ALL_ON):
      return _ProcessProjVisAll(True)

   # Unknow command
   return False

###############################################################################
def _ProcessProjAdd(value: str) -> bool:

   # Create the new project.
   proj = MytProj.Create()

   # Set the current project to be this new project.
   MytState.SetCurrProjId(proj.GetId())

   # Append the new project to the project list.
   MytProjList.Add(proj)

   # Store the new changes.
   MytProjList.FileStore()
   MytState.FileStore()

   return True

###############################################################################
def _ProcessProjName(id: int, value: str) -> bool:

   proj: MytProj.MytProj | None

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
def _ProcessProjDesc(id: int, value: str) -> bool:

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
def _ProcessProjVis(id: int) -> bool:

   # Get the project if there exists a project with that id
   proj = MytProjList.FindById(id)
   if (proj is None):
      return False

   # turn on/off the project's visibility
   proj.SetIsVis(not proj.IsVis())

   # Save the changes
   return MytProjList.FileStore()

###############################################################################
def _ProcessProjVisAll(vis: bool) -> bool:

   count = MytProjList.GetCount()

   # for all projects...
   for index in range(count):
      
      # Get the project.
      proj = MytProjList.GetAt(index)

      # Set the visibility
      proj.SetIsVis(vis)

   # Save the changes
   return MytProjList.FileStore()

###############################################################################
# Process the task command
###############################################################################
def _ProcessTask(line: str, id: int, value: str) -> bool:

   command = line[0:1]
   rest    = line[1:]
   
   if   (command == COMMAND.TASK_ADD):
      return _ProcessTaskAdd(value)

   elif (command == COMMAND.TASK_DESC):
      return _ProcessTaskDesc(id, value)

   elif (command == COMMAND.TASK_PROJID):
      return _ProcessTaskProjId(id, value)

   elif (command == COMMAND.TASK_PRIORITY or
         command == COMMAND.TASK_EFFORT   or
         command == COMMAND.TASK_STATE):
      return _ProcessTaskAttribute(command, id, value)

   return False

###############################################################################
def _ProcessTaskAdd(value: str) -> bool:

   # Get the current project
   proj = MytProjList.FindById(MytState.GetCurrProjId())
   if (proj is None):
      return False

   # Get the new task.
   task = MytTask.Create(
      -1, 
      proj.GetId(), 
      MytTask.STATE.WORK_TODO, 
      MytTask.PRI.VAL1,
      MytTask.EFF.VAL1,
      value)
   if (task is None):
      return False

   # Add the task to the task list
   MytTaskList.Add(task)

   # Store the task list
   return MytTaskList.FileStore()

###############################################################################
def _ProcessTaskDesc(id: int, value: str) -> bool:

   # Get the current task
   task = MytTaskList.FindById(id)
   if (task is None):
      return False

   # Change the description
   task.SetDesc(value)

   # Save the changes
   return MytTaskList.FileStore()

###############################################################################
def _ProcessTaskProjId(id: int, value: str) -> bool:

   # Get the project if it exits.
   proj = MytProjList.FindById(int(value))
   if (proj is None):
      return False

   # Get the current task
   task = MytTaskList.FindById(id)
   if (task is None):
      return False

   # Make the Change
   task.SetProjId(proj.GetId())

   MytTaskList.Sort()

   # Save the changes
   return MytTaskList.FileStore()

###############################################################################
def _ProcessTaskAttribute(command: str, id: int, value: str) -> bool:

   # Get the current task
   task = MytTaskList.FindById(id)
   if (task is None):
      return False

   # Make the change
   if   (command == COMMAND.TASK_PRIORITY):
      task.SetPriority(value)

   elif (command == COMMAND.TASK_EFFORT):
      task.SetEffort(value)

   elif (command == COMMAND.TASK_STATE):
      if   (value == COMMAND.TASK_STATE_NEXT):
         task.SetState(MytTask.STATE.GetNextState(task.GetState()))
      elif (value == COMMAND.TASK_STATE_PREV):
         task.SetState(MytTask.STATE.GetPrevState(task.GetState()))
      else:
         task.SetState(value)

   MytTaskList.Sort()

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

###############################################################################
# Process the task command
###############################################################################
def _ProcessTaskType(line: str) -> bool:

   command = line[0:1]
   
   if   (command == COMMAND.TYPE_WORK):  MytState.SetIsTaskWorkVis(not MytState.IsTaskWorkVis())
   elif (command == COMMAND.TYPE_TEST):  MytState.SetIsTaskTestVis(not MytState.IsTaskTestVis())
   elif (command == COMMAND.TYPE_DOC):   MytState.SetIsTaskDocVis( not MytState.IsTaskDocVis())
   elif (command == COMMAND.TYPE_REL):   MytState.SetIsTaskRelVis( not MytState.IsTaskRelVis())
   elif (command == COMMAND.TYPE_DONE):  MytState.SetIsTaskDoneVis(not MytState.IsTaskDoneVis())
   elif (command == COMMAND.TYPE_ALL_OFF):
      # Turn everything off
      MytState.SetIsTaskWorkVis(False)
      MytState.SetIsTaskTestVis(False)
      MytState.SetIsTaskDocVis( False)
      MytState.SetIsTaskRelVis( False)
      MytState.SetIsTaskDoneVis(False)

   elif (command == COMMAND.TYPE_ALL_ON):
      # turn everything on
      MytState.SetIsTaskWorkVis(True)
      MytState.SetIsTaskTestVis(True)
      MytState.SetIsTaskDocVis( True)
      MytState.SetIsTaskRelVis( True)
      MytState.SetIsTaskDoneVis(True)

   MytState.FileStore()

   return True
