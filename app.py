<html>
<head>
<title>app.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cf8e6d;}
.s1 { color: #bcbec4;}
.s2 { color: #bcbec4;}
.s3 { color: #7a7e85;}
.s4 { color: #6aab73;}
.s5 { color: #2aacb8;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
app.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">streamlit </span><span class="s0">as </span><span class="s1">st</span>
<span class="s0">import </span><span class="s1">pandas </span><span class="s0">as </span><span class="s1">pd</span>
<span class="s0">from </span><span class="s1">datetime </span><span class="s0">import </span><span class="s1">datetime</span><span class="s2">, </span><span class="s1">timedelta</span>
<span class="s0">import </span><span class="s1">random</span>
<span class="s0">import </span><span class="s1">plotly</span><span class="s2">.</span><span class="s1">express </span><span class="s0">as </span><span class="s1">px</span>
<span class="s0">import </span><span class="s1">plotly</span><span class="s2">.</span><span class="s1">graph_objects </span><span class="s0">as </span><span class="s1">go</span>
<span class="s0">import </span><span class="s1">numpy </span><span class="s0">as </span><span class="s1">np</span>

<span class="s3"># Настройка страницы</span>
<span class="s1">st</span><span class="s2">.</span><span class="s1">set_page_config</span><span class="s2">(</span>
    <span class="s1">page_title</span><span class="s2">=</span><span class="s4">&quot;SweetMaster - Кондитерская&quot;</span><span class="s2">,</span>
    <span class="s1">layout</span><span class="s2">=</span><span class="s4">&quot;wide&quot;</span><span class="s2">,</span>
    <span class="s1">page_icon</span><span class="s2">=</span><span class="s4">&quot;🧁&quot;</span><span class="s2">,</span>
    <span class="s1">initial_sidebar_state</span><span class="s2">=</span><span class="s4">&quot;expanded&quot;</span>
<span class="s2">)</span>

<span class="s3"># CSS стили</span>
<span class="s1">st</span><span class="s2">.</span><span class="s1">markdown</span><span class="s2">(</span><span class="s4">&quot;&quot;&quot; 
    &lt;style&gt; 
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
    &lt;/style&gt; 
&quot;&quot;&quot;</span><span class="s2">, </span><span class="s1">unsafe_allow_html</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

<span class="s3"># Инициализация данных</span>
<span class="s0">if </span><span class="s4">'products' </span><span class="s0">not in </span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">:</span>
    <span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">products </span><span class="s2">= [</span>
        <span class="s2">{</span><span class="s4">&quot;ID&quot;</span><span class="s2">: </span><span class="s5">104</span><span class="s2">, </span><span class="s4">&quot;Название&quot;</span><span class="s2">: </span><span class="s4">&quot;Медовик нежный&quot;</span><span class="s2">, </span><span class="s4">&quot;Категория&quot;</span><span class="s2">: </span><span class="s4">&quot;Торты&quot;</span><span class="s2">, </span><span class="s4">&quot;Вес&quot;</span><span class="s2">: </span><span class="s4">&quot;1кг&quot;</span><span class="s2">, </span><span class="s4">&quot;Вес_кг&quot;</span><span class="s2">: </span><span class="s5">1.0</span><span class="s2">, </span><span class="s4">&quot;Цена&quot;</span><span class="s2">: </span><span class="s5">850</span><span class="s2">,</span>
         <span class="s4">&quot;Себестоимость&quot;</span><span class="s2">: </span><span class="s5">420</span><span class="s2">, </span><span class="s4">&quot;Остаток&quot;</span><span class="s2">: </span><span class="s5">5</span><span class="s2">, </span><span class="s4">&quot;Популярность&quot;</span><span class="s2">: </span><span class="s5">90</span><span class="s2">, </span><span class="s4">&quot;Срок_годности_часов&quot;</span><span class="s2">: </span><span class="s5">72</span><span class="s2">, </span><span class="s4">&quot;Ручная_работа_минут&quot;</span><span class="s2">: </span><span class="s5">45</span><span class="s2">},</span>
        <span class="s2">{</span><span class="s4">&quot;ID&quot;</span><span class="s2">: </span><span class="s5">109</span><span class="s2">, </span><span class="s4">&quot;Название&quot;</span><span class="s2">: </span><span class="s4">&quot;Наполеон хрустящий&quot;</span><span class="s2">, </span><span class="s4">&quot;Категория&quot;</span><span class="s2">: </span><span class="s4">&quot;Торты&quot;</span><span class="s2">, </span><span class="s4">&quot;Вес&quot;</span><span class="s2">: </span><span class="s4">&quot;1кг&quot;</span><span class="s2">, </span><span class="s4">&quot;Вес_кг&quot;</span><span class="s2">: </span><span class="s5">1.0</span><span class="s2">, </span><span class="s4">&quot;Цена&quot;</span><span class="s2">: </span><span class="s5">920</span><span class="s2">,</span>
         <span class="s4">&quot;Себестоимость&quot;</span><span class="s2">: </span><span class="s5">450</span><span class="s2">, </span><span class="s4">&quot;Остаток&quot;</span><span class="s2">: </span><span class="s5">4</span><span class="s2">, </span><span class="s4">&quot;Популярность&quot;</span><span class="s2">: </span><span class="s5">94</span><span class="s2">, </span><span class="s4">&quot;Срок_годности_часов&quot;</span><span class="s2">: </span><span class="s5">48</span><span class="s2">, </span><span class="s4">&quot;Ручная_работа_минут&quot;</span><span class="s2">: </span><span class="s5">50</span><span class="s2">},</span>
        <span class="s2">{</span><span class="s4">&quot;ID&quot;</span><span class="s2">: </span><span class="s5">101</span><span class="s2">, </span><span class="s4">&quot;Название&quot;</span><span class="s2">: </span><span class="s4">&quot;Тирамису классический&quot;</span><span class="s2">, </span><span class="s4">&quot;Категория&quot;</span><span class="s2">: </span><span class="s4">&quot;Пирожные&quot;</span><span class="s2">, </span><span class="s4">&quot;Вес&quot;</span><span class="s2">: </span><span class="s4">&quot;200г&quot;</span><span class="s2">, </span><span class="s4">&quot;Вес_кг&quot;</span><span class="s2">: </span><span class="s5">0.2</span><span class="s2">,</span>
         <span class="s4">&quot;Цена&quot;</span><span class="s2">: </span><span class="s5">320</span><span class="s2">, </span><span class="s4">&quot;Себестоимость&quot;</span><span class="s2">: </span><span class="s5">180</span><span class="s2">, </span><span class="s4">&quot;Остаток&quot;</span><span class="s2">: </span><span class="s5">15</span><span class="s2">, </span><span class="s4">&quot;Популярность&quot;</span><span class="s2">: </span><span class="s5">95</span><span class="s2">, </span><span class="s4">&quot;Срок_годности_часов&quot;</span><span class="s2">: </span><span class="s5">48</span><span class="s2">,</span>
         <span class="s4">&quot;Ручная_работа_минут&quot;</span><span class="s2">: </span><span class="s5">15</span><span class="s2">},</span>
        <span class="s2">{</span><span class="s4">&quot;ID&quot;</span><span class="s2">: </span><span class="s5">105</span><span class="s2">, </span><span class="s4">&quot;Название&quot;</span><span class="s2">: </span><span class="s4">&quot;Чизкейк Нью-Йорк&quot;</span><span class="s2">, </span><span class="s4">&quot;Категория&quot;</span><span class="s2">: </span><span class="s4">&quot;Пирожные&quot;</span><span class="s2">, </span><span class="s4">&quot;Вес&quot;</span><span class="s2">: </span><span class="s4">&quot;250г&quot;</span><span class="s2">, </span><span class="s4">&quot;Вес_кг&quot;</span><span class="s2">: </span><span class="s5">0.25</span><span class="s2">, </span><span class="s4">&quot;Цена&quot;</span><span class="s2">: </span><span class="s5">380</span><span class="s2">,</span>
         <span class="s4">&quot;Себестоимость&quot;</span><span class="s2">: </span><span class="s5">200</span><span class="s2">, </span><span class="s4">&quot;Остаток&quot;</span><span class="s2">: </span><span class="s5">7</span><span class="s2">, </span><span class="s4">&quot;Популярность&quot;</span><span class="s2">: </span><span class="s5">96</span><span class="s2">, </span><span class="s4">&quot;Срок_годности_часов&quot;</span><span class="s2">: </span><span class="s5">48</span><span class="s2">, </span><span class="s4">&quot;Ручная_работа_минут&quot;</span><span class="s2">: </span><span class="s5">20</span><span class="s2">},</span>
        <span class="s2">{</span><span class="s4">&quot;ID&quot;</span><span class="s2">: </span><span class="s5">110</span><span class="s2">, </span><span class="s4">&quot;Название&quot;</span><span class="s2">: </span><span class="s4">&quot;Капкейк с вишней&quot;</span><span class="s2">, </span><span class="s4">&quot;Категория&quot;</span><span class="s2">: </span><span class="s4">&quot;Капкейки&quot;</span><span class="s2">, </span><span class="s4">&quot;Вес&quot;</span><span class="s2">: </span><span class="s4">&quot;120г&quot;</span><span class="s2">, </span><span class="s4">&quot;Вес_кг&quot;</span><span class="s2">: </span><span class="s5">0.12</span><span class="s2">, </span><span class="s4">&quot;Цена&quot;</span><span class="s2">: </span><span class="s5">160</span><span class="s2">,</span>
         <span class="s4">&quot;Себестоимость&quot;</span><span class="s2">: </span><span class="s5">60</span><span class="s2">, </span><span class="s4">&quot;Остаток&quot;</span><span class="s2">: </span><span class="s5">15</span><span class="s2">, </span><span class="s4">&quot;Популярность&quot;</span><span class="s2">: </span><span class="s5">87</span><span class="s2">, </span><span class="s4">&quot;Срок_годности_часов&quot;</span><span class="s2">: </span><span class="s5">48</span><span class="s2">, </span><span class="s4">&quot;Ручная_работа_минут&quot;</span><span class="s2">: </span><span class="s5">7</span><span class="s2">},</span>
        <span class="s2">{</span><span class="s4">&quot;ID&quot;</span><span class="s2">: </span><span class="s5">103</span><span class="s2">, </span><span class="s4">&quot;Название&quot;</span><span class="s2">: </span><span class="s4">&quot;Круассан с шоколадом&quot;</span><span class="s2">, </span><span class="s4">&quot;Категория&quot;</span><span class="s2">: </span><span class="s4">&quot;Выпечка&quot;</span><span class="s2">, </span><span class="s4">&quot;Вес&quot;</span><span class="s2">: </span><span class="s4">&quot;120г&quot;</span><span class="s2">, </span><span class="s4">&quot;Вес_кг&quot;</span><span class="s2">: </span><span class="s5">0.12</span><span class="s2">,</span>
         <span class="s4">&quot;Цена&quot;</span><span class="s2">: </span><span class="s5">150</span><span class="s2">, </span><span class="s4">&quot;Себестоимость&quot;</span><span class="s2">: </span><span class="s5">65</span><span class="s2">, </span><span class="s4">&quot;Остаток&quot;</span><span class="s2">: </span><span class="s5">18</span><span class="s2">, </span><span class="s4">&quot;Популярность&quot;</span><span class="s2">: </span><span class="s5">88</span><span class="s2">, </span><span class="s4">&quot;Срок_годности_часов&quot;</span><span class="s2">: </span><span class="s5">8</span><span class="s2">,</span>
         <span class="s4">&quot;Ручная_работа_минут&quot;</span><span class="s2">: </span><span class="s5">5</span><span class="s2">},</span>
        <span class="s2">{</span><span class="s4">&quot;ID&quot;</span><span class="s2">: </span><span class="s5">102</span><span class="s2">, </span><span class="s4">&quot;Название&quot;</span><span class="s2">: </span><span class="s4">&quot;Макаронс клубничные&quot;</span><span class="s2">, </span><span class="s4">&quot;Категория&quot;</span><span class="s2">: </span><span class="s4">&quot;Печенье&quot;</span><span class="s2">, </span><span class="s4">&quot;Вес&quot;</span><span class="s2">: </span><span class="s4">&quot;150г&quot;</span><span class="s2">, </span><span class="s4">&quot;Вес_кг&quot;</span><span class="s2">: </span><span class="s5">0.15</span><span class="s2">,</span>
         <span class="s4">&quot;Цена&quot;</span><span class="s2">: </span><span class="s5">180</span><span class="s2">, </span><span class="s4">&quot;Себестоимость&quot;</span><span class="s2">: </span><span class="s5">70</span><span class="s2">, </span><span class="s4">&quot;Остаток&quot;</span><span class="s2">: </span><span class="s5">24</span><span class="s2">, </span><span class="s4">&quot;Популярность&quot;</span><span class="s2">: </span><span class="s5">92</span><span class="s2">, </span><span class="s4">&quot;Срок_годности_часов&quot;</span><span class="s2">: </span><span class="s5">72</span><span class="s2">,</span>
         <span class="s4">&quot;Ручная_работа_минут&quot;</span><span class="s2">: </span><span class="s5">8</span><span class="s2">},</span>
    <span class="s2">]</span>

<span class="s0">if </span><span class="s4">'sales' </span><span class="s0">not in </span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">:</span>
    <span class="s1">sales_data </span><span class="s2">= []</span>
    <span class="s1">today </span><span class="s2">= </span><span class="s1">datetime</span><span class="s2">.</span><span class="s1">now</span><span class="s2">()</span>
    <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range</span><span class="s2">(</span><span class="s5">300</span><span class="s2">):</span>
        <span class="s1">prod </span><span class="s2">= </span><span class="s1">random</span><span class="s2">.</span><span class="s1">choice</span><span class="s2">(</span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">products</span><span class="s2">)</span>
        <span class="s1">days_ago </span><span class="s2">= </span><span class="s1">random</span><span class="s2">.</span><span class="s1">randint</span><span class="s2">(</span><span class="s5">0</span><span class="s2">, </span><span class="s5">60</span><span class="s2">)</span>
        <span class="s1">sale_date </span><span class="s2">= (</span><span class="s1">today </span><span class="s2">- </span><span class="s1">timedelta</span><span class="s2">(</span><span class="s1">days</span><span class="s2">=</span><span class="s1">days_ago</span><span class="s2">)).</span><span class="s1">strftime</span><span class="s2">(</span><span class="s4">&quot;%Y-%m-%d&quot;</span><span class="s2">)</span>
        <span class="s1">qty </span><span class="s2">= </span><span class="s1">random</span><span class="s2">.</span><span class="s1">randint</span><span class="s2">(</span><span class="s5">1</span><span class="s2">, </span><span class="s5">3</span><span class="s2">)</span>
        <span class="s1">sales_data</span><span class="s2">.</span><span class="s1">append</span><span class="s2">({</span>
            <span class="s4">&quot;Дата&quot;</span><span class="s2">: </span><span class="s1">sale_date</span><span class="s2">,</span>
            <span class="s4">&quot;ID&quot;</span><span class="s2">: </span><span class="s1">prod</span><span class="s2">[</span><span class="s4">&quot;ID&quot;</span><span class="s2">],</span>
            <span class="s4">&quot;Название&quot;</span><span class="s2">: </span><span class="s1">prod</span><span class="s2">[</span><span class="s4">&quot;Название&quot;</span><span class="s2">],</span>
            <span class="s4">&quot;Категория&quot;</span><span class="s2">: </span><span class="s1">prod</span><span class="s2">[</span><span class="s4">&quot;Категория&quot;</span><span class="s2">],</span>
            <span class="s4">&quot;Количество&quot;</span><span class="s2">: </span><span class="s1">qty</span><span class="s2">,</span>
            <span class="s4">&quot;Сумма&quot;</span><span class="s2">: </span><span class="s1">prod</span><span class="s2">[</span><span class="s4">&quot;Цена&quot;</span><span class="s2">] * </span><span class="s1">qty</span>
        <span class="s2">})</span>
    <span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">sales </span><span class="s2">= </span><span class="s1">sales_data</span>

<span class="s0">if </span><span class="s4">'role' </span><span class="s0">not in </span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">:</span>
    <span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">role </span><span class="s2">= </span><span class="s0">None</span>


<span class="s0">def </span><span class="s1">login</span><span class="s2">():</span>
    <span class="s0">with </span><span class="s1">st</span><span class="s2">.</span><span class="s1">sidebar</span><span class="s2">:</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">markdown</span><span class="s2">(</span><span class="s4">&quot;### 🧁 Добро пожаловать!&quot;</span><span class="s2">)</span>
        <span class="s1">username </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">text_input</span><span class="s2">(</span><span class="s4">&quot;👤 Логин&quot;</span><span class="s2">, </span><span class="s1">placeholder</span><span class="s2">=</span><span class="s4">&quot;Введите логин&quot;</span><span class="s2">)</span>
        <span class="s1">password </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">text_input</span><span class="s2">(</span><span class="s4">&quot;🔒 Пароль&quot;</span><span class="s2">, </span><span class="s1">type</span><span class="s2">=</span><span class="s4">&quot;password&quot;</span><span class="s2">, </span><span class="s1">placeholder</span><span class="s2">=</span><span class="s4">&quot;Введите пароль&quot;</span><span class="s2">)</span>
        <span class="s0">if </span><span class="s1">st</span><span class="s2">.</span><span class="s1">button</span><span class="s2">(</span><span class="s4">&quot;🍰 Войти&quot;</span><span class="s2">, </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">):</span>
            <span class="s0">if </span><span class="s1">username </span><span class="s2">== </span><span class="s4">&quot;Admin&quot; </span><span class="s0">and </span><span class="s1">password </span><span class="s2">== </span><span class="s4">&quot;12345678&quot;</span><span class="s2">:</span>
                <span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">role </span><span class="s2">= </span><span class="s4">&quot;Админ&quot;</span>
                <span class="s1">st</span><span class="s2">.</span><span class="s1">rerun</span><span class="s2">()</span>
            <span class="s0">elif </span><span class="s1">username </span><span class="s2">== </span><span class="s4">&quot;Mened&quot; </span><span class="s0">and </span><span class="s1">password </span><span class="s2">== </span><span class="s4">&quot;1234567&quot;</span><span class="s2">:</span>
                <span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">role </span><span class="s2">= </span><span class="s4">&quot;Менеджер&quot;</span>
                <span class="s1">st</span><span class="s2">.</span><span class="s1">rerun</span><span class="s2">()</span>
            <span class="s0">else</span><span class="s2">:</span>
                <span class="s1">st</span><span class="s2">.</span><span class="s1">error</span><span class="s2">(</span><span class="s4">&quot;❌ Неверный логин или пароль&quot;</span><span class="s2">)</span>


<span class="s0">def </span><span class="s1">logout</span><span class="s2">():</span>
    <span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">role </span><span class="s2">= </span><span class="s0">None</span>
    <span class="s1">st</span><span class="s2">.</span><span class="s1">rerun</span><span class="s2">()</span>


<span class="s3"># Основной интерфейс</span>
<span class="s1">st</span><span class="s2">.</span><span class="s1">title</span><span class="s2">(</span><span class="s4">&quot;🧁 SweetMaster&quot;</span><span class="s2">)</span>
<span class="s1">st</span><span class="s2">.</span><span class="s1">caption</span><span class="s2">(</span><span class="s4">&quot;✨ Учёт кондитерских изделий и сладостей ✨&quot;</span><span class="s2">)</span>

<span class="s0">if </span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">role </span><span class="s0">is None</span><span class="s2">:</span>
    <span class="s1">login</span><span class="s2">()</span>
    <span class="s1">st</span><span class="s2">.</span><span class="s1">info</span><span class="s2">(</span><span class="s4">&quot;🍪 Добро пожаловать! Авторизуйтесь в боковой панели&quot;</span><span class="s2">)</span>
<span class="s0">else</span><span class="s2">:</span>
    <span class="s0">with </span><span class="s1">st</span><span class="s2">.</span><span class="s1">sidebar</span><span class="s2">:</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">markdown</span><span class="s2">(</span><span class="s4">f&quot;### 👩‍🍳 Привет, </span><span class="s0">{</span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">role</span><span class="s0">}</span><span class="s4">!&quot;</span><span class="s2">)</span>
        <span class="s0">if </span><span class="s1">st</span><span class="s2">.</span><span class="s1">button</span><span class="s2">(</span><span class="s4">&quot;🚪 Выйти&quot;</span><span class="s2">, </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">):</span>
            <span class="s1">logout</span><span class="s2">()</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">markdown</span><span class="s2">(</span><span class="s4">&quot;---&quot;</span><span class="s2">)</span>
        <span class="s0">if </span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">role </span><span class="s2">== </span><span class="s4">&quot;Админ&quot;</span><span class="s2">:</span>
            <span class="s1">menu </span><span class="s2">= [</span><span class="s4">&quot;🏠 Главная&quot;</span><span class="s2">, </span><span class="s4">&quot;🍰 Наши десерты&quot;</span><span class="s2">, </span><span class="s4">&quot;💸 Продажи&quot;</span><span class="s2">, </span><span class="s4">&quot;📈 Общая аналитика&quot;</span><span class="s2">, </span><span class="s4">&quot;📊 ABC/XYZ анализ&quot;</span><span class="s2">,</span>
                    <span class="s4">&quot;💰 Финансовый анализ&quot;</span><span class="s2">, </span><span class="s4">&quot;🎯 Маркетинговый анализ&quot;</span><span class="s2">, </span><span class="s4">&quot;🔧 Производственная аналитика&quot;</span><span class="s2">, </span><span class="s4">&quot;➕ Новый десерт&quot;</span><span class="s2">,</span>
                    <span class="s4">&quot;📱 Мобильная версия&quot;</span><span class="s2">]</span>
        <span class="s0">else</span><span class="s2">:</span>
            <span class="s1">menu </span><span class="s2">= [</span><span class="s4">&quot;🏠 Главная&quot;</span><span class="s2">, </span><span class="s4">&quot;🍰 Наши десерты&quot;</span><span class="s2">, </span><span class="s4">&quot;💸 Продажи&quot;</span><span class="s2">, </span><span class="s4">&quot;📈 Общая аналитика&quot;</span><span class="s2">, </span><span class="s4">&quot;📱 Мобильная версия&quot;</span><span class="s2">]</span>
        <span class="s1">choice </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">radio</span><span class="s2">(</span><span class="s4">&quot;&quot;</span><span class="s2">, </span><span class="s1">menu</span><span class="s2">, </span><span class="s1">label_visibility</span><span class="s2">=</span><span class="s4">&quot;collapsed&quot;</span><span class="s2">)</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">markdown</span><span class="s2">(</span><span class="s4">&quot;---&quot;</span><span class="s2">)</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">info</span><span class="s2">(</span><span class="s4">&quot;🕐 ПН-ВС: 10:00 - 21:00&quot;</span><span class="s2">)</span>

    <span class="s1">df_products </span><span class="s2">= </span><span class="s1">pd</span><span class="s2">.</span><span class="s1">DataFrame</span><span class="s2">(</span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">products</span><span class="s2">)</span>
    <span class="s1">df_sales </span><span class="s2">= </span><span class="s1">pd</span><span class="s2">.</span><span class="s1">DataFrame</span><span class="s2">(</span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">sales</span><span class="s2">)</span>

    <span class="s3"># ГЛАВНАЯ</span>
    <span class="s0">if </span><span class="s1">choice </span><span class="s2">== </span><span class="s4">&quot;🏠 Главная&quot;</span><span class="s2">:</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">markdown</span><span class="s2">(</span><span class="s4">&quot;&quot;&quot; 
        &lt;div class=&quot;welcome-card&quot;&gt; 
            &lt;div style=&quot;font-size: 64px;&quot;&gt;🧁🍰🎂&lt;/div&gt; 
            &lt;h1&gt;Добро пожаловать в SweetMaster!&lt;/h1&gt; 
            &lt;p style=&quot;font-size: 18px; color: #8b5a2b;&quot;&gt;Ваша система учёта кондитерских изделий и сладостей&lt;/p&gt; 
        &lt;/div&gt; 
        &quot;&quot;&quot;</span><span class="s2">, </span><span class="s1">unsafe_allow_html</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

        <span class="s1">col1</span><span class="s2">, </span><span class="s1">col2</span><span class="s2">, </span><span class="s1">col3</span><span class="s2">, </span><span class="s1">col4 </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">columns</span><span class="s2">(</span><span class="s5">4</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col1</span><span class="s2">:</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">metric</span><span class="s2">(</span><span class="s4">&quot;🍰 Всего товаров&quot;</span><span class="s2">, </span><span class="s1">len</span><span class="s2">(</span><span class="s1">df_products</span><span class="s2">))</span>
        <span class="s0">with </span><span class="s1">col2</span><span class="s2">:</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">metric</span><span class="s2">(</span><span class="s4">&quot;📦 Категорий&quot;</span><span class="s2">, </span><span class="s1">len</span><span class="s2">(</span><span class="s1">df_products</span><span class="s2">[</span><span class="s4">'Категория'</span><span class="s2">].</span><span class="s1">unique</span><span class="s2">()))</span>
        <span class="s0">with </span><span class="s1">col3</span><span class="s2">:</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">metric</span><span class="s2">(</span><span class="s4">&quot;💰 Общая выручка&quot;</span><span class="s2">, </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">df_sales</span><span class="s2">[</span><span class="s4">'Сумма'</span><span class="s2">].</span><span class="s1">sum</span><span class="s2">()</span><span class="s0">:</span><span class="s4">,.0f</span><span class="s0">} </span><span class="s4">₽&quot;</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col4</span><span class="s2">:</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">metric</span><span class="s2">(</span><span class="s4">&quot;🧾 Всего продаж&quot;</span><span class="s2">, </span><span class="s1">len</span><span class="s2">(</span><span class="s1">df_sales</span><span class="s2">))</span>

        <span class="s1">st</span><span class="s2">.</span><span class="s1">subheader</span><span class="s2">(</span><span class="s4">&quot;🏆 Топ-5 продаваемых товаров&quot;</span><span class="s2">)</span>
        <span class="s1">top </span><span class="s2">= </span><span class="s1">df_sales</span><span class="s2">.</span><span class="s1">groupby</span><span class="s2">(</span><span class="s4">'Название'</span><span class="s2">)[</span><span class="s4">'Количество'</span><span class="s2">].</span><span class="s1">sum</span><span class="s2">().</span><span class="s1">sort_values</span><span class="s2">(</span><span class="s1">ascending</span><span class="s2">=</span><span class="s0">False</span><span class="s2">).</span><span class="s1">head</span><span class="s2">(</span><span class="s5">5</span><span class="s2">)</span>
        <span class="s0">if not </span><span class="s1">top</span><span class="s2">.</span><span class="s1">empty</span><span class="s2">:</span>
            <span class="s1">fig </span><span class="s2">= </span><span class="s1">px</span><span class="s2">.</span><span class="s1">bar</span><span class="s2">(</span><span class="s1">x</span><span class="s2">=</span><span class="s1">top</span><span class="s2">.</span><span class="s1">values</span><span class="s2">, </span><span class="s1">y</span><span class="s2">=</span><span class="s1">top</span><span class="s2">.</span><span class="s1">index</span><span class="s2">, </span><span class="s1">orientation</span><span class="s2">=</span><span class="s4">'h'</span><span class="s2">, </span><span class="s1">color</span><span class="s2">=</span><span class="s1">top</span><span class="s2">.</span><span class="s1">values</span><span class="s2">, </span><span class="s1">color_continuous_scale</span><span class="s2">=</span><span class="s4">'oranges'</span><span class="s2">)</span>
            <span class="s1">fig</span><span class="s2">.</span><span class="s1">update_layout</span><span class="s2">(</span><span class="s1">height</span><span class="s2">=</span><span class="s5">300</span><span class="s2">, </span><span class="s1">showlegend</span><span class="s2">=</span><span class="s0">False</span><span class="s2">)</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">plotly_chart</span><span class="s2">(</span><span class="s1">fig</span><span class="s2">, </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

    <span class="s3"># НАШИ ДЕСЕРТЫ</span>
    <span class="s0">elif </span><span class="s1">choice </span><span class="s2">== </span><span class="s4">&quot;🍰 Наши десерты&quot;</span><span class="s2">:</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">header</span><span class="s2">(</span><span class="s4">&quot;🍰 Наши сладости&quot;</span><span class="s2">)</span>
        <span class="s1">col1</span><span class="s2">, </span><span class="s1">col2 </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">columns</span><span class="s2">(</span><span class="s5">2</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col1</span><span class="s2">:</span>
            <span class="s1">cat_filter </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">selectbox</span><span class="s2">(</span><span class="s4">&quot;Категория&quot;</span><span class="s2">, [</span><span class="s4">&quot;Все&quot;</span><span class="s2">] + </span><span class="s1">sorted</span><span class="s2">(</span><span class="s1">df_products</span><span class="s2">[</span><span class="s4">&quot;Категория&quot;</span><span class="s2">].</span><span class="s1">unique</span><span class="s2">()))</span>
        <span class="s0">with </span><span class="s1">col2</span><span class="s2">:</span>
            <span class="s1">sort_by </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">selectbox</span><span class="s2">(</span><span class="s4">&quot;Сортировка&quot;</span><span class="s2">, [</span><span class="s4">&quot;По названию&quot;</span><span class="s2">, </span><span class="s4">&quot;По цене (возр.)&quot;</span><span class="s2">, </span><span class="s4">&quot;По цене (убыв.)&quot;</span><span class="s2">])</span>

        <span class="s1">df_filtered </span><span class="s2">= </span><span class="s1">df_products</span><span class="s2">.</span><span class="s1">copy</span><span class="s2">()</span>
        <span class="s0">if </span><span class="s1">cat_filter </span><span class="s2">!= </span><span class="s4">&quot;Все&quot;</span><span class="s2">:</span>
            <span class="s1">df_filtered </span><span class="s2">= </span><span class="s1">df_filtered</span><span class="s2">[</span><span class="s1">df_filtered</span><span class="s2">[</span><span class="s4">&quot;Категория&quot;</span><span class="s2">] == </span><span class="s1">cat_filter</span><span class="s2">]</span>
        <span class="s0">if </span><span class="s1">sort_by </span><span class="s2">== </span><span class="s4">&quot;По цене (возр.)&quot;</span><span class="s2">:</span>
            <span class="s1">df_filtered </span><span class="s2">= </span><span class="s1">df_filtered</span><span class="s2">.</span><span class="s1">sort_values</span><span class="s2">(</span><span class="s4">&quot;Цена&quot;</span><span class="s2">)</span>
        <span class="s0">elif </span><span class="s1">sort_by </span><span class="s2">== </span><span class="s4">&quot;По цене (убыв.)&quot;</span><span class="s2">:</span>
            <span class="s1">df_filtered </span><span class="s2">= </span><span class="s1">df_filtered</span><span class="s2">.</span><span class="s1">sort_values</span><span class="s2">(</span><span class="s4">&quot;Цена&quot;</span><span class="s2">, </span><span class="s1">ascending</span><span class="s2">=</span><span class="s0">False</span><span class="s2">)</span>
        <span class="s0">else</span><span class="s2">:</span>
            <span class="s1">df_filtered </span><span class="s2">= </span><span class="s1">df_filtered</span><span class="s2">.</span><span class="s1">sort_values</span><span class="s2">(</span><span class="s4">&quot;Название&quot;</span><span class="s2">)</span>

        <span class="s1">display </span><span class="s2">= </span><span class="s1">df_filtered</span><span class="s2">[[</span><span class="s4">'Название'</span><span class="s2">, </span><span class="s4">'Категория'</span><span class="s2">, </span><span class="s4">'Вес'</span><span class="s2">, </span><span class="s4">'Цена'</span><span class="s2">, </span><span class="s4">'Остаток'</span><span class="s2">, </span><span class="s4">'Популярность'</span><span class="s2">]].</span><span class="s1">copy</span><span class="s2">()</span>
        <span class="s1">display</span><span class="s2">[</span><span class="s4">'Цена'</span><span class="s2">] = </span><span class="s1">display</span><span class="s2">[</span><span class="s4">'Цена'</span><span class="s2">].</span><span class="s1">apply</span><span class="s2">(</span><span class="s0">lambda </span><span class="s1">x</span><span class="s2">: </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">x</span><span class="s0">:</span><span class="s4">,.0f</span><span class="s0">} </span><span class="s4">₽&quot;</span><span class="s2">)</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">dataframe</span><span class="s2">(</span><span class="s1">display</span><span class="s2">, </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

    <span class="s3"># ПРОДАЖИ</span>
    <span class="s0">elif </span><span class="s1">choice </span><span class="s2">== </span><span class="s4">&quot;💸 Продажи&quot;</span><span class="s2">:</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">header</span><span class="s2">(</span><span class="s4">&quot;💸 Оформление заказа&quot;</span><span class="s2">)</span>
        <span class="s1">available </span><span class="s2">= [</span><span class="s1">p </span><span class="s0">for </span><span class="s1">p </span><span class="s0">in </span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">products </span><span class="s0">if </span><span class="s1">p</span><span class="s2">[</span><span class="s4">&quot;Остаток&quot;</span><span class="s2">] &gt; </span><span class="s5">0</span><span class="s2">]</span>
        <span class="s0">if </span><span class="s1">available</span><span class="s2">:</span>
            <span class="s1">prod_options </span><span class="s2">= {</span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">p</span><span class="s2">[</span><span class="s4">'Название'</span><span class="s2">]</span><span class="s0">} </span><span class="s4">- </span><span class="s0">{</span><span class="s1">p</span><span class="s2">[</span><span class="s4">'Цена'</span><span class="s2">]</span><span class="s0">} </span><span class="s4">₽&quot;</span><span class="s2">: </span><span class="s1">p </span><span class="s0">for </span><span class="s1">p </span><span class="s0">in </span><span class="s1">available</span><span class="s2">}</span>
            <span class="s1">selected </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">selectbox</span><span class="s2">(</span><span class="s4">&quot;Выберите десерт&quot;</span><span class="s2">, </span><span class="s1">list</span><span class="s2">(</span><span class="s1">prod_options</span><span class="s2">.</span><span class="s1">keys</span><span class="s2">()))</span>
            <span class="s1">prod </span><span class="s2">= </span><span class="s1">prod_options</span><span class="s2">[</span><span class="s1">selected</span><span class="s2">]</span>
            <span class="s1">qty </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">number_input</span><span class="s2">(</span><span class="s4">&quot;Количество&quot;</span><span class="s2">, </span><span class="s5">1</span><span class="s2">, </span><span class="s1">prod</span><span class="s2">[</span><span class="s4">&quot;Остаток&quot;</span><span class="s2">], </span><span class="s5">1</span><span class="s2">)</span>
            <span class="s0">if </span><span class="s1">st</span><span class="s2">.</span><span class="s1">button</span><span class="s2">(</span><span class="s4">&quot;Подтвердить заказ&quot;</span><span class="s2">):</span>
                <span class="s1">prod</span><span class="s2">[</span><span class="s4">&quot;Остаток&quot;</span><span class="s2">] -= </span><span class="s1">qty</span>
                <span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">sales</span><span class="s2">.</span><span class="s1">append</span><span class="s2">({</span>
                    <span class="s4">&quot;Дата&quot;</span><span class="s2">: </span><span class="s1">datetime</span><span class="s2">.</span><span class="s1">now</span><span class="s2">().</span><span class="s1">strftime</span><span class="s2">(</span><span class="s4">&quot;%Y-%m-%d&quot;</span><span class="s2">),</span>
                    <span class="s4">&quot;ID&quot;</span><span class="s2">: </span><span class="s1">prod</span><span class="s2">[</span><span class="s4">&quot;ID&quot;</span><span class="s2">],</span>
                    <span class="s4">&quot;Название&quot;</span><span class="s2">: </span><span class="s1">prod</span><span class="s2">[</span><span class="s4">&quot;Название&quot;</span><span class="s2">],</span>
                    <span class="s4">&quot;Категория&quot;</span><span class="s2">: </span><span class="s1">prod</span><span class="s2">[</span><span class="s4">&quot;Категория&quot;</span><span class="s2">],</span>
                    <span class="s4">&quot;Количество&quot;</span><span class="s2">: </span><span class="s1">qty</span><span class="s2">,</span>
                    <span class="s4">&quot;Сумма&quot;</span><span class="s2">: </span><span class="s1">prod</span><span class="s2">[</span><span class="s4">&quot;Цена&quot;</span><span class="s2">] * </span><span class="s1">qty</span>
                <span class="s2">})</span>
                <span class="s1">st</span><span class="s2">.</span><span class="s1">balloons</span><span class="s2">()</span>
                <span class="s1">st</span><span class="s2">.</span><span class="s1">success</span><span class="s2">(</span><span class="s4">&quot;Заказ оформлен!&quot;</span><span class="s2">)</span>
                <span class="s1">st</span><span class="s2">.</span><span class="s1">rerun</span><span class="s2">()</span>
        <span class="s0">else</span><span class="s2">:</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">warning</span><span class="s2">(</span><span class="s4">&quot;Товаров нет в наличии&quot;</span><span class="s2">)</span>

    <span class="s3"># ОБЩАЯ АНАЛИТИКА</span>
    <span class="s0">elif </span><span class="s1">choice </span><span class="s2">== </span><span class="s4">&quot;📈 Общая аналитика&quot;</span><span class="s2">:</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">header</span><span class="s2">(</span><span class="s4">&quot;Общая аналитика&quot;</span><span class="s2">)</span>
        <span class="s1">cat_sales </span><span class="s2">= </span><span class="s1">df_sales</span><span class="s2">.</span><span class="s1">groupby</span><span class="s2">(</span><span class="s4">'Категория'</span><span class="s2">).</span><span class="s1">agg</span><span class="s2">({</span><span class="s4">'Сумма'</span><span class="s2">: </span><span class="s4">'sum'</span><span class="s2">, </span><span class="s4">'Количество'</span><span class="s2">: </span><span class="s4">'sum'</span><span class="s2">}).</span><span class="s1">reset_index</span><span class="s2">()</span>
        <span class="s1">fig </span><span class="s2">= </span><span class="s1">px</span><span class="s2">.</span><span class="s1">bar</span><span class="s2">(</span><span class="s1">cat_sales</span><span class="s2">, </span><span class="s1">x</span><span class="s2">=</span><span class="s4">'Категория'</span><span class="s2">, </span><span class="s1">y</span><span class="s2">=</span><span class="s4">'Сумма'</span><span class="s2">, </span><span class="s1">title</span><span class="s2">=</span><span class="s4">'Выручка по категориям'</span><span class="s2">, </span><span class="s1">color</span><span class="s2">=</span><span class="s4">'Сумма'</span><span class="s2">,</span>
                     <span class="s1">color_continuous_scale</span><span class="s2">=</span><span class="s4">'oranges'</span><span class="s2">)</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">plotly_chart</span><span class="s2">(</span><span class="s1">fig</span><span class="s2">, </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

        <span class="s1">col1</span><span class="s2">, </span><span class="s1">col2 </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">columns</span><span class="s2">(</span><span class="s5">2</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col1</span><span class="s2">:</span>
            <span class="s1">fig2 </span><span class="s2">= </span><span class="s1">px</span><span class="s2">.</span><span class="s1">pie</span><span class="s2">(</span><span class="s1">cat_sales</span><span class="s2">, </span><span class="s1">values</span><span class="s2">=</span><span class="s4">'Количество'</span><span class="s2">, </span><span class="s1">names</span><span class="s2">=</span><span class="s4">'Категория'</span><span class="s2">, </span><span class="s1">title</span><span class="s2">=</span><span class="s4">'Доля продаж'</span><span class="s2">)</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">plotly_chart</span><span class="s2">(</span><span class="s1">fig2</span><span class="s2">, </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col2</span><span class="s2">:</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">dataframe</span><span class="s2">(</span><span class="s1">cat_sales</span><span class="s2">, </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

    <span class="s3"># ABC/XYZ АНАЛИЗ</span>
    <span class="s0">elif </span><span class="s1">choice </span><span class="s2">== </span><span class="s4">&quot;📊 ABC/XYZ анализ&quot; </span><span class="s0">and </span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">role </span><span class="s2">== </span><span class="s4">&quot;Админ&quot;</span><span class="s2">:</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">header</span><span class="s2">(</span><span class="s4">&quot;ABC/XYZ анализ&quot;</span><span class="s2">)</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">info</span><span class="s2">(</span><span class="s4">&quot;📊 Модуль показывает распределение товаров по категориям A/B/C (по выручке) и X/Y/Z (по стабильности)&quot;</span><span class="s2">)</span>

        <span class="s1">sales_by_product </span><span class="s2">= </span><span class="s1">df_sales</span><span class="s2">.</span><span class="s1">groupby</span><span class="s2">(</span><span class="s4">'ID'</span><span class="s2">).</span><span class="s1">agg</span><span class="s2">({</span><span class="s4">'Сумма'</span><span class="s2">: </span><span class="s4">'sum'</span><span class="s2">, </span><span class="s4">'Количество'</span><span class="s2">: </span><span class="s4">'sum'</span><span class="s2">}).</span><span class="s1">reset_index</span><span class="s2">()</span>
        <span class="s1">analysis </span><span class="s2">= </span><span class="s1">df_products</span><span class="s2">.</span><span class="s1">merge</span><span class="s2">(</span><span class="s1">sales_by_product</span><span class="s2">, </span><span class="s1">on</span><span class="s2">=</span><span class="s4">'ID'</span><span class="s2">, </span><span class="s1">how</span><span class="s2">=</span><span class="s4">'left'</span><span class="s2">).</span><span class="s1">fillna</span><span class="s2">(</span><span class="s5">0</span><span class="s2">)</span>
        <span class="s1">total </span><span class="s2">= </span><span class="s1">analysis</span><span class="s2">[</span><span class="s4">'Сумма'</span><span class="s2">].</span><span class="s1">sum</span><span class="s2">()</span>
        <span class="s1">analysis</span><span class="s2">[</span><span class="s4">'Доля'</span><span class="s2">] = </span><span class="s1">analysis</span><span class="s2">[</span><span class="s4">'Сумма'</span><span class="s2">] / </span><span class="s1">total </span><span class="s2">* </span><span class="s5">100</span>
        <span class="s1">analysis </span><span class="s2">= </span><span class="s1">analysis</span><span class="s2">.</span><span class="s1">sort_values</span><span class="s2">(</span><span class="s4">'Сумма'</span><span class="s2">, </span><span class="s1">ascending</span><span class="s2">=</span><span class="s0">False</span><span class="s2">)</span>
        <span class="s1">analysis</span><span class="s2">[</span><span class="s4">'Накоплено'</span><span class="s2">] = </span><span class="s1">analysis</span><span class="s2">[</span><span class="s4">'Доля'</span><span class="s2">].</span><span class="s1">cumsum</span><span class="s2">()</span>


        <span class="s0">def </span><span class="s1">get_abc</span><span class="s2">(</span><span class="s1">row</span><span class="s2">):</span>
            <span class="s0">if </span><span class="s1">row</span><span class="s2">[</span><span class="s4">'Накоплено'</span><span class="s2">] &lt;= </span><span class="s5">70</span><span class="s2">:</span>
                <span class="s0">return </span><span class="s4">'A'</span>
            <span class="s0">elif </span><span class="s1">row</span><span class="s2">[</span><span class="s4">'Накоплено'</span><span class="s2">] &lt;= </span><span class="s5">90</span><span class="s2">:</span>
                <span class="s0">return </span><span class="s4">'B'</span>
            <span class="s0">return </span><span class="s4">'C'</span>


        <span class="s1">analysis</span><span class="s2">[</span><span class="s4">'ABC'</span><span class="s2">] = </span><span class="s1">analysis</span><span class="s2">.</span><span class="s1">apply</span><span class="s2">(</span><span class="s1">get_abc</span><span class="s2">, </span><span class="s1">axis</span><span class="s2">=</span><span class="s5">1</span><span class="s2">)</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">dataframe</span><span class="s2">(</span><span class="s1">analysis</span><span class="s2">[[</span><span class="s4">'Название'</span><span class="s2">, </span><span class="s4">'Категория'</span><span class="s2">, </span><span class="s4">'Цена'</span><span class="s2">, </span><span class="s4">'Сумма'</span><span class="s2">, </span><span class="s4">'Доля'</span><span class="s2">, </span><span class="s4">'ABC'</span><span class="s2">]], </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

    <span class="s3"># ФИНАНСОВЫЙ АНАЛИЗ (РАБОТАЮЩИЙ МОДУЛЬ)</span>
    <span class="s0">elif </span><span class="s1">choice </span><span class="s2">== </span><span class="s4">&quot;💰 Финансовый анализ&quot; </span><span class="s0">and </span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">role </span><span class="s2">== </span><span class="s4">&quot;Админ&quot;</span><span class="s2">:</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">header</span><span class="s2">(</span><span class="s4">&quot;💰 Финансовый анализ&quot;</span><span class="s2">)</span>

        <span class="s3"># Расчет финансовых показателей</span>
        <span class="s1">total_revenue </span><span class="s2">= </span><span class="s1">df_sales</span><span class="s2">[</span><span class="s4">'Сумма'</span><span class="s2">].</span><span class="s1">sum</span><span class="s2">()</span>

        <span class="s3"># Расчет себестоимости и прибыли по каждому товару</span>
        <span class="s1">product_finance </span><span class="s2">= []</span>
        <span class="s0">for </span><span class="s1">product </span><span class="s0">in </span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">products</span><span class="s2">:</span>
            <span class="s1">product_sales </span><span class="s2">= </span><span class="s1">df_sales</span><span class="s2">[</span><span class="s1">df_sales</span><span class="s2">[</span><span class="s4">'ID'</span><span class="s2">] == </span><span class="s1">product</span><span class="s2">[</span><span class="s4">'ID'</span><span class="s2">]]</span>
            <span class="s1">revenue </span><span class="s2">= </span><span class="s1">product_sales</span><span class="s2">[</span><span class="s4">'Сумма'</span><span class="s2">].</span><span class="s1">sum</span><span class="s2">()</span>
            <span class="s1">quantity_sold </span><span class="s2">= </span><span class="s1">product_sales</span><span class="s2">[</span><span class="s4">'Количество'</span><span class="s2">].</span><span class="s1">sum</span><span class="s2">()</span>
            <span class="s1">cost </span><span class="s2">= </span><span class="s1">product</span><span class="s2">[</span><span class="s4">'Себестоимость'</span><span class="s2">] * </span><span class="s1">quantity_sold</span>
            <span class="s1">gross_profit </span><span class="s2">= </span><span class="s1">revenue </span><span class="s2">- </span><span class="s1">cost</span>
            <span class="s1">margin </span><span class="s2">= (</span><span class="s1">gross_profit </span><span class="s2">/ </span><span class="s1">revenue </span><span class="s2">* </span><span class="s5">100</span><span class="s2">) </span><span class="s0">if </span><span class="s1">revenue </span><span class="s2">&gt; </span><span class="s5">0 </span><span class="s0">else </span><span class="s5">0</span>

            <span class="s1">product_finance</span><span class="s2">.</span><span class="s1">append</span><span class="s2">({</span>
                <span class="s4">'Товар'</span><span class="s2">: </span><span class="s1">product</span><span class="s2">[</span><span class="s4">'Название'</span><span class="s2">],</span>
                <span class="s4">'Категория'</span><span class="s2">: </span><span class="s1">product</span><span class="s2">[</span><span class="s4">'Категория'</span><span class="s2">],</span>
                <span class="s4">'Выручка'</span><span class="s2">: </span><span class="s1">revenue</span><span class="s2">,</span>
                <span class="s4">'Себестоимость'</span><span class="s2">: </span><span class="s1">cost</span><span class="s2">,</span>
                <span class="s4">'Валовая прибыль'</span><span class="s2">: </span><span class="s1">gross_profit</span><span class="s2">,</span>
                <span class="s4">'Маржинальность %'</span><span class="s2">: </span><span class="s1">margin</span>
            <span class="s2">})</span>

        <span class="s1">df_finance </span><span class="s2">= </span><span class="s1">pd</span><span class="s2">.</span><span class="s1">DataFrame</span><span class="s2">(</span><span class="s1">product_finance</span><span class="s2">)</span>
        <span class="s1">total_cost </span><span class="s2">= </span><span class="s1">df_finance</span><span class="s2">[</span><span class="s4">'Себестоимость'</span><span class="s2">].</span><span class="s1">sum</span><span class="s2">()</span>
        <span class="s1">total_profit </span><span class="s2">= </span><span class="s1">df_finance</span><span class="s2">[</span><span class="s4">'Валовая прибыль'</span><span class="s2">].</span><span class="s1">sum</span><span class="s2">()</span>
        <span class="s1">avg_margin </span><span class="s2">= (</span><span class="s1">total_profit </span><span class="s2">/ </span><span class="s1">total_revenue </span><span class="s2">* </span><span class="s5">100</span><span class="s2">) </span><span class="s0">if </span><span class="s1">total_revenue </span><span class="s2">&gt; </span><span class="s5">0 </span><span class="s0">else </span><span class="s5">0</span>

        <span class="s3"># Метрики</span>
        <span class="s1">col1</span><span class="s2">, </span><span class="s1">col2</span><span class="s2">, </span><span class="s1">col3</span><span class="s2">, </span><span class="s1">col4 </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">columns</span><span class="s2">(</span><span class="s5">4</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col1</span><span class="s2">:</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">metric</span><span class="s2">(</span><span class="s4">&quot;📊 Общая выручка&quot;</span><span class="s2">, </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">total_revenue</span><span class="s0">:</span><span class="s4">,.0f</span><span class="s0">} </span><span class="s4">₽&quot;</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col2</span><span class="s2">:</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">metric</span><span class="s2">(</span><span class="s4">&quot;💰 Общая себестоимость&quot;</span><span class="s2">, </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">total_cost</span><span class="s0">:</span><span class="s4">,.0f</span><span class="s0">} </span><span class="s4">₽&quot;</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col3</span><span class="s2">:</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">metric</span><span class="s2">(</span><span class="s4">&quot;💎 Валовая прибыль&quot;</span><span class="s2">, </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">total_profit</span><span class="s0">:</span><span class="s4">,.0f</span><span class="s0">} </span><span class="s4">₽&quot;</span><span class="s2">, </span><span class="s1">delta</span><span class="s2">=</span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">avg_margin</span><span class="s0">:</span><span class="s4">.1f</span><span class="s0">}</span><span class="s4">% маржа&quot;</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col4</span><span class="s2">:</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">metric</span><span class="s2">(</span><span class="s4">&quot;📈 Средняя маржинальность&quot;</span><span class="s2">, </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">avg_margin</span><span class="s0">:</span><span class="s4">.1f</span><span class="s0">}</span><span class="s4">%&quot;</span><span class="s2">)</span>

        <span class="s3"># График прибыли по товарам</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">subheader</span><span class="s2">(</span><span class="s4">&quot;💵 Прибыль по товарам&quot;</span><span class="s2">)</span>
        <span class="s1">fig_profit </span><span class="s2">= </span><span class="s1">px</span><span class="s2">.</span><span class="s1">bar</span><span class="s2">(</span><span class="s1">df_finance</span><span class="s2">.</span><span class="s1">sort_values</span><span class="s2">(</span><span class="s4">'Валовая прибыль'</span><span class="s2">, </span><span class="s1">ascending</span><span class="s2">=</span><span class="s0">False</span><span class="s2">).</span><span class="s1">head</span><span class="s2">(</span><span class="s5">10</span><span class="s2">),</span>
                            <span class="s1">x</span><span class="s2">=</span><span class="s4">'Товар'</span><span class="s2">, </span><span class="s1">y</span><span class="s2">=</span><span class="s4">'Валовая прибыль'</span><span class="s2">, </span><span class="s1">color</span><span class="s2">=</span><span class="s4">'Маржинальность %'</span><span class="s2">,</span>
                            <span class="s1">color_continuous_scale</span><span class="s2">=</span><span class="s4">'oranges'</span><span class="s2">, </span><span class="s1">title</span><span class="s2">=</span><span class="s4">'Топ-10 товаров по валовой прибыли'</span><span class="s2">)</span>
        <span class="s1">fig_profit</span><span class="s2">.</span><span class="s1">update_layout</span><span class="s2">(</span><span class="s1">xaxis_tickangle</span><span class="s2">=-</span><span class="s5">45</span><span class="s2">)</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">plotly_chart</span><span class="s2">(</span><span class="s1">fig_profit</span><span class="s2">, </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

        <span class="s3"># Маржинальность по категориям</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">subheader</span><span class="s2">(</span><span class="s4">&quot;🏷️ Маржинальность по категориям&quot;</span><span class="s2">)</span>
        <span class="s1">cat_margin </span><span class="s2">= </span><span class="s1">df_finance</span><span class="s2">.</span><span class="s1">groupby</span><span class="s2">(</span><span class="s4">'Категория'</span><span class="s2">).</span><span class="s1">agg</span><span class="s2">({</span>
            <span class="s4">'Выручка'</span><span class="s2">: </span><span class="s4">'sum'</span><span class="s2">,</span>
            <span class="s4">'Себестоимость'</span><span class="s2">: </span><span class="s4">'sum'</span><span class="s2">,</span>
            <span class="s4">'Валовая прибыль'</span><span class="s2">: </span><span class="s4">'sum'</span>
        <span class="s2">}).</span><span class="s1">reset_index</span><span class="s2">()</span>
        <span class="s1">cat_margin</span><span class="s2">[</span><span class="s4">'Маржинальность %'</span><span class="s2">] = (</span><span class="s1">cat_margin</span><span class="s2">[</span><span class="s4">'Валовая прибыль'</span><span class="s2">] / </span><span class="s1">cat_margin</span><span class="s2">[</span><span class="s4">'Выручка'</span><span class="s2">] * </span><span class="s5">100</span><span class="s2">).</span><span class="s1">fillna</span><span class="s2">(</span><span class="s5">0</span><span class="s2">)</span>

        <span class="s1">fig_margin </span><span class="s2">= </span><span class="s1">px</span><span class="s2">.</span><span class="s1">pie</span><span class="s2">(</span><span class="s1">cat_margin</span><span class="s2">, </span><span class="s1">values</span><span class="s2">=</span><span class="s4">'Валовая прибыль'</span><span class="s2">, </span><span class="s1">names</span><span class="s2">=</span><span class="s4">'Категория'</span><span class="s2">,</span>
                            <span class="s1">title</span><span class="s2">=</span><span class="s4">'Распределение прибыли по категориям'</span><span class="s2">, </span><span class="s1">hole</span><span class="s2">=</span><span class="s5">0.4</span><span class="s2">)</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">plotly_chart</span><span class="s2">(</span><span class="s1">fig_margin</span><span class="s2">, </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

        <span class="s3"># Таблица с детальной финансовой информацией</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">subheader</span><span class="s2">(</span><span class="s4">&quot;📋 Детальный финансовый анализ&quot;</span><span class="s2">)</span>
        <span class="s1">df_display </span><span class="s2">= </span><span class="s1">df_finance</span><span class="s2">.</span><span class="s1">sort_values</span><span class="s2">(</span><span class="s4">'Валовая прибыль'</span><span class="s2">, </span><span class="s1">ascending</span><span class="s2">=</span><span class="s0">False</span><span class="s2">)</span>
        <span class="s1">df_display</span><span class="s2">[</span><span class="s4">'Выручка'</span><span class="s2">] = </span><span class="s1">df_display</span><span class="s2">[</span><span class="s4">'Выручка'</span><span class="s2">].</span><span class="s1">apply</span><span class="s2">(</span><span class="s0">lambda </span><span class="s1">x</span><span class="s2">: </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">x</span><span class="s0">:</span><span class="s4">,.0f</span><span class="s0">} </span><span class="s4">₽&quot;</span><span class="s2">)</span>
        <span class="s1">df_display</span><span class="s2">[</span><span class="s4">'Себестоимость'</span><span class="s2">] = </span><span class="s1">df_display</span><span class="s2">[</span><span class="s4">'Себестоимость'</span><span class="s2">].</span><span class="s1">apply</span><span class="s2">(</span><span class="s0">lambda </span><span class="s1">x</span><span class="s2">: </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">x</span><span class="s0">:</span><span class="s4">,.0f</span><span class="s0">} </span><span class="s4">₽&quot;</span><span class="s2">)</span>
        <span class="s1">df_display</span><span class="s2">[</span><span class="s4">'Валовая прибыль'</span><span class="s2">] = </span><span class="s1">df_display</span><span class="s2">[</span><span class="s4">'Валовая прибыль'</span><span class="s2">].</span><span class="s1">apply</span><span class="s2">(</span><span class="s0">lambda </span><span class="s1">x</span><span class="s2">: </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">x</span><span class="s0">:</span><span class="s4">,.0f</span><span class="s0">} </span><span class="s4">₽&quot;</span><span class="s2">)</span>
        <span class="s1">df_display</span><span class="s2">[</span><span class="s4">'Маржинальность %'</span><span class="s2">] = </span><span class="s1">df_display</span><span class="s2">[</span><span class="s4">'Маржинальность %'</span><span class="s2">].</span><span class="s1">apply</span><span class="s2">(</span><span class="s0">lambda </span><span class="s1">x</span><span class="s2">: </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">x</span><span class="s0">:</span><span class="s4">.1f</span><span class="s0">}</span><span class="s4">%&quot;</span><span class="s2">)</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">dataframe</span><span class="s2">(</span><span class="s1">df_display</span><span class="s2">, </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

    <span class="s3"># МАРКЕТИНГОВЫЙ АНАЛИЗ (РАБОТАЮЩИЙ МОДУЛЬ)</span>
    <span class="s0">elif </span><span class="s1">choice </span><span class="s2">== </span><span class="s4">&quot;🎯 Маркетинговый анализ&quot; </span><span class="s0">and </span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">role </span><span class="s2">== </span><span class="s4">&quot;Админ&quot;</span><span class="s2">:</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">header</span><span class="s2">(</span><span class="s4">&quot;🎯 Маркетинговый анализ&quot;</span><span class="s2">)</span>

        <span class="s3"># Анализ популярности товаров</span>
        <span class="s1">popularity_data </span><span class="s2">= []</span>
        <span class="s0">for </span><span class="s1">product </span><span class="s0">in </span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">products</span><span class="s2">:</span>
            <span class="s1">product_sales </span><span class="s2">= </span><span class="s1">df_sales</span><span class="s2">[</span><span class="s1">df_sales</span><span class="s2">[</span><span class="s4">'ID'</span><span class="s2">] == </span><span class="s1">product</span><span class="s2">[</span><span class="s4">'ID'</span><span class="s2">]]</span>
            <span class="s1">quantity_sold </span><span class="s2">= </span><span class="s1">product_sales</span><span class="s2">[</span><span class="s4">'Количество'</span><span class="s2">].</span><span class="s1">sum</span><span class="s2">()</span>
            <span class="s1">revenue </span><span class="s2">= </span><span class="s1">product_sales</span><span class="s2">[</span><span class="s4">'Сумма'</span><span class="s2">].</span><span class="s1">sum</span><span class="s2">()</span>

            <span class="s1">popularity_data</span><span class="s2">.</span><span class="s1">append</span><span class="s2">({</span>
                <span class="s4">'Товар'</span><span class="s2">: </span><span class="s1">product</span><span class="s2">[</span><span class="s4">'Название'</span><span class="s2">],</span>
                <span class="s4">'Категория'</span><span class="s2">: </span><span class="s1">product</span><span class="s2">[</span><span class="s4">'Категория'</span><span class="s2">],</span>
                <span class="s4">'Продано шт'</span><span class="s2">: </span><span class="s1">quantity_sold</span><span class="s2">,</span>
                <span class="s4">'Выручка'</span><span class="s2">: </span><span class="s1">revenue</span><span class="s2">,</span>
                <span class="s4">'Популярность (оценка)'</span><span class="s2">: </span><span class="s1">product</span><span class="s2">[</span><span class="s4">'Популярность'</span><span class="s2">],</span>
                <span class="s4">'Цена'</span><span class="s2">: </span><span class="s1">product</span><span class="s2">[</span><span class="s4">'Цена'</span><span class="s2">]</span>
            <span class="s2">})</span>

        <span class="s1">df_popularity </span><span class="s2">= </span><span class="s1">pd</span><span class="s2">.</span><span class="s1">DataFrame</span><span class="s2">(</span><span class="s1">popularity_data</span><span class="s2">)</span>

        <span class="s3"># Метрики</span>
        <span class="s1">col1</span><span class="s2">, </span><span class="s1">col2</span><span class="s2">, </span><span class="s1">col3</span><span class="s2">, </span><span class="s1">col4 </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">columns</span><span class="s2">(</span><span class="s5">4</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col1</span><span class="s2">:</span>
            <span class="s1">avg_popularity </span><span class="s2">= </span><span class="s1">df_popularity</span><span class="s2">[</span><span class="s4">'Популярность (оценка)'</span><span class="s2">].</span><span class="s1">mean</span><span class="s2">()</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">metric</span><span class="s2">(</span><span class="s4">&quot;⭐ Средняя популярность&quot;</span><span class="s2">, </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">avg_popularity</span><span class="s0">:</span><span class="s4">.1f</span><span class="s0">}</span><span class="s4">/100&quot;</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col2</span><span class="s2">:</span>
            <span class="s1">best_seller </span><span class="s2">= </span><span class="s1">df_popularity</span><span class="s2">.</span><span class="s1">loc</span><span class="s2">[</span><span class="s1">df_popularity</span><span class="s2">[</span><span class="s4">'Продано шт'</span><span class="s2">].</span><span class="s1">idxmax</span><span class="s2">(), </span><span class="s4">'Товар'</span><span class="s2">] </span><span class="s0">if </span><span class="s1">len</span><span class="s2">(</span>
                <span class="s1">df_popularity</span><span class="s2">) &gt; </span><span class="s5">0 </span><span class="s0">else </span><span class="s4">&quot;Нет&quot;</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">metric</span><span class="s2">(</span><span class="s4">&quot;🏆 Самый продаваемый&quot;</span><span class="s2">, </span><span class="s1">best_seller</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col3</span><span class="s2">:</span>
            <span class="s1">total_units </span><span class="s2">= </span><span class="s1">df_popularity</span><span class="s2">[</span><span class="s4">'Продано шт'</span><span class="s2">].</span><span class="s1">sum</span><span class="s2">()</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">metric</span><span class="s2">(</span><span class="s4">&quot;🍰 Всего продано&quot;</span><span class="s2">, </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">total_units</span><span class="s0">:</span><span class="s4">,</span><span class="s0">} </span><span class="s4">шт&quot;</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col4</span><span class="s2">:</span>
            <span class="s1">avg_price </span><span class="s2">= </span><span class="s1">df_popularity</span><span class="s2">[</span><span class="s4">'Цена'</span><span class="s2">].</span><span class="s1">mean</span><span class="s2">()</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">metric</span><span class="s2">(</span><span class="s4">&quot;💵 Средний чек&quot;</span><span class="s2">, </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">avg_price</span><span class="s0">:</span><span class="s4">,.0f</span><span class="s0">} </span><span class="s4">₽&quot;</span><span class="s2">)</span>

        <span class="s3"># График популярности vs продажи</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">subheader</span><span class="s2">(</span><span class="s4">&quot;📊 Связь популярности и продаж&quot;</span><span class="s2">)</span>
        <span class="s1">fig_pop </span><span class="s2">= </span><span class="s1">px</span><span class="s2">.</span><span class="s1">scatter</span><span class="s2">(</span><span class="s1">df_popularity</span><span class="s2">, </span><span class="s1">x</span><span class="s2">=</span><span class="s4">'Популярность (оценка)'</span><span class="s2">, </span><span class="s1">y</span><span class="s2">=</span><span class="s4">'Продано шт'</span><span class="s2">,</span>
                             <span class="s1">size</span><span class="s2">=</span><span class="s4">'Выручка'</span><span class="s2">, </span><span class="s1">color</span><span class="s2">=</span><span class="s4">'Категория'</span><span class="s2">, </span><span class="s1">hover_name</span><span class="s2">=</span><span class="s4">'Товар'</span><span class="s2">,</span>
                             <span class="s1">title</span><span class="s2">=</span><span class="s4">'Зависимость продаж от популярности товара'</span><span class="s2">,</span>
                             <span class="s1">labels</span><span class="s2">={</span><span class="s4">'Популярность (оценка)'</span><span class="s2">: </span><span class="s4">'Популярность (из 100)'</span><span class="s2">,</span>
                                     <span class="s4">'Продано шт'</span><span class="s2">: </span><span class="s4">'Количество продаж'</span><span class="s2">})</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">plotly_chart</span><span class="s2">(</span><span class="s1">fig_pop</span><span class="s2">, </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

        <span class="s3"># Продажи по категориям</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">subheader</span><span class="s2">(</span><span class="s4">&quot;📈 Анализ продаж по категориям&quot;</span><span class="s2">)</span>
        <span class="s1">cat_sales_marketing </span><span class="s2">= </span><span class="s1">df_popularity</span><span class="s2">.</span><span class="s1">groupby</span><span class="s2">(</span><span class="s4">'Категория'</span><span class="s2">).</span><span class="s1">agg</span><span class="s2">({</span>
            <span class="s4">'Продано шт'</span><span class="s2">: </span><span class="s4">'sum'</span><span class="s2">,</span>
            <span class="s4">'Выручка'</span><span class="s2">: </span><span class="s4">'sum'</span>
        <span class="s2">}).</span><span class="s1">reset_index</span><span class="s2">()</span>

        <span class="s1">col1</span><span class="s2">, </span><span class="s1">col2 </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">columns</span><span class="s2">(</span><span class="s5">2</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col1</span><span class="s2">:</span>
            <span class="s1">fig_cat_sales </span><span class="s2">= </span><span class="s1">px</span><span class="s2">.</span><span class="s1">bar</span><span class="s2">(</span><span class="s1">cat_sales_marketing</span><span class="s2">, </span><span class="s1">x</span><span class="s2">=</span><span class="s4">'Категория'</span><span class="s2">, </span><span class="s1">y</span><span class="s2">=</span><span class="s4">'Продано шт'</span><span class="s2">,</span>
                                   <span class="s1">title</span><span class="s2">=</span><span class="s4">'Продажи по категориям (шт)'</span><span class="s2">, </span><span class="s1">color</span><span class="s2">=</span><span class="s4">'Продано шт'</span><span class="s2">,</span>
                                   <span class="s1">color_continuous_scale</span><span class="s2">=</span><span class="s4">'oranges'</span><span class="s2">)</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">plotly_chart</span><span class="s2">(</span><span class="s1">fig_cat_sales</span><span class="s2">, </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col2</span><span class="s2">:</span>
            <span class="s1">fig_cat_rev </span><span class="s2">= </span><span class="s1">px</span><span class="s2">.</span><span class="s1">bar</span><span class="s2">(</span><span class="s1">cat_sales_marketing</span><span class="s2">, </span><span class="s1">x</span><span class="s2">=</span><span class="s4">'Категория'</span><span class="s2">, </span><span class="s1">y</span><span class="s2">=</span><span class="s4">'Выручка'</span><span class="s2">,</span>
                                 <span class="s1">title</span><span class="s2">=</span><span class="s4">'Выручка по категориям (₽)'</span><span class="s2">, </span><span class="s1">color</span><span class="s2">=</span><span class="s4">'Выручка'</span><span class="s2">,</span>
                                 <span class="s1">color_continuous_scale</span><span class="s2">=</span><span class="s4">'oranges'</span><span class="s2">)</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">plotly_chart</span><span class="s2">(</span><span class="s1">fig_cat_rev</span><span class="s2">, </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

        <span class="s3"># Топ товаров по популярности</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">subheader</span><span class="s2">(</span><span class="s4">&quot;🏅 Топ-5 самых популярных товаров&quot;</span><span class="s2">)</span>
        <span class="s1">top_popular </span><span class="s2">= </span><span class="s1">df_popularity</span><span class="s2">.</span><span class="s1">nlargest</span><span class="s2">(</span><span class="s5">5</span><span class="s2">, </span><span class="s4">'Популярность (оценка)'</span><span class="s2">)[</span>
            <span class="s2">[</span><span class="s4">'Товар'</span><span class="s2">, </span><span class="s4">'Категория'</span><span class="s2">, </span><span class="s4">'Популярность (оценка)'</span><span class="s2">, </span><span class="s4">'Продано шт'</span><span class="s2">]]</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">dataframe</span><span class="s2">(</span><span class="s1">top_popular</span><span class="s2">, </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

        <span class="s3"># Рекомендации</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">subheader</span><span class="s2">(</span><span class="s4">&quot;💡 Маркетинговые рекомендации&quot;</span><span class="s2">)</span>

        <span class="s3"># Находим товары с высокой популярностью, но низкими продажами</span>
        <span class="s1">df_popularity</span><span class="s2">[</span><span class="s4">'Эффективность'</span><span class="s2">] = </span><span class="s1">df_popularity</span><span class="s2">[</span><span class="s4">'Продано шт'</span><span class="s2">] / (</span><span class="s1">df_popularity</span><span class="s2">[</span><span class="s4">'Популярность (оценка)'</span><span class="s2">] + </span><span class="s5">1</span><span class="s2">)</span>
        <span class="s1">low_efficiency </span><span class="s2">= </span><span class="s1">df_popularity</span><span class="s2">.</span><span class="s1">nsmallest</span><span class="s2">(</span><span class="s5">3</span><span class="s2">, </span><span class="s4">'Эффективность'</span><span class="s2">)</span>

        <span class="s1">st</span><span class="s2">.</span><span class="s1">markdown</span><span class="s2">(</span><span class="s4">&quot;&quot;&quot; 
        &lt;div style=&quot;background: rgba(255,248,240,0.9); padding: 20px; border-radius: 15px; margin-top: 10px;&quot;&gt; 
        &quot;&quot;&quot;</span><span class="s2">, </span><span class="s1">unsafe_allow_html</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

        <span class="s0">if not </span><span class="s1">low_efficiency</span><span class="s2">.</span><span class="s1">empty</span><span class="s2">:</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">write</span><span class="s2">(</span><span class="s4">&quot;🔍 **Требуют продвижения:**&quot;</span><span class="s2">)</span>
            <span class="s0">for </span><span class="s1">_</span><span class="s2">, </span><span class="s1">row </span><span class="s0">in </span><span class="s1">low_efficiency</span><span class="s2">.</span><span class="s1">iterrows</span><span class="s2">():</span>
                <span class="s1">st</span><span class="s2">.</span><span class="s1">write</span><span class="s2">(</span>
                    <span class="s4">f&quot;   • *</span><span class="s0">{</span><span class="s1">row</span><span class="s2">[</span><span class="s4">'Товар'</span><span class="s2">]</span><span class="s0">}</span><span class="s4">* — популярность </span><span class="s0">{</span><span class="s1">row</span><span class="s2">[</span><span class="s4">'Популярность (оценка)'</span><span class="s2">]</span><span class="s0">:</span><span class="s4">.0f</span><span class="s0">}</span><span class="s4">/100, но продано всего </span><span class="s0">{</span><span class="s1">row</span><span class="s2">[</span><span class="s4">'Продано шт'</span><span class="s2">]</span><span class="s0">:</span><span class="s4">.0f</span><span class="s0">} </span><span class="s4">шт&quot;</span><span class="s2">)</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">write</span><span class="s2">(</span><span class="s4">&quot;   *Рекомендация:* Усилить рекламную кампанию или сделать акцию на эти товары.&quot;</span><span class="s2">)</span>

        <span class="s1">st</span><span class="s2">.</span><span class="s1">markdown</span><span class="s2">(</span><span class="s4">&quot;&quot;&quot; 
        &lt;hr&gt; 
        &lt;p style=&quot;text-align: center;&quot;&gt;📢 Рекомендуется проводить кросс-продажи популярных товаров и запустить программу лояльности для постоянных клиентов.&lt;/p&gt; 
        &lt;/div&gt; 
        &quot;&quot;&quot;</span><span class="s2">, </span><span class="s1">unsafe_allow_html</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

    <span class="s3"># ПРОИЗВОДСТВЕННАЯ АНАЛИТИКА</span>
    <span class="s0">elif </span><span class="s1">choice </span><span class="s2">== </span><span class="s4">&quot;🔧 Производственная аналитика&quot; </span><span class="s0">and </span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">role </span><span class="s2">== </span><span class="s4">&quot;Админ&quot;</span><span class="s2">:</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">header</span><span class="s2">(</span><span class="s4">&quot;🔧 Производственная аналитика&quot;</span><span class="s2">)</span>

        <span class="s3"># Расчет производственных показателей</span>
        <span class="s1">prod_data </span><span class="s2">= []</span>
        <span class="s0">for </span><span class="s1">product </span><span class="s0">in </span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">products</span><span class="s2">:</span>
            <span class="s1">product_sales </span><span class="s2">= </span><span class="s1">df_sales</span><span class="s2">[</span><span class="s1">df_sales</span><span class="s2">[</span><span class="s4">'ID'</span><span class="s2">] == </span><span class="s1">product</span><span class="s2">[</span><span class="s4">'ID'</span><span class="s2">]]</span>
            <span class="s1">quantity_sold </span><span class="s2">= </span><span class="s1">product_sales</span><span class="s2">[</span><span class="s4">'Количество'</span><span class="s2">].</span><span class="s1">sum</span><span class="s2">()</span>

            <span class="s1">labor_cost </span><span class="s2">= </span><span class="s1">product</span><span class="s2">[</span><span class="s4">'Ручная_работа_минут'</span><span class="s2">] * </span><span class="s1">quantity_sold</span>
            <span class="s1">labor_hours </span><span class="s2">= </span><span class="s1">labor_cost </span><span class="s2">/ </span><span class="s5">60</span>

            <span class="s1">prod_data</span><span class="s2">.</span><span class="s1">append</span><span class="s2">({</span>
                <span class="s4">'Товар'</span><span class="s2">: </span><span class="s1">product</span><span class="s2">[</span><span class="s4">'Название'</span><span class="s2">],</span>
                <span class="s4">'Категория'</span><span class="s2">: </span><span class="s1">product</span><span class="s2">[</span><span class="s4">'Категория'</span><span class="s2">],</span>
                <span class="s4">'Продано шт'</span><span class="s2">: </span><span class="s1">quantity_sold</span><span class="s2">,</span>
                <span class="s4">'Ручная работа (мин/шт)'</span><span class="s2">: </span><span class="s1">product</span><span class="s2">[</span><span class="s4">'Ручная_работа_минут'</span><span class="s2">],</span>
                <span class="s4">'Всего минут'</span><span class="s2">: </span><span class="s1">labor_cost</span><span class="s2">,</span>
                <span class="s4">'Всего часов'</span><span class="s2">: </span><span class="s1">labor_hours</span><span class="s2">,</span>
                <span class="s4">'Срок годности (ч)'</span><span class="s2">: </span><span class="s1">product</span><span class="s2">[</span><span class="s4">'Срок_годности_часов'</span><span class="s2">]</span>
            <span class="s2">})</span>

        <span class="s1">df_prod </span><span class="s2">= </span><span class="s1">pd</span><span class="s2">.</span><span class="s1">DataFrame</span><span class="s2">(</span><span class="s1">prod_data</span><span class="s2">)</span>
        <span class="s1">total_labor_hours </span><span class="s2">= </span><span class="s1">df_prod</span><span class="s2">[</span><span class="s4">'Всего часов'</span><span class="s2">].</span><span class="s1">sum</span><span class="s2">()</span>

        <span class="s1">col1</span><span class="s2">, </span><span class="s1">col2</span><span class="s2">, </span><span class="s1">col3 </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">columns</span><span class="s2">(</span><span class="s5">3</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col1</span><span class="s2">:</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">metric</span><span class="s2">(</span><span class="s4">&quot;⏱️ Общие трудозатраты&quot;</span><span class="s2">, </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">total_labor_hours</span><span class="s0">:</span><span class="s4">.1f</span><span class="s0">} </span><span class="s4">часов&quot;</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col2</span><span class="s2">:</span>
            <span class="s1">avg_labor </span><span class="s2">= </span><span class="s1">df_prod</span><span class="s2">[</span><span class="s4">'Ручная работа (мин/шт)'</span><span class="s2">].</span><span class="s1">mean</span><span class="s2">()</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">metric</span><span class="s2">(</span><span class="s4">&quot;👩‍🍳 Среднее время на 1 шт&quot;</span><span class="s2">, </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">avg_labor</span><span class="s0">:</span><span class="s4">.0f</span><span class="s0">} </span><span class="s4">минут&quot;</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col3</span><span class="s2">:</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">metric</span><span class="s2">(</span><span class="s4">&quot;📦 Всего произведено&quot;</span><span class="s2">, </span><span class="s4">f&quot;</span><span class="s0">{</span><span class="s1">df_prod</span><span class="s2">[</span><span class="s4">'Продано шт'</span><span class="s2">].</span><span class="s1">sum</span><span class="s2">()</span><span class="s0">:</span><span class="s4">.0f</span><span class="s0">} </span><span class="s4">шт&quot;</span><span class="s2">)</span>

        <span class="s3"># График трудозатрат</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">subheader</span><span class="s2">(</span><span class="s4">&quot;⏰ Трудозатраты по товарам&quot;</span><span class="s2">)</span>
        <span class="s1">fig_labor </span><span class="s2">= </span><span class="s1">px</span><span class="s2">.</span><span class="s1">bar</span><span class="s2">(</span><span class="s1">df_prod</span><span class="s2">.</span><span class="s1">sort_values</span><span class="s2">(</span><span class="s4">'Всего часов'</span><span class="s2">, </span><span class="s1">ascending</span><span class="s2">=</span><span class="s0">False</span><span class="s2">).</span><span class="s1">head</span><span class="s2">(</span><span class="s5">10</span><span class="s2">),</span>
                           <span class="s1">x</span><span class="s2">=</span><span class="s4">'Товар'</span><span class="s2">, </span><span class="s1">y</span><span class="s2">=</span><span class="s4">'Всего часов'</span><span class="s2">, </span><span class="s1">color</span><span class="s2">=</span><span class="s4">'Категория'</span><span class="s2">,</span>
                           <span class="s1">title</span><span class="s2">=</span><span class="s4">'Топ-10 товаров по трудозатратам (часы)'</span><span class="s2">)</span>
        <span class="s1">fig_labor</span><span class="s2">.</span><span class="s1">update_layout</span><span class="s2">(</span><span class="s1">xaxis_tickangle</span><span class="s2">=-</span><span class="s5">45</span><span class="s2">)</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">plotly_chart</span><span class="s2">(</span><span class="s1">fig_labor</span><span class="s2">, </span><span class="s1">use_container_width</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

        <span class="s1">st</span><span class="s2">.</span><span class="s1">info</span><span class="s2">(</span><span class="s4">&quot;📊 Производственный анализ показывает загрузку персонала и трудозатраты на каждый товар&quot;</span><span class="s2">)</span>

    <span class="s3"># НОВЫЙ ДЕСЕРТ</span>
    <span class="s0">elif </span><span class="s1">choice </span><span class="s2">== </span><span class="s4">&quot;➕ Новый десерт&quot; </span><span class="s0">and </span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">role </span><span class="s2">== </span><span class="s4">&quot;Админ&quot;</span><span class="s2">:</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">header</span><span class="s2">(</span><span class="s4">&quot;➕ Добавление десерта&quot;</span><span class="s2">)</span>
        <span class="s1">col1</span><span class="s2">, </span><span class="s1">col2 </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">columns</span><span class="s2">(</span><span class="s5">2</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col1</span><span class="s2">:</span>
            <span class="s1">name </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">text_input</span><span class="s2">(</span><span class="s4">&quot;Название&quot;</span><span class="s2">)</span>
            <span class="s1">cat </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">selectbox</span><span class="s2">(</span><span class="s4">&quot;Категория&quot;</span><span class="s2">, [</span><span class="s4">&quot;Торты&quot;</span><span class="s2">, </span><span class="s4">&quot;Пирожные&quot;</span><span class="s2">, </span><span class="s4">&quot;Капкейки&quot;</span><span class="s2">, </span><span class="s4">&quot;Выпечка&quot;</span><span class="s2">, </span><span class="s4">&quot;Печенье&quot;</span><span class="s2">])</span>
            <span class="s1">price </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">number_input</span><span class="s2">(</span><span class="s4">&quot;Цена (₽)&quot;</span><span class="s2">, </span><span class="s5">50</span><span class="s2">, </span><span class="s5">2000</span><span class="s2">, </span><span class="s5">300</span><span class="s2">)</span>
        <span class="s0">with </span><span class="s1">col2</span><span class="s2">:</span>
            <span class="s1">weight </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">selectbox</span><span class="s2">(</span><span class="s4">&quot;Вес&quot;</span><span class="s2">, [</span><span class="s4">&quot;100г&quot;</span><span class="s2">, </span><span class="s4">&quot;150г&quot;</span><span class="s2">, </span><span class="s4">&quot;200г&quot;</span><span class="s2">, </span><span class="s4">&quot;250г&quot;</span><span class="s2">, </span><span class="s4">&quot;500г&quot;</span><span class="s2">, </span><span class="s4">&quot;1кг&quot;</span><span class="s2">])</span>
            <span class="s1">stock </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">number_input</span><span class="s2">(</span><span class="s4">&quot;Остаток&quot;</span><span class="s2">, </span><span class="s5">0</span><span class="s2">, </span><span class="s5">100</span><span class="s2">, </span><span class="s5">10</span><span class="s2">)</span>
            <span class="s1">cost </span><span class="s2">= </span><span class="s1">st</span><span class="s2">.</span><span class="s1">number_input</span><span class="s2">(</span><span class="s4">&quot;Себестоимость (₽)&quot;</span><span class="s2">, </span><span class="s5">10</span><span class="s2">, </span><span class="s5">1000</span><span class="s2">, </span><span class="s5">100</span><span class="s2">)</span>

        <span class="s0">if </span><span class="s1">st</span><span class="s2">.</span><span class="s1">button</span><span class="s2">(</span><span class="s4">&quot;✨ Добавить&quot;</span><span class="s2">):</span>
            <span class="s1">new_id </span><span class="s2">= </span><span class="s1">max</span><span class="s2">(</span><span class="s1">p</span><span class="s2">[</span><span class="s4">&quot;ID&quot;</span><span class="s2">] </span><span class="s0">for </span><span class="s1">p </span><span class="s0">in </span><span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">products</span><span class="s2">) + </span><span class="s5">1</span>
            <span class="s1">weight_kg </span><span class="s2">= </span><span class="s1">float</span><span class="s2">(</span><span class="s1">weight</span><span class="s2">.</span><span class="s1">replace</span><span class="s2">(</span><span class="s4">&quot;г&quot;</span><span class="s2">, </span><span class="s4">&quot;&quot;</span><span class="s2">).</span><span class="s1">replace</span><span class="s2">(</span><span class="s4">&quot;кг&quot;</span><span class="s2">, </span><span class="s4">&quot;&quot;</span><span class="s2">)) / </span><span class="s5">1000 </span><span class="s0">if </span><span class="s4">&quot;г&quot; </span><span class="s0">in </span><span class="s1">weight </span><span class="s0">else </span><span class="s1">float</span><span class="s2">(</span>
                <span class="s1">weight</span><span class="s2">.</span><span class="s1">replace</span><span class="s2">(</span><span class="s4">&quot;кг&quot;</span><span class="s2">, </span><span class="s4">&quot;&quot;</span><span class="s2">))</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">session_state</span><span class="s2">.</span><span class="s1">products</span><span class="s2">.</span><span class="s1">append</span><span class="s2">({</span>
                <span class="s4">&quot;ID&quot;</span><span class="s2">: </span><span class="s1">new_id</span><span class="s2">, </span><span class="s4">&quot;Название&quot;</span><span class="s2">: </span><span class="s1">name</span><span class="s2">, </span><span class="s4">&quot;Категория&quot;</span><span class="s2">: </span><span class="s1">cat</span><span class="s2">, </span><span class="s4">&quot;Вес&quot;</span><span class="s2">: </span><span class="s1">weight</span><span class="s2">,</span>
                <span class="s4">&quot;Вес_кг&quot;</span><span class="s2">: </span><span class="s1">weight_kg</span><span class="s2">, </span><span class="s4">&quot;Цена&quot;</span><span class="s2">: </span><span class="s1">price</span><span class="s2">, </span><span class="s4">&quot;Себестоимость&quot;</span><span class="s2">: </span><span class="s1">cost</span><span class="s2">,</span>
                <span class="s4">&quot;Остаток&quot;</span><span class="s2">: </span><span class="s1">stock</span><span class="s2">, </span><span class="s4">&quot;Популярность&quot;</span><span class="s2">: </span><span class="s5">70</span><span class="s2">, </span><span class="s4">&quot;Срок_годности_часов&quot;</span><span class="s2">: </span><span class="s5">48</span><span class="s2">, </span><span class="s4">&quot;Ручная_работа_минут&quot;</span><span class="s2">: </span><span class="s5">10</span>
            <span class="s2">})</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">success</span><span class="s2">(</span><span class="s4">f&quot;Десерт '</span><span class="s0">{</span><span class="s1">name</span><span class="s0">}</span><span class="s4">' добавлен!&quot;</span><span class="s2">)</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">rerun</span><span class="s2">()</span>

    <span class="s3"># МОБИЛЬНАЯ ВЕРСИЯ</span>
    <span class="s0">elif </span><span class="s1">choice </span><span class="s2">== </span><span class="s4">&quot;📱 Мобильная версия&quot;</span><span class="s2">:</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">header</span><span class="s2">(</span><span class="s4">&quot;📱 Мобильная версия&quot;</span><span class="s2">)</span>
        <span class="s1">st</span><span class="s2">.</span><span class="s1">info</span><span class="s2">(</span><span class="s4">&quot;Адаптивный режим для мобильных устройств&quot;</span><span class="s2">)</span>
        <span class="s0">if </span><span class="s1">st</span><span class="s2">.</span><span class="s1">toggle</span><span class="s2">(</span><span class="s4">&quot;Адаптивный режим&quot;</span><span class="s2">):</span>
            <span class="s1">st</span><span class="s2">.</span><span class="s1">success</span><span class="s2">(</span><span class="s4">&quot;Включен адаптивный режим&quot;</span><span class="s2">)</span>

<span class="s3"># Информация об авторе</span>
<span class="s1">st</span><span class="s2">.</span><span class="s1">markdown</span><span class="s2">(</span><span class="s4">&quot;---&quot;</span><span class="s2">)</span>
<span class="s1">st</span><span class="s2">.</span><span class="s1">markdown</span><span class="s2">(</span><span class="s4">&quot;&quot;&quot; 
&lt;div class=&quot;author-info&quot;&gt; 
    &lt;p&gt;© 2026 SweetMaster | Сладкая кондитерская&lt;/p&gt; 
    &lt;p&gt;👨‍🍳 Разработчик: Шарнин Семён (ИС-944)&lt;/p&gt; 
&lt;/div&gt; 
&quot;&quot;&quot;</span><span class="s2">, </span><span class="s1">unsafe_allow_html</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span></pre>
</body>
</html>