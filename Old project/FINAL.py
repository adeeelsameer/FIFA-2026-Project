import time
import datetime
import webbrowser
import random
import os
import math
import smtplib
import os
import turtle
import csv

def booktickets():
    def groupstagematches():
        print("\n20/11/2022\n1.  Qatar VS Ecuador\n")
        print("21/11/2022\n2.  England VS Iran")
        print("3.  Senegal VS Netherlands")
        print("4.  USA VS Wales\n")
        print("22/11/2022\n5.  Argentina VS Saudi Arabia")
        print("6.  Mexico VS Poland")
        print("7.  Denmark VS Tunisia")
        print("8.  France VS Australia\n")
        print("23/11/2022\n9.  Morocco VS Croatia")
        print("10. Germany VS Japan")
        print("11. Spain VS Costa Rica")
        print("12. Belgium VS Canada\n")
        print("24/11/2022\n13. Brazil VS Serbia")
        print("14. Portugal VS Ghana")
        print("15. Uruguay VS Korea Republic")
        print("16. Switzerland VS Cameroon\n")
        print("25/11/2022\n17. England VS USA")
        print("18. Netherlands VS Ecuador")
        print("19. Qatar VS Senegal")
        print("20. Wales VS Iran\n")
        print("26/11/2022\n21. Argentina VS Mexico")
        print("22. France VS Denmark")
        print("23. Poland VS Saudi Arabia")
        print("24. Tunisia VS Australia\n")
        print("27/11/2022\n25. Spain VS Germany")
        print("26. Croatia VS Canada")
        print("27. Belgium VS Morocco")
        print("28. Japan VS Costa Rica\n")
        print("28/11/2022\n29. Portugal VS Uruguay")
        print("30. Brazil VS Switzerland")
        print("31. Korea Republic VS Ghana")
        print("32. Cameroon VS Serbia\n")
        print("29/11/2022\n33. Netherlands VS Qatar")
        print("34. Ecuador VS Senegal")
        print("35. Iran VS USA")
        print("36. Wales VS England\n")
        print("30/11/2022\n37. Saudi Arabia VS Mexico")
        print("38. Poland VS Argentina")
        print("39. Tunisia VS France")
        print("40. Australia VS Denmark\n")
        print("01/12/2022\n41. Costa Rica VS Germany")
        print("42. Japan VS Spain")
        print("43. Canada VS Morocco")
        print("44. Croatia VS Belgium\n")
        print("02/12/2022\n45. Cameroon VS Brazil")
        print("46. Serbia VS Switzerland")
        print("47. Korea Reupublic VS Portugal")
        print("48. Ghana VS Uruguay\n")
    def roundof16matches():
        print("\n03/12/2022\n1.  1A VS 2B   6:00 PM")
        print("2.  1C VS 2D   10:00 PM\n")
        print("04/12/2022\n3.  1D VS 2C   6:00 PM")
        print("4.  1B VS 2A   10:00 PM\n")
        print("05/12/2022\n5.  1E VS 2F   6:00 PM")
        print("6. 1G VS 2H    10:00 PM\n")
        print("24/11/2022\n7. 1F VS 2E   6:00 PM")
        print("8. 1H VS 2G   10:00 PM\n")
    def quarterfinalsmatches():
        print("\n09/12/2022\n1.  W53 VS W54   6:00 PM")
        print("2.  W49 VS W50   10:00 PM\n")
        print("10/12/2022\n3.  W55 VS W56   6:00 PM")
        print("4.  W51 VS W52   10:00 PM\n")
    def semifinalsmatches():
        print("\n13/12/2022\n1.  W57 VS W58   10:00 PM\n")
        print("04/12/2022\n2.  W59 VS W60   10:00 PM\n")
    def finalmatches():
        print("\n17/12/2022\n1.  3rd Place   6:00 PM\n")
        print("18/12/2022\n2.  Final   6:00 PM\n")
    def bill():        
        screen = turtle.Screen()
        pen = turtle.Turtle()
        screenwindow = screen.getcanvas().winfo_toplevel()
        screenwindow.call('wm', 'attributes', '.', '-topmost', '1')
        pen.hideturtle()
        pen.speed(100)
        pen.color('black')

        pen.penup()
        pen.goto(-200,300)
        pen.pendown()
        pen.pensize(5)
        pen.color('black')
        pen.forward(400)
        pen.right(90)
        pen.forward(600)
        pen.right(90)
        pen.forward(400)
        pen.right(90)
        pen.forward(600)
        pen.penup()
        pen.goto(-18,250)
        pen.pendown()
        text="BILL"
        pen.write(text, font=('Times New Roman', 15, 'bold'))
        pen.penup()
        pen.goto(-150,200)
        pen.pendown()
        x=-150
        y=200
        for i in lst:
            pen.write(i[0], font=('Times New Roman', 10))
            pen.penup()
            y-=20
            pen.goto(x,y)
            pen.pendown()
        pen.penup()
        pen.goto(100,200)
        pen.pendown()
        a=100
        b=200
        for i in lst:
            pen.write(i[1], font=('Times New Roman', 10))
            pen.penup()
            b-=20
            pen.goto(a,b)
            pen.pendown()
        pen.penup()
        pen.goto(83.5,b)
        pen.pendown()
        equalsto="========"
        pen.write(equalsto, font=('Times New Roman', 10))
        pen.penup()
        pen.goto(a,b-15)
        pen.pendown()
        pen.write(total, font=('Times New Roman', 10,'bold'))
        pen.penup()
        pen.goto(a-270,b-350)
        pen.pendown()
        pen.write(name, font=('Times New Roman', 10,'bold'))
        pen.penup()
        pen.goto(a-270,b-370)
        pen.pendown()
        pen.write(emailid, font=('Times New Roman', 10,'bold'))
        pen.penup()
        pen.goto(a-270,b-390)
        pen.pendown()
        pen.write("FIFA World Cup 2022 Qatar", font=('Times New Roman', 10,'bold'))
        turtle.mainloop()

    def payment():
        print("\n=====================PAYMENT=====================")
        digits = "0123456789"
        OTP = ""
        for i in range (6):
            OTP += digits[math.floor(random.randint(0,9))]
        otp = OTP + " is your OTP. Please do not share this OTP with anyone. Thanks."
        message = otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("fifaprojectkha@gmail.com", "dqgvslcmeaxrzydn")
        s.sendmail('&&&&&&',emailid,message)
        print("OTP sent to your email\n")
        a = input("Enter your OTP >>: ")
        if a == OTP:
            print("Verified")
            time.sleep(1.5)
            print("\nPlease Close the bill to continue")
            bill()
        else:
            print("Wrong OTP")
            print("\nNew OTP sent. Please Check your new OTP.")
            payment()
    def Booking():
        def book_morematches():
            more_matches=input("\nDo you want to book more matches?(y/n) ")
            invalid222=["y","n"]
            while more_matches.lower() not in invalid222:
                print("\nInvalid input. Please type y or n")
                book_morematches()
            if more_matches.lower()=="y":
                Booking()
            elif more_matches.lower()=="n":
                print("\nYour total is: ",total)
                print("\nProceeding to Payment...")
                payment()
                print("\nPAYMENT COMPLETE\n")
                backhome_9 = input("Do you wish to continue, yes or no : \n")
                backhome_9 =backhome_9.lstrip().rstrip()
                list_backhome_9 = ["yes", "no"]
                while backhome_9 not in list_backhome_9:
                    print("\nInvalid input. Please type yes or no . \n")
                    backhome_9 = input("Do you wish to continue, yes or no :  \n")
                    backhome_9 =backhome_9.lstrip().rstrip()
                if backhome_9.lower() == "yes":
                    home()
                if backhome_9.lower() == "no":
                    quitting()
        def cat_separation():
            global total
            with open('FIFA.csv',"r") as csvfile:
                myreader=csv.reader(csvfile,delimiter=',')
                print("%10s"%"Category","%20s"%"Price")
                print("="*35)
                for row in myreader:
                    print("%11s"%row[0],"%20s"%row[1])
            cat=input("\nWhich category do you want? (1,2,3,4) ")
            invalid3=["1","2","3","4"]
            while cat not in invalid3:
                print("\nInvalid input. Please type 1,2,3 or 4 . \n")
                cat_separation()
            if cat=="1":
                p1=["Group Stage Match - Category 1",800]
                lst.append(p1)
                total+=800
                book_morematches()
            if cat=="2":
                p2=["Group Stage Match - Category 2",600]
                lst.append(p2)
                total+=600
                book_morematches()
            if cat=="3":
                p3=["Group Stage Match - Category 3",250]
                lst.append(p3)
                total+=250
                book_morematches()
            if cat=="4":
                p4=["Group Stage Match - Category 4",40]
                lst.append(p4)
                total+=40
                book_morematches()
        def r16_separation():
            global total
            with open('FIFA.csv',"r") as csvfile:
                myreader=csv.reader(csvfile,delimiter=',')
                print("%10s"%"Category","%20s"%"Price")
                print("="*35)
                for row in myreader:
                    print("%11s"%row[2],"%20s"%row[3])
            cat1=input("\nWhich category do you want? (1,2,3,4) ")
            invalid=["1","2","3","4"]
            while cat1 not in invalid:
                print("\nInvalid input. Please type 1,2,3 or 4 . \n")
                r16_separation()
            if cat1=="1":
                p5=["Round of 16 Match - Category 1",1000]
                lst.append(p5)
                total+=1000
                book_morematches()
            if cat1=="2":
                p6=["Round of 16 Match - Category 2",750]
                lst.append(p6)
                total+=750
                book_morematches()
            if cat1=="3":
                p7=["Round of 16 Match - Category 3",350]
                lst.append(p7)
                total+=350
                book_morematches()
            if cat1=="4":
                p8=["Round of 16 Match - Category 4",70]
                lst.append(p8)
                total+=70
                book_morematches()
        def qf_separation():
            global total
            with open('FIFA.csv',"r") as csvfile:
                myreader=csv.reader(csvfile,delimiter=',')
                print("%10s"%"Category","%20s"%"Price")
                print("="*35)
                for row in myreader:
                    print("%11s"%row[4],"%20s"%row[5])
            invalid1=["1","2","3","4"]
            cat2=input("\nWhich category do you want? (1,2,3,4) ")
            while cat2 not in invalid1:
                print("\nInvalid input. Please type 1,2,3 or 4 . \n")
                qf_separation()
            if cat2=="1":
                p9=["Quarter Final Match - Category 1",1550]
                lst.append(p9)
                total+=1550
                book_morematches()
            if cat2=="2":
                p10=["Quarter Final Match - Category 2",1050]
                lst.append(p10)
                total+=1050
                book_morematches()
            if cat2=="3":
                p11=["Quarter Final Match - Category 3",750]
                lst.append(p11)
                total+=750
                book_morematches()
            if cat2=="4":
                p12=["Quarter Final Match - Category 4",300]
                lst.append(p12)
                total+=300
                book_morematches()
        def sf_separation():
            global total
            with open('FIFA.csv',"r") as csvfile:
                myreader=csv.reader(csvfile,delimiter=',')
                print("%10s"%"Category","%20s"%"Price")
                print("="*35)
                for row in myreader:
                    print("%11s"%row[6],"%20s"%row[7])
            invalid2=["1","2","3","4"]
            cat3=input("\nWhich category do you want? (1,2,3,4) ")
            while cat3 not in invalid2:
                print("\nInvalid input. Please type 1,2,3 or 4 . \n")
                sf_separation()
            if cat3=="1":
                p13=["Semi Final Match - Category 1",3480]
                lst.append(p13)
                total+=3480
                book_morematches()
            if cat3=="2":
                p14=["Semi Final Match - Category 2",2400]
                lst.append(p14)
                total+=2400
                book_morematches()
            if cat3=="3":
                p15=["Semi Final Match - Category 3",1300]
                lst.append(p15)
                total+=1300
                book_morematches()
            if cat3=="4":
                p16=["Semi Final Match - Category 4",500]
                lst.append(p16)
                total+=500
                book_morematches()
        def fl_separation():
            global total
            with open('FIFA.csv',"r") as csvfile:
                myreader=csv.reader(csvfile,delimiter=',')
                print("%10s"%"Category","%20s"%"Price")
                print("="*35)
                for row in myreader:
                    print("%11s"%row[8],"%20s"%row[9])
            cat4=input("\nWhich category do you want? (1,2,3,4) ")
            invalid4=["1","2","3","4"]
            while cat4 not in invalid4:
                print("\nInvalid input. Please type 1,2,3 or 4 . \n")
                fl_separation()
            if cat4=="1":
                p17=["Third Place Match - Category 1",1550]
                lst.append(p17)
                total+=1550
                book_morematches()
            if cat4=="2":
                p18=["Third Place Match - Category 2",1100]
                lst.append(p18)
                total+=1100
                book_morematches()
            if cat4=="3":
                p19=["Third Place Match - Category 3",750]
                lst.append(p19)
                total+=750
                book_morematches()
            if cat4=="4":
                p20=["Third Place Match - Category 4",300]
                lst.append(p20)
                total+=300
                book_morematches()
        def f_separation():
            global total
            with open('FIFA.csv',"r") as csvfile:
                myreader=csv.reader(csvfile,delimiter=',')
                print("%10s"%"Category","%20s"%"Price")
                print("="*35)
                for row in myreader:
                    print("%11s"%row[10],"%20s"%row[11])
            cat5=input("\nWhich category do you want? (1,2,3,4) ")
            invalid4=["1","2","3","4"]
            while cat5 not in invalid4:
                print("\nInvalid input. Please type 1,2,3 or 4 . \n")
                f_separation()
            if cat5=="1":
                p21=["Third Place Match - Category 4",5850]
                lst.append(p21)
                total+=5850
                book_morematches()
            if cat5=="2":
                p22=["Third Place Match - Category 4",3650]
                lst.append(p22)
                total+=3650
                book_morematches()
            if cat5=="3":
                p23=["Third Place Match - Category 4",2200]
                lst.append(p23)
                total+=2200
                book_morematches()
            if cat5=="4":
                p24=["Third Place Match - Category 4",750]
                lst.append(p24)
                total+=750
                book_morematches()            
        global total
        print("\n----SELECT MATCH TYPE----")
        print(" 1. Group Stages")
        print(" 2. Round of 16")
        print(" 3. Quartar Finals")
        print(" 4. Semi-Finals")
        print(" 5. Finals")                
        ch=input("\nSelect which type of match you want(Type 1,2,3,4,5): ")
        invalid100=["1","2","3","4","5"]
        while ch not in invalid100:
            print("\nInvalid input. Please type 1,2,3,4,5.\n")
            ch=input("Select which type of match you want(Type 1,2,3,4,5): ")
        if ch=="1":
            print("\n","="*15,"GROUP STAGE","="*15)
            groupstagematches()
            choice=input('Type the match number you want (1,2,3,....,48): ')
            invalid10=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48"]
            while choice not in invalid10:
                print("\nInvalid input. Please type 1,2,3,....,48 . \n")
                choice=input("Type the match number you want (1,2,3,....,48): ")
            if choice=="1":
                print("\n----QATAR VS ECUADOR----\n")
                cat_separation()
            if choice=="2":
                print("\n----ENGLAND VS IRAN----\n")
                cat_separation()
            if choice=="3":
                print("\n----SENEGAL VS NETHERLANDS----\n")
                cat_separation()
            if choice=="4":
                print("\n----USA VS WALES----\n")
                cat_separation()
            if choice=="5":
                print("\n----ARGENTINA VS SAUDI ARABIA----\n")
                cat_separation()
            if choice=="6":
                print("\n----MEXICO VS POLAND----\n")
                cat_separation()
            if choice=="7":
                print("\n----DENMARK VS TUNISIA----\n")
                cat_separation()
            if choice=="8":
                print("\n----FRANCE VS AUSTRALIA----\n")
                cat_separation()
            if choice=="9":
                print("\n----MOROCCO VS CROATIA----\n")
                cat_separation()
            if choice=="10":
                print("\n----GERMANY VS JAPAN----\n")
                cat_separation()
            if choice=="11":
                print("\n----SPAIN VS COSTA RICA----\n")
                cat_separation()
            if choice=="12":
                print("\n----BELGIUM VS CANADA----\n")
                cat_separation()
            if choice=="13":
                print("\n----BRAZIL VS SERBIA----\n")
                cat_separation()
            if choice=="14":
                print("\n----PORTUGAL VS GHANA----\n")
                cat_separation()
            if choice=="15":
                print("\n----URUGUAY VS KOREA REPUBLIC----\n")
                cat_separation()
            if choice=="16":
                print("\n----SWITZERLAND VS CAMEROON----\n")
                cat_separation()
            if choice=="17":
                print("\n----ENGLAND VS USA----\n")
                cat_separation()
            if choice=="18":
                print("\n----NETHERLANDS VS ECUADOR----\n")
                cat_separation()
            if choice=="19":
                print("\n----QATAR VS SENEGAL----\n")
                cat_separation()
            if choice=="20":
                print("\n----WALES VS IRAN----\n")
                cat_separation()
            if choice=="21":
                print("\n----ARGENTINA VS MEXICO----\n")
                cat_separation()
            if choice=="22":
                print("\n----FRANCE VS DENMARK----\n")
                cat_separation()
            if choice=="23":
                print("\n----POLAND VS SAUDI ARABIA----\n")
                cat_separation()
            if choice=="24":
                print("\n----TUNISIA VS AUSTRALIA ----\n")
                cat_separation()
            if choice=="25":
                print("\n----SPAIN VS GERMANY----\n")
                cat_separation()
            if choice=="26":
                print("\n----CROATIA VS CANADA----\n")
                cat_separation()
            if choice=="27":
                print("\n----BELGIUM VS MOROCCO----\n")
                cat_separation()
            if choice=="28":
                print("\n----JAPAN VS COSTA RICA----\n")
                cat_separation()
            if choice=="29":
                print("\n----PORTUGAL VS URUGUAY----\n")
                cat_separation()
            if choice=="30":
                print("\n----BRAZIL VS SWITZERLAND----\n")
                cat_separation()
            if choice=="31":
                print("\n----KOREA REPUBLIC VS GHANA----\n")
                cat_separation()
            if choice=="32":
                print("\n----CAMEROON VS SERBIA----\n")
                cat_separation()
            if choice=="33":
                print("\n----NETHERLANDS VS QATAR----\n")
                cat_separation()
            if choice=="34":
                print("\n----ECUADOR VS SENEGAL----\n")
                cat_separation()
            if choice=="35":
                print("\n----IRAN VS USA----\n")
                cat_separation()
            if choice=="36":
                print("\n----WALES VS ENGLAND----\n")
                cat_separation()
            if choice=="37":
                print("\n----SAUDI ARABIA VS MEXICO----\n")
                cat_separation()
            if choice=="38":
                print("\n----POLAND VS ARGENTINA----\n")
                cat_separation()
            if choice=="39":
                print("\n----TUNISIA VS FRANCE----\n")
                cat_separation()
            if choice=="40":
                print("\n----AUSTRALIA VS DENMARK----\n")
                cat_separation()
            if choice=="41":
                print("\n----COSTA RICA VS GERMANY----\n")
                cat_separation()
            if choice=="42":
                print("\n----JAPAN VS SPAIN----\n")
                cat_separation()
            if choice=="43":
                print("\n----CANADA VS MOROCCO----\n")
                cat_separation()
            if choice=="44":
                print("\n----CROATIA VS BELGIUM----\n")
                cat_separation()
            if choice=="45":
                print("\n----CAMEROON VS BRAZIL----\n")
                cat_separation()
            if choice=="46":
                print("\n----SERBIA VS SWITZERLAND----\n")
                cat_separation()
            if choice=="47":
                print("\n----KOREA REUPUBLIC VS PORTUGAL----\n")
                cat_separation()
            if choice=="48":
                print("\n----GHANA VS URUGUAY----\n")
                cat_separation()

        if ch=="2":
            print("\n","="*15,"ROUND OF 16","="*15)
            roundof16matches()
            choice1=input('Type the match number you want (1,2,3,....,8): ')
            invalid11=["1","2","3","4","5","6","7","8"]
            while choice1 not in invalid11:
                print("\nInvalid input. Please type 1,2,3,....,8 . \n")
                choice1=input("Type the match number you want (1,2,3,....,8): ")
            if choice1=="1":
                print("\n-----------1A VS 2B-----------\n")
                r16_separation()
            if choice1=="2":
                print("\n-----------1C VS 2D-----------\n")
                r16_separation()
            if choice1=="3":
                print("\n-----------1D VS 2C1B VS 2A-----------\n")
                r16_separation()
            if choice1=="4":
                print("\n-----------1B VS 2A-----------\n")
                r16_separation()
            if choice1=="5":
                print("\n-----------1E VS 2F-----------\n")
                r16_separation()
            if choice1=="6":
                print("\n-----------1G VS 2H1E VS 2F-----------\n")
                r16_separation()
            if choice1=="7":
                print("\n-----------1F VS 2E-----------\n")
                r16_separation()
            if choice1=="8":
                print("\n-----------1H VS 2G1F VS 2E-----------\n")
                r16_separation()

        if ch=="3":
            print("\n","="*15,"QUARTER FINALS","="*15)    
            quarterfinalsmatches()
            choice2=input('Type the match number you want (1,2,3 or 4): ')
            invalid12=["1","2","3","4"]
            while choice2 not in invalid12:
                print("\nInvalid input. Please type 1,2,3 or 4 . \n")
                choice2=input("Type the match number you want (1,2,3 or 4): ")
            if choice2=="1":
                print("\n-----------W53 VS W54-----------\n")
                qf_separation()
            if choice2=="2":
                print("\n-----------W49 VS W50-----------\n")
                qf_separation()
            if choice2=="3":
                print("\n-----------W55 VS W56-----------\n")
                qf_separation()
            if choice2=="4":
                print("\n-----------W51 VS W52-----------\n")
                qf_separation()

        if ch=="4":
            print("\n","="*15,"SEMI FINALS","="*15)     
            semifinalsmatches()
            choice3=input('Type the match number you want (1 or 2): ')
            invalid13=["1","2"]
            while choice3 not in invalid13:
                print("\nInvalid input. Please type 1 or 2 . \n")
                choice3=input("Type the match number you want (1 or 2): ")
            if choice3=="1":
                print("\n-----------W57 VS W58-----------\n")
                sf_separation()
            if choice3=="2":
                print("\n-----------W59 VS W60-----------\n")
                sf_separation()
        if ch=="5":
            print("\n","="*15,"FINALS","="*15)
            finalmatches()
            choice4=input('Type the match number you want (1 or 2): ')
            invalid14=["1","2"]
            while choice4 not in invalid14:
                print("\nInvalid input. Please type 1 or 2 . \n")
                choice4=input("Type the match number you want (1 or 2): ")
            if choice4=="1":
                print("\n-----------3RD PLACE-----------\n")
                fl_separation()
            if choice4=="2":
                print("\n-----------FINAL-----------\n")
                f_separation()
    lst=[]
    name=input("\nEnter your full name: ")
    emailid=input("Enter your email ID (Please make sure that the email entered is correct because OTP will be sent to that email): ")
    email="@.com"
    for i in email:
        while i not in emailid:
            print("\nA VALID EMAIL IS REQUIRED FOR THIS PROGRAM TO WORK\n")
            time.sleep(1)
            emailid=input("Enter your email ID (Please make sure that the email entered is correct because OTP will be sent to that email): ")
    Booking()    

def countdown():
    launch = datetime.datetime(2022, 11, 20)
    end = datetime.timedelta(microseconds=-0.00000001)

    countdown = launch - datetime.datetime.now()
    if countdown < end:
        print("The World Cup has Commenced! \n")
        
    else:
        print("The World Cup starts in " + str(countdown.days) + " days. \n")
    time.sleep(1)
    backhome_1 = input("Do you wish to continue, yes or no : \n")
    backhome_1 =backhome_1.lstrip().rstrip()
    list_backhome_1 = ["yes", "no"]
    while backhome_1 not in list_backhome_1:
        print("\nInvalid input. Please type yes or no . \n")
        backhome_1 = input("Do you wish to continue, yes or no :  \n")
        backhome_1 =backhome_1.lstrip().rstrip()
    if backhome_1.lower() == "yes":
        home()
    if backhome_1.lower() == "no":
        quitting()
    else:
        print()

        
def teams():
    with open('FIFA.csv',"r") as csvfile:
                myreader=csv.reader(csvfile)
                print("%10s"%"Group A","%20s"%"Group B","%30s"%"Group C","%40s"%"Group D")
                print("="*105)
                for row in myreader:
                    print("%10s"%row[12],"%20s"%row[13],"%30s"%row[14],"%40s"%row[15])
                print("\n")
    with open('FIFA.csv',"r") as csvfile:
                myreader=csv.reader(csvfile)
                print("%10s"%"Group E","%20s"%"Group F","%30s"%"Group G","%40s"%"Group H")
                print("="*105)
                for row in myreader:
                    print("%10s"%row[16],"%20s"%row[17],"%30s"%row[18],"%40s"%row[19])
                print("\n")
    time.sleep(1)
    backhome_2 = input("Do you wish to continue, yes or no : \n")
    backhome_2 =backhome_2.lstrip().rstrip()
    list_backhome_2 = ["yes", "no"]
    while backhome_2 not in list_backhome_2:
        print("\nInvalid input. Please type yes or no . \n")
        backhome_2 = input("Do you wish to continue, yes or no :  \n")
        backhome_2 =backhome_2.lstrip().rstrip()
    if backhome_2.lower() == "yes":
        home()
    if backhome_2.lower() == "no":
        quitting()
    
def schedule():
    webbrowser.open("https://digitalhub.fifa.com/m/538276bde2718fe6/original/2022fwc_qatar_match_schedule_v34b_11082022_EN_international-use.pdf")
    
    time.sleep(1)
    backhome_3 = input("Do you wish to continue, yes or no : \n")
    backhome_3 =backhome_3.lstrip().rstrip()
    list_backhome_3 = ["yes", "no"]
    while backhome_3 not in list_backhome_3:
        print("\nInvalid input. Please type yes or no . \n")
        backhome_3 = input("Do you wish to continue, yes or no :  \n")
        backhome_3 =backhome_3.lstrip().rstrip()
    if backhome_3.lower() == "yes":
        home()
    if backhome_3.lower() == "no":
        quitting()
        
def tickets():
    webbrowser.open("https://www.fifa.com/fifaplus/en/tournaments/mens/worldcup/qatar2022/tickets")
    
    time.sleep(1)
    backhome_4 = input("Do you wish to continue, yes or no : \n")
    backhome_4 =backhome_4.lstrip().rstrip()
    list_backhome_4 = ["yes", "no"]
    while backhome_4 not in list_backhome_4:
        print("\nInvalid input. Please type yes or no . \n")
        backhome_4 = input("Do you wish to continue, yes or no :  \n")
        backhome_4 =backhome_4.lstrip().rstrip()
    if backhome_4.lower() == "yes":
        home()
    if backhome_4.lower() == "no":
        quitting()
                
        
def worldcupsim():
    print("\nWelcome to the World Cup 2022 Simulator")
    time.sleep(1)
    print("\nType the winner of each group and match and pick your winner!\n")
    time.sleep(1)
    print("(If you would like to go back to the home screen at any time, please type exit)\n")
    time.sleep(2)
    print("Let's begin \n")
    time.sleep(1)
    print("Group A \n")

#Group A
    list_a = ["qatar", "ecuador", "senegal", "netherlands"]
    first_a = input("Who will come first in Group A - (Qatar, Ecuador, Senegal, Netherlands) : \n")
    if first_a.lower()=="exit":
        home()
    
    while first_a.lower() not in list_a:
        print("\nInvalid input \n")
        first_a = input("Who will come first in Group A - (Qatar, Ecuador, Senegal, Netherlands) : \n")
        first_a = first_a.lstrip().rstrip()
        if first_a.lower()=="exit":
            home()
    if first_a.lower() in list_a:
        second_a = input("Who will come second in Group A - (Qatar, Ecuador, Senegal, Netherlands) : \n")
        if second_a.lower()=="exit":
            home()
        second_a = second_a.lstrip().rstrip()
        while second_a.lower() not in list_a or first_a.lower() == second_a.lower():
            print("\nInvalid input \n")
            second_a = input("Who will come second in Group A - (Qatar, Ecuador, Senegal, Netherlands) : \n")
            if second_a.lower()=="exit":
                home()
        if second_a.lower() in list_a:
            print("\nGroup B \n")


#Group B
    list_b = ["england", "iran", "usa", "wales"]
    first_b = input("Who will come first in Group B - (England, Iran, USA, Wales) : \n")
    if first_b.lower()=="exit":
        home()
    first_b = first_b.lstrip().rstrip()
    while first_b.lower() not in list_b:
        print("\n\nInvalid input \n")
        first_b = input("Who will come first in Group B - (England, Iran, USA, Wales) : \n")
        if first_b.lower()=="exit":
            home()
    if first_b.lower() in list_b:
        second_b = input("Who will come second in Group B - (England, Iran, USA, Wales) : \n")
        second_b = second_b.lstrip().rstrip()
        if second_b.lower()=="exit":
            home()
        while second_b.lower() not in list_b or first_b.lower() == second_b.lower():
            print("\n\nInvalid input \n")
            second_b = input("Who will come second in Group B - (England, Iran, USA, Wales) : \n")
            if second_b.lower()=="exit":
                home()
        if second_b.lower() in list_b:
            print("\nGroup C \n")

  
#Group C
    list_c = ["argentina", "saudi arabia", "mexico", "poland"]
    first_c = input("Who will come first in Group C - (Argentina, Saudi Arabia, Mexico, Poland) : \n")
    if first_c.lower()=="exit":
        home()
    first_c = first_c.lstrip().rstrip()
    while first_c.lower() not in list_c:
        print("\n\nInvalid input \n")
        first_c = input("Who will come first in Group C - (Argentina, Saudi Arabia, Mexico, Poland) : \n")
        if first_c.lower()=="exit":
            home()
    if first_c.lower() in list_c:
        second_c = input("Who will come second in Group C - (Argentina, Saudi Arabia, Mexico, Poland) : \n")
        if second_c.lower()=="exit":
            home()
        second_c = second_c.lstrip().rstrip()
        while second_c.lower() not in list_c or first_c.lower() == second_c.lower():
            print("\n\nInvalid input \n")
            second_c = input("Who will come second in Group C - (Argentina, Saudi Arabia, Mexico, Poland) : \n")
            if second_c.lower()=="exit":
                home()
        if second_c.lower() in list_c:
            print("\nGroup D \n")

    
#Group D
    list_d = ["france", "australia", "denmark", "tunisia"]
    first_d = input("Who will come first in Group D - (France, Australia, Denmark, Tunisia) : \n")
    if first_d.lower()=="exit":
        home()
    first_d = first_d.lstrip().rstrip()
    while first_d.lower() not in list_d:
        print("\n\nInvalid input \n")
        first_d = input("Who will come first in Group D - (France, Australia, Denmark, Tunisia) : \n")
        if first_d.lower()=="exit":
            home()
    if first_d.lower() in list_d:
        second_d = input("Who will come second in Group D - (France, Australia, Denmark, Tunisia) : \n")
        second_d = second_d.lstrip().rstrip()
        if second_d.lower()=="exit":
            home()
        while second_d.lower() not in list_d or first_d.lower() == second_d.lower():
            print("\n\nInvalid input \n")
            second_d = input("Who will come second in Group D - (France, Australia, Denmark, Tunisia) : \n")
            if second_d.lower()=="exit":
                home()
        if second_d.lower() in list_d:
            print("\nGroup E \n")

 
#Group E
    list_e = ["spain", "costa rica", "germany", "japan"]
    first_e = input("Who will come first in Group E - (Spain, Costa Rica, Germany, Japan) : \n")
    if first_e.lower()=="exit":
        home()
    first_e = first_e.lstrip().rstrip()
    while first_e.lower() not in list_e:
        print("\nInvalid input \n")
        first_e = input("Who will come first in Group E - (Spain, Costa Rica, Germany, Japan) : \n")
        if first_e.lower()=="exit":
            home()
    if first_e.lower() in list_e:
        second_e = input("Who will come second in Group E - (Spain, Costa Rica, Germany, Japan) : \n")
        second_e = second_e.lstrip().rstrip()
        if second_e.lower()=="exit":
            home()
        while second_e.lower() not in list_e or first_e.lower() == second_e.lower():
            print("\nInvalid input \n")
            second_e = input("Who will come second in Group E - (Spain, Costa Rica, Germany, Japan) : \n")
            if second_e.lower()=="exit":
                home()
        if second_e.lower() in list_e:
            print("\nGroup F \n")

    
#Group F
    list_f = ["belgium", "canada", "morocco", "croatia"]
    first_f = input("Who will come first in Group F - (Belgium, Canada, Morocco, Croatia) : \n")
    if first_f.lower()=="exit":
        home()
    first_f = first_f.lstrip().rstrip()
    while first_f.lower() not in list_f:
        print("\nInvalid input \n")
        first_f = input("Who will come first in Group F - (Belgium, Canada, Morocco, Croatia) : \n")
        if first_f.lower()=="exit":
            home()
    if first_f.lower() in list_f:
        second_f = input("Who will come second in Group F - (Belgium, Canada, Morocco, Croatia) : \n")
        second_f = second_f.lstrip().rstrip()
        if second_f.lower()=="exit":
            home()
        while second_f.lower() not in list_f or first_f.lower() == second_f.lower():
            print("\nInvalid input \n")
            second_f = input("Who will come second in Group F - (Belgium, Canada, Morocco, Croatia) : \n")
            if second_f.lower()=="exit":
                home()
        if second_f.lower() in list_f:
            print("\nGroup G \n")

    
#Group G 
    list_g = ["brazil", "serbia", "switzerland", "cameroon"]
    first_g = input("Who will come first in Group G - (Brazil, Serbia, Switzerland, Cameroon) : \n")
    if first_g.lower()=="exit":
        home()
    first_g = first_g.lstrip().rstrip()
    while first_g.lower() not in list_g:
        print("\nInvalid input \n")
        first_g = input("Who will come first in Group G - (Brazil, Serbia, Switzerland, Cameroon) : \n")
        if first_g.lower()=="exit":
            home()
    if first_g.lower() in list_g:
        second_g = input("Who will come second in Group G - (Brazil, Serbia, Switzerland, Cameroon) : \n")
        second_g = second_g.lstrip().rstrip()
        if second_g.lower()=="exit":
            home()
        while second_g.lower() not in list_g or first_g.lower() == second_g.lower() :
            print("\nInvalid input \n")
            second_g = input("Who will come second in Group G - (Brazil, Serbia, Switzerland, Cameroon) : \n")
            if second_g.lower()=="exit":
                home()
        if second_g.lower() in list_g:
            print("\nGroup H \n")

    
#Group H
    list_h = ["portugal", "ghana", "uruguay", "south korea"]
    first_h = input("Who will come first in Group H - (Portugal, Ghana, Uruguay, South Korea) : \n")
    if first_h.lower()=="exit":
        home()
    first_h = first_h.lstrip().rstrip()
    while first_h.lower() not in list_h:
        print("\nInvalid input \n")
        first_h = input("Who will come first in Group H - (Portugal, Ghana, Uruguay, South Korea) : \n")
        if first_h.lower()=="exit":
            home()
    if first_h.lower() in list_h:
        second_h = input("Who will come second in Group H - (Portugal, Ghana, Uruguay, South Korea) : \n")
        second_h = second_h.lstrip().rstrip()
        if second_h.lower()=="exit":
            home()
        while second_h.lower() not in list_h or first_h.lower() == second_h.lower():
            print("\nInvalid input \n")
            second_h = input("Who will come second in Group H - (Portugal, Ghana, Uruguay, South Korea) : \n")
            if second_h.lower()=="exit":
                home()
        if second_h.lower() in list_h:
            print("\nRound of 16 \n")


    
#Round of 16
    print(first_a.upper() + " VS " + second_b.upper())
    R16_1 = input("Who will win : \n")
    if R16_1.lower()=="exit":
        home()
    R16_1 = R16_1.lstrip().rstrip()
    a=0
    while a == 0 :
        if R16_1.lower() == first_a.lower() or R16_1.lower() == second_b.lower():
            print("Next Match \n")
            a=1
        else:
            if R16_1.lower() != first_a.lower() or R16_1.lower() != second_b.lower():
                print("\nInvalid input \n")
                print(first_a.upper() + " VS " + second_b.upper())
                R16_1 = input("Who will win : \n")
                if R16_1.lower()=="exit":
                    home()
            a=0

    print(first_c.upper() + " VS " + second_d.upper())
    R16_2 = input("Who will win : \n")
    if R16_2.lower()=="exit":
        home()
    R16_2 = R16_2.lstrip().rstrip()
    a=0
    while a == 0 :
        if R16_2.lower() == first_c.lower() or R16_2.lower() == second_d.lower():
            print("Next Match \n")
            a=1
        else:
            if R16_2.lower() != first_c.lower() or R16_2.lower() != second_d.lower():
                print("\nInvalid input \n")
                print(first_c.upper() + " VS " + second_d.upper())
                R16_2 = input("Who will win : \n")
                if R16_2.lower()=="exit":
                    home()
            a=0

    
    print(first_b.upper() + " VS " + second_a.upper())
    R16_3 = input("Who will win : \n")
    if R16_3.lower()=="exit":
        home()
    R16_3 = R16_3.lstrip().rstrip()
    a=0
    while a == 0 :
        if R16_3.lower() == first_b.lower() or R16_3.lower() == second_a.lower():
            print("Next Match \n")
            a=1
        else:
            if R16_3.lower() != first_b.lower() or R16_3.lower() != second_a.lower():
                print("\nInvalid input \n")
                print(first_b.upper() + " VS " + second_a.upper())
                R16_3 = input("Who will win : \n")
                if R16_3.lower()=="exit":
                    home()
            a=0
        

    print(first_d.upper() + " VS " + second_c.upper())
    R16_4 = input("Who will win : \n")
    if R16_4.lower()=="exit":
        home()
    R16_4 = R16_4.lstrip().rstrip()
    a=0
    while a == 0 :
        if R16_4.lower() == first_d.lower() or R16_4.lower() == second_c.lower():
            print("Next Match \n")
            a=1
        else:
            if R16_4.lower() != first_d.lower() or R16_4.lower() != second_c.lower():
                print("\nInvalid input \n")
                print(first_d.upper() + " VS " + second_c.upper())
                R16_4 = input("Who will win : \n")
                if R16_4.lower()=="exit":
                    home()
            a=0


    print(first_g.upper() + " VS " + second_h.upper())
    R16_5 = input("Who will win : \n")
    if R16_5.lower()=="exit":
        home()
    R16_5 = R16_5.lstrip().rstrip()
    a=0
    while a == 0 :
        if R16_5.lower() == first_g.lower() or R16_5.lower() == second_h.lower():
            print("Next Match \n")
            a=1
        else:
            if R16_5.lower() != first_g.lower() or R16_5.lower() != second_h.lower():
                print("\nInvalid input \n")
                print(first_g.upper() + " VS " + second_h.upper())
                R16_5 = input("Who will win : \n")
                if R16_5.lower()=="exit":
                    home()
            a=0


    print(first_e.upper() + " VS " + second_f.upper())
    R16_6 = input("Who will win : \n")
    if R16_6.lower()=="exit":
        home()
    R16_6 = R16_6.lstrip().rstrip()
    a=0
    while a == 0 :
        if R16_6.lower() == first_e.lower() or R16_6.lower() == second_f.lower():
            print("Next Match \n")
            a=1
        else:
            if R16_6.lower() != first_e.lower() or R16_6.lower() != second_f.lower():
                print("\nInvalid input \n")
                print(first_e.upper() + " VS " + second_f.upper())
                R16_6 = input("Who will win : \n")
                if R16_6.lower()=="exit":
                    home()
            a=0


    
    print(first_h.upper() + " VS " + second_g.upper())
    R16_7 = input("Who will win : \n")
    if R16_7.lower()=="exit":
        home()
    R16_7 = R16_7.lstrip().rstrip()
    a=0
    while a == 0 :
        if R16_7.lower() == first_h.lower() or R16_7.lower() == second_g.lower():
            print("Next Match \n")
            a=1
        else:
            if R16_7.lower() != first_h.lower() or R16_7.lower() != second_g.lower():
                print("\nInvalid input \n")
                print(first_h.upper() + " VS " + second_g.upper())
                R16_7 = input("Who will win : \n")
                if R16_7.lower()=="exit":
                    home()
            a=0
    
    print(first_f.upper() + " VS " + second_e.upper())
    R16_8 = input("Who will win : \n")
    if R16_8.lower()=="exit":
        home()
    R16_8 = R16_8.lstrip().rstrip()
    a=0
    while a == 0 :
        if R16_8.lower() == first_f.lower() or R16_8.lower() == second_e.lower():
            print("Quarter-Finals \n")
            a=1
        else:
            if R16_8.lower() != first_f.lower() or R16_8.lower() != second_e.lower():
                print("\nInvalid input \n")
                print(first_f.upper() + " VS " + second_e.upper())
                R16_8 = input("Who will win : \n")
                if R16_8.lower()=="exit":
                    home()
            a=0

    
#Quarter-Finals
    print(R16_1.upper() + " VS " + R16_2.upper())
    QF_1 = input("Who will win : \n")
    if QF_1.lower()=="exit":
        home()
    QF_1 = QF_1.lstrip().rstrip()
    a=0
    while a == 0 :
        if QF_1.lower() == R16_1.lower() or QF_1.lower() == R16_2.lower():
            print("Next Match \n")
            a=1
        else:
            if QF_1.lower() != R16_1.lower() or QF_1.lower() != R16_2.lower():
                print("\nInvalid input \n")
                print(R16_1.upper() + " VS " + R16_2.upper())
                QF_1 = input("Who will win : \n")
                if QF_1.lower()=="exit":
                    home()
            a=0
    
    print(R16_5.upper() + " VS " + R16_6.upper())
    QF_2 = input("Who will win : \n")
    if QF_2.lower()=="exit":
        home()
    QF_2 = QF_2.lstrip().rstrip()
    a=0
    while a == 0 :
        if QF_2.lower() == R16_5.lower() or QF_2.lower() == R16_6.lower():
            print("Next Match \n")
            a=1
        else:
            if QF_2.lower() != R16_5.lower() or QF_2.lower() != R16_6.lower():
                print("\nInvalid input \n")
                print(R16_5.upper() + " VS " + R16_6.upper())
                QF_2 = input("Who will win : \n")
                if QF_2.lower()=="exit":
                    home()
            a=0

    print(R16_3.upper() + " VS " + R16_4.upper())
    QF_3 = input("Who will win : \n")
    if QF_3.lower()=="exit":
        home()
    QF_3 = QF_3.lstrip().rstrip()
    a=0
    while a == 0 :
        if QF_3.lower() == R16_3.lower() or QF_3.lower() == R16_4.lower():
            print("Next Match \n")
            a=1
        else:
            if QF_3.lower() != R16_3.lower() or QF_3.lower() != R16_4.lower():
                print("\nInvalid input \n")
                print(R16_3.upper() + " VS " + R16_4.upper())
                QF_3 = input("Who will win : \n")
                if QF_3.lower()=="exit":
                    home()
            a=0

    
    print(R16_7.upper() + " VS " + R16_8.upper())
    QF_4 = input("Who will win : \n")
    if QF_4.lower()=="exit":
        home()
    QF_4 = QF_4.lstrip().rstrip()
    a=0
    while a == 0 :
        if QF_4.lower() == R16_7.lower() or QF_4.lower() == R16_8.lower():
            print("Semi-Finals \n")
            a=1
        else:
            if QF_4.lower() != R16_7.lower() or QF_4.lower() != R16_8.lower():
                print("\nInvalid input \n")
                print(R16_7.upper() + " VS " + R16_8.upper())
                QF_4 = input("Who will win : \n")
                if QF_4.lower()=="exit":
                    home()
            a=0

    
#Semi-Finals
    print(QF_1.upper() + " VS " + QF_2.upper())
    SF_1 = input("Who will win : \n")
    if SF_1.lower()=="exit":
        home()
    SF_1 = SF_1.lstrip().rstrip()
    a=0
    while a == 0 :
        if SF_1.lower() == QF_1.lower() or SF_1.lower() == QF_2.lower():
            print("Next Match \n")
            a=1
        else:
            if SF_1.lower() != QF_1.lower() or SF_1.lower() != QF_2.lower():
                print("\nInvalid input \n")
                print(QF_1.upper() + " VS " + QF_2.upper())
                SF_1 = input("Who will win : \n")
                if SF_1.lower()=="exit":
                    home()
            a=0
    
    print(QF_3.upper() + " VS " + QF_4.upper())
    SF_2 = input("Who will win : \n")
    if SF_1.lower()=="exit":
        home()
    SF_2 = SF_2.lstrip().rstrip()
    a=0
    while a == 0 :
        if SF_2.lower() == QF_3.lower() or SF_2.lower() == QF_4.lower():
            print("FINALS \n")
            a=1
        else:
            if SF_2.lower() != QF_3.lower() or SF_2.lower() != QF_4.lower():
                print("\nInvalid input \n")
                print(QF_3.upper() + " VS " + QF_4.upper())
                SF_2 = input("Who will win : \n")
                if SF_1.lower()=="exit":
                    home()
            a=0
    
#Finals
    print(SF_1.upper() + " VS " + SF_2.upper())
    FINALS = input("Who will win : \n")
    if FINALS.lower()=="exit":
        home()
    FINALS = FINALS.lstrip().rstrip()
    a=0
    while a == 0 :
        if FINALS.lower() == SF_1.lower() or FINALS.lower() == SF_2.lower():
            print(FINALS.upper() + " are the FIFA World Cup 2022 Winners! \n")
            a=1
        else:
            if FINALS.lower() != SF_1.lower() or FINALS.lower() != SF_2.lower():
                print("\nInvalid input \n")
                print(SF_1.upper() + " VS " + SF_2.upper())
                FINALS = input("Who will win : \n")
                if FINALS.lower()=="exit":
                    home()
            a=0
    
    print("Thank you for playing the World Cup Simulator! \n")
    
    time.sleep(1)
    backhome_5 = input("Do you wish to continue, yes or no :  \n")
    backhome_5 =backhome_5.lstrip().rstrip()
    list_backhome_5 = ["yes", "no"]
    while backhome_5 not in list_backhome_5:
        print("\nInvalid input. Please type yes or no . \n")
        backhome_5 = input("Do you wish to continue, yes or no :  \n")
        backhome_5 =backhome_5.lstrip().rstrip()
    if backhome_5.lower() == "yes":
        home()
    if backhome_5.lower() == "no":
        quitting()
            
def stadiums():
    print("Let's learn about the FIFA World Cup 2022 Qatar Stadiums. \n")
    print("Type the number to choose the stadium. \n")
    print("1.Khalifa International Stadium  2.Al Bayt Stadium  3.Al Janoub Stadium  4.Al Rayyan Stadium  5.Education City stadium  6.Al Thumama Stadium  7.Stadium 974  8.Lusail Stadium \n")
    stadium = input("Enter the number of the stadium: (1,2,3....,8) ")
    stadium = stadium.lstrip().rstrip()
    list_stadium = ["1", "2", "3", "4" , "5", "6", "7", "8"]
    while stadium.lower() not in list_stadium:
        print("\nInvalid input. Please enter . \n")
        print("Thank you for reaching out. These are my features, choose any one of these options by typing the number  \n")
        print("1.Khalifa International Stadium  2.Al Bayt Stadium  3.Al Janoub Stadium  4.Al Rayyan Stadium  5.Education City stadium  6.Al Thumama Stadium  7.Stadium 974  8.Lusail Stadium \n")
        stadium = input("Enter the number of the stadium: (1,2,3....,8) ")
        stadium = stadium.lstrip().rstrip()
        
    if stadium.lower() == "1":
        print("\nDesign inspiration: An ultra-modern stadium that honours Qatar’s sporting history") 
        print("2022 matches: Up to the quarter-final stage")
        print("Legacy: Home stadium of Qatar’s national team") 
        print("2022 Capacity: 40,000\n")
    if stadium.lower() == "2":
        print("\nDesign inspiration: The bayt al-sha’ar of nomadic peoples who have lived in Qatar’s deserts for millennia")
        print("2022 matches: Up to the semi-final stage")
        print("2022 capacity: 60,000")
        print("Legacy: Home of Al Khor Sports Club\n")
    if stadium.lower() == "3":
        print("\nDesign inspirtion: The sails of traditional dhow boats")
        print("2022 matches: Up to the quarter-final stage")
        print("2022 capacity: 40,000")
        print("Legacy: Home of Al Wakrah Sports Club\n")
    if stadium.lower() == "4":
        print("\nDesign inspiration: Qatar’s story – the importance of family, beauty of the desert, and native flora and fauna")
        print("2022 matches: Up to the quarter-final stage")
        print("2022 capacity: 40,000")
        print("Legacy: Home of Al Rayyan Sports Club\n")
    if stadium.lower() == "5":
        print("\nDesign inspiration: The rich history of Islamic architecture blended with striking modernity") 
        print("2022 matches: Up to the quarter-final stage ")
        print("2022 capacity: 40,000 ")
        print("Legacy: Facilities for the Qatar Foundation community and general public\n")
    if stadium.lower() == "6":
        print("\nDesign inspiration: The gahfiya (traditional woven cap) worn by men and boys in the Middle East ")
        print("2022 matches: Up to the quarter-final stage ")
        print("2022 capacity: 40,000 ")
        print("Legacy: Home of a local football club\n")
    if stadium.lower() == "7":
        print("\nDesign inspiration: A beacon of innovation and sustainability on the shores of the Gulf ")
        print("2022 matches: Up to the quarter-final stage ")
        print("2022 capacity: 40,000 ")
        print("Legacy: A seafront development on the stadium site and multiple sporting facilities around Qatar\n")
    if stadium.lower() == "8":
        print("\nDesign inspiration: The interplay of light and shadow that characterises the fanar lantern")
        print("2022 matches: Matches throughout the tournament including the opening game and final ")
        print("2022 capacity: 80,000 ")
        print("Legacy: A unique community hub of schools, housing, shops, cafes and health clinics\n")
    
    tocontinue = input("Do you wish to know about other stadiums - yes or no :\n")
    tocontinue = tocontinue.lstrip().rstrip()
    list_tocontinue = ["yes", "no"]
    while tocontinue not in list_tocontinue:
        print("\nInvalid input. Please type yes or no . \n")
        tocontinue = input("Do you wish to know about other stadiums, yes or no :\n")
        tocontinue = tocontinue.lstrip().rstrip()
    a = 0 
    while a == 0 :
        if tocontinue.lower() == "no":
            
            backhome_6 = input("Do you wish to go back to the home page , yes or no :\n")
            backhome_6 =backhome_6.lstrip().rstrip()
            list_backhome_6 = ["yes", "no"]
            while backhome_6 not in list_backhome_6:
                print("\nInvalid input. Please type yes or no . \n")
                backhome_6 = input("Do you wish to go back to home page, yes or no :\n")
                backhome_6 =backhome_6.lstrip().rstrip()
            if backhome_6.lower() == "yes":
                home()
            if backhome_6.lower() == "no":
                quitting()
            a = 1
            
        if tocontinue.lower() == "yes":
            print("Here are the stadiums :")
            print("1.Khalifa International Stadium  2.Al Bayt Stadium  3.Al Janoub Stadium  4.Al Rayyan Stadium  5.Education City stadium  6.Al Thumama Stadium  7.Stadium 974  8.Lusail Stadium \n")
            stadium = input("Enter the number of the stadium: (1,2,3....,8) ")
            stadium = stadium.lstrip().rstrip()
            list_stadium = ["1", "2", "3", "4" , "5", "6", "7", "8"]
            while stadium not in list_stadium:
                print("\nInvalid input. Please enter . \n")
                print("Here are the stadiums : \n")
                print("1.Khalifa International Stadium  2.Al Bayt Stadium  3.Al Janoub Stadium  4.Al Rayyan Stadium  5.Education City stadium  6.Al Thumama Stadium  7.Stadium 974  8.Lusail Stadium \n")
                stadium = input(" Enter the number of the stadium: (1,2,3....,8) ")
                stadium = stadium.lstrip().rstrip()
            if stadium.lower() == "1":
                print("\nKhalifa International Stadium")
                print("Design inspiration: An ultra-modern stadium that honours Qatar’s sporting history") 
                print("2022 matches: Up to the quarter-final stage")
                print("Legacy: Home stadium of Qatar’s national team") 
                print("2022 Capacity: 40,000\n")
            if stadium.lower() == "2":
                print("\nAl Bayt Stadium")
                print("Design inspiration: The bayt al-sha’ar of nomadic peoples who have lived in Qatar’s deserts for millennia")
                print("2022 matches: Up to the semi-final stage")
                print("2022 capacity: 60,000")
                print("Legacy: Home of Al Khor Sports Club\n")
            if stadium.lower() == "3":
                print("\nAl Janoub Stadium")
                print("Design inspirtion: The sails of traditional dhow boats")
                print("2022 matches: Up to the quarter-final stage")
                print("2022 capacity: 40,000")
                print("Legacy: Home of Al Wakrah Sports Club\n")
            if stadium.lower() == "4":
                print("\nAl Rayyan Stadium")
                print("Design inspiration: Qatar’s story – the importance of family, beauty of the desert, and native flora and fauna")
                print("2022 matches: Up to the quarter-final stage")
                print("2022 capacity: 40,000")
                print("Legacy: Home of Al Rayyan Sports Club\n")
            if stadium.lower() == "5":
                print("\nEducation City Stadium")
                print("Design inspiration: The rich history of Islamic architecture blended with striking modernity") 
                print("2022 matches: Up to the quarter-final stage ")
                print("2022 capacity: 40,000 ")
                print("Legacy: Facilities for the Qatar Foundation community and general public\n")
            if stadium.lower() == "6":
                print("\nAl Thumama Stadium")
                print("Design inspiration: The gahfiya (traditional woven cap) worn by men and boys in the Middle East ")
                print("2022 matches: Up to the quarter-final stage ")
                print("2022 capacity: 40,000 ")
                print("Legacy: Home of a local football club\n")
            if stadium.lower() == "7":
                print("\nStadium 974")
                print("Design inspiration: A beacon of innovation and sustainability on the shores of the Gulf ")
                print("2022 matches: Up to the quarter-final stage ")
                print("2022 capacity: 40,000 ")
                print("Legacy: A seafront development on the stadium site and multiple sporting facilities around Qatar\n")
            if stadium.lower() == "8":
                print("\nLusail Stadium")
                print("Design inspiration: The interplay of light and shadow that characterises the fanar lantern")
                print("2022 matches: Matches throughout the tournament including the opening game and final ")
                print("2022 capacity: 80,000 ")
                print("Legacy: A unique community hub of schools, housing, shops, cafes and health clinics\n")
            
            backhome_7 = input("Do you wish to continue , yes or no :\n")
            backhome_7 =backhome_7.lstrip().rstrip()
            list_backhome_7 = ["yes", "no"]
            while backhome_7 not in list_backhome_7:
                print("\nInvalid input. Please type yes or no . \n")
                backhome_7 = input("Do you wish to continue , yes or no :\n")
                backhome_7 =backhome_7.lstrip().rstrip()
            if backhome_7.lower() == "yes":
                a = 0
            if backhome_7.lower() == "no":
                home()
def quitting():
    print("\nTHANK YOU for using this simulator ")
    time.sleep(2)
    os._exit(0)

def contactus():
    webbrowser.open("https://www.fifa.com/about-fifa/organisation/contact-fifa")    
    time.sleep(1)
    backhome_8 = input("Do you wish to continue, yes or no : \n")
    backhome_8 =backhome_8.lstrip().rstrip()
    list_backhome_8 = ["yes", "no"]
    while backhome_8 not in list_backhome_8:
        print("\nInvalid input. Please type yes or no . \n")
        backhome_8 = input("Do you wish to continue, yes or no :  \n")
        backhome_8 =backhome_8.lstrip().rstrip()
    if backhome_8.lower() == "yes":
        home()
    if backhome_8.lower() == "no":
        quitting()
    
def home():
    choice = input("\n1.Book Tickets(New!)  2.Teams  3.Match Schedule  4.Countdown  5.Stadiums  6.World Cup Predictor 7.Contact Us page  8.Exit \n(1,2,3.....,8): ")
    choice = choice.lstrip().rstrip()
    list_home = ["1", "2", "3", "4" , "5", "6", "7", "8"]
    while choice not in list_home:
        print("\nInvalid input. Please enter 1,2,3.... or 8. \n")
        print("Thank you for reaching out. These are my features, choose any one of these options by typing the number \n")
        choice = input("1.Book Tickets(New!)  2.Teams  3.Match Schedule  4.Countdown  5.Stadiums  6.World Cup Predictor 7.Contact us page  8.Exit \n(1,2,3.....,8): ")
        choice = choice.lstrip().rstrip()
    if choice == "1":
        booktickets()
    if choice == "2":
        teams()
    if choice == "3":
        schedule()
    if choice == "4":
        countdown()
    if choice == "5":
        stadiums()  
    if choice == "6":
        worldcupsim()
    if choice == "7":
        contactus()
    if choice == "8":
        quitting()
        
total=0        
print("\nHi, I am La'eeb, the official mascot of the 2022 FIFA World Cup")
time.sleep(1.5)
print("\nThank you for reaching out. These are my features, choose any one of these options by typing the number ")
home()
