#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

class Videojuegos:

	def __init__(self):
		with open('../src/videojuegos.json', 'r') as file:
			self.vg = json.load(file)

	def getVideojuego(self,idgame):
		if type(idgame) != int:
			return False

		try:
			idgame = abs(int(idgame))
			videojuego = self.vg["Videojuego"][idgame-1]["Nombre"]

		except:
			videojuego = False

		return videojuego

	def getVideojuegos(self):
		videojuegos = []

		try:
			for i in self.vg["Videojuego"]:
				videojuegos.append(i["Nombre"])
		except:
			videojuegos = False

		return videojuegos

	def aniadeVideojuego(self,nombre):
		if type(nombre) != str:
			return False

		try:
			self.vg["Videojuego"].append({'Nombre': nombre})
			with open('./videojuegos.json','w') as file:
				json.dump(self.vg, file)
			return True
		except ValueError:
			return False

	def encuentraVideojuego(self,nombre):
		if type(nombre) != str:
			return False

		cont = 0
		find = -1
		try:
			for i in self.vg["Videojuego"]:
				if i["Nombre"] == nombre:
					find = cont

				cont = cont + 1

			if find == -1:
				return False
			else:
				return find
		except:
			return False

	def borraVideojuego(self,nombre):
		if type(nombre) != str:
			return False

		idgame = self.encuentraVideojuego(nombre)
		if idgame != False:
			try:
				self.vg["Videojuego"].pop(idgame)
				with open('../src/videojuegos.json','w') as file:
					json.dump(self.vg, file)
				return True
			except:
				return False
		else:
			return False
