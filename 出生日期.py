id=input("请输入十八位身份证号码")
sex={o:"girl",1:"boy",2:"girl",3:"boy",4:"girl",5:"boy",6:"girl",7:"boy",8:"girl",9:"boy"}
year=id[6:10]
month=id[10:12]
day=id[12:14]
print("出生日期"+year+"年"+month+"月"+day+"日")