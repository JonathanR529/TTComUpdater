# TTCom Updater
A simple updater for the TeamTalk Commander.

## Getting Started

You can run it directly with:

```
python updater.py
```

Or download the [latest release](https://github.com/JonathanR529/TTComUpdater/releases/latest) for a Windows executable.

When you run the script, it will:

* Ask if you want to update to one of the following:

  * The latest version of TTCom
  * The latest version of TTCom compiled for Windows
  * The latest beta revision of TTCom
  * The latest beta revision of TTCom compiled for Windows

## Warnings

* The script must be placed inside your TTCom directory.
* It will terminate any active TTCom process before proceeding with the update.

## Building

You can build the updater into an executable using PyInstaller:

```
pyinstaller --onefile -n TTCom_Updater updater.py
```

If you have [UPX](https://upx.github.io/) you can optionally use the `--upx-dir` flag with PyInstaller to compress the compiled executable and reduce its file size.

## Credits

Thanks to [Doug Lee](https://dlee.org/) for writing the [TeamTalk Commander](https://dlee.org/teamtalk/ttcom/) program.