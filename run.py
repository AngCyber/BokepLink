#!/usr/bin/python3
#coding=utf-8
#code by Moch Aang Ardiansyah XD.

import os
import sys
import time


P = "\x1b[0;97m"
H = "\x1b[0;92m"

class Bokep:
	
	def __init__(self):
		self.a = ""
		
	def __jalan__(self, janda):
		for pepek in janda + "\n":
			sys.stdout.write(pepek)
			sys.stdout.flush()
			time.sleep(0.03)
			
	def __menu__(self):
		os.system("clear")
		print(f"""{H}   __  __ __  ____\n  /__)/ // / / _  )\n / _ \  _ \ / ___/\n/____/_/ \_\_/{P} v1\n""")
		print(f"{P}[ {H}Welcome Pengocox Handal{P} ]\n")
		print(f"{P}1. Bokep indo ({H}not vpn{P})")
		print(f"{P}2. Bokep japan ({H}use vpn{P})")
		print(f"{P}3. Bokep english ({H}use vpn{P})")
		print(f"{P}4. Download apk {H}xnxx{P}")
		print(f"{P}5. View link bokep terbaru")
		__nanya__ = input(f"\n{P}> Input : ")
		if __nanya__ == "1" or __nanya__ == "01":self.indo()
		elif __nanya__ == "2" or __nanya__ == "02":self.japan()
		elif __nanya__ == "3" or __nanya__ == "03":self.english()
		elif __nanya__ == "4" or __nanya__ == "04":self.download()
		elif __nanya__ == "5" or __nanya__ == "05":self.lihat()
		else:Bokep().__menu__()
		
	def indo(self):
		try:
			print(f"\n\n{P}[ {H}Kumpulan Bokep Indo{P} ]\n")
			print(f"{P}1. Bokep smp ({H}hanya menonton{P})")
			print(f"{P}2. Bokep sma ({H}hanya menonton{P})")
			print(f"{P}3. Bokep remaja ({H}bisa download{P})")
			print(f"{P}4. Bokep hijab ({H}bisa download{P})")
			print(f"{P}5. Bokep colmek ({H}hanya menonton{P})")
			ask = input(f"\n{P}> Input : ")
			if ask == "1":
				self.__jalan__(f"\n{P}!. Sedang masuk ke website ...")
				os.system("xdg-open https://bokepindo13.com/?s=smp");exit()
			elif ask == "2":
				self.__jalan__(f"\n{P}!. Sedang masuk ke website ...")
				os.system("xdg-open https://bokepindo13.com/?s=sma");exit()
			elif ask == "3":
				self.__jalan__(f"\n{P}!. Sedang masuk ke website ...")
				os.system("xdg-open https://itubokep.store/?s=abg");exit()
			elif ask == "4":
				self.__jalan__(f"\n{P}!. Sedang masuk ke website ...")
				os.system("xdg-open https://itubokep.store/?s=hijab+");exit()
			elif ask == "5":
				self.__jalan__(f"\n{P}!. Sedang masuk ke website ...")
				os.system("xdg-open https://linkbokep.me/?s=colmek");exit()
		except:pass

	def japan(self):
		try:
			print(f"\n\n{P}[ {H}Kumpulan Bokep Japan{P} ]\n")
			print(f"{P}1. Bokep japan school ({H}bisa download{P})")
			print(f"{P}2. Bokep japan family ({H}bisa download{P})")
			print(f"{P}3. Bokep japan random video ({H}bisa download{P})")
			ask = input(f"\n{P}> Input : ")
			if ask == "1":
				self.__jalan__(f"\n{P}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xvideos.com/?k=Japanese+school+");exit()
			elif ask == "2":
				self.__jalan__(f"\n{P}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xvideos.com/?k=Japanese+family");exit()
			elif ask == "3":
				self.__jalan__(f"\n{P}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xvideos.com/?k=Japanese%20teacher&top");exit()
			elif ask == "4":
				self.__jalan__(f"\n{P}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xvideos.com/?k=Japanese+hd");exit()
		except:pass
		
	def english(self):
		try:
			print(f"\n\n{P}[ {H}Kumpulan Bokep English{P} ]\n")
			print(f"{P}1. Bokep student & teacher ({H}bisa download{P})")
			print(f"{P}2. Bokep family sex ({H}bisa download{P})")
			print(f"{P}3. Bokep school party sex ({H}bisa download{P})")
			print(f"{P}4. Bokep public random ({H}bisa download{P})")
			print(f"{P}5. Bokep step mom ({H}bisa download{P})")
			print(f"{P}6. Bokep step sister ({H}bisa download{P})")
			ask = input(f"\n{P}> Input : ")
			if ask == "1":
				self.__jalan__(f"\n{P}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xnxx.com/search/English+student");exit()
			elif ask == "2":
				self.__jalan__(f"\n{P}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xnxx.com/search/English+family");exit()
			elif ask == "3":
				self.__jalan__(f"\n{P}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xnxx.com/search/student+party");exit()
			elif ask == "4":
				self.__jalan__(f"\n{P}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xnxx.com/search/public+agent");exit()
			elif ask == "5":
				self.__jalan__(f"\n{P}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xnxx.com/search/step+mom");exit()
			elif ask == "6":
				self.__jalan__(f"\n{P}!. Sedang masuk ke website ...")
				os.system("xdg-open https://www.xnxx.com/search/step%20sister?top");exit()
		except:pass
		
	def download(self):
		try:
			self.__jalan__(f"\n{P}!. Kamu akan diarahkan ke website")
			self.__jalan__(f"{P}!. Pencet Tulisan {H}Download the OFFICIAL XNXX APP (Stable){P}")
			os.system("xdg-open https://www.xnxx.net/");exit()
		except:pass

	def lihat(self):
		self.__jalan__(f"\n\n{P}[ {H}Kumpulan Link Bokep Random{P} ]\n");time.sleep(1)
		print(f"{P}> {H}https://jambulmemek.world");time.sleep(0.03)
		print(f"{P}> {H}https://ngentot.cam");time.sleep(0.03)
		print(f"{P}> {H}https://fakebokep.com");time.sleep(0.03)
		print(f"{P}> {H}https://bokepxxi.lol");time.sleep(0.03)
		print(f"{P}> {H}https://bokepviral.cam");time.sleep(0.03)
		print(f"{P}> {H}https://ngebokep.lol");time.sleep(0.03)
		print(f"{P}> {H}https://xjilbab.xyz");time.sleep(0.03)
		print(f"{P}> {H}https://agenbokep.xyz");time.sleep(0.03)
		print(f"{P}> {H}https://bokeh.top");time.sleep(0.03)
		print(f"{P}> {H}https://bokepin.pics");time.sleep(0.03)
		print(f"{P}> {H}https://bokep.pro");time.sleep(0.03)
		print(f"{P}> {H}https://xvideos.com");time.sleep(0.03)
		print(f"{P}> {H}https://playbokep.ws");time.sleep(0.03)
		print(f"{P}> {H}https://bokepep.me");time.sleep(0.03)
		print(f"{P}> {H}https://www.indo18.com");time.sleep(0.03)
		print(f"{P}> {H}https://linkbokep.cam");time.sleep(0.03)
		print(f"{P}> {H}https://vndevtop.com");time.sleep(0.03)
		print(f"{P}> {H}https://xbokepfb.com");time.sleep(0.03)
		print(f"{P}> {H}https://www.asexyporn.com");time.sleep(0.03)
		print(f"{P}> {H}https://pornkai.com");time.sleep(0.03)
		print(f"{P}> {H}https://bokepcrot.design");time.sleep(0.03)
		print(f"{P}> {H}https://m.spankbang.com");time.sleep(0.03)
		print(f"{P}> {H}https://www.eporner.com");time.sleep(0.03)
		print(f"{P}> {H}https://pornzog.com");time.sleep(0.03)
		print(f"{P}> {H}https://pestasex.cam/categories");time.sleep(0.03)
		print(f"{P}> {H}https://sangetods.net");time.sleep(0.03)
		print(f"{P}> {H}https://perawanbokep.site");time.sleep(0.03)
		print(f"{P}> {H}https://pwetan.com");time.sleep(0.03)
		print(f"{P}> {H}https://www.kontol.in");time.sleep(0.03)
		print(f"{P}> {H}https://malemjumat.lol");time.sleep(0.03)
		print(f"{P}> {H}https://brutalfucking.net/id/");time.sleep(0.03)
		print(f"{P}> {H}https://colmek.link/");time.sleep(0.03)
		self.__jalan__(f"\n{P}[ {H}Full Link Bokep Terbaru{P} ]");exit()
		

Bokep().__menu__()
