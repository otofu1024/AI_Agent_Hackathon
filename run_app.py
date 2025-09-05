# run_app.py
import uvicorn
import os
from dotenv import load_dotenv

# 環境変数を読み込み
load_dotenv()

if __name__ == "__main__":
    print("🚀 TRPGシナリオ作成支援ツールを起動します...")
    print("=" * 50)
    print("📝 アクセスURL: http://localhost:8000")
    print("📚 API仕様: http://localhost:8000/docs")
    print("🔍 ヘルスチェック: http://localhost:8000/health")
    print("=" * 50)
    
    # アプリを起動
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # 開発モード（ファイル変更時に自動再起動）
        log_level="info"
    )
