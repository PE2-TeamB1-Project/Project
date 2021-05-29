from analysispy import *
import analysispy
from applicationpy import *
import applicationpy
import os

#csv 파일 생성 코드
applicationpy.application.df.to_csv("Analysis_B1.csv",mode="w")

#image 파일 생성 코드
os.mkdir("C:/Users/dream/Desktop/수업자료/3-1학기/공프2/clone/images")
# ------------------------------------------------------------------------------
for i in range(0,len(all_LMZ)):
    plot.plot(all_LMZ[i])
    plt.savefig("C:/Users/dream/Desktop/수업자료/3-1학기/공프2/clone/images/Analysis{}.png".format(i))