
# Introduction
- Security manager that implements specific security measures on a Windows 10 operating system.
- All the modules works by changing system values.
- This python script uses winreg library to modify Windows registry values.

# Modules 
#### Disable USB - 
  - This module disables all external usb removable devices so that it cant be connected to the system.
  - This module works by changing the registry in file HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\UsbStor\Start value from 3 to 4 which disables usb devices.

#### Disable CMD - 
  - This module disables Command Prompt (CMD) in windows.
  - This module works by adding a key in registry in file SOFTWARE\Policies\Microsoft\Windows and creating new key "DisableCMD" to 2.

#### Disable Website (Facebook)
  - This module disables access to facebook.com website.
  - This module works by changing the port of facebook.com website in file "C:\WINDOWS\system32\drivers\etc\hosts" so that it doesnt connect to its required port.

#### Disable Bluetooth - 
  - This module disables bluetooth feature in windows.
  - This module works by changing the registry in file "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\ActionCenter\Quick Actions\All\SystemSettings_Device_BluetoothQuickAction" from 0 to 1


# Executable File instructions:
  - Disable antivirus before downloading the exe file.
  - Run the exe file as administrator.


# Redo function:
  - For testing purpose i added a redo function so that i dont need to manually revert the changes the script did
  - I thought i might add that too. 
