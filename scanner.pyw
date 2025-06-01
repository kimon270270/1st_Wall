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

def add_excluded_dirs():
    
    print("\n---------- Adding Directories To Exclude ----------\n\n")
    for path in excluded_dirs:
        
        for root, dirs, files in os.walk(path):
            for d in dirs:
                if not (os.path.join(root,d) in excluded_dirs):
                    excluded_dirs.append(os.path.join(root,d))
        print(f"All directories from {path} added.")


def find_exes():
    
    print("\n\n---------- Finding Executable Files In The System ----------\n\n")
    for root, dirs, files in os.walk(r"C:\\"):
        
        for f in files:
            path = os.path.join(root,f)
            d_path = path.split(f"\\{f}")
            
            if not (d_path in excluded_dirs):
                
                if (f.endswith(".exe")):
                    exe_files.append(os.path.join(root,f))
    
    
def compare_exes():
    
    print("\n\n---------- Comapring And Creating The Scan Result ----------\n\n")
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
                f.write(f"{exe}\n\n")


if __name__ == "__main__":
    add_excluded_dirs()
    find_exes()
    compare_exes()
    print("\n\n---------- Scan Completed!!! ----------\n\n")