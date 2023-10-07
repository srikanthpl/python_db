import os
if os.path.exists("pyre.txt"):
  os.remove("pyre.txt")
else:
  print("The file does not exist")