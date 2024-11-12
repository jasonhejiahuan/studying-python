import requests
import os
import hashlib
import shutil
import random
import string
import sys
from PIL import Image
import matplotlib.pyplot as plt

print("JASON Studio")
print("made by Jason")

dev_mode = True #设置这里，打开开发模式，避免自动覆盖开发版！！！！！！！




disalow_update = False

if dev_mode:
    disalow_update = True
    print()
    print("\033[96mHello, world!\033[0m")
    print()
    print("\033[096m当前处于开发模式！！！\033[0m")

if dev_mode:
    print("\033[95m已阻止自动清屏\033[0m") # 打印红色文字
    pass
else:
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

if disalow_update:
    print("\033[95m已跳过自动更新\033[0m")
    print(f"当前脚本的MD5哈希值为：{calculate_self_hash()}")
    pass
else:
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


if dev_mode:
    print()




print("================================")

print("Image Downloader")
print("·Made By Jason")
print("""
          @                                                 
          @                                                 
          @                                                 
          @                                                 
          @                                                 
          @                                                 
          @@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@@@@@         
          @       @       @               @       @         
          @       @       @@@@@@@@        @       @@@@@@@@@ 
          @       @              @        @       @       @ 
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@       @
""")

print("================================")

# 检查当前目录下是否存在saves文件夹，如果不存在则创建
if not os.path.exists('saves'):
    os.makedirs('saves')
# 切换到saves文件夹
os.chdir('saves')
print("请在" + "saves" + "目录查看下载好的图片")

# 让用户输入
global_image_url = input("""请输入图片的URL
（如果是下载单张图片，则直接填入全部链接，如果是多张，则填入图片前的链接，包括最后一个/）：""")
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
    
    # 构建保存目录路径并创建文件夹
    save_folder = os.path.join('saves', name_prefix)
    os.makedirs(save_folder, exist_ok=True)
    
    # 构建图片保存路径
    save_path = os.path.join(save_folder, file_name)

    # 发送 GET 请求获取图片数据
    response = requests.get(global_image_url)
    if response.status_code == 200:
        print("\033[32m成功下载图片\033[0m" + str(file_name))
        # 保存图片到文件夹
        with open(save_path, 'wb') as f:
            f.write(response.content)

        # 使用保存路径打开图片
        img = Image.open(save_path)
        # 获取图片的宽度和高度
        width, height = img.size
        # 输出图片的宽度和高度
        print("\033[1m图片的宽度为：" + str(width) + "像素\033[0m")
        print("\033[1m图片的高度为：" + str(height) + "像素\033[0m")

        


        # 输出图片信息
        print("\033[1m图片名为：" + file_name + "\033[0m")
        print("\033[1m图片大小为：" + str(len(response.content)) + "字节\033[0m")
        print("\033[1m图片格式为：" + file_name.split('.')[-1] + "\033[0m")

        print(f"\033[94m响应标头为：{response.headers}\033[0m")
        # 显示图片
        plt.imshow(img, cmap="gray")
        #plt.axis('off')  # 不显示坐标轴
        plt.show()
    else:
        print("\033[31m下载失败，状态码:\033[0m", response.status_code)
        sys.exit(2)




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
        if response.status_code == 200:
            print("\033[32m成功下载图片\033[0m" + str(file_name) + "." + file_format)
            # 保存图片到文件夹
            with open (name_prefix + str(file_name) + "." + file_format, 'wb') as f:
                f.write(response.content)
    # 检测目录下是否有图片
    print(os.listdir())
    # 将输出内容存为列表
    files = os.listdir()
    # 输出图片下载成功
    print("\033[32m图片下载成功\033[0m")


    print("共下载了" + str(len(files)) + "张图片")
    print("正在清除无效图片...")
    #清除saves文件夹中文件太小的图片
    for file_name in files:
        if os.path.getsize(file_name) < 5000:
            os.remove(file_name)
            print("已删除无效图片：" + file_name)

#运行
run_mode = input("请输入运行模式（1:下载单张图片，2:下载多张图片）：")
if run_mode == "1":
    download_single_image()
elif run_mode == "2":
    download_multiple_images()
else:
    print("输入错误，请重新运行程序")
    sys.exit(1)

sys.exit(0)