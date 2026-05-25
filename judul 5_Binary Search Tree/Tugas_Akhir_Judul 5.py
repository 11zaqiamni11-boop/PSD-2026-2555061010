class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BSTDasar:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)
        return root

    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def search_node(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        if key < root.key:
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)

    def search(self, key):
        return self.search_node(self.root, key)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.key, end=" ")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(root.key, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.key, end=" ")

    def find_min(self, root):
        if root is None:
            return -1
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def find_max(self, root):
        if root is None:
            return -1
        current = root
        while current.right is not None:
            current = current.right
        return current.key

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def sum_nodes(self, root):
        if root is None:
            return 0
        return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right)

def main():
    sitoserba = BSTDasar()
    pilih = 0
    
    while pilih != 4:
        print("\n=== SiToserba: Manajemen Stok ===")
        print("1. Tambah Kode Barang")
        print("2. Cari Kode Barang")
        print("3. Tampilkan Info Stok")
        print("4. Keluar")
        
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
            continue

        if pilih == 1:
            try:
                x = int(input("Masukkan kode barang (angka): "))
                sitoserba.insert(x)
                print(f"Kode barang {x} berhasil dimasukkan ke sistem.")
            except ValueError:
                print("Input tidak valid! Masukkan angka.")
                
        elif pilih == 2:
            try:
                x = int(input("Cari kode barang: "))
                if sitoserba.search(x):
                    print("Status: Barang Ditemukan di Toko!")
                else:
                    print("Status: Barang Tidak Ada.")
            except ValueError:
                print("Input tidak valid! Masukkan angka.")
                
        elif pilih == 3:
            print(f"Kode barang terkecil: {sitoserba.find_min(sitoserba.root)}")
            print(f"Kode barang terbesar: {sitoserba.find_max(sitoserba.root)}")
            print(f"Total variasi barang di sistem: {sitoserba.count_nodes(sitoserba.root)}")
            
        elif pilih == 4:
            print("Program SiToserba selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
