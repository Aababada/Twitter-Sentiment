import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('D:/twitter.csv')
print(df.columns)
df['Sentiment'] = df['Sentiment'].astype('category')
sns.countplot(x='Sentiment', data=df)
plt.title('Sentiment Distribution in Twitter Data')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()
