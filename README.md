Fairuz Akhtar Randrasyah
2406403955
PBP D
Tugas 2 Individu

Link PWS: https://fairuz-akhtar-kickngoal.pbp.cs.ui.ac.id/

1.  - Pertama yaitu saya inisiasi dahulu folder lokal baru bernama KickNGoal (nama football shop saya), saya inisiasi project django baru dengan nama yang sama. Saya inisiasi dulu dengan benar dan mengconnectkannya ke Github dan juga PWS sebelum lanjut membuat app-nya.
    - Setelah konfigurasi settle, environment telah tersambung dengan git dan pws secara benar, baru saya membuat aplikasi dengan nama main menggunakan command 'python manage.py startapp main' lalu saya masukkan ke INSTALLED_APPS.
    - Lalu, saya melakukan routing dengan membuat file urls.py baru di main dan mengatur urls.py di proyek agar dapat mengarahkan ke aplikasi main.
    - Selanjutnya, saya define model dengan menambahkan class Product dengan attribute wajib name, price, description, thumbnail, category, is_featured dan attribute tambahan stock, dan brand. Setelah mendefinisikan model, saya migrasi untuk membuat tabel yang sesuai di database.
    - Setelah itu, saya buat folder baru bernama templates di main dan membuat file baru didalamnya bernama main.html untuk menjadi tampilan dan mengubah views untuk menampilkan info yang sesuai pada halaman yaitu greetings, nama, npm, dan kelas
    - Dan terakhir, saya deploy ke PWS dan tak lupa untuk push ke repositori Github

2.  Client Request → urls.py → views.py → models.py (akses data)
                                  ↓
                              templates/main.html ← context data
                                  ↓
                             HTTP Response → Client

    urls.py: routing URL ke view yang sesuai
    views.py: business logic, memproses request dan mengembalikan response
    models.py: define struktur data dan berinteraksi dengan database
    templates/main.html: template untuk rendering HTML

3.  settings.py merupakan file konfigurasi utama untuk sebuah proyek django, didalamnya terdapat komponen-komponen yang memiliki perannya masing-masing seperti:
    * INSTALLED_APPS: mendaftarkan semua aplikasi yang aktif di dalam proyek.
    * DATABASES: mengkonfigurasi koneksi ke database (misalnya SQLite dan PostgreSQL).
    * SECRET_KEY: kunci rahasia untuk keamanan kriptografi.
    * DEBUG: mode debugging yang menampilkan informasi error terperinci selama pengembangan.
    * STATIC_URL: mengatur lokasi file statis seperti CSS, JavaScript, dan gambar.

4.  Migrasi merupakan cara django untuk mengelola perubahan pada skema database secara terstruktur dan terotomatisasi. Prosesnya ada dua dan harus dilakukan bertahap dan berurutan, yaitu:
    * makemigrations: membandingkan definisi model di models.py dengan file migrasi yang ada. jika ada perubahan (seperti menambah field atau model baru), django akan membuat file migrasi baru yang berisi instruksi untuk menerapkan perubahan tersebut.
    * migrate: menjalankan file-file migrasi yang belum diterapkan. perintah ini akan menerjemahkan instruksi Python dari file migrasi menjadi perintah SQL yang sesuai dan mengeksekusinya di database, sehingga struktur tabel database sinkron dengan model kita.

5.  Menurut saya pertama karena struktur arsitekturnya jelas, MVT dengan separation of concernnya itu mengajarkan kita praktik pengembangan aplikasi yang baik dan terorganisir, proses debugging juga akan jadi lebih mudah. Secara keamanan, django juga relatif aman karena secara otomatis melindungi dari banyak celah misalnya seperti SQL injection. Terakhir, django sudah dikenal luas sehingga sumber belajarnya sangat banyak, dokumentasinya lengkap, jelas, dan tersebar di internet sehingga memudahkan kita untuk mempelajarinya, terutama bagi pemula.

6.  So far, sudah sangat baik. Saya sendiri personally sangat terbantu dengan adanya tutorial yang ada sejauh ini, tidak ada kendala. Mungkin saran saya bisa dibanyaki lagi pre-cautios agar kita lebih was was ketika mau melakukan suatu perintah untuk kita check dan recheck lagi dulu state yang ada sekarang.