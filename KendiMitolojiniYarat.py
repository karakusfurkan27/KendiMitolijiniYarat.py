import random
import tkinter as tk
from tkinter import messagebox

# Karakter sınıfı
class Character:
    def __init__(self, name, role, powers, health=100, alignment="Neutral", level=1, backstory=""):
        self.name = name
        self.role = role
        self.powers = powers
        self.health = health
        self.alignment = alignment  # "İyi", "Kötü", "Neutral"
        self.level = level
        self.backstory = backstory

    def __str__(self):
        return f"{self.name}, {self.role} rolünde, güçler: {', '.join(self.powers)}\nArka Plan: {self.backstory}"

    def attack(self, other):
        power = random.choice(self.powers)
        damage = random.randint(10, 30) * self.level
        other.health -= damage
        return f"{self.name} {other.name}'a {power} kullanarak {damage} hasar verdi!"

    def heal(self):
        healing = random.randint(10, 20) * self.level
        self.health += healing
        return f"{self.name} {healing} sağlık kazandı!"

    def level_up(self):
        self.level += 1
        return f"{self.name} seviyesini arttırarak {self.level}. seviyeye ulaştı!"

    def gain_power(self, new_power):
        self.powers.append(new_power)
        return f"{self.name} yeni güç kazandı: {new_power}"

    def status(self):
        return f"{self.name} - Sağlık: {self.health}, Seviye: {self.level}, Yönelim: {self.alignment}"


# Türk Hükümdarları ve Kahramanları
alparslan = Character("Alparslan", "Büyük Selçuklu Hükümdarı", ["Malazgirt Zaferi", "Ordu Komutanlığı", "Stratejik Zeka"], backstory="Selçuklu'nun en büyük zaferini kazanan hükümdar, Bizans İmparatoru IV. Romanos Diogenes'i yenerek Anadolu'nun kapılarını Türklere açmıştır.")
fatih_sultan_mehmet = Character("Fatih Sultan Mehmet", "Osmanlı Hükümdarı", ["İstanbul'u Fetih", "Savaş Stratejisi", "Yüce Liderlik"], backstory="Osmanlı Devleti'nin 7. padişahı olan Fatih, İstanbul'u fethederek Batı ile Doğu arasındaki kapıları kapatmıştır.")
battal_gazi = Character("Battal Gazi", "Türk Kahramanı", ["Savaşçılık", "Zorlu Savaşlar", "Zafer"], backstory="Battal Gazi, İslam ordusunda büyük kahramanlıklar sergileyerek halk arasında efsaneleşmiştir.")
köroğlu = Character("Köroğlu", "Türk Halk Kahramanı", ["Okçuluk", "At Binme", "Zalimlere Karşı Direniş"], backstory="Türk halkının en büyük halk kahramanlarından biri olan Köroğlu, zalimlere karşı verdiği mücadele ile bilinir.")
mustafa_kemal_atatürk = Character("Mustafa Kemal Atatürk", "Türkiye Cumhuriyeti'nin Kurucusu", 
                                   ["Cumhuriyet İlanı", "Bağımsızlık Savaşı", "Devlet Reformları", "Devrimci Zeka"], 
                                   backstory="Türk milletinin bağımsızlık mücadelesinin simgesi, Türkiye Cumhuriyeti'nin kurucusu ve ilk Cumhurbaşkanıdır.")

# Mitoloji sınıfı
class Mythology:
    def __init__(self, name):
        self.name = name
        self.characters = []
        self.locations = []
        self.stories = []

    def add_character(self, character):
        self.characters.append(character)

    def add_location(self, location):
        self.locations.append(location)

    def add_story(self, story):
        self.stories.append(story)

    def random_story(self):
        return random.choice(self.stories)

    def random_event(self):
        event = random.choice(["Savaş", "İttifak", "İhanet", "Keşif"])
        return event

    def story_summary(self):
        return f"Mitoloji: {self.name}\nKarakterler:\n" + "\n".join(str(c) for c in self.characters) + "\nYerler:\n" + ", ".join(self.locations)


# Mitolojiye karakterleri ve yerleri ekleme
mythology = Mythology("Türk Mitolojisi")
mythology.add_character(alparslan)
mythology.add_character(fatih_sultan_mehmet)
mythology.add_character(battal_gazi)
mythology.add_character(köroğlu)
mythology.add_character(mustafa_kemal_atatürk)

# Yerler ve Efsaneler
mythology.add_location("Ergenekon")
mythology.add_location("Tengri Dağı")
mythology.add_story("Fatih Sultan Mehmet'in İstanbul'u Fethi")
mythology.add_story("Alparslan'ın Malazgirt Zaferi")
mythology.add_story("Battal Gazi'nin Kahramanlıkları")
mythology.add_story("Mustafa Kemal Atatürk'ün Kurtuluş Savaşı ve Cumhuriyet'i Kuruluşu")

# GUI ile Mitoloji gösterimi
class MythologyApp:
    def __init__(self, root, mythology):
        self.root = root
        self.mythology = mythology
        self.root.title("Türk Mitolojisi Yaratıcı")
        self.root.geometry("600x500")
        self.root.config(bg="#f0f0f0")  # Arka plan rengi

        # Başlık
        self.label = tk.Label(root, text="Türk Mitolojisi Yaratıcısına Hoşgeldiniz!", font=("Helvetica", 16), bg="#f0f0f0")
        self.label.pack(pady=10)

        # Butonlar
        self.story_button = tk.Button(root, text="Rastgele Hikaye Göster", command=self.show_random_story, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.story_button.pack(pady=5)

        self.event_button = tk.Button(root, text="Rastgele Etkinlik Oluştur", command=self.generate_event, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.event_button.pack(pady=5)

        self.interaction_button = tk.Button(root, text="Karakter Etkileşimini Göster", command=self.show_interaction, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.interaction_button.pack(pady=5)

        self.character_button = tk.Button(root, text="Karakter Bilgilerini Göster", command=self.show_character_info, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.character_button.pack(pady=5)

        self.add_character_button = tk.Button(root, text="Yeni Karakter Ekle", command=self.add_new_character, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.add_character_button.pack(pady=5)

    def show_random_story(self):
        story = self.mythology.random_story()
        messagebox.showinfo("Rastgele Hikaye", story)

    def generate_event(self):
        event = self.mythology.random_event()
        messagebox.showinfo("Rastgele Etkinlik", f"Bir rastgele etkinlik meydana geldi: {event}")

    def show_interaction(self):
        # Karakterler arasında etkileşim
        interaction = alparslan.attack(köroğlu)
        messagebox.showinfo("Karakter Etkileşimi", interaction)

    def show_character_info(self):
        # Karakter bilgilerini göster
        character_info = "\n".join([str(c) for c in self.mythology.characters])
        messagebox.showinfo("Karakter Bilgisi", character_info)

    def add_new_character(self):
        # Kullanıcıdan yeni karakter bilgilerini al
        def save_character():
            name = name_entry.get()
            role = role_entry.get()
            powers = powers_entry.get().split(",")
            backstory = backstory_entry.get()
            new_character = Character(name, role, powers, backstory=backstory)
            self.mythology.add_character(new_character)
            messagebox.showinfo("Yeni Karakter", f"{name} adlı karakter başarıyla eklendi!")

        # Yeni karakter için pencere açma
        add_window = tk.Toplevel(self.root)
        add_window.title("Yeni Karakter Ekle")
        add_window.geometry("300x300")

        tk.Label(add_window, text="Karakter Adı:").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack(pady=5)

        tk.Label(add_window, text="Rol:").pack(pady=5)
        role_entry = tk.Entry(add_window)
        role_entry.pack(pady=5)

        tk.Label(add_window, text="Güçler (Virgülle ayırın):").pack(pady=5)
        powers_entry = tk.Entry(add_window)
        powers_entry.pack(pady=5)

        tk.Label(add_window, text="Arka Plan:").pack(pady=5)
        backstory_entry = tk.Entry(add_window)
        backstory_entry.pack(pady=5)

        save_button = tk.Button(add_window, text="Kaydet", command=save_character)
        save_button.pack(pady=10)


# Ana pencereyi başlatma
if __name__ == "__main__":
    root = tk.Tk()
    app = MythologyApp(root, mythology)
    root.mainloop()
