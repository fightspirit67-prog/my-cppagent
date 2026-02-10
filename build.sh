#!/bin/bash

echo "C++ 게임 개발 학습 도구 - 빌드 스크립트"
echo "=========================================="

# 의존성 설치
echo "1. 의존성 설치 중..."
pip install -q -r requirements.txt

# PyInstaller로 exe 빌드
echo "2. exe 파일 생성 중..."
cd src
pyinstaller --onefile \
    --windowed \
    --name "CPP_Learning_Tool" \
    --add-data "../data/cpp_rules.txt:data" \
    --add-data "../data/exercises.json:data" \
    --hidden-import anthropic \
    --hidden-import PyQt6.QtCore \
    --hidden-import PyQt6.QtGui \
    --hidden-import PyQt6.QtWidgets \
    main.py

echo "3. 빌드 완료!"
echo "생성된 파일: src/dist/CPP_Learning_Tool.exe"
