from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://creator.douyin.com/")
    page.get_by_text("登录").click()
    page.goto("https://creator.douyin.com/creator-micro/home")
    page.get_by_text("内容管理").click()
    page.locator("li").filter(has_text=re.compile(r"^作品管理$")).click()
    page.get_by_role("button", name="发布作品").click()
    page.locator("label").click()
    page.locator("body").set_input_files("temp.mp4")
    page.get_by_placeholder("好的作品标题可获得更多浏览").click()
    page.get_by_placeholder("好的作品标题可获得更多浏览").fill("123")
    page.locator(".zone-container").click()
    page.locator(".zone-container").fill("#三国杀​")
    page.get_by_text("三国杀斗地主").click()
    page.locator(".zone-container").fill("​ #三国杀斗地主  #三国杀​")
    page.get_by_text("三国杀移动版", exact=True).click()
    page.locator(".zone-container").fill("​ #三国杀斗地主  ​ #三国杀移动版  #游戏​")
    page.get_by_text("游戏", exact=True).click()
    page.get_by_text("为进度条增加章节信息").click()
    page.locator("div").filter(has_text=re.compile(r"^选择封面$")).nth(2).click()
    page.get_by_text(":00优质封面提示封面有精炼的文字能吸引更多人浏览").click()
    page.get_by_text("上传封面").click()
    page.locator("#dialog-0").get_by_role("img").nth(1).click()
    page.get_by_text("请选择合集").click()
    page.locator("#garfish_app_for_content_cbvkb02d #root div").filter(has_text="作品描述3/30").nth(2).click()
    page.get_by_text("请选择合集").click()
    page.get_by_role("option", name="易经").click()
    page.get_by_text("第1集", exact=True).click()
    page.get_by_role("option").get_by_text("第1集").click()
    page.locator("div").filter(has_text=re.compile(r"^今日头条提示：打开同步开关可以同步内容至头条绑定账号$")).get_by_role("switch").uncheck()
    page.locator("div").filter(has_text=re.compile(r"^今日头条提示：打开同步开关可以同步内容至头条绑定账号$")).get_by_role("switch").check()
    page.get_by_text("+").click()
    page.get_by_role("tab", name="游戏").click()
    page.locator(".semi-tabs-bar-arrow-end > .semi-button").click()
    page.locator(".semi-sidesheet-header > .semi-button").click()
    page.get_by_text("+").click()
    page.get_by_role("tab", name="游戏").click()
    page.get_by_role("tab", name="美食").click()
    page.get_by_role("tab", name="时尚").click()
    page.get_by_role("tab", name="文化教育").click()
    page.locator("div:nth-child(2) > .checkbox--1BFlY > .semi-checkbox > .semi-checkbox-inner > .semi-checkbox-inner-display > .semi-icons").click()
    page.get_by_text("确认", exact=True).click()
    page.get_by_text("点击输入热点词").click()
    page.locator("div").filter(has_text=re.compile(r"^点击输入热点词$")).first.click()
    page.get_by_text("点击输入热点词").click()
    page.locator("#garfish_app_for_content_cbvkb02d #root div").filter(has_text="作品描述3/30").nth(2).click()
    page.locator("#garfish_app_for_content_cbvkb02d #root div").filter(has_text="作品描述3/30").nth(2).click()
    page.locator("#garfish_app_for_content_cbvkb02d div").filter(has_text=re.compile(r"^易经$")).first.press("Escape")
    page.get_by_text("#游戏").first.click()
    page.locator(".zone-container").press("Escape")
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
