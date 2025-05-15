import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\SUDHIR KR\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\SUDHIR KR\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

executables = [cx_Freeze.Executable("Face_Recognize_Software.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "Face Recognize Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'Image','Data','database','Attendance Report']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System | Developed By Sudheer",
    executables = executables
    )
