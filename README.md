**Image Downloader V3.0更新内容：**

-添加了通过响应标头来判断是否是有效图片的功能<br>
-添加了开发模式<br>
-添加了单个图片或多个图片的选项<br>
-添加了单个图片下载完成后的预览功能<br>
-添加了退出返回码<br>
-添加了程序信息显示<br>
-修复了download.single.image()和download_multiple_images()可能存在的递归错误问题<br>
-移除了if __name__ == "__main__"判断<br>
-单个图片下载可以显示响应标头<br>
-优化了终端输出内容<br>
-使用os.path.join(save_folder, file_name)创建文件路径<br>
-修改了”请输入图片的URL“输入框提示
