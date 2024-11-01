Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Autorun.bat" & chr(34), 0
Set WshShell = Nothing
