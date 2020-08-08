#!/usr/bin/env python
# coding: utf-8

# Tuples ile lists arasındaki en önemli fark: tuple lar değişmez sabitlerdir dolayısıyla append, remove, pop gibi fonksiyonlar kullanılmaz; yani tuple ın içindeki değerlere ekleme yapılamaz silinemez ya da güncellenemezdir.
# 
# List() fonksiyonunda köşeli parantez [] kullanılırken; tuple da normal parantez () kullanılır ya da parantez kullanılmadan direkt virgüllerle de ayrılabilir.
# 
# Tanımlanan değişken sayısı tuple ın uzunluğuna eşit olmalıdır.

# # Soru 1:
# Create a tuple named "week" containing weekdays.

# In[1]:


week={'monday','tuesday','wednesday','thursday','friday','saturday','sunday'}
print(week)


# # Soru 2:
# Create a set named "fruits" containing followings: apple, mango, orange

# In[2]:


fruits={'apple','mango','orange'}
print(fruits)


# # Soru 3:
# Create a new set named "new_fruits" containing followings: cherry, peach, apple, mango

# In[3]:


new_fruits={'cherry', 'peach', 'apple', 'mango'}
print(new_fruits)


# # Soru 4: 
# Find the fruits which are in new_fruits but not in fruits.

# In[6]:


fruits={'apple','mango','orange'}
new_fruits={'cherry', 'peach', 'apple', 'mango'}

print(new_fruits.difference(fruits))


# # Soru 5:
# Find the fruits which are in both new_fruits and fruits.

# In[7]:


fruits={'apple','mango','orange'}
new_fruits={'cherry', 'peach', 'apple', 'mango'}

print(new_fruits.intersection(fruits))

