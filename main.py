import sys
import os
import time
from Utilities.Return_Tools import Technique_Info_Scanner, Trait_Info_Scanner

techdata = Technique_Info_Scanner.getTechniqueInfo("Limitless")
print(techdata)
traitdata = Trait_Info_Scanner.getTraitInfo("Perfected_Vessel")
print(traitdata)