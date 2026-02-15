# 🧩 SYSTEM TEMPLATES: АРХЕТИПЫ ГОТОВЫХ РЕШЕНИЙ

## 🎯 ГЛАВНАЯ ИДЕЯ

**Не писать каждый раз с нуля. Копируешь архетип → адаптируешь под клиента → deploy.**

У нас есть **5 главных архетипов**, каждый = минимум 10-15 вариантов клиентов.

---

## 📊 АРХЕТИП 1: DASHBOARD (дашборд контроля)

**ДЛЯ ЧЕГ О:** Любой собственник хочет видеть бизнес за одним экраном

**ПРИМЕРЫ КЛИЕНТОВ:**
- SPA салон (выручка, очередь, мастера)
- Интернет-магазин (продажи, остатки, возвраты)
- Строй-компания (проекты, бюджет, сроки)
- Ресторан (заказы, кухня, доставка)
- Логистика (грузы, маршруты, время)

### СТРУКТУРА КОДА

```
/dashboard-api/
├── routes/
│   ├── metrics.js         GET /api/metrics/kpi
│   ├── timeline.js        GET /api/timeline/revenue
│   └── alerts.js          GET /api/alerts
├── models/
│   ├── KPI.js
│   ├── TimeSeries.js
│   └── Alert.js
├── services/
│   ├── calculationEngine.js    (считаем метрики)
│   └── alertingService.js      (алерты)
└── config/
    └── metrics-schema.json     (какие метрики показываем)

/dashboard-ui/
├── components/
│   ├── DashboardLayout.jsx
│   ├── MetricCard.jsx          (красивая карточка)
│   ├── Chart.jsx               (график)
│   ├── Table.jsx               (таблица)
│   ├── AlertBanner.jsx         (красный флаг)
│   └── KPIFooter.jsx           (итоги)
├── pages/
│   ├── Dashboard.jsx           (главная страница)
│   ├── Settings.jsx            (выбор метрик)
│   └── History.jsx             (история значений)
└── hooks/
    └── useMetrics.js           (подтягиваем данные)
```

### ЧТО БЫСТРО МЕНЯЕТСЯ ДЛЯ КАЖДОГО КЛИЕНТА

1. **metrics-schema.json** (какие показатели показываем)
   ```json
   {
     "kpis": [
       {"name": "revenue", "unit": "₽", "target": 100000},
       {"name": "queue", "unit": "шт", "target": 10},
       {"name": "cancellations", "unit": "%", "target": 5}
     ]
   }
   ```

2. **data-source.js** (откуда берём данные)
   - Для SPA салона: из 1C / Google Sheets
   - Для ИМ: из Shopify API / 1C
   - Для строй-компании: из их CRM

3. **colors + branding** (их лого и цвета)
   - src/config/branding.json
   - Основной цвет: #FF6B35
   - Лого: их логотип

4. **notifications** (куда отправляем алерты)
   - Slack: #sales канал
   - Email: boss@company.ru
   - SMS: +7-XXX-XXX

### ПРОТОТИП (30 МИН)

```bash
# Создаём проект из template
git clone https://github.com/galaxy/template-dashboard new-dashboard
cd new-dashboard

# Адаптируем под клиента
nano config/metrics-schema.json      # Выбираем KPI
nano config/branding.json            # Лого и цвета
nano config/data-source.json         # Откуда данные берём

# Запускаем
docker-compose up
# Dashboard готов на localhost:3000

# Деплоим
docker build . -t newclient:latest
docker push registry.galaxy.io/newclient:latest
# Deploy на их ВМ
```

### ПРИМЕРЫ МЕТРИК ДЛЯ РАЗНЫХ БИЗНЕСОВ

**SPA САЛОН:**
- Выручка за день
- Среднее время услуги
- Загрузка мастеров
- Количество отмен

**ИНТЕРНЕТ-МАГАЗИН:**
- Заказы за день
- Средний чек
- Возвраты
- Конверсия

**ЛОГИСТИКА:**
- Активные маршруты
- Время в пути
- Доставлено вчера
- Опозданий

---

## 📝 АРХЕТИП 2: FORM ENGINE (сбор данных)

**ДЛЯ ЧЕГО:** Когда клиентам нужно вводить данные в систему

**ПРИМЕРЫ КЛИЕНТОВ:**
- Продажи (форма заказа)
- HR (форма найма)
- Поддержка (форма тикета)
- Строй-сметы (форма расчёта)

### СТРУКТУРА КОДА

```
/form-engine-api/
├── routes/
│   ├── forms.js          GET /api/forms/:id
│   ├── submissions.js    POST /api/forms/:id/submit
│   └── validation.js     POST /api/forms/:id/validate
├── models/
│   ├── Form.js
│   ├── Field.js
│   └── Submission.js
├── services/
│   ├── validationEngine.js    (проверяем данные)
│   ├── workflowEngine.js      (что делать после формы)
│   └── notificationService.js (отправляем результаты)
└── config/
    └── form-templates/        (готовые формы)
        ├── order-form.json
        ├── ticket-form.json
        └── hiring-form.json

/form-engine-ui/
├── components/
│   ├── FormRenderer.jsx   (рисует форму)
│   ├── FieldBuilder.jsx   (конструктор полей)
│   └── FieldTypes/
│       ├── Text.jsx
│       ├── Dropdown.jsx
│       ├── DatePicker.jsx
│       └── FileUpload.jsx
└── pages/
    ├── FormView.jsx       (главная форма)
    └── FormBuilder.jsx    (админка - редактирование форм)
```

### ГОТОВЫЕ ШАБЛОНЫ ФОРМ

```json
// forms/order-form.json
{
  "id": "order-form",
  "title": "Новый заказ",
  "fields": [
    {
      "id": "client-name",
      "type": "text",
      "label": "ФИО клиента",
      "required": true
    },
    {
      "id": "product",
      "type": "dropdown",
      "label": "Выберите услугу",
      "options": ["Услуга 1", "Услуга 2"],
      "required": true
    },
    {
      "id": "date",
      "type": "date",
      "label": "Дата услуги",
      "required": true
    }
  ],
  "actions": [
    {
      "type": "slack",
      "channel": "#new-orders",
      "message": "Новый заказ от {client-name}"
    },
    {
      "type": "email",
      "to": "orders@company.ru",
      "subject": "Новый заказ"
    },
    {
      "type": "webhook",
      "url": "https://their-system.com/webhook",
      "method": "POST"
    }
  ]
}
```

### АДАПТАЦИЯ ДЛЯ КЛИЕНТА (30 МИН)

```bash
# Копируем base
git clone https://github.com/galaxy/template-form-engine new-form

# Создаём form-schema.json под их процесс
cat > config/form-schema.json << 'EOF'
{
  "title": "Форма заказа для салона",
  "fields": [
    {"id": "name", "type": "text", "label": "Имя клиента"},
    {"id": "phone", "type": "tel", "label": "Телефон"},
    {"id": "service", "type": "dropdown", "label": "Услуга", 
     "options": ["Стрижка", "Окрас", "Укладка"]},
    {"id": "date", "type": "date", "label": "Дата"},
    {"id": "master", "type": "dropdown", "label": "Мастер",
     "options": ["Елена", "Марина", "Ольга"]}
  ],
  "actions": [
    {"type": "slack", "channel": "#orders"},
    {"type": "email", "to": "salon@email.ru"}
  ]
}
EOF

# Запускаем
npm start

# Deploy
```

---

## 📊 АРХЕТИП 3: ANALYTICS ENGINE (анализ данных)

**ДЛЯ ЧЕГО:** Когда нужны тренды, прогнозы, рекомендации

**ПРИМЕРЫ КЛИЕНТОВ:**
- Интернет-магазин (спрос, цены, рекомендации)
- Маркетинг (метрики кампаний)
- HR (производительность команды)
- Финансы (прогноз cash flow)

### СТРУКТУРА КОДА

```
/analytics-engine/
├── routes/
│   ├── trends.js         GET /api/analytics/trends
│   ├── forecast.js       GET /api/analytics/forecast
│   ├── recommendations.js GET /api/analytics/recommendations
│   └── cohorts.js        GET /api/analytics/cohorts
├── services/
│   ├── trendAnalyzer.js       (линейный тренд)
│   ├── forecastEngine.js      (ARIMA / Prophet)
│   ├── recommendationEngine.js (ИИ рекомендации)
│   └── cohortAnalyzer.js      (сегментация)
├── ml/
│   ├── models/
│   │   ├── demand-forecast.pkl    (обученная модель)
│   │   └── churn-prediction.pkl
│   └── training/
│       ├── train-demand.py
│       └── train-churn.py
└── data/
    └── seed-data.csv           (примеры для обучения)
```

### ПРИМЕРЫ АНАЛИТИКИ

**ДЛЯ ИНТЕРНЕТ-МАГАЗИНА:**
```json
{
  "trend": {
    "metric": "sales",
    "direction": "up",
    "percent_change": 23,
    "forecast": "Скорее всего рост продолжится"
  },
  "recommendations": [
    {
      "action": "raise_prices",
      "reason": "Спрос выше предложения",
      "potential_revenue": "+50k ₽/месяц"
    },
    {
      "action": "restock_product_X",
      "reason": "Почти закончились",
      "lead_time": "3 дня"
    }
  ]
}
```

**ДЛЯ HR:**
```json
{
  "team_performance": {
    "average_output": 95,
    "top_performer": "Иван (+15%)",
    "at_risk": ["Петр (-30%)"]
  },
  "recommendations": [
    {
      "action": "interview_peter",
      "reason": "Снизилась производительность",
      "impact": "Возможен уход сотрудника"
    }
  ]
}
```

---

## 🤖 АРХЕТИП 4: AUTOMATION ENGINE (автоматизация процессов)

**ДЛЯ ЧЕГО:** Когда рутину можно автоматизировать

**ПРИМЕРЫ КЛИЕНТОВ:**
- Email рассылки
- Slack/Telegram боты
- Синхронизация систем
- Расписание задач

### СТРУКТУРА КОДА

```
/automation-engine/
├── routes/
│   ├── workflows.js      GET/POST /api/workflows
│   ├── triggers.js       GET /api/triggers
│   └── actions.js        GET /api/actions
├── services/
│   ├── workflowExecutor.js    (выполняем workflow)
│   ├── triggerManager.js      (следим за триггерами)
│   └── actionExecutor.js      (выполняем экшены)
├── connectors/
│   ├── slack.js          (интеграция со Slack)
│   ├── email.js          (email API)
│   ├── webhooks.js       (external webhooks)
│   ├── crm.js            (их CRM)
│   └── sheets.js         (Google Sheets)
└── workflows/            (готовые workflows)
    ├── daily-report.json
    ├── new-order-alert.json
    └── sync-crm-to-sheets.json
```

### ПРИМЕРЫ WORKFLOWS

**WORKFLOW 1: Daily Report**
```json
{
  "id": "daily-report",
  "name": "Ежедневный отчёт",
  "trigger": {
    "type": "schedule",
    "time": "21:00"
  },
  "actions": [
    {
      "type": "collect",
      "from": "dashboard_api",
      "what": "kpi_of_today"
    },
    {
      "type": "generate",
      "format": "email_html"
    },
    {
      "type": "send",
      "to": "boss@company.ru"
    }
  ]
}
```

**WORKFLOW 2: New Order Alert**
```json
{
  "id": "order-alert",
  "name": "Алерт новых заказов",
  "trigger": {
    "type": "webhook",
    "url": "/api/webhook/new-order"
  },
  "actions": [
    {
      "type": "send_slack",
      "channel": "#sales",
      "message": "🔔 Новый заказ: {order_id} от {client_name}"
    },
    {
      "type": "send_email",
      "to": "team@company.ru",
      "subject": "New Order Alert"
    }
  ]
}
```

**WORKFLOW 3: Sync CRM to Sheets**
```json
{
  "id": "crm-to-sheets",
  "name": "Синхронизация CRM → Google Sheets",
  "trigger": {
    "type": "schedule",
    "interval": "every_hour"
  },
  "actions": [
    {
      "type": "fetch",
      "from": "crm_api",
      "what": "deals_updated_today"
    },
    {
      "type": "transform",
      "format": "csv"
    },
    {
      "type": "upload_to_sheets",
      "sheet_id": "xxx",
      "worksheet": "deals"
    }
  ]
}
```

---

## 🤝 АРХЕТИП 5: CRM ENGINE (управление взаимоотношениями)

**ДЛЯ ЧЕГО:** Когда нужна база клиентов, сделок, истории

**ПРИМЕРЫ КЛИЕНТОВ:**
- Продажи (B2B CRM)
- Сервис (ticketing system)
- Агентства (клиенты + проекты)

### СТРУКТУРА КОДА

```
/crm-api/
├── routes/
│   ├── clients.js        CRUD /api/clients
│   ├── deals.js          CRUD /api/deals
│   ├── interactions.js   CRUD /api/interactions
│   ├── pipeline.js       GET /api/pipeline (воронка)
│   └── reports.js        GET /api/reports
├── models/
│   ├── Client.js         (компания / человек)
│   ├── Deal.js           (сделка)
│   ├── Interaction.js    (встреча / звонок / email)
│   ├── Task.js           (задача)
│   └── Note.js           (заметка)
├── services/
│   ├── pipelineEngine.js     (воронка продаж)
│   ├── forecastService.js    (прогноз доходов)
│   └── automationService.js  (авто-задачи)
└── config/
    └── crm-schema.json   (структура данных)

/crm-ui/
├── components/
│   ├── ClientList.jsx
│   ├── DealCard.jsx
│   ├── PipelineBoard.jsx (Kanban)
│   ├── InteractionTimeline.jsx
│   └── ReportGenerator.jsx
└── pages/
    ├── Clients.jsx
    ├── Deals.jsx
    ├── Pipeline.jsx
    └── Reports.jsx
```

---

## 🔧 КАК ИСПОЛЬЗОВАТЬ АРХЕТИПЫ

### СЦЕНАРИЙ: У КЛИЕНТА НУЖЕН DASHBOARD + FORM

```bash
# ШАГ 1: Выбираем архетипы
Template 1 = Dashboard
Template 2 = Form Engine

# ШАГ 2: Копируем оба
git clone https://github.com/galaxy/template-dashboard-api dashboard-api
git clone https://github.com/galaxy/template-form-engine-api form-api

# ШАГ 3: Создаём docker-compose.yml
cat > docker-compose.yml << 'EOF'
version: '3'
services:
  dashboard-api:
    build: ./dashboard-api
    ports: ["3001:3000"]
    env_file: .env
  
  form-api:
    build: ./form-api
    ports: ["3002:3000"]
    env_file: .env
  
  db:
    image: postgres:14
    environment:
      POSTGRES_PASSWORD: pass
    volumes:
      - postgres_data:/var/lib/postgresql/data

  ui:
    build: ./ui
    ports: ["3000:3000"]
    environment:
      VITE_DASHBOARD_API: http://localhost:3001
      VITE_FORM_API: http://localhost:3002

volumes:
  postgres_data:
EOF

# ШАГ 4: Адаптируем под клиента
echo "DASHBOARD_METRICS=revenue,queue,cancellations" >> .env
echo "FORM_SCHEMA=salon-order" >> .env

# ШАГ 5: Запускаем
docker-compose up

# ШАГ 6: Деплоим
docker-compose push
```

---

## 📚 АРХЕТИПЫ + ИНТЕГРАЦИИ

Каждый архетип можно комбинировать с интеграциями:

### DASHBOARD + интеграции
- Google Sheets (читаем метрики)
- Slack (отправляем алерты)
- 1C (читаем финансы)
- Stripe (читаем платежи)

### FORM ENGINE + интеграции
- Email (отправляем подтверждение)
- Slack (уведомляем команду)
- CRM (создаём контакт)
- Webhook (отправляем в их систему)

### ANALYTICS ENGINE + интеграции
- ИИ (Claude / GPT для рекомендаций)
- BigQuery (большие данные)
- Metabase / BI (красивые графики)

### AUTOMATION ENGINE + интеграции
- Все остальные

### CRM ENGINE + интеграции
- Email (отправляем письма)
- SMS (отправляем SMS)
- Calendar (создаём события)
- Zapier (интегрируем с кем угодно)

---

## 💾 БАЗА ИНТЕГРАЦИЙ

```
/connectors/
├── google-sheets/
│   ├── auth.js
│   ├── reader.js       (читаем данные)
│   └── writer.js       (пишем данные)
├── slack/
│   ├── sender.js       (отправляем сообщения)
│   └── commands.js     (команды из Slack)
├── email/
│   ├── smtp.js         (отправляем email)
│   └── templates/      (шаблоны писем)
├── 1c/
│   ├── auth.js         (Oauth)
│   ├── reader.js       (читаем их БД)
│   └── writer.js       (пишем)
├── crm/
│   ├── salesforce.js
│   ├── hubspot.js
│   └── pipedrive.js
├── payment/
│   ├── stripe.js
│   ├── yookassa.js
│   └── paypal.js
├── communication/
│   ├── telegram.js
│   ├── whatsapp.js
│   └── sms.js
└── external/
    ├── webhook.js      (их вебхуки)
    ├── api-client.js   (их API)
    └── json-rest.js    (generic REST)
```

---

## 🎯 ИТОГОВАЯ СХЕМА

```
КЛИЕНТ ЗВОНИТ
        ↓
ВЫЖИМАЕМ ТЗ
        ↓
ВЫБИРАЕМ АРХЕТИПЫ (Dashboard? Form? Analytics?)
        ↓
КОПИРУЕМ TEMPLATES
        ↓
АДАПТИРУЕМ (30-60 мин)
        ↓
ДОБАВЛЯЕМ ИНТЕГРАЦИИ (30-60 мин)
        ↓
ТЕСТИРУЕМ (1-2 часа)
        ↓
ДЕПЛОИМ
        ↓
LIVE на их домене за 3 дня
        ↓
✅ ГОТОВО
```

---

## 📈 СКОРОСТЬ РАЗРАБОТКИ С АРХЕТИПАМИ

### БЕЗ АРХЕТИПОВ:
- Dashboard с нуля: 3-4 дня
- Form engine с нуля: 2-3 дня
- Интеграции: 1-2 дня каждая
- **ИТОГО: 1-2 недели**

### С АРХЕТИПАМИ:
- Dashboard из template: 4-6 часов
- Form engine из template: 2-3 часа
- Интеграции (уже готовые): 1-2 часа
- **ИТОГО: 1-2 дня**

**УСКОРЕНИЕ: 5-7х раз**

---

**Это LEGO. Каждый кирпичик уже готов. Собираешь дом за день.**

🏗️

