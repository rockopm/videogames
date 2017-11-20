import numpy as np
import pandas as pd
import urllib2 as ul   # https://docs.python.org/2/library/urllib2.html
# import requests as req


# Para revisar el catalogo completo de video-juegos no usados
# 'https://gameplanet.com/catalogo/video-juegos/condici%C3%B3n/nuevo.html'
# 'https://gameplanet.com/catalogo/video-juegos/software/condici%C3%B3n/nuevo.html'
# Para la pag-esima pagina de video-juegos no usados
# 'https://gameplanet.com/catalogo/video-juegos/condici%C3%B3n/nuevo/page/' + str(pag) + '.html'



# Obtiene el codigo html de la "url" (:str)
def get_code(url) :

    # Busca el codigo html de la pagina
    code = ul.urlopen(url).readlines()
    code = [x.strip() for x in code]
    code = ''.join(code)

    # Regresa el codigo obtenido
    return code




# Obtiene el numero total de paginas en el catalogo
num_paginas = 164 # 164 paginas de videojuegos no usados


def game_title(code, index) :

    # Para buscar el nombre del juego
    look_name_beg = '<h2 class="product-name lista-title">'
    look_name_end = '</h2>'

    # Busca el substring en donde se encuentra el nombre
    start = code.find(look_name_beg, index)
    end = code.find(look_name_end, start + 1)
    substring = code[start:end]

    # Busca el nombre dentro del substring
    look_name_beg_ss = 'title="'
    look_name_end_ss = '">'
    start_ss = substring.find(look_name_beg_ss)
    end_ss = substring.find(look_name_end_ss, substring.find(look_name_beg_ss))

    # Asigna el titulo del juego ( len(title=) = 7 )
    return substring[(start_ss + len(look_name_beg_ss)):end_ss].strip()




def game_console(code, index) :

    # Para buscar el nombre del juego
    look_cons_beg = "<span class='att_plat_contenedor'>"
    look_cons_end = '</span>'

    # Busca el substring en donde se encuentra el nombre
    start = code.find(look_cons_beg, index)
    end = code.find(look_cons_end, start + 1)
    substring = code[start:end]

    # Busca el nombre dentro del substring
    look_cons_beg_ss = '<strong>'
    look_cons_end_ss = '</strong>'
    start_ss = substring.find(look_cons_beg_ss)
    end_ss = substring.find(look_cons_end_ss, substring.find(look_cons_beg_ss))

    # Asigna el titulo del juego ( len(title=) = 7 )
    return substring[(start_ss + len(look_cons_beg_ss)):end_ss].strip()





def game_upc(code, index) :

    # Para buscar el nombre del juego
    look_upc_beg = '<div class="detalles-producto-catalogo detalles-container">'
    look_upc_end = '</div>'

    # Busca el substring en donde se encuentra el nombre
    start = code.find(look_upc_beg, index)
    end = code.find(look_upc_end, start + len(look_upc_beg))
    substring = code[start:end]

    # Busca el nombre dentro del substring
    look_upc_beg_ss = '<strong>UPC</strong>&nbsp;&nbsp;&nbsp;'
    look_upc_end_ss = '<br>'
    start_ss = substring.find(look_upc_beg_ss)
    end_ss = substring.find(look_upc_end_ss, substring.find(look_upc_beg_ss))

    # Asigna el titulo del juego ( len(title=) = 7 )
    return substring[(start_ss + len(look_upc_beg_ss)):end_ss].strip()





def game_genero(code, index) :

    # Para buscar el nombre del juego
    look_gen_beg = '<div class="detalles-producto-catalogo detalles-container">'
    look_gen_end = '</div>'

    # Busca el substring en donde se encuentra el nombre
    start = code.find(look_gen_beg, index)
    end = code.find(look_gen_end, start + len(look_gen_beg))
    substring = code[start:end]

    # Busca el nombre dentro del substring
    look_gen_beg_ss = '<strong>Género</strong>&nbsp;&nbsp;&nbsp;'
    look_gen_end_ss = '<br>'
    start_ss = substring.find(look_gen_beg_ss)
    end_ss = substring.find(look_gen_end_ss, substring.find(look_gen_beg_ss))

    # Asigna el titulo del juego ( len(title=) = 7 )
    return substring[(start_ss + len(look_gen_beg_ss)):end_ss].strip()





def game_lanz(code, index) :

    # Para buscar el nombre del juego
    look_lanz_beg = '<div class="detalles-producto-catalogo detalles-container">'
    look_lanz_end = '</div>'

    # Busca el substring en donde se encuentra el nombre
    start = code.find(look_lanz_beg, index)
    end = code.find(look_lanz_end, start + len(look_lanz_beg))
    substring = code[start:end]

    # Busca el nombre dentro del substring
    look_gen_beg_ss = '<strong>Lanzamiento</strong>&nbsp;&nbsp;&nbsp;'
    look_gen_end_ss = '<br>'
    start_ss = substring.find(look_gen_beg_ss)
    end_ss = substring.find(look_gen_end_ss, substring.find(look_gen_beg_ss))

    # Asigna el titulo del juego ( len(title=) = 7 )
    return substring[(start_ss + len(look_gen_beg_ss)):end_ss].strip()






# Inicializa arrays en donde guardar datos
ar_upc = []
ar_title = []
ar_gen = []
ar_cons = []
ar_lanz = []

# Ejecuta para todas las páginas
for currpag in range(1, 165) : 
#range(1, 164) :
    print currpag

    # Obtiene el titulo del juego
    ss_feat = '<div class="detalles-producto-catalogo detalles-container">'
    ss_title = '<h2 class="product-name lista-title">'
    ss_cons = "<span class='att_plat_contenedor'>"

    if currpag == 1 :
        # Obtiene la url adecuada para np
        url = 'https://gameplanet.com/catalogo/video-juegos/software/condici%C3%B3n/nuevo.html'
        # Obtiene el codigo adecuado para np
        page_code = get_code(url)
        # Numero de juegos en la pagina
        num_games_in_page = page_code.count(ss_title)
        # Inicializa el indice de busqueda
        index_upc = 0
        index_title = 0
        index_gen = 0
        index_cons = 0
        index_lanz = 0

        for n_game in range(1, num_games_in_page + 1) :
            ar_upc.append(game_upc(page_code, index_upc))
            ar_title.append(game_title(page_code, index_title))
            ar_gen.append(game_genero(page_code, index_gen))
            ar_cons.append(game_console(page_code, index_cons))
            ar_lanz.append(game_lanz(page_code, index_lanz))
            
            index_upc = page_code.find(ss_feat, index_upc) + len(ss_feat)
            index_title = page_code.find(ss_title, index_title) + len(ss_title)
            index_gen = page_code.find(ss_feat, index_gen) + len(ss_feat)
            index_cons = page_code.find(ss_cons, index_cons) + len(ss_cons)
            index_lanz = page_code.find(ss_feat, index_lanz) + len(ss_feat)
            

    else :
        # Obtiene la url adecuada para np
        url = 'https://gameplanet.com/catalogo/video-juegos/software/condici%C3%B3n/nuevo/page/' + str(currpag) + '.html'
        # Obtiene el codigo adecuado para np
        page_code = get_code(url)
        # Numero de juegos en la pagina
        num_games_in_page = page_code.count(ss_title)
        # Inicializa el indice de busqueda
        index_upc = 0
        index_title = 0
        index_gen = 0
        index_cons = 0
        index_lanz = 0

        for n_game in range(1, num_games_in_page + 1) :
            ar_upc.append(game_upc(page_code, index_upc))
            ar_title.append(game_title(page_code, index_title))
            ar_gen.append(game_genero(page_code, index_gen))
            ar_cons.append(game_console(page_code, index_cons))
            ar_lanz.append(game_lanz(page_code, index_lanz))
            
            index_upc = page_code.find(ss_feat, index_upc) + len(ss_feat)
            index_title = page_code.find(ss_title, index_title) + len(ss_title)
            index_gen = page_code.find(ss_feat, index_gen) + len(ss_feat)
            index_cons = page_code.find(ss_cons, index_cons) + len(ss_cons)
            index_lanz = page_code.find(ss_feat, index_lanz) + len(ss_feat)



# Crea dataframe con datos
upc = pd.Series(ar_upc)
title = pd.Series(ar_title)
genero = pd.Series(ar_gen)
consola = pd.Series(ar_cons)
lanzamiento = pd.Series(ar_lanz)

cat_juegos = pd.DataFrame({'upc' : upc,
              'titulo' : title,
              'genero' : genero,
              'consola' : consola,
              'lanzamiento' : lanzamiento})


    
# Exporta a un csv
cat_juegos.to_csv('/home/rockopm/Documents/datasets/cat_videojuegos.csv', index=False)
