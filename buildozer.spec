[app]
title = Capri AI
package.name = capri_ai
package.domain = org.capri
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Добавили requests для работы с Groq
requirements = python3==3.10.12, hostpython3==3.10.12, kivy==2.3.0, cython==0.29.36, requests

orientation = portrait
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = INTERNET
android.archs = arm64-v8a
p4a.branch = master
