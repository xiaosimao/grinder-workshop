@ECHO off
del /Q log\*
java -cp lib\jython.jar;lib\json-20080701.jar;lib\grinder.jar net.grinder.Grinder %1
