define r = Character("Raka", color="#87CEEB")
define n = Character("Nadia", color="#FFB6C1")
define by = Character("Bu Yuni", color="#90EE90")
define pd = Character("Pak Dodi", color="#F4A460")
define t = Character("Terra", color="#40E0D0", what_prefix='"', what_suffix='"')

image bg kelas = "kelas.jpg"
image bg kantin = "kantin.jpg"
image bg laptop = "laptop.jpg"
image bg bank sampah = "bank_sampah.jpg"
image img linear economy = "linear_economy_diagram.png"
image img circular economy = "circular_economy_diagram.png"

image raka = "raka.png"
image yuni = "bu_yuni.png"
image dodi = "pak_dodi.png"
image nadia = "nadia.png"
image terra avatar = "terra.png"

transform fullscreen:
    xsize config.screen_width
    ysize config.screen_height

transform bottom_right:
    xalign 1.0
    yalign 1.0
    zoom 1.8
    matrixcolor BrightnessMatrix(0.0)

transform bottom_left:
    xalign 0.0
    yalign 1.0
    zoom 1.8
    matrixcolor BrightnessMatrix(0.0)

transform bottom_center:
    xalign 0.5
    yalign 1.0
    zoom 1.8
    matrixcolor BrightnessMatrix(0.0)

transform on_laptop:
    xalign 0.525
    yalign 0.78
    zoom 0.5

transform bottom_right_bottom:
    xalign 1.0
    yalign 1.8
    zoom 2.0
    matrixcolor BrightnessMatrix(0.0)

transform bottom_left_bottom:
    xalign 0.0
    yalign 1.8
    zoom 2.0
    matrixcolor BrightnessMatrix(0.0)

transform bottom_right_bottom_dim:
    xalign 1.0
    yalign 1.8
    zoom 2.0
    matrixcolor BrightnessMatrix(-0.6)

transform bottom_left_bottom_dim:
    xalign 0.0
    yalign 1.8
    zoom 2.0
    matrixcolor BrightnessMatrix(-0.6)

transform bottom_right_dim:
    xalign 1.0
    yalign 1.0
    zoom 1.8
    matrixcolor BrightnessMatrix(-0.6)

transform bottom_left_dim:
    xalign 0.0
    yalign 1.0
    zoom 1.8
    matrixcolor BrightnessMatrix(-0.6)

transform bottom_center_dim:
    xalign 0.5
    yalign 1.0
    zoom 1.8
    matrixcolor BrightnessMatrix(-0.6)

transform center_on_board:
    xalign 0.75
    yalign 0.38
    zoom 0.5

label start:
    stop music
    play music "audio/theme_calm.mp3" volume 0.8

    scene bg kantin at fullscreen with fade
    "--- Jam Istirahat, di Kantin Sekolah ---"
    voice "audio/scene1/kalimat1.mp3"
    "Aku baru saja akan membuang nampanku. Sisa nasi goreng yang tak habis, botol plastik teh, dan bungkus keripik. Tiga poin, langsung masuk keranjang sampah."
    voice "audio/scene1/kalimat2.mp3"
    "Tiba-tiba, Raka menahanku dengan lembut. Ia menatap nampanku, bukan dengan tatapan menghakimi, tapi lebih seperti... heran."

    show raka at bottom_right
    show nadia at bottom_left
    with moveinleft

    show nadia at bottom_left_dim
    voice "audio/scene1/kalimat3.mp3"
    r "Yakin mau dibuang semua, Nad?"

    show raka at bottom_right_dim
    show nadia at bottom_left
    voice "audio/scene1/kalimat4.mp3"
    n "Kenapa? Udah kenyang. Lagian cuma sisa sedikit."
    
    show raka at bottom_right
    show nadia at bottom_left_dim
    voice "audio/scene1/kalimat5.mp3"
    r "Bukan cuma soal sisa sedikitnya. Tapi coba lihat, ada sisa makanan, ada plastik, ada kemasan. Ini bukan cuma sampah, ini adalah 'jejak' kita."
    
    show raka at bottom_right_dim
    show nadia at bottom_left
    voice "audio/scene1/kalimat6.mp3"
    n "Jejak? Maksudmu?"

    show raka at bottom_right
    show nadia at bottom_left_dim
    voice "audio/scene1/kalimat7.mp3"
    r "Setiap tahun, Indonesia membuang sekitar 23-48 juta ton makanan. Makanan sisa kita di TPA itu menghasilkan gas metana, yang 28 kali lebih berbahaya dari karbon dioksida untuk iklim."

    show raka at bottom_right_dim
    show nadia at bottom_left
    voice "audio/scene1/kalimat8.mp3"
    n "(Aku terdiam. Gas metana? Dari sisa nasi gorengku? Tiba-tiba ini terasa lebih serius dari sekadar membuang sampah.)"
    voice "audio/scene1/kalimat9.mp3"
    n "Oke... oke, aku paham soal makanan. Tapi botol ini kan cuma plastik biasa."

    show raka at bottom_right
    show nadia at bottom_left_dim
    voice "audio/scene1/kalimat10.mp3"
    r "Itu masalah lainnya. Kebiasaan 'sekali pakai-buang'. Ini semua terhubung dalam satu masalah besar: cara kita mengonsumsi dan berproduksi tidak bertanggung jawab."
    
    show raka at bottom_right_dim
    show nadia at bottom_left
    voice "audio/scene1/kalimat11.mp3"
    n "Konsumsi dan Produksi yang Bertanggung Jawab... Istilahnya berat banget."

    show raka at bottom_right
    show nadia at bottom_left_dim
    voice "audio/scene1/kalimat12.mp3"
    r "Memang. Itu salah satu dari 17 Tujuan Pembangunan Berkelanjutan, atau SDGs. Nomor 12, tepatnya. Kebetulan Bu Yuni mau mengadakan seminar singkat soal ini. Mau ikut? Ini bukan cuma soal sampah, tapi soal bagaimana kita bisa hidup lebih baik tanpa merusak planet."
    
    show raka at bottom_right_dim
    show nadia at bottom_left
    voice "audio/scene1/kalimat13.mp3"
    n "SDGs... Oke, kedengarannya penting. Aku ikut."

    scene bg kelas at fullscreen with dissolve
    "--- Pulang Sekolah, di Ruang Seminar ---"
    "Di depan, Bu Yuni menampilkan slide dengan judul besar: 'SDG 12: Menjadi Konsumen dan Produsen Cerdas'."

    show yuni at bottom_center zorder 2
    
    voice "audio/scene2/kalimat1.mp3"
    by "Selamat sore, anak-anak. Kalian semua adalah konsumen. Setiap hari kalian membeli, menggunakan, dan membuang. Tapi pernahkah kita berpikir, dari mana semua itu datang dan ke mana perginya?"
    
    voice "audio/scene2/kalimat2.mp3"
    by "Saat ini, kita hidup dalam 'Ekonomi Linear'. Ambil dari alam, kita olah jadi produk, kita pakai, lalu kita buang. Garis lurus menuju kerusakan."
    
    show img linear economy at center_on_board zorder 1 with dissolve
    
    voice "audio/scene2/kalimat3.mp3"
    by "Model ini menguras sumber daya alam kita yang terbatas dan mencemari lingkungan. Setiap produk yang kita beli memiliki 'Jejak Ekologis'—jumlah air, tanah, dan energi yang dibutuhkan untuk membuatnya."
    
    hide img linear economy with dissolve
    
    voice "audio/scene2/kalimat4.mp3"
    by "Kita butuh model baru. Sebuah 'Ekonomi Sirkular'."
    
    show img circular economy at center_on_board zorder 1 with dissolve
    
    voice "audio/scene2/kalimat5.mp3"
    by "Di sini, tidak ada 'sampah'. Semua dirancang agar bisa digunakan kembali, diperbaiki, atau didaur ulang menjadi produk baru. Ini adalah siklus regeneratif yang meniru alam."
    
    voice "audio/scene2/kalimat6.mp3"
    by "Kuncinya ada pada kita. Dengan mengubah cara kita mengonsumsi, kita mengirim sinyal ke produsen untuk menciptakan produk yang lebih ramah lingkungan. Perubahan dimulai dari pilihan kita sehari-hari."
    
    hide img circular economy with dissolve
    hide yuni with moveoutbottom

    scene bg laptop at fullscreen with fade
    "--- Keesokan Harinya, di Perpustakaan ---"

    show raka at bottom_right_bottom
    show nadia at bottom_left_bottom
    voice "audio/scene3/kalimat1.mp3"
    r "Kenalan dulu, ini Terra."

    show terra avatar at on_laptop with dissolve
    "Avatar AI itu muncul di layar laptop."

    show raka at bottom_right_bottom_dim
    show nadia at bottom_left_bottom_dim
    voice "audio/scene3/kalimat2.mp3"
    t "Selamat datang kembali, Nadia. Analisis menunjukkan tingkat kesadaranmu terhadap isu keberlanjutan meningkat 450%%. Mari kita lanjutkan."

    show raka at bottom_right_bottom_dim
    show nadia at bottom_left_bottom    
    voice "audio/scene3/kalimat3.mp3"
    n "Terra, bagaimana cara menerapkan ekonomi sirkular dalam hidupku sebagai pelajar?"

    show raka at bottom_right_bottom_dim
    show nadia at bottom_left_bottom_dim
    voice "audio/scene3/kalimat4.mp3"
    t "Pertanyaan bagus. Kita bisa menggunakan kerangka 4R. Bukan hanya 3R."

    voice "audio/scene3/kalimat5.mp3"
    t "'Refuse' (Menolak) adalah yang pertama dan terkuat. Tolak sedotan plastik, kantong kresek, atau brosur yang tidak perlu. Ini mencegah sampah bahkan sebelum tercipta."
    
    voice "audio/scene3/kalimat6.mp3"
    t "'Reduce' (Mengurangi) adalah mengurangi apa yang kita butuhkan. Contoh, membeli satu baju berkualitas tinggi yang tahan lama lebih baik daripada tiga baju 'fast fashion' yang cepat rusak."
    
    voice "audio/scene3/kalimat7.mp3"
    t "'Reuse' (Menggunakan Kembali) adalah memperpanjang umur barang. Industri tekstil adalah pencemar air kedua terbesar di dunia. Dengan melakukan 'thrifting' atau barter seragam, Anda secara langsung mengurangi jejak air tersebut."
    
    voice "audio/scene3/kalimat8.mp3"
    t "'Recycle' (Mendaur Ulang) adalah pilihan terakhir. Mengapa? Karena proses daur ulang sendiri masih membutuhkan energi. Namun, mendaur ulang satu kaleng aluminium dapat menghemat energi yang cukup untuk menyalakan TV selama 3 jam."

    show raka at bottom_right_bottom
    show nadia at bottom_left_bottom_dim
    voice "audio/scene3/kalimat9.mp3"
    r "Jadi, kita butuh sebuah sistem yang mendukung keempat pilar ini di sekolah?"

    show raka at bottom_right_bottom_dim
    show nadia at bottom_left_bottom_dim
    voice "audio/scene3/kalimat10.mp3"
    t "Tepat sekali. Sebuah 'Pusat Inovasi Sirkular' yang tidak hanya mengelola sampah, tapi mengubah perilaku dari akarnya."

    show raka at bottom_right_bottom_dim
    show nadia at bottom_left_bottom
    voice "audio/scene3/kalimat11.mp3"
    n "Refuse, Reduce, Reuse, Recycle... Sekarang aku benar-benar paham urutannya."

    hide terra avatar with dissolve

    # --- SCENE 4: MERANCANG RENCANA AKSI YANG KOMPREHENSIF ---
    scene bg kelas at fullscreen with dissolve
    "--- Siang Hari, Merancang Proyek ---"
    
    show raka at bottom_right_dim
    show nadia at bottom_left
    voice "audio/scene4/kalimat1.mp3"
    n "Oke, 'Pusat Inovasi Sirkular' kita harus punya empat pilar, sesuai saran Terra."

    show raka at bottom_right
    show nadia at bottom_left_dim
    voice "audio/scene4/kalimat2.mp3"
    r "Setuju! Pilar pertama, {b}Refuse & Reduce{/b}. Kita kampanyekan 'Jumat Bebas Sekali Pakai'. Tidak ada botol atau kemasan plastik di hari itu. Kita beri insentif untuk kelas yang paling patuh."

    show raka at bottom_right_dim
    show nadia at bottom_left
    voice "audio/scene4/kalimat3.mp3"
    n "Aku suka itu! Pilar kedua, {b}Reuse{/b}. 'Pojok Barter' kita perluas. Bukan cuma buku dan seragam, tapi juga peralatan olahraga, bahkan barang hobi. Kita adakan 'Repair Cafe' sebulan sekali, di mana siswa bisa belajar memperbaiki barang elektronik sederhana atau menjahit."
    
    show raka at bottom_right
    show nadia at bottom_left_dim
    voice "audio/scene4/kalimat4.mp3"
    r "Brilian, Nad! Itu membangun keterampilan! Pilar ketiga, {b}Recycle{/b}. 'Bank Sampah Cerdas' kita tetap jalan, tapi kita tambahkan satu hal krusial..."
    
    show raka at bottom_right_dim
    show nadia at bottom_left
    voice "audio/scene4/kalimat5.mp3"
    n "Apa itu?"
    
    show raka at bottom_right
    show nadia at bottom_left_dim
    voice "audio/scene4/kalimat6.mp3"
    r "Pengelolaan sampah organik! Kita buat lubang kompos untuk sisa makanan dari kantin. Komposnya bisa kita pakai untuk kebun sekolah."
    
    show raka at bottom_right_dim
    show nadia at bottom_left
    voice "audio/scene4/kalimat7.mp3"
    n "Itu jenius! Itu langsung menyelesaikan masalah sampah makanan yang kamu sebutkan! Jadi pilar keempat adalah {b}Edukasi{/b}. Kita harus terus menyebarkan informasi ini lewat mading, media sosial sekolah, dan seminar kecil."
    
    show raka at bottom_right
    show nadia at bottom_left_dim
    voice "audio/scene4/kalimat8.mp3"
    r "Tepat. Infrastruktur tanpa perubahan pola pikir akan sia-sia. Rencana ini sempurna. Ayo kita ajukan ke Pak Dodi."

    # --- SCENE 5: PRESENTASI BERBASIS DATA ---
    scene bg kantin at fullscreen with dissolve
    "--- Menemui Pak Dodi ---"
    "Kami masuk ke ruangan Pak Dodi bukan dengan proposal, tapi dengan sebuah visi yang didukung data."

    show dodi at bottom_center
    voice "audio/scene5/kalimat1.mp3"
    pd "Raka, Nadia. Ada apa?"

    voice "audio/scene5/kalimat2.mp3"
    r "Selamat siang, Pak. Kami ingin mengajukan proposal untuk 'Pusat Inovasi Sirkular SMAN 1', sebuah program untuk mewujudkan SDG 12 di lingkungan sekolah kita."
    
    voice "audio/scene5/kalimat3.mp3"
    n "Program ini berdiri di atas empat pilar, Pak: Menolak & Mengurangi, Menggunakan Kembali, Mendaur Ulang, serta Edukasi Berkelanjutan. "
    
    voice "audio/scene5/kalimat4.mp3"
    n "Kami tidak hanya akan mengurangi sampah plastik, tapi juga mengatasi sampah makanan melalui pengomposan, dan mengurangi limbah tekstil melalui 'Pojok Barter' dan 'Repair Cafe'."
    
    voice "audio/scene5/kalimat5.mp3"
    r "Berdasarkan analisis data, program ini berpotensi mengurangi volume sampah total sekolah hingga 50%% dan menciptakan sumber pendapatan baru dari bank sampah serta pupuk kompos. "
    
    voice "audio/scene5/kalimat6.mp3"
    r "Ini bukan program kebersihan, Pak. Ini adalah laboratorium hidup bagi siswa untuk menjadi pemimpin masa depan yang berkelanjutan."
    
    pd "..."
    "Pak Dodi menatap kami, lalu tersenyum lebar."
    
    voice "audio/scene5/kalimat7.mp3"
    pd "Anak-anak, ini bukan sekadar proposal. Ini adalah masterplan. Kalian telah memikirkan semuanya, dari akar masalah hingga solusi yang terukur dan edukatif. Sekolah tidak hanya mendukung, sekolah akan menjadikan ini program unggulan kita. Segera bentuk tim kalian."
    
    n "(Kami berhasil!)"
    hide dodi

    # --- SCENE 6: EPILOG - DAMPAK YANG TERUKUR DAN BERKELANJUTAN ---
    scene bg bank sampah at fullscreen with fade
    "--- Satu Tahun Kemudian ---"
    "Sekolah kami telah bertransformasi. 'Jumat Bebas Sekali Pakai' menjadi tradisi. 'Pojok Barter' dan 'Repair Cafe' adalah pusat kegiatan sosial yang ramai. Dan di belakang sekolah, tumpukan kompos kami mengubah sisa makanan menjadi 'emas hitam' untuk kebun."

    show raka at bottom_right_dim
    show nadia at bottom_left
    voice "audio/scene6/kalimat1.mp3"
    n "Lihat papan data itu, Rak. Dalam setahun, kita berhasil mencegah 50.000 botol plastik dan 5 ton sampah makanan masuk ke TPA."
    
    show raka at bottom_right
    show nadia at bottom_left_dim
    voice "audio/scene6/kalimat2.mp3"
    r "Dan 'Pojok Barter' kita telah memfasilitasi pertukaran lebih dari 1000 item. Itu penghematan sumber daya dan uang saku yang luar biasa."
    
    show raka at bottom_right_dim
    show nadia at bottom_left
    voice "audio/scene6/kalimat3.mp3"
    n "Yang paling aku banggakan adalah tim edukasi kita. Mereka sekarang diundang ke SMP sebelah untuk berbagi tentang program ini."
    
    show raka at bottom_right
    show nadia at bottom_left_dim
    voice "audio/scene6/kalimat4.mp3"
    r "Lihat kan? Perubahan itu menular. Dulu kamu pikir ini semua hanya soal sampah di nampanmu."
    
    show raka at bottom_right_dim
    show nadia at bottom_left
    voice "audio/scene6/kalimat5.mp3"
    n "Dan sekarang aku tahu. Ini bukan hanya soal sampah. Ini soal merancang masa depan yang kita inginkan, satu pilihan cerdas pada satu waktu."

    scene black with fade
    centered "Perjalanan menuju konsumsi dan produksi yang bertanggung jawab dimulai dari satu kesadaran.\nDengan menolak, mengurangi, menggunakan kembali, dan mendaur ulang, kita tidak hanya menyelamatkan planet.\nKita membangun kreativitas, komunitas, dan masa depan yang lebih adil untuk semua.\nInilah kekuatan sejati dari SDG 12."
    pause
    
    return