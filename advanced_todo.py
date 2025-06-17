
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser, font
from datetime import datetime, timedelta
import json
import os
import re
from collections import defaultdict
import webbrowser
import sys
import platform
def load_fonts():
    
    import os
    system = platform.system()
    fonts_dir = os.path.join(os.path.dirname(__file__), 'fonts')
    if os.path.exists(fonts_dir):
        try:
            if system == 'Windows':
                import ctypes
                from ctypes import wintypes
                gdi32 = ctypes.WinDLL('gdi32')
                AddFontResourceEx = gdi32.AddFontResourceExW
                AddFontResourceEx.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.LPVOID]
                AddFontResourceEx.restype = ctypes.c_int
                for font_file in os.listdir(fonts_dir):
                    if font_file.endswith(('.ttf', '.otf')):
                        font_path = os.path.join(fonts_dir, font_file)
                        AddFontResourceEx(font_path, 0x10, 0)
                        print(f"Зарегистрирован шрифт: {font_file}")
        except Exception as e:
            print(f"Ошибка регистрации шрифтов: {e}")
    font_families = {
        'primary': ['Mulish', 'Inter', 'SF Pro Display', 'Segoe UI Variable', 'Segoe UI', 'Arial'],
        'secondary': ['Mulish', 'Source Sans Pro', 'Open Sans', 'Roboto', 'Helvetica Neue', 'Arial'],
        'accent': ['Mulish', 'Montserrat', 'Poppins', 'Nunito', 'Raleway', 'Segoe UI Semibold']
    }
    available_fonts = font.families()
    selected_fonts = {}
    for font_type, fonts_list in font_families.items():
        for font_name in fonts_list:
            if font_name in available_fonts:
                selected_fonts[font_type] = font_name
                print(f"Выбран шрифт {font_type}: {font_name}")
                break
        else:
            if system == 'Windows':
                selected_fonts[font_type] = 'Segoe UI'
            elif system == 'Darwin':
                selected_fonts[font_type] = 'SF Pro Display'
            else:
                selected_fonts[font_type] = 'Ubuntu'
    return selected_fonts
FONTS = {}
ICONS = {
    'add': '➕',
    'edit': '✏️', 
    'delete': '🗑️',
    'refresh': '🔄',
    'save': '💾',
    'search': '🔍',
    'filter': '🔽',
    'sort': '📊',
    'check': '✅',
    'clock': '⏰',
    'warning': '⚠️',
    'fire': '🔥',
    'star': '⭐',
    'flag': '🚩',
    'work': '💼',
    'home': '🏠', 
    'study': '📚',
    'health': '🏥',
    'shopping': '🛒',
    'entertainment': '🎮',
    'sport': '⚽',
    'travel': '✈️',
    'menu': '☰',
    'settings': '⚙️',
    'info': 'ℹ️',
    'help': '❓',
    'close': '✖️',
    'minimize': '➖',
    'maximize': '⬜',
    'calendar': '📅',
    'tag': '🏷️',
    'folder': '📁',
    'chart': '📈',
    'export': '📤',
    'import': '📥',
    'sync': '🔄',
    'backup': '📦',
    'analytics': '📊',
    'clean': '🧹',
    'category': '📂'
}
THEMES = {
    'light': {
        'bg': '#f8fafc',
        'card_bg': '#ffffff',
        'sidebar_bg': '#ffffff',
        'header_bg': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'primary': '#667eea',
        'primary_light': '#7c3aed',
        'primary_dark': '#5b21b6',
        'secondary': '#64748b',
        'success': '#10b981',
        'success_light': '#34d399',
        'warning': '#f59e0b',
        'warning_light': '#fbbf24',
        'danger': '#ef4444',
        'danger_light': '#f87171',
        'info': '#3b82f6',
        'info_light': '#60a5fa',
        'text': '#1e293b',
        'text_muted': '#64748b',
        'text_light': '#ffffff',
        'border': '#e2e8f0',
        'shadow': '#e2e8f0',
        'hover': '#f1f5f9',
        'accent': '#8b5cf6',
        'gradient_start': '#667eea',
        'gradient_end': '#764ba2',
        'modal_overlay': '#000000',
        'glass': '#f8fafc'
    },
    'dark': {
        'bg': '#0f172a',
        'card_bg': '#1e293b',
        'sidebar_bg': '#1e293b',
        'header_bg': 'linear-gradient(135deg, #1e293b 0%, #334155 100%)',
        'primary': '#8b5cf6',
        'primary_light': '#a78bfa',
        'primary_dark': '#7c3aed',
        'secondary': '#64748b',
        'success': '#10b981',
        'success_light': '#34d399',
        'warning': '#f59e0b',
        'warning_light': '#fbbf24',
        'danger': '#ef4444',
        'danger_light': '#f87171',
        'info': '#3b82f6',
        'info_light': '#60a5fa',
        'text': '#f8fafc',
        'text_muted': '#94a3b8',
        'text_light': '#ffffff',
        'border': '#334155',
        'shadow': '#1e293b',
        'hover': '#334155',
        'accent': '#8b5cf6',
        'gradient_start': '#8b5cf6',
        'gradient_end': '#3b82f6',
        'modal_overlay': '#000000',
        'glass': '#1e293b'
    },
    'blue': {
        'bg': '#ebf4ff',
        'card_bg': '#ffffff',
        'sidebar_bg': '#dbeafe',
        'header_bg': '#ffffff',
        'primary': '#1e40af',
        'primary_light': '#3b82f6',
        'primary_dark': '#1e3a8a',
        'secondary': '#64748b',
        'success': '#059669',
        'success_light': '#10b981',
        'warning': '#d97706',
        'warning_light': '#f59e0b',
        'danger': '#dc2626',
        'danger_light': '#ef4444',
        'info': '#0284c7',
        'info_light': '#0ea5e9',
        'text': '#1e3a8a',
        'text_muted': '#64748b',
        'text_light': '#ffffff',
        'border': '#bfdbfe',
        'shadow': '#dbeafe',
        'hover': '#f0f9ff',
        'accent': '#1d4ed8',
        'gradient_start': '#1e40af',
        'gradient_end': '#1e3a8a'
    }
}
PRIORITIES = {
    'low': {'name': 'Низкий', 'color': '#10b981', 'icon': '🟢'},
    'medium': {'name': 'Средний', 'color': '#f59e0b', 'icon': '🟡'},
    'high': {'name': 'Высокий', 'color': '#ef4444', 'icon': '🔴'},
    'urgent': {'name': 'Срочный', 'color': '#dc2626', 'icon': '🚨'}
}
CATEGORIES = [
    {'name': f"{ICONS['work']} Работа", 'color': '#3b82f6', 'icon': ICONS['work'], 'gradient': '#60a5fa'},
    {'name': f"{ICONS['home']} Дом", 'color': '#10b981', 'icon': ICONS['home'], 'gradient': '#34d399'},
    {'name': f"{ICONS['study']} Учеба", 'color': '#f59e0b', 'icon': ICONS['study'], 'gradient': '#fbbf24'},
    {'name': f"{ICONS['health']} Здоровье", 'color': '#ef4444', 'icon': ICONS['health'], 'gradient': '#f87171'},
    {'name': f"{ICONS['shopping']} Покупки", 'color': '#8b5cf6', 'icon': ICONS['shopping'], 'gradient': '#a78bfa'},
    {'name': f"{ICONS['entertainment']} Развлечения", 'color': '#06b6d4', 'icon': ICONS['entertainment'], 'gradient': '#22d3ee'},
    {'name': f"{ICONS['sport']} Спорт", 'color': '#84cc16', 'icon': ICONS['sport'], 'gradient': '#a3e635'},
    {'name': f"{ICONS['travel']} Путешествия", 'color': '#f97316', 'icon': ICONS['travel'], 'gradient': '#fb923c'}
]
SORT_OPTIONS_RU = {
    'Дата создания': 'created_at',
    'Название': 'title', 
    'Приоритет': 'priority',
    'Срок выполнения': 'due_date',
    'Категория': 'category'
}
ORDER_OPTIONS_RU = {
    'По возрастанию': False,
    'По убыванию': True
}

LANGUAGES = {
    'ru': {
        'app_title': 'FRKHD',
        'app_subtitle': 'Современный менеджер задач',
        'new_task': 'Новая задача',
        'refresh': 'Обновить',
        'quick_search': 'Быстрый поиск:',
        'category': 'Категория:',
        'priority': 'Приоритет:',
        'status': 'Статус:',
        'all': 'Все',
        'active': 'Активные',
        'completed': 'Выполненные',
        'overdue': 'Просроченные',
        'control_panel': 'Панель управления',
        'quick_actions': 'Быстрые действия',
        'create_task': 'Создать задачу',
        'analytics': 'Аналитика',
        'sync': 'Синхронизация',
        'clear_completed': 'Очистить выполненные',
        'backup': 'Резервная копия',
        'categories': 'Категории',
        'statistics': 'Статистика',
        'total': 'Всего',
        'pending': 'Осталось',
        'task_list': 'Список задач',
        'sort_by': 'Сортировка:',
        'created_date': 'Дата создания',
        'title': 'Название',
        'due_date': 'Срок выполнения',
        'ascending': 'По возрастанию',
        'descending': 'По убыванию',
        'no_tasks_title': 'Задач пока нет',
        'no_tasks_subtitle': 'Создайте первую задачу чтобы начать работу',
        'create_first_task': 'Создать первую задачу',
        'task_title': 'Название задачи *',
        'description': 'Описание',
        'set_due_date': 'Установить срок',
        'tags': 'Теги (через запятую)',
        'save': 'Сохранить',
        'cancel': 'Отмена',
        'edit_task': 'Редактировать задачу',
        'add_task': 'Новая задача',
        'edit': 'Редактировать',
        'delete': 'Удалить',
        'confirm': 'Подтверждение',
        'delete_task_confirm': 'Удалить задачу',
        'success': 'Успех',
        'task_deleted': 'Задача удалена!',
        'task_created': 'создана',
        'task_updated': 'обновлена',
        'error': 'Ошибка',
        'enter_task_title': 'Введите название задачи!',
        'invalid_date_format': 'Неверный формат даты! Используйте: ГГГГ-ММ-ДД ЧЧ:ММ',
        'clear_completed_confirm': 'Очистить все выполненные задачи?',
        'no_completed_tasks': 'Нет выполненных задач для удаления.',
        'tasks_cleared': 'задач удалено!',
        'menu_file': 'Файл',
        'menu_edit': 'Правка',
        'menu_view': 'Вид',
        'menu_help': 'Справка',
        'menu_export': 'Экспорт...',
        'menu_import': 'Импорт...',
        'menu_exit': 'Выход',
        'menu_find': 'Найти',
        'menu_clear_filters': 'Очистить фильтры',
        'menu_light_theme': 'Светлая тема',
        'menu_dark_theme': 'Темная тема',
        'menu_blue_theme': 'Синяя тема',
        'menu_language': 'Язык',
        'menu_russian': 'Русский',
        'menu_english': 'English',
        'menu_statistics': 'Статистика',
        'menu_shortcuts': 'Горячие клавиши',
        'menu_about': 'О программе',
        'theme_changed': 'Тема изменена',
        'theme_applied': 'Применена тема:',
        'language_changed': 'Язык изменен',
        'language_applied': 'Применен язык:',
        'detailed_statistics': 'Подробная статистика',
        'category_stats': 'Статистика по категориям:',
        'priority_stats': 'Статистика по приоритетам:',
        'export_success': 'Задачи экспортированы в',
        'export_error': 'Не удалось экспортировать:',
        'import_confirm': 'Импортировать',
        'import_success': 'Задачи импортированы!',
        'import_error': 'Не удалось импортировать:',
        'shortcuts_title': 'Горячие клавиши',
        'shortcuts_text': '''⌨️ Горячие клавиши

Ctrl+N - Новая задача
Ctrl+F - Поиск
F5 - Обновить список
Delete - Удалить выбранную задачу
Escape - Закрыть диалог
Enter - Сохранить в диалоге

🖱️ Мышь

Правый клик - Контекстное меню
Двойной клик - Редактировать задачу
Колесо мыши - Прокрутка списка''',
        'about_title': 'О программе',
        'about_text': '''📝 FRKHD - Современный менеджер задач

Версия: 2.0
Дата: 2024

Функции:
• Создание и редактирование задач
• Категории и приоритеты
• Сроки выполнения
• Фильтрация и поиск
• Экспорт/импорт данных
• Настраиваемые темы
• Подробная статистика

Сделано с ❤️ на Python + tkinter''',
        'categories_list': [
            f"{ICONS['work']} Работа",
            f"{ICONS['home']} Дом", 
            f"{ICONS['study']} Учеба",
            f"{ICONS['health']} Здоровье",
            f"{ICONS['shopping']} Покупки",
            f"{ICONS['entertainment']} Развлечения",
            f"{ICONS['sport']} Спорт",
            f"{ICONS['travel']} Путешествия"
        ],
        'priorities_list': {
            'low': 'Низкий',
            'medium': 'Средний', 
            'high': 'Высокий',
            'urgent': 'Срочный'
        }
    },
    'en': {
        'app_title': 'FRKHD',
        'app_subtitle': 'Modern Task Manager',
        'new_task': 'New Task',
        'refresh': 'Refresh',
        'quick_search': 'Quick search:',
        'category': 'Category:',
        'priority': 'Priority:',
        'status': 'Status:',
        'all': 'All',
        'active': 'Active',
        'completed': 'Completed',
        'overdue': 'Overdue',
        'control_panel': 'Control Panel',
        'quick_actions': 'Quick Actions',
        'create_task': 'Create Task',
        'analytics': 'Analytics',
        'sync': 'Synchronization',
        'clear_completed': 'Clear Completed',
        'backup': 'Backup',
        'categories': 'Categories',
        'statistics': 'Statistics',
        'total': 'Total',
        'pending': 'Pending',
        'task_list': 'Task List',
        'sort_by': 'Sort by:',
        'created_date': 'Created Date',
        'title': 'Title',
        'due_date': 'Due Date',
        'ascending': 'Ascending',
        'descending': 'Descending',
        'no_tasks_title': 'No tasks yet',
        'no_tasks_subtitle': 'Create your first task to get started',
        'create_first_task': 'Create First Task',
        'task_title': 'Task Title *',
        'description': 'Description',
        'set_due_date': 'Set due date',
        'tags': 'Tags (comma separated)',
        'save': 'Save',
        'cancel': 'Cancel',
        'edit_task': 'Edit Task',
        'add_task': 'New Task',
        'edit': 'Edit',
        'delete': 'Delete',
        'confirm': 'Confirmation',
        'delete_task_confirm': 'Delete task',
        'success': 'Success',
        'task_deleted': 'Task deleted!',
        'task_created': 'created',
        'task_updated': 'updated',
        'error': 'Error',
        'enter_task_title': 'Please enter task title!',
        'invalid_date_format': 'Invalid date format! Use: YYYY-MM-DD HH:MM',
        'clear_completed_confirm': 'Clear all completed tasks?',
        'no_completed_tasks': 'No completed tasks to delete.',
        'tasks_cleared': 'tasks deleted!',
        'menu_file': 'File',
        'menu_edit': 'Edit',
        'menu_view': 'View',
        'menu_help': 'Help',
        'menu_export': 'Export...',
        'menu_import': 'Import...',
        'menu_exit': 'Exit',
        'menu_find': 'Find',
        'menu_clear_filters': 'Clear Filters',
        'menu_light_theme': 'Light Theme',
        'menu_dark_theme': 'Dark Theme',
        'menu_blue_theme': 'Blue Theme',
        'menu_language': 'Language',
        'menu_russian': 'Русский',
        'menu_english': 'English',
        'menu_statistics': 'Statistics',
        'menu_shortcuts': 'Shortcuts',
        'menu_about': 'About',
        'theme_changed': 'Theme Changed',
        'theme_applied': 'Applied theme:',
        'language_changed': 'Language Changed',
        'language_applied': 'Applied language:',
        'detailed_statistics': 'Detailed Statistics',
        'category_stats': 'Statistics by categories:',
        'priority_stats': 'Statistics by priorities:',
        'export_success': 'Tasks exported to',
        'export_error': 'Failed to export:',
        'import_confirm': 'Import',
        'import_success': 'Tasks imported!',
        'import_error': 'Failed to import:',
        'shortcuts_title': 'Keyboard Shortcuts',
        'shortcuts_text': '''⌨️ Keyboard Shortcuts

Ctrl+N - New task
Ctrl+F - Search
F5 - Refresh list
Delete - Delete selected task
Escape - Close dialog
Enter - Save in dialog

🖱️ Mouse

Right click - Context menu
Double click - Edit task
Mouse wheel - Scroll list''',
        'about_title': 'About',
        'about_text': '''📝 FRKHD - Modern Task Manager

Version: 2.0
Date: 2024

Features:
• Create and edit tasks
• Categories and priorities
• Due dates
• Filtering and search
• Export/import data
• Customizable themes
• Detailed statistics

Made with ❤️ using Python + tkinter''',
        'categories_list': [
            f"{ICONS['work']} Work",
            f"{ICONS['home']} Home",
            f"{ICONS['study']} Study", 
            f"{ICONS['health']} Health",
            f"{ICONS['shopping']} Shopping",
            f"{ICONS['entertainment']} Entertainment",
            f"{ICONS['sport']} Sport",
            f"{ICONS['travel']} Travel"
        ],
        'priorities_list': {
            'low': 'Low',
            'medium': 'Medium',
            'high': 'High', 
            'urgent': 'Urgent'
        }
    }
}
class AdvancedTodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Продвинутый ToDo Менеджер")
        self.root.geometry("1400x900")
        self.root.minsize(1200, 700)
        try:
            pass
        except:
            pass
        self.data_file = "advanced_tasks.json"
        self.settings_file = "settings.json"
        self.settings = self.load_settings()
        self.current_theme = self.settings.get('theme', 'light')
        self.current_language = self.settings.get('language', 'ru')
        self.tasks = self.load_tasks()
        self.search_var = tk.StringVar()
        self.category_filter_var = tk.StringVar(value=self.get_text('all'))
        self.priority_filter_var = tk.StringVar(value=self.get_text('all'))
        self.status_filter_var = tk.StringVar(value=self.get_text('all'))
        self.sort_var = tk.StringVar(value=self.get_text('created_date'))
        self.order_var = tk.StringVar(value=self.get_text('descending'))
        self.setup_fonts()
        self.setup_styles()
        self.create_menu()
        self.create_main_interface()
        self.refresh_task_list()
        self.search_var.trace('w', self.on_filter_change)
        self.category_filter_var.trace('w', self.on_filter_change)
        self.priority_filter_var.trace('w', self.on_filter_change)
        self.status_filter_var.trace('w', self.on_filter_change)
        self.root.attributes('-alpha', 0.0)
        self.fade_in()
    def setup_fonts(self):
        
        global FONTS
        FONTS = load_fonts()
        self.font_config = {
            'title': (FONTS['accent'], 32, 'bold'),
            'subtitle': (FONTS['accent'], 20, 'bold'),
            'header': (FONTS['primary'], 18, 'bold'), 
            'subheader': (FONTS['primary'], 16, 'bold'),
            'section': (FONTS['primary'], 14, 'bold'),
            'body': (FONTS['primary'], 12, 'normal'),
            'body_bold': (FONTS['primary'], 12, 'bold'),
            'body_large': (FONTS['primary'], 14, 'normal'),
            'body_medium': (FONTS['primary'], 11, 'normal'),
            'body_small': (FONTS['secondary'], 10, 'normal'),
            'body_tiny': (FONTS['secondary'], 9, 'normal'),
            'button': (FONTS['primary'], 12, 'bold'),
            'button_large': (FONTS['primary'], 14, 'bold'),
            'button_small': (FONTS['secondary'], 10, 'normal'),
            'monospace': ('Cascadia Code', 11, 'normal'),
            'menu': (FONTS['primary'], 12, 'normal'),
            'tooltip': (FONTS['secondary'], 9, 'normal'),
            'stats': (FONTS['accent'], 24, 'bold'),
            'card_title': (FONTS['primary'], 13, 'bold'),
            'card_text': (FONTS['secondary'], 11, 'normal')
        }
        self.fonts = {}
        for name, config in self.font_config.items():
            try:
                self.fonts[name] = font.Font(family=config[0], size=config[1], weight=config[2])
            except:
                self.fonts[name] = font.Font(family='Segoe UI', size=config[1], weight=config[2])
    def fade_in(self):
        
        alpha = self.root.attributes('-alpha')
        if alpha < 1.0:
            alpha += 0.05
            self.root.attributes('-alpha', alpha)
            self.root.after(20, self.fade_in)
    
    def get_text(self, key):
        
        return LANGUAGES[self.current_language].get(key, key)
    def create_modern_button(self, parent, text, command, bg_color, hover_color=None, 
                           font_style='button', padding_x=20, padding_y=12, width=None, 
                           style='primary', icon=None, tooltip=None):
        
        if hover_color is None:
            hover_color = self.lighten_color(bg_color, 0.15)
        button_styles = {
            'primary': {'bg': bg_color or THEMES[self.current_theme]['primary'], 'fg': 'white'},
            'secondary': {'bg': bg_color or THEMES[self.current_theme]['secondary'], 'fg': 'white'},
            'success': {'bg': bg_color or THEMES[self.current_theme]['success'], 'fg': 'white'},
            'danger': {'bg': bg_color or THEMES[self.current_theme]['danger'], 'fg': 'white'},
            'outline': {'bg': THEMES[self.current_theme]['card_bg'], 'fg': THEMES[self.current_theme]['primary']},
        }
        style_config = button_styles.get(style, button_styles['primary'])
        display_text = f"{icon} {text}" if icon else text
        button = tk.Button(
            parent,
            text=display_text,
            command=command,
            bg=style_config['bg'],
            fg=style_config['fg'],
            font=self.fonts.get(font_style, self.fonts['button']),
            relief='flat',
            bd=0,
            padx=padding_x,
            pady=padding_y,
            cursor='hand2',
            activebackground=hover_color,
            activeforeground=style_config['fg']
        )
        if width:
            button.config(width=width)
        def on_enter(e):
            button.config(bg=hover_color)
            if style == 'outline':
                button.config(bg=THEMES[self.current_theme]['hover'])
        def on_leave(e):
            button.config(bg=style_config['bg'])
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
        if tooltip:
            self.create_tooltip(button, tooltip)
        return button
    def create_card_frame(self, parent, bg_color, shadow=True):
        
        if shadow:
            shadow_frame = tk.Frame(
                parent,
                bg=THEMES[self.current_theme]['shadow'],
                height=2
            )
            shadow_frame.pack(fill='x', padx=2, pady=(0, 1))
        card_frame = tk.Frame(
            parent,
            bg=bg_color,
            relief='flat',
            bd=1,
            highlightbackground=THEMES[self.current_theme]['border'],
            highlightthickness=1
        )
        return card_frame
    def lighten_color(self, color, factor):
        
        try:
            color = color.lstrip('#')
            r, g, b = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            r = min(255, int(r + (255 - r) * factor))
            g = min(255, int(g + (255 - g) * factor))
            b = min(255, int(b + (255 - b) * factor))
            return f'#{r:02x}{g:02x}{b:02x}'
        except:
            return color
    def create_tooltip(self, widget, text):
        
        def on_enter(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
            label = tk.Label(
                tooltip,
                text=text,
                background=THEMES[self.current_theme]['accent'],
                foreground='white',
                font=self.fonts['tooltip'],
                relief='flat',
                padx=8,
                pady=4
            )
            label.pack()
            widget._tooltip = tooltip
        def on_leave(event):
            if hasattr(widget, '_tooltip'):
                widget._tooltip.destroy()
                delattr(widget, '_tooltip')
        widget.bind('<Enter>', on_enter)
        widget.bind('<Leave>', on_leave)
    def create_modern_modal(self, title, width=600, height=500):
        
        theme = THEMES[self.current_theme]
        modal = tk.Toplevel(self.root)
        modal.title(title)
        modal.resizable(False, False)
        modal.transient(self.root)
        modal.grab_set()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        modal.geometry(f"{width}x{height}+{x}+{y}")
        modal.overrideredirect(True)
        overlay = tk.Toplevel(self.root)
        overlay.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        overlay.configure(bg='black')
        overlay.attributes('-alpha', 0.5)
        overlay.overrideredirect(True)
        overlay.transient(self.root)
        modal_frame = tk.Frame(
            modal,
            bg=theme['card_bg'],
            relief='flat',
            bd=0
        )
        modal_frame.pack(fill='both', expand=True)
        shadow_frame = tk.Frame(
            modal_frame,
            bg='#000000',
            height=8,
            width=8
        )
        shadow_frame.place(x=8, y=8, relwidth=1, relheight=1)
        content_frame = tk.Frame(
            modal_frame,
            bg=theme['card_bg'],
            relief='flat',
            bd=0
        )
        content_frame.place(x=0, y=0, relwidth=1, relheight=1)
        header_frame = tk.Frame(
            content_frame,
            bg=theme['primary'],
            height=60
        )
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        header_content = tk.Frame(header_frame, bg=theme['primary'])
        header_content.pack(fill='both', expand=True, padx=20, pady=15)
        title_label = tk.Label(
            header_content,
            text=title,
            font=self.fonts['subtitle'],
            fg='white',
            bg=theme['primary']
        )
        title_label.pack(side='left')
        close_btn = tk.Button(
            header_content,
            text=ICONS['close'],
            command=lambda: self.close_modal(modal, overlay),
            bg=theme['danger'],
            fg='white',
            font=self.fonts['button'],
            relief='flat',
            bd=0,
            width=3,
            height=1,
            cursor='hand2'
        )
        close_btn.pack(side='right')
        def on_close_enter(e):
            close_btn.config(bg=theme['danger_light'])
        def on_close_leave(e):
            close_btn.config(bg=theme['danger'])
        close_btn.bind('<Enter>', on_close_enter)
        close_btn.bind('<Leave>', on_close_leave)
        body_frame = tk.Frame(
            content_frame,
            bg=theme['card_bg']
        )
        body_frame.pack(fill='both', expand=True, padx=20, pady=20)
        footer_frame = tk.Frame(
            content_frame,
            bg=theme['hover'],
            height=70
        )
        footer_frame.pack(fill='x', side='bottom')
        footer_frame.pack_propagate(False)
        modal.attributes('-alpha', 0.0)
        self.animate_modal_in(modal)
        return modal, overlay, body_frame, footer_frame
    def close_modal(self, modal, overlay):
        
        self.animate_modal_out(modal, overlay)
    def animate_modal_in(self, modal):
        
        alpha = 0.0
        def fade_in():
            nonlocal alpha
            if alpha < 1.0:
                alpha += 0.1
                modal.attributes('-alpha', alpha)
                modal.after(20, fade_in)
        fade_in()
    def animate_modal_out(self, modal, overlay):
        
        alpha = 1.0
        def fade_out():
            nonlocal alpha
            if alpha > 0.0:
                alpha -= 0.1
                modal.attributes('-alpha', alpha)
                modal.after(20, fade_out)
            else:
                overlay.destroy()
                modal.destroy()
        fade_out()
    def create_gradient_label(self, parent, text, start_color, end_color, font_style='body_bold'):
        
        label = tk.Label(
            parent,
            text=text,
            bg=start_color,
            fg='white',
            font=self.fonts.get(font_style, self.fonts['body_bold']),
            relief='flat',
            padx=15,
            pady=8
        )
        shadow_label = tk.Label(
            parent,
            text=text,
            bg=THEMES[self.current_theme]['shadow'],
            fg=THEMES[self.current_theme]['shadow'],
            font=self.fonts.get(font_style, self.fonts['body_bold']),
            relief='flat',
            padx=15,
            pady=8
        )
        return label
    def setup_styles(self):
        
        theme = THEMES[self.current_theme]
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background=theme['bg'])
        style.configure('TLabel', 
                       background=theme['bg'], 
                       foreground=theme['text'],
                       font=self.fonts.get('body', ('Segoe UI', 11)))
        style.configure('Title.TLabel',
                       background=theme['bg'],
                       foreground=theme['text'],
                       font=self.fonts.get('title', ('Segoe UI', 28, 'bold')))
        style.configure('Heading.TLabel', 
                       background=theme['bg'],
                       foreground=theme['text'],
                       font=self.fonts.get('header', ('Segoe UI', 16, 'bold')))
        style.configure('Subheading.TLabel',
                       background=theme['bg'], 
                       foreground=theme['text'],
                       font=self.fonts.get('subheader', ('Segoe UI', 14, 'bold')))
        style.configure('Modern.TButton',
                       background=theme['primary'],
                       foreground='white',
                       font=self.fonts.get('button', ('Segoe UI', 11, 'bold')),
                       borderwidth=0,
                       focuscolor='none')
        style.map('Modern.TButton',
                 background=[('active', theme.get('primary_light', theme['primary'])),
                           ('pressed', theme.get('primary_dark', theme['primary']))])
        style.configure('Modern.TEntry',
                       fieldbackground=theme['card_bg'], 
                       foreground=theme['text'],
                       font=self.fonts.get('body', ('Segoe UI', 11)))
        style.configure('Modern.TCombobox',
                       fieldbackground=theme['card_bg'],
                       foreground=theme['text'], 
                       font=self.fonts.get('body', ('Segoe UI', 11)))
        style.configure('Accent.TLabel',
                       background=theme['bg'],
                       foreground=theme['primary'],
                       font=self.fonts.get('body_bold', ('Segoe UI', 11, 'bold')))
        style.configure('Muted.TLabel',
                       background=theme['bg'],
                       foreground=theme['text_muted'],
                       font=self.fonts.get('body_small', ('Segoe UI', 10)))
        self.root.configure(bg=theme['bg'])
    def load_settings(self):
        
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    def save_settings(self):
        
        try:
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить настройки: {e}")
    def load_tasks(self):
        
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    def save_tasks(self):
        
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить задачи: {e}")
    def create_menu(self):
        
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.get_text('menu_file'), menu=file_menu)
        file_menu.add_command(label=self.get_text('new_task'), command=self.add_task_dialog, accelerator="Ctrl+N")
        file_menu.add_separator()
        file_menu.add_command(label=self.get_text('menu_import'), command=self.import_tasks)
        file_menu.add_command(label=self.get_text('menu_export'), command=self.export_tasks)
        file_menu.add_separator()
        file_menu.add_command(label=self.get_text('menu_exit'), command=self.root.quit)
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.get_text('menu_edit'), menu=edit_menu)
        edit_menu.add_command(label=self.get_text('menu_find'), command=self.focus_search, accelerator="Ctrl+F")
        edit_menu.add_command(label=self.get_text('menu_clear_filters'), command=self.clear_filters)
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.get_text('menu_view'), menu=view_menu)
        theme_menu = tk.Menu(view_menu, tearoff=0)
        view_menu.add_cascade(label="Theme", menu=theme_menu)
        theme_menu.add_command(label=self.get_text('menu_light_theme'), command=lambda: self.change_theme('light'))
        theme_menu.add_command(label=self.get_text('menu_dark_theme'), command=lambda: self.change_theme('dark'))
        theme_menu.add_command(label=self.get_text('menu_blue_theme'), command=lambda: self.change_theme('blue'))
        language_menu = tk.Menu(view_menu, tearoff=0)
        view_menu.add_cascade(label=self.get_text('menu_language'), menu=language_menu)
        language_menu.add_command(label=self.get_text('menu_russian'), command=lambda: self.change_language('ru'))
        language_menu.add_command(label=self.get_text('menu_english'), command=lambda: self.change_language('en'))
        view_menu.add_separator()
        view_menu.add_command(label=self.get_text('menu_statistics'), command=self.show_statistics)
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.get_text('menu_help'), menu=help_menu)
        help_menu.add_command(label=self.get_text('menu_shortcuts'), command=self.show_shortcuts)
        help_menu.add_command(label=self.get_text('menu_about'), command=self.show_about)
        self.root.bind('<Control-n>', lambda e: self.add_task_dialog())
        self.root.bind('<Control-f>', lambda e: self.focus_search())
        self.root.bind('<F5>', lambda e: self.refresh_task_list())
        self.root.bind('<Delete>', lambda e: self.delete_selected_task())
    def create_main_interface(self):
        
        theme = THEMES[self.current_theme]
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        self.create_top_panel(main_frame, theme)
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill='both', expand=True, pady=(10, 0))
        self.create_left_panel(content_frame, theme)
        self.create_right_panel(content_frame, theme)
        self.create_bottom_panel(main_frame, theme)
    def create_top_panel(self, parent, theme):
        
        header_frame = tk.Frame(parent, bg=theme['primary'], height=80)
        header_frame.pack(fill='x', pady=(0, 0))
        header_frame.pack_propagate(False)
        gradient_frame = tk.Frame(header_frame, bg=theme['accent'], height=4)
        gradient_frame.pack(fill='x', side='bottom')
        header_content = tk.Frame(header_frame, bg=theme['primary'])
        header_content.pack(fill='both', expand=True, padx=30, pady=15)
        left_header = tk.Frame(header_content, bg=theme['primary'])
        left_header.pack(side='left', fill='y')
        title_frame = tk.Frame(left_header, bg=theme['primary'])
        title_frame.pack(side='left', fill='y')
        title_container = tk.Frame(title_frame, bg=theme['primary'])
        title_container.pack(side='left', fill='y', padx=(20, 0))
        app_title = tk.Label(
            title_container,
            text=self.get_text('app_title'),
            font=self.fonts['title'],
            fg='white',
            bg=theme['primary']
        )
        app_title.pack(pady=5)
        subtitle = tk.Label(
            title_container,
            text=self.get_text('app_subtitle'),
            font=self.fonts['body_medium'],
            fg=theme['text_light'],
            bg=theme['primary']
        )
        subtitle.pack()
        right_header = tk.Frame(header_content, bg=theme['primary'])
        right_header.pack(side='right', fill='y')
        add_btn = self.create_modern_button(
            right_header,
            self.get_text('new_task'),
            self.add_task_dialog,
            theme['success'],
            font_style='button_large',
            padding_x=25,
            padding_y=12,
            style='success',
            icon=ICONS['add'],
            tooltip=self.get_text('create_task')
        )
        add_btn.pack(side='right', padx=(10, 0))
        refresh_btn = self.create_modern_button(
            right_header,
            self.get_text('refresh'),
            self.refresh_task_list,
            theme['info'],
            font_style='button_small',
            padding_x=20,
            padding_y=10,
            style='primary',
            icon=ICONS['refresh'],
            tooltip=self.get_text('refresh')
        )
        refresh_btn.pack(side='right', padx=(10, 0))
        filter_main_frame = tk.Frame(parent, bg=theme['card_bg'], height=70)
        filter_main_frame.pack(fill='x', pady=(0, 15))
        filter_main_frame.pack_propagate(False)
        shadow_frame = tk.Frame(parent, bg=theme['shadow'], height=2)
        shadow_frame.pack(fill='x', pady=(0, 5))
        filter_frame = tk.Frame(filter_main_frame, bg=theme['card_bg'])
        filter_frame.pack(fill='both', expand=True, padx=30, pady=15)
        search_section = tk.Frame(filter_frame, bg=theme['card_bg'])
        search_section.pack(side='left', fill='y')
        search_label = tk.Label(
            search_section,
            text=f"{ICONS['search']} {self.get_text('quick_search')}",
            font=self.fonts['body_bold'],
            bg=theme['card_bg'],
            fg=theme['text']
        )
        search_label.pack(side='left', pady=5)
        search_frame = tk.Frame(search_section, bg=theme['card_bg'])
        search_frame.pack(side='left', padx=(10, 30))
        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=self.fonts['body'],
            width=35,
            relief='flat',
            bd=5,
            bg='white',
            fg=theme['text'],
            insertbackground=theme['primary']
        )
        self.search_entry.pack(pady=5)
        search_underline = tk.Frame(search_frame, bg=theme['primary'], height=2)
        search_underline.pack(fill='x')
        filters_section = tk.Frame(filter_frame, bg=theme['card_bg'])
        filters_section.pack(side='right', fill='y')
        self.create_modern_filters(filters_section, theme)
    def create_modern_filters(self, parent, theme):
        
        category_options = [self.get_text('all')] + [cat['name'] for cat in CATEGORIES]
        priority_options = [self.get_text('all')] + [p['name'] for p in PRIORITIES.values()]
        status_options = [self.get_text('all'), self.get_text('active'), self.get_text('completed'), self.get_text('overdue')]
        
        filters = [
            (f"{ICONS['folder']} {self.get_text('category')}", self.category_filter_var, category_options),
            (f"{ICONS['flag']} {self.get_text('priority')}", self.priority_filter_var, priority_options),
            (f"{ICONS['chart']} {self.get_text('status')}", self.status_filter_var, status_options)
        ]
        for i, (label_text, var, values) in enumerate(filters):
            filter_container = tk.Frame(parent, bg=theme['card_bg'])
            filter_container.pack(side='left', padx=(0, 20))
            label = tk.Label(
                filter_container,
                text=label_text,
                font=self.fonts['body_small'],
                bg=theme['card_bg'],
                fg=theme['text']
            )
            label.pack(anchor='w')
            combo = ttk.Combobox(
                filter_container,
                textvariable=var,
                values=values,
                state='readonly',
                font=self.fonts['body_small'],
                width=15
            )
            combo.set(values[0])
            combo.pack(pady=(2, 0))
            style = ttk.Style()
            style.configure('TCombobox', 
                          fieldbackground='white',
                          background=theme['primary'],
                          foreground=theme['text'],
                          borderwidth=0)
    def create_left_panel(self, parent, theme):
        
        left_container = tk.Frame(parent, bg=theme['bg'])
        left_container.pack(side='left', fill='y', padx=(0, 15))
        sidebar = tk.Frame(
            left_container,
            bg=theme['sidebar_bg'],
            relief='solid',
            bd=1,
            width=320,
            padx=20,
            pady=20
        )
        sidebar.pack(fill='y', expand=False)
        sidebar.pack_propagate(False)
        control_header = tk.Label(
            sidebar,
            text=f"{ICONS['settings']} {self.get_text('control_panel')}",
            font=self.fonts['header'],
            bg=theme['sidebar_bg'],
            fg=theme['text']
        )
        control_header.pack(pady=(0, 20), anchor='w')
        actions_section = tk.Frame(sidebar, bg=theme['sidebar_bg'])
        actions_section.pack(fill='x', pady=(0, 25))
        actions_label = tk.Label(
            actions_section,
            text=f"{ICONS['star']} {self.get_text('quick_actions')}",
            font=self.fonts['subheader'],
            bg=theme['sidebar_bg'],
            fg=theme['text']
        )
        actions_label.pack(anchor='w', pady=(0, 10))
        actions = [
            (self.get_text('create_task'), self.add_task_dialog, theme['success'], ICONS['add']),
            (self.get_text('analytics'), self.show_statistics, theme['info'], ICONS['analytics']),
            (self.get_text('sync'), self.refresh_task_list, theme['primary'], ICONS['sync']),
            (self.get_text('clear_completed'), self.clear_completed, theme['danger'], ICONS['clean']),
            (self.get_text('backup'), self.export_tasks, theme['warning'], ICONS['backup'])
        ]
        for text, command, color, icon in actions:
            btn_container = tk.Frame(actions_section, bg=theme['sidebar_bg'])
            btn_container.pack(fill='x', pady=3)
            btn = self.create_modern_button(
                btn_container,
                text.replace('➕ ', '').replace('📊 ', '').replace('🔄 ', '').replace('🗑️ ', '').replace('💾 ', ''),
                command,
                color,
                font_style='button_small',
                padding_x=15,
                padding_y=10,
                width=25,
                icon=icon
            )
            btn.pack(fill='x')
        separator = tk.Frame(sidebar, bg=theme['border'], height=2)
        separator.pack(fill='x', pady=20)
        categories_section = tk.Frame(sidebar, bg=theme['sidebar_bg'])
        categories_section.pack(fill='x', pady=(0, 20))
        categories_header = tk.Label(
            categories_section,
            text=f"{ICONS['folder']} {self.get_text('categories')}",
            font=self.fonts['subheader'],
            bg=theme['sidebar_bg'],
            fg=theme['text']
        )
        categories_header.pack(anchor='w', pady=(0, 10))
        self.categories_container = tk.Frame(categories_section, bg=theme['sidebar_bg'])
        self.categories_container.pack(fill='x')
        stats_section = tk.Frame(sidebar, bg=theme['sidebar_bg'])
        stats_section.pack(fill='x', side='bottom', pady=(20, 0))
        stats_header = tk.Label(
            stats_section,
            text=f"{ICONS['chart']} {self.get_text('statistics')}",
            font=self.fonts['subheader'],
            bg=theme['sidebar_bg'],
            fg=theme['text']
        )
        stats_header.pack(anchor='w', pady=(0, 10))
        self.quick_stats_container = tk.Frame(stats_section, bg=theme['sidebar_bg'])
        self.quick_stats_container.pack(fill='x')
        self.update_category_counters()
        self.update_quick_stats()
    def update_quick_stats(self):
        
        theme = THEMES[self.current_theme]
        for widget in self.quick_stats_container.winfo_children():
            widget.destroy()
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.get('completed', False))
        pending = total - completed
        from datetime import datetime
        now = datetime.now()
        overdue = sum(1 for task in self.tasks 
                     if not task.get('completed', False) and 
                        task.get('due_date') and 
                        datetime.fromisoformat(task['due_date']) < now)
        stats_data = [
            (f"{ICONS['folder']} {self.get_text('total')}", total, theme['primary']),
            (f"{ICONS['check']} {self.get_text('completed')}", completed, theme['success']),
            (f"{ICONS['clock']} {self.get_text('pending')}", pending, theme['warning']),
            (f"{ICONS['warning']} {self.get_text('overdue')}", overdue, theme['danger'])
        ]
        for i, (label, value, color) in enumerate(stats_data):
            stat_card = tk.Frame(
                self.quick_stats_container,
                bg=color,
                relief='flat',
                pady=8,
                padx=12
            )
            stat_card.pack(fill='x', pady=2)
            stat_label = tk.Label(
                stat_card,
                text=f"{label}: {value}",
                font=self.fonts['body_bold'],
                bg=color,
                fg='white'
            )
            stat_label.pack()
    def update_category_counters(self):
        
        theme = THEMES[self.current_theme]
        for widget in self.categories_container.winfo_children():
            widget.destroy()
        from collections import defaultdict
        category_counts = defaultdict(int)
        for task in self.tasks:
            if not task.get('completed', False):
                category_counts[task.get('category', 'Без категории')] += 1
        for category in CATEGORIES:
            count = category_counts.get(category['name'], 0)
            cat_frame = tk.Frame(self.categories_container, bg=theme['sidebar_bg'])
            cat_frame.pack(fill='x', pady=2)
            cat_btn = tk.Button(
                cat_frame,
                text=f"{category['icon']} {category['name'].split(' ', 1)[1]} ({count})",
                command=lambda c=category['name']: self.filter_by_category(c),
                bg=category['color'],
                fg='white',
                font=self.fonts['body_small'],
                relief='flat',
                bd=0,
                pady=8,
                anchor='w',
                cursor='hand2'
            )
            cat_btn.pack(fill='x')
            def on_enter(e, btn=cat_btn, color=category['gradient']):
                btn.config(bg=color)
            def on_leave(e, btn=cat_btn, color=category['color']):
                btn.config(bg=color)
            cat_btn.bind('<Enter>', on_enter)
            cat_btn.bind('<Leave>', on_leave)
    def create_right_panel(self, parent, theme):
        
        right_frame = tk.Frame(parent, bg=theme['bg'])
        right_frame.pack(side='right', fill='both', expand=True)
        header_frame = tk.Frame(right_frame, bg=theme['bg'])
        header_frame.pack(fill='x', pady=(0, 10))
        tk.Label(
            header_frame,
            text=f"{ICONS['folder']} {self.get_text('task_list')}",
            font=self.fonts['header'],
            bg=theme['bg'],
            fg=theme['text']
        ).pack(side='left')
        sort_frame = tk.Frame(header_frame, bg=theme['bg'])
        sort_frame.pack(side='right')
        tk.Label(sort_frame, text=self.get_text('sort_by'), bg=theme['bg'], fg=theme['text']).pack(side='left')
        self.sort_options = {
            self.get_text('created_date'): 'created_at',
            self.get_text('title'): 'title', 
            self.get_text('priority'): 'priority',
            self.get_text('due_date'): 'due_date',
            self.get_text('category'): 'category'
        }
        self.order_options = {
            self.get_text('ascending'): 'asc',
            self.get_text('descending'): 'desc'
        }
        sort_combo = ttk.Combobox(
            sort_frame,
            width=18,
            state='readonly',
            font=self.fonts['body_small']
        )
        sort_combo['values'] = list(self.sort_options.keys())
        sort_combo.set(self.get_text('created_date'))
        sort_combo.pack(side='left', padx=(5, 5))
        sort_combo.bind('<<ComboboxSelected>>', self.on_sort_change)
        order_combo = ttk.Combobox(
            sort_frame,
            width=15,
            state='readonly',
            font=self.fonts['body_small']
        )
        order_combo['values'] = list(self.order_options.keys())
        order_combo.set(self.get_text('descending'))
        order_combo.pack(side='left', padx=(5, 0))
        order_combo.bind('<<ComboboxSelected>>', self.on_order_change)
        self.sort_combo = sort_combo
        self.order_combo = order_combo
        list_frame = tk.Frame(right_frame, bg=theme['bg'])
        list_frame.pack(fill='both', expand=True)
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side='right', fill='y')
        self.canvas = tk.Canvas(
            list_frame,
            bg=theme['bg'],
            yscrollcommand=scrollbar.set,
            highlightthickness=0
        )
        self.canvas.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.canvas.yview)
        self.tasks_container = tk.Frame(self.canvas, bg=theme['bg'])
        self.canvas_window = self.canvas.create_window(
            0, 0, anchor='nw', window=self.tasks_container
        )
        self.tasks_container.bind('<Configure>', self.on_frame_configure)
        self.canvas.bind('<Configure>', self.on_canvas_configure)
        self.canvas.bind('<MouseWheel>', lambda e: self.canvas.yview_scroll(-1 * int(e.delta/120), "units"))
    def create_bottom_panel(self, parent, theme):
        
        bottom_frame = tk.Frame(parent, bg=theme['card_bg'], relief='solid', bd=1)
        bottom_frame.pack(fill='x', pady=(10, 0))
        self.stats_label = tk.Label(
            bottom_frame,
            text="",
            font=self.fonts['body_medium'],
            bg=theme['card_bg'],
            fg=theme['text'],
            pady=12
        )
        self.stats_label.pack()
        self.update_statistics()
    def on_frame_configure(self, event):
        
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    def on_canvas_configure(self, event):
        
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)
    def on_filter_change(self, *args):
        
        self.refresh_task_list()
    def on_sort_change(self, event):
        
        selected_text = self.sort_combo.get()
        self.sort_var.set(self.sort_options.get(selected_text, 'created_at'))
        self.refresh_task_list()
    def on_order_change(self, event):
        
        selected_text = self.order_combo.get()
        self.order_var.set(self.order_options.get(selected_text, 'desc'))
        self.refresh_task_list()
    def focus_search(self):
        
        self.search_entry.focus_set()
    def clear_filters(self):
        
        self.search_var.set('')
        self.category_filter_var.set(self.get_text('all'))
        self.priority_filter_var.set(self.get_text('all'))
        self.status_filter_var.set(self.get_text('all'))
    def filter_by_category(self, category):
        
        self.category_filter_var.set(category)
    def get_filtered_tasks(self):
        
        filtered_tasks = self.tasks[:]
        search_text = self.search_var.get().lower()
        if search_text:
            filtered_tasks = [
                task for task in filtered_tasks
                if search_text in task.get('title', '').lower() or
                   search_text in task.get('description', '').lower()
            ]
        category_filter = self.category_filter_var.get()
        if category_filter and category_filter != self.get_text('all'):
            filtered_tasks = [
                task for task in filtered_tasks
                if task.get('category') == category_filter
            ]
        priority_filter = self.priority_filter_var.get()
        if priority_filter and priority_filter != self.get_text('all'):
            priority_key = None
            for key, value in PRIORITIES.items():
                if value['name'] == priority_filter:
                    priority_key = key
                    break
            if priority_key:
                filtered_tasks = [
                    task for task in filtered_tasks
                    if task.get('priority') == priority_key
                ]
        status_filter = self.status_filter_var.get()
        if status_filter and status_filter != self.get_text('all'):
            now = datetime.now()
            if status_filter == self.get_text('active'):
                filtered_tasks = [
                    task for task in filtered_tasks
                    if not task.get('completed', False)
                ]
            elif status_filter == self.get_text('completed'):
                filtered_tasks = [
                    task for task in filtered_tasks
                    if task.get('completed', False)
                ]
            elif status_filter == self.get_text('overdue'):
                filtered_tasks = [
                    task for task in filtered_tasks
                    if not task.get('completed', False) and
                       task.get('due_date') and
                       datetime.fromisoformat(task['due_date']) < now
                ]
        return filtered_tasks
    def sort_tasks(self, tasks):
        
        sort_key = self.sort_var.get()
        reverse = self.order_var.get() == 'desc'
        if sort_key == 'created_at':
            return sorted(tasks, key=lambda x: x.get('created_at', ''), reverse=reverse)
        elif sort_key == 'title':
            return sorted(tasks, key=lambda x: x.get('title', '').lower(), reverse=reverse)
        elif sort_key == 'priority':
            priority_order = {'low': 1, 'medium': 2, 'high': 3, 'urgent': 4}
            return sorted(tasks, key=lambda x: priority_order.get(x.get('priority', 'low'), 1), reverse=reverse)
        elif sort_key == 'due_date':
            return sorted(tasks, key=lambda x: x.get('due_date', '9999-12-31'), reverse=reverse)
        elif sort_key == 'category':
            return sorted(tasks, key=lambda x: x.get('category', ''), reverse=reverse)
        return tasks
    def refresh_task_list(self):
        
        for widget in self.tasks_container.winfo_children():
            widget.destroy()
        filtered_tasks = self.get_filtered_tasks()
        sorted_tasks = self.sort_tasks(filtered_tasks)
        if not sorted_tasks:
            no_tasks_frame = tk.Frame(self.tasks_container, bg=THEMES[self.current_theme]['bg'])
            no_tasks_frame.pack(expand=True, fill='both')
            icon_label = tk.Label(
                no_tasks_frame,
                text="📝",
                font=('Segoe UI', 72),
                bg=THEMES[self.current_theme]['bg'],
                fg=THEMES[self.current_theme]['text_muted']
            )
            icon_label.pack(pady=(100, 20))
            message_label = tk.Label(
                no_tasks_frame,
                text=self.get_text('no_tasks_title'),
                font=('Segoe UI', 18, 'bold'),
                bg=THEMES[self.current_theme]['bg'],
                fg=THEMES[self.current_theme]['text_muted']
            )
            message_label.pack()
            subtitle_label = tk.Label(
                no_tasks_frame,
                text=self.get_text('no_tasks_subtitle'),
                font=('Segoe UI', 12),
                bg=THEMES[self.current_theme]['bg'],
                fg=THEMES[self.current_theme]['text_muted']
            )
            subtitle_label.pack(pady=(10, 0))
            create_btn = self.create_modern_button(
                no_tasks_frame,
                self.get_text('create_first_task'),
                self.add_task_dialog,
                THEMES[self.current_theme]['success'],
                font_style='button_large',
                padding_x=30,
                padding_y=15,
                style='success',
                icon=ICONS['add'],
                tooltip=self.get_text('create_first_task')
            )
            create_btn.pack(pady=30)
        else:
            for i, task in enumerate(sorted_tasks):
                self.create_task_widget(task, i)
        self.update_category_counters()
        self.update_statistics()
        self.update_quick_stats()
    def create_task_widget(self, task, index):
        
        theme = THEMES[self.current_theme]
        is_completed = task.get('completed', False)
        priority = task.get('priority', 'low')
        priority_info = PRIORITIES[priority]
        card_container = tk.Frame(self.tasks_container, bg=theme['bg'])
        card_container.pack(fill='x', padx=15, pady=12)
        shadow_layers = [
            (6, '#f1f5f9'),
            (4, '#e2e8f0'),
            (2, '#cbd5e1')
        ]
        for offset, color in shadow_layers:
            shadow = tk.Frame(
                card_container,
                bg=color,
                height=2
            )
            shadow.place(x=offset, y=offset, relwidth=1, relheight=1)
        main_card = tk.Frame(
            card_container,
            bg=theme['card_bg'],
            relief='flat',
            bd=0,
            highlightthickness=1,
            highlightbackground=theme['border'],
            highlightcolor=theme['primary']
        )
        main_card.place(x=0, y=0, relwidth=1, relheight=1)
        priority_stripe = tk.Frame(
            main_card,
            bg=priority_info['color'],
            width=8
        )
        priority_stripe.pack(side='left', fill='y')
        content_frame = tk.Frame(main_card, bg=theme['card_bg'])
        content_frame.pack(side='left', fill='both', expand=True, padx=25, pady=25)
        header_row = tk.Frame(content_frame, bg=theme['card_bg'])
        header_row.pack(fill='x', pady=(0, 10))
        header_left = tk.Frame(header_row, bg=theme['card_bg'])
        header_left.pack(side='left', fill='x', expand=True)
        completed_var = tk.BooleanVar(value=is_completed)
        checkbox_frame = tk.Frame(header_left, bg=theme['card_bg'])
        checkbox_frame.pack(side='left', padx=(0, 15))
        checkbox = tk.Checkbutton(
            checkbox_frame,
            variable=completed_var,
            command=lambda: self.toggle_task_completion(task, completed_var.get()),
            bg=theme['card_bg'],
            activebackground=theme['card_bg'],
            selectcolor=priority_info['color'],
            font=self.fonts['body'],
            cursor='hand2'
        )
        checkbox.pack()
        title_text = task.get('title', 'Без названия')
        title_font = self.fonts['card_title'] if not is_completed else self.fonts['card_text']
        title_color = theme['text'] if not is_completed else theme['text_muted']
        if is_completed:
            title_text = f"✅ {title_text}"
        title_label = tk.Label(
            header_left,
            text=title_text,
            font=title_font,
            bg=theme['card_bg'],
            fg=title_color,
            anchor='w',
            wraplength=400
        )
        title_label.pack(side='left', fill='x', expand=True)
        actions_frame = tk.Frame(header_row, bg=theme['card_bg'])
        actions_frame.pack(side='right')
        edit_btn = tk.Button(
            actions_frame,
            text=ICONS['edit'],
            command=lambda: self.edit_task_dialog(task),
            bg=theme['warning'],
            fg='white',
            font=self.fonts['button_small'],
            relief='flat',
            bd=0,
            width=4,
            height=2,
            cursor='hand2'
        )
        edit_btn.pack(side='left', padx=3)
        delete_btn = tk.Button(
            actions_frame,
            text=ICONS['delete'],
            command=lambda: self.delete_task(task),
            bg=theme['danger'],
            fg='white',
            font=self.fonts['button_small'],
            relief='flat',
            bd=0,
            width=4,
            height=2,
            cursor='hand2'
        )
        delete_btn.pack(side='left', padx=3)
        def create_hover_effect(button, normal_color, hover_color):
            def on_enter(e):
                button.config(bg=hover_color)
            def on_leave(e):
                button.config(bg=normal_color)
            button.bind('<Enter>', on_enter)
            button.bind('<Leave>', on_leave)
        create_hover_effect(edit_btn, theme['warning'], self.lighten_color(theme['warning'], 0.2))
        create_hover_effect(delete_btn, theme['danger'], self.lighten_color(theme['danger'], 0.2))
        description = task.get('description', '')
        if description and description.strip():
            desc_label = tk.Label(
                content_frame,
                text=description,
                font=self.fonts['body_medium'],
                bg=theme['card_bg'],
                fg=theme['text_muted'],
                anchor='w',
                wraplength=600,
                justify='left'
            )
            desc_label.pack(anchor='w', pady=(0, 15))
        meta_row = tk.Frame(content_frame, bg=theme['card_bg'])
        meta_row.pack(fill='x')
        meta_left = tk.Frame(meta_row, bg=theme['card_bg'])
        meta_left.pack(side='left', fill='x', expand=True)
        priority_badge = tk.Label(
            meta_left,
            text=f"{priority_info['icon']} {priority_info['name']}",
            font=self.fonts['body_tiny'],
            bg=priority_info['color'],
            fg='white',
            padx=12,
            pady=4
        )
        priority_badge.pack(side='left', padx=(0, 10))
        category = task.get('category', '')
        if category:
            cat_info = None
            for cat in CATEGORIES:
                if cat['name'] == category:
                    cat_info = cat
                    break
            if cat_info:
                category_badge = tk.Label(
                    meta_left,
                    text=f"{cat_info['icon']} {category.split(' ', 1)[1] if ' ' in category else category}",
                    font=('Segoe UI', 9, 'bold'),
                    bg=cat_info['color'],
                    fg='white',
                    padx=12,
                    pady=4
                )
                category_badge.pack(side='left', padx=(0, 10))
        tags = task.get('tags', [])
        if tags:
            for tag in tags[:3]:
                tag_badge = tk.Label(
                    meta_left,
                    text=f"🏷️ {tag}",
                    font=('Segoe UI', 8),
                    bg=theme['secondary'],
                    fg='white',
                    padx=8,
                    pady=2
                )
                tag_badge.pack(side='left', padx=(0, 5))
        meta_right = tk.Frame(meta_row, bg=theme['card_bg'])
        meta_right.pack(side='right')
        due_date = task.get('due_date')
        if due_date:
            try:
                from datetime import datetime
                due_dt = datetime.fromisoformat(due_date)
                now = datetime.now()
                days_left = (due_dt - now).days
                hours_left = int((due_dt - now).total_seconds() / 3600)
                if days_left < 0:
                    due_text = f"⏰ Просрочено на {abs(days_left)} дн."
                    due_color = theme['danger']
                elif days_left == 0:
                    if hours_left > 0:
                        due_text = f"⏰ Через {hours_left} ч."
                        due_color = theme['warning']
                    else:
                        due_text = "⏰ Сегодня"
                        due_color = theme['warning']
                elif days_left == 1:
                    due_text = "⏰ Завтра"
                    due_color = theme['info']
                else:
                    due_text = f"⏰ Через {days_left} дн."
                    due_color = theme['info']
                due_badge = tk.Label(
                    meta_right,
                    text=due_text,
                    font=('Segoe UI', 9, 'bold'),
                    bg=due_color,
                    fg='white',
                    padx=12,
                    pady=4
                )
                due_badge.pack(side='right', padx=(10, 0))
            except:
                pass
        created_at = task.get('created_at', '')
        if created_at:
            try:
                from datetime import datetime
                created_dt = datetime.fromisoformat(created_at)
                created_text = f"📅 {created_dt.strftime('%d.%m.%Y')}"
                created_label = tk.Label(
                    meta_right,
                    text=created_text,
                    font=('Segoe UI', 9),
                    bg=theme['card_bg'],
                    fg=theme['text_muted']
                )
                created_label.pack(side='right', padx=(10, 0))
            except:
                pass
        def on_card_enter(e):
            main_card.config(highlightbackground=priority_info['color'], highlightthickness=2)
        def on_card_leave(e):
            main_card.config(highlightthickness=0)
        widgets_to_bind = [main_card, content_frame, header_row, header_left, meta_row, meta_left, meta_right]
        for widget in widgets_to_bind:
            widget.bind('<Enter>', on_card_enter)
            widget.bind('<Leave>', on_card_leave)
        def on_double_click(e):
            self.edit_task_dialog(task)
        for widget in widgets_to_bind:
            widget.bind('<Double-Button-1>', on_double_click)
    def toggle_task_completion(self, task, completed):
        
        task['completed'] = completed
        if completed:
            task['completed_at'] = datetime.now().isoformat()
        else:
            task.pop('completed_at', None)
        self.save_tasks()
        self.refresh_task_list()
    def delete_task(self, task):
        
        if messagebox.askyesno("Подтверждение", f"Удалить задачу '{task.get('title', '')}'?"):
            self.tasks.remove(task)
            self.save_tasks()
            self.refresh_task_list()
            messagebox.showinfo("Успех", "Задача удалена!")
    def delete_selected_task(self):
        
        pass
    def clear_completed(self):
        
        completed_count = sum(1 for task in self.tasks if task.get('completed', False))
        if completed_count == 0:
            messagebox.showinfo("Информация", "Нет выполненных задач для удаления")
            return
        if messagebox.askyesno("Подтверждение", 
                              f"Удалить {completed_count} выполненных задач?"):
            self.tasks = [task for task in self.tasks if not task.get('completed', False)]
            self.save_tasks()
            self.refresh_task_list()
            messagebox.showinfo("Успех", f"Удалено {completed_count} задач!")
    def add_task_dialog(self):
        
        self.task_dialog(None, self.get_text('add_task'))
    def edit_task_dialog(self, task):
        
        self.task_dialog(task, self.get_text('edit_task'))
    def task_dialog(self, task=None, title="Задача"):
        
        theme = THEMES[self.current_theme]
        is_edit = task is not None
        modal, overlay, body_frame, footer_frame = self.create_modern_modal(
            title=f"{ICONS['add']} {title}" if not task else f"{ICONS['edit']} {self.get_text('edit_task')}",
            width=700,
            height=650
        )
        tk.Label(
            body_frame,
            text=f"{ICONS['edit']} {self.get_text('task_title')}",
            font=self.fonts['body_bold'],
            bg=theme['card_bg'],
            fg=theme['text']
        ).pack(anchor='w', pady=(0, 5))
        title_entry = tk.Entry(
            body_frame,
            font=self.fonts['body'],
            width=50,
            relief='flat',
            bd=10,
            bg=theme['hover'],
            fg=theme['text']
        )
        title_entry.pack(fill='x', pady=(0, 20))
        tk.Label(
            body_frame,
            text=f"{ICONS['info']} {self.get_text('description')}",
            font=self.fonts['body_bold'],
            bg=theme['card_bg'],
            fg=theme['text']
        ).pack(anchor='w', pady=(0, 5))
        desc_frame = tk.Frame(body_frame, bg=theme['card_bg'])
        desc_frame.pack(fill='x', pady=(0, 20))
        desc_text = tk.Text(
            desc_frame,
            font=self.fonts['body_medium'],
            height=4,
            wrap='word',
            relief='flat',
            bd=10,
            bg=theme['hover'],
            fg=theme['text']
        )
        desc_text.pack(side='left', fill='both', expand=True)
        desc_scroll = tk.Scrollbar(desc_frame, command=desc_text.yview)
        desc_scroll.pack(side='right', fill='y')
        desc_text.config(yscrollcommand=desc_scroll.set)
        settings_frame = tk.Frame(body_frame, bg=theme['card_bg'])
        settings_frame.pack(fill='x', pady=(0, 20))
        left_col = tk.Frame(settings_frame, bg=theme['card_bg'])
        left_col.pack(side='left', fill='both', expand=True, padx=(0, 15))
        tk.Label(
            left_col,
            text=f"{ICONS['category']} {self.get_text('category')}",
            font=self.fonts['body_bold'],
            bg=theme['card_bg'],
            fg=theme['text']
        ).pack(anchor='w', pady=(0, 5))
        category_var = tk.StringVar()
        category_combo = ttk.Combobox(
            left_col,
            textvariable=category_var,
            state='readonly',
            width=25,
            font=self.fonts['body_medium']
        )
        category_combo['values'] = [cat['name'] for cat in CATEGORIES]
        category_combo.pack(fill='x', pady=(0, 15))
        tk.Label(
            left_col,
            text=f"{ICONS['flag']} {self.get_text('priority')}",
            font=self.fonts['body_bold'],
            bg=theme['card_bg'],
            fg=theme['text']
        ).pack(anchor='w', pady=(0, 5))
        priority_var = tk.StringVar()
        priority_combo = ttk.Combobox(
            left_col,
            textvariable=priority_var,
            state='readonly',
            width=25,
            font=self.fonts['body_medium']
        )
        priority_combo['values'] = [p['name'] for p in PRIORITIES.values()]
        priority_combo.pack(fill='x', pady=(0, 15))
        right_col = tk.Frame(settings_frame, bg=theme['card_bg'])
        right_col.pack(side='right', fill='both', expand=True, padx=(15, 0))
        tk.Label(
            right_col,
            text=f"{ICONS['clock']} {self.get_text('due_date')}",
            font=self.fonts['body_bold'],
            bg=theme['card_bg'],
            fg=theme['text']
        ).pack(anchor='w', pady=(0, 5))
        due_frame = tk.Frame(right_col, bg=theme['card_bg'])
        due_frame.pack(fill='x', pady=(0, 15))
        due_var = tk.BooleanVar()
        due_check = tk.Checkbutton(
            due_frame,
            text=self.get_text('set_due_date'),
            variable=due_var,
            bg=theme['card_bg'],
            fg=theme['text'],
            font=self.fonts['body_medium'],
            selectcolor=theme['hover']
        )
        due_check.pack(anchor='w', pady=(0, 5))
        due_date_entry = tk.Entry(
            due_frame,
            font=self.fonts['body_medium'],
            width=25,
            relief='flat',
            bd=10,
            bg=theme['hover'],
            fg=theme['text_muted']
        )
        due_date_entry.pack(fill='x')
        due_date_entry.insert(0, "ГГГГ-ММ-ДД ЧЧ:ММ")
        due_date_entry.config(state='disabled')
        def toggle_due_date():
            if due_var.get():
                due_date_entry.config(state='normal')
                due_date_entry.delete(0, tk.END)
                tomorrow = datetime.now() + timedelta(days=1)
                due_date_entry.insert(0, tomorrow.strftime("%Y-%m-%d %H:%M"))
            else:
                due_date_entry.config(state='disabled')
                due_date_entry.delete(0, tk.END)
                due_date_entry.insert(0, "ГГГГ-ММ-ДД ЧЧ:ММ")
        due_check.config(command=toggle_due_date)
        tk.Label(
            right_col,
            text=f"{ICONS['tag']} {self.get_text('tags')}",
            font=self.fonts['body_bold'],
            bg=theme['card_bg'],
            fg=theme['text']
        ).pack(anchor='w', pady=(0, 5))
        tags_entry = tk.Entry(
            right_col,
            font=self.fonts['body_medium'],
            width=25,
            relief='flat',
            bd=10,
            bg=theme['hover'],
            fg=theme['text']
        )
        tags_entry.pack(fill='x')
        if is_edit:
            title_entry.insert(0, task.get('title', ''))
            desc_text.insert('1.0', task.get('description', ''))
            category_combo.set(task.get('category', ''))
            priority_key = task.get('priority', 'low')
            priority_combo.set(PRIORITIES[priority_key]['name'])
            if task.get('due_date'):
                due_var.set(True)
                toggle_due_date()
                due_date_entry.delete(0, tk.END)
                due_date_entry.insert(0, task['due_date'])
            tags_entry.insert(0, ', '.join(task.get('tags', [])))
        else:
            priority_combo.set('Средний')
        buttons_container = tk.Frame(footer_frame, bg=theme['hover'])
        buttons_container.pack(expand=True, fill='both', padx=20, pady=15)
        def save_task():
            title_text = title_entry.get().strip()
            if not title_text:
                messagebox.showwarning("Ошибка", "Введите название задачи!")
                title_entry.focus()
                return
            priority_name = priority_var.get()
            priority_key = 'medium'
            for key, value in PRIORITIES.items():
                if value['name'] == priority_name:
                    priority_key = key
                    break
            tags_text = tags_entry.get().strip()
            tags = [tag.strip() for tag in tags_text.split(',') if tag.strip()] if tags_text else []
            task_data = {
                'title': title_text,
                'description': desc_text.get('1.0', tk.END).strip(),
                'category': category_var.get(),
                'priority': priority_key,
                'tags': tags,
                'completed': task.get('completed', False) if is_edit else False
            }
            if due_var.get():
                due_date_text = due_date_entry.get().strip()
                try:
                    due_date = datetime.strptime(due_date_text, "%Y-%m-%d %H:%M")
                    task_data['due_date'] = due_date.isoformat()
                except ValueError:
                    messagebox.showwarning("Ошибка", 
                                         "Неверный формат даты! Используйте: ГГГГ-ММ-ДД ЧЧ:ММ")
                    due_date_entry.focus()
                    return
            if is_edit:
                task.update(task_data)
                task['updated_at'] = datetime.now().isoformat()
            else:
                task_data.update({
                    'id': max([t.get('id', 0) for t in self.tasks] + [0]) + 1,
                    'created_at': datetime.now().isoformat()
                })
                self.tasks.append(task_data)
            self.save_tasks()
            self.refresh_task_list()
            action = "обновлена" if is_edit else "создана"
            messagebox.showinfo("Успех", f"Задача '{title_text}' {action}!")
        def cancel():
            self.close_modal(modal, overlay)
        save_btn = self.create_modern_button(
            buttons_container,
            text=f"{ICONS['save']} Сохранить",
            command=lambda: [save_task(), self.close_modal(modal, overlay)],
            bg_color=theme['success'],
            hover_color=theme['success_light'],
            font_style='button',
            padding_x=25,
            padding_y=12,
            style='success'
        )
        save_btn.pack(side='right', padx=(10, 0))
        cancel_btn = self.create_modern_button(
            buttons_container,
            text=f"{ICONS['close']} Отмена",
            command=cancel,
            bg_color=theme['secondary'],
            hover_color=theme['text_muted'],
            font_style='button',
            padding_x=25,
            padding_y=12,
            style='secondary'
        )
        cancel_btn.pack(side='right')
        modal.bind('<Return>', lambda e: [save_task(), self.close_modal(modal, overlay)])
        modal.bind('<Escape>', lambda e: cancel())
        title_entry.focus()
    def change_theme(self, theme_name):
        
        self.current_theme = theme_name
        self.settings['theme'] = theme_name
        self.save_settings()
        for widget in self.root.winfo_children():
            widget.destroy()
        self.setup_styles()
        self.create_menu()
        self.create_main_interface()
        self.refresh_task_list()
        messagebox.showinfo(self.get_text('theme_changed'), f"{self.get_text('theme_applied')} {theme_name}")
    
    def change_language(self, language_code):
        
        self.current_language = language_code
        self.settings['language'] = language_code
        self.save_settings()
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_menu()
        self.create_main_interface()
        self.refresh_task_list()
        messagebox.showinfo(self.get_text('language_changed'), f"{self.get_text('language_applied')} {language_code}")
    def update_statistics(self):
        
        if not hasattr(self, 'stats_label'):
            return
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.get('completed', False))
        pending = total - completed
        now = datetime.now()
        overdue = sum(1 for task in self.tasks 
                     if not task.get('completed', False) and 
                        task.get('due_date') and 
                        datetime.fromisoformat(task['due_date']) < now)
        today = now.date()
        today_tasks = sum(1 for task in self.tasks 
                         if not task.get('completed', False) and 
                            task.get('due_date') and 
                            datetime.fromisoformat(task['due_date']).date() == today)
        stats_text = (f"📊 Всего: {total} | "
                     f"✅ Выполнено: {completed} | "
                     f"⏳ Осталось: {pending} | "
                     f"⚠️ Просрочено: {overdue} | "
                     f"📅 На сегодня: {today_tasks}")
        self.stats_label.config(text=stats_text)
    def show_statistics(self):
        
        stats_window = tk.Toplevel(self.root)
        stats_window.title("📊 Статистика")
        stats_window.geometry("600x400")
        stats_window.configure(bg=THEMES[self.current_theme]['bg'])
        frame = tk.Frame(stats_window, bg=THEMES[self.current_theme]['bg'], padx=20, pady=20)
        frame.pack(fill='both', expand=True)
        tk.Label(
            frame,
            text="📊 Подробная статистика",
            font=('Segoe UI', 16, 'bold'),
            bg=THEMES[self.current_theme]['bg'],
            fg=THEMES[self.current_theme]['text']
        ).pack(pady=(0, 20))
        category_stats = defaultdict(int)
        for task in self.tasks:
            category_stats[task.get('category', 'Без категории')] += 1
        stats_text = "Статистика по категориям:\n\n"
        for category, count in category_stats.items():
            stats_text += f"{category}: {count}\n"
        priority_stats = defaultdict(int)
        for task in self.tasks:
            priority = task.get('priority', 'low')
            priority_stats[PRIORITIES[priority]['name']] += 1
        stats_text += "\nСтатистика по приоритетам:\n\n"
        for priority, count in priority_stats.items():
            stats_text += f"{priority}: {count}\n"
        text_widget = tk.Text(
            frame,
            font=('Segoe UI', 11),
            wrap='word',
            bg=THEMES[self.current_theme]['card_bg'],
            fg=THEMES[self.current_theme]['text']
        )
        text_widget.pack(fill='both', expand=True)
        text_widget.insert('1.0', stats_text)
        text_widget.config(state='disabled')
    def export_tasks(self):
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("CSV files", "*.csv"), ("Text files", "*.txt")]
        )
        if filename:
            try:
                if filename.endswith('.json'):
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(self.tasks, f, ensure_ascii=False, indent=2)
                elif filename.endswith('.csv'):
                    import csv
                    with open(filename, 'w', newline='', encoding='utf-8') as f:
                        if self.tasks:
                            writer = csv.DictWriter(f, fieldnames=self.tasks[0].keys())
                            writer.writeheader()
                            writer.writerows(self.tasks)
                else:
                    with open(filename, 'w', encoding='utf-8') as f:
                        for task in self.tasks:
                            f.write(f"Задача: {task.get('title', '')}\n")
                            f.write(f"Описание: {task.get('description', '')}\n")
                            f.write(f"Категория: {task.get('category', '')}\n")
                            f.write(f"Приоритет: {PRIORITIES.get(task.get('priority', 'low'), {}).get('name', '')}\n")
                            f.write(f"Выполнено: {'Да' if task.get('completed') else 'Нет'}\n")
                            f.write("-" * 50 + "\n")
                messagebox.showinfo("Успех", f"Задачи экспортированы в {filename}")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось экспортировать: {e}")
    def import_tasks(self):
        
        filename = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json")]
        )
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    imported_tasks = json.load(f)
                if messagebox.askyesno("Импорт", 
                                     f"Импортировать {len(imported_tasks)} задач?"):
                    self.tasks.extend(imported_tasks)
                    self.save_tasks()
                    self.refresh_task_list()
                    messagebox.showinfo("Успех", "Задачи импортированы!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось импортировать: {e}")
    def show_shortcuts(self):
        
        shortcuts_window = tk.Toplevel(self.root)
        shortcuts_window.title("⌨️ Горячие клавиши")
        shortcuts_window.geometry("400x300")
        shortcuts_window.configure(bg=THEMES[self.current_theme]['bg'])
        frame = tk.Frame(shortcuts_window, bg=THEMES[self.current_theme]['bg'], padx=20, pady=20)
        frame.pack(fill='both', expand=True)
        shortcuts_text = """⌨️ Горячие клавиши

Ctrl+N - Новая задача
Ctrl+F - Поиск
F5 - Обновить список
Delete - Удалить выбранную задачу
Escape - Закрыть диалог
Enter - Сохранить в диалоге

🖱️ Мышь

Правый клик - Контекстное меню
Двойной клик - Редактировать задачу
Колесо мыши - Прокрутка списка"""
        text_widget = tk.Text(
            frame,
            font=('Segoe UI', 11),
            wrap='word',
            bg=THEMES[self.current_theme]['card_bg'],
            fg=THEMES[self.current_theme]['text']
        )
        text_widget.pack(fill='both', expand=True)
        text_widget.insert('1.0', shortcuts_text)
        text_widget.config(state='disabled')
    def show_about(self):
        about_text = """📝 FRKHD - Современный менеджер задач

Версия: 2.0
Дата: 2024

Функции:
• Создание и редактирование задач
• Категории и приоритеты
• Сроки выполнения
• Фильтрация и поиск
• Экспорт/импорт данных
• Настраиваемые темы
• Подробная статистика

Сделано с ❤️ на Python + tkinter"""
        messagebox.showinfo("О программе", about_text)
def main():
    
    root = tk.Tk()
    app = AdvancedTodoApp(root)
    root.mainloop()
if __name__ == "__main__":
    main() 