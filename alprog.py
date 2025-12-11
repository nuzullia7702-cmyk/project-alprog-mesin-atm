# =========================================
# PROGRAM SIMULASI ATM (CLI)
# =========================================

saldo = 23456895  # saldo awal
riwayat = []     # list penyimpanan transaksi
PIN = "9843"     # PIN default


# -----------------------------------------
# Fungsi Login PIN
# -----------------------------------------
def login():
    print("===== SELAMAT DATANG DI ATM =====")
    for i in range(3):
        pin_input = input("Masukkan PIN: ")

        if pin_input == PIN:
            print("✔ Login berhasil!\n")
            return True
        else:
            print("❌ PIN salah!")

    print("❌ Terlalu banyak percobaan. Kartu diblokir.")
    return False


# -----------------------------------------
# Fungsi Cek Saldo
# -----------------------------------------
def cek_saldo():
    print(f"\nSaldo Anda saat ini: Rp {saldo:,}")
    riwayat.append("Cek Saldo")


# -----------------------------------------
# Fungsi Setor Uang
# -----------------------------------------
def setor():
    global saldo
    print("\n--- Setor Tunai ---")

    try:
        jumlah = int(input("Masukkan jumlah setor: "))
        if jumlah <= 0:
            print("❌ Jumlah harus lebih dari 0!")
            return
    except ValueError:
        print("❌ Input harus angka!")
        return

    saldo += jumlah
    riwayat.append(f"Setor Rp {jumlah:,}")
    print("✔ Setor berhasil!")


# -----------------------------------------
# Fungsi Tarik Uang
# -----------------------------------------
def tarik():
    global saldo
    print("\n--- Tarik Tunai ---")

    try:
        jumlah = int(input("Masukkan jumlah tarik: "))
        if jumlah <= 0:
            print("❌ Jumlah harus lebih dari 0!")
            return
    except ValueError:
        print("❌ Input harus angka!")
        return

    if jumlah > saldo:
        print("❌ Saldo tidak cukup!")
        return

    saldo -= jumlah
    riwayat.append(f"Tarik Rp {jumlah:,}")
    print ("✔ Saldo Cukup")
    print("✔ Penarikan berhasil!")


# -----------------------------------------
# Fungsi Riwayat Transaksi
# -----------------------------------------
def tampilkan_riwayat():
    print("\n--- Riwayat Transaksi ---")
    if len(riwayat) == 0:
        print("Belum ada transaksi.")
        return

    for r in riwayat:
        print("-", r)


# -----------------------------------------
# MENU UTAMA (while True)
# -----------------------------------------
def menu():
    while True:
        print("\n========= MENU ATM =========")
        print("1. Cek Saldo")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Riwayat Transaksi")
        print("5. Keluar")
        print("==============================")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            cek_saldo()
        elif pilihan == "2":
            setor()
        elif pilihan == "3":
            tarik()
        elif pilihan == "4":
            tampilkan_riwayat()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan ATM!")
            break
        else:
            print("❌ Pilihan tidak valid, coba lagi.")


# -----------------------------------------
# Program Utama
# -----------------------------------------
if login():
    menu()
