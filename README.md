# OnlineBookStore_backend
2021.1.10 计算机网络实验--网上书店

### 主要框架
- 服务器: 腾讯云轻量级服务器
- 系统: CentOS 7
- 代理服务器: Nginx(处理静态请求)
- 通信协议: uWSGI(Nginx与Django的桥梁)
- 框架: Django
- 数据库: MySQL

### 工程目录
- bookstoreDjango 工程文件夹
- bookstoreDjango/api 应用文件夹，应用名为api
  1. models.py 构建模型，对应数据库中的每一个表
  2. utils.py 工具函数，用于获取格式化日期等等
  3. views.py 映射视图函数，对应url映射到这些函数上，对请求的数据和发送的数据进行进一步的数据操作或者渲染  
- bookstoreDjango/bookstoreDjango 工程配置文件夹
  1. settings.py 配置Django工程的数据库连接、跨域设置、白名单等等
- bookstoreDjango/uwsgi uWSGI配置文件夹，内含uwsgi启动初始化文件
