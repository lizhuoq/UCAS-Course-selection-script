# 国科大自动选课  
# 国科大选课 全自动
# UCAS Automatic course selection 

**无须输入验证码，可以自动识别验证码** 基于[ddddocr](https://github.com/sml2h3/ddddocr)和[dddd_trainer](https://github.com/sml2h3/dddd_trainer)  

***目前只在非高峰时期测试过，帮助大家捡漏有人退课的课，目前还不完善，在高峰期间使用可能存在bug，需要调整sleep的时间等，<span style="color:red; font-weight:bold;">禁止恶意抢课</span>，如有bug，欢迎发起issue***


## 使用方法 
`python main.py {yourUSERNAME} {yourPASSWORD} {SUBJECTID} {COURSEID} --driverPath --noCaptcha`  
*输入的时候不需要输入`{}`*   

- yourUSERNAME 例如 zhangsan@mails.ucas.ac.cn
- PASSWORD 输入自己的sep登录密码
- SUBJECTID 学院对应的- ID，目前只可选一个学院，如需增加可以在代码中自行修改
- COURSEID 课程编码，可在学期课表或选择课程中查找
- driverPath 如果没有chrome浏览器需要下载chrome浏览器，默认路径在`C:\Program Files\Google\Chrome\Application`，根据自己路径调整 
- noCaptcha 为可选参数，有时登录界面不需要验证码，此时需要加上--noCaptcha，需要验证码时，不需要加该参数

## 1. 安装所需依赖 
`pip install -r requirements.txt -i https://pypi.douban.com/simple` 
python的版本为3.9.16

## 2.学院和- ID对应 
- ID: id_910, 学院名:  数学学院
- ID: id_911, 学院名:  物理学院
- ID: id_957, 学院名:  天文学院
- ID: id_912, 学院名:  化学学院
- ID: id_928, 学院名:  材料学院
- ID: id_913, 学院名:  生命学院
- ID: id_914, 学院名:  地球学院
- ID: id_921, 学院名:  资环学院
- ID: id_951, 学院名:  计算机学院
- ID: id_952, 学院名:  电子学院
- ID: id_958, 学院名:  工程学院
- ID: id_917, 学院名:  经管学院
- ID: id_945, 学院名:  公管学院
- ID: id_927, 学院名:  人文学院
- ID: id_964, 学院名:  马克思主义学院
- ID: id_915, 学院名:  外语系
- ID: id_954, 学院名:  中丹学院
- ID: id_955, 学院名:  国际学院
- ID: id_959, 学院名:  存济医学院
- ID: id_946, 学院名:  体育部
- ID: id_961, 学院名:  集成电路学院
- ID: id_962, 学院名:  未来技术学院
- ID: id_963, 学院名:  网络空间安全学院
- ID: id_968, 学院名:  心理学系
- ID: id_969, 学院名:  人工智能学院
- ID: id_970, 学院名:  纳米科学与技术学院
- ID: id_971, 学院名:  艺术中心
- ID: id_972, 学院名:  光电学院
- ID: id_967, 学院名:  创新创业学院
- ID: id_973, 学院名:  核学院
- ID: id_974, 学院名:  现代农业科学学院
- ID: id_975, 学院名:  化学工程学院
- ID: id_976, 学院名:  海洋学院
- ID: id_977, 学院名:  航空宇航学院
- ID: id_979, 学院名:  杭州高等研究院
- ID: id_985, 学院名:  南京学院
- ID: id_987, 学院名:  应急管理科学与工程学院  

## 3.data文件和model文件
```
data/ 
|---- labels.txt
|---- images
            |----...num.png
``` 
labels 每行内容为  
num值.png\t1+1=?\n  
\t为制表符，\n为换行符 

利用[dddd_trainer](https://github.com/sml2h3/dddd_trainer)训练  
```
models/  
  |---- ocr_1.0_299_3000_2023-06-07-12-34-41.onnx 
  |---- charsets.json
```


模型在models文件夹中，识别带个位数字带运算符的验证码准确率达到99%以上
