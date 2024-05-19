import pygame
import random
import os
from serangan import Crosshair, group_serangan
from dukun import Dukun1,Dukun2,Dukun3
from menu import Menu
from button import Button
from pendopo import Pendopo
from demit import Demit


class Game:
    def __init__(self, width, height, title):
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.TITLE = title

        # Inisialisasi Pygame
        pygame.init()

        # Membuat layar
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption(self.TITLE)
        self.clock = pygame.time.Clock()
        self.FPS = 60

        # Membuat variabel yang diperlukan untuk permainan
        self.level = 1
        self.high_score = 0
        self.level_difficulty = 0
        self.target_difficulty = 1000
        self.DIFFICULTY_MULTIPLIER = 1.1
        self.game_over = False
        self.next_level = False
        self.MAX_ENEMIES = 10
        self.ENEMY_TIME = 1000
        self.last_enemy = pygame.time.get_ticks()
        self.enemies_alive = 0

        # Memuat file high_score.txt
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read())
            file.close()
        
        # Mendefinisikan warna
        self.WHITE = (255, 255, 255)

        # Memuat semua assets
        self.load_assets()
    
    def load_assets(self):
        # Assets untuk bagian font
        self.font_file = ("assets/menu/font.ttf")  
        self.font = pygame.font.Font(self.font_file, 15)
        self.font_30 = pygame.font.Font(self.font_file, 30)

        # Assets untuk bagian menu
        self.background_img = pygame.image.load("assets/menu/bg_menu.png") 
        self.button_img = pygame.image.load("assets/menu/button.png")

        # Assets untuk bagian sound
        self.sound_play = pygame.mixer.Sound("assets/sound/play.mp3")

        # Assets untuk bagian pendopo
        self.pendopo_img_100 = pygame.image.load("assets/castle/Castle_100.png").convert_alpha()
        self.pendopo_img_50 = pygame.image.load('assets/castle/Castle_50.png').convert_alpha()
        self.pendopo_img_25 = pygame.image.load('assets/castle/Castle_25.png').convert_alpha()
        self.bg_basic = pygame.image.load('assets/castle/Latar_belakang.png').convert_alpha()
        self.bg = pygame.transform.scale(self.bg_basic, (900,650))

        # Assets untuk bagian dukun
        self.dukun1_img = pygame.image.load("assets/dukun/dukun_1.png").convert_alpha()
        self.dukun2_img = pygame.image.load("assets/dukun/dukun_2.png").convert_alpha()
        self.dukun3_img = pygame.image.load("assets/dukun/dukun_3.png").convert_alpha()

        # Assets untuk bagian button
        self.perbaiki_img = pygame.image.load("assets/repair.png").convert_alpha()
        self.pertahanan_img = pygame.image.load("assets/armour.png").convert_alpha()

        # Assets untuk bagian demit
        self.animasi_demit = []
        self.tipe_demit = ["banaspati", "suster", "kuntilanak",  "butoijo"]
        self.darah_demit = [75, 100, 125, 150]
        self.tipe_animasi = ["jalan", "serang", "mati"]
        for demit in self.tipe_demit:
            animasi_list = []
            for animasi in self.tipe_animasi:
                temp_list = []
                num_of_frames = 6
                for i in range(num_of_frames):
                    img = pygame.image.load(f"assets/demit/{demit}/{animasi}/{i}.png").convert_alpha()
                    temp_list.append(img)
                animasi_list.append(temp_list)
            self.animasi_demit.append(animasi_list)
    
    def buat_objek(self):
        self.menu = Menu(width=900, height=650, bg_img=self.background_img, btn_img=self.button_img, font_path=self.font_file)
        self.pendopo = Pendopo(image100=self.pendopo_img_100, image50=self.pendopo_img_50, image25=self.pendopo_img_25,
                               bg=self.bg, x=900-250, y=650-300, scale=0.2)
        self.crosshair = Crosshair(0.045)
        self.perbaiki_btn = Button(x=self.SCREEN_WIDTH - 195, y=10, image=self.perbaiki_img, scale=0.5)
        self.pertahan_btn = Button(x=self.SCREEN_WIDTH - 80, y=10, image=self.pertahanan_img, scale=1.2)
        self.dukun_1 = Dukun1(gambar=self.dukun1_img, lebar=410, tinggi=210, x=710, y=400)
        self.dukun_2 = Dukun2(gambar=self.dukun2_img, lebar=600, tinggi=250, x=710, y=400)
        self.dukun_3 = Dukun3(gambar=self.dukun3_img, lebar=500, tinggi=250, x=705, y=400)
        self.demit_group = pygame.sprite.Group()
    
    def gambar_teks(self, text, font, warna, x, y):
        img = font.render(text, True, warna)
        self.screen.blit(img, (x, y))
    
    def show_info(self):
        self.gambar_teks("Uang: " + str(self.pendopo.get_uang()), self.font, self.WHITE, 10, 10)
        self.gambar_teks("Skor: " + str(self.pendopo.get_skor()), self.font, self.WHITE, 180, 10)
        self.gambar_teks("Skor Tertinggi: " + str(self.high_score), self.font, self.WHITE, 180, 30)
        self.gambar_teks("Level: " + str(self.level), self.font, self.WHITE, 530, 10)
        self.gambar_teks("Darah: " + str(self.pendopo.get_kesehatan()) + " / " + str(self.pendopo.get_maks_kesehatan()), self.font, self.WHITE, 
                         self.SCREEN_WIDTH - 300, self.SCREEN_HEIGHT - 50)
        self.gambar_teks('1000', self.font, self.WHITE, self.SCREEN_WIDTH - 195, 70)
        self.gambar_teks('500', self.font, self.WHITE, self.SCREEN_WIDTH - 80, 70)
    
    def mulai_game(self):
        self.buat_objek() # Memanggil method, untuk membuat semua objek

        # Memanggil method tampil menu yang kemudian nilai disimpan di variabel pilihan
        pilihan = self.menu.tampil_menu()
        
        run = True
        while run:
            self.clock.tick(self.FPS)
            pygame.display.update()
            if self.game_over == False:
                # membuat pendopo & crosshair
                self.pendopo.render()
                self.crosshair.draw(self.screen)

                self.sound_play.play() # Play musik
                # cek pilihan untuk memanggil method sesuai dukun yg dipilih
                if pilihan == 1:
                    self.dukun_1.display(self.screen)
                    self.dukun_1.shoot(self.screen)
                elif pilihan == 2:
                    self.dukun_2.display(self.screen)
                    self.dukun_2.shoot(self.screen)
                else:
                    self.dukun_3.display(self.screen)
                    self.dukun_3.shoot(self.screen)
                
                # membuat sihir
                group_serangan.update()
                group_serangan.draw(self.screen)

                # membuat demit
                self.demit_group.update(self.screen, self.pendopo, group_serangan)

                # menampilkan info
                self.show_info()

                # membuat tombol perbaiki dan pertahanan
                if self.perbaiki_btn.draw(self.screen):
                    self.pendopo.perbaiki()
                if self.pertahan_btn.draw(self.screen):
                    self.pendopo.pertahanan()
                
                # cek apabila jumlah maksimal demit sudah tercapai
                if self.level_difficulty < self.target_difficulty:
                    if pygame.time.get_ticks() - self.last_enemy > self.ENEMY_TIME:
                        # Membuat demit
                        e = random.randint(0, len(self.tipe_demit)-1)
                        self.demit = Demit(darah=self.darah_demit[e], animation_list=self.animasi_demit[e], x=-100, y=490, speed=1)
                        self.demit_group.add(self.demit)
                        # reset enemy timer
                        self.last_enemy = pygame.time.get_ticks()
                        # menaikkan level difficulty sesuai darah demit
                        self.level_difficulty += self.darah_demit[0]

                # cek apabila semua demit sudah dipanggil
                if self.level_difficulty >= self.target_difficulty:
                    # cek berapa yang masih hidup
                    self.enemies_alive = 0
                    for e in self.demit_group:
                        if e.alive == True:
                            self.enemies_alive += 1
                    # apabila sudah mati semua, maka level selesai
                    if self.enemies_alive == 0 and self.next_level == False:
                        self.next_level = True  
                        self.level_reset_time = pygame.time.get_ticks()    

                # Lanjut ke level selanjutnya
                if self.next_level == True:
                    self.gambar_teks(text="LEVEL COMPLETE", font=self.font_30, warna=self.WHITE, x=255, y=170)
                    # update high score
                    if self.pendopo.get_skor() > self.high_score:
                        self.high_score = self.pendopo.get_skor()
                        with open("high_score.txt", 'w') as file:
                            file.write(str(self.high_score))
                        file.close()   
                    if pygame.time.get_ticks() - self.level_reset_time > 1500:
                        self.next_level = False
                        self.level += 1
                        self.last_enemy = pygame.time.get_ticks()
                        self.target_difficulty *= self.DIFFICULTY_MULTIPLIER
                        self.level_difficulty = 0
                        self.demit_group.empty()
                
                # cek apabila game over
                if self.pendopo.get_kesehatan() <= 0:
                    self.game_over = True
            
            else:
                self.sound_play.stop()
                self.gambar_teks(text="GAME OVER!", font=self.font, warna=self.WHITE, x=350, y=275)
                self.gambar_teks(text="PRESS 'P' TO PLAY AGAIN",font=self.font, warna=self.WHITE, x=250, y=335)
                pygame.mouse.set_visible(True)
                key = pygame.key.get_pressed()
                if key[pygame.K_p]:
                    # reset semua variabel permainan
                    self.game_over = False
                    self.level = 1
                    self.target_difficulty = 1000
                    self.level_difficulty = 0
                    self.last_enemy = pygame.time.get_ticks()
                    self.demit_group.empty()
                    self.pendopo.set_skor(0)
                    self.pendopo.set_kesehatan(1000)
                    self.pendopo.set_maks_kesehatan(self.pendopo.get_kesehatan())
                    self.pendopo.set_uang(0)
                    pygame.mouse.set_visible(False)
        
            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        
        # Update display window
        pygame.display.update()


if __name__ == "__main__":
    game = Game(width=900, height=650, title="DVD")
    game.mulai_game()