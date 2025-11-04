# 🤖 Telegram Auto Forwarder (Telethon)

Script sederhana untuk meneruskan pesan otomatis dari satu grup ke grup lain menggunakan **Telethon**.

---

## 🚀 Fitur
- Meneruskan **teks dan media (foto, video, dokumen, dll.)**
- Menghapus media sementara setelah dikirim
- Logging status pesan terkirim di terminal

---

## 🧠 Persiapan

1. **Clone repo ini:**
   ```bash
   git clone https://github.com/verifiedlabs/telegram_forwarder.git
   cd telegram_forwarder
   ```

2. **Install dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Edit file `forwarder.py`:**
   Ganti dengan kredensial dan grup kamu:
   ```python
   api_id = 'YOUR_API_ID'
   api_hash = 'YOUR_API_HASH'
   source_group = 123456789  # ID grup sumber
   destination_group_username = "targetgroup"  # tanpa @
   ```

4. **Jalankan bot:**
   ```bash
   python forwarder.py
   ```

---

## 📂 Struktur File

```
forwarder.py         # Script utama
requirements.txt     # Daftar library
downloads/           # Folder media sementara
```

---

## ⚙️ Catatan
- Gunakan API ID & hash milikmu sendiri dari [my.telegram.org](https://my.telegram.org).
- Pastikan akun kamu sudah join ke grup sumber dan target.
- Bot ini **menggunakan akun pribadi (bukan bot token)**.

---

> 🧩 Buatan: [Verified Labs](https://github.com/verifiedlabs)
