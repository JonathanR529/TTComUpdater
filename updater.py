import os
import shutil
import subprocess
import urllib.request
import zipfile
import platform
import psutil
import sys

def safe_remove_file(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
    except Exception as e:
        print(f"Warning: could not remove file {path}: {e}")

def safe_remove_folder(path):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
    except Exception as e:
        print(f"Warning: could not remove folder {path}: {e}")

def kill_ttcom():
    found_procs = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            name = proc.info['name'] or ''
            cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ''
            if 'ttcom.exe' in name.lower() or 'ttcom.py' in cmdline.lower():
                found_procs.append((proc, name or cmdline))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not found_procs:
        return

    print("\nWARNING: The following TTCom processes will be terminated:")
    for _, pname in found_procs:
        print(f"  - {pname}")
    confirm = input("Do you want to continue? (y/N): ").strip().lower()

    if confirm != 'y':
        print("Aborting script.")
        sys.exit(0)

    for proc, pname in found_procs:
        try:
            proc.kill()
            print(f"[+] Killed: {pname}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            print(f"[-] Could not kill: {pname}")

# ------------------ Updater Logic ------------------

def main():
    print("Welcome to TTCom Updater, please select an option.")
    while True:
        choice = input(
            "1. Update to the latest version of TTCom\n"
            "2. Update to the latest version of TTCom compiled for Windows\n"
            "3. Update to the latest beta revision of TTCom\n"
            "4. Update to the latest beta revision of TTCom compiled for Windows\n"
            "Press any other key to exit.\n"
            "Your choice: "
        ).strip()
        if choice in ["1", "2", "3", "4"]:
            kill_ttcom()

        if choice == "1":
            update_ttcom()
            break
        elif choice == "2":
            update_ttcom(windows=True)
            break
        elif choice == "3":
            update_ttcom(beta=True)
            break
        elif choice == "4":
            update_ttcom(beta=True, windows=True)
            break
        else:
            print("Exiting program.")
            exit()

def update_ttcom(beta=False, windows=False):
    print("Updating, please wait.")
    remove_pre_extraction_files(windows)

    if beta:
        download_url = "https://www.dlee.org/teamtalk/ttcom/beta/ttcom.zip"
        if windows:
            download_url = "https://www.dlee.org/teamtalk/ttcom/beta/ttcom_win.zip"
    else:
        download_url = "https://www.dlee.org/teamtalk/ttcom/ttcom.zip"
        if windows:
            download_url = "https://www.dlee.org/teamtalk/ttcom/ttcom_win.zip"

    if windows:
        remove_internal_folder()

    download_file(download_url, windows)
    extract_file("ttcom.zip" if not windows else "ttcom_win.zip")
    cleanup_post_extraction_files(windows)

def remove_pre_extraction_files(windows=False):
    if not windows:
        files_to_delete = [
            "banreq.py", "bitflags.py", "conf.py", "geolocator.py", "LICENSE.txt",
            "parmline.py", "trigger_cc.py", "triggers.py", "tt_attrdict.py",
            "ttapi.py", "ttcom.exe", "ttcom.htm", "ttcom.py", "TTComCmd.py",
            "ttflags.py", "upgrade_conf.py"
        ]
        for file in files_to_delete:
            safe_remove_file(file)
        safe_remove_folder("mplib")
    else:
        safe_remove_file("ttcom.exe")

def download_file(url, windows=False):
    print("Downloading, please wait.")
    local_filename = url.split('/')[-1]
    urllib.request.urlretrieve(url, local_filename)

def remove_internal_folder():
    safe_remove_folder("_internal")

def extract_file(file_name):
    print(f"Extracting {file_name}, please wait.")
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall()

def cleanup_post_extraction_files(windows=False):
    print("Deleting unnecessary files, please wait.")
    safe_remove_file("ttcom.zip" if not windows else "ttcom_win.zip")
    safe_remove_file("ttcom.conf.sample")

if __name__ == "__main__":
    main()
