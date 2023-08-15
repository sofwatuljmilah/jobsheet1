import random
from guess import TebakAngka

tebak = TebakAngka()
tebak.jawaban = random.randint(1,10)
tebak.tebakan = int(input("Tebak angka dari 1 s.d 10:  "))

if tebak.cek() :
	print("Jawaban Kamu Benar !")
else :
	print("Jawaban Kamu Salah !")