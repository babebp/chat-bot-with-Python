import os, binascii
webhook_endpoint = (binascii.b2a_hex(os.urandom(30))).decode("utf-8")
print(webhook_endpoint)

VERIFY_TOKEN = (binascii.b2a_hex(os.urandom(25))).decode("utf-8") # put this value in bot.views.py
print(VERIFY_TOKEN)

# c63e313b2235ac8744df7b1f4a2a66100a383c964b0d40a8723a82ba410b
# 2b6d15f1166b10fc6f66a28abb5bda6790e886bba0e6e2c184