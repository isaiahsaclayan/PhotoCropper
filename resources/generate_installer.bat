cd..

if exist build (
    rmdir /s /q build
)

pyinstaller --clean build/AutoCropApp
pyinstaller --name AutoCropApp ^
    --onefile ^
    --windowed ^
    --icon=../resources/assets/icon.ico ^
    --specpath build ^
    --distpath build/output ^
    --workpath build/temp ^
    --paths=source ^
    source/main.py
