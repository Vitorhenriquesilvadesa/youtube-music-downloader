from pytubefix import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def convert_to_mp3(video_path, mp3_path=None):
    if mp3_path is None:
        mp3_path = os.path.splitext(video_path)[0] + '.mp3'
    
    with VideoFileClip(video_path) as video:
        audio = video.audio
        audio.write_audiofile(mp3_path, codec='mp3')
        audio.close()
    
    return mp3_path

def download(link, output_path='.'):
    youtube_video = YouTube(link)
    stream = youtube_video.streams.get_highest_resolution()
    output_file = stream.download(output_path=output_path)
    return output_file

def main():
    links = [
        'https://youtu.be/G04wzqSZaSg?si=E3KRCWuKyWnWre-I',
        'https://youtu.be/OLURGq3VdNM?si=-q6FcZDPA4qr08jp',
        'https://youtu.be/o4HrvYNi9o4?si=wtPVmxwX5_4QMjDZ',
        'https://youtu.be/31Baj4N2Crw?si=YseZq6ZgkM8-D1HN',
        'https://youtu.be/ez7bz7juHvw?si=45fmjYVi0fiIG0J1',
        'https://youtu.be/2pwQ0ixD1NU?si=fo0xFNSd4Jeq-zN3',
        'https://youtu.be/6VKkoOkA6Kc?si=7atglN6GffJBqAAH',
        'https://youtu.be/Y-M5P93HHmM?si=97Xpc-2DxSOOKHNT',
        'https://youtu.be/oHUWuMP52YA?si=4d0icXw2a8sQule-',
        'https://youtu.be/kPa7bsKwL-c?si=IuopQNBH_dUuudIP',
        'https://youtu.be/QvYSckKSL5g?si=1kAWk9qj0yN0Bq_V',
        'https://youtu.be/6h4BuzcCDfI?si=L4yiEXUSQGJFHUJf',
        'https://youtu.be/3OFWabmJ4Lc?si=6icY4HuALSiEOcUY',
        'https://youtu.be/rhfWrND1evE?si=2Bs7LGUbs15S_oim',
        'https://youtu.be/a4HL9u798EM?si=Zgt-oKkl6RipElLK',
        'https://youtu.be/kNWKuKI_844?si=MfcGiIE2Yp-y_2Ds',
        'https://youtu.be/_r6AEkGjudQ?si=xLDIeWIWllqmc0wK',
        'https://youtu.be/CzG5zaobF30?si=PthA8IeaVsz9l8bu',
        'https://youtu.be/M_KZs_D_wSk?si=oJmZqwdJzOPvexuK',
    ]
    
    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)

    for link in links:
        print(f"Baixando: {link}")
        video_path = download(link, output_dir)
        print(f"Convertendo para mp3: {video_path}")
        mp3_path = convert_to_mp3(video_path)
        print(f"Salvo mp3 em: {mp3_path}")

if __name__ == "__main__":
    main()
