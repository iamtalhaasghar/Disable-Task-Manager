import winreg


def disable_control_panel():
    # Path to the explorer properties
    registry_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer"
    # Name of the key
    registry_name = "NoControlPanel"
    # Value that the registry key is set to
    value = 1
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, registry_name, 0, winreg.REG_DWORD, value)
        winreg.CloseKey(reg_key)
        print('done')
    except WindowsError as e:
        print("Failed to write to the registry. {}".format(e))

disable_control_panel()
