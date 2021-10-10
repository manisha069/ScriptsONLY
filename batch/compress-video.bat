::========================================================================+
:: Author: Harsh Navdhare                                                 |
:: Description:    This script takes a video file as an arguement and     |
::                 compresses it by encoding it in H265.                  |
::                 See https://unix.stackexchange.com/a/38380             |
:: Prerequisites : The script assumes you have ffmpeg installed on your   |
::                 computer and added to your path.                       |
::                 If not, see                                            |
::                 https://spadebee.com/2020/06/02/how-to-install-ffmpeg/ |
::                                                                        |
:: How to use: Just drag and drop the file to be compressed to            |
::             compress-file.bat                                          |
::========================================================================+
@echo off
SET file=%1

:: Obtain file path, filename from the whole path
:: See https://stackoverflow.com/a/47487854/9664447

FOR /F "delims=" %%i IN ("%file%") DO (
SET filepath=%%~pi
SET filename=%%~ni
SET fileextension=%%~xi
)

@echo on
:: The main command to compress the file.
:: File will be stored in the same directory as of input file
:: With "- compressed" appended to its name

ffmpeg -i %file% -c:v libx265 -c:a copy -crf 28 "%filepath%\%filename% - compressed.mp4"

pause