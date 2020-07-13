import pyrogram, tgcrypto
from ascii import userbyte_string

print(userbyte_string)
print("\nCreate Userbyte String Session\n")

APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")

with pyrogram.Client(":memory:", api_id=APP_ID, api_hash=API_HASH) as byte:
  
  byte_str = byte.export_session_string()
  byte.send_message("me", byte_str)
  byte.send_message("me", "👆This is your Userbyte String Session 👆\n▶️▶️ [Click Here](url) To Create Again ◀️◀️")
  
  print("Check Your Telegram Saved Messages")
