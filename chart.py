import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style = "ticks" , color_codes = True)
titanic = sns.load_dataset("titanic")
# print(titanic.head())
graph = sns.FacetGrid(titanic , row = "sex" , hue = "alone")
graph = (graph.map(plt.scatter , "age" , "fare").add_legend())
plt.show()
#tHIS cOMMIT IN GIT EDITOR
