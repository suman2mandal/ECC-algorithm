import numpy as geek

def polynomial(LHS, RHS, n):
    for i in range(0, n):
        LHS[0].append(i)
        RHS[0].append(i)
        LHS[1].append((i * i * i + a * i + b) % n)
        RHS[1].append((i * i) % n)


def points_generate(arr_x, arr_y, n):
    count = 0
    for i in range(0, n):
        for j in range(0, n):
            if (LHS[1][i] == RHS[1][j]):
                count += 1
                arr_x.append(LHS[0][i])
                arr_y.append(RHS[0][j])
    return count

def read_file(name):
    file_ = open(name,'rb')
    temp=''
    for i in file_:
        temp+=i.decode('ISO-8859-1')

    file_.close()
    return temp

def write_file(name,data):
    file_ = open(name,'wb')
    for j in data:
        file_.write(j.encode('ISO-8859-1'))

    file_.close()

n = int(input ("Enter n(prime) :"))

LHS = [[],[]]
RHS = [[],[]]

print("Enter a:")
a= int(input())

print("Enter b:")
b =int(input())
polynomial(LHS, RHS, n)

arr_x = []
arr_y = []

count = points_generate(arr_x, arr_y, n)

bx = arr_x[5]
by = arr_y[0]
print("G:\t(", bx, ",", by, ")\n")

print("Enter the Private key of Sender d (d<n):", end=" ")
d = int(input())
print("Private Key for recipients  : ", d )
if (d >= n):
    print("'d' should be smaller than 'n'.")
else:
    Qx = d * bx
    Qy = d * by
    print("Public key :\t(", Qx, ",", Qy, ")\n")

    # Encrytion
    k = d
    if (k >= n):
        print("'k' should be smaller than 'n'")
    else:

        # Cipher text 1 generation
        C1x = k * Qx
        C1y = k * Qy
        print("Point generated for Encryption:\t(", C1x, ",", C1y, ")\n")

        # Cipher text 2 generation
        C2x = k * bx
        C2y = k * by
        print("Point generated for Decryption :\t(", C2x, ",", C2y, ")\n")

        Et1 = chr(C2x)
        Et2 = chr(C2y)
        

        Ek = C1x
        
        Eb = [bin(Ek)[2:].zfill(8)]
        Ebb= ','.join(Eb)
       

        # print("Enter the message to be sent:\n")
        # B = str(input())
        # take input from file
        file_name = input("Enter file name containing message:")
        B = read_file(file_name)



        In = [ord(c) for c in B]
        print(In)

        Bi = [bin(x) [2:].zfill(8) for x in In]
        Bii= ','.join(Bi)

        data = Bii
        key = Ebb

        in_arr1 = In
        in_arr2 = [Ek]

        #print("Input array1 : ", in_arr1)
        #print("Input array2 : ", in_arr2)

        out_arr = geek.bitwise_xor(in_arr1, in_arr2)
        Ekb = [bin(x)[2:].zfill(8) for x in out_arr]
        Dekripsi_xor = ''.join([chr(int(x, 2)) for x in Ekb])
        

        q= Et1
        w= Et2
        e= Dekripsi_xor
        t= '#'
        z= q+t+w+t+e
        
        Dz=z[4:]
        
        bz = [ord(c) for c in Dz]
        print(bz)
        
        bzi = [bin(x)[2:].zfill(8) for x in bz]

        Kt1= k*C2x
        Kt2= k*C2y
        #print("Point KP (Decryption Point) :\t(", Kt1, ",", Kt2, ")\n")

        Edt = Kt1
        #print("Absent Point KKP = ", Edt)
        Edtb = [bin(Edt)[2:].zfill(8)]
        Edtbb = ','.join(Edtb)

        Dek_arr1 = bz
        Dek_arr2 = [Edt]

        print("Input array1 : ", Dek_arr1)
        print("Input array2 : ", Dek_arr2)

        Fin_arr = geek.bitwise_xor(Dek_arr1, Dek_arr2)
        #print("Output array after bitwise_xor: ", Fin_arr)

        Pl = [bin(x)[2:].zfill(8) for x in Fin_arr]
        
        Plaintex_ecc = ''.join([chr(int(x, 2)) for x in Pl])

        # Write the data in file
        write_file_name = input("Enter file name to write message:")
        write_file(write_file_name,Plaintex_ecc)
        print("The original text is =",Plaintex_ecc)


input("Encrytion and Decryption done. Press any key to exit.")
