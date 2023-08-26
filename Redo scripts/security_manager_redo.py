import winreg

class redo():

    def enable_cmd(self):
        path = winreg.HKEY_CURRENT_USER
        cmd = winreg.OpenKeyEx(path, r"SOFTWARE\Policies\Microsoft\Windows", 0, winreg.KEY_SET_VALUE)
        system = winreg.CreateKey(cmd, r"System")
        winreg.SetValueEx(system, "DisableCMD", 0, winreg.REG_DWORD, 0)
        if system:
            winreg.CloseKey(system)

    def enable_bluetooth(self):
        path = winreg.HKEY_LOCAL_MACHINE
        bt = winreg.OpenKeyEx(path,
                              r"SOFTWARE\Microsoft\Windows\CurrentVersion\ActionCenter\Quick Actions\All\SystemSettings_Device_BluetoothQuickAction",
                              0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(bt, "type", 0, winreg.REG_DWORD, 0)
        if (bt):
            winreg.CloseKey(bt)

    def enable_sites(self):
        host = open('C:\\WINDOWS\\system32\\drivers\\etc\\hosts', 'r+')
        host.seek(0)
        host.truncate()



    def enable_usb(self):
        path = winreg.HKEY_LOCAL_MACHINE
        usb = winreg.OpenKeyEx(path,
                               r"SOFTWARE\Policies\Microsoft\Windows",
                               0, winreg.KEY_SET_VALUE)
        usb_disble = winreg.CreateKeyEx(usb, r"RemovableStorageDevices")
        winreg.SetValueEx(usb_disble, "Deny_All", 0, winreg.REG_DWORD, 0)
        if (usb):
            winreg.CloseKey(usb)
        usb_stopr = winreg.OpenKeyEx(path, r"SYSTEM\CurrentControlSet\Services\UsbStor",0,winreg.KEY_SET_VALUE)
        winreg.SetValueEx(usb_stopr, "Start", 0, winreg.REG_DWORD, 3)

    def main(self):
        self.enable_bluetooth()
        self.enable_usb()
        self.enable_sites()
        self.enable_cmd()

if __name__ == "__main__":
    obj = redo()
    obj.main()