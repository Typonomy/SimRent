#Full Notes in SimRent Readme.txt

# Add a city budget.  Pay for subsidies by dividing the total among the tax brackets below, so like 30% among the wealthy and #10% paid amongst the lower and so on.  This changes the tax rate everybody pays.  Taxes go down if rents go down, but add #that mechanism later.

#Later add a tax for each person currently homeless, for services etc.  
#For each homeless person, add $100 taxes.
#Calculate realistic expenses for a homeless person each month - say like idk $50-100 supplies, a subroutine to gamble their 
#living arrangement(30 times: shelter=$0, motel=$60, couch=$0, hostel=$15, street=$0, car=$5, tent=$0)
#Above would be their personal expenses.

#When rents go down, the highest subsidy amounts are lowered to match it.  So save all subsidies applied in a list, so it
#saves them at their current "market rate", then if rents go down, go through that list and adjust it so the new lower rent is #the maximum.




import tkinter as tk
import pandas as pd
import csv
import numpy
import random


x=0

incomes=[]
totalpop=1000
grouplist=[]
ishomeless=[]
indivrent=[]
taxes=[]
taxrate=30 #Make tax brackets, figure out how to apply "classes" to these.
classisms=[]
balances=[]
unemployment_spans=[]
mon=0
yr=0
homelesscount=0
rounds_unemployed=0
unemployment=0
citybudget=0
subsidiestotalovertime=0#what is this supposed to be?
subsidytotalovertime=0#One of these needs to be a list of prices.
qualia=0
qualialist=[]



def getIncome():
    global totalpop
    global balances
    global classisms
    global incomes
    global group0
    global group1
    global group2
    global group3
    global group4
    global group5
    global grouplist
    global mon
    global yr
    global unemployment_spans
    global unemployment
    mon=1
    yr=1
#This section separates the total into income cohorts.
    group0=int(totalpop/(random.uniform(10,50)))
    group1=int(totalpop/(random.uniform(2,5)))
    group2=int(totalpop/(random.uniform(3,5)))
    group3=int(totalpop/(random.uniform(3,6)))
    group4=int(totalpop/(random.uniform(4,10)))
    groups=int(group0+group1+group2+group3+group4)
    if groups<totalpop:
        group5=int(totalpop-groups)
    else:
        group5=10
    grouplist.append(group0)
    grouplist.append(group1)
    grouplist.append(group2)
    grouplist.append(group3)
    grouplist.append(group4)
    grouplist.append(group5)

#This section assigns them each an income, a class of sorts, an unemployment status and so on.
    while group0>=0:
        incomes.append(random.randint(0, 10000))
        classisms.append("Hobo")
        group0=group0-1
        unemployment_spans.append(unemployment)
    while group1>=0: #This is the "pleb" income group
        incomes.append(random.randint(10000, 30000))
        classisms.append("Pleb")
        unemployment_spans.append(unemployment)
        group1=group1-1
    while group2>0:
        incomes.append(random.randint(30000, 70000))
        classisms.append("Blue Collar")
        unemployment_spans.append(unemployment)
        group2=group2-1
    while group3>0:
        incomes.append(random.randint(70000, 150000))
        classisms.append("Middle")
        unemployment_spans.append(unemployment)
        group3=group3-1
    while group4>0:
        incomes.append(random.randint(150000, 700000))
        classisms.append("Upper")
        unemployment_spans.append(unemployment)
        group4=group4-1
    while group5>0:
        incomes.append(random.randint(700000, 10000000))
        classisms.append("Rich")
        unemployment_spans.append(unemployment)
        group5=group5-1
    for inc in incomes:
        balances.append(inc)
    return incomes, classisms, balances, unemployment_spans, qualialist

#Method for the "Homeless Census" button, also gets unemployment rate.
def getIsHomeless():
    global homelesscount
    global ishomeless
    global indivrent
    for i in incomes:
        voteyes=0
        odds=0
        thevote=False
        if i<12000:
            odds=7
            voteyes=random.randint(1,10)
            if voteyes<=odds:
                thevote=False
            else:
                thevote=True
        elif i<35000:
            odds=1
            voteyes=random.randint(1,15)
            if voteyes>odds:
                thevote=False
            else:
                thevote=True
        else:
            odds=1
            voteyes=random.randint(1,100)
            if voteyes>odds:
                thevote=False
            else:
                thevote=True
                
        ishomeless.append(thevote)
        if thevote==True:
            homelesscount=homelesscount+1
            indivrent.append(int(0))
        elif thevote==False:
            indivrent.append(int(i/36))
    return ishomeless, indivrent

#Calculates the tax rate, this can become more complicated.
def getTaxes():
    global taxes
    global ishomeless
    taxadd=0
    for i in ishomeless:
        if ishomeless==True:
            taxadd=taxadd+100
    for i in incomes:
        if i < 12000:
            taxes.append(0)
        elif i<35000:
            thistax=(i/10)
            thisx=0
            for d in incomes:
                if ((d<35000) and (d>12000)):
                    thisx=thisx+1 #counts the tax bracket
            thistax=thistax+((taxadd/10)/thisx)
                
            taxes.append(thistax)
        elif i<150000:
            thistax=(i/3)
            thisx=0
            for d in incomes:
                if ((d>35000) and (d<150000)):
                    thisx=thisx+1 #counts the tax bracket
            thistax=thistax+((taxadd/10)/thisx)
            taxes.append(thistax)
        else:
            taxes.append(100000)
    #The above is the base starting tax rate.  Any services that are initially offered should go into this method.
    #Subsidies that get added in for health or shelter, or reductions, go into the update method.
    
    return taxes

#Method to get the city budget.
def getBudget():
    global subsidytotalovertime
    global citybudget
    taxadd=0
    for i in ishomeless:
        if ishomeless==True:
            taxadd=taxadd+100
    citybudget=citybudget-taxadd
    citybudget=(citybudget+((df['Taxes'].sum())/12))-subsidytotalovertime
    
    return int(citybudget)


#Define a hospital method.  Every turn, 10% of people with wellbeing below like 6 can go to the hospital and gain 2 health for 
#$1000.  If their balance is lower than twice their rent plus 1000, they don't go.  Everyone (at a rate of 20%) gains or loses 1-3 health at random intrevals of 1-24 turns.  

#"Health Subsidy" button will calculate the difference between 10 and each item in "wellbeing", then multiply that by 500.
#(Sprites can't buy 1 health.)  It applies that "price" to the number of individuals specified based on the number of points they #need, starting at the lowest income.  This amount gets removed from the budget and they're restored to full health.

#Assign "wellbeing" here.

def getQualia():
    global qualia
    global qualialist
    for i in incomes:
        thisindex=incomes.index(i)
        qualia=random.randint(1,10)
        if ishomeless[thisindex]==True:
            qualia=qualia-1
        elif balances[thisindex]>100000:
            qualia=qualia+1
        qualialist.append(qualia)
    return qualialist
        


getIncome()
getIsHomeless()
getTaxes()
getQualia()


df = pd.DataFrame({'col':incomes})
df.columns=['Incomes']
df['Class']=classisms
df['Is Homeless']=ishomeless
df['Taxes']=taxes
df['Rents']=indivrent
df['Balance']=balances
df['Wellbeing']=qualialist
citybudget=getBudget()
print (df)

print(df['Incomes'].describe().apply(lambda x: format(x, 'f')))
print(df['Rents'].describe().apply(lambda x: format(x, 'f')))
print(grouplist)
print("City Budget: {}".format(citybudget))
print("month {}, year {}".format(mon, yr))



def nextMonth():
    
    global mon
    global yr
    global balances
    global incomes
    global taxes
    global indivrent
    global ishomeless
    global classisms
    global rounds_unemployed
    global unemployment_spans
    global unemployment
    global citybudget
    if mon<12:
        mon=mon+1
    else:
        mon=1
        yr=yr+1
        #annual rent increases
        for i in indivrent:
            ind=indivrent.index(i)
            increase=((random.randint(10,25))/100)
            i=(i+(i*increase))
            indivrent[ind]=int(i)
    marketrent=int(df['Rents'].median())
    housingline=marketrent*5
    incomeline=marketrent*3
    for i in incomes:#Start - This block gives everyone a 5% chance of being fired for 1-6 rounds
        thisindex=incomes.index(i)
        turnsFired=random.randint(1,6)
        oddsFired=random.randint(1,200)
        if unemployment_spans[thisindex]>1:
            incomes[thisindex]=0
            unemployment_spans[thisindex]=(unemployment_spans[thisindex])-1
        elif unemployment_spans[thisindex]==1:
            unemployment_spans[thisindex]=(unemployment_spans[thisindex])-1
            incomes[thisindex]=random.randint(1000,10000000)            
        else:
            print("This")
        if oddsFired==1:
            incomes[thisindex]=0
            unemployment_spans[thisindex]=turnsFired
        else:
            print("This")  #End - this gives everyone a 5% chance of being fired for 1-6 rounds
        thisbal=balances[thisindex]
            #The following section checks to see if a homeless person has the resources to get a place on their own.
            #But it also excludes them if they have a lot of money because that indicates they're homeless for other reasons.
            #Subsidies aren't means tested in this.
        if ((ishomeless[thisindex]==True) and (thisbal<200000)):
            if ((i>incomeline) and (thisbal>housingline)):
                balances[thisindex]=thisbal-(marketrent*3)#Takes marketrent*4 from balance, the next loop takes the other 1x
                indivrent[thisindex]=marketrent #Set rent to market rate
                ishomeless[thisindex]=False #Set ishomeless to False
            

    #add some lines to save the stats of each turn and be able to look back through them.
    for i in balances:
        itemindex=balances.index(i)
        if i < indivrent[itemindex]:
            i=i+(incomes[itemindex]/12)
            i=i-(taxes[itemindex]/12)
            ishomeless[itemindex]=True
            #In this version so far, the rate of homelessness can only increase.
            indivrent[itemindex]=0
        else:
            i=i+(incomes[itemindex]/12)
            i=i-(indivrent[itemindex])
            i=i-(taxes[itemindex]/12)
            balances[itemindex]=int(i)

        if i<10000:
            classisms[itemindex]="Hobo"        
        elif i<30000:
            classisms[itemindex]="Pleb"
        elif i<70000:
            classisms[itemindex]="Blue Collar"
        elif i<150000:
            classisms[itemindex]="Middle"
        elif i<700000:
            classisms[itemindex]="Upper"
        else:
            classisms[itemindex]="Rich"
    getBudget()            
     #This subsidy variable should be a list
    #qualiaUpdate()
    #also make a function to change tax levels - taxes go up when homelessness goes up.
    df['Incomes']=incomes
    df['Class']=classisms  #Make it so they go up and down in class as well.
    df['Is Homeless']=ishomeless
    df['Taxes']=taxes
    df['Rents']=indivrent
    df['Balance']=balances
    df['Wellbeing']=qualialist
    print(df)
    print(df['Incomes'].describe().apply(lambda x: format(x, 'f')))
    print(df['Rents'].describe().apply(lambda x: format(x, 'f')))
    print("City Budget: {}".format(citybudget))
    print(grouplist)
    print("month {}, year {}".format(mon, yr))

def homelessCensus():
    global unemployment_spans
    global ishomeless
    global homelesscount
    homelesscount=0
    unemployment=0
    for i in ishomeless:
        if i==True:
            homelesscount=homelesscount+1
        else:
            continue
    for d in unemployment_spans:
        if d>0:
            unemployment=unemployment+1
    print("Homeless Count: {}".format(homelesscount))
    print("Unemployment: {}".format(unemployment))

def isSubsidy():
    global homelesscount
    global ishomeless
    global indivrent
    global incomes
    global subsidiestotalovertime
    global subsidytotalovertime
    global citybudget
    inp = numSubsidy.get()
    marketrent=int(df['Rents'].median())
    subsidiestotalovertime=subsidiestotalovertime+inp
    subsidyprice=inp*marketrent  #This has to be kept in a list to avoid recalculating the total-
#Use a list so that subsidies of earlier months stay the same price and people can be edged out by increases.
    subsidytotalovertime=subsidytotalovertime+subsidyprice
    if ((inp>homelesscount) or (subsidyprice>citybudget)):
        lbl.config(text = "Too Many") #Fix the text input width too.
    else:
        citybudget=getBudget()
        lbl.config(text = "OK!")        
        subsidyprice=inp*marketrent #Use this for the tax increase later
        for i in ishomeless:
            hindex=ishomeless.index(i)
            subincome=incomes[hindex]
            if i==True:
                if inp>0:
                    ishomeless[hindex]=False
                    indivrent[hindex]=marketrent
                    incomes[hindex]=subincome+marketrent
                    inp=inp-1
    return incomes, indivrent, ishomeless, subsidyprice, int(citybudget), subsidytotalovertime

def qualiaUpdate():#Qualia getter for 'next month' method.
    global qualialist
    for i in qualialist:
        thisindex=qualialist.index(i)
#        if ishomeless[thisindex]==True:
#            i=i-1
#        elif balances[thisindex]>100000:
#            i=i+1

        chance=random.randint(1,50)#Odds of a health incident is 2% over 1 month
        debuff=random.randint(1,3)
        if chance==1:
            i=i-debuff
        else:
            i=qualialist[thisindex]
            
        qualialist[thisindex]=i
    return qualialist


#def hospitalSubsidy():
#    global qualialist
#    global citybudget 
#    for i in qualialist:
#        thisindex=qualialist.index(i)
#Get input here
#        hospitalnumber=numHospital.get()
#        while hospitalnumber>0:
#            if i<10:
#                i=i+2 #Gives 2 health
#                citybudget=citybudget-1000 #Costs $1000
#            hospitalnumber=hospitalnumber-1
#        qualialist[thisindex]=i
#    print("City Budget: {}".format(int(citybudget)))
#    return qualialist, int(citybudget)
    

    
    
window=tk.Tk()
window.geometry("200x200")
numSubsidy=tk.IntVar()
#numHospital=tk.IntVar()
btn=tk.Button(window, text="Enter", fg='cyan', command=nextMonth)
subsidyinput = tk.Entry(window,textvariable = numSubsidy)
#hospitalinput = tk.Entry(window,textvariable = numHospital)#Hospital

btn2=tk.Button(window, text="Homeless Census", fg='cyan', command=homelessCensus)
btn3=tk.Button(window, text="Subsidize Rents", fg='cyan', command=isSubsidy)

#btn4=tk.Button(window, text="Hospital Subsidy", fg='cyan', command=hospitalSubsidy)#Hospital
btn.place(x=70, y=25)
btn2.place(x=36, y=155)
lbl = tk.Label(window, text = "How Many Subsidies?")
lbl.place(x=38, y=60)
subsidyinput.place(x=61, y=75, width=80)
#lblHosp = tk.Label(window, text = "How Many Get Healthcare?")#Hospital
#lblHosp.place(x=28, y=195)#Hospital
#hospitalinput.place(x=61, y=210, width=80)#Hospital
btn3.place(x=40, y=95)
#btn4.place(x=40, y=235) #Hospital




#with open('./TestIncomes1.csv', 'w') as q:
#    writer=csv.writer(q)
#    writer.writerow(incomes)

    
window.mainloop()

