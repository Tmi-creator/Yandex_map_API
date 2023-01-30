import os
import sys

import pygame
import requests

class mapa:
    def __init__(self):
        self.x = 135
        self.y = -27
        self.z = 4
        self.l = 'sat'
        self.params = {
            'll': str(self.x) + ',' + str(self.y),
            'z': str(self.z),
            'l': str(self.l)
        }
        
    def request(self):
        search_api_server = 'https://static-maps.yandex.ru/1.x/'
        response = requests.get(search_api_server, params=self.params)
        if not response:
            print("Ошибка выполнения запроса:")
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
        return response
        



map1 = mapa()


# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(map1.request().content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
