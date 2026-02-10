"""
C++ 게임 개발 학습 도구 - 메인 애플리케이션
"""
import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QLineEdit, QPushButton, QListWidget, QSplitter,
    QLabel, QMessageBox, QListWidgetItem
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QTextCursor

from claude_api import ClaudeAPI
from exercise_manager import ExerciseManager


class ClaudeWorker(QThread):
    """Claude API 호출을 백그라운드에서 처리하는 워커 스레드"""
    response_ready = pyqtSignal(str)
    error_occurred = pyqtSignal(str)
    
    def __init__(self, claude_api, message, system_prompt=None):
        super().__init__()
        self.claude_api = claude_api
        self.message = message
        self.system_prompt = system_prompt
    
    def run(self):
        try:
            response = self.claude_api.send_message(self.message, self.system_prompt)
            self.response_ready.emit(response)
        except Exception as e:
            self.error_occurred.emit(str(e))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("C++ 게임 개발 실전 학습 도구")
        self.setGeometry(100, 100, 1400, 800)
        
        # API 키 설정 (환경변수 또는 config.ini에서 로드)
        self.api_key = self.load_api_key()
        if not self.api_key:
            QMessageBox.warning(
                self,
                "API 키 없음",
                "Claude API 키를 설정해주세요.\n\n방법 1: 환경변수 CLAUDE_API_KEY 설정\n방법 2: config.ini 파일 생성"
            )
        self.claude_api = ClaudeAPI(self.api_key) if self.api_key else None
        
        # 연습 문제 관리자
        self.exercise_manager = ExerciseManager()
        
        # C++ 규칙 로드
        self.cpp_rules = self.load_cpp_rules()
        
        # 워커 스레드
        self.worker = None
        
        # UI 초기화
        self.init_ui()
        
        # 시작 메시지
        self.add_system_message("C++ 게임 개발 학습 도구에 오신 것을 환영합니다!")
        self.add_system_message("왼쪽 사이드바에서 난이도를 선택하고 연습 문제를 클릭하거나,")
        self.add_system_message("자유롭게 질문을 입력하세요.")
    
    def load_api_key(self):
        """API 키 로드 (환경변수 또는 config.ini)"""
        # 1. 환경변수에서 로드
        api_key = os.environ.get('CLAUDE_API_KEY')
        if api_key:
            return api_key
        
        # 2. config.ini 파일에서 로드
        config_file = 'config.ini'
        if os.path.exists(config_file):
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.startswith('CLAUDE_API_KEY='):
                            return line.split('=', 1)[1].strip()
            except Exception:
                pass
        
        return None
    
    def load_cpp_rules(self):
        """C++ 규칙 파일 로드"""
        try:
            with open("data/cpp_rules.txt", 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return "규칙 파일을 찾을 수 없습니다."
    
    def init_ui(self):
        """UI 초기화"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout(central_widget)
        
        # 왼쪽: 사이드바 (연습 문제 목록)
        sidebar = self.create_sidebar()
        
        # 오른쪽: 채팅 인터페이스
        chat_widget = self.create_chat_widget()
        
        # 스플리터로 분할
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(sidebar)
        splitter.addWidget(chat_widget)
        splitter.setStretchFactor(0, 1)  # 사이드바
        splitter.setStretchFactor(1, 3)  # 채팅
        
        main_layout.addWidget(splitter)
    
    def create_sidebar(self):
        """사이드바 생성"""
        sidebar_widget = QWidget()
        sidebar_layout = QVBoxLayout(sidebar_widget)
        
        # 제목
        title_label = QLabel("📚 연습 문제")
        title_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        sidebar_layout.addWidget(title_label)
        
        # 난이도별 섹션
        levels = self.exercise_manager.get_levels()
        
        for level in levels:
            # 난이도 레이블
            level_label = QLabel(f"▶ {level}")
            level_label.setFont(QFont("Arial", 11, QFont.Weight.Bold))
            level_label.setStyleSheet("margin-top: 10px;")
            sidebar_layout.addWidget(level_label)
            
            # 연습 문제 리스트
            exercises = self.exercise_manager.get_exercises_by_level(level)
            for i, exercise in enumerate(exercises):
                item_widget = QPushButton(f"  {i+1}. {exercise['title']}")
                item_widget.setStyleSheet("""
                    QPushButton {
                        text-align: left;
                        padding: 8px;
                        border: none;
                        background-color: transparent;
                    }
                    QPushButton:hover {
                        background-color: #e0e0e0;
                    }
                """)
                item_widget.clicked.connect(
                    lambda checked, lvl=level, idx=i: self.load_exercise(lvl, idx)
                )
                sidebar_layout.addWidget(item_widget)
        
        # 대화 초기화 버튼
        sidebar_layout.addStretch()
        clear_btn = QPushButton("🔄 대화 초기화")
        clear_btn.clicked.connect(self.clear_conversation)
        sidebar_layout.addWidget(clear_btn)
        
        return sidebar_widget
    
    def create_chat_widget(self):
        """채팅 인터페이스 생성"""
        chat_widget = QWidget()
        chat_layout = QVBoxLayout(chat_widget)
        
        # 채팅 히스토리 표시 영역
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont("Consolas", 10))
        chat_layout.addWidget(self.chat_display)
        
        # 입력 영역
        input_layout = QHBoxLayout()
        
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("질문이나 코드를 입력하세요...")
        self.input_field.setFont(QFont("Arial", 11))
        self.input_field.returnPressed.connect(self.send_message)
        
        self.send_button = QPushButton("전송")
        self.send_button.setFont(QFont("Arial", 11))
        self.send_button.clicked.connect(self.send_message)
        
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.send_button)
        
        chat_layout.addLayout(input_layout)
        
        return chat_widget
    
    def add_system_message(self, message):
        """시스템 메시지 추가"""
        self.chat_display.append(f'<p style="color: #666; font-style: italic;">ℹ️ {message}</p>')
        self.chat_display.moveCursor(QTextCursor.MoveOperation.End)
    
    def add_user_message(self, message):
        """사용자 메시지 추가"""
        self.chat_display.append(f'<p style="color: #0066cc; font-weight: bold;">👤 당신:</p>')
        self.chat_display.append(f'<p style="margin-left: 20px;">{message}</p>')
        self.chat_display.moveCursor(QTextCursor.MoveOperation.End)
    
    def add_assistant_message(self, message):
        """어시스턴트 메시지 추가"""
        self.chat_display.append(f'<p style="color: #00aa00; font-weight: bold;">🤖 Claude:</p>')
        # 코드 블록 하이라이팅
        formatted_message = message.replace('\n', '<br>')
        self.chat_display.append(f'<p style="margin-left: 20px;">{formatted_message}</p>')
        self.chat_display.moveCursor(QTextCursor.MoveOperation.End)
    
    def load_exercise(self, level, index):
        """연습 문제 로드"""
        prompt = self.exercise_manager.get_exercise_prompt(level, index)
        if prompt:
            self.add_system_message(f"{level} - 문제 {index+1} 로드됨")
            self.input_field.setText(prompt)
            self.send_message()
    
    def send_message(self):
        """메시지 전송"""
        user_message = self.input_field.text().strip()
        
        if not user_message:
            return
        
        # API 키 확인
        if not self.claude_api:
            self.add_system_message("❌ API 키가 설정되지 않았습니다.")
            return
        
        # 입력창 초기화
        self.input_field.clear()
        
        # 사용자 메시지 표시
        self.add_user_message(user_message)
        
        # 버튼 비활성화
        self.send_button.setEnabled(False)
        self.add_system_message("Claude가 응답을 생성하고 있습니다...")
        
        # 백그라운드에서 API 호출
        self.worker = ClaudeWorker(
            self.claude_api,
            user_message,
            self.cpp_rules
        )
        self.worker.response_ready.connect(self.on_response_ready)
        self.worker.error_occurred.connect(self.on_error)
        self.worker.start()
    
    def on_response_ready(self, response):
        """응답 수신 완료"""
        self.add_assistant_message(response)
        self.send_button.setEnabled(True)
    
    def on_error(self, error_message):
        """에러 발생"""
        self.add_system_message(f"❌ 오류: {error_message}")
        self.send_button.setEnabled(True)
    
    def clear_conversation(self):
        """대화 초기화"""
        reply = QMessageBox.question(
            self,
            "대화 초기화",
            "대화 기록을 모두 삭제하시겠습니까?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.claude_api.clear_history()
            self.chat_display.clear()
            self.add_system_message("대화가 초기화되었습니다.")


def main():
    app = QApplication(sys.argv)
    
    # 다크 모드 스타일 적용 (선택사항)
    app.setStyle("Fusion")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
