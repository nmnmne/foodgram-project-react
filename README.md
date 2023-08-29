# Проект "FoodGram"

Проект "FoodGram" - это веб-приложение, разработанное для помощи пользователям в поиске, сохранении и организации их любимых рецептов. Оно позволяет пользователям искать рецепты, добавлять их в избранное и создавать список покупок на основе выбранных рецептов.

## Особенности

- Просмотр и поиск рецептов.
- Добавление рецептов в избранное.
- Создание списка покупок на основе выбранных рецептов.
- Загрузка списка покупок в формате TXT.
- Аутентификация и авторизация пользователей.
- API-точки доступа для взаимодействия с приложением программным способом.

## API-точки доступа
Приложение предоставляет API-точки доступа для программного взаимодействия. Ниже представлены некоторые из доступных точек доступа:

`/api/recipes/`: Список рецептов.
`/api/recipes/<int:pk>/`: Детали конкретного рецепта.
`/api/recipes/<int:pk>/favorite/`: Добавление или удаление рецепта из избранного.
`/api/recipes/<int:pk>/shopping_cart/`: Добавление или удаление рецепта из корзины покупок.
`/api/recipes/download_shopping_cart/`: Загрузка корзины покупок в формате TXT.
`/api/docs/redoc.html`:Для получения более подробной информации о точках доступа API.

## Содействие
Приветствуются ваши вклады! Чтобы внести вклад в проект "FoodGram", выполните следующие шаги:

Форкните репозиторий.
Создайте новую ветку для своей функции или исправления багов: `git checkout -b имя-функции`.
Зафиксируйте свои изменения: `git commit -m "Добавление новой функции"`.
Отправьте изменения в свой форк: `git push origin имя-функции`.
Создайте запрос на включение изменений в основной репозиторий.
