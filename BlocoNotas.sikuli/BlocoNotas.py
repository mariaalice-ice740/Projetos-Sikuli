"""
Desafio: Abrir o Bloco de Notas e digitar uma mensagem
Abra o Bloco de Notas (ou qualquer editor de texto simples) usando o Sikuli.
Digite a mensagem:
Olá, estou aprendendo Python com Sikuli!
Salve o arquivo com o nome teste.txt na sua área de trabalho.
"""
# -*- coding: utf-8 -*-

doubleClick("1759074562137.png")
wait("1759075621847.png")
click("1759075009412.png")
type("Oi, estou aprendendo Python com Sikuli!")
type("s", Key.CTRL)
wait("1759075481157.png")
type("TesteSikuli.txt")
click("1759075524825.png")


