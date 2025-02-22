from torchvision import models       # импорт моделей
from PIL import Image         # импорт библиотеки для работы с изображениями


class Vgg16:                 # создание класса модели
    '''
    Объект представляет собой модель для классификации изображения с помощью модели Vgg16
    '''
    def __init__(self):      # инициализация класса
        super().__init__()

        self.vgg16 = models.vgg16(weights='DEFAULT')         # подгрузка весов для модели
        self.vgg_weights = models.VGG16_Weights.DEFAULT      # подгрузка весов в отдельную переменную
        self.transforms_1 = self.vgg_weights.transforms()    # трансформации к входному сигналу
        self.cats = self.vgg_weights.meta['categories']      # классы для классификации
        self.vgg16.eval()                                    # перевод модели в рабочее состояние

    def image_classification(self, path: str) -> dict:       # для классификации изображений. path - путь к файлу
        '''
        Метод для непосредственно классификации изображения.
        Передается path - путь к файлу для классификации
        Возвращается словарь в формате {название класса: вероятность этого класса}
        '''

        img = Image.open(path).convert('RGB')           # подгрузка изображения в формате RGB
        img_net = self.transforms_1(img).unsqueeze(0)   # применение трансформаций к изображению

        p = self.vgg16(img_net).squeeze()               # удаляем первую ось, которую мы сделали чуть ранее
        res = p.softmax(dim=0).sort(descending=True)    # интерпретация данных, полученных моделью
        the_most_likely_options = {}                    # создание словаря для
        for s, i in zip(res[0][:5], res[1][:5]):        # перебор наиболее вероятных исходов
            the_most_likely_options[self.cats[i]] = f"{s:.4f}"        # запись в словарь

        return the_most_likely_options    # возврат значения

