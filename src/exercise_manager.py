"""
연습 문제 관리 모듈
"""
import json
import os


class ExerciseManager:
    def __init__(self, data_file="data/exercises.json"):
        """
        연습 문제 관리자 초기화
        
        Args:
            data_file: 연습 문제 데이터 파일 경로
        """
        self.data_file = data_file
        self.exercises = self.load_exercises()
        self.levels = ["초급", "초급후반", "중급초반", "중급", "중급후반"]
    
    def load_exercises(self):
        """연습 문제 데이터 로드"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def get_levels(self):
        """난이도 목록 반환"""
        return self.levels
    
    def get_exercises_by_level(self, level):
        """
        특정 난이도의 연습 문제 목록 반환
        
        Args:
            level: 난이도 (초급, 초급후반, 중급초반, 중급, 중급후반)
            
        Returns:
            연습 문제 리스트
        """
        return self.exercises.get(level, [])
    
    def get_exercise_prompt(self, level, index):
        """
        연습 문제를 Claude에게 전달할 프롬프트 형식으로 반환
        
        Args:
            level: 난이도
            index: 문제 인덱스 (0부터 시작)
            
        Returns:
            프롬프트 문자열
        """
        exercises = self.get_exercises_by_level(level)
        
        if index >= len(exercises):
            return None
        
        exercise = exercises[index]
        
        prompt = f"""
[연습 문제: {exercise['title']}]

난이도: {level}

문제 설명:
{exercise['description']}

예제:
{exercise['example']}

힌트:
{exercise['hint']}

---
위 문제를 풀어주세요. 
C++ 규칙에 따라 코드를 작성하고, 왜 그런 선택을 했는지 설명해주세요.
        """
        
        return prompt
