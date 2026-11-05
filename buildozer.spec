rm -f ~/capri_native/buildozer.spec
cat << 'EOF' > ~/capri_native/buildozer.spec
[app]
title = Capri AI
package.name = capri_ai
package.domain = org.capri
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,pyjnius,plyer,requests
orientation = portrait
android.api = 33
android.minapi = 23
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = RECORD_AUDIO,FOREGROUND_SERVICE,SYSTEM_ALERT_WINDOW,INTERNET
p4a.branch = master
EOF
