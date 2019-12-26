# 静态资源存储库
* **img**

  用于储存图片文件。

* **music**

  用于储存音频文件。

* **cur**

  用于储存鼠标图片.cur文件。

* **blog_img**

  用于储存blog文章中引用的图片文件。

* **auto_pyscript**

  储存编写好的python脚本程序，用于与hexo配合自动更新页面代码，当music添加或删除音频文件时，会自动识别并在对应的ejs文件进行修改，以使音频文件能部署到站点上。

  - config.yaml

    用于配置对应的文件路径

  - MusTool.py

    用于手动添加或删除ejs对应的音频链接

  - DirListener.py

    全自动化处理，识别Music文件夹变化并作对应处理

  - status.code

    用于记录Music文件夹上一次的状态，若不存在在运行DirListen.py后将自动创建。

* **auto_deploy.bat**

  bat批处理文件，在auto_pyscript的基础上，更进一步的自动化，打开即自动完成github仓库更新推送，自动检测音频文件并作对应的处理，最后再重新部署hexo博客，一步到位。