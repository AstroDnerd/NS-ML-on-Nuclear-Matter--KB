import pandas as pd
df1 = pd.read_table('Case1.dat',names=['e(0)','rho(0)','K(0)','Q(0)','J(0)','L(0)',
                                       'Ksym(0)','NS mass','Rmax','R14','Lambda10',
                                       'Lambda14','Lambda18','Vs','Qsym'])
df1.to_excel('NS_EOS_Case1.xlsx')

df2 = pd.read_table('Case2.dat',names=['e(0)','rho(0)','K(0)','Q(0)','J(0)','L(0)',
                                       'Ksym(0)','NS mass','Rmax','R14','Lambda10',
                                       'Lambda14','Lambda18','Vs','Qsym'])
df2.to_excel('NS_EOS_Case2.xlsx')

df3 = pd.read_table('Case3.dat',names=['e(0)','rho(0)','K(0)','Q(0)','J(0)','L(0)',
                                       'Ksym(0)','NS mass','Rmax','R14','Lambda10',
                                       'Lambda14','Lambda18','Vs','Qsym'])
df3.to_excel('NS_EOS_Case3.xlsx')

df_m = pd.concat([df1,df2],ignore_index=True)
DF = pd.concat([df_m,df3],ignore_index=True)
DF.to_excel('NS_EOS.xlsx')
