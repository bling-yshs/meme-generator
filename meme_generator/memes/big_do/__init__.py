from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def big_do(images: list[BuildImage], texts, args):
    # 将图片转换为圆形，并且缩放为60x60
    user_head = images[0].convert('RGBA').circle().resize((60, 60))
    frames: list[IMG] = []

    # 第一帧
    frame = BuildImage.open(img_dir / f"1.png") 
    frame.paste(user_head, (25, 21), alpha=True)
    frames.append(frame.image)

    # 第二帧
    frame = BuildImage.open(img_dir / f"2.png")
    frame.paste(user_head, (24, 20), alpha=True)
    frames.append(frame.image)

    # 第三帧
    frame = BuildImage.open(img_dir / f"3.png")
    frame.paste(user_head, (24, 20), alpha=True)
    frames.append(frame.image)

    # 第四帧
    frame = BuildImage.open(img_dir / f"4.png")
    frame.paste(user_head, (24, 20), alpha=True)
    frames.append(frame.image)

    # 第五帧
    frame = BuildImage.open(img_dir / f"5.png") 
    frame.paste(user_head, (25, 21), alpha=True)
    frames.append(frame.image)

    # 第六帧
    frame = BuildImage.open(img_dir / f"6.png")
    frame.paste(user_head, (26, 22), alpha=True)
    frames.append(frame.image)

    # 第七帧
    frame = BuildImage.open(img_dir / f"7.png")
    frame.paste(user_head, (27, 23), alpha=True)
    frames.append(frame.image)

    # 第八帧
    frame = BuildImage.open(img_dir / f"8.png")
    frame.paste(user_head, (27, 23), alpha=True)
    frames.append(frame.image)

    # 第九帧
    frame = BuildImage.open(img_dir / f"9.png")
    frame.paste(user_head, (26, 22), alpha=True)
    frames.append(frame.image)

    # 第十帧
    frame = BuildImage.open(img_dir / f"10.png")
    frame.paste(user_head, (25, 21), alpha=True)
    frames.append(frame.image)

    return save_gif(frames, 0.05)


add_meme(
    "big_do",
    big_do,
    min_images=1,
    max_images=1,
    keywords=["大撅", "狠狠地撅"],
    date_created=datetime(2025, 1, 10),
    date_modified=datetime(2025, 1, 10),
)
