from pytubefix import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
from concurrent.futures import ThreadPoolExecutor, as_completed
import os


def convert_to_mp3(video_path, mp3_path=None):
    if mp3_path is None:
        mp3_path = os.path.splitext(video_path)[0] + ".mp3"

    with VideoFileClip(video_path) as video:
        audio = video.audio
        audio.write_audiofile(mp3_path, codec="mp3")
        audio.close()

    return mp3_path


def download_and_convert(link, output_path="."):
    try:
        print(f"[+] Iniciando: {link}")
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        video_path = stream.download(output_path=output_path)
        mp3_path = convert_to_mp3(video_path)
        print(f"[✓] Finalizado: {link} -> {mp3_path}")
        return mp3_path
    except Exception as e:
        print(f"[!] Erro em {link}: {e}")
        return None


def main():
    links = [
        "https://youtu.be/WtA1Ux4hB68?si=4d2fUITI6vpMVnhl",
        "https://youtu.be/nyKCX7wM4bg?si=0XpgW0KXrimfiSEU",
        "https://www.youtube.com/watch?v=uLcJIqdFpFM",
        "https://www.youtube.com/watch?v=xNRtGCwmoQw",
        "https://www.youtube.com/watch?v=a_rxi0ujVGI",
        "https://www.youtube.com/watch?v=bxo9mtJjvS0",
        "https://www.youtube.com/watch?v=KSKjY-TXZ4U",
        "https://www.youtube.com/watch?v=EXePBB2BYpc",
        "https://www.youtube.com/watch?v=Z_HhD0f1LKU",
        "https://youtu.be/nHC3ylRf000?si=SK3z3clsLNPik0Jn",
    ]

    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(download_and_convert, link, output_dir) for link in links
        ]

        for future in as_completed(futures):
            result = future.result()
            if result:
                print(f"[✓] MP3 salvo em: {result}")


if __name__ == "__main__":
    main()
