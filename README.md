# 📊 Analisis Data E-Commerce Tugas Paul David D

Dashboard ini digunakan untuk menganalisis data e-commerce dengan fokus pada:
- **Tren Pembelian:** Menampilkan kota dengan total nilai pembelian tertinggi dan terendah.
- **Analisis Pembayaran:** Menampilkan metode pembayaran dominan serta relevansinya dengan nilai transaksi.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://submissionpauldavid.streamlit.app/)

---

## 🚀 Fitur

1. **Analisis Kota**  
   - Menampilkan Top 10 kota dengan total nilai pembelian tertinggi.  
   - Menampilkan Top 10 kota dengan total nilai pembelian terendah.

2. **Analisis Pembayaran**  
   - Distribusi frekuensi metode pembayaran.  
   - Rata-rata dan total nilai transaksi per metode pembayaran.

---

## 📋 Prasyarat

- **Python 3.7+**
- **Git**
- **Library:**  
  - pandas  
  - matplotlib  
  - seaborn  
  - streamlit

---

## 🛠️ Instalasi & Menjalankan Dashboard

Ikuti langkah-langkah berikut secara berurutan:
**Clone Repository, Setup Virtual Environment, Install Dependencies, dan Menjalankan Dashboard:**

   - **Clone Repository:**  
     Buka terminal dan jalankan:
     ```bash
     git clone https://github.com/PaulD4vd/analisis-data-submission.git
     cd analisis-data-submission
     ```

   - **Setup Virtual Environment:**  
     Buat virtual environment dengan perintah:
     ```bash
     python -m venv venv
     ```  
     Aktifkan virtual environment:
     - **Windows:**
       ```bash
       venv\Scripts\activate
       ```
     - **macOS/Linux:**
       ```bash
       source venv/bin/activate
       ```

   - **Install Dependencies dan Menjalankan Dashboard:**  
     Instal semua library yang dibutuhkan:
     ```bash
     pip install -r requirements.txt
     ```  
     Setelah instalasi selesai, jalankan dashboard dengan perintah:
     ```bash
     streamlit run submission/dashboard/dashboard.py
     ```

---

Dokumentasi ini mencakup seluruh langkah dari clone repository, setup virtual environment, instalasi dependencies, hingga menjalankan dashboard. Jika ada pertanyaan atau perbaikan lebih lanjut, silakan hubungi pembuat.
