[app]
title = Capri AI
package.name = capri_ai
package.domain = org.capri
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# ЗОЛОТАЯ СВЯЗКА: Python 3.10, Kivy 2.3.0, Cython 0.29.36
requirements = python3==3.10.12, hostpython3==3.10.12, kivy==2.3.0, cython==0.29.36

orientation = portrait
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = RECORD_AUDIO,FOREGROUND_SERVICE,SYSTEM_ALERT_WINDOW,INTERNET
android.archs = arm64-v8a
p4a.branch = master
