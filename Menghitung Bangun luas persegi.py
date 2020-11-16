#Dibuat oleh Atalaric Raihan dan Imron Assidiqi
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
def kelilingsegitiga(sisi1,sisi2,sisi3):
    keliling=sisi1+sisi2+sisi3
    return keliling
def luaslingkaran(jari):
    luas=3.14*(jari*jari)
    return luas
def kelilinglingkaran(jari):
    keliling=2*3.14*jari
    return keliling
def luasjajargenjang(alas,tinggi):
    luas=alas*tinggi
    return luas
def kelilingjajargenjang(alas,miring):
    keliling=2*(alas+miring)
    return keliling
    
class bangundatar:
    pass
pilihan=1
while pilihan !=0:
    print("1. menghitung luas persegi")
    print("2. menghitung keliling persegi")
    print("3. menghitung luas persegi panjang")
    print("4. menghitung keliling persegi panjang")
    print("5. menghitung luas segitiga")
    print("6. menghitung keliling segitiga")
    print("7. menghitung luas lingkaran")
    print("8. menghitung keliling lingkaran")
    print("9. menghitung luas jajar genjang")
    print("10. menghitung keliling jajar genjang")
    print("0. keluar")
    
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
    elif pilihan==7:
        A=int(input("masukkan jari-jari :"))
        print("Luas lingkaran : 3.14*(",A,")^2 =",luaslingkaran(A))
        print("")
    elif pilihan==8:
        A=int(input("masukkan jari-jari :"))
        print("Keliling lingkaran : 2 * 3.14 *",A,"=",kelilinglingkaran(A))
        print("")
    elif pilihan==9:
        A=int(input("masukkan alas   :"))
        B=int(input("masukkan tinggi :"))
        print("Luas jajar genjang :",A,"*",B,"=",luasjajargenjang(A,B))
        print("")
    elif pilihan==10:
        A=int(input("masukkan sisi alas   :"))
        B=int(input("masukkan sisi miring :"))
        print("Keliling jajar genjang : 2*(",A,"+",B,")=",kelilingjajargenjang(A,B))
        print("")
    elif pilihan==0:
        print("TERIMAKASIH TELAH MENCOBA")
    else:
        print("INPUT SALAH")
        print("") 
