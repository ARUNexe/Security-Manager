import winreg

class SecurityManager:
    def disable_cmd(self):
        path = winreg.HKEY_CURRENT_USER
        cmd = winreg.OpenKeyEx(path, r"SOFTWARE\Policies\Microsoft\Windows", 0, winreg.KEY_SET_VALUE)
        system = winreg.CreateKey(cmd, r"System")
        winreg.SetValueEx(system, "DisableCMD", 0, winreg.REG_DWORD, 2)
        if system:
            winreg.CloseKey(system)

    def disble_bluetooth(self):
        path = winreg.HKEY_LOCAL_MACHINE
        bt = winreg.OpenKeyEx(path,
                              r"SOFTWARE\Microsoft\Windows\CurrentVersion\ActionCenter\Quick Actions\All\SystemSettings_Device_BluetoothQuickAction",
                              0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(bt, "type", 0, winreg.REG_DWORD, 1)
        if (bt):
            winreg.CloseKey(bt)

    def disable_sites(self):
        host = open('C:\\WINDOWS\\system32\\drivers\\etc\\hosts', 'a')
        site = "0.0.0.0 facebook.com \n"
        site2 = "0.0.0.0 www.facebook.com \n"
        host.write(site)
        host.write(site2)
        host.close()

    def disble_usb(self):
        path = winreg.HKEY_LOCAL_MACHINE
        usb = winreg.OpenKeyEx(path, r"SOFTWARE\Policies\Microsoft\Windows", 0, winreg.KEY_SET_VALUE)
        usb_disble = winreg.CreateKeyEx(usb, r"RemovableStorageDevices")
        winreg.SetValueEx(usb_disble, "Deny_All", 0, winreg.REG_DWORD, 1)
        if (usb):
            winreg.CloseKey(usb)
        usb_stopr = winreg.OpenKeyEx(path, r"SYSTEM\CurrentControlSet\Services\UsbStor",0,winreg.KEY_SET_VALUE)
        winreg.SetValueEx(usb_stopr, "Start", 0, winreg.REG_DWORD, 4)
        if(usb_stopr):
            winreg.CloseKey(usb_stopr)

    def main(self):
        self.disable_sites()
        self.disble_usb()
        self.disble_bluetooth()
        self.disable_cmd()

# code to execute the class
if __name__ == "__main__":
    obj = SecurityManager()
    obj.main()
