import os
import sys

import pygame
import requests

class mapa:
    def __init__(self):
        self.x = 135
        self.y = 63
        self.spn = (3.0, 3.0)
        self.l = 'sat'
        self.params = {
            'll': str(self.x) + ',' + str(self.y),
            'l': str(self.l),
            'spn': str(self.spn[0]) + ',' + str(self.spn[1])
        }
        
    def request(self):
        search_api_server = 'https://static-maps.yandex.ru/1.x/'
        response = requests.get(search_api_server, params=self.params)
        if not response:
            print("Ошибка выполнения запроса:")
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
        print(11)
        return response
        
    def change_spn(self, x, y):
        if 0 <= x < 20 and 0 <= y < 20:
            self.spn = (x, y)
            self.params = {
                'll': str(self.x) + ',' + str(self.y),
                'l': str(self.l),
                'spn': str(self.spn[0]) + ',' + str(self.spn[1])
            }
            return self.request()
        print(self.spn)
        return 0
            
    def change_coord(self, way):
        if way == 0 and -170 < self.x < 170:
            self.x += self.spn[0]
        if way == 1 and -170 < self.x < 170:
            self.x -= self.spn[0]
        if way == 2 and -80 < self.y < 80:
            self.y -= self.spn[1]
        if way == 3 and -80 < self.y < 80:
            self.y += self.spn[1]
        self.params = {
            'll': str(self.x) + ',' + str(self.y),
            'l': str(self.l),
            'spn': str(self.spn[0]) + ',' + str(self.spn[1])
        }
        return self.request()

    
        



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

running = True
while running:
    # внутри игрового цикла ещё один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        x = 0
        if event.type == pygame.KEYDOWN:
            if event.key == 1073741902:
                x = map1.change_spn(map1.spn[0] - 1, map1.spn[1] - 1)
            if event.key == 1073741899:
                x = map1.change_spn(map1.spn[0] + 1, map1.spn[1] + 1)
            if event.key - 1073741903 in [0, 1, 2, 3]:
                x = map1.change_coord(event.key - 1073741903)
        if x == 0:
            pass
        else:
            with open(map_file, "wb") as file:
                file.write(x.content)
            
        screen.blit(pygame.image.load(map_file), (0, 0))
    # обновление экрана
        pygame.display.flip()
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
