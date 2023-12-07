import os
import subprocess
import textwrap
from PIL import Image, ImageDraw, ImageFont
import importlib
import configparser

# Import the necessary function from the specified module
config = configparser.ConfigParser()
config.read('config.txt')
reader_module_name = config.get('key', 'readbook', fallback='readYiJing')
reader_module = importlib.import_module(reader_module_name[:-3])

def text_to_image(text, font_size=36, output_path='output.png', line_width=15):
    # 创建一个明信片背景图片
    postcard_path = "postcard.jpg"  # Replace with the path to your postcard image file
    postcard = Image.open(postcard_path)
    width, height = postcard.size

    # 获取字体
    font_path = "simhei.ttf"  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # 创建一个可绘制的对象
    draw = ImageDraw.Draw(postcard)

    # 自动换行
    wrapped_text = textwrap.fill(text, width=line_width)

    # 计算文本在图片中的位置
    text_width, text_height = draw.textsize(wrapped_text, font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # 将文本写入图片
    draw.text((x, y), wrapped_text, font=font, fill='black')

    # 保存图片，添加 force=True 参数
    postcard.save(output_path)


def combine_image_audio(image_path, audio_path, output_path='output.mp4', duration=5):
    # 检查输出文件是否存在，如果存在则删除（添加 overwrite=True 参数）
    if os.path.exists(output_path):
        os.remove(output_path)

    # 使用 FFmpeg 将图片和音频合成为视频
    cmd = [
        'ffmpeg',
        '-y',  # 强制覆盖输出文件
        '-loop', '1', '-i', image_path,
        '-i', audio_path,
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-strict', 'experimental',
        '-b:a', '192k',
        '-t', str(duration),  # 设置视频时长
        output_path
    ]
    subprocess.run(cmd)


def generate_postcard():
    key, value = reader_module.get_key_value_by_index()
    text_to_image(value, output_path='output.png')
    combine_image_audio('output.png', 'temp.wav', output_path='output_video.mp4', duration=10)


if __name__ == '__main__':
    generate_postcard()
