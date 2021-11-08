@echo %off

python "%~dp0\rename_file_versions.py" %1 %2
goto :finished 
:finished 
echo ---------------------------------------------------------------------------