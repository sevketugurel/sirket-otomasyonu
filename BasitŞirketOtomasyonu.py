class Sirket():
    def __init__(self,ad):
        self.ad=ad
        self.calisma=True

    def program(self):
        secim=self.menusecim()

        if secim==1:
            self.calisanEkle()
        elif secim==2:
            self.calisanCikar()
        elif secim==3:
            self.verilecekMaasGoster()
        elif secim==4:
            self.maaslariVer()
        

    def menusecim(self):
        secim=int(input("\n*** {} otomasyona hoşgeldiniz..***\n\n1-Çalışan Ekle \n2-Çalışan Çıkar\n3-Verilecek Maaş Göster\n4-maasları ver \n5-Masraf Gir\n6- Gelir Gir\nSeçiminizi giriniz...".format(self.ad)))
        while secim<1 or secim>6:
            secim=int(input("lütfen 1-6 arasında bedlirtilen seçeneklerden birisini giriniz: "))
        return secim
    
    def calisanEkle(self):
        id=1
        ad=input("Çalışan Adını giriniz..")
        soyad=input("Çalışan soyadını giriniz..")
        yaş=input("Çalışan yaşını  giriniz..")
        cinsiyet=input("Çalışan cinsiyetini giriniz..")
        maaş=input("Çalışan maaşını giriniz..")

        with open("/Users/sevketugurel/Desktop/Python/Yaptığım Projeler/Calisanlar.txt","r",) as Dosya:
            calisanlarListesi=Dosya.readlines()

        if len(calisanlarListesi)==0:
            id=1+")"
        else:
            with open("/Users/sevketugurel/Desktop/Python/Yaptığım Projeler/Calisanlar.txt","r",) as Dosya:
                id=int(Dosya.readlines()[-2].split(")")[0])+1


        with open("/Users/sevketugurel/Desktop/Python/Yaptığım Projeler/Calisanlar.txt","a+",) as Dosya:
            Dosya.write("{}){}-{}-{}-{}-{}\n".format(id,ad,soyad,yaş,cinsiyet,maaş))

    def calisanCikar(self):
        with open("/Users/sevketugurel/Desktop/Python/Yaptığım Projeler/Calisanlar.txt","r") as Dosya:
            calisanlar=Dosya.readlines()
        gCalisanlar=[]

        for calisan in calisanlar:
            gCalisanlar.append(" ".join(calisan[:-1].split("-")))

        for calisan in gCalisanlar:
            print(calisan)
        secim=int(input("Lütfen Çıkarmak isteidiğiniz çalışanın numrasını giriniz(1-{})".format(len(gCalisanlar))))
        while secim>len(gCalisanlar) or secim<1:
            secim=int(input("lütfen 1-{} arasında bir numara giriniz..".format(len(gCalisanlar))))
        calisanlar.pop(secim-1)
        
        sayac=1

        dCalisanlar=[]

        for calisan in calisanlar:
            dCalisanlar.append(str(sayac)+")"+calisan.split(")")[1])
            sayac+=1
        
        with open("/Users/sevketugurel/Desktop/Python/Yaptığım Projeler/Calisanlar.txt","w",) as Dosya:
            Dosya.writelines(dCalisanlar)

    
    def verilecekMaasGoster(self,hesap="a"):
        """ hesap: a ise aylık, y ise yıllık"""
        with open("/Users/sevketugurel/Desktop/Python/Yaptığım Projeler/Calisanlar.txt","r",) as Dosya:
            calisanlar=Dosya.readlines()
        maaslar=[]
        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))
        print("\nBu ay Ödemeniz gereken toplam Maaş tutarı:{}".format(sum(maaslar)))

    def maaslariVer(self):
        with open("/Users/sevketugurel/Desktop/Python/Yaptığım Projeler/Calisanlar.txt","r",) as Dosya:
            calisanlar=Dosya.readlines()
        maaslar=[]
        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))
        toplamMaas=sum(maaslar)

        ### bütçeden maaşşı alma
        with open("/Users/sevketugurel/Desktop/Python/Yaptığım Projeler/Butce.txt","r",) as Dosya:
           toplamButce= int(Dosya.readlines()[0])
        
        toplamButce=toplamButce-toplamMaas

        with open("/Users/sevketugurel/Desktop/Python/Yaptığım Projeler/Butce.txt","w",) as Dosya:
            Dosya.write(str(toplamButce))



sirket=Sirket("Ugurel LLC")
while sirket.calisma:
    sirket.program()
