# -*- coding: utf-8 -*-
import asyncio

from playwright.async_api import Playwright, async_playwright
from 读取易经 import get_key_value_by_index,increment_and_get_index
from createPicture import generate_postcard


class set_video(object):
    def __init__(self):
        key, value = get_key_value_by_index()
        self.title_text = key
        self.path = r'C:\Demos\douyin_uplod'  # 资源目录


class pw(set_video):
    def __init__(self):
        super(pw, self).__init__()

    async def upload(self, playwright: Playwright) -> None:
        browser = await playwright.chromium.launch(headless=False)

        context = await browser.new_context(storage_state=self.path + "\\cookie.json")

        page = await context.new_page()

        await page.goto("https://creator.douyin.com/creator-micro/content/upload")

        await page.wait_for_url("https://creator.douyin.com/creator-micro/content/upload")

        await page.locator(
            "label:has-text(\"点击上传 或直接将视频文件拖入此区域为了更好的观看体验和平台安全，平台将对上传的视频预审。超过40秒的视频建议上传横版视频\")").set_input_files(
            "output_video.mp4")
        await page.wait_for_timeout(10000)
        # 标题
        await page.get_by_placeholder("好的作品标题可获得更多浏览").click()
        await page.get_by_placeholder("好的作品标题可获得更多浏览").fill(self.title_text)
        # 添加话题
        await page.locator(".zone-container").click()
        await page.locator(".zone-container").fill("#易经​")
        await page.get_by_text("易经").click()
        await page.locator(".zone-container").fill("​ #易经  #中国传统文化​")
        await page.get_by_text("中国传统文化", exact=True).click()
        await page.locator(".zone-container").fill("​ #易经  ​ #中国传统文化  #玄学​")
        await page.get_by_text("玄学", exact=True).click()

        # 作品活动奖励
        await page.get_by_text("+").click()
        await page.get_by_role("tab", name="文化教育").click()
        await page.locator(
            "div:nth-child(2) > .checkbox--1BFlY > .semi-checkbox > .semi-checkbox-inner > .semi-checkbox-inner-display > .semi-icons").click()
        await page.get_by_text("确认", exact=True).click()

        # 添加到
        # await page.get_by_text("请选择合集").click()
        # await page.get_by_role("option", name="易经").click()

        # 允许他人保存视频
        await page.locator("label").filter(has_text="不允许").click()
        await page.get_by_role("button", name="发布", exact=True).click()
        increment_and_get_index()

        await context.storage_state(path=self.path + "\\cookie.json")
        await page.wait_for_timeout(20000)
        await context.close()
        await browser.close()

    async def main(self):
        async with async_playwright() as playwright:
            await self.upload(playwright)


def job_1():
    generate_postcard()
    app = pw()
    asyncio.run(app.main())


if __name__ == '__main__':
    # scheduler = BlockingScheduler(timezone='Asia/Shanghai')
    # scheduler.add_job(job_1, 'cron', day='1-31', hour='5', minute='20', misfire_grace_time=180)
    # scheduler.start()
    job_1()
