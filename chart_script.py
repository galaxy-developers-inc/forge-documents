diagram_code = '''
flowchart TD
    A["ЗВОНОК (30 мин)"] --> B["ТЗ-АВТОГЕНЕРАТОР (30 мин)"]
    B --> C["ВЫБОР АРХЕТИПОВ (5 template'ов)"]

    C --> C1["Dashboard"]
    C --> C2["Form Engine"]
    C --> C3["Analytics"]
    C --> C4["Automation"]
    C --> C5["CRM"]

    C --> D["КОМБИНИРОВАНИЕ + ИНТЕГРАЦИИ"]

    D --> D1["Slack"]
    D --> D2["Email"]
    D --> D3["Google Sheets"]
    D --> D4["1C"]
    D --> D5["Другие"]

    D --> E["РАЗРАБОТКА (2-3 дня)"]

    E --> E1["Backend (Вася)"]
    E --> E2["Frontend (Маша)"]
    E --> E3["Параллельная работа"]

    E --> F["ДЕПЛОЙ (1 день)"]

    F --> F1["Setup ВМ (Саша)"]
    F --> F2["Docker/Nginx"]
    F --> F3["SSL/домен"]

    F --> G["✅ LIVE на их домене"]
    G --> H["30 ДНЕЙ ПОДДЕРЖКИ"]
    H --> H1["Баг-фиксы"]
    H --> H2["Консультация"]
'''

png_path, svg_path = create_mermaid_diagram(diagram_code, 'chart.png', 'chart.svg')

print(f"PNG saved to: {png_path}")
print(f"SVG saved to: {svg_path}")
