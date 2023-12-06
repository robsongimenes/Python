@echo off

echo "**********************************************"
echo           Project Directory Creator
echo "**********************************************"

echo This batch file will help you create a project directory.


echo "**********************************************"
echo          Press [Ctrl+C] to exit or any key to continue
echo "**********************************************"
pause 

set /p NAME=Enter the name of the project:  

echo Creating project directory %NAME%...
mkdir %NAME%

cd %NAME%

echo Creating subdirectories...
mkdir Documentation
mkdir Tests
mkdir Examples
mkdir Source

cls
echo Project directory %NAME% created successfully!

echo "**********************************************"
echo                Directory Structure
echo "**********************************************"
tree /f
cd ..