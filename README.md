# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Selama lebih dari dua dekade, institusi ini telah membangun reputasi yang sangat baik dalam mencetak lulusan berkualitas di berbagai program sarjana, termasuk agronomi, desain, pendidikan, keperawatan, jurnalistik, manajemen, layanan sosial, dan teknologi.

### Permasalahan Bisnis

Meskipun memiliki track record yang baik, Jaya Jaya Institut menghadapi tantangan serius terkait tingkat dropout mahasiswa:

1. Tingginya angka dropout mahasiswa yang berdampak signifikan terhadap:
   - Reputasi institusi sebagai lembaga pendidikan
   - Efektivitas program akademik
   - Keberlanjutan finansial institusi
2. Keterbatasan dalam mendeteksi secara dini mahasiswa yang berisiko dropout
3. Kebutuhan sistem monitoring yang efektif untuk memantau performa akademik mahasiswa
4. Perlunya program bimbingan khusus yang tepat sasaran untuk mahasiswa berisiko

### Cakupan Proyek

1. Analisis data mahasiswa yang mencakup:
   - Informasi demografis dan sosial-ekonomi
   - Latar belakang akademik
   - Performa akademik semester 1 dan 2
2. Pengembangan model machine learning untuk:
   - Memprediksi risiko dropout mahasiswa
   - Mengidentifikasi faktor-faktor yang mempengaruhi keberhasilan akademik
3. Pembuatan dashboard visualisasi untuk monitoring performa mahasiswa
4. Rekomendasi strategi intervensi berdasarkan hasil analisis

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:

```bash
pip install -r requirements.txt
```

## Business Dashboard

Dashboard bisnis telah dibuat untuk memvisualisasikan:

1. Summary Metrics (KPI Cards)
   Tiga kartu utama yang langsung memberikan informasi ringkas:

   - Enrolled Student: 794 mahasiswa yang sedang aktif kuliah.
   - Dropout Student: 1.421 mahasiswa yang putus kuliah.
   - Graduate Students: 2.209 mahasiswa yang telah lulus.

   **🔍 Insight:**

   Total mahasiswa: 4.424, dengan dropout rate sekitar 32.12%, angka yang cukup signifikan dan perlu dianalisis lebih dalam.

2. Funnel Analysis
   Visualisasi funnel menunjukkan transisi status mahasiswa:

   - Tahapan: Total → Enrolled → Dropout / Graduate
   - Terlihat 100% enrolled → 32.12% dropout → 49.93% graduate.

   **🔍 Insight:**

   - Dropout terjadi cukup awal dalam perjalanan akademik.
   - Perlu strategi retensi dan intervensi lebih awal bagi mahasiswa.

3. Unemployment Rate vs Dropout Rate (Scatter Plot)
   Sumbu X: Tingkat pengangguran rata-rata per negara
   Sumbu Y: Dropout rate per negara
   Ukuran bubble: jumlah mahasiswa.

   **🔍 Insight:**

   - Terlihat beberapa negara dengan pengangguran tinggi juga memiliki dropout tinggi.
   - Faktor ekonomi negara asal bisa berpengaruh terhadap kelangsungan studi mahasiswa.

4. Dropout Count over Application Order (Line Chart)
   Visualisasi jumlah dropout dan graduate berdasarkan urutan pilihan program studi (application_order).

   **🔍 Insight:**

   - Mayoritas dropout terjadi pada urutan pertama dan kedua.
   - Hal ini bisa menunjukkan bahwa mahasiswa tidak siap atau salah memilih program studi sejak awal.

5. Distribusi Dropout Berdasarkan Previous Qualification Grade (Bar Chart)
   Visualisasi distribusi mahasiswa berdasarkan nilai akademik sebelumnya (GPA) dan statusnya (Enrolled, Dropout, Graduate).

   **🔍 Insight:**

   - Dropout banyak terjadi di mahasiswa dengan GPA rendah.
   - Diperlukan sistem peringatan dini (early warning system) berdasarkan nilai masuk.

6. Dropout Rate Per Course (Horizontal Stacked Bar)
   Menampilkan total dropout dan total student per kode program studi/course.

   **🔍 Insight:**

   - Program studi tertentu memiliki jumlah dropout jauh lebih tinggi dari rata-rata.
   - Evaluasi kurikulum atau sistem pembelajaran sangat disarankan untuk course dengan dropout dominan.

7. Dropout by Parental Education (Stacked Bar Chart)
   Menampilkan komposisi mahasiswa dropout dan graduate berdasarkan tingkat pendidikan orang tua (parent_qual).

   **🔍 Insight:**

   - Terlihat bahwa mahasiswa dengan orang tua berpendidikan rendah cenderung lebih banyak dropout.
   - Implikasi: perlu pendekatan sosial atau pendampingan ekstra bagi mahasiswa dengan latar belakang keluarga berpendidikan rendah.

---

Dashboard dapat diakses melalui file djatikusuma-dashboard.pdf

---

**Menjalankan Dashboard**:

1. Dashboard proyek dibuat menggunakan `metabase` yang terinstall di `Docker`, untuk menjalankan lakukan perintah berikut:

   ```
   docker pull metabase/metabase:v0.46.4
   ```

2. Jalankan container Metabase yang ada di Docker menggunakan perintah berikut:

   ```
   docker run -p 3000:3000 --name metabase metabase/metabase
   ```

3. Login ke Metabase menggunakan username dan password berikut:
   ```
   username: root@mail.com
   password: root123
   ```

## Menjalankan Sistem Machine Learning

Untuk menjalankan prototype sistem machine learning:

1. Pastikan semua dependencies telah terinstall:

```bash
pip install -r requirements.txt
```

2. Jalankan aplikasi:

```bash
streamlit run app.py
```

Atau dengan akses ke: https://djatikusuma-ds-proyek-akhir.streamlit.app

## Conclusion

Berdasarkan analisis yang telah dilakukan:

1. Model machine learning berhasil mengidentifikasi mahasiswa berisiko dropout dengan akurasi yang baik
2. Faktor-faktor utama yang mempengaruhi keberhasilan akademik telah teridentifikasi
3. Sistem dapat membantu institusi dalam mengambil tindakan preventif lebih awal

### Rekomendasi Action Items

- Implementasi sistem early warning untuk mahasiswa berisiko dropout
- Pengembangan program mentoring khusus berdasarkan faktor risiko individual
- Optimalisasi alokasi sumber daya pendukung akademik berdasarkan prediksi model
- Evaluasi dan penyesuaian kurikulum berdasarkan pola kesulitan akademik yang teridentifikasi
- Peningkatan layanan konseling dan dukungan untuk mahasiswa dengan latar belakang sosial-ekonomi tertentu
