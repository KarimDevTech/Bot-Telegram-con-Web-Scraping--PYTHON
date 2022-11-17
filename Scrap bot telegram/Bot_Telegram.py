from bs4 import BeautifulSoup
import requests
import time
import webbrowser

#Traer la direccion de la pagina de la cual quiero la informacion
url = requests.get("https://articulo.mercadolibre.com.ar/MLA-896435545-alpargata-clasica-reforzada-simil-yute-toro-y-pampa-_JM#backend=item_decorator&backend_type=function&client=bookmarks-polycard")


soup = BeautifulSoup(url.content, "html.parser")

resultado = soup.find("span", {"class":"andes-money-amount__fraction"})
precioInicio_text = resultado.text
precioInicial = float(precioInicio_text)
precioDeseado = 1.700


#Función que se inicializa si el precio del producto esta en el rango deseado
def telegram_bot_sendtext(bot_message):
    
    bot_token = '5653725613:AAGXOmbAGQdQar0_2k1nLYJphnysJY1-z7k'
    bot_chatID = '0000000' #Aca va el chat ID de telegram que por motivos de privacidad no lo pongo
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    
if precioInicial <= precioDeseado:
    test = telegram_bot_sendtext(f"HAY REBAJA, el precio esta en: {'$'+ str(precioInicial)}\nApurate Karim, te dejo el link\n https://articulo.mercadolibre.com.ar/MLA-896435545-alpargata-clasica-reforzada-simil-yute-toro-y-pampa-_JM#backend=item_decorator&backend_type=function&client=bookmarks-polycard")


