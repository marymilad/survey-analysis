import pandas as pd
from statsmodels.formula.api import ols


#import .csv
df = pd.read_csv('dataset.csv', header = 0)

#create smaller dataframes for each of the definitions
cyber_attack = df.loc[df['Definition'] == 'Cyber Attack']
cyber_extortion = df.loc[df['Definition'] == 'Cyber Extortion']
cyberbullying = df.loc[df['Definition'] == 'Cyberbullying']
data_breach = df.loc[df['Definition'] == 'Data Breach']
identity_theft = df.loc[df['Definition'] == 'Identity Theft']
online_fraud = df.loc[df['Definition'] == 'Online Fraud']


#print(df.columns.tolist()), print all column names
fit = ols('cost_adjusted_cyber_attack ~ action_impersonation + action_steal_data + action_disclose_data + action_data_loss + action_blackmail + action_deceit + action_public_cyberbullying + action_private_cyberbullying + action_harassment + action_discrimination + action_other_cyberbullying + action_hack + action_ddos + action_misc', data=cyber_attack).fit()
print(fit.summary())