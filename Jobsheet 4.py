def luaspersegi(sisi):
    luas=sisi*sisi
    return luas
def kelilingpersegi(sisi):
    keliling=4*sisi
    return keliling
def luaspersegipanjang(panjang,lebar):
    luas=panjang*lebar
    return luas
def kelilingpersegipanjang(panjang,lebar):
    keliling=2*(panjang+lebar)
    return keliling
def luassegitiga(alas,tinggi):
    luas=0.5*alas*tinggi
    return luas
    
class bangundatar:
    pass
pilihan=1
while pilihan !=0:
    print("1. menghitung luas persegi")
    print("2. menghitung keliling persegi")
    print("3. menghitung luas persegi panjang")
    print("4. menghitung keliling persegi panjang")
    print("5. menghitung luas segitiga")
    
    print("")
    print("")
    pilihan=int(input("masukkan pilihan anda :"))
    print("")
    print("")
    
    if pilihan==1:
        A=int(input("masukkan sisi persegi :"))
        print("Luas persegi :",A,"*",A,"=",luaspersegi(A))
        print("")
    elif pilihan==2:
        A=int(input("masukkan sisi persegi :"))
        print("Keliling persegi : 4*(",A,") =",kelilingpersegi(A))
        print("")
    elif pilihan==3:
        A=int(input("masukkan panjang :"))
        B=int(input("masukkan lebar   :"))
        print("Luas persegi panjang :",A,"*",B,"=",luaspersegipanjang(A,B))
        print("")
    elif pilihan==4:
        A=int(input("masukkan panjang :"))
        B=int(input("masukkan lebar   :"))
        print("Keliling persegi panjang : 2*(",A,"+",B,")=",kelilingpersegipanjang(A,B))
        print("")
    elif pilihan==5:
        A=int(input("masukkan alas   :"))
        B=int(input("masukkan tinggi :"))
        print("Luas segitiga : 0.5*",A,"*",B,"=",luassegitiga(A,B))
        print("")
    elif pilihan==6:
        A=int(input("masukkan sisi a :"))
        B=int(input("masukkan sisi b :"))
        C=int(input("masukkan sisi c :"))
        print("Keliling segitiga :",A,"+",B,"+",C,"=",kelilingsegitiga(A,B,C))
        print("")
    elif pilihan==0:
        print("TERIMAKASIH TELAH MENCOBA")
    else:
        print("INPUT SALAH")
        print("") 
