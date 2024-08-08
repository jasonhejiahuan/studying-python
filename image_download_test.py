import requests
import os
import hashlib
import shutil

def calculate_self_hash():
    # 获取当前脚本的文件名
    script_filename = os.path.abspath(__file__)

    # 读取文件内容
    with open(script_filename, 'rb') as f:
        file_content = f.read()

    # 计算MD5哈希值
    md5_hash = hashlib.md5(file_content).hexdigest()

    return md5_hash

def update_self():
    # 获取当前脚本的文件名
    script_filename = os.path.abspath(__file__)

    # 创建备份文件夹
    backup_folder = "ota_backup"
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # 创建备份文件名
    backup_filename = os.path.join(backup_folder, os.path.basename(script_filename))

    # 备份当前脚本
    shutil.copy(script_filename, backup_filename)

    # 下载更新后的脚本文件
    url = "https://raw.githubusercontent.com/jasonhejiahuan/studying-python/main/image_download_test.py"
    response = requests.get(url)
    with open(script_filename, 'wb') as f:
        f.write(response.content)

    # 下载预期的MD5哈希值
    hash_url = "https://raw.githubusercontent.com/jasonhejiahuan/studying-python/main/image_download_test.py-md5.txt"
    hash_response = requests.get(hash_url)
    expected_hash = hash_response.text.strip()
    print(f"线上版本的MD5哈希值为：", expected_hash)

    # 检查当前脚本的MD5哈希值是否与预期值匹配
    if calculate_self_hash() != expected_hash:
        print("有新版本可用，正在更新脚本...")
        # 执行更新后的脚本文件
        os.system(f"python {script_filename}")
    else:
        print("\033[32m更新完成\033[0m")

def ota():
    print(f"这个程序的MD5哈希值为: {calculate_self_hash()}")
    update_self()

def download_image():
    # 检查当前目录下是否存在saves文件夹，如果不存在则创建
    if not os.path.exists('saves'):
        os.makedirs('saves')
    # 切换到saves文件夹
    os.chdir('saves')

    # 让用户输入
    image_url = input("请输入图片的URL：")
    name_prefix = input("请输入图片的前缀：")

    # 检查当前目录下是否存在name_prefix文件夹，如果不存在则创建
    if not os.path.exists(name_prefix):
        os.makedirs(name_prefix)

    # 切换到name_prefix文件夹
    os.chdir(name_prefix)

    # 定义图片名
    file_name = image_url.split('/')[-1]
    print("原始名称：" + file_name)
    # 发送GET请求获取图片数据
    response = requests.get(image_url)

    # 保存图片到文件夹
    with open (name_prefix + file_name, 'wb') as f:
        f.write(response.content)

    # 检测目录下是否有图片
    print(os.listdir())
    # 将输出内容存为列表
    files = os.listdir()
    # 输出图片下载成功
    print("\033[32m图片下载成功\033[0m")
    # 输出图片名
    print("图片名为：" + file_name)
    # 输出图片大小
    print("图片大小为：" + str(len(response.content)) + "字节")
    # 输出图片格式
    print("图片格式为：" + file_name.split('.')[-1])

if __name__ == "__main__":
    ota()
    download_image()
