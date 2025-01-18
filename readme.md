
# Pet Project: Анализ продаж и построение Data Pipeline

## Цель проекта
Создать pipeline для обработки и анализа данных о продажах. Вы освоите основы ETL (Extract, Transform, Load), работу с реляционной базой данных и визуализацию данных.

---

## Основные задачи
1. **Сбор данных**: Создать CSV-файл с данными о продажах (например, магазины, категории товаров, цены, количество).
2. **ETL-процесс**:
   - **Extract**: Загрузка данных из CSV-файла.
   - **Transform**: Очистка и преобразование данных (удаление дубликатов, обработка пропущенных значений, расчет новых метрик).
   - **Load**: Загрузка данных в базу данных (PostgreSQL).
3. **Анализ данных**:
   - Написание SQL-запросов для анализа:
     - Определение самых популярных товаров.
     - Расчет выручки и прибыли по категориям.
     - Анализ продаж по времени.
4. **Визуализация данных**:
   - Использовать Python-библиотеки (Matplotlib, Seaborn) для построения графиков.

---

## Технологии
- **Языки программирования**: Python (Pandas, SQLAlchemy)
- **База данных**: PostgreSQL
- **Инструменты визуализации**: Matplotlib, Seaborn
- **Системы контроля версий**: Git

---

## Шаги реализации
### 1. Подготовка данных
Создайте CSV-файл `sales_data.csv` со следующей структурой:
```
transaction_id,store_id,product_id,category,price,quantity,sale_date
1,1,101,Electronics,100,2,2025-01-01
2,1,102,Groceries,50,5,2025-01-02
...
```

### 2. Реализация ETL
1. Загрузите данные из `sales_data.csv` в Python (используя Pandas).
2. Очистите данные:
   - Убедитесь в отсутствии дубликатов.
   - Обработайте пропущенные значения.
   - Добавьте новые столбцы, например, `total_price = price * quantity`.
3. Загрузите обработанные данные в PostgreSQL.

### 3. SQL-аналитика
Напишите SQL-запросы для анализа:
```sql
-- Выручка по категориям
SELECT category, SUM(price * quantity) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;

-- Самый популярный товар
SELECT product_id, SUM(quantity) AS total_quantity
FROM sales
GROUP BY product_id
ORDER BY total_quantity DESC
LIMIT 1;
```

### 4. Визуализация
Создайте графики:
- Выручка по категориям (гистограмма).
- Динамика продаж по времени (линейный график).

### 5. Документация
- Опишите реализацию в `README.md`.
- Сохраняйте код в репозитории GitHub.

---

## Результаты
- Data Pipeline, который обрабатывает данные о продажах.
- Готовые SQL-запросы для анализа данных.
- Графики, помогающие понять ключевые метрики бизнеса.

---

## Дополнительные задачи (по желанию)
- Добавить интеграцию с API (например, загрузка данных с внешнего источника).
- Настроить оркестрацию через Apache Airflow.
- Реализовать потоковую обработку данных с использованием Kafka.

---

## Полезные ссылки
- [Документация Pandas](https://pandas.pydata.org/docs/)
- [PostgreSQL](https://www.postgresql.org/)
- [Matplotlib](https://matplotlib.org/stable/index.html)

