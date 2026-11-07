[app]
title = Capri AI
package.name = capri_ai
package.domain = org.capri
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Фиксируем версии Python, Kivy, pyjnius и Cython
requirements = python3==3.12.9, hostpython3==3.12.9, kivy==2.3.1, pyjnius==1.4.0, cython==3.0.11

orientation = portrait
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = RECORD_AUDIO,FOREGROUND_SERVICE,SYSTEM_ALERT_WINDOW,INTERNET
android.archs = arm64-v8a
p4a.branch = master
