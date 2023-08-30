import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one-hot кодировку
one_hot_encoded = pd.get_dummies(data['whoAmI'], prefix='whoAmI')

# Объединение исходного DataFrame с one-hot кодированным
data = pd.concat([data, one_hot_encoded], axis=1)

# Удаление исходного столбца 'whoAmI'
data = data.drop('whoAmI', axis=1)

data.head()
