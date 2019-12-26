::提交更新到github
call git add .
call git commit -m "update"
call git push origin master

::启用python修改ejs文件
cd auto_pyscript
call python DirListener.py

::部署博客系统
cd ../../iblog
call auto-deploy.bat