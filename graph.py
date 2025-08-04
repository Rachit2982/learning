import pandas as pd
import matplotlib.pyplot as plt
a=pd.DataFrame({"name":["Rachit","sarthak"],"roll_no":[1,2]})

plt.plot(a["roll_no"],",")
plt.show()
plt.plot(a["roll_no"],"P")
plt.show()
