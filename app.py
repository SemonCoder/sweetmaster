import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Настройка страницы
st.set_page_config(
    page_title="SweetMaster - Кондитерская",
    layout="wide",
    page_icon="🧁",
    initial_sidebar_state="expanded"
)

# CSS стили
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff5e6 0%, #ffe0cc 50%, #ffd4b8 100%);
    }
    h1, h2, h3 {
        background: linear-gradient(135deg, #d48c4a 0%, #c47b3a 50%, #e8a96a 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700 !important;
    }
    .stButton button {
        background: linear-gradient(135deg, #e8a96a 0%, #d48c4a 100%);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 10px 24px;
        font-weight: 600;
    }
    .stMetric {
        background: rgba(255,248,240,0.95);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(212, 140, 74, 0.3);
    }
    .welcome-card {
        text-align: center;
        padding: 40px 20px;
        background: rgba(255,248,240,0.7);
        border-radius: 30px;
        margin: 20px 0;
    }
    .menu-card {
        background: rgba(255,248,240,0.9);
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid rgba(212, 140, 74, 0.3);
    }
    .author-info {
        background: rgba(255,248,240,0.95);
        border-radius: 20px;
        padding: 15px;
        margin-top: 20px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Инициализация данных
if 'products' not in st.session_state:
    st.session_state.products = [
        {"ID": 104, "Название": "Медовик нежный", "Категория": "Торты", "Вес": "1кг", "Вес_кг": 1.0, "Цена": 850,
         "Себестоимость": 420, "Остаток": 5, "Популярность": 90, "Срок_годности_часов": 72, "Ручная_работа_минут": 45},
        {"ID": 109, "Название": "Наполеон хрустящий", "Категория": "Торты", "Вес": "1кг", "Вес_кг": 1.0, "Цена": 920,
         "Себестоимость": 450, "Остаток": 4, "Популярность": 94, "Срок_годности_часов": 48, "Ручная_работа_минут": 50},
        {"ID": 101, "Название": "Тирамису классический", "Категория": "Пирожные", "Вес": "200г", "Вес_кг": 0.2,
         "Цена": 320, "Себестоимость": 180, "Остаток": 15, "Популярность": 95, "Срок_годности_часов": 48,
         "Ручная_работа_минут": 15},
        {"ID": 105, "Название": "Чизкейк Нью-Йорк", "Категория": "Пирожные", "Вес": "250г", "Вес_кг": 0.25, "Цена": 380,
         "Себестоимость": 200, "Остаток": 7, "Популярность": 96, "Срок_годности_часов": 48, "Ручная_работа_минут": 20},
        {"ID": 110, "Название": "Капкейк с вишней", "Категория": "Капкейки", "Вес": "120г", "Вес_кг": 0.12, "Цена": 160,
         "Себестоимость": 60, "Остаток": 15, "Популярность": 87, "Срок_годности_часов": 48, "Ручная_работа_минут": 7},
        {"ID": 103, "Название": "Круассан с шоколадом", "Категория": "Выпечка", "Вес": "120г", "Вес_кг": 0.12,
         "Цена": 150, "Себестоимость": 65, "Остаток": 18, "Популярность": 88, "Срок_годности_часов": 8,
         "Ручная_работа_минут": 5},
        {"ID": 102, "Название": "Макаронс клубничные", "Категория": "Печенье", "Вес": "150г", "Вес_кг": 0.15,
         "Цена": 180, "Себестоимость": 70, "Остаток": 24, "Популярность": 92, "Срок_годности_часов": 72,
         "Ручная_работа_минут": 8},
    ]

if 'sales' not in st.session_state:
    sales_data = []
    today = datetime.now()
    for i in range(300):
        prod = random.choice(st.session_state.products)
        days_ago = random.randint(0, 60)
        sale_date = (today - timedelta(days=days_ago)).strftime("%Y-%m-%d")
        qty = random.randint(1, 3)
        sales_data.append({
            "Дата": sale_date,
            "ID": prod["ID"],
            "Название": prod["Название"],
            "Категория": prod["Категория"],
            "Количество": qty,
            "Сумма": prod["Цена"] * qty
        })
    st.session_state.sales = sales_data

if 'role' not in st.session_state:
    st.session_state.role = None


def login():
    with st.sidebar:
        st.markdown("### 🧁 Добро пожаловать!")
        username = st.text_input("👤 Логин", placeholder="Введите логин")
        password = st.text_input("🔒 Пароль", type="password", placeholder="Введите пароль")
        if st.button("🍰 Войти", use_container_width=True):
            if username == "Admin" and password == "12345678":
                st.session_state.role = "Админ"
                st.rerun()
            elif username == "Mened" and password == "1234567":
                st.session_state.role = "Менеджер"
                st.rerun()
            else:
                st.error("❌ Неверный логин или пароль")


def logout():
    st.session_state.role = None
    st.rerun()


# Основной интерфейс
st.title("🧁 SweetMaster")
st.caption("✨ Учёт кондитерских изделий и сладостей ✨")

if st.session_state.role is None:
    login()
    st.info("🍪 Добро пожаловать! Авторизуйтесь в боковой панели")
else:
    with st.sidebar:
        st.markdown(f"### 👩‍🍳 Привет, {st.session_state.role}!")
        if st.button("🚪 Выйти", use_container_width=True):
            logout()
        st.markdown("---")
        if st.session_state.role == "Админ":
            menu = ["🏠 Главная", "🍰 Наши десерты", "💸 Продажи", "📈 Общая аналитика", "📊 ABC/XYZ анализ",
                    "💰 Финансовый анализ", "🎯 Маркетинговый анализ", "🔧 Производственная аналитика", "➕ Новый десерт",
                    "📱 Мобильная версия"]
        else:
            menu = ["🏠 Главная", "🍰 Наши десерты", "💸 Продажи", "📈 Общая аналитика", "📱 Мобильная версия"]
        choice = st.radio("", menu, label_visibility="collapsed")
        st.markdown("---")
        st.info("🕐 ПН-ВС: 10:00 - 21:00")

    df_products = pd.DataFrame(st.session_state.products)
    df_sales = pd.DataFrame(st.session_state.sales)

    # ГЛАВНАЯ
    if choice == "🏠 Главная":
        st.markdown("""
        <div class="welcome-card">
            <div style="font-size: 64px;">🧁🍰🎂</div>
            <h1>Добро пожаловать в SweetMaster!</h1>
            <p style="font-size: 18px; color: #8b5a2b;">Ваша система учёта кондитерских изделий и сладостей</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("🍰 Всего товаров", len(df_products))
        with col2:
            st.metric("📦 Категорий", len(df_products['Категория'].unique()))
        with col3:
            st.metric("💰 Общая выручка", f"{df_sales['Сумма'].sum():,.0f} ₽")
        with col4:
            st.metric("🧾 Всего продаж", len(df_sales))

        st.subheader("🏆 Топ-5 продаваемых товаров")
        top = df_sales.groupby('Название')['Количество'].sum().sort_values(ascending=False).head(5)
        if not top.empty:
            fig = px.bar(x=top.values, y=top.index, orientation='h', color=top.values, color_continuous_scale='oranges')
            fig.update_layout(height=300, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

    # НАШИ ДЕСЕРТЫ
    elif choice == "🍰 Наши десерты":
        st.header("🍰 Наши сладости")
        col1, col2 = st.columns(2)
        with col1:
            cat_filter = st.selectbox("Категория", ["Все"] + sorted(df_products["Категория"].unique()))
        with col2:
            sort_by = st.selectbox("Сортировка", ["По названию", "По цене (возр.)", "По цене (убыв.)"])

        df_filtered = df_products.copy()
        if cat_filter != "Все":
            df_filtered = df_filtered[df_filtered["Категория"] == cat_filter]
        if sort_by == "По цене (возр.)":
            df_filtered = df_filtered.sort_values("Цена")
        elif sort_by == "По цене (убыв.)":
            df_filtered = df_filtered.sort_values("Цена", ascending=False)
        else:
            df_filtered = df_filtered.sort_values("Название")

        display = df_filtered[['Название', 'Категория', 'Вес', 'Цена', 'Остаток', 'Популярность']].copy()
        display['Цена'] = display['Цена'].apply(lambda x: f"{x:,.0f} ₽")
        st.dataframe(display, use_container_width=True)

    # ПРОДАЖИ
    elif choice == "💸 Продажи":
        st.header("💸 Оформление заказа")
        available = [p for p in st.session_state.products if p["Остаток"] > 0]
        if available:
            prod_options = {f"{p['Название']} - {p['Цена']} ₽": p for p in available}
            selected = st.selectbox("Выберите десерт", list(prod_options.keys()))
            prod = prod_options[selected]
            qty = st.number_input("Количество", 1, prod["Остаток"], 1)
            if st.button("Подтвердить заказ"):
                prod["Остаток"] -= qty
                st.session_state.sales.append({
                    "Дата": datetime.now().strftime("%Y-%m-%d"),
                    "ID": prod["ID"],
                    "Название": prod["Название"],
                    "Категория": prod["Категория"],
                    "Количество": qty,
                    "Сумма": prod["Цена"] * qty
                })
                st.balloons()
                st.success("Заказ оформлен!")
                st.rerun()
        else:
            st.warning("Товаров нет в наличии")

    # ОБЩАЯ АНАЛИТИКА
    elif choice == "📈 Общая аналитика":
        st.header("Общая аналитика")
        cat_sales = df_sales.groupby('Категория').agg({'Сумма': 'sum', 'Количество': 'sum'}).reset_index()
        fig = px.bar(cat_sales, x='Категория', y='Сумма', title='Выручка по категориям', color='Сумма',
                     color_continuous_scale='oranges')
        st.plotly_chart(fig, use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            fig2 = px.pie(cat_sales, values='Количество', names='Категория', title='Доля продаж')
            st.plotly_chart(fig2, use_container_width=True)
        with col2:
            st.dataframe(cat_sales, use_container_width=True)

    # ABC/XYZ АНАЛИЗ
    elif choice == "📊 ABC/XYZ анализ" and st.session_state.role == "Админ":
        st.header("ABC/XYZ анализ")
        st.info("📊 Модуль показывает распределение товаров по категориям A/B/C (по выручке) и X/Y/Z (по стабильности)")

        sales_by_product = df_sales.groupby('ID').agg({'Сумма': 'sum', 'Количество': 'sum'}).reset_index()
        analysis = df_products.merge(sales_by_product, on='ID', how='left').fillna(0)
        total = analysis['Сумма'].sum()
        analysis['Доля'] = analysis['Сумма'] / total * 100
        analysis = analysis.sort_values('Сумма', ascending=False)
        analysis['Накоплено'] = analysis['Доля'].cumsum()


        def get_abc(row):
            if row['Накоплено'] <= 70:
                return 'A'
            elif row['Накоплено'] <= 90:
                return 'B'
            return 'C'


        analysis['ABC'] = analysis.apply(get_abc, axis=1)
        st.dataframe(analysis[['Название', 'Категория', 'Цена', 'Сумма', 'Доля', 'ABC']], use_container_width=True)

    # ФИНАНСОВЫЙ АНАЛИЗ (РАБОТАЮЩИЙ МОДУЛЬ)
    elif choice == "💰 Финансовый анализ" and st.session_state.role == "Админ":
        st.header("💰 Финансовый анализ")

        # Расчет финансовых показателей
        total_revenue = df_sales['Сумма'].sum()

        # Расчет себестоимости и прибыли по каждому товару
        product_finance = []
        for product in st.session_state.products:
            product_sales = df_sales[df_sales['ID'] == product['ID']]
            revenue = product_sales['Сумма'].sum()
            quantity_sold = product_sales['Количество'].sum()
            cost = product['Себестоимость'] * quantity_sold
            gross_profit = revenue - cost
            margin = (gross_profit / revenue * 100) if revenue > 0 else 0

            product_finance.append({
                'Товар': product['Название'],
                'Категория': product['Категория'],
                'Выручка': revenue,
                'Себестоимость': cost,
                'Валовая прибыль': gross_profit,
                'Маржинальность %': margin
            })

        df_finance = pd.DataFrame(product_finance)
        total_cost = df_finance['Себестоимость'].sum()
        total_profit = df_finance['Валовая прибыль'].sum()
        avg_margin = (total_profit / total_revenue * 100) if total_revenue > 0 else 0

        # Метрики
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📊 Общая выручка", f"{total_revenue:,.0f} ₽")
        with col2:
            st.metric("💰 Общая себестоимость", f"{total_cost:,.0f} ₽")
        with col3:
            st.metric("💎 Валовая прибыль", f"{total_profit:,.0f} ₽", delta=f"{avg_margin:.1f}% маржа")
        with col4:
            st.metric("📈 Средняя маржинальность", f"{avg_margin:.1f}%")

        # График прибыли по товарам
        st.subheader("💵 Прибыль по товарам")
        fig_profit = px.bar(df_finance.sort_values('Валовая прибыль', ascending=False).head(10),
                            x='Товар', y='Валовая прибыль', color='Маржинальность %',
                            color_continuous_scale='oranges', title='Топ-10 товаров по валовой прибыли')
        fig_profit.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_profit, use_container_width=True)

        # Маржинальность по категориям
        st.subheader("🏷️ Маржинальность по категориям")
        cat_margin = df_finance.groupby('Категория').agg({
            'Выручка': 'sum',
            'Себестоимость': 'sum',
            'Валовая прибыль': 'sum'
        }).reset_index()
        cat_margin['Маржинальность %'] = (cat_margin['Валовая прибыль'] / cat_margin['Выручка'] * 100).fillna(0)

        fig_margin = px.pie(cat_margin, values='Валовая прибыль', names='Категория',
                            title='Распределение прибыли по категориям', hole=0.4)
        st.plotly_chart(fig_margin, use_container_width=True)

        # Таблица с детальной финансовой информацией
        st.subheader("📋 Детальный финансовый анализ")
        df_display = df_finance.sort_values('Валовая прибыль', ascending=False)
        df_display['Выручка'] = df_display['Выручка'].apply(lambda x: f"{x:,.0f} ₽")
        df_display['Себестоимость'] = df_display['Себестоимость'].apply(lambda x: f"{x:,.0f} ₽")
        df_display['Валовая прибыль'] = df_display['Валовая прибыль'].apply(lambda x: f"{x:,.0f} ₽")
        df_display['Маржинальность %'] = df_display['Маржинальность %'].apply(lambda x: f"{x:.1f}%")
        st.dataframe(df_display, use_container_width=True)

    # МАРКЕТИНГОВЫЙ АНАЛИЗ (РАБОТАЮЩИЙ МОДУЛЬ)
    elif choice == "🎯 Маркетинговый анализ" and st.session_state.role == "Админ":
        st.header("🎯 Маркетинговый анализ")

        # Анализ популярности товаров
        popularity_data = []
        for product in st.session_state.products:
            product_sales = df_sales[df_sales['ID'] == product['ID']]
            quantity_sold = product_sales['Количество'].sum()
            revenue = product_sales['Сумма'].sum()

            popularity_data.append({
                'Товар': product['Название'],
                'Категория': product['Категория'],
                'Продано шт': quantity_sold,
                'Выручка': revenue,
                'Популярность (оценка)': product['Популярность'],
                'Цена': product['Цена']
            })

        df_popularity = pd.DataFrame(popularity_data)

        # Метрики
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            avg_popularity = df_popularity['Популярность (оценка)'].mean()
            st.metric("⭐ Средняя популярность", f"{avg_popularity:.1f}/100")
        with col2:
            best_seller = df_popularity.loc[df_popularity['Продано шт'].idxmax(), 'Товар'] if len(
                df_popularity) > 0 else "Нет"
            st.metric("🏆 Самый продаваемый", best_seller)
        with col3:
            total_units = df_popularity['Продано шт'].sum()
            st.metric("🍰 Всего продано", f"{total_units:,} шт")
        with col4:
            avg_price = df_popularity['Цена'].mean()
            st.metric("💵 Средний чек", f"{avg_price:,.0f} ₽")

        # График популярности vs продажи
        st.subheader("📊 Связь популярности и продаж")
        fig_pop = px.scatter(df_popularity, x='Популярность (оценка)', y='Продано шт',
                             size='Выручка', color='Категория', hover_name='Товар',
                             title='Зависимость продаж от популярности товара',
                             labels={'Популярность (оценка)': 'Популярность (из 100)',
                                     'Продано шт': 'Количество продаж'})
        st.plotly_chart(fig_pop, use_container_width=True)

        # Продажи по категориям
        st.subheader("📈 Анализ продаж по категориям")
        cat_sales_marketing = df_popularity.groupby('Категория').agg({
            'Продано шт': 'sum',
            'Выручка': 'sum'
        }).reset_index()

        col1, col2 = st.columns(2)
        with col1:
            fig_cat_sales = px.bar(cat_sales_marketing, x='Категория', y='Продано шт',
                                   title='Продажи по категориям (шт)', color='Продано шт',
                                   color_continuous_scale='oranges')
            st.plotly_chart(fig_cat_sales, use_container_width=True)
        with col2:
            fig_cat_rev = px.bar(cat_sales_marketing, x='Категория', y='Выручка',
                                 title='Выручка по категориям (₽)', color='Выручка',
                                 color_continuous_scale='oranges')
            st.plotly_chart(fig_cat_rev, use_container_width=True)

        # Топ товаров по популярности
        st.subheader("🏅 Топ-5 самых популярных товаров")
        top_popular = df_popularity.nlargest(5, 'Популярность (оценка)')[
            ['Товар', 'Категория', 'Популярность (оценка)', 'Продано шт']]
        st.dataframe(top_popular, use_container_width=True)

        # Рекомендации
        st.subheader("💡 Маркетинговые рекомендации")

        # Находим товары с высокой популярностью, но низкими продажами
        df_popularity['Эффективность'] = df_popularity['Продано шт'] / (df_popularity['Популярность (оценка)'] + 1)
        low_efficiency = df_popularity.nsmallest(3, 'Эффективность')

        st.markdown("""
        <div style="background: rgba(255,248,240,0.9); padding: 20px; border-radius: 15px; margin-top: 10px;">
        """, unsafe_allow_html=True)

        if not low_efficiency.empty:
            st.write("🔍 **Требуют продвижения:**")
            for _, row in low_efficiency.iterrows():
                st.write(
                    f"   • *{row['Товар']}* — популярность {row['Популярность (оценка)']:.0f}/100, но продано всего {row['Продано шт']:.0f} шт")
            st.write("   *Рекомендация:* Усилить рекламную кампанию или сделать акцию на эти товары.")

        st.markdown("""
        <hr>
        <p style="text-align: center;">📢 Рекомендуется проводить кросс-продажи популярных товаров и запустить программу лояльности для постоянных клиентов.</p>
        </div>
        """, unsafe_allow_html=True)

    # ПРОИЗВОДСТВЕННАЯ АНАЛИТИКА
    elif choice == "🔧 Производственная аналитика" and st.session_state.role == "Админ":
        st.header("🔧 Производственная аналитика")

        # Расчет производственных показателей
        prod_data = []
        for product in st.session_state.products:
            product_sales = df_sales[df_sales['ID'] == product['ID']]
            quantity_sold = product_sales['Количество'].sum()

            labor_cost = product['Ручная_работа_минут'] * quantity_sold
            labor_hours = labor_cost / 60

            prod_data.append({
                'Товар': product['Название'],
                'Категория': product['Категория'],
                'Продано шт': quantity_sold,
                'Ручная работа (мин/шт)': product['Ручная_работа_минут'],
                'Всего минут': labor_cost,
                'Всего часов': labor_hours,
                'Срок годности (ч)': product['Срок_годности_часов']
            })

        df_prod = pd.DataFrame(prod_data)
        total_labor_hours = df_prod['Всего часов'].sum()

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("⏱️ Общие трудозатраты", f"{total_labor_hours:.1f} часов")
        with col2:
            avg_labor = df_prod['Ручная работа (мин/шт)'].mean()
            st.metric("👩‍🍳 Среднее время на 1 шт", f"{avg_labor:.0f} минут")
        with col3:
            st.metric("📦 Всего произведено", f"{df_prod['Продано шт'].sum():.0f} шт")

        # График трудозатрат
        st.subheader("⏰ Трудозатраты по товарам")
        fig_labor = px.bar(df_prod.sort_values('Всего часов', ascending=False).head(10),
                           x='Товар', y='Всего часов', color='Категория',
                           title='Топ-10 товаров по трудозатратам (часы)')
        fig_labor.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_labor, use_container_width=True)

        st.info("📊 Производственный анализ показывает загрузку персонала и трудозатраты на каждый товар")

    # НОВЫЙ ДЕСЕРТ
    elif choice == "➕ Новый десерт" and st.session_state.role == "Админ":
        st.header("➕ Добавление десерта")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Название")
            cat = st.selectbox("Категория", ["Торты", "Пирожные", "Капкейки", "Выпечка", "Печенье"])
            price = st.number_input("Цена (₽)", 50, 2000, 300)
        with col2:
            weight = st.selectbox("Вес", ["100г", "150г", "200г", "250г", "500г", "1кг"])
            stock = st.number_input("Остаток", 0, 100, 10)
            cost = st.number_input("Себестоимость (₽)", 10, 1000, 100)

        if st.button("✨ Добавить"):
            new_id = max(p["ID"] for p in st.session_state.products) + 1
            weight_kg = float(weight.replace("г", "").replace("кг", "")) / 1000 if "г" in weight else float(
                weight.replace("кг", ""))
            st.session_state.products.append({
                "ID": new_id, "Название": name, "Категория": cat, "Вес": weight,
                "Вес_кг": weight_kg, "Цена": price, "Себестоимость": cost,
                "Остаток": stock, "Популярность": 70, "Срок_годности_часов": 48, "Ручная_работа_минут": 10
            })
            st.success(f"Десерт '{name}' добавлен!")
            st.rerun()

    # МОБИЛЬНАЯ ВЕРСИЯ
    elif choice == "📱 Мобильная версия":
        st.header("📱 Мобильная версия")
        st.info("Адаптивный режим для мобильных устройств")
        if st.toggle("Адаптивный режим"):
            st.success("Включен адаптивный режим")

# Информация об авторе
st.markdown("---")
st.markdown("""
<div class="author-info">
    <p>© 2026 SweetMaster | Сладкая кондитерская</p>
    <p>👨‍🍳 Разработчик: Шарнин Семён (ИС-944)</p>
</div>
""", unsafe_allow_html=True)