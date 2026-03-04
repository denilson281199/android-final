[app]
title = System Update
package.name = sysupdate
package.domain = org.android.logs
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

# Android
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30
android.ndk_path = 
android.sdk_path = 
android.accept_sdk_license = True
android.permissions = INTERNET
