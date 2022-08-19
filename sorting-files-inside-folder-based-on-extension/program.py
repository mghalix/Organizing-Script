import os, shutil

def organize(path):
  path+='\\'
  def extensionType(file):
    if not os.path.exists(file):
      return "File doesn't exist"
    if os.path.isfile(file):
      i = file.rindex('.') #to get the index of the last dot in a file's name
      return file[i+1:].lower() #lowercase in for the scenario where the file extension is uppercase
    return "Error not a file. This is a directory"

  names = os.listdir(path)

  def remapDirName(name):
    for key, value in folders.items():
      for val in value:
        if val == name:
          return key
    return "Unknown"

  folders = {
    "Images" : ["jpg", "png", "tif"],
    "Music" : ["mp3", "m4a", "aac"],
    "Photoshop" : ["psd"],
    "Videos" : ["mov", "mp4", "mkv"],
    "Documents" : ["txt", "pdf", "docx"],
    "Compressed" : ["zip", "rar"],
    "Programs" : ["exe"],
  }
  folder_name = []
  for name in names:
    if os.path.isdir(path+name): continue
    if extensionType(path+name) not in folder_name:
      # folder_name.append(extensionType(path+name)) #if you want to make the folder name as the extension type without the dot
      folder_name.append(remapDirName(extensionType(name))) #if you want to categorize multiple extension type in related folder

  for i in range(0,len(folder_name)):
    if not os.path.exists(path+folder_name[i]):
      os.makedirs(path+folder_name[i])

  for file in names:
    if os.path.isfile(path+file) and not os.path.exists(path+extensionType(path+file)+'\\'+file):
      shutil.move(path+file, path+remapDirName(extensionType(file))+'\\'+file)
  
organize(os.getcwd())