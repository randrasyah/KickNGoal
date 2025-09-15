# KickNGoal - Football Shop

**Nama:** Fairuz Akhtar Randrasyah
**NPM:** 2406403955
**Kelas:** PBP D

## Tugas Individu

**Link PWS:** https://fairuz-akhtar-kickngoal.pbp.cs.ui.ac.id/
---

## Tugas 2

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

---

## Tugas 3

**1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

    Data Delivery sangat penting agar app yang berbeda dapat saling berkomunikasi. Data delivery memungkinkan pertukaran informasi antara klien (ex: browser) dan server. Ketika klien membutuhkan sesuatu, server tidak hanya mengirimkan tampilan, tetapi juga mengirimkan data mentah dalam format terstruktur seperti XML atau JSON.  Contohnya, antara backend dengan aplikasi mobile, atau untuk menyediakan API bagi third party.

**2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

    Menurut saya pribadi, tampilan dari data XML lebih enak untuk dipandang karena lebih terstruktur dengan kuat. Namun, secara keseluruhan, JSON mungkin lebih baik dan lebih populer karena JSON memiliki sintaks yang ringan dan ringkas sehingga ukuran datanya lebih kecil dan transfer data lebih cepat. Selain itu, strukturnya yang sederhana juga memudahkan kita untuk membaca dan menulis kode yang diinginkan dibandingkan XML yang kaku. Struktur data JSON juga secara langsung memetakan struktur data umum yang ada hampir di semua bahasa pemrograman modern.

**3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**

    Method is_valid() pada form Django berfungsi sebagai gerbang validasi utama untuk data yang dikirimkan oleh pengguna. Ketika dipanggil, method ini akan memeriksa apakah data yang masuk sudah sesuai dengan semua aturan yang ditetapkan pada form, contohnya seperti tipe data yang benar, field yang wajib diisi, dan aturan lainnya. Jika semua data valid, method ini mengembalikan True dan memindahkan data yang sudah bersih ke dalam atribut form.cleaned_data agar aman untuk digunakan. Jika tidak, ia mengembalikan False dan menyimpan pesan eror untuk ditampilkan kepada pengguna. Kita butuh menggunakan is_valid() mencegah input berbahaya, dan memberikan validasi input yang benar kepada pengguna.

**4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

    Kita membutuhkan csrf_token untuk mencegah serangan Cross-Site Request Forgery (CSRF). Serangan CSRF terjadi ketika seorang penyerang memanfaatkan vulnerability dengan menipu pengguna yang sedang login untuk tanpa sadar mengirimkan permintaan berbahaya ke aplikasi web kita (ex: mengubah password atau menghapus data), hal ini lah yang dapat terjadi ketika kita tidak menambahkan csrf_token pada kode kita. Token ini bekerja dengan cara menanamkan sebuah secret value yang unik di dalam form. Saat form dikirim, Django akan memverifikasi apakah token tersebut cocok dengan yang ada di sesi pengguna. Karena situs penyerang tidak dapat mengetahui nilai token ini, setiap permintaan palsu dari mereka akan otomatis ditolak oleh Django.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)**

    - Saya buat direktori baru templates di direktori utama, lalu saya buat file base.html didalamnya untuk menjadi template dasar dari template-template saya lainnya (template lain tinggal extend base.html)
    - Saya tambahkan 'DIRS': [BASE_DIR / 'templates'] di templates pada setting.py agar base.html terbaca
    - Saya extend base.html di main.html saya dan memasukkan kode sebelumnya kedalam block content
    - Saya membuat form dengan membuat file forms.py di main dan mengisi fields-fields yang perlu di input pengguna (fieldsnya berupa atribut dari objek Product di models)
    - Saya membuat fungsi create_product dan show_product pada views lalu menambahkan path url dari fungsi yang telah dibuat
    - Saya update template pada main agar menampilkan data dari product yang ada dan menambahkan button untuk add product
    - Saya membuat 2 file html baru yaitu create_product dan product_detail untuk halaman form input dan read more (pada create product saya tidak lupa untuk menambahkan csrf token untuk menghindari serangan CSRF)
    - Saya menambahkan link deployment saya pada CSRF_TRUSTED_ORIGIN di settings pada direktori project
    - Saya menambahkan fungsi show_xml, show_json, show_xml_by_id, show_json_by_id di views yang mengembalikan HttpResponse untuk menyusun respons yang ingin dikembalikan user kepada user (pada show by id, saya menambahkan try and except untuk memvalidasi jika suatu id tidak ditemukan)
    - Saya import fungsi-fungsi yang saya telah buat sebelumnya ke urls di main lalu menambahkan path URL ke dalam urlpatterns
    - Saya menjalankan server untuk membuka 4 link dan menscreenshot tiap hasil akses URL di POSTMAN

**6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?**

    Aman ajaaaa..

**Screenshot POSTMAN:**
![alt text](ss_xml.png)
![alt text](ss_xml_by_id.png)
![alt text](ss_json.png)
![alt text](ss_json_by_id.png)