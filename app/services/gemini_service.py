# app/services/gemini_service.py
import os
from vertexai.generative_models import GenerativeModel
from dotenv import load_dotenv

# 環境変数を読み込み
load_dotenv()

class GeminiService:
    def __init__(self):
        # 環境変数を設定
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './key.json'
        
        # Geminiモデルを初期化
        self.model = GenerativeModel("gemini-2.5-flash-lite")
        print("✅ Geminiサービスが初期化されました")
    
    def generate_text(self, prompt: str) -> str:
        """テキストを生成する"""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"エラーが発生しました: {str(e)}"
    
    def generate_scenario_outline(self, theme: str) -> str:
        """シナリオの骨子を生成する"""
        prompt = f"""
        以下のテーマでTRPGシナリオの骨子を作成してください：
        
        テーマ: {theme}
        
        以下の要素を含めてください：
        1. シナリオの概要
        2. 主要なプロットポイント
        3. 主要NPC
        4. 舞台設定
        
        日本語で回答してください。
        """
        
        return self.generate_text(prompt)
    
    def enhance_description(self, text: str, enhancement_type: str = "魅力的") -> str:
        """描写を強化する"""
        prompt = f"""
        以下のテキストを{enhancement_type}に強化してください：
        
        {text}
        
        より魅力的で没入感のある描写にしてください。
        """
        
        return self.generate_text(prompt)
    
    def generate_ideas(self, context: str, idea_type: str = "展開案") -> str:
        """アイデアを生成する"""
        prompt = f"""
        以下のコンテキストに基づいて、{idea_type}を3つ提案してください：
        
        {context}
        
        各アイデアは簡潔で実用的なものにしてください。
        """
        
        return self.generate_text(prompt)
