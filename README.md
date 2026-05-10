# 🏥 NHSU: Analytics & Audit

**NHSU: Analytics & Audit** is a powerful set of web tools for processing, converting, and deep visual analysis of medical reports from the National Health Service of Ukraine (NHSU). The project is designed to transform "dry" tables into actionable insights, helping medical institutions effectively manage finances and service quality.

---

## 📌 Key Features

- **⚙️ Smart Converter (`converter.html`):** Rapid conversion of bulky `.xlsx` reports into a lightweight `.json` format without data loss.
- **📊 Interactive Dashboard (`index.html`):** Visualization of key metrics, error auditing, and financial analysis.
- **🛡️ Full Confidentiality:** All calculations are performed on your computer (Client-side). No patient data is ever transmitted to any servers.
- **💰 Financial Control:** Automatic calculation of earned and lost funds based on a flexible tariff system.
- **👨‍⚕️ Staff Analytics:** Physician ratings by income, error count, and workload.

---

## 🚀 Quick Start

A built-in Python server is used to ensure correct local script execution and page navigation.

### Running the system:
1. Ensure you have **Python 3** installed.
2. Run the file corresponding to your OS:
   - **Windows:** Open `start.bat`
   - **Linux/macOS:** Run `sh start.sh`
3. Your browser will automatically open the main page (`main.html`).

---

## 🛠 Tech Stack

The project is built on modern web technologies without heavy frameworks, ensuring maximum performance:

- **Frontend:** Vanilla JS (ES6+), HTML5, CSS3.
- **Design:** Custom design system using CSS Variables (Plus Jakarta Sans font).
- **Data Processing:** [SheetJS (xlsx.js)](https://sheetjs.com/) — for Excel parsing.
- **Visualization:** [Chart.js](https://www.chartjs.org/) — for interactive charts.
- **Persistence:** `localStorage` for personal tariff settings.

---

## 📂 System Modules

### 1. Smart Converter
- Drag-and-drop support for file uploads.
- Automatic column detection (ID, dates, doctors, etc.).
- Converts all sheets of an Excel file into a single JSON.

### 2. Analytics Dashboard
- **General Overview:** Success metrics and report submission dynamics.
- **Error Audit:** Deep analysis of rejection reasons (parsing JSON details from NHSU).
- **Financial Impact:** Potential income calculation.
- **Patient Portrait:** Age and gender distribution.
- **Record Registry:** User-friendly table with search and error code tooltips.

---

## 📋 System Requirements

- Modern web browser (Chrome, Firefox, Edge, Safari).
- Python 3.x (for the local server).

---

**Author:** [Tymur Halas](https://github.com/BrownyOFF)

---
---

# 🏥 НСЗУ: Аналітика та Аудит (UA)

**НСЗУ: Аналітика та Аудит** — це потужний набір веб-інструментів для обробки, конвертації та глибокого візуального аналізу медичних звітів Національної служби здоров'я України (НСЗУ). Проєкт створений для того, щоб перетворити "сухі" таблиці на зрозумілі дані, допомагаючи медичним закладам ефективно управляти фінансами та якістю послуг.

---

## 📌 Основні можливості

- **⚙️ Розумний Конвертер (`converter.html`):** Швидке перетворення об'ємних `.xlsx` звітів у легкий `.json` формат без втрати даних.
- **📊 Інтерактивний Дашборд (`index.html`):** Візуалізація ключових метрик, аудит помилок та фінансовий аналіз.
- **🛡️ Повна конфіденційність:** Усі обчислення виконуються на вашому комп'ютері (Client-side). Жодні дані пацієнтів не передаються на сервери.
- **💰 Фінансовий контроль:** Автоматичний розрахунок зароблених та втрачених коштів на основі гнучкої системи тарифів.
- **👨‍⚕️ Аналітика по персоналу:** Рейтинги лікарів за доходом, кількістю помилок та завантаженістю.

---

## 🚀 Швидкий старт

Для коректної роботи локальних скриптів та переходів між сторінками використовується вбудований Python-сервер.

### Запуск системи:
1. Переконайтеся, що у вас встановлено **Python 3**.
2. Запустіть файл відповідно до вашої ОС:
   - **Windows:** Відкрийте `start.bat`
   - **Linux/macOS:** Запустіть `sh start.sh`
3. Браузер автоматично відкриє головну сторінку (`main.html`).

---

## 🛠 Технологічний стек

Проєкт побудований на сучасних веб-технологіях без використання складних фреймворків, що забезпечує максимальну швидкість роботи:

- **Frontend:** Vanilla JS (ES6+), HTML5, CSS3.
- **Дизайн:** Власна дизайн-система на CSS Variables (шрифт Plus Jakarta Sans).
- **Обробка даних:** [SheetJS (xlsx.js)](https://sheetjs.com/) — парсинг Excel.
- **Візуалізація:** [Chart.js](https://www.chartjs.org/) — інтерактивні графіки.
- **Збереження:** `localStorage` для персональних налаштувань тарифів.

---

## 📂 Модулі системи

### 1. Конвертер (Smart Converter)
- Підтримка Drag-and-drop для завантаження файлів.
- Автоматичний пошук потрібних колонок (ID, дати, лікарі тощо).
- Конвертація всіх листів Excel-файлу в один JSON.

### 2. Дашборд (Analytics Dashboard)
- **Загальний огляд:** Метрики успішності та динаміка подачі звітів.
- **Аудит помилок:** Глибокий аналіз причин відхилення записів (парсинг JSON-деталей від НСЗУ).
- **Фінансовий вплив:** Розрахунок потенційного доходу.
- **Портрет пацієнта:** Віковий та статевий розподіл.
- **Реєстр записів:** Зручна таблиця з пошуком та розшифровкою кодів помилок.

---

## 📋 Системні вимоги

- Сучасний веб-браузер (Chrome, Firefox, Edge, Safari).
- Python 3.x (для локального серверу).

---

**Автор:** [Тимур Галас](https://github.com/BrownyOFF)
