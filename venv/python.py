import numpy as np          #匯入陣列套件
import pandas as pd         #匯入
import math

#[patient ID,N,volume of PN, glucose,a.a.,fat,Zn,[t],3-way]

yourchoose=input("請選擇你要的作業內容：\n1：計算明日應準備器具數量\n2：調配微量物質")

if yourchoose=="1":
    number=input("請輸入明日要準備人數")
    number=eval(number)
    PNinformation=[]

    #輸入資訊
    for i in range(number):
        PNinformation.append([])
        patientID=input("請輸入病人 ID")
        PNinformation[i].append(patientID)
        Nn=eval(input("是否有大 N，無請按0，有請按1"))
        PNinformation[i].append(Nn)
        PNvolume=eval(input("請輸入 PN 體積"))
        PNinformation[i].append(PNvolume)
        glucosepercent=eval(input("請輸入葡萄糖濃度"))
        PNinformation[i].append(glucosepercent)
        aminoacidpercent = eval(input("請輸入氨基酸濃度"))
        PNinformation[i].append(aminoacidpercent)
        fatvolume = eval(input("請輸入 fat 毫升數"))
        PNinformation[i].append(fatvolume)
        Zn = eval(input("請輸入所需鋅毫升數"))
        PNinformation[i].append(Zn)
        Znt = eval(input("請輸入所需 [t] 毫升數"))
        PNinformation[i].append(Znt)
        threeway = eval(input("請輸入所需 3-way 數量"))
        PNinformation[i].append(threeway)
        finish="你完成第 %d 筆資料"%(i+1)
        print(finish)

    #修正錯誤資訊
    confirm=input("確認輸入資料無誤，若有錯誤請按1，如無錯誤請按2")
    while confirm=="1":
        wrongID=input("請輸入欲修改的病人ID")
        wrongdata=input("請輸入欲修改項目：\n1.病人ID\n2.N\n3.PN 體積"
                        "\n4.葡萄糖含量\n5.氨基酸含量\n6.脂質毫升數"
                        "\n7.鋅毫升數\n8.[t]毫升數\n9.3-way數量")
        wrongdata=eval(wrongdata)-1
        rightdata=input("請輸入正確資訊")
        if wrongdata !="1":
            rightdata=eval(rightdata)
        for i in range(number):
            if PNinformation[i][0]==wrongID:
                PNinformation[i][wrongdata]=rightdata
                for i in range(number):
                    displayarray = PNinformation[i]
                    print(displayarray)
        confirm1=input("確認輸入資料無誤，若有錯誤請按1，如無錯誤請按2")
        if confirm1 == "2":
            for i in range(number):
                displayarray= PNinformation[i]
                print(displayarray)
            break
    while confirm=="2":
        for i in range(number):
            displayarray=PNinformation[i]
            print(displayarray)
        break


    glucose=0.0
    glucose50=50/100
    totalglucose=0.0
    #計算葡萄糖總量
    for i in range(number):
        glucose=PNinformation[i][2]*(PNinformation[i][3]/100)
        totalglucose=totalglucose+glucose
    totalglucosemL=math.ceil(totalglucose/glucose50/500)
    youneedglucose="你總共需要準備%d瓶葡萄糖溶液"%(totalglucosemL)
    print(youneedglucose)

if yourchoose=="2":
    #設定離子參數
    K2PO4_K=4.4
    K2PO4_PO4=3
    NaOAc_Na=4
    NaOAc_OAc=4
    KCl_K=2
    KCl_Cl=2
    NaCl_Na=0.51
    NaCl_Cl=0.51
    Aminoplasmal_Na=0.050
    Aminoplasmal_K=0.025
    Aminoplasmal_Mg=0.005
    Aminoplasmal_OAc=0.046
    Aminoplasmal_Cl=0.052
    Aminoplasmal_PO4=0.010
    Moriamin_OAc=0.06
    Aminosteril_OAc=0.078
    MgSO4_Mg=0.811
    Cagluconate_Ca=0.465
    Pedicare=0.058

    #設定原料藥濃度
    Aminoplasmal=10/100
    NaCl=3/100
    MgSO4=10/100
    KCl=15/100
    #Cagluconate=10/100
    glucose50_1=50/100

    #輸入資訊
    number1 = input("請輸入明日要準備人數")
    number1 = eval(number1)
    PNinformation1 = []

    for i in range(number1):
        PNinformation1.append([])
        patientID1=input("請輸入病人 ID")
        PNinformation1[i].append(patientID1)
        PNvolume1 = eval(input("請輸入 PN 總體積"))
        PNinformation1[i].append(PNvolume1)
        glucosepercent1 = eval(input("請輸入葡萄糖含量"))
        PNinformation1[i].append(glucosepercent1)
        aminoacidpercent1 = eval(input("請輸入氨基酸含量"))
        PNinformation1[i].append(aminoacidpercent1)
        Na = eval(input("請輸入鈉總含量"))
        PNinformation1[i].append(Na)
        K = eval(input("請輸入鉀總含量"))
        PNinformation1[i].append(K)
        Cl = eval(input("請輸入氯總含量"))
        PNinformation1[i].append(Cl)
        Mg = eval(input("請輸入鎂總含量"))
        PNinformation1[i].append(Mg)
        Ca = eval(input("請輸入鈣總含量"))
        PNinformation1[i].append(Ca)
        P = eval(input("請輸入磷總含量"))
        PNinformation1[i].append(P)
        finish2="你完成第 %d 筆資料"%(i+1)
        print(finish2)

    # 修正錯誤資訊
    confirm2 = input("確認輸入資料無誤，若有錯誤請按1，如無錯誤請按2")
    while confirm2 == "1":
        wrongID1 = input("請輸入欲修改的病人ID")
        wrongdata1 = input("請輸入欲修改項目："
                            "\n1.病人ID"    #0
                            "\n2.PN 總體積" #1
                            "\n3.葡萄糖含量" #2
                            "\n4.氨基酸含量" #3
                            "\n5.鈉總量"    #4
                            "\n6.鉀總量"    #5
                            "\n7.氯總量"    #6
                            "\n8.鎂總量"    #7
                            "\n9.鈣總量"    #8
                            "\n10.磷總量")  #9
        wrongdata1 = eval(wrongdata1) - 1
        rightdata1 = input("請輸入正確資訊")
        if wrongdata1 != "1":
            rightdata1 = eval(rightdata1)
        for i in range(number1):
            if PNinformation1[i][0] == wrongID1:
                    PNinformation1[i][wrongdata1] = rightdata1
                    for i in range(number1):
                        displayarray1=PNinformation1[i]
                        print(displayarray1)
                    print(PNinformation1)
        confirm3 = input("確認輸入資料無誤，若有錯誤請按1，如無錯誤請按2")
        if confirm3 == "2":
            for i in range(number1):
                displayarray1 = PNinformation1[i]
                print(displayarray1)
            break
    while confirm2 == "2":
        for i in range(number1):
            displayarray1 = PNinformation1[i]
            print(displayarray1)
        break

    materialmL=[]
    for i in range(number1):
        glucose1= (PNinformation1[i][1]*PNinformation1[i][2]/100)/glucose50_1
        aminoacid1=(PNinformation1[i][1]*PNinformation1[i][3]/100)/Aminoplasmal
        Ca_mL = PNinformation1[i][8]/Cagluconate_Ca
        Mg_mL = (PNinformation1[i][7]-aminoacid1*Aminoplasmal_Mg)/MgSO4_Mg
        K2PO4_mL = (PNinformation1[i][9]-aminoacid1*Aminoplasmal_PO4)/K2PO4_PO4
        KCl_mL = (PNinformation1[i][5]-aminoacid1*Aminoplasmal_K-K2PO4_mL*K2PO4_K)/KCl_K
        NaCl_mL= (PNinformation1[i][6]-aminoacid1*Aminoplasmal_Cl-KCl_mL*KCl_Cl)/NaCl_Cl
        NaOAc_mL=(PNinformation1[i][4]-aminoacid1*Aminoplasmal_Na-NaCl_mL*NaCl_Na)/NaOAc_Na

        if NaCl_mL<0:
            A1=NaCl_Na
            B1=NaOAc_Na
            C1=PNinformation1[i][4]-aminoacid1*Aminoplasmal_Na
            A2=NaCl_Cl
            B2=-NaOAc_OAc
            C2=aminoacid1*Aminoplasmal_OAc-aminoacid1*Aminoplasmal_Cl-KCl_mL*KCl_Cl

            Eq1=np.array([[A1,B1],[A2,B2]])
            Eq2=np.array([C1,C2]).reshape(2,1)
            Eq1_inv=np.linalg.inv(Eq1)
            ANS=Eq1=Eq1_inv.dot(Eq2)
            NaCl_mL=float(ANS[0])
            NaOAc_mL=float(ANS[1])

        glucose1=round(glucose1,2)
        aminoacid1=round(aminoacid1,2)
        Ca_mL=round(Ca_mL,2)
        Mg_mL=round(Mg_mL,2)
        K2PO4_mL=round(K2PO4_mL,2)
        KCl_mL=round(KCl_mL,2)
        NaCl_mL=round(NaCl_mL,2)
        NaOAc_mL=round(NaOAc_mL,2)

        patient="病人ID %s"%(PNinformation1[i][0])
        glucose1mL="你需要 %f mL 葡萄糖溶液"%(glucose1)
        aminoacid1mL="你需要 %f mL Aminoplasmal-Neo E"%(aminoacid1)
        CamL = "你需要 %f mL Ca gluconate\n"%(Ca_mL)
        MgmL = "你需要 %f mL MgSO4 溶液"%(Mg_mL)
        K2PO4mL="你需要 %f mL K2PO4 溶液"%(K2PO4_mL)
        KClmL = "你需要 %f mL KCl 溶液"%(KCl_mL)
        NaClmL = "你需要 %f mL NaCl 溶液"%(NaCl_mL)
        NaOAcmL = "你需要 %f mL NaOAc 溶液"%(NaOAc_mL)



        print(patient)

        if glucose1 <0 or aminoacid1<0 or Ca_mL <0 or Mg_mL <0 or K2PO4_mL<0 or KCl_mL<0 or NaCl_mL<0 or NaOAc_mL<0:
            print("本程式已使用線性代數幫你找到最佳解\n如依然是負數，煩請人工調整")

        print(glucose1mL)
        print(aminoacid1mL)
        print(NaClmL)
        print(K2PO4mL)
        print(MgmL)
        print(KClmL)
        print(NaOAcmL)
        print(CamL)
