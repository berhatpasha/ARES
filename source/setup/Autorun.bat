@echo off
:a
::-------V----Change this to your drive Letter
if exist D:\ (goto Yes) else (goto a)

:Yes
::V----Change this to your drive Letter
G:
::----V----You can put any Program you want here
start File.bat
goto end

:end
exit