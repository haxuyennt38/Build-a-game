#The list has many elements
teams = ["Barcelona","Real Madrid","Manchester United","Liverpool","Chelsea"]#dung dau ngoac vuong de python hieu day la danh sach du lieu
#print(teams)
#print(teams[0]) in phan tu tu vi tri dau tu trai qua phai
#print(teams[-2]) #in tu phai qua trai
#print(teams[1:]) #in tu vi tri so mot va tat ca cac phan tu sau no
#print(teams[1:4]) #lay cac danh sach cac phan tu <=4 va >=1
#teams[1] = "Arsenal" #gan mot gia tri khac vao list truoc do minh da tao
#print(teams)

##########################################################################
student_names = ["Nguyen","Hung","Tuyen","Trung","Sang","Truong"]
math_scores = [10, 9, 8, 7, 6, 5]
#extend(): la ham them thong tin vao phia sau danh sach minh muon hay con goi la ham noi hai danh sach lai voi nhau
#student_names.extend(math_scores)
#Su dung ham append() de muon them cac phan tu rieng le
#student_names.append("Thang")
#insert(index,object) la ham muon them phan tu vao vi tri mong muon
#student_names.insert(1,"Dung")
#remove("ten phan tu muon xoa") la ham xoa gia tri
#student_names.remove("Sang")
#clear() la ham xoa toan bo cac phan tu
#Ham pop giup loai bo mot phan tu
#student_names.pop()
#Muon kiem tra mot phan tu cu the co trong danh sach hay khong
#count("ten bien") la ham dem gia tri cua bien co trong danh sach
#sort() sap xem tang dan theo bang chu cai
#print(student_names.index("Tuyen"))
#student_names.sort()
#math_scores.sort()
#print(math_scores)
#Ham reverse() la ham muon dao nguoc danh sach ban dau
#math_scores.reverse()
#Ham copy la ham sao chep mot danh sach khac tu danh sach cu
student_names_2 = student_names.copy()
print(student_names_2)

