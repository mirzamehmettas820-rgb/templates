from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.core.window import Window

class SohbetBotu(App):
    def build(self):
        self.title = "Mirza AI"
        Window.clearcolor = (0.1, 0.1, 0.1, 1) # Koyu arka plan

        # Ana Düzen
        ana_duzen = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Sohbet Geçmişi Ekranı
        self.scroll = ScrollView(size_hint=(1, 0.8))
        self.sohbet_kutusu = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.sohbet_kutusu.bind(minimum_height=self.sohbet_kutusu.setter('height'))
        self.scroll.add_widget(self.sohbet_kutusu)
        
        # Karşılama Mesajı
        self.mesaj_ekle("Bot: Merhaba! Ben senin yapay zekanım. Nasılsın?", (0.2, 0.6, 1, 1))

        # Alt Kısım (Yazma Alanı ve Buton)
        alt_duzen = BoxLayout(size_hint=(1, 0.2), spacing=10)
        
        self.girdi = TextInput(text='', multiline=False, hint_text="Bir şeyler yaz...", font_size=18)
        self.girdi.bind(on_text_validate=self.mesaj_gonder)
        
        gonder_btn = Button(text="Gönder", size_hint=(0.3, 1), background_color=(0.2, 0.8, 0.2, 1))
        gonder_btn.bind(on_press=self.mesaj_gonder)

        alt_duzen.add_widget(self.girdi)
        alt_duzen.add_widget(gonder_btn)

        ana_duzen.add_widget(self.scroll)
        ana_duzen.add_widget(alt_duzen)

        return ana_duzen

    def mesaj_gonder(self, instance):
        kullanici_mesaji = self.girdi.text.strip()
        if not kullanici_mesaji:
            return

        # Kullanıcı mesajını ekrana yaz
        self.mesaj_ekle(f"Sen: {kullanici_mesaji}", (0.9, 0.9, 0.9, 1))
        self.girdi.text = ''

        # Basit Yapay Zeka Mantığı
        cevap = self.yapay_zeka_dusun(kullanici_mesaji.lower())
        
        # Botun cevabını ekrana yaz
        self.mesaj_ekle(f"Bot: {cevap}", (0.2, 0.6, 1, 1))

    def yapay_zeka_dusun(self, mesaj):
        if "merhaba" in mesaj or "selam" in mesaj:
            return "Merhaba! Sana nasıl yardımcı olabilirim?"
        elif "nasılsın" in mesaj:
            return "Ben bir yazılımım, her zaman harikayım! Sen nasılsın?"
        elif "adın ne" in mesaj or "kimsin" in mesaj:
            return "Ben Mirza AI. Senin tarafından Kivy ile kodlandım."
        elif "oyun" in mesaj:
            return "Oyun yapmayı çok severim! CS:GO tarzı oyunlar favorim."
        elif "sağol" in mesaj or "teşekkür" in mesaj:
            return "Rica ederim, ne demek!"
        elif "görüşürüz" in mesaj or "bye" in mesaj:
            return "Görüşmek üzere, kendine iyi bak!"
        else:
            return "Bunu henüz öğrenmedim ama yakında öğreneceğim! Bana başka bir şey sor."

    def mesaj_ekle(self, metin, renk):
        lbl = Label(text=metin, size_hint_y=None, text_size=(Window.width - 40, None), halign='left', valign='middle', color=renk)
        lbl.bind(texture_size=lbl.setter('size'))
        self.sohbet_kutusu.add_widget(lbl)
        # Yeni mesaj geldiğinde en alta kaydır
        self.scroll.scroll_y = 0

if __name__ == '__main__':
    SohbetBotu().run()
