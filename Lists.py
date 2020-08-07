#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x=list()
x.append(55) #boş liste yaratıp append fonksiyonuyla o listeye 3 atamaktansa direkt x=[3] de yazılabilirdi. 
             #append fonksiyonu tek bir değer eklemek içindir.append fonksiyonu ile listeye birden fazla değer eklenmez.
y=[3,4,5,'afra','artar',44]
y.append(x)
y.extend(("data","science",9,"ocak",1994))
y.insert(1,"test")

print("y listesi : ",y)
print("x listesi : ",x)
print(y[2:-2]) # y listesinde baştan 2. değerden başlayarak al ve sondan 2.ye kadar.sondan 2. dahil değil.
print("y listesinin uzunluğu : ",len(y))


# append: bir listeye tek bir değer ekler
# extend: bir listeye birden fazla değer ekler
# insert: bir listedeki belli bir indeks yerine değer eklemek için kullanılır.


# # Listeden Değer Silme Yöntemleri:
# 
# 1. remove(): bir listede belirtilen ilk değeri siler; eğer aynı değerler diğer indexlerde varsa onlar kalır. yani sadece ilk karşılaştığı değeri siler.
# 2. pop(): belirtilen spesifik indeksteki değeri siler; yani 3. indeksteki değeri sil dersek bu kullanılır.
# 3. del(): belli bir aralıktaki değerleri siler; yani 2. indeks ile 5. indeks arasındaki değerleri sil dediğimizde kullanılır.
# 4. clear(): bir listedeki tüm değerleri siler, bu fonksiyondan sonra liste tamamen boşalır

# In[ ]:


y=[1,2,3,4,5,"afranur","artar","menekşe","papatya","kiraz",3,4,1,"artar"]
y.remove(1) # 0. indeksten başlayarak ilk gördüğü 1 değerini kaldır ve bırak, diğerlerini silme demektir.
y.pop(4)    # sadece 4. indeksteki değeri siler. pop() dan önce remove ile 1 değerini kaldırdığımız için son oluşan listenin
            # üzerinden 4. indeksi kaldırır.
del y[3:5]  # son oluşan listeden 3. indeksten başlayarak 5. indekse kadarki tüm değerleri siler.
y.clear()   # listedeki tüm değerleri siler boş listeye döndürür.
print(y)


# # Soru 1:
# 
# Write a code to compute the sum of the two lowest numbers and the two highest numbers in the following list.
# 
#  my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]

# In[ ]:


my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]

my_list.sort()
print("Ascending order                              :",my_list)
x=my_list[0:2]
y=my_list[9:]
z=x+y
print("Two lowest and two highest numbers           :",z)

sum=0
for i in range(0,len(z)):
    sum=sum+z[i]
print("Sum of the two lowest and two highest numbers:",sum)


# 

# # Soru 2:
# The following two lists contain student names and scores. Write a code that gets the name from the user and prints the score of that student.
# 
#  names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven", 
#           "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra", "Eric"]
# 
#  scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]

# In[ ]:


name=input("What is your name: ")

names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven", "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra", "Eric"]
scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]

for i in range(0,len(names)):
    if name==names[i]:
        print(scores[i])


# In[ ]:





# # Soru 3:
# By using the two lists above, what is the maximum score and how many students got that score?

# In[ ]:


names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven", "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra", "Eric"]
scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]

scores.sort(reverse=True)
print(scores)
print("Count of the student:",scores.count(scores[0]))
print("maximum score is: ",scores[0])
#Her öğrenciye karşılık bir not bulunmaktadır. 
#Not sayısının tekrarlanması o notu alan birden fazla öğrenci olduğu anlamına gelir,
#O yüzden sadece score listesindeki notların sayısını kontrol ettim.


# 

# # Soru 4:
# We can confuse about how many days a month is. Create a list to handle it. You will have month names and day counts in your list together as a nested list.

# In[ ]:


months=['January','February','March','April','May','June','July','August','September','October','November','December']
days=[31,29,31,30,31,30,31,30,31,30,31,30]

for i in range(0,len(months)):
    for j in range(0,len(days)):
        if i==j:
            months_days=months[i],days[j]
            print(months_days)
            


# 

# # Soru:5
# 
# Now create lists of months for each season. Get month names and day counts from the list that you create before with slicing. Name the lists with seasons.

# In[22]:


winter=['December','January','February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
fall = ['September', 'October', 'November']
seasons=(winter,spring,summer,fall)
days=[31,31,29,31,30,31,30,31,30,31,30,31]
#Listeyi bölmeden önceki ayrı ayrı gün ayların isim listeleri:
print(seasons,"\n")
print(days,"\n")

# Listeyi böldükten sonraki kod:
for k in range(0,len(seasons)):
    for i in range(0,len(seasons[k-1])):
        for j in range(0,len(days)):
            if i==j:
                winter_days=seasons[k][i],days[j]
                print(winter_days)
               

# bu kodda günler hep ilk 3 indeksin sayılarını döndürmektedir; yani 31,31,29.diğer indeksleri nasıl
# getirebilirim ???


# In[ ]:





# # Soru 6:
# Finally, from the list in the previous question, calculate how many days the summer season lasts.

# In[27]:


summer = ['June', 'July', 'August']

len(summer)

# summer listesindeki gün sayısını sorduğu için direkt len fonksiyonunu kullandım.


# In[ ]:




