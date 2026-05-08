@echo off
TITLE НСЗУ Аналітика: Запуск сервера
echo Запуск локального сервера для НСЗУ Аналітика...
echo Це дозволяє уникнути проблем з безпекою браузерів при відкритті файлів.

set PORT=8000

:checkport
netstat -ano | findstr :%PORT% | findstr LISTENING >nul
if %errorlevel% equ 0 (
    set /a PORT=%PORT%+1
    goto checkport
)

echo Сервер запускається на http://localhost:%PORT%
start "" "http://localhost:%PORT%/main.html"
python -m http.server %PORT%

pause
