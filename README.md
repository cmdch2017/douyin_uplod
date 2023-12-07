# douyin_uplod
项目比起原项目借用了其playwright保存cookie文件
易经文字转图片，图片转视频，视频推送抖音
![image](https://github.com/cmdch2017/douyin_uplod/assets/32605664/edd49ec5-3d4c-4303-82fd-dab67e15a61e)
不会写代码用
playwright codegen -o script.py 

# 原理
1、通过playwright发布合成的视频

# 技术栈
- python
- playwright
- ffmpeg


```python
pip install ffmpy
pip install playwright
python -m playwright install
```
- 然后通过playwright把cookie文件保存下来，执行以下命令，扫码登录完成后即可

```python
playwright codegen www.douyin.com --save-storage=cookie.json
```
- ffmpeg需要添加到环境变量，如不添加需要修改`ffmpeg.exe`目录`ctrl+左键点击ffmpeg`进入，把`executable='ffmpeg.exe'`修改成你`下载ffmpeg`的目录

```python
def __init__(
        self, executable=r'E:\ffmpeg\ffmpeg-5.0.1-essentials_build\bin\ffmpeg.exe', global_options=None, inputs=None, outputs=None
    )
```
# 改进建议
**此程序有非常多的待改善部分，可玩性非常高，示例如下：**
- 改进一：如何判断视频是否发送成功呢，当然不是傻等了
    - 方式一：通过`page.wait_for_url()`
    ```python
    try:
        await page.wait_for_url("https://creator.douyin.com/creator-micro/content/manage",
                                timeout=1500)
        print("视频发布成功")
    except Exception as e:
        print("判断视频是否发布成功")
    ```
    - 方式二：通过获取网页的msg消息
    ```python
    await page.locator('button.button--1SZwR:nth-child(1)').click()
    msg = await page.locator('//*[@class="semi-toast-content-text"]').all_text_contents()
                            for msg_txt in msg:
                                print("实时消息：" + msg_txt)
    ```
- 改进二：如何判断用户是否登录了呢？
    - 通过登录按钮判断，未登录会有登录按钮，登录了就没有登录按钮
    ```python
        try:
            await page.goto("https://creator.douyin.com/creator-micro/content/upload")
            await page.locator(".login").click(timeout=1500)
            print("未登录")
        except Exception as e:
            print("已登录")
    ```
- 改进三：如何添加话题？
    - 分析：首先要从视频文件中取出视频名并把`#xxx `这种格式的取出来，然后剩余的部分作为视频标题
    - 参考下面代码，注：话题命名格式必须严格参照`#+话题名+空格`此格式
    - 此方式不完美，只支持话题在前面的，否则会报错
    ```python
    import re
    video_desc = "#风景 #夕阳 落霞与孤鹜齐飞，秋水共长天一色"
    r = r"#.* "
    rs = re.search(r, video_desc).group()
    video_desc_tag = rs[:-1].split(" ")  # ["#风景", "#夕阳"]
    video_desc2 = video_desc[len(rs):]  # 落霞与孤鹜齐飞，秋水共长天一色
    
    css_selector = ".zone-container"
    tag_index = 0
    for tag in video_desc_tag:
        tag_index += 1
        print("正在添加第%s个话题" % tag_index)
        await page.type(css_selector, tag)
        await page.press(css_selector, "Space")
    await page.type(css_selector, video_desc2)
    print("视频标题输入完毕，等待发布")
    ```
    - 完美解决方式，不管话题在前面或者后面或者中间或者无话题或者N个话题都完美适用
    ```python
    video_desc = "#前面话题1 #前面话题2 落霞与孤鹜齐飞#中间话题1 秋水共#中间话题2 长天一色#后面话题1 #后面话题2 "
    video_desc_tag = []
    tag_rs = re.findall(r"(#.*? )", video_desc)
    if len(tag_rs) > 0:
        if len(tag_rs) > 1:
            video_desc = video_desc[:-1]
        video_desc_tag = video_desc.split(" ")
        print("该视频有话题")
    else:
        video_desc_tag.append(video_desc)
        print("该视频没有检测到话题")
    tag_index = 0
    for tag in video_desc_tag:
        tag_index += 1
        if tag.find("#") > 0:  # 代表话题在中间的处理方式
            print("正在添加第%s个话题" % tag_index)
            await page.type(css_selector, tag)
            await page.press(css_selector, "Space")
        elif tag.find("#") == 0:  # 代表话题在前面或者后面的处理方式
            print("正在添加第%s个话题" % tag_index)
            await page.type(css_selector, tag_rs[tag_index - 1])
            await page.press(css_selector, "Space")
        elif tag.find("#") == -1:  # 代表无话题的处理方式
            await page.type(css_selector, tag)
    print("视频标题输入完毕，等待发布")
    ```
    - 是我想复杂了，直接按空格分割即可，参考下面示例
    ```python
    video_desc = "#前面话题1 #前面话题2 落霞与孤鹜齐飞#中间话题1 秋水共#中间话题2 长天一色#后面话题1 #后面话题2 "
    video_desc_tag = []
    tag_rs = re.findall(r"(#.*? )", video_desc)
    if len(tag_rs) > 0:
        if len(tag_rs) > 1:
            video_desc = video_desc[:-1]
        video_desc_tag = video_desc.split(" ")
        print("该视频有话题")
    else:
        video_desc_tag.append(video_desc)
        print("该视频没有检测到话题")
    tag_index = 0
    for tag in video_desc_tag:
        tag_index += 1
        print("正在添加第%s个话题" % tag_index)
        await page.type(css_selector, tag)
        await page.press(css_selector, "Space")
    print("视频标题输入完毕，等待发布")
    ```
![示例图片](https://raw.githubusercontent.com/Superheroff/douyin_uplod/main/tag.png)

