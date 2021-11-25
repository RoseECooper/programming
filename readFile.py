import os

rootdir="C:/Users/znc46146/OneDrive - Science and Technology Facilities Council/Documents/programming"
print(rootdir)
for dirs, subdirs, files in os.walk(rootdir):
  for subdir in subdirs:
    print(os.path.join(rootdir, subdir))
  for file in files:
    print(os.path.join(rootdir, file))