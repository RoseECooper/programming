import os

rootdir="/home/znc46146/programming"
print(rootdir)
for dirs, subdirs, files in os.walk(rootdir):
  for subdir in subdirs:
    workdir=os.path.join(rootdir, subdir)
    print(workdir)
    for file in files:
      filePath=os.path.join(workdir, file)
      print(filePath)