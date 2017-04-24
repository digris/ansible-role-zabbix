# -*- coding: utf-8 -*-

tg_key = "{{ zabbix_plugin_zbxtg_key }}"  # telegram bot api key

zbx_tg_prefix = "zbxtg"  # variable for separating text from script info
zbx_tg_tmp_dir = "/tmp/" + zbx_tg_prefix  # directory for saving caches, uids, cookies, etc.
zbx_tg_signature = False

zbx_server = "https://{{ zabbix_hostname }}"  # zabbix server full url
zbx_api_user = "{{ zabbix_plugin_zbxtg_api_user }}"
zbx_api_pass = "{{ zabbix_plugin_zbxtg_api_password }}"
zbx_api_verify = True  # True - do not ignore self signed certificates, False - ignore

proxy_to_zbx = None
proxy_to_tg = None

emoji_map = {
    "ok": "✅",
    "problem": "❗",
    "info": "ℹ️",
    "warning": "⚠️",
    "disaster": "❌",
    "bomb": "💣",
    "fire": "🔥",
    "hankey": "💩",
}
