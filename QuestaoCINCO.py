letra = input()


letra = letra.lower()

if (letra=='a' or letra=='b' or letra=='c' or letra=='d' or letra=='e' or letra=='f'
    or letra=='g' or letra=='h' or letra=='i' or letra=='j' or letra=='k' or letra=='l'
    or letra=='m' or letra=='n' or letra=='o' or letra=='p' or letra=='q' or letra=='r'
    or letra=='s' or letra=='t' or letra=='u' or letra=='v' or letra=='w' or letra=='x'
    or letra=='y' or letra=='z'):
    print(False)

elif (letra=='0' or letra=='1' or letra=='2' or letra=='3' or letra=='4' or letra=='5'
      or letra=='6' or letra=='7' or letra=='8' or letra=='9'):
    print(False)


else:
    print(True)
