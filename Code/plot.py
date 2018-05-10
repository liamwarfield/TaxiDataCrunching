import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.svm import SVC

plt.style.use('ggplot')
plt.plot([1,2,3,4],[1,2,3,5],'r.')
plt.title("tip amount vs Fair")
plt.ylabel("Fair cost")
plt.xlabel("tip")
plt.savefig('tip amount vs Fair.png')
