###############################################################################
# file:       MYT_proj
# author:     Robbert de Groot
# company:    Zekaric
# copyright:  2022, Zekaric
# 
# description:
# Project handling.
###############################################################################

###############################################################################
# import
###############################################################################
import os

###############################################################################
# global
# class
###############################################################################
###############################################################################
# Project Class
###############################################################################
class MytProj:
   
   _clsIdMax: int = 0

   def __init__(self, id: int, isVis: bool, name: str, desc: str):
      
      self._id    = id;
      self._name  = name
      self._desc  = desc
      self._isVis = isVis

      if id < 0:
         self._id = MytProj._clsIdMax
         MytProj._clsIdMax += 1

      else:
         if MytProj._clsIdMax < id:
            MytProj._clsIdMax = id + 1


   def __eq__(self, other):
      return self.id == other.id

   def __ge__(self, other):
      return self.name >= other.name

   def __gt__(self, other):
      return self.name > other.name

   def __le__(self, other):
      return self.name <= other.name

   def __lt__(self, other):
      return self.name < other.name

   def __ne__(self, other):
      return self.id != other.id

   def __str__(self):
      return f'{self._id}\t{self._isVis}\t{self._name}\t{self._desc}\n'


   def GetDesc(self) -> str:
      return self._desc

   def GetId(self) -> int:
      return self._id

   def GetName(self) -> str:
      return self._name


   def IsVis(self) -> bool:
      return self._isVis


   def SetDesc(self, value: str):
      self._desc = value

   def SetName(self, value: str):
      self._name = value

###############################################################################
# global
# function
###############################################################################
###############################################################################
# Create
###############################################################################
def Create(id: int, isVis: bool, name: str, desc: str = '') -> MytProj:
   return Project(id, isVis, name, desc)

###############################################################################
# Create a project from the string.
###############################################################################
def CreateFromStr(line: str) -> MytProj:
   
   # Split the line
   part = line.split('\t')

   # Not enought values.
   if len(part) < 4:
      return None

   # Get the values.
   id    = int( part[0])
   isVis = bool(part[1])
   name  =      part[2]
   desc  =      part[3]
   
   return Create(id, isVis, name, desc)