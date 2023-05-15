import pandas as pd

data = {
    'Reactor_ID': [1, 2, 3, 4, 5],
    'Location': ['USA', 'France', 'China', 'Japan', 'Russia'],
    'Capacity (MW)': [1000, 1500, 1200, 2000, 1800],
    'Status': ['Operational', 'Operational', 'Under Construction', 'Operational', 'Decomissioned']
}

df = pd.DataFrame(data)

print(df)
print(df.describe())
print(df.info())

import matplotlib.pyplot as plt

plt.bar(df['Reactor_ID'], df['Capacity (MW)'])
plt.xlabel('Reactor_ID')
plt.ylabel('Capacity (MW)')
plt.title('Nuclear Reactor Capacities')
plt.show()