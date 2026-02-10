"""
Claude API 통신 모듈
"""
import os
from anthropic import Anthropic


class ClaudeAPI:
    def __init__(self, api_key: str):
        """
        Claude API 클라이언트 초기화
        
        Args:
            api_key: Claude API 키
        """
        self.api_key = api_key
        self.client = Anthropic(api_key=api_key)
        self.conversation_history = []
        
    def send_message(self, user_message: str, system_prompt: str = None) -> str:
        """
        Claude에게 메시지를 보내고 응답을 받습니다.
        
        Args:
            user_message: 사용자 메시지
            system_prompt: 시스템 프롬프트 (선택)
            
        Returns:
            Claude의 응답 텍스트
        """
        try:
            # 대화 기록에 사용자 메시지 추가
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            # API 호출
            if system_prompt:
                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=4096,
                    system=system_prompt,
                    messages=self.conversation_history
                )
            else:
                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=4096,
                    messages=self.conversation_history
                )
            
            # 응답 추출
            assistant_message = response.content[0].text
            
            # 대화 기록에 어시스턴트 응답 추가
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            return f"오류 발생: {str(e)}"
    
    def clear_history(self):
        """대화 기록 초기화"""
        self.conversation_history = []
    
    def get_history(self):
        """대화 기록 반환"""
        return self.conversation_history
