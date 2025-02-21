# Django Client Management System

Это веб-приложение для учета клиентов и их контактных данных. Проект написан на **Django** и предоставляет функциональность для добавления, редактирования, удаления клиентов и управления их контактной информацией.

## Технологии

- **Django**: Для серверной логики и взаимодействия с базой данных.
- **Bootstrap 5**: Для стилизации пользовательского интерфейса и адаптивной верстки.
- **Python 3.x**: Для работы с Django и серверной логики.
- **SQLite**: Используется как база данных по умолчанию.

## Требования

Перед тем как запустить проект, убедитесь, что у вас установлены следующие компоненты:

- **Python 3.x** (рекомендуется Python 3.8 и выше)
- **Pip**: Установите зависимости, используя pip.

## Установка и настройка

1. **Клонируйте репозиторий**:

   ```bash
   git clone <URL-репозитория>
   cd <папка проекта>
   ```

2. **Создайте и активируйте виртуальное окружение**:

Для Linux/macOS:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

Для Windows:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Установите зависимости:

Установите необходимые пакеты с помощью pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Настройте базу данных:

Сделайте миграции базы данных:

   ```bash
   python manage.py migrate
   ```

5. Запустите сервер разработки:

Для запуска локального сервера используйте команду:

   ```bash
   python manage.py runserver
   ```

## Структура проекта 

clients/: Главная директория с приложением для управления клиентами.
models.py: Модели данных для клиентов.
forms.py: Формы для добавления/редактирования клиентов.
views.py: Представления для работы с клиентами.
urls.py: Маршруты для страниц приложения.
templates/clients/: Шаблоны для отображения информации о клиентах.
templates/base.html: Основной шаблон с меню и навигацией.

## Использование
 
### Добавление клиента
1.Перейдите на страницу добавления клиента.
2.Заполните форму с информацией о клиенте: имя, email, телефон и (опционально) компания.
3.При добавлении клиента с уже существующим номером телефона появится ошибка, и данные не будут сохранены.

### Редактирование клиента
1.Перейдите на страницу редактирования клиента.
2.Измените необходимые данные и сохраните изменения.

### Удаление клиента
На странице клиента нажмите кнопку "Удалить" для удаления клиента.

### Просмотр списка клиентов
На главной странице отобразится список всех клиентов с возможностью просмотра, редактирования или удаления информации о них.