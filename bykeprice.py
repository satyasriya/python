#write a program to check the on road price of a byke under the conditions:
#if the price is greater than 72,000 then income tax is 10% of 72,000 and insurance will be 15% of actual price
#if the price is greater than 1,50,000 and less than 2,00,000 taxwould be 25% and insurance will be 20% of actual price
#if price is above 2,00,000 tax is 35% and insurance will be 28%
#otherwise minimum price starts with 72,000 enter valid price
#print on road price actual price +tax+insurance


ap=int(input("enter actual price:"))
if ap>72000 and ap< 150000:
    it=(10/100)*ap
    ins=(15/100) *ap
    road_price =ap+it+ins
    print(int(road_price))
elif ap>150000 and ap< 200000:
    it=(25/100)*ap
    ins=(20/100) *ap
    road_price =ap+it+ins
    print(int(road_price))
elif ap>200000:
    it=(35/100)*ap
    ins=(28/100) *ap
    road_price =ap+it+ins
    print(int(road_price))
else:
    print("minimum price starts with 72,000 enter valid price")
