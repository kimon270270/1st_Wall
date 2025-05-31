import os
import pandas as pd
from datetime import date

exe_files = []
excluded_dirs = [
    "C:\\System Volume Information",
    "C:\\$Recycle.Bin",
    "C:\\Windows\\WinSxS",
    "C:\\Windows\\System32\\config",
    "C:\\Windows\\CSC",
    "C:\\Program Files\\WindowsApps",
    "C:\\Recovery",
    "C:\\EFI",
    "C:\\Windows\\Fonts",
    "C:\\Windows\\Logs",
    "C:\\Windows\\Help",
    "C:\\Windows\\Inf",
]


def find_exes():
    for root, dirs, files in os.walk(r"C:\Users\anils\OneDrive\Desktop\Cyber Security"):
        
        for d in dirs:
            if not (os.path.join(root,d) in excluded_dirs):
                
                for f in files:
                    if (f.endswith(".exe")):
                        exe_files.append(os.path.join(root,f))
                        
    print(exe_files)
    
    
def compare_exes():
    
    # Read fisrt column of .csv file
    df = pd.read_csv("exe_whitelist.csv", usecols=[0])
    today = date.today()
    scan_result = os.path.join("1st_Wall_Scan_Result",f"{today}_scan_result.txt")
    os.makedirs("1st_Wall_Scan_Result", exist_ok=True)
    with open(scan_result, "w") as f:
        pass
    
    for exe in exe_files:
        if not (exe in df.values):
            with open (scan_result, "a") as f:
                f.write(f"{exe}\n")


if __name__ == "__main__":
    find_exes()
    compare_exes()