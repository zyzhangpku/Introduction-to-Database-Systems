# 学生信息管理项目说明
元培学院 张朕源 2200017763
## 解释
使用csv文件`.\data\students.csv`存储所有学生数据，包括每个学生的姓名、学号、生日、院系、课程成绩。实际上采用线性表存储数据。采用命令行交互，通过python的csv模块进行csv文件的读取、删除、修改。
支持4项操作：添加、修改、删除、查询操作。
当输入的数据错误时，会有提示；支持任意时刻退出。
将数据写入csv文件中以实现持久化。
使用python的csv模块来实现以上操作。
在csv文件中，第一行为该列数据的类型，名字、学号或课程名等。
第二列开始为每个学生的信息。若该同学未选课，成绩记为0分。
学生数据和课程数据均为随机生成。
## Demo
在`StudentManagement`目录下打开命令行。
```
PS C:\StudentManagement> py initialize.py # 运行initialize.py
Initializing...
Done.
```
初始化完毕，生成了学生数据。
接下来先添加一位同学的数据：
```
PS C:\path\to\your\script> py main.py # 运行main.py
Loading...
Enter a, d, u, i for adding, deleting, updating, inquire student's information
Enter Q to quit
a # 添加一位同学
--Now you are adding a student--
!!If you want to quit, please enter the letter q!!
Please enter name
xiaoming
Please enter ID number
666
Please enter birthday, in the form like:2024-2-25
2000-1-1
Please enter college
dk
Please enter department
No.0
Now you are adding the courses and grades. Enter the letter s to save this student's info.
Please enter a course selected
Introduction of Biology (Honor Track)
Please enter the grade
100
Please enter a course selected
s # 添加完毕，下面显示了刚添加的同学的信息
You add a student. Here is the information of this student:
Name: xiaoming
ID Number: 666
Birthday: 2000-1-1
College: dk
Department: No.0
Courses Grades:
        Introduction of Biology (Honor Track): 100
```
然后来查询该同学的信息：
```
Enter a, d, u, i for adding, deleting, updating, inquire student's information
Enter Q to quit
i # 查询刚添加的同学的信息
--Now you are asking for a student's info--
Please enter the name or ID
xiaoming
xiaoming's information:
ID: 666
Birthday: 2000-1-1
College: dk
Department: No.0
Introduction of Biology (Honor Track): 100

```
接着修改其信息：
```
Enter a, d, u, i for adding, deleting, updating, inquire student's information
Enter Q to quit
u # 修改同学信息
--Now you are updating a student's info--
Please enter name
xiaoming
Please enter ID number
200
Please enter birthday, in the form like:2024-2-25
p # 代表不修改此信息
Please enter college
p
Please enter department
p
Now you are adding the courses and grades. Enter the letter s to save this student's info.
Please enter a course selected
p
Update successfully # 修改后显示信息
xiaoming's information:
ID: 200
Birthday: 2000-1-1
College: dk
Department: No.0
Introduction of Biology (Honor Track): 100
```
最后删除信息：
```
Enter a, d, u, i for adding, deleting, updating, inquire student's information
Enter Q to quit
d # 删除学生信息
--Now you are deleting a student's information
!!If you want to quit, please enter the letter q!!
Please enter student's name
xiaoming
Delete Successfully
Enter a, d, u, i for adding, deleting, updating, inquire student's information
Enter Q to quit
i # 再查询学生信息，无结果
--Now you are asking for a student's info--
Please enter the name or ID
xiaoming
xiaoming's information:
No record found for xiaoming.
```

