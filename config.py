"""
RadioPlayerV2, Telegram Voice Chat Userbot
Copyright (C) 2021  Asm Safone <https://t.me/asmsafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re


class Config:
    ADMIN = os.environ.get("ADMINS", "1832447570")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", "3898418"))
    CHAT = int(os.environ.get("CHAT", "-1001489244957"))
    LOG_GROUP = os.environ.get("LOG_GROUP", "")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None
    STREAM_URL = os.environ.get("STREAM_URL", "https://radioindia.net/radio/hungamanow/icecast.audio")
    API_HASH = os.environ.get("API_HASH", "5a82313211da04d63297bd4de436228c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1645277361:AAG15fdypo92MVNP-73flxcUgmJjTLi9BHw") 
    SESSION = os.environ.get("SESSION_STRING", "BQAXiBfd_2Cfe1s_K_ajo8XGsmKwwX4eYSe1EG1nhGXbLFkelgbdlJH-wRciDRZq6lYTDfXlGVEhE_qJf4WMKIh5SzhOR_m8Kr00hBqWcAZqFT5ynKsKEhnKgR_dIvuCqcu7-dwbtiCNvmG7xpL4N1ek6MP3QUA7ON74E6w9Gdr3MVpuPbwkDpdmc0CtRs-W0h67I-k_T8mTgGviRBA82M1XQfc8_cw7ZbPb28dN3Xa3l8DNSkBzNn8p-gZ_np4c7P50HDUlkiIZd9rfv_Wt_KVxv2uawqeBUtYYRB1jeiUw8Or1-cKNU0m5XO9GmJsoBUEuULrB_2j1fq-wV7rBalI0X9XNvAA")

