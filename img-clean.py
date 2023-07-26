import os
import re

def get_referenced_images(markdown_path):
    with open(markdown_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # 使用正则表达式提取Markdown中的图片引用
        referenced_images = re.findall(r'\!\[.*\]\((.*?)\)', content)
    return referenced_images

def remove_unused_images(posts_path, assets_path):
    referenced_images = set()

    # 遍历所有Markdown文件，获取被引用的图片列表
    for root, _, files in os.walk(posts_path):
        for file in files:
            if file.endswith('.md'):
                markdown_path = os.path.join(root, file)
                referenced_images.update(get_referenced_images(markdown_path))

    # 遍历assets目录，删除未被引用的图片
    for root, _, files in os.walk(assets_path):
        for file in files:
            image_path = os.path.join(root, file)
            if image_path not in referenced_images:
                os.remove(image_path)
                print(f'Removed: {image_path}')

if __name__ == '__main__':
    posts_path = './_posts'
    assets_path = './_posts/assets'
    remove_unused_images(posts_path, assets_path)
