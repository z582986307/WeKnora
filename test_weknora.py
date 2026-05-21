from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    try:
        print("正在访问前端页面...")
        page.goto('http://127.0.0.1:5173', timeout=15000)
        page.wait_for_load_state('networkidle', timeout=15000)
        
        print(f"页面标题: {page.title()}")
        print(f"页面 URL: {page.url}")
        
        # 截图
        page.screenshot(path='/workspace/test_screenshot.png', full_page=True)
        print("截图已保存")
        
        # 检查页面内容
        content = page.content()
        if "WeKnora" in content:
            print("✅ 页面包含 WeKnora 内容")
        else:
            print("⚠️ 页面可能没有正确加载")
            
    except Exception as e:
        print(f"访问出错: {e}")
    finally:
        browser.close()
