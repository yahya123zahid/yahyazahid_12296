import requests

# Meminta input URL dari pengguna
tiktok_url = input("Masukkan URL video TikTok: ")

# Gunakan API pihak ketiga seperti Snaptik atau lainnya
api_url = f"https://api.snaptik.app/download?url={tiktok_url}"

try:
    # Kirim permintaan ke API
    response = requests.get(api_url)
    response.raise_for_status()  # Menangani error HTTP
    
    video_data = response.json()
    
    if "url" in video_data:
        video_link = video_data["url"]
        print(f"Video siap didownload dari: {video_link}")
        
        # Download video
        video_content = requests.get(video_link).content
        with open("tiktok_video.mp4", "wb") as f:
            f.write(video_content)
        
        print("✅ Download berhasil! Video tersimpan sebagai 'tiktok_video.mp4'.")
    else:
        print("⚠ Gagal mendapatkan link video.")
except requests.exceptions.RequestException as e:
    print(f"❌ Terjadi kesalahan: {e}")
