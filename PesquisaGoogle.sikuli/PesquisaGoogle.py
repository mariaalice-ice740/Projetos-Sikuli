# -*- coding: utf-8 -*-
"""
Desafio Abrir o navegador e pesquisar no Google
Abra o Google Chrome.
Va ate o site do Google.
Digite a pesquisa
Python com Sikuli
Pressione Enter para ver os resultados.
"""

doubleClick("atalho_chrome.png")
click("maximizar.png")
click("barra_pesquisa.png")
type("Python com Sikuli")
type(Key.ENTER)



