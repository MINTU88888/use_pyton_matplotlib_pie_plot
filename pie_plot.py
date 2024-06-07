import matplotlib.pyplot as plt
x = [10,20,30,40]
y = ["c","c++","java","python"]
ex = [0.4,0,0,0]
c = ["g","b","y","r"]
# explode perameter ye show kr rha hai ki pie ka ak column kitna bhaar nikal na hai
# autopct perameter ye betata hai ki hume ye show krwana hai ki humari kitni percentage value hai eske ander autopct use krte hai(eski value 0-1 ke bich mai hoti hai)
# shadow perameter pie chart ki shadow show krta hai hai 
# radius perameter se hum graph/circle ko increase ya decrease kr skte hai 
# startingangle graph ko rotate krta hai iski value humesa angle mai aati hai
plt.title("language knowledge",fontsize = 30)
plt.pie(x,labels=y,explode=ex,colors = c,autopct="%1.2f%%",shadow=True,radius=1,startangle=240)
plt.legend()
print(plt.show())