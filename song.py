class Song:
    def __init__(self, title, artist, genre, filepath):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.filepath = filepath

# Predefined list of songs with dummy file paths
songs = [
    Song("Shape of You", "Ed Sheeran", "Pop", "/music/pop/shape_of_you.mp3"),
    Song("Blinding Lights", "The Weeknd", "Pop", "/music/pop/blinding_lights.mp3"),
    Song("Tera Ban Jaunga", "Akhil Sachdeva", "Romantic", "/music/romantic/tera_ban_jaunga.mp3"),
    Song("Hallelujah", "Leonard Cohen", "Folk", "/music/folk/hallelujah.mp3"),
    Song("Rolling in the Deep", "Adele", "Pop", "/music/pop/rolling_in_the_deep.mp3"),
    Song("Take Me Home, Country Roads", "John Denver", "Country", "/music/country/take_me_home.mp3"),
    Song("Bohemian Rhapsody", "Queen", "Rock", "/music/rock/bohemian_rhapsody.mp3"),
    Song("Hotel California", "Eagles", "Rock", "/music/rock/hotel_california.mp3"),
    Song("Someone Like You", "Adele", "Pop", "/music/pop/someone_like_you.mp3"),
    Song("Thinking Out Loud", "Ed Sheeran", "Pop", "/music/pop/thinking_out_loud.mp3"),
    Song("Bad Guy", "Billie Eilish", "Pop", "/music/pop/bad_guy.mp3"),
    Song("Smells Like Teen Spirit", "Nirvana", "Rock", "/music/rock/smells_like_teen_spirit.mp3"),
    Song("Let It Be", "The Beatles", "Rock", "/music/rock/let_it_be.mp3"),
    Song("Sweet Child O' Mine", "Guns N' Roses", "Rock", "/music/rock/sweet_child_o_mine.mp3"),
    Song("All of Me", "John Legend", "Soul", "/music/soul/all_of_me.mp3"),
    Song("Imagine", "John Lennon", "Pop", "/music/pop/imagine.mp3"),
    Song("Perfect", "Ed Sheeran", "Pop", "/music/pop/perfect.mp3"),
    Song("Shallow", "Lady Gaga", "Pop", "/music/pop/shallow.mp3"),
    Song("Yesterday", "The Beatles", "Rock", "/music/rock/yesterday.mp3"),
    Song("Believer", "Imagine Dragons", "Rock", "/music/rock/believer.mp3"),

    # Urdu Songs
    Song("Tajdar-e-Haram", "Atif Aslam", "Sufi", "/music/sufi/tajdar_e_haram.mp3"),
    Song("Dil Diyan Gallan", "Atif Aslam", "Romantic", "/music/romantic/dil_diyan_gallan.mp3"),
    Song("Afreen Afreen", "Rahat Fateh Ali Khan", "Sufi", "/music/sufi/afreen_afreen.mp3"),
    Song("Jeene Laga Hoon", "Atif Aslam", "Romantic", "/music/romantic/jeene_laga_hoon.mp3"),
    Song("Zindagi Gulzar Hai", "Ali Zafar", "Pop", "/music/pop/zindagi_gulzar_hai.mp3"),
    Song("Mast Qalandar", "Nusrat Fateh Ali Khan", "Sufi", "/music/sufi/mast_qalandar.mp3"),
    Song("Pehli Nazar Mein", "Atif Aslam", "Romantic", "/music/romantic/pehli_nazar_mein.mp3"),
    Song("Channa Mereya", "Arijit Singh", "Romantic", "/music/romantic/channa_mereya.mp3"),
    Song("Kahani Suno", "Kaifi Khalil", "Pop", "/music/pop/kahani_suno.mp3"),
    Song("Mera Saeein", "Rahim Shah", "Sufi", "/music/sufi/mera_saeein.mp3"),
    Song("Dastaan-e-Ishq", "Shafqat Amanat Ali", "Romantic", "/music/romantic/dastaan_e_ishq.mp3"),
    Song("Bulleya", "Abida Parveen", "Sufi", "/music/sufi/bulleya.mp3"),
    Song("Dil Meri Na Sune", "Rahat Fateh Ali Khan", "Pop", "/music/pop/dil_meri_na_sune.mp3"),
    Song("Meri Zindagi Hai Tu", "Atif Aslam", "Romantic", "/music/romantic/meri_zindagi_hai_tu.mp3"),
    Song("Tera Hone Laga Hoon", "Amitabh Bhattacharya", "Romantic", "/music/romantic/tera_hone_laga_hoon.mp3"),
    Song("Jannat", "Ali Zafar", "Romantic", "/music/romantic/jannat.mp3"),
    Song("Sun Saathiya", "Priya Saraiya", "Romantic", "/music/romantic/sun_saathiya.mp3"),
    Song("Khuda Ki Azmat", "Abida Parveen", "Sufi", "/music/sufi/khuda_ki_azmat.mp3"),

    # Punjabi Songs
    Song("Laung Laachi", "Mannat Noor", "Folk", "/music/folk/laung_laachi.mp3"),
    Song("Tareefan", "Badshah", "Pop", "/music/pop/tareefan.mp3"),
    Song("Ve Maahi", "Arijit Singh", "Romantic", "/music/romantic/ve_maahi.mp3"),
    Song("Pakka Punjabi", "Mankirt Aulakh", "Bhangra", "/music/bhangra/pakka_punjabi.mp3"),
    Song("Mann Bharrya", "B Praak", "Romantic", "/music/romantic/mann_bharrya.mp3"),
    Song("3 Peg", "Sharry Mann", "Bhangra", "/music/bhangra/3_peg.mp3"),
    Song("Lahore", "Guru Randhawa", "Pop", "/music/pop/lahore.mp3"),
    Song("Munde Di Jatti", "Naseebo Lal", "Folk", "/music/folk/munde_di_jatti.mp3"),
    Song("High Rated Gabru", "Guru Randhawa", "Pop", "/music/pop/high_rated_gabru.mp3"),
    Song("Laake Jatti", "Ammy Virk", "Bhangra", "/music/bhangra/laake_jatti.mp3"),
    Song("Jatt Waadi", "Mankirt Aulakh", "Bhangra", "/music/bhangra/jatt_waadi.mp3"),
    Song("Gallan Goodiyan", "Shankar-Ehsaan-Loy", "Folk", "/music/folk/gallan_goodiyan.mp3"),
    Song("Patiala Peg", "Diljit Dosanjh", "Bhangra", "/music/bhangra/patiala_peg.mp3"),
    Song("Suit Suit", "Guru Randhawa", "Pop", "/music/pop/suit_suit.mp3"),
    Song("Sadi Gali", "Lehmber Hussainpuri", "Bhangra", "/music/bhangra/sadi_gali.mp3"),
    Song("Kya Baat Ay", "Hardy Sandhu", "Pop", "/music/pop/kya_baat_ay.mp3"),
    Song("So High", "Sidhu Moosewala", "Bhangra", "/music/bhangra/so_high.mp3"),
    Song("Akhar", "Satinder Sartaaj", "Sufi", "/music/sufi/akhar.mp3"),
    Song("Raat Di Gedi", "Diljit Dosanjh", "Bhangra", "/music/bhangra/raat_di_gedi.mp3"),
    Song("Tere Te", "Sidhu Moosewala", "Pop", "/music/pop/tere_te.mp3")
]
