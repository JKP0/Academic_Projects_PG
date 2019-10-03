#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


d08=pd.read_csv("1902HackDATA/IPL2008CSV.csv")

#***Basic/General/Normal Information
d08.head()
d08.dtypes
d08.info()
d08.describe()


# In[3]:


d08


# In[4]:


d08['Strike Rate1']=None
d08['Economy1']=None


# In[5]:


for i in range(d08.shape[0]):
    try:
        d08['Strike Rate1'][i]=float(d08['Strike Rate'][i])
    except ValueError:
        d08['Strike Rate1'][i]=0.0
    try:
        d08['Economy1'][i]=float(d08['Economy'][i])
    except ValueError:
        d08['Economy1'][i]=0.0
        


# In[6]:


pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',100)
#pd.reset_option('display.max_rows')
#pd.reset_option('display.max_columns')
#d08.isnull().any()
d08


# In[7]:


for x in d08['Strike Rate1']:
    if(x<0):
        print('True')
print('No_one')
for x in d08['Economy1']:
    if(x<0):
        print('True1')
print('No_one1')


# In[8]:


d08.isnull().any()


# In[9]:


print([x for x in d08])
    


# In[10]:


for x in ['Runs', 'Balls', 'Balls Bowled', 'Runs Conceded', 'Wickets', 'Ct_St',
          'Run Outs', 'Matches Played ', 'Age', 'Strike Rate1', 'Economy1']:
    print(x, min(d08[x]), max(d08[x]))


# In[11]:


pdtr=['Year','RunMi','RunMx','BallMi','BallMx',"4'sMi","4'sMx","6'sMi","6'sMx",'Highest Run Scored Mi','Highest Run Scored Mx','Balls  Bowled Mi',
      'Balls  Bowled Mx','Runs Conceded Mi','Runs Conceded Mx','WicketsMi','WicketsMx','Ct_StMi','Ct_StMx','Run Outs Mi', 'Run Outs Mx','Matches Played Mi',
      'Matches Played Mx','Strike Rate1 Mi','Strike Rate1 Mx','Economy1Mi','Economy1Mx']


# In[12]:


len(d08['Player'].unique())


# In[13]:


fo=open('1902HackData/PdtrCSV.csv', 'w+')
fo.write('Sl.No')
for a in pdtr:
    fo.write(',')
    fo.write(a)
fo.write('\n')


# In[14]:


from matplotlib.lines import Line2D
clr=['blue','red']
stl=[Line2D([0],[0], color=c, linewidth=3, linestyle='--') for c in clr]
plt.scatter(d08['Runs'],d08['Strike Rate1'],c='blue')
plt.scatter(d08['Runs'],d08['Balls'],c='red')
lbl=['RunVsStrike Rate', 'RunVsBalls']
plt.legend(stl, lbl)
plt.ylim((0,400))
plt.xlabel('Run',fontsize=16)
plt.ylabel('StrikeRate/Balls', fontsize=16)
plt.title('Scatter Visulization',fontsize=16)


# In[15]:


plt.scatter(d08['Matches Played '],d08['Strike Rate1'],c='blue')
plt.xlabel('Matches Played', fontsize=16)
plt.ylabel('Strike Rate', fontsize=16)
plt.title('Scatter Visulization',fontsize=16)


# In[16]:


lbl=['Runs Conceded','Balls Bowled','Wickets']
plt.scatter(d08['Runs Conceded'],d08['Economy1'],c='green')
plt.scatter(d08['Balls Bowled'],d08['Economy1'],c='yellow')
plt.scatter(d08['Wickets'],d08['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('Economy',fontsize=16)
plt.ylabel('RunsConceded/BallsBowled/Wickets', fontsize=12)
plt.title('Scatter Visulization',fontsize=16)


# In[17]:


plt.scatter(d08['Matches Played '], d08['Economy1'],c='blue')
plt.xlabel('Matches Played')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=16)


# In[18]:


lbl=['Ct_St','Run Outs']
plt.scatter(d08['Matches Played '],d08['Ct_St'],c='red')
plt.scatter(d08['Matches Played '],d08['Run Outs'],c='pink')
plt.legend(lbl)
plt.xlabel('Matches Played')
plt.ylabel('Ct_St/Run Outs')
plt.title('Scatter Visulization',fontsize=14)


# In[19]:


val=['2008','0','410','0','300','0' ,'0' ,'0' ,'0' ,'12' ,'48','15','310',
     '10','450','0','9','2','8','0','0','1','14','80','160','6','13']
fo.write('1')
for va in val:
    fo.write(',')
    fo.write(va)
fo.write('\n')


# In[20]:


d09=pd.read_csv("1902HackDATA/IPL2009CSV.csv")

#***Basic/General/Normal Information
d09.head()
d09.dtypes
d09.info()
d09.describe()


# In[21]:


d09


# In[22]:


d09.shape


# In[23]:


d09.isnull().any()


# In[24]:


d09['Strike Rate1']=None
d09['Economy1']=None


# In[25]:


for i in range(d09.shape[0]):
    try:
        d09['Strike Rate1'][i]=float(d09['Strike Rate'][i])
    except ValueError:
        d09['Strike Rate1'][i]=0.0
    try:
        d09['Economy1'][i]=float(d09['Economy'][i])
    except ValueError:
        d09['Economy1'][i]=0.0


# In[26]:


pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',100)
#pd.reset_option('display.max_rows')
#pd.reset_option('display.max_columns')
#d09.isnull().any()
d09


# In[27]:


d09.isnull().any()


# In[28]:


len(d09['Player'].unique())


# In[29]:


lbl=['Strike Rate1', 'Balls']
plt.scatter(d09['Runs'],d09['Strike Rate1'],c='blue')
plt.scatter(d09['Runs'],d09['Balls'],c='red')
plt.legend(lbl)
plt.xlabel('Run')
plt.ylabel("StrikeRate/Balls")
plt.title('Scatter Visulization',fontsize=14)


# In[30]:


plt.scatter(d09['Matches Played'],d09['Strike Rate1'],c='blue')
plt.xlabel('Matches Played')
plt.ylabel('Strike Rate')
plt.title('Scatter Visulization',fontsize=14)


# In[31]:


lbl=['Runs Conceded','Balls Bowled','Wickets']
plt.scatter(d09['Runs Conceded'],d09['Economy1'],c='green')
plt.scatter(d09['Balls Bowled'],d09['Economy1'],c='yellow')
plt.scatter(d09['Wickets'],d09['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('RunsConceded/BallsBowled/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[32]:


lbl=['Matches Played', 'Wickets']
plt.scatter(d09['Matches Played'], d09['Economy1'],c='blue')
plt.scatter(d09['Wickets'],d09['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[33]:


lbl=['Ct_St','Run Outs']
plt.scatter(d09['Matches Played'],d09['Ct_St'],c='red')
plt.scatter(d09['Matches Played'],d09['Run Outs'],c='pink')
plt.legend(lbl)
plt.xlabel('Matches Played')
plt.ylabel('Ct_St/RunOuts')
plt.title('Scatter Visulization',fontsize=14)


# In[34]:


val=['2009','0','390','0','300','0' ,'0' ,'0' ,'0' ,'12' ,'48','5','300','4','400',
     '0','15','2.5','10','0','0','1','16','90','150','5','10']
fo.write('2')
for va in val:
    fo.write(',')
    fo.write(va)
fo.write('\n')


# In[35]:


d10=pd.read_csv("1902HackDATA/IPL2010CSV.csv")

#***Basic/General/Normal Information
d10.head()
d10.dtypes
d10.info()
d10.describe()


# In[36]:


d10


# In[37]:


d10.isnull().any()


# In[38]:


artt=[x for x in d10]
print(artt)


# In[39]:


d10['Strike Rate1']=None
d10['Economy1']=None


# In[40]:


martt=['Runs', 'Balls', 'Four', 'Six', 'Strike Rate', 'Balls Bowled', 'Runs Conceded',
       'Economy', 'Wickets']
for x in martt:
    d10[x].fillna(0, inplace=True)
    


# In[41]:


d10.isnull().any()


# In[42]:


for i in range(d10.shape[0]):
    try:
        d10['Strike Rate1'][i]=float(d10['Strike Rate'][i])
    except ValueError:
        d10['Strike Rate1'][i]=0.0
    try:
        d10['Economy1'][i]=float(d10['Economy'][i])
    except ValueError:
        d10['Economy1'][i]=0.0


# In[43]:


#pd.set_option('display.max_rows',500)
#pd.set_option('display.max_columns',100)
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
d10.isnull().any()
d10


# In[44]:


print([x for x in d10], '\n')
print(len(d10['Player Name'].unique()))


# In[45]:


lbl=['Strike Rate', 'Balls']
plt.scatter(d10['Runs'],d10['Strike Rate1'],c='blue')
plt.scatter(d10['Runs'],d10['Balls'],c='red')
plt.legend(lbl)
plt.xlabel('Run')
plt.ylabel('StrikeRate/Balls')
plt.title('Scatter Visulization',fontsize=14)


# In[46]:


lbl=['Strike Rate','Run Outs','Four', 'Six']
plt.scatter(d10['Matches Played'],d10['Strike Rate1'],c='blue')
plt.scatter(d10['Matches Played'],d10['Run Outs'],c='black')
plt.scatter(d10['Matches Played'],d10['Four'],c='green')
plt.scatter(d10['Matches Played'],d10['Six'],c='red')
plt.legend(lbl)
plt.xlabel('Matches Played')
plt.ylabel('StrikeRate/Run Outs/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[47]:


lbl=['Runs Conceded','Balls Bowled','Wickets']
plt.scatter(d10['Runs Conceded'],d10['Economy1'],c='green')
plt.scatter(d10['Balls Bowled'],d10['Economy1'],c='yellow')
plt.scatter(d10['Wickets'],d10['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('RunsConceded/BallsBowled/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[48]:


lbl=['Matches Played', 'Wickets']
plt.scatter(d10['Matches Played'], d10['Economy1'],c='blue')
plt.scatter(d10['Wickets'],d10['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[49]:


lbl=['Ct_St','Run Outs','Four', 'Six']
plt.scatter(d10['Matches Played'],d10['ct_st'],c='red')
plt.scatter(d10['Matches Played'],d10['Run Outs'],c='black')
plt.scatter(d10['Matches Played'],d10['Four'],c='blue')
plt.scatter(d10['Matches Played'],d10['Six'],c='green')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('ct_st/Run Outs/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[50]:


val=['2010','0','450','0','380','10' ,'50' ,'0' ,'15' ,'12' ,'50','6','300','10','400',
     '0','15','5','15','0','2.5','1','16','120','190','7','10']
fo.write('3')
for va in val:
    fo.write(',')
    fo.write(va)
fo.write('\n')


# In[51]:


d11=pd.read_csv("1902HackDATA/IPL2011CSV.csv")

#***Basic/General/Normal Information
d11.head()
d11.dtypes
d11.info()
d11.describe()


# In[52]:


d11


# In[53]:


d11.isnull().any()


# In[54]:


print([x for x in d11], '\n', len(d09['Player'].unique()))


# In[55]:


martt11=['Runs', 'Balls ', 'Strike Rate', 'Four', 'Six', 'Balls Bowled', 'Runs Conceded',
       'Wicket', 'Economy']
for x in martt11:
    d11[x].fillna(0, inplace=True)
    


# In[56]:


d11['Strike Rate1']=None
d11['Economy1']=None


# In[57]:


for i in range(d11.shape[0]):
    try:
        d11['Strike Rate1'][i]=float(d11['Strike Rate'][i])
    except ValueError:
        d11['Strike Rate1'][i]=0.0
    try:
        d11['Economy1'][i]=float(d11['Economy'][i])
    except ValueError:
        d11['Economy1'][i]=0.0


# In[58]:


d11.isnull().any()


# In[59]:


pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',100)
#pd.reset_option('display.max_rows')
#pd.reset_option('display.max_columns')
#d11.isnull().any()
d11


# In[60]:


print([x for x in d11], '\n')
print(len(d11['Player Name'].unique()))


# In[61]:


lbl=['Strike Rate', 'Balls']
plt.scatter(d11['Runs'],d11['Strike Rate1'],c='blue')
plt.scatter(d11['Runs'],d11['Balls '],c='red')
plt.legend(lbl)
plt.xlabel('Run')
plt.ylabel('StrikeRate/Balls')
plt.title('Scatter Visulization',fontsize=14)


# In[62]:


lbl=['Strike Rate','Run Outs','Four', 'Six']
plt.scatter(d11['Matches Played'],d11['Strike Rate1'],c='blue')
plt.scatter(d11['Matches Played'],d11['Run Outs'],c='black')
plt.scatter(d11['Matches Played'],d11['Four'],c='green')
plt.scatter(d11['Matches Played'],d11['Six'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('StrikeRate/RunOuts/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[63]:


lbl=['Runs Conceded','Balls Bowled','Wickets']
plt.scatter(d11['Runs Conceded'],d11['Economy1'],c='green')
plt.scatter(d11['Balls Bowled'],d11['Economy1'],c='yellow')
plt.scatter(d11['Wicket'],d11['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('RunsConcede/BallsBowled/Wicket')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[64]:


lbl=['Matches Played', 'Wickets']
plt.scatter(d11['Matches Played'], d11['Economy1'],c='blue')
plt.scatter(d11['Wicket'],d11['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed/Wicket')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[65]:


lbl=['Ct_St','Run Outs','Four', 'Six']
plt.scatter(d11['Matches Played'],d11['ct_st'],c='red')
plt.scatter(d11['Matches Played'],d11['Run Outs'],c='black')
plt.scatter(d11['Matches Played'],d11['Four'],c='blue')
plt.scatter(d11['Matches Played'],d11['Six'],c='green')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('ct_st/Run Outs/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[66]:


val=['2011','0','480','0','400','20' ,'55' ,'5' ,'20' ,'12' ,'50','12','300','10','400','4',
     '15','8','20','0','2.5','1','16','130','200','7','12']
fo.write('4')
for va in val:
    fo.write(',')
    fo.write(va)
fo.write('\n')


# In[67]:


d12=pd.read_csv("1902HackDATA/IPL2012CSV.csv")

#***Basic/General/Normal Information
d12.head()
d12.dtypes
d12.info()
d12.describe()


# In[68]:


d12.isnull().any()


# In[69]:


d12['Strike Rate1']=None
d12['Economy1']=None


# In[70]:


for i in range(d12.shape[0]):
    try:
        d12['Strike Rate1'][i]=float(d12['Strike Rate'][i])
    except ValueError:
        d12['Strike Rate1'][i]=0.0
    try:
        d12['Economy1'][i]=float(d12['Economy'][i])
    except ValueError:
        d12['Economy1'][i]=0.0


# In[71]:


#pd.set_option('display.max_rows',500)
#pd.set_option('display.max_columns',100)
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
d12


# In[72]:


#d12.isnull().any()
print([x for x in d12], '\n')
print(len(d12["Player's Name"].unique()))


# In[73]:


lbl=['Strike Rate', 'Balls']
plt.scatter(d12['Run'],d12['Strike Rate1'],c='blue')
plt.scatter(d12['Run'],d12['Ball'],c='red')
plt.legend(lbl)
plt.xlabel('Run')
plt.ylabel('StrikeRate/Ball')
plt.title('Scatter Visulization',fontsize=14)


# In[74]:


lbl=['Strike Rate','Four', 'Six']
plt.scatter(d12['Matches Played'],d12['Strike Rate1'],c='blue')
plt.scatter(d12['Matches Played'],d12['Four'],c='green')
plt.scatter(d12['Matches Played'],d12['Six'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('StrikeRate/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[75]:


lbl=['Runs Conceded','Balls Bowled','Wickets']
plt.scatter(d12['Runs Concede'],d12['Economy1'],c='green')
plt.scatter(d12['Balls Bowled'],d12['Economy1'],c='yellow')
plt.scatter(d12['Wickets'],d12['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('RunsConcede/BallsBowled/Wicket')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[76]:


lbl=['Matches Played', 'Wickets']
plt.scatter(d12['Matches Played'], d12['Economy1'],c='blue')
plt.scatter(d12['Wickets'],d12['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[77]:


lbl=['Ct_St','Four', 'Six']
plt.scatter(d12['Matches Played'],d12['Ct_St'],c='red')
plt.scatter(d12['Matches Played'],d12['Four'],c='blue')
plt.scatter(d12['Matches Played'],d12['Six'],c='green')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('Ct_St/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[78]:


val=['2012','0','495','0','480','25' ,'60' ,'3' ,'10' ,'0' ,'0','12','350','20','380','5',
     '18','8','10','0','2','1','17','130','170','7.1','9']
fo.write('5')
for va in val:
    fo.write(',')
    fo.write(va)
fo.write('\n')


# In[79]:


d13=pd.read_csv("1902HackDATA/IPL2013CSV.csv")

#***Basic/General/Normal Information
d13.head()
d13.dtypes
d13.info()
d13.describe()


# In[80]:


#d13
d13.isnull().any()


# In[81]:


d13['Strike Rate1']=None
d13['Economy1']=None


# In[82]:


for i in range(d13.shape[0]):
    try:
        d13['Strike Rate1'][i]=float(d13['Strike Rate'][i])
    except ValueError:
        d13['Strike Rate1'][i]=0.0
    try:
        d13['Economy1'][i]=float(d13['Economy'][i])
    except ValueError:
        d13['Economy1'][i]=0.0


# In[83]:


#pd.set_option('display.max_rows',500)
#pd.set_option('display.max_columns',100)
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
#d13.isnull().any()
d13


# In[84]:


print([x for x in d13], '\n')
print(len(d13["Player's Name"].unique()))


# In[85]:


lbl=['Strike Rate', 'Balls']
plt.scatter(d13['Run'],d13['Strike Rate1'],c='blue')
plt.scatter(d13['Run'],d13['Ball'],c='red')
plt.legend(lbl)
plt.xlabel('Run')
plt.ylabel('StrikeRate/Ball')
plt.title('Scatter Visulization',fontsize=14)


# In[86]:


lbl=['Balls','Strike Rate']
plt.scatter(d13['Highest Run Scored'],d13['Ball'],c='red')
plt.scatter(d13['Highest Run Scored'],d13['Strike Rate1'],c='green')
plt.legend(lbl)
plt.xlabel('HighestRunScored')
plt.ylabel('Ball/Strike Rate')
plt.title('Scatter Visulization',fontsize=14)


# In[87]:


lbl=['Strike Rate', 'Run Outs', 'Four', 'Six']
plt.scatter(d13['Matches Played'],d13['Strike Rate1'],c='blue')
plt.scatter(d13['Matches Played'],d13['Run Outs'],c='black')
plt.scatter(d13['Matches Played'],d13['Four'],c='green')
plt.scatter(d13['Matches Played'],d13['Six'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('StrikeRate/RunOuts/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[88]:


lbl=['Runs Conceded','Balls Bowled','Wickets']
plt.scatter(d13['RunsConceded'],d13['Economy1'],c='green')
plt.scatter(d13['BallsBowled'],d13['Economy1'],c='yellow')
plt.scatter(d13['Wickets'],d13['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('RunsConcede/BallsBowled/Wicket')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[89]:


lbl=['Matches Played', 'Wickets']
plt.scatter(d13['Matches Played'], d13['Economy1'],c='blue')
plt.scatter(d13['Wickets'],d13['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[90]:


lbl=['Ct_St', 'Run Outs', 'Four', 'Six']
plt.scatter(d13['Matches Played'],d13['Ct_St'],c='red')
plt.scatter(d13['Matches Played'],d13['Run Outs'],c='black')
plt.scatter(d13['Matches Played'],d13['Four'],c='blue')
plt.scatter(d13['Matches Played'],d13['Six'],c='green')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('Ct_St/RunOuts/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[91]:


val=['2013','0','540','0','450','28' ,'65' ,'10' ,'20' ,'20' ,'100','12','405',
     '10','490','7','11','10','20','0','2.5','1','18','130','180','7.5','10.5']
fo.write('6')
for va in val:
    fo.write(',')
    fo.write(va)
fo.write('\n')


# In[92]:


d14=pd.read_csv("1902HackDATA/IPL2014CSV.csv")

#***Basic/General/Normal Information
d14.head()
d14.dtypes
d14.info()
d14.describe()


# In[93]:


#d14
d14.isnull().any()


# In[94]:


d14['Strike Rate1']=None
d14['Economy1']=None


# In[95]:


for i in range(d14.shape[0]):
    try:
        d14['Strike Rate1'][i]=float(d14['Strike Rate'][i])
    except ValueError:
        d14['Strike Rate1'][i]=0.0
    try:
        d14['Economy1'][i]=float(d14['Economy'][i])
    except ValueError:
        d14['Economy1'][i]=0.0


# In[96]:


#pd.set_option('display.max_rows',500)
#pd.set_option('display.max_columns',100)
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
#d14.isnull().any()
d14


# In[97]:


print([x for x in d14], '\n')
print(len(d14['Players Name'].unique()))


# In[98]:


lbl=['Strike Rate', 'Balls']
plt.scatter(d14['Run'],d14['Strike Rate1'],c='blue')
plt.scatter(d14['Run'],d14['Ball'],c='red')
plt.legend(lbl)
plt.xlabel('Run')
plt.ylabel('StrikeRate/Ball')
plt.title('Scatter Visulization',fontsize=14)


# In[99]:


lbl=['Balls','Strike Rate']
plt.scatter(d14['Highest Run Scored'],d14['Ball'],c='red')
plt.scatter(d14['Highest Run Scored'],d14['Strike Rate1'],c='green')
plt.legend(lbl)
plt.xlabel('HighestRunScored')
plt.ylabel('Ball/StrikeRate')
plt.title('Scatter Visulization',fontsize=14)


# In[100]:


lbl=['Strike Rate', 'Run Outs', 'Four', 'Six']
plt.scatter(d14['Matches Played'],d14['Strike Rate1'],c='blue')
plt.scatter(d14['Matches Played'],d14['Run Outs'],c='black')
plt.scatter(d14['Matches Played'],d14['Four'],c='green')
plt.scatter(d14['Matches Played'],d14['Six'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('StrikeRate/RunOuts/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[101]:


lbl=['Runs Conceded','Balls Bowled','Wickets']
plt.scatter(d14['Runs Scored'],d14['Economy1'],c='green')
plt.scatter(d14['Balls Bowled'],d14['Economy1'],c='yellow')
plt.scatter(d14['Wickets'],d14['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('RunsConceded/BallsBowled/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[102]:


lbl=['Matches Played', 'Wickets']
plt.scatter(d14['Matches Played'], d14['Economy1'],c='blue')
plt.scatter(d14['Wickets'],d14['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[103]:


lbl=['Ct_St', 'Run Outs', 'Four', 'Six']
plt.scatter(d14['Matches Played'],d14['Ct_St'],c='red')
plt.scatter(d14['Matches Played'],d14['Run Outs'],c='black')
plt.scatter(d14['Matches Played'],d14['Four'],c='blue')
plt.scatter(d14['Matches Played'],d14['Six'],c='green')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('Ct_St/RunOuts/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[104]:


val=['2014','10','450','20','390','25' ,'50' ,'5' ,'24' ,'10' ,'100','12','390','20',
     '490','2','19','8','18','0','2.5','1','16','100','150','7','12']
fo.write('7')
for va in val:
    fo.write(',')
    fo.write(va)
fo.write('\n')


# In[105]:


d15=pd.read_csv("1902HackDATA/IPL2015CSV.csv")

#***Basic/General/Normal Information
d15.head()
d15.dtypes
d15.info()
d15.describe()


# In[106]:


d15.isnull().any()


# In[107]:


d15['Strike Rate1']=None
d15['Economy1']=None


# In[108]:


for i in range(d15.shape[0]):
    try:
        d15['Strike Rate1'][i]=float(d15['Strike Rate'][i])
    except ValueError:
        d15['Strike Rate1'][i]=0.0
    try:
        d15['Economy1'][i]=float(d15['Economy'][i])
    except ValueError:
        d15['Economy1'][i]=0.0


# In[109]:


#pd.set_option('display.max_rows',500)
#pd.set_option('display.max_columns',100)
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
#d14.isnull().any()
d15


# In[110]:


print([x for x in d15], '\n')
print(len(d15["Player's Name"].unique()))


# In[111]:


lbl=['Strike Rate', 'Balls']
plt.scatter(d15['Run'],d15['Strike Rate1'],c='blue')
plt.scatter(d15['Run'],d15['Ball'],c='red')
plt.legend(lbl)
plt.xlabel('Run')
plt.ylabel('StrikeRate/Ball')
plt.title('Scatter Visulization',fontsize=14)


# In[112]:


lbl=['Balls','Strike Rate']
plt.scatter(d15['Highest Run Scored'],d15['Ball'],c='red')
plt.scatter(d15['Highest Run Scored'],d15['Strike Rate1'],c='green')
plt.legend(lbl)
plt.xlabel('HighestRunScored')
plt.ylabel('Ball/StrikeRate')
plt.title('Scatter Visulization',fontsize=14)


# In[113]:


lbl=['Strike Rate', 'Run Outs', 'Four', 'Six']
plt.scatter(d15['Matches Played'],d15['Strike Rate1'],c='blue')
plt.scatter(d15['Matches Played'],d15['Run Outs'],c='black')
plt.scatter(d15['Matches Played'],d15['Four'],c='green')
plt.scatter(d15['Matches Played'],d15['Six'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('StrikeRate/RunOuts/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[114]:


lbl=['Runs Conceded','Balls Bowled','Wickets']
plt.scatter(d15['Runs Conceded'],d15['Economy1'],c='green')
plt.scatter(d15['Balls Bowled'],d15['Economy1'],c='yellow')
plt.scatter(d15['Wickets'],d15['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('RunsConceded/BallsBowled/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[115]:


lbl=['Matches Played', 'Wickets']
plt.scatter(d15['Matches Played'], d15['Economy1'],c='blue')
plt.scatter(d15['Wickets'],d15['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[116]:


lbl=['Ct_St', 'Run Outs', 'Four', 'Six']
plt.scatter(d15['Matches Played'],d15['Ct_St'],c='red')
plt.scatter(d15['Matches Played'],d15['Run Outs'],c='black')
plt.scatter(d15['Matches Played'],d15['Four'],c='blue')
plt.scatter(d15['Matches Played'],d15['Six'],c='green')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('Ct_St/RunOuts/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[117]:


val=['2015','20','480','30','330','15' ,'40' ,'5' ,'12' ,'10' ,'110','12','330','10',
     '410','7','22','8','16','0','3.1','1','17','125','180','7.8','11']
fo.write('8')
for va in val:
    fo.write(',')
    fo.write(va)
fo.write('\n')


# In[118]:


d16=pd.read_csv("1902HackDATA/IPL2016CSV.csv")

#***Basic/General/Normal Information
d16.head()
d16.dtypes
d16.info()
d16.describe()


# In[119]:


d16.isnull().any()


# In[120]:


d16['Ct_St'].fillna(0, inplace=True)


# In[121]:


d16['Strike Rate1']=None
d16['Economy1']=None


# In[122]:


for i in range(d16.shape[0]):
    try:
        d16['Strike Rate1'][i]=float(d16['Strike Rate'][i])
    except ValueError:
        d16['Strike Rate1'][i]=0.0
    try:
        d16['Economy1'][i]=float(d16['Economy'][i])
    except ValueError:
        d16['Economy1'][i]=0.0


# In[123]:


#pd.set_option('display.max_rows',500)
#pd.set_option('display.max_columns',100)
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
#d16.isnull().any()
d16


# In[124]:


print([x for x in d16], '\n')
print(len(d16["Player's Name"].unique()))


# In[125]:


lbl=['Strike Rate', 'Balls']
plt.scatter(d16['Run'],d16['Strike Rate1'],c='blue')
plt.scatter(d16['Run'],d16['Ball'],c='red')
plt.legend(lbl)
plt.xlabel('Run')
plt.ylabel('StrikeRate/Ball')
plt.title('Scatter Visulization',fontsize=14)


# In[126]:


lbl=['Balls','Strike Rate']
plt.scatter(d16['Highest Run Scored'],d16['Ball'],c='red')
plt.scatter(d16['Highest Run Scored'],d16['Strike Rate1'],c='green')
plt.legend(lbl)
plt.xlabel('HigestRunScored')
plt.ylabel('Ball/StrikeRate')
plt.title('Scatter Visulization',fontsize=14)


# In[127]:


lbl=['Strike Rate', 'Run Outs', 'Four', 'Six']
plt.scatter(d16['Matches Played'],d16['Strike Rate1'],c='blue')
plt.scatter(d16['Matches Played'],d16['Run Outs'],c='black')
plt.scatter(d16['Matches Played'],d16['Four'],c='green')
plt.scatter(d16['Matches Played'],d16['Six'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('StrikeRate/RunOuts/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[128]:


lbl=['Runs Conceded','Balls Bowled','Wickets']
plt.scatter(d16['Runs Conceded'],d16['Economy1'],c='green')
plt.scatter(d16['Balls Bowled'],d16['Economy1'],c='yellow')
plt.scatter(d16['Wickets'],d16['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('RunConcede/BallBowled/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[129]:


lbl=['Matches Played', 'Wickets']
plt.scatter(d16['Matches Played'], d16['Economy1'],c='blue')
plt.scatter(d16['Wickets'],d16['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[130]:


lbl=['Ct_St', 'Run Outs', 'Four', 'Six']
plt.scatter(d16['Matches Played'],d16['Ct_St'],c='red')
plt.scatter(d16['Matches Played'],d16['Run Outs'],c='black')
plt.scatter(d16['Matches Played'],d16['Four'],c='blue')
plt.scatter(d16['Matches Played'],d16['Six'],c='green')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('Ct_St/RunOuts/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[131]:


val=['2016','30','500','40','470','18' ,'60' ,'8' ,'24' ,'10' ,'113','12','360','10','410',
     '3','20','8','20','0','2.5','1','17','100','160','7.5','10']
fo.write('9')
for va in val:
    fo.write(',')
    fo.write(va)
fo.write('\n')


# In[132]:


d17=pd.read_csv("1902HackDATA/IPL2017CSV.csv")

#***Basic/General/Normal Information
d17.head()
d17.dtypes
d17.info()
d17.describe()


# In[133]:


d17.isnull().any()


# In[134]:


d17['Six'].fillna(0, inplace=True)


# In[135]:


d17['Strike Rate1']=None
d17['Economy1']=None


# In[136]:


for i in range(d17.shape[0]):
    try:
        d17['Strike Rate1'][i]=float(d17['Strike Rate'][i])
    except ValueError:
        d17['Strike Rate1'][i]=0.0
    try:
        d17['Economy1'][i]=float(d17['Economy'][i])
    except ValueError:
        d17['Economy1'][i]=0.0


# In[137]:


#pd.set_option('display.max_rows',500)
#pd.set_option('display.max_columns',100)
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
#d17.isnull().any()
d17


# In[138]:


print([x for x in d17], '\n')
print(len(d17["Player's Name"].unique()))


# In[139]:


lbl=['Strike Rate', 'Balls']
plt.scatter(d17['Run'],d17['Strike Rate1'],c='blue')
plt.scatter(d17['Run'],d17['Ball'],c='red')
plt.legend(lbl)
plt.xlabel('Run')
plt.ylabel('StrikeRate/Ball')
plt.title('Scatter Visulization',fontsize=14)


# In[140]:


lbl=['Balls','Strike Rate']
plt.scatter(d17['Highest Run Scored'],d17['Ball'],c='red')
plt.scatter(d17['Highest Run Scored'],d17['Strike Rate1'],c='green')
plt.legend(lbl)
plt.xlabel('HighestRunScored')
plt.ylabel('Ball/StrikeRate')
plt.title('Scatter Visulization',fontsize=14)


# In[141]:


lbl=['Strike Rate', 'Run Outs', 'Four', 'Six']
plt.scatter(d17['Matches Played'],d17['Strike Rate1'],c='blue')
plt.scatter(d17['Matches Played'],d17['Run Outs'],c='black')
plt.scatter(d17['Matches Played'],d17['Four'],c='green')
plt.scatter(d17['Matches Played'],d17['Six'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('StrikeRate/RunOuts/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[142]:


lbl=['Runs Conceded','Balls Bowled','Wickets']
plt.scatter(d17['Runs Conceded'],d17['Economy1'],c='green')
plt.scatter(d17['Balls Bowled'],d17['Economy1'],c='yellow')
plt.scatter(d17['Wickets'],d17['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('RunConceded/BallBowled/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[143]:


lbl=['Matches Played', 'Wickets']
plt.scatter(d17['Matches Played'], d17['Economy1'],c='blue')
plt.scatter(d17['Wickets'],d17['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[144]:


lbl=['Ct_St', 'Run Outs', 'Four', 'Six']
plt.scatter(d17['Matches Played'],d17['Ct_St'],c='red')
plt.scatter(d17['Matches Played'],d17['Run Outs'],c='black')
plt.scatter(d17['Matches Played'],d17['Four'],c='blue')
plt.scatter(d17['Matches Played'],d17['Six'],c='green')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('Ct_St/RunOuts/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[145]:


val=['2017','10','500','10','400','25' ,'40' ,'10' ,'26' ,'10' ,'105','18','340','20','430',
     '3','18','10','17','0','3.5','1','17','130','160','7.5','12']
fo.write('10')
for va in val:
    fo.write(',')
    fo.write(va)
fo.write('\n')


# In[146]:


d18=pd.read_csv("1902HackDATA/IPL2018CSV.csv")

#***Basic/General/Normal Information
d18.head()
d18.dtypes
d18.info()
d18.describe()


# In[147]:


#d18.isnull().any().count()
pd.isnull(d18).sum()


# In[148]:


d18['Economy'].fillna(0, inplace=True)


# In[149]:


d18['Strike Rate1']=None
d18['Economy1']=None


# In[150]:


for i in range(d18.shape[0]):
    try:
        d18['Strike Rate1'][i]=float(d18['Strike Rate'][i])
    except ValueError:
        d18['Strike Rate1'][i]=0.0
    try:
        d18['Economy1'][i]=float(d18['Economy'][i])
    except ValueError:
        d18['Economy1'][i]=0.0


# In[151]:


#pd.set_option('display.max_rows',500)
#pd.set_option('display.max_columns',100)
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
#d18.isnull().any()
d18


# In[152]:


print([x for x in d18], '\n')
print(len(d18["Player's Name"].unique()))


# In[153]:


lbl=['Strike Rate', 'Balls']
plt.scatter(d18['Run'],d18['Strike Rate1'],c='blue')
plt.scatter(d18['Run'],d18['Ball'],c='red')
plt.legend(lbl)
plt.xlabel('Run')
plt.ylabel('StrikeRate/Ball')
plt.title('Scatter Visulization',fontsize=14)


# In[154]:


lbl=['Balls','Strike Rate']
plt.scatter(d18['Highest Run Scored'],d18['Ball'],c='red')
plt.scatter(d18['Highest Run Scored'],d18['Strike Rate1'],c='green')
plt.legend(lbl)
plt.xlabel('HighestRunScored')
plt.ylabel('Ball/StrikeRate')
plt.title('Scatter Visulization',fontsize=14)


# In[155]:


lbl=['Strike Rate', 'Run Outs', 'Four', 'Six']
plt.scatter(d18['Matches Played'],d18['Strike Rate1'],c='blue')
plt.scatter(d18['Matches Played'],d18['Run Outs'],c='black')
plt.scatter(d18['Matches Played'],d18["4's"],c='green')
plt.scatter(d18['Matches Played'],d18["6's"],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('StrikeRate/RunOuts/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[156]:


lbl=['Runs Conceded','Balls Bowled','Wickets']
plt.scatter(d18['Runs Scored'],d18['Economy1'],c='green')
plt.scatter(d18['Balls  Bowled'],d18['Economy1'],c='yellow')
plt.scatter(d18['Wickets'],d18['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('RunsConcede/BallsBowled/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[157]:


lbl=['Matches Played', 'Wickets']
plt.scatter(d18['Matches Played'], d18['Economy1'],c='blue')
plt.scatter(d18['Wickets'],d18['Economy1'],c='red')
plt.legend(lbl)
plt.xlabel('MatchesPlayed/Wickets')
plt.ylabel('Economy')
plt.title('Scatter Visulization',fontsize=14)


# In[158]:


lbl=['Ct_St', 'Run Outs', 'Four', 'Six']
plt.scatter(d18['Matches Played'],d18['Ct_St'],c='red')
plt.scatter(d18['Matches Played'],d18['Run Outs'],c='black')
plt.scatter(d18['Matches Played'],d18["4's"],c='blue')
plt.scatter(d18['Matches Played'],d18["6's"],c='green')
plt.legend(lbl)
plt.xlabel('MatchesPlayed')
plt.ylabel('Ct_St/RunOuts/Four/Six')
plt.title('Scatter Visulization',fontsize=14)


# In[159]:


val=['2018','20','600','30','420','20' ,'60' ,'8' ,'27' ,'12' ,'115','12','400','20','480',
     '2','19','9','18.5','0','2.5','1','17','140','180','7.4','11.9']
fo.write('11')
for va in val:
    fo.write(',')
    fo.write(va)
fo.write('\n')
fo.close()


# In[160]:


dptr=pd.read_csv("1902HackDATA/PdtrCSV.csv")
#***Basic/General/Normal Information
dptr.head()
dptr.dtypes
dptr.info()
dptr.describe()


# In[161]:


#pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',100)
#pd.reset_option('display.max_rows')
#pd.reset_option('display.max_columns')
#ddptr.isnull().any()
dptr


# In[162]:


dptr.shape


# In[163]:


lbl=[pdtr[x] for x in range(1,7)]
plt.plot(dptr['Year'], dptr[lbl[0]],c='purple')
plt.plot(dptr['Year'], dptr[lbl[1]],c='red')
plt.plot(dptr['Year'], dptr[lbl[2]],c='blue')
plt.plot(dptr['Year'], dptr[lbl[3]],c='green')
plt.plot(dptr['Year'], dptr[lbl[4]],c='brown')
plt.plot(dptr['Year'], dptr[lbl[5]],c='black')
plt.xlabel('Year')
plt.ylabel('Statistic')
plt.legend(lbl)
plt.title('Line Plot Visulization',fontsize=14)


# In[164]:


lbl=[pdtr[x] for x in range(7,15)]
plt.plot(dptr['Year'], dptr[lbl[0]],c='purple')
plt.plot(dptr['Year'], dptr[lbl[1]],c='red')
plt.plot(dptr['Year'], dptr[lbl[2]],c='blue')
plt.plot(dptr['Year'], dptr[lbl[3]],c='green')
plt.plot(dptr['Year'], dptr[lbl[4]],c='yellow')
plt.plot(dptr['Year'], dptr[lbl[5]],c='black')
plt.plot(dptr['Year'], dptr[lbl[6]],c='cyan')
plt.plot(dptr['Year'], dptr[lbl[7]],c='magenta')
plt.xlabel('Year')
plt.ylabel('Statistic')
plt.legend(lbl)
plt.title('Line Plot Visulization',fontsize=14)


# In[165]:


lbl=[pdtr[x] for x in range(15,21)]
plt.plot(dptr['Year'], dptr[lbl[0]],c='purple')
plt.plot(dptr['Year'], dptr[lbl[1]],c='red')
plt.plot(dptr['Year'], dptr[lbl[2]],c='blue')
plt.plot(dptr['Year'], dptr[lbl[3]],c='green')
plt.plot(dptr['Year'], dptr[lbl[4]],c='yellow')
plt.plot(dptr['Year'], dptr[lbl[5]],c='black')
plt.xlabel('Year')
plt.ylabel('Statistic')
plt.legend(lbl)
plt.title('Line Plot Visulization',fontsize=14)


# In[166]:


lbl=[pdtr[x] for x in range(21,27)]
plt.plot(dptr['Year'], dptr[lbl[0]],c='olive')
plt.plot(dptr['Year'], dptr[lbl[1]],c='red')
plt.plot(dptr['Year'], dptr[lbl[2]],c='blue')
plt.plot(dptr['Year'], dptr[lbl[3]],c='green')
plt.plot(dptr['Year'], dptr[lbl[4]],c='grey')
plt.plot(dptr['Year'], dptr[lbl[5]],c='black')
plt.xlabel('Year')
plt.ylabel('Statistic')
plt.legend(lbl)
plt.title('Line Plot Visulization',fontsize=14)


# In[167]:


ev_al_m=['Year', 'Run', 'Ball', "4's", "6's", 'Highest Run Scored', 'Balls  Bowled', 'Runs Conceded', 'Wickets',
         'Ct_St', 'Run Outs', 'Matches Played', 'Strike Rate1', 'Economy1']
evbt=['Year', 'Run', 'Ball', "4's", "6's", 'Highest Run Scored', 'Wickets', 'Ct_St','Run Outs', 'Matches Played', 'Strike Rate1']
evbl=['Year', 'Highest Run Scored', 'Balls  Bowled', 'Runs Conceded', 'Wickets', 'Ct_St', 'Run Outs', 'Matches Played', 'Economy1']


# In[168]:


val19=[]
for x in dptr:
    sm=0
    for i in range(6):
        sm+=float(dptr[x][i])
    for i in range(6,11):
        sm+=(i-5)*float(dptr[x][i])
    val19.append(round(sm/21,5))
val19[0]=12
val19[1]=2019
#print(val19)
val19m=[]
for x in range(0, len(val19), 2):
     ttt=(float(val19[x])+float(val19[x+1]))/2
     val19m.append(round(ttt,5))
val19m[0]=2019
#print(val19m)   


# In[169]:


val19bt=[2019]
val19bl=[2019]
val19al=[2019]
for x in range(2,12,2):
    ttt=(float(val19[x])+2.82*float(val19[x+1]))/3
    val19bt.append(round(ttt,5))
for x in range(2,10,2):
    ttt=(float(val19[x])+2.82*float(val19[x+1]))/3
    val19al.append(round(ttt,5))
for x in range(10, 15, 2):
    ttt=(7*float(val19[x])+float(val19[x+1]))/7
    val19bl.append(round(ttt,5))
    val19al.append(round(ttt,5))
ttt=(float(val19[16])+0.45*float(val19[17]))/2
val19bt.append(round(ttt,5))
ttt=(float(val19[16])+1.4*float(val19[17]))/2
val19bl.append(round(ttt,5))
ttt=(float(val19[16])+1.05*float(val19[17]))/2
val19al.append(round(ttt,5))
for x in range(18, 22, 2):
    ttt=(float(val19[x])+1.3*float(val19[x+1]))/2
    val19bt.append(round(ttt,5))
    val19bl.append(round(ttt,5))
    val19al.append(round(ttt,5))    
ttt=(float(val19[22])+1.72*float(val19[23]))/2
val19bt.append(round(ttt,5))
val19bl.append(round(ttt,5))
val19al.append(round(ttt,5))
ttt=(float(val19[24])+7*float(val19[25]))/7
val19bt.append(round(ttt,5))
val19al.append(round(ttt,5))
ttt=(5*float(val19[26])+float(val19[27]))/5
val19bl.append(round(ttt,5))
val19al.append(round(ttt,5))
#print(val19bt)
#print(val19bl)
#print(val19al)


# In[170]:


print(len(val19al),len(val19m),len(ev_al_m))
#print(len(val19al),val19[18],val19[19],val19[20],val19[21],val19[22])
#d14['Run'][1]


# In[171]:


#ev_al_m --> val19m'Pram1' and val19al'Pram2'
#evbt --> val19bt'Pram3'
#evbl --> val19bl'Pram4'
#Because all data set does not have same column name
ev_al_m14=['Year', 'Run', 'Ball', "Four", "Six", 'Highest Run Scored', 'Balls Bowled', 'Runs Scored', 'Wickets',
         'Ct_St', 'Run Outs', 'Matches Played', 'Strike Rate1', 'Economy1']
evbt14=['Year', 'Run','Ball', "Four", "Six", 'Highest Run Scored', 'Wickets', 'Ct_St','Run Outs', 'Matches Played', 'Strike Rate1']
evbl14=['Year','Highest Run Scored','Balls Bowled', 'Runs Scored', 'Wickets', 'Ct_St', 'Run Outs', 'Matches Played', 'Economy1']

ev_al_m15=['Year', 'Run', 'Ball', "Four", "Six", 'Highest Run Scored', 'Balls Bowled', 'Runs Conceded', 'Wickets',
         'Ct_St', 'Run Outs', 'Matches Played', 'Strike Rate1', 'Economy1']
evbt15=['Year', 'Run','Ball', "Four", "Six", 'Highest Run Scored', 'Wickets', 'Ct_St','Run Outs', 'Matches Played', 'Strike Rate1']
evbl15=['Year','Highest Run Scored','Balls Bowled', 'Runs Conceded', 'Wickets', 'Ct_St', 'Run Outs', 'Matches Played', 'Economy1']

ev_al_m16=['Year', 'Run', 'Ball', "Four", "Six", 'Highest Run Scored', 'Balls Bowled', 'Runs Conceded', 'Wickets',
         'Ct_St', 'Run Outs', 'Matches Played', 'Strike Rate1', 'Economy1']
evbt16=['Year', 'Run','Ball', "Four", "Six", 'Highest Run Scored', 'Wickets', 'Ct_St','Run Outs', 'Matches Played', 'Strike Rate1']
evbl16=['Year','Highest Run Scored','Balls Bowled', 'Runs Conceded', 'Wickets', 'Ct_St', 'Run Outs', 'Matches Played', 'Economy1']

ev_al_m17=['Year', 'Run', 'Ball', "Four", "Six", 'Highest Run Scored', 'Balls Bowled', 'Runs Conceded', 'Wickets',
         'Ct_St', 'Run Outs', 'Matches Played', 'Strike Rate1', 'Economy1']
evbt17=['Year', 'Run','Ball', "Four", "Six", 'Highest Run Scored', 'Wickets', 'Ct_St','Run Outs', 'Matches Played', 'Strike Rate1']
evbl17=['Year','Highest Run Scored','Balls Bowled', 'Runs Conceded', 'Wickets', 'Ct_St', 'Run Outs', 'Matches Played', 'Economy1']

ev_al_m18=['Year', 'Run', 'Ball', "4's", "6's", 'Highest Run Scored', 'Balls  Bowled', 'Runs Scored', 'Wickets',
         'Ct_St', 'Run Outs', 'Matches Played', 'Strike Rate1', 'Economy1']
evbt18=['Year', 'Run', 'Ball', "4's", "6's", 'Highest Run Scored', 'Wickets', 'Ct_St','Run Outs', 'Matches Played', 'Strike Rate1']
evbl18=['Year', 'Highest Run Scored', 'Balls  Bowled', 'Runs Scored', 'Wickets', 'Ct_St', 'Run Outs', 'Matches Played', 'Economy1']


# In[172]:


d14['Pram_m']=None
d14['Pram_al']=None
d14['Pram_bt']=None
d14['Pram_bl']=None
d14['PramN']=None
pd.set_option('precision', 6)
for i in range(d14.shape[0]):
    tv=0
    for j in range(1, len(val19m)):
        #print(ev_al_m14[j], d14[ev_al_m14[j]][i])
        tv+=(d14[ev_al_m14[j]][i]-val19m[j])**2
    d14['Pram_m'][i]=1000/(tv**0.5)
    
    tv=0
    for j in range(1, len(val19al)):
        tv+=(d14[ev_al_m14[j]][i]-val19al[j])**2
    d14['Pram_al'][i]=1000/(tv**0.5)
    
    tv=0
    for j in range(1, len(val19bt)):
        tv+=(d14[evbt14[j]][i]-val19bt[j])**2
    d14['Pram_bt'][i]=1000/(tv**0.5)
    
    tv=0
    for j in range(1, len(val19bl)):
        tv+=(d14[evbl14[j]][i]-val19bl[j])**2
    d14['Pram_bl'][i]=1000/(tv**0.5)
    
    d14['PramN'][i]=(0.6*d14['Pram_m'][i]+0.75*d14['Pram_al'][i]+0.93*d14['Pram_bt'][i]+0.95*d14['Pram_bl'][i])/4
    


# In[173]:


#print([x for x in d14[ev_al_m14[1]]])
#pd.set_option('display.max_rows',500)
#pd.set_option('display.max_columns',100)
pd.reset_option('display.max_rows')
#pd.reset_option('display.max_columns')
d14
#2**0.5


# In[174]:


d15['Pram_m']=None
d15['Pram_al']=None
d15['Pram_bt']=None
d15['Pram_bl']=None
d15['PramN']=None
pd.set_option('precision', 6)
for i in range(d15.shape[0]):
    tv=0
    for j in range(1, len(val19m)):
        tv+=(d15[ev_al_m15[j]][i]-val19m[j])**2
    d15['Pram_m'][i]=1000/(tv**0.5)
    
    tv=0
    for j in range(1, len(val19al)):
        tv+=(d15[ev_al_m15[j]][i]-val19al[j])**2
    d15['Pram_al'][i]=1000/(tv**0.5)
    
    tv=0
    for j in range(1, len(val19bt)):
        tv+=(d15[evbt15[j]][i]-val19bt[j])**2
    d15['Pram_bt'][i]=1000/(tv**0.5)
    
    tv=0
    for j in range(1, len(val19bl)):
        tv+=(d15[evbl15[j]][i]-val19bl[j])**2
    d15['Pram_bl'][i]=1000/(tv**0.5)
    
    d15['PramN'][i]=(0.6*d15['Pram_m'][i]+0.75*d15['Pram_al'][i]+0.93*d15['Pram_bt'][i]+0.95*d15['Pram_bl'][i])/4
    


# In[175]:


d16['Pram_m']=None
d16['Pram_al']=None
d16['Pram_bt']=None
d16['Pram_bl']=None
d16['PramN']=None
pd.set_option('precision', 6)
for i in range(d16.shape[0]):
    tv=0
    for j in range(1, len(val19m)):
        tv+=(d16[ev_al_m16[j]][i]-val19m[j])**2
    d16['Pram_m'][i]=1000/(tv**0.5)
    
    tv=0
    for j in range(1, len(val19al)):
        tv+=(d16[ev_al_m16[j]][i]-val19al[j])**2
    d16['Pram_al'][i]=1000/(tv**0.5)
    
    tv=0
    for j in range(1, len(val19bt)):
        tv+=(d16[evbt16[j]][i]-val19bt[j])**2
    d16['Pram_bt'][i]=1000/(tv**0.5)
    
    tv=0
    for j in range(1, len(val19bl)):
        tv+=(d16[evbl16[j]][i]-val19bl[j])**2
    d16['Pram_bl'][i]=1000/(tv**0.5)
    
    d16['PramN'][i]=(0.6*d16['Pram_m'][i]+0.75*d16['Pram_al'][i]+0.93*d16['Pram_bt'][i]+0.95*d16['Pram_bl'][i])/4
    


# In[176]:


d17['Pram_m']=None
d17['Pram_al']=None
d17['Pram_bt']=None
d17['Pram_bl']=None
d17['PramN']=None
pd.set_option('precision', 6)
for i in range(d17.shape[0]):
    tv=0
    for j in range(1, len(val19m)):
        tv+=(d17[ev_al_m17[j]][i]-val19m[j])**2
    d17['Pram_m'][i]=1000/(tv**0.5)
    
    tv=0
    for j in range(1, len(val19al)):
        tv+=(d17[ev_al_m17[j]][i]-val19al[j])**2
    d17['Pram_al'][i]=1000/(tv**0.5)
    
    tv=0
    for j in range(1, len(val19bt)):
        tv+=(d17[evbt17[j]][i]-val19bt[j])**2
    d17['Pram_bt'][i]=1000/(tv**0.5)
    
    tv=0
    for j in range(1, len(val19bl)):
        tv+=(d17[evbl17[j]][i]-val19bl[j])**2
    d17['Pram_bl'][i]=1000/(tv**0.5)
    
    d17['PramN'][i]=(0.6*d17['Pram_m'][i]+0.75*d17['Pram_al'][i]+0.93*d17['Pram_bt'][i]+0.95*d17['Pram_bl'][i])/4
    


# In[177]:


d18['Pram_m']=None
d18['Pram_al']=None
d18['Pram_bt']=None
d18['Pram_bl']=None
d18['PramN']=None
pd.set_option('precision', 6)
for i in range(d18.shape[0]):
    tv=0
    for j in range(1, len(val19m)):
        tv+=(d18[ev_al_m18[j]][i]-val19m[j])**2
    d18['Pram_m'][i]=1000/(tv**0.5)
    
    tv=0
    for j in range(1, len(val19al)):
        tv+=(d18[ev_al_m18[j]][i]-val19al[j])**2
    d18['Pram_al'][i]=1000/(tv**0.5)
    
    tv=0
    for j in range(1, len(val19bt)):
        tv+=(d18[evbt18[j]][i]-val19bt[j])**2
    d18['Pram_bt'][i]=1000/(tv**0.5)
    
    tv=0
    for j in range(1, len(val19bl)):
        tv+=(d18[evbl18[j]][i]-val19bl[j])**2
    d18['Pram_bl'][i]=1000/(tv**0.5)
    
    d18['PramN'][i]=(0.6*d18['Pram_m'][i]+0.75*d18['Pram_al'][i]+0.93*d18['Pram_bt'][i]+0.95*d18['Pram_bl'][i])/4
    


# In[178]:


Namels=set()
for x in d16.sort_values(by='Pram_m', ascending=False).head(20)["Player's Name"]:
    Namels.add(x)
for x in d16.sort_values(by='Pram_m', ascending=True).head(10)["Player's Name"]:
    Namels.add(x)
for x in d16.sort_values(by='Pram_al', ascending=False).head(20)["Player's Name"]:
    Namels.add(x)
for x in d16.sort_values(by='Pram_al', ascending=True).head(20)["Player's Name"]:
    Namels.add(x)
for x in d16.sort_values(by='Pram_bt', ascending=False).head(20)["Player's Name"]:
    Namels.add(x)
for x in d16.sort_values(by='Pram_bl', ascending=True).head(20)["Player's Name"]:
    Namels.add(x)
for x in d17.sort_values(by='Pram_m', ascending=False).head(25)["Player's Name"]:
    Namels.add(x)
for x in d17.sort_values(by='Pram_m', ascending=True).head(10)["Player's Name"]:
    Namels.add(x)
for x in d17.sort_values(by='Pram_al', ascending=False).head(25)["Player's Name"]:
    Namels.add(x)
for x in d17.sort_values(by='Pram_al', ascending=True).head(25)["Player's Name"]:
    Namels.add(x)
for x in d17.sort_values(by='Pram_bt', ascending=False).head(25)["Player's Name"]:
    Namels.add(x)
for x in d17.sort_values(by='Pram_bl', ascending=True).head(25)["Player's Name"]:
    Namels.add(x)
for x in d18.sort_values(by='Pram_m', ascending=False).head(30)["Player's Name"]:
    Namels.add(x)
for x in d18.sort_values(by='Pram_m', ascending=True).head(10)["Player's Name"]:
    Namels.add(x)
for x in d18.sort_values(by='Pram_al', ascending=False).head(30)["Player's Name"]:
    Namels.add(x)
for x in d18.sort_values(by='Pram_al', ascending=True).head(30)["Player's Name"]:
    Namels.add(x)
for x in d18.sort_values(by='Pram_bt', ascending=False).head(30)["Player's Name"]:
    Namels.add(x)
for x in d18.sort_values(by='Pram_bl', ascending=True).head(30)["Player's Name"]:
    Namels.add(x)


# In[179]:


#d18.Pram_al1[d18["Player's Name"]==nm].iloc[0]=round(tv/i,5)
#d18.loc[d18["Player's Name"]==nm].iloc[0]=round(tv/i,5)
#pra=['Pram_m','Pram_al','Pram_bt','Pram_bl','PramN']
d16['Pram_Ny']=None
d17['Pram_Ny']=None
d18['Pram_Ny']=None
d16['PramN1']=None
d17['PramN1']=None
d18['PramN1']=None
pd.set_option('precision', 6)
for nm in Namels:
    i=0
    tv1=tv2=tv3=tv4=tv=0
    if(nm in d14["Players Name"].values):
        #print(d14.PramN[d14["Players Name"]==nm].iloc[0],1)
        tv1+=d14.Pram_m[d14["Players Name"]==nm].iloc[0]
        tv2+=d14.Pram_al[d14["Players Name"]==nm].iloc[0]
        tv3+=d14.Pram_bt[d14["Players Name"]==nm].iloc[0]
        tv4+=d14.Pram_bl[d14["Players Name"]==nm].iloc[0]
        i+=1
    if(nm in d15["Player's Name"].values):
        tv1+=1.6*d15.Pram_m[d15["Player's Name"]==nm].iloc[0]
        tv2+=1.6*d15.Pram_al[d15["Player's Name"]==nm].iloc[0]
        tv3+=1.6*d15.Pram_bt[d15["Player's Name"]==nm].iloc[0]
        tv4+=1.6*d15.Pram_bt[d15["Player's Name"]==nm].iloc[0]
        tv+=1.6*d15.PramN[d15["Player's Name"]==nm].iloc[0]
        i+=1
    if(nm in d16["Player's Name"].values):
        tv1+=2*d16.Pram_m[d16["Player's Name"]==nm].iloc[0]
        tv2+=2*d16.Pram_al[d16["Player's Name"]==nm].iloc[0]
        tv3+=2*d16.Pram_bt[d16["Player's Name"]==nm].iloc[0]
        tv4+=2*d16.Pram_bl[d16["Player's Name"]==nm].iloc[0]
        tv+=2*d16.PramN[d16["Player's Name"]==nm].iloc[0]
        i+=1.7
    if(nm in d17["Player's Name"].values):
        tv1+=2.75*d17.Pram_m[d17["Player's Name"]==nm].iloc[0]
        tv2+=2.75*d17.Pram_al[d17["Player's Name"]==nm].iloc[0]
        tv3+=2.75*d17.Pram_bt[d17["Player's Name"]==nm].iloc[0]
        tv4+=2.75*d17.Pram_bl[d17["Player's Name"]==nm].iloc[0]
        tv+=3*d17.PramN[d17["Player's Name"]==nm].iloc[0]
        i+=2.2
    if(nm in d18["Player's Name"].values):
        tv1+=3*d18.Pram_m[d18["Player's Name"]==nm].iloc[0]
        tv2+=3*d18.Pram_al[d18["Player's Name"]==nm].iloc[0]
        tv3+=3*d18.Pram_bt[d18["Player's Name"]==nm].iloc[0]
        tv4+=3*d18.Pram_bl[d18["Player's Name"]==nm].iloc[0]
        tv+=3*d18.PramN[d18["Player's Name"]==nm].iloc[0]
        i+=2.5
    PNy=round((tv1+tv2+tv3+tv4)/(4*i), 5)
    PN1=round(tv/(3*i), 5)
    if(nm in d16["Player's Name"].values):
        d16.loc[d16["Player's Name"]==nm,'Pram_Ny']=PNy
        d16.loc[d16["Player's Name"]==nm,'PramN1']=PN1
    if(nm in d17["Player's Name"].values):
        d17.loc[d17["Player's Name"]==nm,'Pram_Ny']=PNy
        d17.loc[d17["Player's Name"]==nm,'PramN1']=PN1
    if(nm in d18["Player's Name"].values):
        d18.loc[d18["Player's Name"]==nm,'Pram_Ny']=PNy
        d18.loc[d18["Player's Name"]==nm,'PramN1']=PN1       


# In[180]:


for x in d16.sort_values(by='PramN', ascending=False).head(15)["Player's Name"]:
    Namels.add(x)
for x in d16.sort_values(by='PramN', ascending=True).head(15)["Player's Name"]:
    Namels.add(x)
for x in d17.sort_values(by='PramN', ascending=False).head(20)["Player's Name"]:
    Namels.add(x)
for x in d17.sort_values(by='PramN', ascending=True).head(20)["Player's Name"]:
    Namels.add(x)
for x in d18.sort_values(by='PramN', ascending=False).head(25)["Player's Name"]:
    Namels.add(x)
for x in d18.sort_values(by='PramN', ascending=True).head(25)["Player's Name"]:
    Namels.add(x)
len(Namels)            


# In[181]:


NameP19=set()
f19=open("1902HackDATA/IP_L.txt",'r')
for ln in f19:
    tln=ln.strip().split(':')
    if(len(tln)==1):
        if(tln[0] in Namels):
            NameP19.add(tln[0])
print(NameP19,'\n',len(NameP19),len(Namels))


# In[182]:


#print(d17['Type'].unique(),d18['Type'].unique())
print(d17['From'].unique(),d18['From'].unique())


# In[183]:


#consider the Constrains given
x1=d17.loc[(d17['Type']=='WK')&(d17["Player's Name"].isin(NameP19))]
y1=d18.loc[(d18['Type']=='WK')&(d18["Player's Name"].isin(NameP19))]
y1.rename(columns={'Runs Scored':'Runs Conceded'}, inplace=True)
x1.columns=[x for x in y1]
x1['YeaR']='2017'
y1['YeaR']='2018'
d19WK=x1.append(y1)
x1=d17.loc[(d17['Type']=='BAT')&(d17["Player's Name"].isin(NameP19))]
y1=d18.loc[(d18['Type']=='BAT')&(d18["Player's Name"].isin(NameP19))]
y1.rename(columns={'Runs Scored':'Runs Conceded'}, inplace=True)
x1.columns=[x for x in y1]
x1['YeaR']='2017'
y1['YeaR']='2018'
d19BT=x1.append(y1)
x1=d17.loc[(d17['Type']=='Bowl')&(d17["Player's Name"].isin(NameP19))]
y1=d18.loc[(d18['Type']=='Bowl')&(d18["Player's Name"].isin(NameP19))]
y1.rename(columns={'Runs Scored':'Runs Conceded'}, inplace=True)
x1.columns=[x for x in y1]
x1['YeaR']='2017'
y1['YeaR']='2018'
d19BL=x1.append(y1)
x1=d17.loc[(d17['Type']=='AR')&(d17["Player's Name"].isin(NameP19))]
y1=d18.loc[(d18['Type']=='AR')&(d18["Player's Name"].isin(NameP19))]
y1.rename(columns={'Runs Scored':'Runs Conceded'}, inplace=True)
x1.columns=[x for x in y1]
x1['YeaR']='2017'
y1['YeaR']='2018'
d19AR=x1.append(y1)
x1=d17.loc[(d17['From']!='IND')&(d17["Player's Name"].isin(NameP19))]
y1=d18.loc[(d18['From']!='IND')&(d18["Player's Name"].isin(NameP19))]
y1.rename(columns={'Runs Scored':'Runs Conceded'}, inplace=True)
x1.columns=[x for x in y1]
x1['YeaR']='2017'
y1['YeaR']='2018'
d19F=x1.append(y1)
print(d19WK.shape,d19BT.shape,d19BL.shape,d19AR.shape,d19F.shape)


# In[184]:


#Let's select the Team to fight 2019 as d19
# Given at least 1 wivket keepr
S1=d19WK.sort_values(by='Matches Played', ascending=False).head(10)
S2=S1.sort_values(by='Ct_St', ascending=False).head(5)
SW=S2.sort_values(by='Strike Rate1', ascending=False).head(1)
SW


# In[185]:


# Given  at least 2 all-rounder
S1=d19AR.sort_values(by='Matches Played', ascending=False).head(15)
S2=S1.sort_values(by='Wickets', ascending=False).head(12)
S3=S2.sort_values(by='Economy1', ascending=True).head(10)
S4=S3.sort_values(by='Pram_bl', ascending=False).head(5)
S5=s4.sort_values(by='YeaR', ascending=False).head(3)
SAl=S5.sort_values(by='PramN1', ascending=False).head(2)
SAl


# In[186]:


#Given 3 bowler
S1=d19BL.sort_values(by='Matches Played', ascending=False).head(20)
S2=S1.sort_values(by='Wickets', ascending=False).head(15)
S3=S2.sort_values(by='Economy1', ascending=True).head(10)
S4=S3.sort_values(by='Pram_bl', ascending=False).head(7)
SBl=S4.sort_values(by='PramN', ascending=False).head(3)
SBl


# In[187]:


#Given batsman #5
S1=d19BT.sort_values(by='Matches Played', ascending=False).head(20)
S2=S1.sort_values(by='Run', ascending=False).head(15)
S3=S2.sort_values(by='Strike Rate1', ascending=False).head(10)
S4=S3.sort_values(by='YeaR', ascending=False).head(7)
SBt=S4.sort_values(by='YeaR', ascending=False).head(5)
SBt


# In[188]:


#d19.to_csv('1902HackDATA/19WK.csv',sep=',',encoding='utf-8', index=False)
d19t=d19=None
d19t=SW.sort_values(by='Pram_m', ascending=False).head(2)
d19t=d19t.append(SAl)
d19t=d19t.append(SBl)
d19t=d19t.append(SBt)
d19=d19t.drop(['Strike Rate1','Economy1','Pram_m','Pram_al','Pram_bt','Pram_bl','PramN','Pram_Ny','PramN1'], axis=1)
d19['Team']='SuWi11'
d19['Sl.No']=[1,2,3,4,5,6,7,8,9,10,11]
d19.to_csv('Predicter/MyTeam2019.csv',sep=',',encoding='utf-8', index=False)
print(d19.shape)
print("Now You can the  CSV file 'Predicter/MyPlayer2019.csv' and 'Predicter/MyPlayer2019.csv'\n ",
      " from the dirctory to see the our to see Team detail and player's name \n",
      "'Super Wining 11' whose captian is MS Dhoni and vice-captian is Virat Kohli. /n Thanks! ")
f19=open("Predicter/MyTeam2019.txt",'w+')
f19.write("Super Wining 11' whose captian is MS Dhoni and \nvice-captian is Virat Kohli aand Players")
for pl in d19["Player's Name"]:
    f19.write('\n')
    f19.write(pl)
f19.close()
d19

