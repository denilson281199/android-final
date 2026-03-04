[app]
title = System Update
package.name = sysupdate
package.domain = org.android.logs
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

# Android specific
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 34
android.ndk_path = 
android.sdk_path = 
android.ant_path = 
android.gradle_dependencies = 
android.permissions = INTERNET
android.extra_src = 
