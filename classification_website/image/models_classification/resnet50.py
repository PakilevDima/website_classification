from torchvision import models
from PIL import Image
class ResNet50:
    '''
    Объект представляет собой модель для классификации изображения с помощью модели ResNet50
    '''
    def __init__(self):
        super().__init__()

        self.resnet_weights = models.ResNet50_Weights.DEFAULT       # подгрузка весов в отдельную переменную
        self.model = models.resnet50(weights=self.resnet_weights)   # подгрузка весов для модели
        self.cats = self.resnet_weights.meta['categories']          # классы для классификации
        self.transforms = self.resnet_weights.transforms()          # трансформации к входному сигналу
        self.model.eval()                                           # перевод модели в рабочее состояние
    def image_classification(self, path: str) -> dict:        # для классификации изображений. path - путь к файлу
        '''
        Метод для непосредственно классификации изображения.
        Передается path - путь к файлу для классификации
        Возвращается словарь в формате {название класса: вероятность этого класса}
        '''
        img = Image.open(path).convert('RGB')                       # подгрузка изображения в формате RGB
        img_net = self.transforms(img).unsqueeze(0)                 # применение трансформаций к изображению

        p = self.model(img_net).squeeze()                           # удаляем первую ось, которую мы сделали чуть ранее
        res = p.softmax(dim=0).sort(descending=True)                # интерпретация данных, полученных моделью
        the_most_likely_options = {}                                # создание словаря для
        for s, i in zip(res[0][:5], res[1][:5]):                    # перебор наиболее вероятных исходов
            the_most_likely_options[self.cats[i]] = f"{s:.4f}"      # запись в словарь

        return the_most_likely_options  # возврат значения