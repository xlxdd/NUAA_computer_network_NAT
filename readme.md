# NUAA计算机网络课程实验——NAT技术模拟实验
***
## 使用的工具
使用python库:socket,pyqt5,threading,json,sys  
  
其他工具:QTdesigner,PyUic  
## 如何使用
* 客户机进程client  
  * 运行client文件夹中的clientrelease，选择客户机标识符，输入文本内容，点击发送按钮  
  * clientui.py定义图形界面类
  * client类为客户机类，虽然后来舍弃了这种写法
  * clientrelease.py整合图形界面，定义按钮事务逻辑
* 交换机进程switcher
  * 运行switcher文件夹中的switcherrelease.py，点击开始按钮
  * switcherui.py定义图形界面类
  * switcherrelease.py整合图形界面，定义按钮事务逻辑
* 路由器进程router
  * 类似交换机进程
* 服务器进程server
  * 类似交换机进程

## 备注
* 此项目并不完善，有一些功能实际并没有做，比如报文格式的定义就十分简陋，因此也没有做IP地址的替换。  
* 但是因为这个实验中路由器到服务器是直连的，因此不替换IP也并不影响最后呈现的结果。  
* 如果以后有人要用到这个代码，希望他能完善一下，哈哈哈。