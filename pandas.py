import pandas as pd
import random
import numpy as np

student = 'db/student.csv'
topic = 'db/topic.csv'

df_1 = pd.read_csv(student, header=0)
df_2 = pd.read_csv(topic, header=0)
association = pd.concat([df_1, df_2], axis=1)

print(association)

mylist = [
  'Tayeb', 'Oscar', 'Antoine', 'Anis', 'Victor', 'Souleyman', 'Etienne', 'Nael'
]

print(random.choice(mylist))
