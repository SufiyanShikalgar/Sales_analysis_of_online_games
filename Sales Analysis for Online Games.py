#!/usr/bin/env python
# coding: utf-8

# # Phase 1

# # Task 1:

# In[1]:


# 1. import relevant packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# 2.import datasets


# In[3]:


companies=pd.read_excel('games.xlsx',sheet_name='companies')
sales=pd.read_excel('games.xlsx',sheet_name='sales')


# In[4]:


companies.head()


# In[5]:


sales.head()


# In[6]:


# 3. Check data set


# In[7]:


companies.shape


# In[8]:


sales.shape


# In[9]:


companies.info()


# In[10]:


sales.info()


# In[11]:


companies.describe(include='all')


# In[12]:


sales.describe(include='all')


# In[13]:


# 4. Concatinate data sets


# In[14]:


vg=pd.concat([companies, sales],axis=1)
vg


# In[15]:


vg.isnull().sum()


# # Task 2

# In[16]:


# 1. Drop missing values
vg.dropna(inplace=True)
vg


# In[17]:


# 2. Drop duplicate records
vg.drop_duplicates()
vg


# In[18]:


# 3. Convert year to integer
vg.Year=pd.to_numeric(vg['Year'], downcast="integer")
vg


# In[19]:


vg.info()


# In[20]:


# 4. Create a column “Total_Sales” that is sum of “NA_Sales” , “EU_Sales” and “JP_Sales”

vg['Total_Sales']=vg[['NA_Sales','EU_Sales','JP_Sales']].sum(axis=1)
vg


# # Phase 2

# In[21]:


# 1. Univariate analysis


# In[22]:


# Univariate analysis - Name
vg.Name.describe()


# In[23]:


vg.Name.value_counts()


# In[164]:


# top 25 games sold

Name_count = pd.DataFrame(vg['Name'].value_counts()).reset_index().head(25)
Name_count.columns = ['Name','Value_counts']

g = sns.catplot(y='Name',x='Value_counts', data=Name_count, kind='bar', palette='Blues_r')
g.fig.suptitle('Top Games', y = 1.03)
g.set(ylabel='Games name',xlabel='')
plt.show()


# In[25]:


# Top 25 games with less sale

N_count = pd.DataFrame(vg['Name'].value_counts()).reset_index().tail(25)
N_count.columns = ['Name','Value_counts']

g = sns.catplot(y='Name',x='Value_counts', data=N_count, kind='bar', palette='Blues_r')
g.fig.suptitle('Top Games', y = 1.03)
g.set(ylabel='Games name',xlabel='')
plt.show()


# In[26]:


vg.Platform.value_counts()


# In[27]:


vg.Platform.describe()


# In[28]:


Platform_count = pd.DataFrame(vg['Platform'].value_counts()).reset_index()
Platform_count.columns = ['Platform','Value_counts']

g = sns.catplot(y='Platform',x='Value_counts', data=Platform_count, kind='bar', palette='Blues_r')
g.fig.suptitle('Top Platform', y = 1.03)
g.set(ylabel='Platform name',xlabel='')
plt.show()


# In[178]:


# Univariate analysis - Year

a=vg.Year.value_counts().reset_index()
a.rename(columns={'index':'Year','Year':'Count'}, inplace=True)
a


# In[179]:


b=a.head(10)


# In[182]:



g = sns.catplot(y='Count',x='Year', data=b, kind='bar', palette='Blues_r')
g.fig.suptitle('Top Sales Year', y = 1.03)
g.set(ylabel='Games sold',xlabel='')
plt.show()


# In[183]:


c=a.tail(10)
g = sns.catplot(y='Count',x='Year', data=c, kind='bar', palette='Blues_r')
g.fig.suptitle('Low Sales Year', y = 1.03)
g.set(ylabel='Games sold',xlabel='')
plt.show()


# In[30]:


vg.Year.describe()


# In[31]:


# Univariate analysis - Genre
vg.Genre.describe()


# In[32]:


vg.Genre.value_counts()


# In[33]:


Genre_count = pd.DataFrame(vg['Genre'].value_counts()).reset_index()
Genre_count.columns = ['Genre','Value_counts']

g = sns.catplot(y='Genre',x='Value_counts', data=Genre_count, kind='bar', palette='Blues_r')
g.fig.suptitle('Top Genre', y = 1.03)
g.set(ylabel='Genre name',xlabel='')
plt.show()


# In[34]:


# Univariate analysis - Publisher
vg.Publisher.describe()


# In[35]:


vg.Publisher.value_counts()


# In[36]:


# top 20 game publishers

Publisher_count = pd.DataFrame(vg['Publisher'].value_counts()).reset_index().head(20)
Publisher_count.columns = ['Publisher','Value_counts']

g = sns.catplot(y='Publisher',x='Value_counts', data=Publisher_count, kind='bar', palette='pastel')
g.fig.suptitle('Top Publisher', y = 1.03)
g.set(ylabel='Publisher name',xlabel='')
plt.show()


# In[37]:


# Univariate analysis - NA_Sales 
vg.NA_Sales.describe()


# In[38]:


# Univariate analysis - EU_Sales 
vg.EU_Sales.describe()


# In[184]:


# Univariate analysis - JP_Sales 
vg.JP_Sales.describe()


# In[185]:


# Univariate analysis - Global_Sales 
vg.Global_Sales.describe()


# In[39]:


numerical=vg[['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales','Total_Sales']]


# In[40]:


numerical.describe()


# In[41]:


# Bivariate analysis


# In[42]:


#1.  game vs NA_sales


# In[43]:


# top 10 games with most sales in NA reion
a=vg.groupby(['Name'])['NA_Sales'].sum().reset_index()
b=a.sort_values(by=['NA_Sales'],ascending=False).head(10)
b


# In[44]:


c=sns.barplot(x='NA_Sales', y='Name', data=b)

d=c.bar_label(c.containers[0])


# In[45]:


# 2.  game vs EU_sales


# In[46]:


# top 10 games with most sales in EU reion
e=vg.groupby(['Name'])['EU_Sales'].sum().reset_index()
f=e.sort_values(by=['EU_Sales'],ascending=False).head(10)
f


# In[47]:


g=sns.barplot(x='EU_Sales', y='Name', data=f)
hd=g.bar_label(g.containers[0])


# In[48]:


# 3.  game vs JP_sales


# In[49]:


# top 10 games with most sales in JP region
i=vg.groupby(['Name'])['JP_Sales'].sum().reset_index()
j=i.sort_values(by=['JP_Sales'],ascending=False).head(10)
j


# In[50]:


k=sns.barplot(x='JP_Sales', y='Name', data=j)
l=k.bar_label(k.containers[0])


# In[51]:


# 4.  game vs Other_sales


# In[52]:


# top 10 games with most sales in Other region
aa=vg.groupby(['Name'])['Other_Sales'].sum().reset_index()
ab=aa.sort_values(by=['Other_Sales'],ascending=False).head(10)
ab


# In[53]:


ac=sns.barplot(x='Other_Sales', y='Name', data=ab)
ad=ac.bar_label(ac.containers[0])


# In[54]:


# 5.  game vs Global_sales


# In[55]:


# top 10 games with most sales globally
ba=vg.groupby(['Name'])['Global_Sales'].sum().reset_index()
bb=ba.sort_values(by=['Global_Sales'],ascending=False).head(10)
bb


# In[56]:


bc=sns.barplot(x='Global_Sales', y='Name', data=bb)
bd=bc.bar_label(bc.containers[0])


# In[57]:


# 6. Platform vs NA_Sales


# In[58]:


# top 10 Platform with most sales in N.A. region
ca=vg.groupby(['Platform'])['NA_Sales'].sum().reset_index()
cb=ca.sort_values(by=['NA_Sales'],ascending=False).head(10)
cb


# In[59]:


cc=sns.barplot(x='NA_Sales', y='Platform', data=cb)
cd=cc.bar_label(cc.containers[0])


# In[60]:


# 7. Platform vs EU_Sales


# In[61]:


# top 10 Platform with most sales in EU region
da=vg.groupby(['Platform'])['EU_Sales'].sum().reset_index()
db=da.sort_values(by=['EU_Sales'],ascending=False).head(10)
db


# In[62]:


dc=sns.barplot(x='EU_Sales', y='Platform', data=db)
dd=dc.bar_label(dc.containers[0])


# In[63]:


# 8. Platform vs JP_Sales


# In[64]:


# top 10 Platform with most sales in JP region
ea=vg.groupby(['Platform'])['JP_Sales'].sum().reset_index()
eb=ea.sort_values(by=['JP_Sales'],ascending=False).head(10)
eb


# In[65]:


ec=sns.barplot(x='JP_Sales', y='Platform', data=eb)
ed=ec.bar_label(ec.containers[0])


# In[66]:


# 9. Platform vs Other_Sales


# In[67]:


# top 10 Platform with most sales in Other region
fa=vg.groupby(['Platform'])['Other_Sales'].sum().reset_index()
fb=fa.sort_values(by=['Other_Sales'],ascending=False).head(10)
fb


# In[68]:


fc=sns.barplot(x='Other_Sales', y='Platform', data=fb)
fd=fc.bar_label(fc.containers[0])


# In[69]:


# 10. Platform vs Global_Sales


# In[70]:


# top 10 Platform with most sales in Global region
ga=vg.groupby(['Platform'])['Global_Sales'].sum().reset_index()
gb=ga.sort_values(by=['Global_Sales'],ascending=False).head(10)
gb


# In[71]:


gc=sns.barplot(x='Global_Sales', y='Platform', data=gb)
gd=gc.bar_label(gc.containers[0])


# In[72]:


# 11. Year vs NA_Sales


# In[73]:


# last 10 years Yearwise sale in NA region
ha=vg.groupby(['Year'])['NA_Sales'].sum().reset_index()
hb=ha.sort_values(by=['Year'],ascending=False).head(10)
hb


# In[74]:


hc=sns.barplot(x='Year', y='NA_Sales', data=hb)
hd=hc.bar_label(gc.containers[0])


# In[75]:


# 12. Year vs EU_Sales


# In[76]:


# last 10 years' Yearwise sale in EU region
ia=vg.groupby(['Year'])['EU_Sales'].sum().reset_index()
ib=ia.sort_values(by=['Year'],ascending=False).head(10)
ib


# In[77]:


ic=sns.barplot(x='Year', y='EU_Sales', data=ib)
id=ic.bar_label(gc.containers[0])


# In[78]:


# 13. Year vs JP_Sales


# In[79]:


# last 10 years' Yearwise sale in JP region
ja=vg.groupby(['Year'])['JP_Sales'].sum().reset_index()
jb=ja.sort_values(by=['Year'],ascending=False).head(10)
jb


# In[80]:


jc=sns.barplot(x='Year', y='JP_Sales', data=jb)
jd=jc.bar_label(jc.containers[0])


# In[81]:


# 14. Year vs Other_Sales


# In[82]:


# last 10 years' Yearwise sale in Other region
ka=vg.groupby(['Year'])['Other_Sales'].sum().reset_index()
kb=ka.sort_values(by=['Year'],ascending=False).head(10)
kb


# In[83]:


kc=sns.barplot(x='Year', y='Other_Sales', data=kb)
kd=kc.bar_label(kc.containers[0])


# In[84]:


# 15. Year vs Global_Sales


# In[85]:


# last 10 years' Yearwise sales globally
la=vg.groupby(['Year'])['Global_Sales'].sum().reset_index()
lb=la.sort_values(by=['Year'],ascending=False).head(10)
lb


# In[86]:


lc=sns.barplot(x='Year', y='Global_Sales', data=lb)
ld=lc.bar_label(lc.containers[0])


# After 2016 even sale of 1 million is not done

# In[87]:


# Genre vs sales


# In[88]:


# 16. Genre vs NA_Sales


# In[89]:


# Top 10 salling genres in NA region
ma=vg.groupby(['Genre'])['NA_Sales'].sum().reset_index().sort_values(by=['NA_Sales'],ascending=False).head(10)
ma


# In[90]:


mb=sns.barplot(x='NA_Sales', y='Genre', data=ma)
mc=mb.bar_label(mb.containers[0])


# In[91]:


# 17. Genre vs EU_Sales


# In[92]:


# top 10 salling genres in EU region
na=vg.groupby(['Genre'])['EU_Sales'].sum().reset_index().sort_values(by=['EU_Sales'],ascending=False).head(10)
na


# In[93]:


nb=sns.barplot(x='EU_Sales', y='Genre', data=na)
nc=nb.bar_label(nb.containers[0])


# In[94]:


# 18. Genre vs JP_Sales


# In[95]:


# top 10 salling genres in JP region
oa=vg.groupby(['Genre'])['JP_Sales'].sum().reset_index().sort_values(by=['JP_Sales'],ascending=False).head(10)
oa


# In[96]:


ob=sns.barplot(x='JP_Sales', y='Genre', data=oa)
oc=ob.bar_label(ob.containers[0])


# In[97]:


# 19. Genre vs Other_Sales


# In[98]:


# top 10 salling genres in Other region
pa=vg.groupby(['Genre'])['Other_Sales'].sum().reset_index().sort_values(by=['Other_Sales'],ascending=False).head(10)
pa


# In[99]:


pb=sns.barplot(x='Other_Sales', y='Genre', data=pa)
pc=pb.bar_label(pb.containers[0])


# In[100]:


# 20. Genre vs Global_Sales


# In[101]:


# top 10 salling genres in Other region
qa=vg.groupby(['Genre'])['Global_Sales'].sum().reset_index().sort_values(by=['Global_Sales'],ascending=False).head(10)
qa


# In[102]:


qb=sns.barplot(x='Global_Sales', y='Genre', data=qa)
qc=qb.bar_label(qb.containers[0])


# In[103]:


vg.head()


# In[104]:


# 21. Publisher vs NA_Sales


# In[105]:


# top 10 salling publishers in NA region
ra=vg.groupby(['Publisher'])['NA_Sales'].sum().reset_index().sort_values(by=['NA_Sales'],ascending=False).head(10)
ra


# In[106]:


rb=sns.barplot(x='NA_Sales', y='Publisher', data=ra)
rc=rb.bar_label(rb.containers[0])


# In[107]:


# 22. Publisher vs EU_Sales


# In[108]:


# top 10 salling publishers in EU region
sa=vg.groupby(['Publisher'])['EU_Sales'].sum().reset_index().sort_values(by=['EU_Sales'],ascending=False).head(10)
sa


# In[109]:


sb=sns.barplot(x='EU_Sales', y='Publisher', data=sa)
sc=sb.bar_label(sb.containers[0])


# In[110]:


# 23. Publisher vs JP_Sales


# In[111]:


# top 10 salling publishers in JP region
ta=vg.groupby(['Publisher'])['JP_Sales'].sum().reset_index().sort_values(by=['JP_Sales'],ascending=False).head(10)
ta


# In[112]:


tb=sns.barplot(x='JP_Sales', y='Publisher', data=ta)
tc=tb.bar_label(tb.containers[0])


# In[113]:


# 24. Publisher vs Other_Sales


# In[114]:


# top 10 salling publishers in Other region
ua=vg.groupby(['Publisher'])['Other_Sales'].sum().reset_index().sort_values(by=['Other_Sales'],ascending=False).head(10)
ua


# In[115]:


ub=sns.barplot(x='Other_Sales', y='Publisher', data=ua)
uc=ub.bar_label(ub.containers[0])


# In[116]:


# 25. Publisher vs Global_Sales


# In[117]:


va=vg.groupby(['Publisher'])['Global_Sales'].sum().reset_index().sort_values(by=['Global_Sales'],ascending=False).head(10)
va


# In[118]:


vb=sns.barplot(x='Global_Sales', y='Publisher', data=va)
vc=vb.bar_label(vb.containers[0])


# # Multivariate analysis 

# In[119]:


# 1. Sales columns analysis


# In[120]:


# Numerical analysis 
numeric=numerical[['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
numeric


# In[121]:


corr=numeric.corr()[['Global_Sales']]
corr


# In[122]:


ai=vg[['NA_Sales','EU_Sales','JP_Sales','Other_Sales']].sum().reset_index()


# In[123]:


aj=ai.rename(columns={'index':'Region',0:'Sales_sum'})
aj


# In[124]:


plt.pie(aj['Sales_sum'], labels = aj['Region'], autopct='%1.1f%%', startangle=90, explode = [0.1,0,0,0])
#plt.legend(title = "Sum of regionwise sales")
plt.show()


# In[125]:


# 2. Top 10 game wise sales analysis  


# In[126]:


aaa=vg.groupby(['Name'])['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales'].sum().reset_index().sort_values(by=['Global_Sales'],ascending=False).head(10)
aaa


# In[127]:


aab=aaa.plot(x='Name', y=['NA_Sales','EU_Sales','Other_Sales','JP_Sales','Global_Sales'],kind='bar')


# In[128]:


# 3. Genre vs sales


# In[129]:


# top 10 Genre vs sales analysis 
baa=vg.groupby(['Genre'])['NA_Sales','EU_Sales','JP_Sales','Other_Sales', 'JP_Sales','Global_Sales'].sum().reset_index().sort_values(by=['Global_Sales'],ascending=False).head(10)
baa


# In[130]:


bab=baa.plot(x='Genre', y=['NA_Sales','EU_Sales','Other_Sales', 'JP_Sales','Global_Sales'],kind='bar')


# In[131]:


# 4. year wise  sales analysis


# In[132]:


# Last 10 Genre vs sales analysis 
caa=vg.groupby(['Year'])['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales'].sum().reset_index().sort_values(by=['Year'],ascending=False).head(10)
cab=caa.sort_values(by=['Year'],ascending=True)
cab


# In[133]:


cac=cab.plot(x='Year', y=['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales'],kind='bar')


# In[134]:


# 5. Platform vs Sales


# In[135]:


# Last 10 saling platforms vs sales analysis 
daa=vg.groupby(['Platform'])['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales'].sum().reset_index().sort_values(by=['Global_Sales'],ascending=False).head(10)
daa


# In[136]:


dab=daa.plot(x='Platform', y=['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales'],kind='bar')


# In[137]:


# 6. Publisher vs sales analysis


# In[138]:


# Last 10 saling Publishers vs sales analysis 
eaa=vg.groupby(['Publisher'])['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales'].sum().reset_index().sort_values(by=['Global_Sales'],ascending=False).head(10)
eaa


# In[139]:


eab=eaa.plot(x='Publisher', y=['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales'],kind='bar')


# # Value distribution

# In[140]:


plt.boxplot(vg[['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']])
plt.show()


# # Phase 3

# In[141]:


vg.Year.describe()


# In[142]:


# Filtering result

# there are negligible sales after 2016 , so removing data after 2016
vh=vg[vg['Year']<=2016]
vh


# In[143]:


# Genre vs Global sales strip plot


# In[144]:


# top 5 salling genres in GLobally region
qa=vg.groupby(['Genre'])['Global_Sales'].sum().reset_index().sort_values(by=['Global_Sales'],ascending=False).head(5)
qa


# In[145]:


ia=vg.Genre.value_counts().reset_index().head(5)


# In[146]:


ba=ia.rename(columns={'Genre':'Genre_count','index':'Genre'})
ba


# In[147]:


Genre_list=ba.Genre.values.tolist()
genre_in=tuple(Genre_list)
genre_in


# In[148]:


myData=vg[vg['Genre'].isin(Genre_list)]
myData1=myData[['Genre','Global_Sales']].sort_values(by=['Global_Sales'],ascending=True)
myData1


# In[149]:


sns.stripplot(x=myData1["Genre"], y=myData1["Global_Sales"])


# In[150]:


# 3. top 5 frequent publishers vs Global sales


# In[151]:


records=vg.Publisher.value_counts().reset_index().head(5)
records.rename(columns={'index':'Publisher', 'Publisher':'Frequency'}, inplace=True)
records


# In[152]:


Publisher_list=records.Publisher.values.tolist()


# In[153]:


myData=vg[vg['Publisher'].isin(Publisher_list)]
myData1=myData[['Publisher','Global_Sales']].sort_values(by=['Global_Sales'],ascending=True)
myData1


# In[154]:


eab=eaa.plot(x='Publisher', y='Global_Sales' ,kind='bar')


# In[155]:


correlation=vh.corr()[['Global_Sales']]
correlation


# 1. Year has negative correlation with global sales i.e. Global sales is decreasing
# 2. Regions that affect global sales are sequencially as below
# 
#     A. North_American region
#     B. Europian region 
#     C. Other regions
#     D. Japan region

# ## 4. Create Functions that can create group on the basis of categorical columns and show the total collection of the sales

# In[156]:


vg.info() # checking column info


# In[157]:


categorical=vg.select_dtypes(include="O")
a=categorical.columns.tolist()


# In[158]:


def categorical(x):

    l=vg.groupby([x])['Total_Sales'].sum().reset_index().head(10)
    m=sns.barplot(x=x, y='Total_Sales', data=l)
    plt.xticks(rotation=90)
    n=m.bar_label(m.containers[0])
    plt.show()

for i in a:
    categorical(i)


# ## 5.	Show the line chart for the gaming Publisher and display the overall collection of sales in NA, EU and JP with respect to the year in the same chart.

# In[159]:


va=vg.groupby(['Publisher','Year'])['Global_Sales'].sum().reset_index().sort_values('Global_Sales',ascending=False).head(10)
p=va.Publisher.values.tolist()
p


# In[160]:


a=vg.query("Publisher in @p")
a


# In[161]:


sales=a.groupby(['Publisher','Year'])['NA_Sales','EU_Sales','JP_Sales'].sum().reset_index()
sales


# In[162]:


sns.lineplot(x=sales.Year, y=sales.NA_Sales, hue=sales.Publisher, style=sales.Publisher, palette='Paired')
sns.lineplot(x=sales.Year, y=sales.EU_Sales, hue=sales.Publisher, style=sales.Publisher, palette='flare')
sns.lineplot(x=sales.Year, y=sales.JP_Sales, hue=sales.Publisher, style=sales.Publisher, palette='viridis')
plt.show()


# # Insights
# 
# > North American region is major contributor in Global sales
# 
# > North America, Europe, Other have similar trend in Sales
# 
# > Japan has differnece in sales trend
# 
# > Top selling genres are Acion, Sport, Shooter, Role play
# 
# > In Japan Role_play games are on top 
# 
# > As per result sales is decreasing yearly
# 
# > Top selling game Platform are PS2, X360, PS3
# 
# > Top games are published by Nintendo, Electronix Arts, Activision
# 
# 
# 
# 
# > To get most sale we need Games in action category, for PS2, X360
# 

# In[ ]:




