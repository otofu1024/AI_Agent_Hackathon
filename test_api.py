# test_api.py
import requests
import json

# APIのベースURL
BASE_URL = "http://localhost:8000"

def test_health_check():
    """ヘルスチェックテスト"""
    print("🔍 ヘルスチェックテスト...")
    
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ ヘルスチェック成功")
            print("📊 レスポンス:", response.json())
            return True
        else:
            print(f"❌ ヘルスチェック失敗: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ ヘルスチェックエラー: {e}")
        return False

def test_scenario_generation():
    """シナリオ生成テスト"""
    print("\n🔍 シナリオ生成テスト...")
    
    try:
        data = {"theme": "1920年代の怪事件"}
        response = requests.post(
            f"{BASE_URL}/api/scenarios/generate-outline",
            json=data
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ シナリオ生成成功")
            print("📖 生成されたシナリオ:")
            print(result["scenario"][:300] + "..." if len(result["scenario"]) > 300 else result["scenario"])
            return True
        else:
            print(f"❌ シナリオ生成失敗: {response.status_code}")
            print("📝 エラー詳細:", response.text)
            return False
    except Exception as e:
        print(f"❌ シナリオ生成エラー: {e}")
        return False

def test_description_enhancement():
    """描写強化テスト"""
    print("\n🔍 描写強化テスト...")
    
    try:
        data = {
            "text": "暗い部屋に机がある",
            "enhancement_type": "不気味で神秘的に"
        }
        response = requests.post(
            f"{BASE_URL}/api/scenarios/enhance-description",
            json=data
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ 描写強化成功")
            print("📝 元のテキスト:", result["original_text"])
            print("✨ 強化されたテキスト:", result["enhanced_text"])
            return True
        else:
            print(f"❌ 描写強化失敗: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 描写強化エラー: {e}")
        return False

def test_idea_generation():
    """アイデア生成テスト"""
    print("\n🔍 アイデア生成テスト...")
    
    try:
        data = {
            "context": "プレイヤーが謎の部屋に迷い込んだ",
            "idea_type": "脱出方法"
        }
        response = requests.post(
            f"{BASE_URL}/api/scenarios/generate-ideas",
            json=data
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ アイデア生成成功")
            print("💡 生成されたアイデア:")
            print(result["ideas"])
            return True
        else:
            print(f"❌ アイデア生成失敗: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ アイデア生成エラー: {e}")
        return False

if __name__ == "__main__":
    print("🚀 TRPGシナリオ作成支援ツール - APIテスト開始")
    print("=" * 60)
    
    # ヘルスチェック
    health_ok = test_health_check()
    
    if health_ok:
        # 各機能をテスト
        scenario_ok = test_scenario_generation()
        enhancement_ok = test_description_enhancement()
        idea_ok = test_idea_generation()
        
        if all([scenario_ok, enhancement_ok, idea_ok]):
            print("\n🎉 すべてのAPIテストが成功しました！")
        else:
            print("\n⚠️ 一部のテストに失敗しました")
    else:
        print("\n⚠️ ヘルスチェックに失敗しました")
        print("💡 アプリが起動しているか確認してください: uvicorn app.main:app --reload")
    
    print("=" * 60)
