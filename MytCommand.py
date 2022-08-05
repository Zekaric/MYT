###############################################################################
# file:       MytCommand
# author:     Robbert de Groot
# company:    Zekaric
# copyright:  2022, Zekaric
# 
# description:
# Web site commands.
#
# l        - switch from displaying the item list or the project list.
#
# p-[ID]   - hide project items
# p+[ID]   - show project items
# p0       - hide all project items.
# p1       - show all project items.
# pa[Name] - add a new project.
# pn[Name] - rename a project.
# pd[Desc] - add a description for the project.
# p=[ID]   - set the current project.
#
# ia[Desc] - add a new item to the current project.
# id[Desc] - edit a description.
# iP[ID]   - set the project id.
# ip[VAL]  - set the priority VAL = 1-6 or x - xxxxx
# ie[VAL]  - set the effort   VAL = 1-6 or x - xxxxx, inf
# is[VAL]  - set the state    VAL = WORK_TODO, WORK_IN_PROG
#                                   TEST_TODO, TEST_IN_PROG
#                                   DOC_TODO,  DOC_IN_PROG
#                                   REL_TODO,  REL_IN_PROG
#                                   ARCHIVE
# iS+      - progress the item state.
# iS-      - regress  the item state.
# i=[ID]   - set the current item
###############################################################################

###############################################################################
# imports:
###############################################################################
import cgi

from dataclasses import dataclass

import MytProj
import MytTast
import MytState

###############################################################################
# local
# constants
###############################################################################
@dataclass
class MYT_COMMAND:
   CMD             : str = 'cmd'

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
   
   VAL1            : str = 'x'
   VAL2            : str = 'xx'
   VAL3            : str = 'xxx'
   VAL4            : str = 'xxxx'
   VAL5            : str = 'xxxxx'
   VALI            : str = 'inf'
   
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
   
   if MYT_COMMAND.CMD not in form:
      return False

   commandFull = form.getvalue(MYT_COMMAND.CMD)

   return _Process(commandFull)

###############################################################################
# local 
# function
###############################################################################
###############################################################################
# Process the command string.
###############################################################################
def _Process(line: str) -> bool:
   
   command = line[0:1]
   rest    = line[1:]

   if   command == 'l':
      return _ProcessList(rest)

   elif command == 'i':
      return _ProcessTask(rest)

   elif command == 'p':
      return _ProcessProj(rest)

   # Unknown command
   return False

###############################################################################
# process the list command
###############################################################################
def _ProcessList(line: str) -> bool:

   MytState.SetIsShowingProjectList(!MytState.IsShowingProjectList())

   return MytState.FileStore();

###############################################################################
# Process the project command
###############################################################################
def _ProcessProj(line: str) -> bool:

   command = restFull[0:1]
   rest    = restFull[1:]

   # add a new project
   if   command == 'a':
      return _ProcessProjAdd(rest)

   elif command == '=':
      return _ProcessProjSet(rest)

   elif command == 'n':
      return _ProcessProjName(rest)

   elif command == 'd':
      return _ProcessProjDesc(rest)

   elif command == '-' or
        command == '+':
      return _ProcessProjVis(command, rest)

   elif command == '0' or
        command == '1':
      return _ProcessProjVisAll(command)

   # Unknow command
   return False


def _ProcessProjAdd(line: str) -> bool:

   # Create the new project.
   proj = MytProj.Create(-1, True, str, "")
   if proj == None:
      return False

   # Set the current project to be this new project.
   MytState.SetCurrentProjId(proj.GetId())

   # Append the new project to the project list.
   MytProjList._list.append(proj)
   # Sort the new project.
   MytProjList._list.sort()

   # Store the new changes.
   MytProjList.FileStore()
   MytState.FileStore()

   return True


def _ProcessProjName(line: str) -> bool:

   # Find the current project.
   proj = MytProjList.FindById(MytState.GetCurrentProjId())
   if proj == None:
      return False

   # Set the project description.
   proj.SetName(line)

   # Store the new changes.
   MytProjList.FileStore()

   return True


def _ProcessProjDesc(line: str) -> bool:

   # Find the current project.
   proj = MytProjList.FindById(MytState.GetCurrentProjId())
   if proj == None:
      return False

   # Set the project description.
   proj.SetDesc(line)

   # Store the new changes.
   MytProjList.FileStore()

   return True


def _ProcessProjSet(line: str) -> bool:

   # Get the id the user wants to set to.
   id = int(line)

   # Get the project if there exists a project with that id
   proj = MytProjList.FindById(id)
   if proj == None:
      return False

   # Set the project to be the current one.
   MytState.SetCurrentProjId(id)

   # Save the changes
   return MytState.FileStore()


def _ProcessProjVis(command: str, line: str) -> bool:

   # Get the id the user wants to set to.
   id = int(line)

   # Get the project if there exists a project with that id
   proj = MytProjList.FindById(id)
   if proj == None:
      return False

   # turn on/off the project's visibility
   proj.SetIsVis(command == '+')

   # Save the changes
   return MytProjList.FileStore()


def _ProcessProjVisAll(command: str) -> bool:

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
def _ProcessTask(line: str) -> bool:

   command = restFull[0:1]
   rest    = restFull[1:]
   
   if   command == 'a':
      return _ProcessTaskAdd(rest)

   elif command == '=':
      return _ProcessTaskSet(rest)

   elif command == 'd':
      return _ProcessTaskDesc(rest)

   elif command == 'P':
      return _ProcessTaskProjId(rest)

   elif command == 'p' or
        command == 'e' or
        command == 's':
      return _ProcessTaskAttribute(command, rest)

   elif command == 'S':
      return _ProcessTaskState(rest)

   return False


def _ProcessTaskAdd(line: str) -> bool:

   # Get the current project
   proj = MytProjList.FindById(MytState.GetCurrentProjId())
   if proj == None:
      return False

   # Get the new task.
   task = MytTask.Create(
      -1, 
      proj.GetId(), 
      MYT_COMMAND.STATE_WORK_TODO, 
      MYT_COMMAND.VAL1,
      MYT_COMMAND.VAL1,
      line)
   if task == None:
      return False

   # Add the task to the task list
   MytTaskList.Add(task)

   # Store the task list
   return MytTaskList.FileStore()


def _ProcessTaskSet(line: str) -> bool:

   # Get the id of the task
   id = int(str)

   # Find the task if it is there.
   task = MytTaskList.FindByid(id)
   if task == None:
      return False

   # Set the current task id.
   MytState.SetCurrentTaskId(id)

   # Save the changes
   return MytState.FileStore()


def _ProcessTaskDesc(line: str) -> bool:

   # Get the current task
   task = MytTaskList.FindById(MytState.GetCurrentTaskId())
   if task == None:
      return False

   # Change the description
   task.SetDesc(line)

   # Save the changes
   return MytTaskList.FileStore()


def _ProcessTaskProjId(line: str) -> bool:

   # what is the id.
   id = int(line)

   # Get the project if it exits.
   proj = MytProjList.FindById(id)
   if proj == None:
      return False

   # Get the current task
   task = MytTaskList.FindById(MytState.GetCurrentTaskId())
   if task == None:
      return False

   # Make the Change
   task.SetProjId(id)

   # Save the changes
   return MytTaskList.FileStore()


def _ProcessTaskAttribute(command: str, line: str) -> bool:

   # Get the current task
   task = MytTaskList.FindById(MytState.GetCurrentTaskId())
   if task == None:
      return False

   # Make the change
   if   command == 'p':
      task.SetPriority(line)
   elif command == 'e':
      task.SetEffort(line)
   elif command == 's':
      task.SetState(line)

   # Save the changes
   return MytTaskList.FileStore()


def _ProcessTaskState(line: str) -> bool:

   # Get the current task
   task = MytTaskList.FindById(MytState.GetCurrentTaskId())
   if task == None:
      return False

   # Make the change
   if   line == '-':
      task.SetState(line)
   elif line == '+':
      task.SetState(line)

   # Save the changes
   return MytTaskList.FileStore()
