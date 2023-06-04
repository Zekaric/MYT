###############################################################################
# file:       MytDisplay
# author:     Robbert de Groot
# company:    Zekaric
# copyright:  2022, Zekaric
#
# description:
#
###############################################################################

###############################################################################
# imports:
###############################################################################
from MytUtil import *

import os
import cgi

import MytState
import MytProj
import MytProjList
import MytTask
import MytTaskList

###############################################################################
# local
# variable
###############################################################################
class MytDisplay:
   _command: str                       = ""
   _debug  : str                       = ""
   _form   : cgi.FieldStorage | None   = None

   @classmethod
   def GetCommand(cls)                          -> str:                       return cls._command
   @classmethod
   def GetDebug(  cls)                          -> str:                       return cls._debug
   @classmethod
   def GetForm(   cls)                          -> cgi.FieldStorage | None:   return cls._form
   @classmethod
   def SetCommand(cls, value: str)              -> None:                      cls._command   = value
   @classmethod
   def SetDebug(  cls, value: str)              -> None:                      cls._debug     = value
   @classmethod
   def SetForm(   cls, value: cgi.FieldStorage) -> None:                      cls._form      = value

###############################################################################
# global
# function
###############################################################################
###############################################################################
# Process the display
###############################################################################
def Process() -> str:

   value = """<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">

 <head>
  <meta charset="utf-8" />
  <link rel="stylesheet" type="text/css" href="style_reset.css">
  <link rel="stylesheet" type="text/css" href="style.css">
  <title>Zekaric:MYT</title>
 </head>

 <body>
"""

   if (MytState.IsProjListVis()):
      value += """
  <h1>Zekaric : MYT Projects</h1>
"""
      value += _DisplayProjList()
   else:
      value += """
  <h1>Zekaric : MYT Tasks</h1>
"""
      value += _DisplayTaskList()

   #DEBUG
   #_DisplayDebug()
   #_DisplayDebugForm()
   #_DisplayDebugCmd()
   #_DisplayDebugEnv()

   value += """
 </body>
</html>"""

   return value

###############################################################################
# Set the command that was to be processed
###############################################################################
def DebugAppend(line: str) -> None:
   MytDisplay.SetDebug(MytDisplay.GetDebug() + line + "</br>\n")

###############################################################################
# Set the command that was to be processed
###############################################################################
def DebugSetCommand(line: str) -> None:
   MytDisplay.SetCommand(line)

###############################################################################
# Set the command that was to be processed
###############################################################################
def DebugSetForm(form: cgi.FieldStorage) -> None:
   MytDisplay.SetForm(form)

###############################################################################
# local
# function
###############################################################################
###############################################################################
# Display the project list.
###############################################################################
def _DisplayProjList() -> str:

   value = """
  <table>
   <tbody>
    <tr>
     <td colspan=4>
      {goToTaskBtn}
      {hideAllBtn}
      {showAllBtn}
      {newProjFld}
     </td>
    </tr><tr>
     <th             ><nobr>Vis</nobr></th>
     <th             ><nobr>PID</nobr></th>
     <th             ><nobr>Project</nobr></th>
     <th class="fill"><nobr>Description</nobr></th>
    </tr>""".format(
       goToTaskBtn = _GetButtonCmd("l",  "Go To Tasks"),
       hideAllBtn  = _GetButtonCmd("p0", "{img} {img} {img}".format(img = _GetBit(StrFromBool(False)))),
       showAllBtn  = _GetButtonCmd("p1", "{img} {img} {img}".format(img = _GetBit(StrFromBool(True)))),
       newProjFld  = _GetInputCmdVal("pa", "New Project Name", 15))

   isAlt = False;
   projCount = MytProjList.GetCount()
   for index in range(projCount):

      proj: MytProj.MytProj = MytProjList.GetAt(index)

      itemp = proj.GetId()

      isVisValue = _GetLinkCmdId(    "pv", itemp, _GetBit(StrFromBool(proj.IsVis())))
      nameValue  = _GetInputCmdIdVal("pn", itemp, proj.GetName(), 15)
      descValue  = _GetInputCmdIdVal("pd", itemp, proj.GetDesc(), 200)

      value += """
    {tr}
     <td class="bool">{isVis}</td>
     <td class="num" >{id}</td>
     <td             >{name}</td>
     <td class="fill">{desc}</td>
    </tr>""".format(
      tr    = _GetTableRow(isAlt),
      id    = proj.GetId(),
      isVis = isVisValue,
      name  = nameValue,
      desc  = descValue)

      isAlt = not isAlt

   value += """
    </tr>
   </tbody>
  </table>
"""

   return value

###############################################################################
# Display the task list.
###############################################################################
def _DisplayTaskList() -> str:

   value = """
  <table>
   <tbody>
    <tr>
     <td colspan=4>
      {goToProjs}
     </td>
    </tr>
    <tr>
     <td                  >
      {stateVisList}
     </td>
     <td                  >
      {projVisList}
     </td>
     <td class="fillNoPad">
      {taskList}
     </td>
    </tr>
   </tbody>
  </table>
""".format(
      goToProjs    = _GetButtonCmd("l", "Go To Projects"),
      stateVisList = _DisplayTaskList_StateVisList(),
      projVisList  = _DisplayTaskList_ProjVisList(),
      taskList     = _DisplayTaskList_TaskList())

   return value

###############################################################################
def _DisplayTaskList_ProjVisList() -> str:

   str = """
      <table class="narrow">
       <tbody>
        <tr>
         <td colspan=4><nobr>
          {hideAllBtn}
          {showAllBtn}
         </nobr></td>
        </tr><tr>
         <th             ><nobr>Vis</nobr></th>
         <!--<th             ><nobr>PID</nobr></th>-->
         <th             ><nobr>Project</nobr></th>
        </tr>""".format(
      hideAllBtn  = _GetButtonCmd("p0", "{img} {img} {img}".format(img = _GetBit(StrFromBool(False)))),
      showAllBtn  = _GetButtonCmd("p1", "{img} {img} {img}".format(img = _GetBit(StrFromBool(True )))))

   isAlt     = False;
   projCount = MytProjList.GetCount()
   for index in range(projCount):

      proj:    MytProj.MytProj = MytProjList.GetAt(index)
      itemp:   int             = proj.GetId()

      isVisValue = _GetLinkCmdId("pv", itemp, _GetBit(StrFromBool(proj.IsVis())))
      nameValue  = proj.GetName()

      str = str + """
    {tr}
     <td class="bool">{isVis}</td>
     <!--<td class="num" >{id}</td>-->
     <td             >{name}</td>
    </tr>""".format(
      tr    = _GetTableRow(isAlt),
      id    = proj.GetId(),
      isVis = isVisValue,
      name  = nameValue)

      isAlt = not isAlt

   str = str + """
       </tbody>
      </table>
"""
   return str

###############################################################################
def _DisplayTaskList_StateVisList() -> str:
   return """
      <table class="narrow">
       <tbody>
        {trNrm}<td colspan=2><nobr>
          {hideAllBtn}
          {showAllBtn}
        </nobr></td></tr>
        {trNrm}<th>Vis</th><th><nobr>Task State</nobr></th></tr>
        {trNrm}<td>{wIsVis}</td><td>Work</td></tr>
        {trAlt}<td>{tIsVis}</td><td>Test</td></tr>
        {trNrm}<td>{dIsVis}</td><td>Doc </td></tr>
        {trAlt}<td>{rIsVis}</td><td>Rel </td></tr>
        {trNrm}<td>{xIsVis}</td><td>Done</td></tr>
       </tbody>
      </table>
""".format(
      trNrm      = _GetTableRow(False),
      trAlt      = _GetTableRow(True),
      hideAllBtn = _GetButtonCmd("d0", "{img} {img} {img}".format(img = _GetBit(StrFromBool(False)))),
      showAllBtn = _GetButtonCmd("d1", "{img} {img} {img}".format(img = _GetBit(StrFromBool(True)))),
      wIsVis     = _GetLinkCmd("dw", _GetBit(StrFromBool(MytState.IsTaskWorkVis()))),
      tIsVis     = _GetLinkCmd("dt", _GetBit(StrFromBool(MytState.IsTaskTestVis()))),
      dIsVis     = _GetLinkCmd("dd", _GetBit(StrFromBool(MytState.IsTaskDocVis()))),
      rIsVis     = _GetLinkCmd("dr", _GetBit(StrFromBool(MytState.IsTaskRelVis()))),
      xIsVis     = _GetLinkCmd("dx", _GetBit(StrFromBool(MytState.IsTaskDoneVis()))))

###############################################################################
def _DisplayTaskList_TaskList() -> str:

   newTaskPrjVal = ""
   newTaskFldVal = ""
   if (MytProjList.GetCount() != 0):
      newTaskPrjVal = _GetCurrProjPullDown()
      newTaskFldVal = _GetInputCmdVal("ta", "New Task", 100)

   str = """
      <table class="wide">
       <tbody>
        <tr>
         <td colspan=7>
          {newTaskPrj} {newTaskFld}
         </td>
        </tr>
        <tr>
          <th             >ID</th>
          <!--<th             >PID</th>-->
          <th             >Project</th>
          <th             >Status</th>
          <th             >Pri</th>
          <th             >Eff</th>
          <th class="fill">Description</th>
        </tr>
""".format(
      newTaskPrj = newTaskPrjVal,
      newTaskFld = newTaskFldVal)

   isAlt     = False
   taskCount = MytTaskList.GetCount()
   for index in range(taskCount):

      task: MytTask.MytTask = MytTaskList.GetAt(index)
      taskId                = task.GetId()

      state = task.GetState()
      if ((state == MytTask.STATE.WORK_TODO  or
           state == MytTask.STATE.WORK_PROG)    and
          not MytState.IsTaskWorkVis()):
         continue

      if ((state == MytTask.STATE.TEST_TODO  or
           state == MytTask.STATE.TEST_PROG)    and
          not MytState.IsTaskTestVis()):
         continue

      if ((state == MytTask.STATE.DOC_TODO   or
           state == MytTask.STATE.DOC_PROG)     and
          not MytState.IsTaskDocVis()):
         continue

      if ((state == MytTask.STATE.REL_TODO   or
           state == MytTask.STATE.REL_PROG)     and
          not MytState.IsTaskRelVis()):
         continue

      if (state == MytTask.STATE.DONE and not MytState.IsTaskDoneVis()):
         continue

      proj: MytProj.MytProj = task.GetProj()
      if (not proj.IsVis()):
         continue

      priVal = _GetDotGraph("tp", taskId, task.GetPriority(), False);
      effVal = _GetDotGraph("te", taskId, task.GetEffort(),   True);

      if (task.GetState() == MytTask.STATE.DONE):
         stateDoneVal = ""
      else:
         stateDoneVal = _GetButtonCmdIdVal("ts", taskId, "xx", "Done")

      projPullDown  = _GetTaskProjPullDown(      taskId, proj)
      statePullDown = _GetTaskTypePullDown("ts", taskId, task.GetState())

      descFld = _GetInputCmdIdVal("td", taskId, task.GetDesc(), 120)

      str = str + """
         {tr}
          <td class="num"      >{id}</td>
          <!--<td class="num"      >{projId}</td>-->
          <td            ><nobr>{projName}</nobr></td>
          <td            ><nobr>{statePrev}{stateNext} {state} {stateDone}</nobr></td>
          <td            ><nobr>{pri}</nobr></td>
          <td            ><nobr>{eff}</nobr></td>
          <td            ><nobr>{desc} {delVal}</nobr></td>
         </tr>
""".format(
      tr        = _GetTableRowTask(isAlt, task.GetState()),
      id        = taskId,
      projId    = proj.GetId(),
      projName  = projPullDown,
      statePrev = _GetButtonCmdIdVal("ts", taskId, "p",  "<"),
      stateNext = _GetButtonCmdIdVal("ts", taskId, "n",  ">"),
      stateDone = stateDoneVal,
      state     = statePullDown,
      pri       = priVal,
      eff       = effVal,
      desc      = descFld,
      delVal    = _GetButtonCmdId("tx", taskId, "X"))

      isAlt = not isAlt

   str = str + """
       </tbody>
      </table>
"""
   return str

###############################################################################
# Display the form
###############################################################################
def _DisplayDebug() -> None:
   print(MytDisplay.GetDebug())

###############################################################################
# Display the form
###############################################################################
def _DisplayDebugForm() -> None:

   if (MytDisplay.GetForm() is None):
      return

   print("""
<h1>Form</h1>
<p>{form}</p>
""".format(form = MytDisplay.GetForm()))

###############################################################################
# Display the command
###############################################################################
def _DisplayDebugCmd() -> None:

   print("""
<h1>Command</h1>
<p>{cmd}</p>
""".format(cmd = MytDisplay.GetCommand()))

###############################################################################
# Display the environment
###############################################################################
def _DisplayDebugEnv() -> None:

   print("""
<h1>Environment</h1>
<table>
 <tbody>
""")

   for param in os.environ.keys() :
      print("""
<tr><td>{key}</td><td>{value}</td></tr>""".format(key = param, value = os.environ[param]))

   print("""
 </tbody>
</table>
""")

###############################################################################
# Convenience function to get a bit image.
###############################################################################
def _GetBit(value: str) -> str:

   if   (value == "T"):
      return "<img class=sized src=rankBit1.svg />"

   elif (value == "F"):
      return "<img class=sized src=rankBit0.svg />"

   return "<img class=sized src=rankBitU.svg />"

###############################################################################
# Convenience function for displaying a simple button form.
###############################################################################
def _GetButtonCmd(command: str, content: str) -> str:

   return """
<form style="display:inline-block"><!--
--><input type="hidden" name="cmd" value="{cmdVal}" /><!--
--><button type="submit">{conVal}</button></form>""".format(
      cmdVal = command,
      conVal = content)

###############################################################################
# Convenience function for displaying a simple button form.
###############################################################################
def _GetButtonCmdId(command: str, id: int, content: str) -> str:

   return """
<form style="display:inline-block"><!--
--><input type="hidden" name="cmd" value="{cmdVal}" /><!--
--><input type="hidden" name="id" value="{idVal}" /><!--
--><button type="submit">{conVal}</button></form>""".format(
      cmdVal = command,
      idVal  = id,
      conVal = content)

###############################################################################
# Convenience function for displaying a simple button form.
###############################################################################
def _GetButtonCmdIdVal(command: str, id: int, val: str, content: str) -> str:

   return """<form style="display:inline-block"><!--
--><input type="hidden" name="cmd" value="{cmdVal}" /><!--
--><input type="hidden" name="id"  value="{idVal}" /><!--
--><input type="hidden" name="val" value="{valVal}" /><!--
--><button type="submit">{conVal}</button></form>""".format(
      cmdVal = command,
      idVal  = id,
      valVal = val,
      conVal = content)

###############################################################################
# Convenience function for displaying a simple button form.
###############################################################################
def _GetLinkCmd(command: str, content: str) -> str:

   return """<a href="?cmd={cmdVal}">{conVal}</a>""".format(
      cmdVal = command,
      conVal = content)

###############################################################################
# Convenience function for displaying a simple button form.
###############################################################################
def _GetLinkCmdId(command: str, id: int, content: str) -> str:

   return """<a href="?cmd={cmdVal}&id={idVal}">{conVal}</a>""".format(
      cmdVal = command,
      idVal  = id,
      conVal = content)

###############################################################################
# Convenience function for displaying a simple button form.
###############################################################################
def _GetLinkCmdIdVal(command: str, id: int, val: str, content: str) -> str:

   return """<a href="?cmd={cmdVal}&id={idVal}&val={valVal}">{conVal}</a>""".format(
      cmdVal = command,
      idVal  = id,
      valVal = val,
      conVal = content)

###############################################################################
# Convenience function for displaying a simple input form
###############################################################################
def _GetDotGraph(command: str, id: int, val: str, isImaginary: bool) -> str:

   bitVal = -1
   if   (val == MytTask.EFF.VAL1): bitVal = 1
   elif (val == MytTask.EFF.VAL2): bitVal = 2
   elif (val == MytTask.EFF.VAL3): bitVal = 3
   elif (val == MytTask.EFF.VAL4): bitVal = 4
   elif (val == MytTask.EFF.VAL5): bitVal = 5

   if (isImaginary and bitVal == -1):
      return (
         _GetLinkCmdIdVal(command, id, MytTask.EFF.VAL1, _GetBit("I")) +
         _GetLinkCmdIdVal(command, id, MytTask.EFF.VAL2, _GetBit("I")) +
         _GetLinkCmdIdVal(command, id, MytTask.EFF.VAL3, _GetBit("I")) +
         _GetLinkCmdIdVal(command, id, MytTask.EFF.VAL4, _GetBit("I")) +
         _GetLinkCmdIdVal(command, id, MytTask.EFF.VAL5, _GetBit("I")) +
         " " +
         _GetLinkCmdIdVal(command, id, MytTask.EFF.VALI, _GetBit(StrFromBool(True))))

   str  = (
      _GetLinkCmdIdVal(command, id, MytTask.EFF.VAL1, _GetBit(StrFromBool(1 <= bitVal))) +
      _GetLinkCmdIdVal(command, id, MytTask.EFF.VAL2, _GetBit(StrFromBool(2 <= bitVal))) +
      _GetLinkCmdIdVal(command, id, MytTask.EFF.VAL3, _GetBit(StrFromBool(3 <= bitVal))) +
      _GetLinkCmdIdVal(command, id, MytTask.EFF.VAL4, _GetBit(StrFromBool(4 <= bitVal))) +
      _GetLinkCmdIdVal(command, id, MytTask.EFF.VAL5, _GetBit(StrFromBool(5 <= bitVal))))

   if (isImaginary):
      return str + " " + _GetLinkCmdIdVal(command, id, MytTask.EFF.VALI, _GetBit(StrFromBool(False)))

   return str

###############################################################################
# Convenience function for displaying a simple input form
###############################################################################
def _GetInputCmdVal(command: str, value: str, size: int) -> str:

   return """
<form style="display:inline-block"><!--
--><input type="hidden" name="cmd" value="{cmdVal}" /><!--
--><input type="text" name="val" size="{sizeVal}" value="{valVal}" /><!--
--><input type="submit" hidden /></form>""".format(
      cmdVal  = command,
      valVal  = value,
      sizeVal = size)

###############################################################################
# Convenience function for displaying a simple input form
###############################################################################
def _GetInputCmdIdVal(command: str, id: int, value: str, size: int) -> str:

   return """
<form style="display:inline-block"><!--
--><input type="hidden" name="cmd" value="{cmdVal}" /><!--
--><input type="hidden" name="id" value="{idVal}" /><!--
--><input type="text" name="val" size="{sizeVal}" value="{valVal}" /><!--
--><input type="submit" hidden /></form>""".format(
      cmdVal  = command,
      idVal   = id,
      valVal  = value,
      sizeVal = size)

###############################################################################
# Convenience function for displaying a simple input form
###############################################################################
def _GetTaskTypePullDown(command: str, id: int, value: str) -> str:

   str = """<form style="display:inline-block"><!--
--><input type="hidden" name="cmd" value="{cmdVal}" /><!--
--><input type="hidden" name="id"  value="{idVal}" /><!--
--><select name="val" onchange="this.form.submit()">""".format(
      cmdVal = command,
      idVal  = id)

   isSel = ""
   if (value == MytTask.STATE.WORK_TODO): isSel = "selected"
   str = str + """<option value="{codeVal}" {selVal}>Work Todo</option>""".format(
      codeVal = MytTask.STATE.WORK_TODO,
      selVal  = isSel)

   isSel = ""
   if (value == MytTask.STATE.WORK_PROG): isSel = "selected"
   str = str + """<option value="{codeVal}" {selVal}>Work In Progress</option>""".format(
      codeVal = MytTask.STATE.WORK_PROG,
      selVal  = isSel)

   isSel = ""
   if (value == MytTask.STATE.TEST_TODO): isSel = "selected"
   str = str + """<option value="{codeVal}" {selVal}>Test Todo</option>""".format(
      codeVal = MytTask.STATE.TEST_TODO,
      selVal  = isSel)

   isSel = ""
   if (value == MytTask.STATE.TEST_PROG): isSel = "selected"
   str = str + """<option value="{codeVal}" {selVal}>Test In Progress</option>""".format(
      codeVal = MytTask.STATE.TEST_PROG,
      selVal  = isSel)

   isSel = ""
   if (value == MytTask.STATE.DOC_TODO): isSel = "selected"
   str = str + """<option value="{codeVal}" {selVal}>Doc Todo</option>""".format(
      codeVal = MytTask.STATE.DOC_TODO,
      selVal  = isSel)

   isSel = ""
   if (value == MytTask.STATE.DOC_PROG): isSel = "selected"
   str = str + """<option value="{codeVal}" {selVal}>Doc In Progress</option>""".format(
      codeVal = MytTask.STATE.DOC_PROG,
      selVal  = isSel)

   isSel = ""
   if (value == MytTask.STATE.REL_TODO): isSel = "selected"
   str = str + """<option value="{codeVal}" {selVal}>Rel Todo</option>""".format(
      codeVal = MytTask.STATE.REL_TODO,
      selVal  = isSel)

   isSel = ""
   if (value == MytTask.STATE.REL_PROG): isSel = "selected"
   str = str + """<option value="{codeVal}" {selVal}>Rel In Progress</option>""".format(
      codeVal = MytTask.STATE.REL_PROG,
      selVal  = isSel)

   isSel = ""
   if (value == MytTask.STATE.DONE): isSel = "selected"
   str = str + """<option value="{codeVal}" {selVal}>Done</option>""".format(
      codeVal = MytTask.STATE.DONE,
      selVal  = isSel)

   return str + """</select><input type="submit" hidden /></form>"""

###############################################################################
# Convenience function for displaying a simple input form
###############################################################################
def _GetCurrProjPullDown() -> str:
   str = """<form style="display:inline-block"><!--
--><input type="hidden" name="cmd" value="pc" /><!--
--><select name="id" onchange="this.form.submit()">"""

   # build the options
   projCount  = MytProjList.GetCount()
   currProjId = MytState.GetCurrIdProj()

   for index in range(projCount):

      proj = MytProjList.GetAt(index)

      isSel = ""
      if proj.GetId() == currProjId:
         isSel = "selected"

      str = str + """<option value="{projIdVal}" {selVal}>{projNameVal}</option>""".format(
         projIdVal   = proj.GetId(),
         selVal      = isSel,
         projNameVal = proj.GetName())

   return str + """</select><input type="submit" hidden /></form>"""

###############################################################################
# Convenience function for displaying a simple input form
###############################################################################
def _GetTaskProjPullDown(id: int, proj: MytProj.MytProj) -> str:

   str = """<form style="display:inline-block"><!--
--><input type="hidden" name="cmd" value="tP" /><!--
--><input type="hidden" name="id"  value="{idVal}" /><!--
--><select name="val" onchange="this.form.submit()">""".format(
      idVal  = id)

   # build the options
   projCount = MytProjList.GetCount()

   for index in range(projCount):

      ptemp = MytProjList.GetAt(index)

      isSel = ""
      if ptemp.GetId() == proj.GetId():
         isSel = "selected"

      str = str + """<option value="{projIdVal}" {selVal}>{projNameVal}</option>""".format(
         projIdVal   = ptemp.GetId(),
         selVal      = isSel,
         projNameVal = ptemp.GetName())

   return str + """</select><input type="submit" hidden /></form>"""

###############################################################################
# Convenience function for displaying a simple input form
###############################################################################
def _GetTableRow(isAlt: bool) -> str:

   if (isAlt):
      return """<tr class="rowAlt">
"""
   return    """<tr               >
"""

###############################################################################
# Convenience function for displaying a simple input form
###############################################################################
def _GetTableRowTask(isAlt: bool, state: str) -> str:

   if (isAlt):
      if (state == "wt"):   return '<tr class="rowStyle1Alt">'
      if (state == "wp"):   return '<tr class="rowStyle2Alt">'
      if (state == "tt"):   return '<tr class="rowStyle3Alt">'
      if (state == "tp"):   return '<tr class="rowStyle4Alt">'
      if (state == "dt"):   return '<tr class="rowStyle5Alt">'
      if (state == "dp"):   return '<tr class="rowStyle6Alt">'
      if (state == "rt"):   return '<tr class="rowStyle7Alt">'
      if (state == "rp"):   return '<tr class="rowStyle8Alt">'

      return '<tr class="rowStyle9Alt">'

   if (state == "wt"):   return '<tr class="rowStyle1">'
   if (state == "wp"):   return '<tr class="rowStyle2">'
   if (state == "tt"):   return '<tr class="rowStyle3">'
   if (state == "tp"):   return '<tr class="rowStyle4">'
   if (state == "dt"):   return '<tr class="rowStyle5">'
   if (state == "dp"):   return '<tr class="rowStyle6">'
   if (state == "rt"):   return '<tr class="rowStyle7">'
   if (state == "rp"):   return '<tr class="rowStyle8">'

   return '<tr class="rowStyle9">'
