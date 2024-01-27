ДЗ от 22.12.23
Создайте абстрактный класс Книга, принимающий атрибуты title, author, genre при создании экземпляра
определите абстрактный метод show_info для отображения информации о книге
Создайте подклассы Science, Adventure, Detective,Poetry выберите реальные книги и добавьте им соответствующие значения
в атрибуты title,author,genre
import abc
class AbstractBook(abc.ABC):
    def __init__(self,title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    @abc.abstractmethod
    def show_info(self):
        raise NotImplementedError('Нельзя вызывать абстрактный метод, переопределите его')

class Science(AbstractBook):
    def show_info(self):
        return f"{self.author}: \"{self.title}\" [{self.genre}]"

class Poetry(AbstractBook):
    def show_info(self):
        return f"~~~~~~~~ {self.title} ~~~~~~~~\n\t\t\t{self.genre}\n\t\t{self.author}"

hoking = Science('Краткая история времени','Стивен хокнинг','Научная литература')
pushkin = Poetry('Лучшие стихи','Александр Пушкин','Поэзия')
print(hoking.show_info())
print(pushkin.show_info())
