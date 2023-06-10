# CommonNeighborAnalysis-Python
CommonNeighborAnalysis core algorithm written in python  
## 使用方法：  
1、准备一个data文件，不需要太大，几百个原子就够了。从data文件里面找一个原子，最好从盒子的中心处取，待会要查找这个原子的邻居等参数，记录一下原子在data文件第几行。  
2、去choose函数修改几个参数，**第一个是要读取的data文件名**，**第二个是邻居个数**，一般是12或者14，对应到程序里填13或者15（因为我程序写的不是太完美，需要把邻居数+1才能正常运行，实际还是按照12或14个邻居计算的），**第三个参数是cline**，就是要计算的原子在data文件的第几行，需要手动减去1，因为python读取的时候第一行的下标是0。**还有一个参数是type**，因为choose函数定义了好几种类型，type需要指定其中一种。  
#### 注：这个程序只是用来测试cna所需要的（i,j,k）三个参数，最终是要借助ovito识别，后面还需要去修改ovito的源码，cna的adaptive部分，加几个判断条件。  
![image](https://github.com/okihane/CommonNeighborAnalysis-Python/assets/30775452/9888e3f2-ccc1-4040-924c-396363ecbd8d)
上图是一个fcc原子的识别结果，输出的内容有三行，分别代表i,j,k三个数，每一行有12个数，就是邻居的个数，每一个邻居原子的(i,j,k)三个参数都是(4,2,1)  
![image](https://github.com/okihane/CommonNeighborAnalysis-Python/assets/30775452/f66bfa70-6693-45b1-8335-31742be68c0f)
这个是我用到的A15结构中Nb原子的输出结果，用到了14个邻居原子，可以看到他有2个邻居原子的(i,j,k)是(6,6,6)，有12个邻居原子的(i,j,k)是(5,5,5).  
## ovito源码的修改：
目录：src\ovito\particles\modifier\analysis\cna  
.h文件(头文件)里修改一处
![image](https://github.com/okihane/CommonNeighborAnalysis-Python/assets/30775452/401e7ab1-8f3b-41f0-a023-d0cd065b6d78)
.cpp文件里再修改几处，这里需要根据自己的情况进行修改。
![image](https://github.com/okihane/CommonNeighborAnalysis-Python/assets/30775452/9cf0bb3b-b174-4407-bd01-394e4962b901)
![image](https://github.com/okihane/CommonNeighborAnalysis-Python/assets/30775452/21aaa38f-ea4e-41c0-a410-ccd66ccafb62)
![image](https://github.com/okihane/CommonNeighborAnalysis-Python/assets/30775452/f7948ab8-4788-4b2e-8438-9df0cb1d2244)
### 结果展示：  
原版
![image](https://github.com/okihane/CommonNeighborAnalysis-Python/assets/30775452/d8811e4b-fac0-4d21-a870-ccbf2a26a887)
修改版
![image](https://github.com/okihane/CommonNeighborAnalysis-Python/assets/30775452/35a56d47-f9ac-4a9e-9b0d-7fb7d47fe23a)
