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
from MytUtil import *

###############################################################################
# global
# class
###############################################################################
###############################################################################
# Project Class
###############################################################################
class MytProj:
   
   _clsIdMax: int = 0

   def __init__(self, id: int = 0, isVis: bool = False, name: str = "", desc: str = ""):
      
      self._id:      int   = id;
      self._name:    str   = name
      self._desc:    str   = desc
      self._isVis:   bool  = isVis

      if (id < 0):
         self._id = MytProj._clsIdMax

         MytProj._clsIdMax += 1

      else:
         if (MytProj._clsIdMax < id):
            MytProj._clsIdMax = id + 1


   def __eq__(self, other: object) -> bool:
      if (isinstance(other, MytProj)):
         return self._id == other._id
      return NotImplemented

   def __ge__(self, other: object) -> bool:
      if (isinstance(other, MytProj)):
         return self._name >= other._name
      return NotImplemented

   def __gt__(self, other: object) -> bool:
      if (isinstance(other, MytProj)):
         return self._name > other._name
      return NotImplemented

   def __le__(self, other: object) -> bool:
      if (isinstance(other, MytProj)):
         return self._name <= other._name
      return NotImplemented

   def __lt__(self, other: object) -> bool:
      if (isinstance(other, MytProj)):
         return self._name < other._name
      return NotImplemented

   def __ne__(self, other: object) -> bool:
      if (isinstance(other, MytProj)):
         return self._id != other._id
      return NotImplemented

   def __str__(self):
      return "{id}\t{isVis}\t{name}\t{desc}\n".format(
         id    = StrFromInt( self._id),
         isVis = StrFromBool(self._isVis),
         name  =             self._name,
         desc  =             self._desc)


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

   def SetIsVis(self, value: bool):
      self._isVis = value

   def SetName(self, value: str):
      self._name = value

###############################################################################
# global
# function
###############################################################################
###############################################################################
# Create
###############################################################################
def Create(id: int = 0, isVis: bool = False, name: str = "", desc: str = "") -> MytProj:
   return MytProj(id, isVis, name, desc)

###############################################################################
# Create a project from the string.
###############################################################################
def CreateFromStr(line: str) -> MytProj | None:
   
   # Split the line
   part = line.split('\t')

   # Not enought values.
   if (len(part) < 4):
      return None

   # Get the values.
   id    = IntFromStr( part[0])
   isVis = BoolFromStr(part[1])
   name  =             part[2]
   desc  =             part[3]
   
   return Create(id, isVis, name, desc)
