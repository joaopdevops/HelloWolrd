import sys
pip install - U yt-dlp
yt-dlp - -skip-download - -yes-playlist - -print "%(playlist_index)02d;%(duration_string)s;%(title)s" "https://youtube.com/playlist?list=PLdpzxOOAlwvIKMhk8WhzN1pYoJ1YU8Csa" > devops_playlist.csv
yt-dlp - -skip-download - -yes-playlist - -print "%(duration)s" "https://youtube.com/playlist?list=PLdpzxOOAlwvIKMhk8WhzN1pYoJ1YU8Csa" \
    | python - << 'PY'
total = sum(int(x) for x in sys.stdin if x.strip().isdigit())
h, r = divmod(total, 3600)
m, s = divmod(r, 60)
print(f"Tempo total da playlist: {h:02d}:{m:02d}:{s:02d}")
PY
