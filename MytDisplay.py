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
   _command: str              = ""
   _debug  : str              = ""
   _form   : cgi.FieldStorage = None

###############################################################################
# global
# function
###############################################################################
###############################################################################
# Process the display
###############################################################################
def Process():
   
   print("Content-Type: text/html\n\n")

   print("""<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">

 <head>
  <meta charset="utf-8" />
  <link rel="stylesheet" type="text/css" href="style_reset.css">
  <link rel="stylesheet" type="text/css" href="style.css">
  <title>Zekaric:MYT</title>
 </head>

 <body>
""")

   if (MytState.IsShowingProjList()):
      print("""
  <h1>Zekaric : MYT Projects</h1>
""")
      _DisplayProjList()
   else:
      print("""
  <h1>Zekaric : MYT Tasks</h1>
""")
      _DisplayTaskList()

   #DEBUG
   #_DisplayDebug()
   #_DisplayDebugForm()
   #_DisplayDebugCmd()
   #_DisplayDebugEnv()

   print("""
 </body>
</html>""")

###############################################################################
# Set the command that was to be processed
###############################################################################
def DebugAppend(line: str) -> None:
   MytDisplay._debug = MytDisplay._debug + line + "</br>\n"

###############################################################################
# Set the command that was to be processed
###############################################################################
def DebugSetCommand(line: str) -> None:
   MytDisplay._command = line

###############################################################################
# Set the command that was to be processed
###############################################################################
def DebugSetForm(form: cgi.FieldStorage) -> None:
   MytDisplay._form = form

###############################################################################
# local
# function
###############################################################################
###############################################################################
# Display the project list.
###############################################################################
def _DisplayProjList():

   if ("SCRIPT_NAME" not in os.environ):
      urlValue = "localHost/index.py"
   else:
      urlValue = os.environ["SCRIPT_NAME"]

   print("""
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
       hideAllBtn  = _GetButtonCmd("p0", "{img} {img} {img}".format(img = _GetBit(False))),
       showAllBtn  = _GetButtonCmd("p1", "{img} {img} {img}".format(img = _GetBit(True))),
       newProjFld  = _GetInputCmdVal("pa", "New Project Name", 15)))

   isAlt = False;
   for proj in MytProjList.Get():

      itemp = proj.GetId()

      isVisValue = _GetButtonCmdId(  "pv", itemp, _GetBit(proj.IsVis()))
      nameValue  = _GetInputCmdIdVal("pn", itemp, proj.GetName(), 15)
      descValue  = _GetInputCmdIdVal("pd", itemp, proj.GetDesc(), 200)

      print("""
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
      desc  = descValue))

      isAlt = not isAlt

   print("""
    </tr>
   </tbody>
  </table>
""")

###############################################################################
# Display the task list.
###############################################################################
def _DisplayTaskList():

   print("""
  <table>
   <tbody>
    <tr>
     <td colspan=4>
      {goToProjs}
     </td>
    </tr>""".format(goToProjs = _GetButtonCmd("l", "Go To Projects")))
    
   # The task visibility
   print("""
    <tr>
     <td> 
      <table class="narrow">
       <tbody>
        {trNrm}<td colspan=2>
          {hideAllBtn}
          {showAllBtn}
        </td></tr>
        {trNrm}<th>Vis</th><th><nobr>Task State</nobr></th></tr>
        {trNrm}<td>{wIsVis}</td><td>Work</td></tr>
        {trAlt}<td>{tIsVis}</td><td>Test</td></tr>
        {trNrm}<td>{dIsVis}</td><td>Doc </td></tr>
        {trAlt}<td>{rIsVis}</td><td>Rel </td></tr>
        {trNrm}<td>{xIsVis}</td><td>Done</td></tr>
       </tbody>
      </table></br>
    """.format(
      trNrm      = _GetTableRow(False),
      trAlt      = _GetTableRow(True),
      hideAllBtn = _GetButtonCmd("d0", "{img} {img} {img}".format(img = _GetBit(False))),
      showAllBtn = _GetButtonCmd("d1", "{img} {img} {img}".format(img = _GetBit(True))),
      wIsVis     = _GetButtonCmd("dw", _GetBit(MytState.IsShowingTaskWork())),
      tIsVis     = _GetButtonCmd("dt", _GetBit(MytState.IsShowingTaskTest())),
      dIsVis     = _GetButtonCmd("dd", _GetBit(MytState.IsShowingTaskDoc())),
      rIsVis     = _GetButtonCmd("dr", _GetBit(MytState.IsShowingTaskRel())),
      xIsVis     = _GetButtonCmd("dx", _GetBit(MytState.IsShowingTaskDone()))))

   # The project list
   print("""
      <table class="narrow">
       <tbody>
        <tr>
         <td colspan=4>
          {hideAllBtn}
          {showAllBtn}
         </td>
        </tr><tr>
         <th             ><nobr>Vis</nobr></th>
         <th             ><nobr>PID</nobr></th>
         <th             ><nobr>Project</nobr></th>
        </tr>""".format(
      hideAllBtn  = _GetButtonCmd("p0", "{img} {img} {img}".format(img = _GetBit(False))),
      showAllBtn  = _GetButtonCmd("p1", "{img} {img} {img}".format(img = _GetBit(True)))))

   isAlt = False;
   for proj in MytProjList.Get():

      itemp = proj.GetId()

      isVisValue = _GetButtonCmdId(  "pv", itemp, _GetBit(proj.IsVis()))
      nameValue  = proj.GetName()

      print("""
    {tr}
     <td class="bool">{isVis}</td>
     <td class="num" >{id}</td>
     <td             >{name}</td>
    </tr>""".format(
      tr    = _GetTableRow(isAlt),
      id    = proj.GetId(), 
      isVis = isVisValue,
      name  = nameValue))

      isAlt = not isAlt

   print("""
       </tbody>
      </table class="narrow">
     </td>
""")


   print("""
   </tbody>
  </table>
""")

###############################################################################
# Display the form
###############################################################################
def _DisplayDebug():
   print(MytDisplay._debug)

###############################################################################
# Display the form
###############################################################################
def _DisplayDebugForm():
   if (MytDisplay._form is None):
      return

   print("""
<h1>Form</h1>
<p>{form}</p>
""".format(form = MytDisplay._form))

###############################################################################
# Display the command
###############################################################################
def _DisplayDebugCmd():
   print("""
<h1>Command</h1>
<p>{cmd}</p>
""".format(cmd = MytDisplay._command))

###############################################################################
# Display the environment
###############################################################################
def _DisplayDebugEnv():
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
def _GetBit(value: bool) -> str:
   if (value):
      return "<img class=sized src=rankBit1.svg />"
   return "<img class=sized src=rankBit0.svg />"

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
def _GetTableRow(isAlt: bool) -> str:
   if (isAlt):
      return """<tr class="rowAlt">
"""
   return    """<tr               >
"""