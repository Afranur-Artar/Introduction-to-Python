#!/usr/bin/env python
# coding: utf-8

# Bir sözlük key ve ona karşılık gelen value dan oluşmaktadır ve {} ile tanımlanır.Önce key ardından value gelir, ikisini birden ifade eden değere de items denir. Keys değeri tek tırnak içinde gösterilir ve : konulur.
# 
# Örneğin;
# x={isim:'Afra', 
#     soyisim:'artar',
#     yas:'26'}
# 
# Burada isim, soyisim ve yas değerleri key; Afra, artar ve 26 değerleri value; key ve value nun tamamı da items dır.

# In[ ]:


x={'isim':'Afra', 
   'soyisim':'artar', 
   'yas':26}
print(x.items(),"\n")
print(x.keys(),"\n")
print(x.values(),"\n")


# # Soru 1:
# Create a dictionary with 7 days. Ask the user to choose 2 different days by listing the (e.g. "12" for Monday and Tuesday). Delete the user-selected days from the dictionary and print the remaining 5 days on the screen.

# In[41]:


days={'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
lists_days=list(days)
print(list(days))

selected_days=list()
i=1
while i<3:
    choose_day=input("Please choose a day:")
    selected_days.append(choose_day)
    i=i+1
    if i>=3:
        break
print("Selected days are: ", selected_days)
      

for k in range(0,len(selected_days)):
    for j in range(0,len(lists_days)):
        if selected_days[k]==lists_days[j]:
            lists_days.pop(lists_days[j])
        print("Remaining days:",lists_days)
          
        
# pop() fonksiyonunda hata vermektedir !!! 
# Ayrıca dictionary yi listeye çevirmeden nasıl yapabilirim?       


# In[ ]:





# # Soru 2:
# Create a dictionary with the following personnel. Use names as keys.

# In[69]:


personnel={"Names":{"John":(25,'Male'),
           "Lisa":(28,'Female'),
           "Linda":(32,'Female'),
           "Michael":(41,'Male')
                   }
          }

print(personnel)


# In[ ]:





# # Soru 3:
# 
# Add child information to Michael and Linda. Michael has two children (Karen (age : 12, female) and Greg (age : 7, male) and Linda has one child (Susan (age: 6, female))

# In[81]:


personnel["Names"]["Linda"]={"Child":{"Susan":(6,"Female")}}
print(personnel["Names"]["Linda"],"\n")


personnel["Names"]["Michael"]={"Children":{"Karen":(12,"Female"),"Greg":(7,"Male")}}
print(personnel["Names"]["Michael"],"\n")

print(personnel)


# 

# # Soru 4:
# Print the names of Michael's children in a list.

# In[84]:


personnel={"Names":{"John":(25,'Male'),
           "Lisa":(28,'Female'),
           "Linda":(32,'Female'),
           "Michael":(41,'Male')
                   }
          }

# Added Linda's child
personnel["Names"]["Linda"]={"Child":{"Susan":(6,"Female")}}


# Added Michael'S children
personnel["Names"]["Michael"]={"Children":{"Karen":(12,"Female"),"Greg":(7,"Male")}}



print("Michaels's children are: ",personnel["Names"]["Michael"]["Children"])

