REM https://soft-setup.ru/administrirovanie/sozdanie-bekapa-bazy-postgresql-dlya-windows/ ��������
REM http://dl.gsu.by/doc/use/ntcmds.htm �������� ��������� ������
REM Postgres psql https://postgrespro.ru/docs/postgresql/9.6/app-psql
REM Postgres pg_dump https://postgrespro.ru/docs/postgrespro/10/app-pgdump
REM Postgres dropdb https://postgrespro.ru/docs/postgrespro/9.5/app-dropdb
REM Postgres createdb https://postgrespro.ru/docs/postgresql/9.6/app-createdb
REM Postgres pg_restore https://postgrespro.ru/docs/postgrespro/10/app-pgrestore
REM Postgres ������� ��� ������ https://postgrespro.ru/docs/postgrespro/9.5/manage-ag-templatedbs
REM Postgres ��������� ��������� https://postgrespro.ru/docs/postgrespro/9.5/multibyte

REM ������ �������� ��������� ����� ���� ���� ������ �� ������� POSTGRESQL

REM ���� �� ������� �� ������ ��������� ��������!!!

REM ������� ����� ������ ���� Anklav24@gmail.com
REM 2019

REM ������� �����
CLS
ECHO OFF
REM ��������� ��������� ��� ����������� ����������� ����� � ��������� msg
CHCP 1251
CLS
REM ��������� ���������� ���������
SET PGBIN=C:\Program Files\PostgreSQL\11.5-12.1C\bin
SET PGHOST=localhost
SET PGPORT=5432
SET PGUSER=postgres
SET PGPASSWORD=Control!PG
REM ������������� ���������� ���� ����� ������� ����� ����������� �������� �������
SET DAYDELETE=7

REM ������� ���� �� ������� ���� ��� �� ����� ������� Postgres
"%PGBIN%\psql" -A -t -c "select datname from pg_database">SQLDataBaseList.log

setlocal enabledelayedexpansion

ECHO ======================================================================================================
ECHO START LOOP / ������ ����� ����������� ��� 
ECHO !DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!_!TIME:~0,2!-!TIME:~3,2!-!TIME:~6,2!
ECHO ======================================================================================================

ECHO ======================================================================================================>>%~n0.log
ECHO START LOOP / ������ ����� ����������� ���>>%~n0.log
ECHO !DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!_!TIME:~0,2!-!TIME:~3,2!-!TIME:~6,2!>>%~n0.log>>%~n0.log
ECHO ======================================================================================================>>%~n0.log

REM ============================================================================================
REM ������� ������ ��� ��� ������
ECHO ������ ���:
ECHO C����� ���:>>%~n0.log
ECHO.
ECHO.>>%~n0.log

REM ������ �����

FOR /F "tokens=1,2" %%I IN (%~dp0SQLDataBaseList.log) DO (
ECHO %%I
ECHO %%I>>%~n0.log
REM ����� �����
)

ECHO.
ECHO.>>%~n0.log
REM ============================================================================================

REM ������ �����
FOR /F "tokens=1,2" %%I IN (%~dp0SQLDataBaseList.log) DO (
REM ������������ ����� ����� ��������� ����� � �����-������
ECHO =============================
ECHO Backup %%I
ECHO !DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!_!TIME:~0,2!-!TIME:~3,2!-!TIME:~6,2!
ECHO =============================
ECHO =============================>>%~n0.log
ECHO Backup %%I>>%~n0.log
ECHO !DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!_!TIME:~0,2!-!TIME:~3,2!-!TIME:~6,2!>>%~n0.log
ECHO =============================>>%~n0.log
REM ECHO DATEDAY: !DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!
REM  DUMPFILE: %%I !DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!_!TIME:~0,2!-!TIME:~3,2!-!TIME:~6,2!.backup
REM  LOGFILE: %%I !DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!_!TIME:~0,2!-!TIME:~3,2!-!TIME:~6,2!.log
REM  DUMPPATH: %~dp0%~n0\!DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!\%%I !DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!_!TIME:~0,2!-!TIME:~3,2!-!TIME:~6,2!.backup
REM  LOGPATH: %~dp0%~n0\!DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!\%%I !DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!_!TIME:~0,2!-!TIME:~3,2!-!TIME:~6,2!.log
REM  NAMEFOLDERBACKUP: %~d0\%~n0\!DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!

REM ������� ����� ���� ����� ��������� ������
IF NOT EXIST "%~dp0%~n0\!DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!" MD "%~dp0%~n0\!DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!"
REM ���������� ������ ����
REM ��� ��� ������ ��������� � ����������� "%PGBIN%\pg_dump.exe" --format=custom --verbose --file=%DUMPPATH% 2>%LOGPATH%
"%PGBIN%\pg_dump" -d "%%I" --format=custom --verbose --file="%~dp0%~n0\!DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!\%%I_!DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!_!TIME:~0,2!-!TIME:~3,2!-!TIME:~6,2!.backup" 2>"%~dp0%~n0\!DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!\%%I_!DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!_!TIME:~0,2!-!TIME:~3,2!-!TIME:~6,2!.log"

REM ������ ������
IF NOT !ERRORLEVEL!==0 ECHO ������. !ERRORLEVEL!
IF NOT !ERRORLEVEL!==1 ECHO ������� ���������. !ERRORLEVEL!
IF NOT !ERRORLEVEL!==0 ECHO ������. !ERRORLEVEL!>>%~n0.log
IF NOT !ERRORLEVEL!==1 ECHO ������� ���������. !ERRORLEVEL!>>%~n0.log

ECHO.>>%~n0.log

REM ����� �����
Timeout 5
)

ECHO ==================================
ECHO END LOOP / ����� ����� �����������
ECHO !DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!_!TIME:~0,2!-!TIME:~3,2!-!TIME:~6,2!
ECHO ==================================

ECHO ==================================>>%~n0.log
ECHO END LOOP / ����� ����� �����������>>%~n0.log
ECHO !DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!_!TIME:~0,2!-!TIME:~3,2!-!TIME:~6,2!>>%~n0.log>>%~n0.log
ECHO.==================================>>%~n0.log

ECHO.
ECHO.>>%~n0.log

REM ������� ������ �������
ECHO ==================================
ECHO �������� ������ ������ %DAYDELETE% (���/����)
ECHO !DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!_!TIME:~0,2!-!TIME:~3,2!-!TIME:~6,2!
ECHO ==================================
ECHO ==================================>>%~n0.log
ECHO �������� ������ ������ %DAYDELETE% (���/����)>>%~n0.log
ECHO !DATE:~0,4!-!DATE:~5,2!-!DATE:~8,2!_!TIME:~0,2!-!TIME:~3,2!-!TIME:~6,2!>>%~n0.log>>%~n0.log
ECHO ==================================>>%~n0.log
REM �������� ������
forfiles /P "%~dp0%~n0" /S /D -%DAYDELETE% /C "cmd /c del /f /a /q @file"

REM ������ ������
IF NOT %ERRORLEVEL%==0 ECHO ������: �� ������� �����, ���������� �������� ������. %ERRORLEVEL%
IF NOT %ERRORLEVEL%==1 ECHO ������� ���������. %ERRORLEVEL%
IF NOT %ERRORLEVEL%==1 ECHO ������� ���������. %ERRORLEVEL%>>%~n0.log

REM �������� �����
forfiles /P "%~dp0%~n0" /d -%DAYDELETE% /C "cmd /c rd /s /q @path" 2>>%~n0.log

REM ������ ������
IF NOT %ERRORLEVEL%==0 ECHO ������: �� ������� �����, ���������� �������� ������. %ERRORLEVEL%
IF NOT %ERRORLEVEL%==1 ECHO ������� ���������. %ERRORLEVEL%
IF NOT %ERRORLEVEL%==1 ECHO ������� ���������. %ERRORLEVEL%>>%~n0.log

ECHO.>>%~n0.log

Timeout 60