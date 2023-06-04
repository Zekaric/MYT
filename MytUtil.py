################################################################################
# file:       MytUtil
# author:     Robbert de Groot
# company:    Zekaric
# copyright:  2022, Zekaric
#
# description:
# Utility functions
################################################################################

################################################################################
# global
# function
################################################################################
def IntFromStr(value: str) -> int:
   return int(value)

def StrFromInt(value: int) -> str:
   return str(value)

# Python fucked up here.  Above we have int conversion.  Looks sane.  You'd
# expect bool(str) to work the same.  NO IT DOESN'T.  That's fucked up.
def BoolFromStr(value: str) -> bool:
   return value == "T"

def StrFromBool(value: bool) -> str:
   if (value):
      return "T"
   return "F"
