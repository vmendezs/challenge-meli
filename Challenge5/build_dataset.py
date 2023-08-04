# Creador: Valeria Mendez
# Fecha: 03 - Agosto - 2023

# In[Importe de librerías necesarias para acceder a la api]:

import pandas as pd
import sys
import requests

# In[Creacion de funcion para obtener items]:

def fetch_items(site):
    # Link de la url de la api
    url = f"https://api.mercadolibre.com/sites/{site}/search?q=tv%2&condition=new"
    
    # Lista en la que voy a almacenar toda la información de los items recolectados
    items = []
    
    # Obtener información de la api deshabilitando la verificación del certificado de acceso SSL
    response_api = requests.get(url, verify=False).json()
    
    # Obtener toda la información posible sobre la paginación "paging"
    # Total de items en la api:
    total_items = response_api['paging']['total']
    # Limite de items en la api por pagina:
    limit_per_page = response_api['paging']['limit']
    # Maximo valor de offset posible:
    max_possible_offset = 1000
    # Maximo valor de items necesarios (+/- 5mil según el enunciado)
    remaining_items_needed = min(5100, total_items)

    print("total_items:", total_items)
    print("limit_per_page:", limit_per_page)
    print("max_possible_offset:", max_possible_offset)
    print("remaining_items_needed:", remaining_items_needed)
    
    # Inicializo el minimo valor que puede tomar el offset para crear una especie de "paginacion"
    offset = 0
    
    # Creo un loop en el cual tengo el limite del valor del offset en 1000
    # Y tambien tengo en cuenta que los valores tienen que ser al menos 5100
    while offset < 1000 and remaining_items_needed > 0:
        # Determino que el limite de la pagina no excede el remaining_items_needed o limit_per_page
        limit = min(limit_per_page, remaining_items_needed)

        # Obtener información de la api deshabilitando la verificación del certificado de acceso SSL
        # Añadiendole información al api request del limite y offset sobre la paginacion
        response_api = requests.get(url + f"&limit={limit}" + f"&offset={offset}", verify=False).json()
        
        # Creación de loop para obtener todos los items disponibles dentro de la pagina
        # Y guardarlos en la lista llamada items juntos con los campos: id, title, price, domain, brand
        for item in response_api['results']:
            item_id = item['id']
            title = item['title']
            price = item['price']
            domain_id = item['domain_id']
            brand = item['attributes'][0]['value_name']
            # El enunciado indica que solo pueden ser items con condition = new por lo cual se realiza
            # el filtro correspondiente y de esa manera obtener solo los items nuevos
            #if item['condition'] == "new":
            items.append({
                'ITEM_ID': item_id,
                'TITLE': title,
                'PRICE': price,
                'DOMAIN_ID': domain_id,
                'BRAND': brand
            })
                
            # Decrecer el the remaining_items_needed que empezo en 5100 hasta llegar a 0
            remaining_items_needed -= 1
            
            # Finalizar el loop cuando el tamaño de items este entre 4900 y 5100 items            
            if len(items) >= 4900 and len(items) <= 5100:  
                return items
        # print("offset:", offset)
        # print("limit:", limit)
        
        # Incrementar el offset hasta donde el limite de la pagina lo permita
        offset += limit  

    return items

# In[4]:
    
def main():
    # Compruebo si el número de argumentos en la línea de comandos es diferente de 2
    # Si no es igual a 2, muestra el mensaje de uso correcto y termina el codigo.
    if len(sys.argv) != 2:
        print("Uso del llamado debe ser: python build_dataset.py SITE")
        return
    
    # Si es igual a 2, ingreso el valor del segundo argumento de la línea del cmd (site)
    # y lo asigna a la variable site.
    site = sys.argv[1]
    
    # Verifico que el valor de site este en la lista
    # Si no esta en la lista, muestro el mensaje del uso correcto y termino el codigo
    if site not in ["MLA", "MLB", "MLM"]:
        print("SITE invalido. Vuelva a intentar con alguno de estos valores : MLA, MLB, MLM")
        return
    
    # Si encuentra el site en la lista, llamo a la funcion fetch_items para que empiece
    # a realizar la busqueda de todos los items disponibles con las condiciones
    # y caracteristicas necesarias de acuerdo al site especificado
    items = fetch_items(site)
    
    # Verifico si items esta vacio, muestra el mensaje y termina el codigo
    if not items:
        print("No hay items disponibles en esta api")
        return
    
    # Convierto la lista de items en un dataframe
    df = pd.DataFrame(items)
    
    # Guardo el dataframe como dataset.csv e imprimo que fue creado el dataset
    df.to_csv("dataset.csv", index=False)
    print("Dataset creado")


# In[Realizo el llamado de la funcion main que contiene el menu]:

if __name__ == "__main__":
    main()
