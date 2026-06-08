<html>
<head>
<title>setup_app.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cf8e6d;}
.s1 { color: #bcbec4;}
.s2 { color: #bcbec4;}
.s3 { color: #7a7e85;}
.s4 { color: #5f826b; font-style: italic;}
.s5 { color: #6aab73;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
setup_app.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">os</span>
<span class="s0">import </span><span class="s1">sys</span>
<span class="s0">import </span><span class="s1">subprocess</span>

<span class="s0">import </span><span class="s1">streamlit </span><span class="s0">as </span><span class="s1">st</span>
<span class="s0">from </span><span class="s1">datetime </span><span class="s0">import </span><span class="s1">datetime</span><span class="s2">, </span><span class="s1">timedelta</span>
<span class="s0">import </span><span class="s1">random</span>
<span class="s0">import </span><span class="s1">pandas </span><span class="s0">as </span><span class="s1">pd</span>
<span class="s0">import </span><span class="s1">plotly</span><span class="s2">.</span><span class="s1">express </span><span class="s0">as </span><span class="s1">px</span>
<span class="s0">import </span><span class="s1">plotly</span><span class="s2">.</span><span class="s1">graph_objects </span><span class="s0">as </span><span class="s1">go</span>


<span class="s3"># Добавьте PWA манифест и service worker</span>
<span class="s0">def </span><span class="s1">add_pwa_support</span><span class="s2">():</span>
    <span class="s4">&quot;&quot;&quot;Добавляет поддержку PWA для установки на телефон&quot;&quot;&quot;</span>

    <span class="s3"># Манифест для PWA</span>
    <span class="s1">manifest </span><span class="s2">= </span><span class="s5">&quot;&quot;&quot; 
    &lt;link rel=&quot;manifest&quot; href=&quot;/manifest.json&quot;&gt; 
    &lt;meta name=&quot;apple-mobile-web-app-capable&quot; content=&quot;yes&quot;&gt; 
    &lt;meta name=&quot;apple-mobile-web-app-status-bar-style&quot; content=&quot;black-translucent&quot;&gt; 
    &lt;meta name=&quot;apple-mobile-web-app-title&quot; content=&quot;SweetMaster&quot;&gt; 
    &lt;meta name=&quot;theme-color&quot; content=&quot;#d48c4a&quot;&gt; 
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0, viewport-fit=cover&quot;&gt; 
    &quot;&quot;&quot;</span>

    <span class="s1">st</span><span class="s2">.</span><span class="s1">markdown</span><span class="s2">(</span><span class="s1">manifest</span><span class="s2">, </span><span class="s1">unsafe_allow_html</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

    <span class="s3"># JavaScript для service worker</span>
    <span class="s1">pwa_js </span><span class="s2">= </span><span class="s5">&quot;&quot;&quot; 
    &lt;script&gt; 
    if ('serviceWorker' in navigator) { 
        navigator.serviceWorker.register('/sw.js') 
        .then(function(reg) { 
            console.log('Service Worker registered'); 
        }) 
        .catch(function(err) { 
            console.log('Service Worker registration failed: ', err); 
        }); 
    } 
 
    let deferredPrompt; 
    window.addEventListener('beforeinstallprompt', (e) =&gt; { 
        e.preventDefault(); 
        deferredPrompt = e; 
 
        // Показываем кнопку установки 
        const installBtn = document.createElement('button'); 
        installBtn.textContent = '📱 Установить приложение'; 
        installBtn.style.cssText = ` 
            position: fixed; 
            bottom: 20px; 
            right: 20px; 
            background: linear-gradient(135deg, #e8a96a, #d48c4a); 
            color: white; 
            border: none; 
            border-radius: 50px; 
            padding: 12px 24px; 
            z-index: 9999; 
            cursor: pointer; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.2); 
            font-weight: bold; 
        `; 
 
        installBtn.addEventListener('click', () =&gt; { 
            deferredPrompt.prompt(); 
            deferredPrompt.userChoice.then((choiceResult) =&gt; { 
                if (choiceResult.outcome === 'accepted') { 
                    console.log('User accepted the install prompt'); 
                } 
                installBtn.remove(); 
                deferredPrompt = null; 
            }); 
        }); 
 
        document.body.appendChild(installBtn); 
    }); 
    &lt;/script&gt; 
    &quot;&quot;&quot;</span>

    <span class="s1">st</span><span class="s2">.</span><span class="s1">markdown</span><span class="s2">(</span><span class="s1">pwa_js</span><span class="s2">, </span><span class="s1">unsafe_allow_html</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>


<span class="s3"># Вызовите функцию в начале</span>
<span class="s1">add_pwa_support</span><span class="s2">()</span>


<span class="s3"># Остальной ваш код...</span>
<span class="s0">def </span><span class="s1">create_spec_file</span><span class="s2">():</span>
    <span class="s4">&quot;&quot;&quot;Создает spec-файл для PyInstaller&quot;&quot;&quot;</span>
    <span class="s1">spec_content </span><span class="s2">= </span><span class="s5">&quot;&quot;&quot; 
# -*- mode: python ; coding: utf-8 -*- 
 
a = Analysis( 
    ['app.py'], 
    pathex=[], 
    binaries=[], 
    datas=[ 
        ('C:/Users/username/AppData/Local/Programs/Python/Python311/Lib/site-packages/streamlit', 'streamlit'), 
        ('C:/Users/username/AppData/Local/Programs/Python/Python311/Lib/site-packages/pandas', 'pandas'), 
    ], 
    hiddenimports=[ 
        'streamlit', 
        'pandas', 
        'plotly', 
        'plotly.express', 
        'plotly.graph_objects', 
        'streamlit.runtime', 
        'streamlit.web', 
        'streamlit.web.cli' 
    ], 
    hookspath=[], 
    hooksconfig={}, 
    runtime_hooks=[], 
    excludes=[], 
    noarchive=False, 
) 
 
pyz = PYZ(a.pure) 
 
exe = EXE( 
    pyz, 
    a.scripts, 
    a.binaries, 
    a.datas, 
    [], 
    name='SweetMaster', 
    debug=False, 
    bootloader_ignore_signals=False, 
    strip=False, 
    upx=True, 
    upx_exclude=[], 
    runtime_tmpdir=None, 
    console=True,  # Показывать консоль для отладки 
    disable_windowed_traceback=False, 
    argv_emulation=False, 
    target_arch=None, 
    codesign_identity=None, 
    entitlements_file=None, 
    icon='icon.ico'  # Добавьте иконку если есть 
) 
&quot;&quot;&quot;</span>

    <span class="s0">with </span><span class="s1">open</span><span class="s2">(</span><span class="s5">'sweetmaster.spec'</span><span class="s2">, </span><span class="s5">'w'</span><span class="s2">, </span><span class="s1">encoding</span><span class="s2">=</span><span class="s5">'utf-8'</span><span class="s2">) </span><span class="s0">as </span><span class="s1">f</span><span class="s2">:</span>
        <span class="s1">f</span><span class="s2">.</span><span class="s1">write</span><span class="s2">(</span><span class="s1">spec_content</span><span class="s2">)</span>


<span class="s0">def </span><span class="s1">create_launcher</span><span class="s2">():</span>
    <span class="s4">&quot;&quot;&quot;Создает лаунчер для запуска Streamlit приложения&quot;&quot;&quot;</span>
    <span class="s1">launcher_content </span><span class="s2">= </span><span class="s5">''' 
import subprocess 
import sys 
import os 
import webbrowser 
import time 
import socket 
 
def find_free_port(): 
    &quot;&quot;&quot;Находит свободный порт&quot;&quot;&quot; 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        s.bind(('', 0)) 
        s.listen(1) 
        port = s.getsockname()[1] 
    return port 
 
def main(): 
    port = find_free_port() 
 
    # Запускаем Streamlit приложение 
    cmd = [ 
        sys.executable, '-m', 'streamlit', 'run', 'app.py', 
        '--server.port', str(port), 
        '--server.headless', 'true', 
        '--browser.serverAddress', 'localhost', 
        '--server.enableCORS', 'false', 
        '--server.enableXsrfProtection', 'false' 
    ] 
 
    # Открываем браузер через секунду 
    def open_browser(): 
        time.sleep(1.5) 
        webbrowser.open(f'http://localhost:{port}') 
 
    import threading 
    threading.Thread(target=open_browser, daemon=True).start() 
 
    # Запускаем процесс 
    process = subprocess.Popen(cmd) 
 
    try: 
        process.wait() 
    except KeyboardInterrupt: 
        process.terminate() 
 
if __name__ == '__main__': 
    main() 
'''</span>

    <span class="s0">with </span><span class="s1">open</span><span class="s2">(</span><span class="s5">'launcher.py'</span><span class="s2">, </span><span class="s5">'w'</span><span class="s2">, </span><span class="s1">encoding</span><span class="s2">=</span><span class="s5">'utf-8'</span><span class="s2">) </span><span class="s0">as </span><span class="s1">f</span><span class="s2">:</span>
        <span class="s1">f</span><span class="s2">.</span><span class="s1">write</span><span class="s2">(</span><span class="s1">launcher_content</span><span class="s2">)</span>


<span class="s0">def </span><span class="s1">create_batch_file</span><span class="s2">():</span>
    <span class="s4">&quot;&quot;&quot;Создает BAT файл для быстрого запуска&quot;&quot;&quot;</span>
    <span class="s1">batch_content </span><span class="s2">= </span><span class="s5">'''@echo off 
echo Starting SweetMaster... 
start &quot;&quot; python launcher.py 
exit 
'''</span>

    <span class="s0">with </span><span class="s1">open</span><span class="s2">(</span><span class="s5">'start_app.bat'</span><span class="s2">, </span><span class="s5">'w'</span><span class="s2">, </span><span class="s1">encoding</span><span class="s2">=</span><span class="s5">'utf-8'</span><span class="s2">) </span><span class="s0">as </span><span class="s1">f</span><span class="s2">:</span>
        <span class="s1">f</span><span class="s2">.</span><span class="s1">write</span><span class="s2">(</span><span class="s1">batch_content</span><span class="s2">)</span>


<span class="s0">if </span><span class="s1">__name__ </span><span class="s2">== </span><span class="s5">'__main__'</span><span class="s2">:</span>
    <span class="s1">print</span><span class="s2">(</span><span class="s5">&quot;Создание файлов для сборки приложения...&quot;</span><span class="s2">)</span>
    <span class="s1">create_spec_file</span><span class="s2">()</span>
    <span class="s1">create_launcher</span><span class="s2">()</span>
    <span class="s1">create_batch_file</span><span class="s2">()</span>
    <span class="s1">print</span><span class="s2">(</span><span class="s5">&quot;&quot;&quot; 
Готово! Теперь выполните команды: 
 
1. Для создания EXE файла: 
   pyinstaller sweetmaster.spec 
 
2. Приложение будет в папке 'dist/SweetMaster/' 
 
ИЛИ для быстрого запуска: 
   Используйте start_app.bat 
    &quot;&quot;&quot;</span><span class="s2">)</span></pre>
</body>
</html>