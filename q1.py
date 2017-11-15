import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import math
import operator


data=pd.read_csv('FullData.csv')

k=data.groupby('Nationality')
xTicks=['varun']
h=['0']
del h[0]
del xTicks[0]
i=0
for name,group in k:
    xTicks.insert(i,name)
    g=[group['Freekick_Accuracy'].agg(np.mean),
    group['Volleys'].agg(np.mean),
    group['Curve'].agg(np.mean),
    group['Long_Shots'].agg(np.mean),
    group['Finishing'].agg(np.mean),
    group['Shot_Power'].agg(np.mean),
    group['Ball_Control'].agg(np.mean),
    group['Marking'].agg(np.mean),
    group['Attacking_Position'].agg(np.mean),
    group['Vision'].agg(np.mean),
    group['Acceleration'].agg(np.mean),
    group['Strength'].agg(np.mean),
    group['Balance'].agg(np.mean),
    group['Agility'].agg(np.mean),
    group['Heading'].agg(np.mean)]
    h.insert(i,np.mean(g))
    i=i+1

x = list(range(160))
pl.xticks(x, xTicks)
pl.xticks(range(160), xTicks,rotation=90)
pl.title('best goal')
pl.xlabel('Teams')
pl.ylabel('Attributes')
pl.plot(x,h,'*',color='red')
plt.grid()
pl.show()


# question first finishes


# -> question second

i=0;
m=['0']
del m[0]
for key,value in k:
	aggression=[value['Aggression'].agg(np.mean)]
	m.insert(i,aggression)
	i+=1

pl.xticks(x, xTicks)
pl.xticks(range(160), xTicks,rotation=45)
pl.title('Aggression')
pl.xlabel('Teams')
pl.ylabel('Attributes')
pl.plot(x,m,'*',color='blue')
plt.grid()
pl.show()


# question second finishes



# -> question third

africa = ['Algeria','Guinea Bissau','São Tomé & Príncipe','Guinea Bissau ','DR Congo','Central African Rep.','Angola','Benin','Botswana',
              'Burkina Faso','Burundi','Cameroon','Cape Verde','Central African Republic','Chad','Comoros','Congo','Congo Democratic Republic of',
              'Djibouti','Egypt','Equatorial Guinea','Eritrea','Ethiopia','Gabon','Gambia','Ghana','Guinea','Guinea-Bissau','Ivory Coast','Kenya',
              'Lesotho','Liberia','Libya','Madagascar','Malawi','Mali','Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger','Nigeria',
              'Rwanda','Sao Tome and Principe','Senegal','Seychelles','Sierra Leone','Somalia','South Africa','South Sudan','Sudan','Swaziland',
              'Tanzania','Togo','Tunisia','Uganda','Zambia','Zimbabwe','Burkina Faso']
asia = ['Afghanistan','China PR','Korea Republic','Palestine','Korea DPR','Timor-Leste','Chinese Taipei','Bahrain','Armenia','Bangladesh',
            'Azerbaijan','Bhutan','Brunei','Burma (Myanmar)','Cambodia','China','East Timor','India','Indonesia','Iran','Iraq','Israel','Japan',
            'Jordan','Georgia','Kazakhstan','North Korea','South Korea','Kuwait','Kyrgyzstan','Laos','Lebanon','Malaysia','Maldives','Mongolia',
            'Nepal','Oman','Pakistan','Philippines','Qatar','Russian Federation','Saudi Arabia','Singapore','Sri Lanka','Syria','Tajikistan',
            'Thailand','Turkey','Turkmenistan','United Arab Emirates','Uzbekistan','Vietnam','Yemen']
europe =  ['Albania','FYR Macedonia','Faroe Islands','Serbia','Gibraltar','Kosovo','Bosnia Herzegovina','Andorra','Scotland','Austria','Belarus',
              'Belgium','Bosnia and Herzegovina','Bulgaria','Croatia','Cyprus','Czech Republic','Denmark','Estonia','Finland','France','Germany',
              'Greece','Hungary','Iceland','Republic of Ireland','Italy','Latvia','Liechtenstein','Northern Ireland','Lithuania','Luxembourg',
              'Macedonia','Malta','Moldova','Monaco','Montenegro','Netherlands','Norway','Poland','Portugal','Romania','Russia','San Marino','Serbi',
              'Slovakia','Slovenia','Spain','Sweden','Switzerland','Ukraine','England','Vatican City','Republic of Ireland','Wales']
north_america = ['Antigua and Barbuda','Puerto Rico','St Lucia','Antigua & Barbuda','Montserrat','Bermuda','St Kitts Nevis','Bahamas','Barbados',
                 'Belize','Canada','Costa Rica','Cuba','Dominica','Dominican Republic','El Salvador','Grenada','Guatemala','Haiti','Honduras',
                 'Jamaica','Mexico','Nicaragua','Panama','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Trinidad and Tobago',
                 'United States']
australia = ['Australia','FIFA16_NationName_215','Guam','Fiji','Kiribati','Marshall Islands','Micronesia','Nauru','New Zealand','Palau',
             'Papua New Guinea','Samoa','Solomon Islands','Tonga','Tuvalu','Vanuatu']
south_america =['Argentina','Curacao','Trinidad & Tobago','Aruba','Bolivia','Brazil','Chile','Colombia','Ecuador','Guyana','Paraguay','Peru',
                'Suriname','Uruguay','Venezuela']

nationality=data['Nationality'].tolist()
continent=[]
i=0
while i<17588:
    if nationality[i] in africa:
        continent.insert(i,'africa')
    elif nationality[i] in asia:
        continent.insert(i,'asia')
    elif nationality[i] in europe:
        continent.insert(i,'europe')
    elif nationality[i] in north_america:
        continent.insert(i,'north_america')
    elif nationality[i] in australia:
        continent.insert(i,'australia')
    elif nationality[i] in south_america:
        continent.insert(i,'south_america')
    i=i+1


se = pd.Series(continent)
data['Continent'] = se.values

#continentInput=input("Enter the continent")


manish=data.set_index('Continent')
rai=manish.loc['asia']


continentpreferedvalues= { 'Ball_Control'       : rai['Ball_Control'].agg(np.mean),                 #Picking the attributes for continent asia
                           'Dribbling'          : rai['Dribbling'].agg(np.mean),
                           'Dribbling'          : rai['Dribbling'].agg(np.mean),
                           'Marking'            : rai['Marking'].agg(np.mean),
                           'Sliding_Tackle'     : rai['Sliding_Tackle'].agg(np.mean),
                           'Standing_Tackle'    : rai['Standing_Tackle'].agg(np.mean),
                           'Aggression'         : rai['Aggression'].agg(np.mean),
                           'Reactions'          : rai['Reactions'].agg(np.mean),
                           'Attacking_Position' : rai['Attacking_Position'].agg(np.mean),
                           'Interceptions'      : rai['Interceptions'].agg(np.mean),
                           'Vision'             : rai['Vision'].agg(np.mean),
                           'Composure'          : rai['Composure'].agg(np.mean),
                           'Crossing'           : rai['Crossing'].agg(np.mean),
                           #'Short_Pass'         : rai['Short_Pass'].agg(np.mean),
                           #'Long_Pass'          : rai['Long_Pass'].agg(np.mean),
                           #'Acceleration'       : rai['Acceleration'].agg(np.mean),
                           #'Speed'              : rai['Speed'].agg(np.mean),
                           #'Stamina'            : rai['Stamina'].agg(np.mean),
                           #'Strength'           : rai['Strength'].agg(np.mean),
                           #'Balance'            : rai['Balance'].agg(np.mean),
                           'Agility'            : rai['Agility'].agg(np.mean),
                          # 'Jumping'            : rai['Jumping'].agg(np.mean),
                           'Heading'            : rai['Heading'].agg(np.mean),
                           'Shot_Power'         : rai['Shot_Power'].agg(np.mean),
                           'Finishing'          : rai['Finishing'].agg(np.mean),
                           'Long_Shots'         : rai['Long_Shots'].agg(np.mean),
                           'Curve'              : rai['Curve'].agg(np.mean),
                           'Freekick_Accuracy'  : rai['Freekick_Accuracy'].agg(np.mean),
                           'Penalties'          : rai['Penalties'].agg(np.mean),
                           'Volleys'            : rai['Volleys'].agg(np.mean)}

sorted_attributes = sorted(continentpreferedvalues.items(), key=operator.itemgetter(1),reverse=True)
key=[cs[0] for cs in sorted_attributes]
value=[cs[1] for cs in sorted_attributes]
asia_attributes=key[0]
asia_max=value[0]




manish=data.set_index('Continent')
rai=manish.loc['europe']


continentpreferedvalues= { 'Ball_Control'       : rai['Ball_Control'].agg(np.mean),             #Picking the attributes for continent europe
                           'Dribbling'          : rai['Dribbling'].agg(np.mean),
                           'Marking'            : rai['Marking'].agg(np.mean),
                           'Sliding_Tackle'     : rai['Sliding_Tackle'].agg(np.mean),
                           'Standing_Tackle'    : rai['Standing_Tackle'].agg(np.mean),
                           'Aggression'         : rai['Aggression'].agg(np.mean),
                           'Reactions'          : rai['Reactions'].agg(np.mean),
                           'Attacking_Position' : rai['Attacking_Position'].agg(np.mean),
                           'Interceptions'      : rai['Interceptions'].agg(np.mean),
                           'Vision'             : rai['Vision'].agg(np.mean),
                           'Composure'          : rai['Composure'].agg(np.mean),
                           'Crossing'           : rai['Crossing'].agg(np.mean),
                           #'Short_Pass'         : rai['Short_Pass'].agg(np.mean),
                           #'Long_Pass'          : rai['Long_Pass'].agg(np.mean),
                           #'Acceleration'       : rai['Acceleration'].agg(np.mean),
                           #'Speed'              : rai['Speed'].agg(np.mean),
                           #'Stamina'            : rai['Stamina'].agg(np.mean),
                           #'Strength'           : rai['Strength'].agg(np.mean),
                           #'Balance'            : rai['Balance'].agg(np.mean),
                          # 'Agility'            : rai['Agility'].agg(np.mean),
                           #'Jumping'            : rai['Jumping'].agg(np.mean),
                           'Heading'            : rai['Heading'].agg(np.mean),
                           'Shot_Power'         : rai['Shot_Power'].agg(np.mean),
                           'Finishing'          : rai['Finishing'].agg(np.mean),
                           'Long_Shots'         : rai['Long_Shots'].agg(np.mean),
                           'Curve'              : rai['Curve'].agg(np.mean),
                           'Freekick_Accuracy'  : rai['Freekick_Accuracy'].agg(np.mean),
                           'Penalties'          : rai['Penalties'].agg(np.mean),
                           'Volleys'            : rai['Volleys'].agg(np.mean)}

sorted_attributes = sorted(continentpreferedvalues.items(), key=operator.itemgetter(1),reverse=True)
key=[cs[0] for cs in sorted_attributes]
value=[cs[1] for cs in sorted_attributes]
europe_attributes=key[0]
europe_max=value[0]



manish=data.set_index('Continent')
rai=manish.loc['africa']


continentpreferedvalues= { 'Ball_Control'       : rai['Ball_Control'].agg(np.mean),                     #Picking the attributes for continent africa
                           'Dribbling'          : rai['Dribbling'].agg(np.mean),
                           'Marking'            : rai['Marking'].agg(np.mean),
                           'Sliding_Tackle'     : rai['Sliding_Tackle'].agg(np.mean),
                           'Standing_Tackle'    : rai['Standing_Tackle'].agg(np.mean),
                           'Aggression'         : rai['Aggression'].agg(np.mean),
                           #'Reactions'          : rai['Reactions'].agg(np.mean),
                           'Attacking_Position' : rai['Attacking_Position'].agg(np.mean),
                           'Interceptions'      : rai['Interceptions'].agg(np.mean),
                           'Vision'             : rai['Vision'].agg(np.mean),
                           'Composure'          : rai['Composure'].agg(np.mean),
                           'Crossing'           : rai['Crossing'].agg(np.mean),
                           #'Short_Pass'         : rai['Short_Pass'].agg(np.mean),
                          # 'Long_Pass'          : rai['Long_Pass'].agg(np.mean),
                           'Acceleration'       : rai['Acceleration'].agg(np.mean),
                          # 'Speed'              : rai['Speed'].agg(np.mean),
                           #'Stamina'            : rai['Stamina'].agg(np.mean),
                           #'Strength'           : rai['Strength'].agg(np.mean),
                           #'Balance'            : rai['Balance'].agg(np.mean),
                           #'Agility'            : rai['Agility'].agg(np.mean),
                           #'Jumping'            : rai['Jumping'].agg(np.mean),
                           'Heading'            : rai['Heading'].agg(np.mean),
                           'Shot_Power'         : rai['Shot_Power'].agg(np.mean),
                           'Finishing'          : rai['Finishing'].agg(np.mean),
                           'Long_Shots'         : rai['Long_Shots'].agg(np.mean),
                           'Curve'              : rai['Curve'].agg(np.mean),
                           'Freekick_Accuracy'  : rai['Freekick_Accuracy'].agg(np.mean),
                           'Penalties'          : rai['Penalties'].agg(np.mean),
                           'Volleys'            : rai['Volleys'].agg(np.mean)}

sorted_attributes = sorted(continentpreferedvalues.items(), key=operator.itemgetter(1),reverse=True)
key=[cs[0] for cs in sorted_attributes]
value=[cs[1] for cs in sorted_attributes]
africa_attributes=key[0]
africa_max=value[0]


manish=data.set_index('Continent')
rai=manish.loc['north_america']


continentpreferedvalues= { 'Ball_Control'       : rai['Ball_Control'].agg(np.mean),                 #Picking the attributes for continent north_america
                           'Dribbling'          : rai['Dribbling'].agg(np.mean),
                           'Marking'            : rai['Marking'].agg(np.mean),
                           'Sliding_Tackle'     : rai['Sliding_Tackle'].agg(np.mean),
                           'Standing_Tackle'    : rai['Standing_Tackle'].agg(np.mean),
                           'Aggression'         : rai['Aggression'].agg(np.mean),
                           'Reactions'          : rai['Reactions'].agg(np.mean),
                           'Attacking_Position' : rai['Attacking_Position'].agg(np.mean),
                           'Interceptions'      : rai['Interceptions'].agg(np.mean),
                           'Vision'             : rai['Vision'].agg(np.mean),
                           'Composure'          : rai['Composure'].agg(np.mean),
                           'Crossing'           : rai['Crossing'].agg(np.mean),
                           #'Short_Pass'         : rai['Short_Pass'].agg(np.mean),
                           #'Long_Pass'          : rai['Long_Pass'].agg(np.mean),
                           #'Acceleration'       : rai['Acceleration'].agg(np.mean),
                           'Speed'              : rai['Speed'].agg(np.mean),
                           #'Stamina'            : rai['Stamina'].agg(np.mean),
                           #'Strength'           : rai['Strength'].agg(np.mean),
                           #'Balance'            : rai['Balance'].agg(np.mean),
                          # 'Agility'            : rai['Agility'].agg(np.mean),
                           #'Jumping'            : rai['Jumping'].agg(np.mean),
                           'Heading'            : rai['Heading'].agg(np.mean),
                           'Shot_Power'         : rai['Shot_Power'].agg(np.mean),
                           'Finishing'          : rai['Finishing'].agg(np.mean),
                           'Long_Shots'         : rai['Long_Shots'].agg(np.mean),
                           'Curve'              : rai['Curve'].agg(np.mean),
                           'Freekick_Accuracy'  : rai['Freekick_Accuracy'].agg(np.mean),
                           'Penalties'          : rai['Penalties'].agg(np.mean),
                           'Volleys'            : rai['Volleys'].agg(np.mean)}

sorted_attributes = sorted(continentpreferedvalues.items(), key=operator.itemgetter(1),reverse=True)
key=[cs[0] for cs in sorted_attributes]
value=[cs[1] for cs in sorted_attributes]
north_america_attributes=key[0]
north_america_max=value[0]



manish=data.set_index('Continent')
rai=manish.loc['australia']


continentpreferedvalues= { 'Ball_Control'       : rai['Ball_Control'].agg(np.mean),                 #Picking the attributes for continent australia
                           'Dribbling'          : rai['Dribbling'].agg(np.mean),
                           'Marking'            : rai['Marking'].agg(np.mean),
                           'Sliding_Tackle'     : rai['Sliding_Tackle'].agg(np.mean),
                           'Standing_Tackle'    : rai['Standing_Tackle'].agg(np.mean),
                           'Aggression'         : rai['Aggression'].agg(np.mean),
                           #'Reactions'          : rai['Reactions'].agg(np.mean),
                           'Attacking_Position' : rai['Attacking_Position'].agg(np.mean),
                           'Interceptions'      : rai['Interceptions'].agg(np.mean),
                           #'Vision'             : rai['Vision'].agg(np.mean),
                           'Composure'          : rai['Composure'].agg(np.mean),
                           'Crossing'           : rai['Crossing'].agg(np.mean),
                           #'Short_Pass'         : rai['Short_Pass'].agg(np.mean),
                           #'Long_Pass'          : rai['Long_Pass'].agg(np.mean),
                          # 'Acceleration'       : rai['Acceleration'].agg(np.mean),
                           #'Speed'              : rai['Speed'].agg(np.mean),
                           #'Stamina'            : rai['Stamina'].agg(np.mean),
                           #'Strength'           : rai['Strength'].agg(np.mean),
                           #'Balance'            : rai['Balance'].agg(np.mean),
                          # 'Agility'            : rai['Agility'].agg(np.mean),
                           #'Jumping'            : rai['Jumping'].agg(np.mean),
                           #'Heading'            : rai['Heading'].agg(np.mean),
                           #'Shot_Power'         : rai['Shot_Power'].agg(np.mean),
                           'Finishing'          : rai['Finishing'].agg(np.mean),
                           #'Long_Shots'         : rai['Long_Shots'].agg(np.mean),
                           #'Curve'              : rai['Curve'].agg(np.mean),
                           'Freekick_Accuracy'  : rai['Freekick_Accuracy'].agg(np.mean),
                           'Penalties'          : rai['Penalties'].agg(np.mean),
                           'Volleys'            : rai['Volleys'].agg(np.mean)}

sorted_attributes = sorted(continentpreferedvalues.items(), key=operator.itemgetter(1),reverse=True)
key=[cs[0] for cs in sorted_attributes]
value=[cs[1] for cs in sorted_attributes]
australia_attributes=key[0]
australia_max=value[0]



manish=data.set_index('Continent')
rai=manish.loc['south_america']


continentpreferedvalues= { 'Ball_Control'       : rai['Ball_Control'].agg(np.mean),               #Picking the attributes for continent South America
                           'Dribbling'          : rai['Dribbling'].agg(np.mean),
                           'Marking'            : rai['Marking'].agg(np.mean),
                           'Sliding_Tackle'     : rai['Sliding_Tackle'].agg(np.mean),
                           'Standing_Tackle'    : rai['Standing_Tackle'].agg(np.mean),
                           'Aggression'         : rai['Aggression'].agg(np.mean),
                           'Reactions'          : rai['Reactions'].agg(np.mean),
                           'Attacking_Position' : rai['Attacking_Position'].agg(np.mean),
                           'Interceptions'      : rai['Interceptions'].agg(np.mean),
                           #'Vision'             : rai['Vision'].agg(np.mean),
                           'Composure'          : rai['Composure'].agg(np.mean),
                           'Crossing'           : rai['Crossing'].agg(np.mean),
                           #'Short_Pass'         : rai['Short_Pass'].agg(np.mean),
                           #'Long_Pass'          : rai['Long_Pass'].agg(np.mean),
                           #'Acceleration'       : rai['Acceleration'].agg(np.mean),
                           #'Speed'              : rai['Speed'].agg(np.mean),
                          # 'Stamina'            : rai['Stamina'].agg(np.mean),
                           #'Strength'           : rai['Strength'].agg(np.mean),
                           #'Balance'            : rai['Balance'].agg(np.mean),
                          # 'Agility'            : rai['Agility'].agg(np.mean),
                           #'Jumping'            : rai['Jumping'].agg(np.mean),
                           'Heading'            : rai['Heading'].agg(np.mean),
                           'Shot_Power'         : rai['Shot_Power'].agg(np.mean),
                           'Finishing'          : rai['Finishing'].agg(np.mean),
                           'Long_Shots'         : rai['Long_Shots'].agg(np.mean),
                           'Curve'              : rai['Curve'].agg(np.mean),
                           'Freekick_Accuracy'  : rai['Freekick_Accuracy'].agg(np.mean),
                           'Penalties'          : rai['Penalties'].agg(np.mean),
                           'Volleys'            : rai['Volleys'].agg(np.mean)}

sorted_attributes = sorted(continentpreferedvalues.items(), key=operator.itemgetter(1),reverse=True)
key=[cs[0] for cs in sorted_attributes]
value=[cs[1] for cs in sorted_attributes]
south_america_attributes=key[0]
south_america_max=value[0]


Continent_wise_atttribute=[asia_attributes+'\nContinent - Asia',
                           europe_attributes+'\nContinent - europe',
                           africa_attributes+'\nContinent - Africa',
                           north_america_attributes+'\nContinent - North_America'
                           ,australia_attributes+'\nContinent - Australia',
                           south_america_attributes+'\nContinent - South_America']


max_attribute=[asia_max,europe_max,africa_max,north_america_max,australia_max,south_america_max]

'''
i=0
while i<5:
    Continent_name.insert(i,key[i])
    best_attributes.insert(i,value[i])
    i=i+1                                                             #for pie chart
plt.pie(best_attributes, labels=Continent_name,
                autopct='%1.1f%%', shadow=True, startangle=90)
'''

name_continent=['Asia','Europe','Africa','North_America','Australia','South_America',]
rg=list(range(6))
pl.xticks(rg, Continent_wise_atttribute)
pl.xticks(range(6),Continent_wise_atttribute)
pl.title('Best attributes of the players of a particular continents')
pl.xlabel('Continent_wise_atttribute ->')
pl.ylabel('max_attribute ->')
pl.bar(rg,max_attribute,color=['red','blue','green','black','cyan','magenta'])     #Ploting The Graph
pl.show()



# question Third finishes

# -> question fourth




clubInput=input("Enter the club")
varun=data.set_index('Club')
gupta=varun.loc[clubInput]


clubPreferredAttributes= { 'Ball_Control'       : gupta['Ball_Control'].agg(np.mean),
                           'Dribbling'          : gupta['Dribbling'].agg(np.mean),
                           'Marking'            : gupta['Marking'].agg(np.mean),
                           'Sliding_Tackle'     : gupta['Sliding_Tackle'].agg(np.mean),
                           'Standing_Tackle'    : gupta['Standing_Tackle'].agg(np.mean),
                           'Aggression'         : gupta['Aggression'].agg(np.mean),
                           'Reactions'          : gupta['Reactions'].agg(np.mean),
                           'Attacking_Position' : gupta['Attacking_Position'].agg(np.mean),
                           'Interceptions'      : gupta['Interceptions'].agg(np.mean),
                           'Vision'             : gupta['Vision'].agg(np.mean),
                           'Composure'          : gupta['Composure'].agg(np.mean),
                           'Crossing'           : gupta['Crossing'].agg(np.mean),
                           'Short_Pass'         : gupta['Short_Pass'].agg(np.mean),
                           'Long_Pass'          : gupta['Long_Pass'].agg(np.mean),
                           'Acceleration'       : gupta['Acceleration'].agg(np.mean),
                           'Speed'              : gupta['Speed'].agg(np.mean),
                           'Stamina'            : gupta['Stamina'].agg(np.mean),
                           'Strength'           : gupta['Strength'].agg(np.mean),
                           'Balance'            : gupta['Balance'].agg(np.mean),
                           'Agility'            : gupta['Agility'].agg(np.mean),
                           'Jumping'            : gupta['Jumping'].agg(np.mean),
                           'Heading'            : gupta['Heading'].agg(np.mean),
                           'Shot_Power'         : gupta['Shot_Power'].agg(np.mean),
                           'Finishing'          : gupta['Finishing'].agg(np.mean),
                           'Long_Shots'         : gupta['Long_Shots'].agg(np.mean),
                           'Curve'              : gupta['Curve'].agg(np.mean),
                           'Freekick_Accuracy'  : gupta['Freekick_Accuracy'].agg(np.mean),
                           'Penalties'          : gupta['Penalties'].agg(np.mean),
                           'Volleys'            : gupta['Volleys'].agg(np.mean)}


sorted_d = sorted(clubPreferredAttributes.items(), key=operator.itemgetter(1),reverse=True)



key1=[]
key1=[x[0] for x in sorted_d]
value1=[]
value1=[x[1] for x in sorted_d]
key2=[]
value2=[]
i=0
while i<5:
    key2.insert(i,key1[i])
    value2.insert(i,value1[i])
    i=i+1


plt.pie(value2, labels=key2,
                autopct='%1.1f%%', shadow=True, startangle=90)


plt.show()

# question fourth finishes

# -> question fifth



i=0
name = data['Name'].tolist()

clubJoining=data['Club_Joining'].tolist()
contractExpiry=data['Contract_Expiry'].tolist()
joiningYear=['1']
del joiningYear[0]
s=['a']
del s[0]
while i<100:
    c=clubJoining[i]
    c=c[-4:]
    joiningYear.insert(i,c);
    joiningYear[i]=float(joiningYear[i])
    joiningYear[i]=contractExpiry[i]-joiningYear[i]
    s.insert(i,name[i])
    i=i+1


rg=list(range(100))
pl.xticks(rg, s)
pl.xticks(range(100), s,rotation=90)
pl.title('Contract Period')
pl.xlabel('Player')
pl.ylabel('Duration')
pl.plot(rg,joiningYear,'*',color='blue')
plt.grid()
pl.show()

# question fifth finishes




#question sixth
gkPositioning=data['GK_Positioning'].tolist()
gkDiving=data['GK_Diving'].tolist()
gkKicking=data['GK_Kicking'].tolist()
gkHandling=data['GK_Handling'].tolist()
gkReflexes=data['GK_Reflexes'].tolist()
playerGoalKepperSkills=[]
i=0
while i<17588:
    sumOfGoalKeeperSkills=gkPositioning[i]+gkDiving[i]+gkKicking[i]+gkHandling[i]+gkReflexes[i]
    playerGoalKepperSkills.insert(i,sumOfGoalKeeperSkills)
    sumOfGoalKeeperSkills=0
    i=i+1

#print(playerGoalKepperSkills[0])
goalSkillsSumSeries = pd.Series(playerGoalKepperSkills)
data['Goal_Skills_Sum'] = goalSkillsSumSeries.values
teamsNames=[]
teamGoalKeeperSkills=[]
i=0
for va,gu in k:
    teamsNames.insert(i,va)
    groups=gu['Goal_Skills_Sum']
    teamGoalKeeperSkills.insert(i,groups)
    i=i+1;
maxGoalSkills=[]
i=0
while i<160:
    maxPlayer=max(teamGoalKeeperSkills[i])
    maxGoalSkills.insert(i,maxPlayer)
    i=i+1

#dictionary = dict(zip(teamsNames, maxGoalSkills))
#sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1),reverse=True)



'''
i=0
while i<15:
    sortedGoalKey1.insert(i,sortedGoalKey[i])
    sortedGoalValue1.insert(i,sortedGoalValue[i])
    i=i+1


plt.pie(sortedGoalValue1, labels=sortedGoalKey1,
                autopct='%1.1f%%', shadow=True, startangle=90)


plt.show()
'''


xqw = list(range(160))
pl.xticks(xqw, teamsNames)
pl.xticks(range(160), xTicks,rotation=90)
pl.title('best goal keeper')
pl.xlabel('Teams')
pl.ylabel('Attributes')
pl.plot(x,maxGoalSkills,'*',color='red')
plt.grid()
pl.show()


#question sixth

#question seven



team_name = input('Enter the Team name')
kumar=data.set_index('Nationality')
rai=kumar.loc[team_name]

prakhar=rai['Preffered_Foot']
pra=prakhar.tolist()
pralen=len(pra)
i=0
left=0
right=0

while i<pralen:
    if pra[i] == 'Right':
        right=right+1
    else:
        left=left+1
    i=i+1

foot=['Left','Right']
foot_count_list=[left,right]
plt.pie(foot_count_list, labels=foot,
                autopct='%1.1f%%', shadow=True, startangle=90)


plt.show()
