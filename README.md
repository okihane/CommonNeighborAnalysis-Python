# CommonNeighborAnalysis-Python
CommonNeighborAnalysis core algorithm written in python  
使用方法：  
1、准备一个data文件，不需要太大，几百个原子就够了。从data文件里面找一个原子，最好从盒子的中心处取，待会要查找这个原子的邻居等参数，记录一下原子在data文件第几行。  
2、去choose函数修改几个参数，第一个是要读取的“data文件名”，第二个是“邻居个数”，一般是12或者14，对应到程序里填13或者15（因为我程序写的不是太完美，需要把邻居数+1才能正常运行，实际还是按照12或14个邻居计算的），第三个参数是“cline”，就是要计算的原子在data文件的第几行，需要手动减去1，因为python读取的时候第一行的下标是0。  
注：这个程序只是用来测试cna所需要的（i,j,k）三个参数，最终是要借助ovito识别，后面还需要去修改ovito的源码，cna的adaptive部分，加几个判断条件。
