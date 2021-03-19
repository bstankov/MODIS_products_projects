@echo off 
echo %DATE%
echo %TIME%

python -V 
@echo OFF
rem How to run a Python script in a given conda environment from a batch file.

rem It doesn't require:
rem - conda to be in the PATH
rem - cmd.exe to be initialized with conda init

rem Define here the path to your conda installation
set CONDAPATH=C:\ProgramData\Anaconda3
rem Define here the name of the environment
set ENVNAME=mygdal

rem The following command activates the base environment.
rem call C:\ProgramData\Miniconda3\Scripts\activate.bat C:\ProgramData\Miniconda3
rem if %ENVNAME%==base (set ENVPATH=%CONDAPATH%) else (set ENVPATH=%CONDAPATH%\envs\%ENVNAME%)
if %ENVNAME%==base (set ENVPATH=%CONDAPATH%) else (set ENVPATH=%UserProfile%\AppData\Local\conda\conda\envs\%ENVNAME%)

rem Activate the conda environment
rem Using call is required here, see: https://stackoverflow.com/questions/24678144/conda-environments-and-bat-files
call %CONDAPATH%\Scripts\activate.bat %ENVPATH%

rem Run a python script in that environment that identify and download hdf files
python U:\RS_Task_Workspaces\NDSI\scripts\MOD_proc_functs_fin.py

rem Deactivate the environment
rem call conda deactivate
call deactivate

rem If conda is directly available from the command line then the following code works.
rem call activate someenv
rem python script.py
rem conda deactivate

rem One could also use the conda run command
rem conda run -n someenv python script.py