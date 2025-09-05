# test_gemini.py
import os
from dotenv import load_dotenv

# 環境変数を読み込み
load_dotenv()

# Google Cloudの設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './key.json'

def test_gemini_connection():
    """Gemini接続テスト"""
    print("🔍 Gemini接続テストを開始します...")
    
    try:
        from vertexai.generative_models import GenerativeModel
        
        # Geminiモデルを初期化
        model = GenerativeModel("gemini-1.5-flash")
        print("✅ Geminiモデルの初期化に成功しました")
        
        # 簡単なテスト
        response = model.generate_content("こんにちは、テストです。短く返答してください。")
        print("✅ 接続成功！")
        print("📝 レスポンス:", response.text)
        
        return True
        
    except Exception as e:
        print("❌ エラーが発生しました:", str(e))
        print("💡 対処法:")
        print("   1. key.jsonファイルが正しい場所にあるか確認")
        print("   2. Google CloudプロジェクトIDが正しいか確認")
        print("   3. Vertex AI APIが有効になっているか確認")
        return False

def test_gemini_service():
    """Geminiサービステスト"""
    print("\n🔍 Geminiサービステストを開始します...")
    
    try:
        from app.services.gemini_service import GeminiService
        
        # サービスを初期化
        service = GeminiService()
        
        # シナリオ生成テスト
        print("📝 シナリオ生成テスト...")
        scenario = service.generate_scenario_outline("ファンタジー冒険")
        print("✅ シナリオ生成成功！")
        print("📖 生成されたシナリオ:")
        print(scenario[:200] + "..." if len(scenario) > 200 else scenario)
        
        return True
        
    except Exception as e:
        print("❌ エラーが発生しました:", str(e))
        return False

if __name__ == "__main__":
    print("🚀 TRPGシナリオ作成支援ツール - テスト開始")
    print("=" * 50)
    
    # 接続テスト
    connection_ok = test_gemini_connection()
    
    if connection_ok:
        # サービステスト
        service_ok = test_gemini_service()
        
        if service_ok:
            print("\n🎉 すべてのテストが成功しました！")
            print("💡 次のステップ: uvicorn app.main:app --reload でアプリを起動してください")
        else:
            print("\n⚠️ サービステストに失敗しました")
    else:
        print("\n⚠️ 接続テストに失敗しました")
    
    print("=" * 50)
