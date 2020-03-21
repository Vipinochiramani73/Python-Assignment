file=open('timestat.txt')
import re,statistics
real_m=[]
real_s=[]
real=[]
for line in file :
	if line.startswith("real"):
	 a=re.findall('(\S+)m\S+s',line)
	 b=re.findall('\S+m(\S+)s',line)
	 real_m.append(int(a[0]))
	 real_s.append(float(b[0]))
	 s=str(float(a[0]))+"m"+b[0]+"s"
	 real.append(s)

real_avg_m=sum(real_m)/len(real_m)
real_avg_s=sum(real_s)/len(real_s)
real_avg=str(real_avg_m)+"m"+str(real_avg_s)+"s"
real_std_m=statistics.pstdev(real_m)
real_std_s=statistics.pstdev(real_s)
real_std=str(real_std_m)+"m"+str(real_std_s)+"s"
real_lower_range=str(real_avg_m-real_std_m)+"m"+str(real_avg_s-real_std_s)+"s"
real_upper_range=str(real_avg_m+real_std_m)+"m"+str(real_avg_s+real_std_s)+"s"


real_count=0
for i in real:
	if real_lower_range<i<real_upper_range:
		real_count=real_count+1


user_m=[]
user_s=[]
user=[]
for line in file :
	if line.startswith("user"):
	 a=re.findall('(\S+)m\S+s',line)
	 b=re.findall('\S+m(\S+)s',line)
	 user_m.append(int(a[0]))
	 user_s.append(float(b[0]))
	 s=str(float(a[0]))+"m"+b[0]+"s"
	 user.append(s)

user_avg_m=sum(user_m)/len(user_m)
user_avg_s=sum(user_s)/len(user_s)
user_std_m=statistics.pstdev(user_m)
user_std_s=statistics.pstdev(user_s)
user_lower_range=str(user_avg_m-user_std_m)+"m"+str(user_avg_s-user_std_s)+"s"
user_upper_range=str(user_avg_m+user_std_m)+"m"+str(user_avg_s+user_std_s)+"s"

user_count=0
for i in user:
	if user_lower_range<i<user_upper_range:
		user_count=user_count+1

sys_m=[]
sys_s=[]
sys=[]
for line in file :
	if line.startswith("sys"):
	 a=re.findall('(\S+)m\S+s',line)
	 b=re.findall('\S+m(\S+)s',line)
	 sys_m.append(int(a[0]))
	 sys_s.append(float(b[0]))
	 s=str(float(a[0]))+"m"+b[0]+"s"
	 sys.append(s)

sys_avg_m=sum(sys_m)/len(sys_m)
sys_avg_s=sum(sys_s)/len(sys_s)
sys_std_m=statistics.pstdev(sys_m)
sys_std_s=statistics.pstdev(sys_s)
sys_lower_range=str(sys_avg_m-sys_std_m)+"m"+str(sys_avg_s-sys_std_s)+"s"
sys_upper_range=str(sys_avg_m+sys_std_m)+"m"+str(sys_avg_s+sys_std_s)+"s"

sys_count=0
for i in sys:
	if sys_lower_range<i<sys_upper_range:
		sys_count=sys_count+1

print("Number of runs:",len(real_m))
print("real_avg"=real_avg)
print("real_std"=real_std)
