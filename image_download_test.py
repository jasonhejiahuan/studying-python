import requests
import os
import hashlib
import shutil
import random
import string

os.system("clear") #执行时清屏

def calculate_self_hash():
    # 获取当前脚本的文件名
    script_filename = os.path.abspath(__file__)

    # 读取文件内容
    with open(script_filename, 'rb') as f:
        file_content = f.read()

    # 计算MD5哈希值
    md5_hash = hashlib.md5(file_content).hexdigest()

    return md5_hash

def generate_random_prefix(length=8):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def update_self():
    # 获取当前脚本的文件名
    script_filename = os.path.abspath(__file__)

    # 创建备份文件夹
    backup_folder = "ota_backup"
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # 生成随机前缀
    random_prefix = generate_random_prefix()

    # 创建备份文件名
    backup_filename = os.path.join(backup_folder, f"{random_prefix}_{os.path.basename(script_filename)}")

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
    if hash_response.status_code == 200:
        print("成功获取线上版本的MD5哈希值")
    else:
        print("\033[1;31m获取线上版本的MD5哈希值失败\033[0m")
    expected_hash = hash_response.text.strip()
    print(f"线上版本的MD5哈希值为：{expected_hash}")

    # 检查当前脚本的MD5哈希值是否与预期值匹配
    if calculate_self_hash() != expected_hash:
        print("有新版本可用，正在更新脚本...")
        # 执行更新后的脚本文件
        os.system(f"python3 {script_filename}")
    else:
        print("\033[1;42m现在是最新版本\033[0m")


print(f"这个程序的MD5哈希值为: {calculate_self_hash()}")
update_self()

# 检查当前目录下是否存在saves文件夹，如果不存在则创建
if not os.path.exists('saves'):
    os.makedirs('saves')
# 切换到saves文件夹
os.chdir('saves')
print("请在" + "saves" + "目录查看下载好的图片")

# 让用户输入
global_image_url = input("请输入图片的URL：")
name_prefix = input("请输入图片的前缀：")

# 检查当前目录下是否存在name_prefix文件夹，如果不存在则创建
if not os.path.exists(name_prefix):
    os.makedirs(name_prefix)

# 切换到name_prefix文件夹
os.chdir(name_prefix)


#选项1:下载单张图片
def download_single_image():


    # 定义图片名
    file_name = global_image_url.split('/')[-1]
    print("原始名称：" + file_name)
    # 发送GET请求获取图片数据
    response = requests.get(global_image_url)

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
    download_single_image()



# 选项2:下载多张图片
def download_multiple_images():
    print("你输入的URL是" + global_image_url)
    print("请确保你输入的URL不包括图片本身，而是图片前面的路径")
    # 让用户输入图片名称范围
    file_name_min = int(input("请输入图片名称NUMBER最小值："))
    file_name_max = int(input("请输入图片名称NUMBER最大值："))
    # 让用户输入图片格式
    file_format = input("请输入图片格式，不包括点，比如png：")
    for file_name in range(file_name_min, file_name_max + 1): #遍历所有可能要下载的图片名称NUMBER
        image_url = global_image_url + str(file_name) + "." + file_format
        print("正在下载图片" + str(file_name) + "." + file_format)
        # 发送GET请求获取图片数据
        response = requests.get(image_url)
        # 保存图片到文件夹
        with open (name_prefix + str(file_name) + "." + file_format, 'wb') as f:
            f.write(response.content)
    # 检测目录下是否有图片
    print(os.listdir())
    # 将输出内容存为列表
    files = os.listdir()
    # 输出图片下载成功
    print("\033[32m图片下载成功\033[0m")
    # 输出图片名
    print("图片名为：" + str(file_name) + "." + file_format)
    # 输出图片大小
    print("图片大小为：" + str(len(response.content)) + "字节")
    # 输出图片格式
    print("图片格式为：" + file_format)
    for file_name in files:
        print("图片名为：" + file_name)
        print("图片大小为：" + str(os.path.getsize(file_name)) + "字节")
        print("图片格式为：" + file_name.split('.')[-1])
    print("共下载了" + str(len(files)) + "张图片")



download_multiple_images()
