# Cara Berkontribusi
1. Fork repo ini
2. Clone repo ini
3. Commit setiap perubahan
4. Buat Branch Baru (WAJIB) Biar gak tabrakan pushnya
5. Buat pull request ke branch 


# Jangan DIpedulikan Cuma Tugas LOGMAT:
# Table Bagian 3 Project Mini System Voting
| A | B | C | A·B | B·C | A·C | F | Sensor Aktif |     Alarm      |
|---|---|---|-----|-----|-----|---|--------------|----------------|
| 0 | 0 | 0 |  0  |  0  |  0  | 0 |      0       | ❌ Tidak Menyala |
| 0 | 0 | 1 |  0  |  0  |  0  | 0 |      1       | ❌ Tidak Menyala |
| 0 | 1 | 0 |  0  |  0  |  0  | 0 |      1       | ❌ Tidak Menyala |
| 0 | 1 | 1 |  0  |  1  |  0  | 1 |      2       | ✅ Menyala       |
| 1 | 0 | 0 |  0  |  0  |  0  | 0 |      1       | ❌ Tidak Menyala |
| 1 | 0 | 1 |  0  |  0  |  1  | 1 |      2       | ✅ Menyala       |
| 1 | 1 | 0 |  1  |  0  |  0  | 1 |      2       | ✅ Menyala       |
| 1 | 1 | 1 |  1  |  1  |  1  | 1 |      3       | ✅ Menyala       |


## Bonus Challenge: SOP (Sum of Products)
Berdasarkan tabel kebenaran, output F = 1 pada minterm berikut:
- **m₃** (011): A=0, B=1, C=1 → A'BC
- **m₅** (101): A=1, B=0, C=1 → AB'C
- **m₆** (110): A=1, B=1, C=0 → ABC'
- **m₇** (111): A=1, B=1, C=1 → ABC

**Notasi Sum of Products:**
F = Σm(3, 5, 6, 7)

**Bentuk SOP :**
F = A'BC + AB'C + ABC' + ABC
