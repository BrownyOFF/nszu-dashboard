# 🏥 NHSU: Analytics & Audit

**NHSU: Analytics & Audit** is a set of web tools for processing, converting, and deep visual analysis of medical reports from the National Health Service of Ukraine (NHSU).

## 📌 Project Overview
The project is designed to automate work with large volumes of NHSU data. The main feature is **full confidentiality**. All calculations and file processing occur exclusively on the client-side (in your browser). Data is never transmitted anywhere.

## 🛠 Tech Stack
- **Core:** Vanilla HTML5, CSS3, JavaScript (ES6+).
- **Design:** Custom CSS system using CSS Variables and the *Plus Jakarta Sans* font.
- **Libraries (via CDN):**
  - [SheetJS (xlsx.js)](https://sheetjs.com/) — for parsing XLSX files.
  - [Chart.js](https://www.chartjs.org/) — for building interactive charts.
- **Data Persistence:** `localStorage` for price settings.

## 📂 Structure & Components

## 🚀 Як запустити / How to Run

Проєкт використовує локальний сервер для забезпечення коректної навігації між сторінками.

### Linux & Windows:
1. Запустіть відповідний скрипт для вашої системи:
   - **Linux:** `./start.sh`
   - **Windows:** `start.bat`

Ці скрипти використовують `serve.py`, який автоматично знаходить вільний порт та відкриває головну сторінку в браузері.

*Примітка: Для роботи потрібен встановлений Python 3.*

---

### 1. ⚙️ Smart Converter (`converter.html`)
Allows you to quickly convert heavy `.xlsx` NHSU reports into a lightweight `.json` format. This is necessary for instant data loading into the analytical dashboard.
- Drag-and-drop support.
- Automatic conversion of all Excel workbook sheets.
- JSON file generation for download.

### 2. 📊 Analytics Dashboard (`index.html`)
The main SPA (Single Page Application) dashboard for analyzing the received data.
- **General Overview:** Key performance indicators and trends.
- **Error Audit:** Detailed analysis of record rejection reasons (with parsing of nested JSON from text fields).
- **Financial Impact:** Calculation of earned and lost funds based on a flexible tariff system.
- **Physician Analysis:** Ratings by income, workload, and error count.
- **Patient Portrait:** Demographic data, focusing on the pediatric population (0-17 years).
- **Record Registry:** Convenient table with pagination and tooltips for error codes.

## 🗄 Data Mapping
The system features intelligent column mapping. It automatically searches for required data (ID, date, doctor, service package, report status, errors, etc.), even if the column order in the NHSU file changes.

## 💰 Business Logic
The application implements a dynamic service cost evaluation system. You can manually configure tariffs for different NHSU packages in the "Settings" tab. These changes will be saved in your browser.

## 🚀 How to Start
1. Open `converter.html` and upload your `.xlsx` report from NHSU.
2. Download the generated `.json` file.
3. Open `index.html` and select the received `.json` file.
4. Explore the analytics!

---
**Author:** Tymur Halas ([BrownyOFF](https://github.com/BrownyOFF))

---

# 🏥 НСЗУ: Аналітика та Аудит (UA)

**НСЗУ: Аналітика та Аудит** — це набір веб-інструментів для обробки, конвертації та глибокого візуального аналізу медичних звітів Національної служби здоров'я України (НСЗУ).

## 📌 Огляд проєкту
Проєкт розроблений для автоматизації роботи з великими обсягами даних НСЗУ. Головна особливість — **повна конфіденційність**. Усі обчислення та обробка файлів відбуваються виключно на стороні клієнта (Client-side) у вашому браузері. Дані нікуди не передаються.

## 🛠 Технологічний стек
- **Основа:** Vanilla HTML5, CSS3, JavaScript (ES6+).
- **Дизайн:** Власна CSS-система з використанням CSS Variables та шрифту *Plus Jakarta Sans*.
- **Бібліотеки (через CDN):**
  - [SheetJS (xlsx.js)](https://sheetjs.com/) — для парсингу XLSX файлів.
  - [Chart.js](https://www.chartjs.org/) — для побудови інтерактивних графіків.
- **Збереження даних:** `localStorage` для налаштувань тарифів.

## 📂 Структура та компоненти

### 1. ⚙️ Розумний Конвертер (`converter.html`)
Дозволяє швидко перетворити важкі `.xlsx` звіти НСЗУ у формат `.json`.
- Підтримка Drag-and-drop.
- Автоматична конвертація всіх листів книги Excel.
- Генерація JSON-файлу для завантаження.

### 2. 📊 Дашборд Аналітики (`index.html`)
Основна SPA-панель (Single Page Application) для аналізу отриманих даних.
- **Загальний огляд:** Ключові показники успішності та тренди.
- **Аудит помилок:** Детальний аналіз причин відхилення записів.
- **Фінансовий вплив:** Розрахунок зароблених та втрачених коштів.
- **Аналіз по лікарях:** Рейтинги за доходом та навантаженням.
- **Портрет пацієнта:** Демографічні дані (діти 0-17 років).
- **Реєстр записів:** Таблиця з пагінацією та підказками.

---
**Автор:** Тимур Галас ([BrownyOFF](https://github.com/BrownyOFF))
