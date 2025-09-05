# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.services.gemini_service import GeminiService
import logging

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPIアプリを作成
app = FastAPI(
    title="TRPGシナリオ作成支援ツール",
    description="AIを活用したTRPGシナリオ作成支援ツール",
    version="1.0.0"
)

# Geminiサービスを初期化
try:
    gemini_service = GeminiService()
    logger.info("Geminiサービスが正常に初期化されました")
except Exception as e:
    logger.error(f"Geminiサービスの初期化に失敗しました: {e}")
    gemini_service = None

# リクエスト用のデータクラス
class ScenarioRequest(BaseModel):
    theme: str

class EnhancementRequest(BaseModel):
    text: str
    enhancement_type: str = "魅力的"

class IdeaRequest(BaseModel):
    context: str
    idea_type: str = "展開案"

# ルートエンドポイント
@app.get("/")
async def root():
    return {
        "message": "TRPGシナリオ作成支援ツールへようこそ！",
        "status": "running",
        "version": "1.0.0"
    }

# ヘルスチェック
@app.get("/health")
async def health_check():
    if gemini_service is None:
        raise HTTPException(status_code=500, detail="Geminiサービスが利用できません")
    
    return {
        "status": "healthy",
        "gemini_service": "available"
    }

# シナリオ生成エンドポイント
@app.post("/api/scenarios/generate-outline")
async def generate_scenario_outline(request: ScenarioRequest):
    if gemini_service is None:
        raise HTTPException(status_code=500, detail="Geminiサービスが利用できません")
    
    try:
        # Geminiでシナリオを生成
        scenario = gemini_service.generate_scenario_outline(request.theme)
        
        return {
            "success": True,
            "theme": request.theme,
            "scenario": scenario
        }
    except Exception as e:
        logger.error(f"シナリオ生成中にエラーが発生しました: {e}")
        raise HTTPException(status_code=500, detail=f"シナリオ生成に失敗しました: {str(e)}")

# 描写強化エンドポイント
@app.post("/api/scenarios/enhance-description")
async def enhance_description(request: EnhancementRequest):
    if gemini_service is None:
        raise HTTPException(status_code=500, detail="Geminiサービスが利用できません")
    
    try:
        enhanced_text = gemini_service.enhance_description(
            request.text, 
            request.enhancement_type
        )
        
        return {
            "success": True,
            "original_text": request.text,
            "enhanced_text": enhanced_text
        }
    except Exception as e:
        logger.error(f"描写強化中にエラーが発生しました: {e}")
        raise HTTPException(status_code=500, detail=f"描写強化に失敗しました: {str(e)}")

# アイデア生成エンドポイント
@app.post("/api/scenarios/generate-ideas")
async def generate_ideas(request: IdeaRequest):
    if gemini_service is None:
        raise HTTPException(status_code=500, detail="Geminiサービスが利用できません")
    
    try:
        ideas = gemini_service.generate_ideas(
            request.context, 
            request.idea_type
        )
        
        return {
            "success": True,
            "context": request.context,
            "idea_type": request.idea_type,
            "ideas": ideas
        }
    except Exception as e:
        logger.error(f"アイデア生成中にエラーが発生しました: {e}")
        raise HTTPException(status_code=500, detail=f"アイデア生成に失敗しました: {str(e)}")

# アプリケーション起動時の処理
@app.on_event("startup")
async def startup_event():
    logger.info("TRPGシナリオ作成支援ツールが起動しました")

# アプリケーション終了時の処理
@app.on_event("shutdown")
async def shutdown_event():
    logger.info("TRPGシナリオ作成支援ツールが終了しました")
