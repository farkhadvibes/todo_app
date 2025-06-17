# 📝 FRKHD - Современный менеджер задач / Modern Task Manager

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

**Красивый и функциональный менеджер задач с современным дизайном**

*Beautiful and functional task manager with modern design*

[🇷🇺 Русский](#-русская-версия) | [🇬🇧 English](#-english-version)

</div>

---

## 🇷🇺 Русская версия

### 📖 Описание

FRKHD - это современный менеджер задач, созданный на Python с использованием Tkinter. Приложение сочетает в себе простоту использования и мощный функционал для эффективного управления вашими делами.

### ✨ Основные возможности

- 🎨 **Современный дизайн** - Material Design интерфейс с тремя темами
- 🌍 **Многоязычность** - поддержка русского и английского языков
- 📂 **Категории задач** - 8 предустановленных категорий с иконками
- 🚩 **Приоритеты** - 4 уровня важности (низкий, средний, высокий, срочный)
- 📅 **Сроки выполнения** - установка дедлайнов для задач
- 🔍 **Поиск и фильтрация** - быстрый поиск по названию и описанию
- 📊 **Статистика** - подробная аналитика выполнения задач
- 💾 **Импорт/Экспорт** - сохранение данных в JSON, CSV, TXT форматах
- 🎯 **Модальные окна** - красивые диалоги с анимацией
- ⌨️ **Горячие клавиши** - быстрое управление с клавиатуры

### 🚀 Быстрый старт

#### Требования
- Python 3.7 или выше
- Операционная система: Windows, macOS, Linux

### 🎮 Как использовать

#### Создание задачи
1. Нажмите кнопку **"Новая задача"** или используйте `Ctrl+N`
2. Заполните название задачи (обязательно)
3. Добавьте описание (опционально)
4. Выберите категорию и приоритет
5. Установите срок выполнения при необходимости
6. Добавьте теги через запятую
7. Нажмите **"Сохранить"**

#### Управление задачами
- ✅ **Отметить выполненной** - кликните по чекбоксу
- ✏️ **Редактировать** - двойной клик по задаче или кнопка "Редактировать"
- 🗑️ **Удалить** - кнопка "Удалить" или клавиша `Delete`
- 🔍 **Найти** - используйте поле поиска или `Ctrl+F`

#### Фильтрация и сортировка
- Используйте выпадающие списки для фильтрации по категории, приоритету и статусу
- Сортируйте задачи по дате, названию, приоритету или сроку выполнения
- Кликайте по категориям в боковой панели для быстрой фильтрации

#### Смена темы и языка
- **Тема**: Меню → Вид → Тема → выберите светлую, темную или синюю
- **Язык**: Меню → Вид → Язык → выберите русский или английский

### ⌨️ Горячие клавиши

| Комбинация | Действие |
|------------|----------|
| `Ctrl+N` | Создать новую задачу |
| `Ctrl+F` | Фокус на поиске |
| `F5` | Обновить список задач |
| `Delete` | Удалить выбранную задачу |
| `Escape` | Закрыть диалоговое окно |
| `Enter` | Сохранить в диалоге |

### 📊 Статистика

Приложение автоматически ведет статистику:
- Общее количество задач
- Выполненные и активные задачи
- Просроченные задачи
- Статистика по категориям и приоритетам

### 💾 Импорт и экспорт

- **Экспорт**: Меню → Файл → Экспорт → выберите формат (JSON/CSV/TXT)
- **Импорт**: Меню → Файл → Импорт → выберите JSON файл

### 🎨 Темы

- **Светлая тема** - классический светлый интерфейс
- **Темная тема** - современный темный дизайн
- **Синяя тема** - стильная синяя цветовая схема

### 📁 Структура файлов

```
todo_app/
├── advanced_todo.py      # Основной файл приложения
├── requirements.txt      # Зависимости Python
├── settings.json        # Настройки приложения (создается автоматически)
├── advanced_tasks.json  # База данных задач (создается автоматически)
└── fonts/              # Папка со шрифтами
    ├── Mulish-Bold.ttf
    └── Mulish-Regular.ttf
```

### 🤝 Вклад в проект

Мы приветствуем вклад в развитие проекта! Если у вас есть идеи или вы нашли баг:

1. Создайте Fork репозитория
2. Создайте ветку для новой функции (`git checkout -b feature/amazing-feature`)
3. Зафиксируйте изменения (`git commit -m 'Add amazing feature'`)
4. Отправьте в ветку (`git push origin feature/amazing-feature`)
5. Создайте Pull Request

### 📝 Лицензия

Этот проект распространяется под лицензией MIT. Подробности в файле [LICENSE](LICENSE).

### 📞 Поддержка

Если у вас возникли вопросы или проблемы:
- Создайте Issue в GitHub
- Опишите проблему максимально подробно
- Приложите скриншоты если необходимо

---

## 🇬🇧 English Version

### 📖 Description

FRKHD is a modern task manager built with Python and Tkinter. The application combines ease of use with powerful functionality for efficient task management.

### ✨ Key Features

- 🎨 **Modern Design** - Material Design interface with three themes
- 🌍 **Multi-language** - Russian and English language support
- 📂 **Task Categories** - 8 preset categories with icons
- 🚩 **Priorities** - 4 importance levels (low, medium, high, urgent)
- 📅 **Due Dates** - Set deadlines for tasks
- 🔍 **Search & Filter** - Quick search by title and description
- 📊 **Statistics** - Detailed task completion analytics
- 💾 **Import/Export** - Save data in JSON, CSV, TXT formats
- 🎯 **Modal Windows** - Beautiful animated dialogs
- ⌨️ **Hotkeys** - Quick keyboard control

### 🚀 Quick Start

#### Requirements
- Python 3.7 or higher
- Operating System: Windows, macOS, Linux

### 🎮 How to Use

#### Creating a Task
1. Click the **"New Task"** button or use `Ctrl+N`
2. Fill in the task title (required)
3. Add description (optional)
4. Select category and priority
5. Set due date if needed
6. Add tags separated by commas
7. Click **"Save"**

#### Task Management
- ✅ **Mark as completed** - click the checkbox
- ✏️ **Edit** - double-click the task or click "Edit" button
- 🗑️ **Delete** - click "Delete" button or press `Delete` key
- 🔍 **Search** - use the search field or `Ctrl+F`

#### Filtering and Sorting
- Use dropdown lists to filter by category, priority, and status
- Sort tasks by date, title, priority, or due date
- Click categories in the sidebar for quick filtering

#### Theme and Language
- **Theme**: Menu → View → Theme → choose light, dark, or blue
- **Language**: Menu → View → Language → choose Russian or English

### ⌨️ Hotkeys

| Combination | Action |
|-------------|--------|
| `Ctrl+N` | Create new task |
| `Ctrl+F` | Focus on search |
| `F5` | Refresh task list |
| `Delete` | Delete selected task |
| `Escape` | Close dialog |
| `Enter` | Save in dialog |

### 📊 Statistics

The application automatically tracks statistics:
- Total number of tasks
- Completed and active tasks
- Overdue tasks
- Statistics by categories and priorities

### 💾 Import and Export

- **Export**: Menu → File → Export → choose format (JSON/CSV/TXT)
- **Import**: Menu → File → Import → select JSON file

### 🎨 Themes

- **Light Theme** - classic light interface
- **Dark Theme** - modern dark design
- **Blue Theme** - stylish blue color scheme

### 📁 File Structure

```
todo_app/
├── advanced_todo.py      # Main application file
├── requirements.txt      # Python dependencies
├── settings.json        # Application settings (auto-created)
├── advanced_tasks.json  # Task database (auto-created)
└── fonts/              # Fonts folder
    ├── Mulish-Bold.ttf
    └── Mulish-Regular.ttf
```

### 🤝 Contributing

We welcome contributions to the project! If you have ideas or found a bug:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Create a Pull Request

### 📝 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

### 📞 Support

If you have questions or issues:
- Create an Issue on GitHub
- Describe the problem in detail
- Attach screenshots if necessary

---

<div align="center">

**Сделано с ❤️ на Python | Made with ❤️ using Python**

⭐ **Поставьте звезду, если проект понравился! | Star if you like the project!** ⭐

</div> 
