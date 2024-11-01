@echo off
:a
:: Change this to your drive Letter
if exist D:\ (goto Yes) else (goto a)

:Yes
:: Change this to your drive Letter
G:
:: You can put any Program you want here
start index.exe
goto end

:end
exit