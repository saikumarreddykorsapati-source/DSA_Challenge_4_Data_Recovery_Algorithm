import shutil, os, sys
from utils import func
import pyminizip
from zipfile import ZipFile
import zipfile
from tkinter import *
from tkinter import filedialog




def create_folder(filepath,dir):
  if not os.path.exists(os.getcwd()+"/assets/"+dir+"_Files"):
    os.makedirs(os.getcwd()+"/assets/"+dir+"_Files")
    print("Created Directory : ", dir+"_Files" )
    shutil.copy(filepath, os.getcwd()+"/assets/"+dir+"_Files")
    print("File uploaded")
  else:
    print("Directory already existed :  ", dir+"_Files" )
    shutil.copy(filepath, os.getcwd()+"/assets/"+dir+"_Files")
    print("file uploaded")
  return dir

def filehandle(filepath,filename_in, ext):
        create_folder(filepath,ext)

def singleZip():
  print("Enter Input_File_name :" )
  file_path,file_name = func.browseFiles()  
  oupt = os.getcwd()+"/assets/Back_Ups/output_"+file_name+".zip"
  password = input("Enter Password to protect your backsups : ")
  pyminizip.compress(file_path, None, oupt, password, 9)
  sys.exit("\n-> Backup Successful...")

def recZip():

  file_path,file_name = func.browseFiles()
  pswd = input("\n Enter you backup zip file - PASSWORD : ")

  with zipfile.ZipFile(file_path) as file:
      file.extractall(path=os.getcwd()+"/assets/Recovery/",pwd = bytes(pswd, 'utf-8'))
  sys.exit("\n\n\t-> Recovery Successful...")

def mulZip():
  file_path1 = filedialog.askdirectory()
  if file_path1=="":
        sys.exit("\nNo file selected from opened pop up window")
  print(file_path1)
  to_zip1 = []
  for i in os.listdir(file_path1):
    to_zip1.append(file_path1+"/"+i)
  
  zip_path = os.getcwd()+"/assets/Back_Ups/"+os.path.basename(file_path1).split("/")[-1]+".zip"
  
  k="/"
  files_path = []
  for i in range(len(to_zip1)):
      files_path.append(k)
  
  pass1 = input("Enter Password for backup data authentication")
  
  pyminizip.compress_multiple(to_zip1,files_path, zip_path, pass1, 9)
  sys.exit("\n-> Multiple Files Backup Successful...")
