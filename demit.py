import pygame

class Demit(pygame.sprite.Sprite):
    def __init__(self, darah, animation_list, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.__kecepatan = speed
        self.__darah = darah
        self.last_attack = pygame.time.get_ticks()
        self.attack_cooldown = 1000
        self.animation_list = animation_list
        self.frame_index = 0
        self.action = 0 # 0:jalan, 1:serang, 2:mati
        self.update_time = pygame.time.get_ticks()

        # select starting image
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0, 0, 25, 70)
        self.rect.center = (x, y)
    
    # Method getter untuk mendapatkan info darah
    def get_darah(self):
        return self.__darah
    
    # Method getter untuk mendapatkan info kecepatan
    def get_kecepatan(self):
        return self.__kecepatan
    
    # Method setter untuk mengeset nilai darah yang berkurang
    def set_kurang_darah(self, damage):
        self.__darah -= damage
    
    def update(self, surface, target, group_serangan):
        if self.alive:
            # periksa sihir mengenai demit
            if pygame.sprite.spritecollide(self, group_serangan, True):
                # mengurangi darah demit
                self.set_kurang_darah(25)

            # periksa jika demit mecapai pendopo
            if self.rect.right > target.rect.left:
                self.update_action(1)

            # demit bergerak
            if self.action == 0:
                # perbarui posisi
                self.rect.x += self.get_kecepatan()

            # demit menyerang
            if self.action == 1:
                # periksa apakah waktu sudah cukup sejak serangan terakhir
                if pygame.time.get_ticks() - self.last_attack > self.attack_cooldown:
                    target.set_kurang_kesehatan(25)
                    if target.get_kesehatan() < 0:
                        target.set_kesehatan(0)
                    self.last_attack = pygame.time.get_ticks()

            # periksa jika darah demit sudah mencapai nol
            if self.get_darah() <= 0:
                target.set_tambah_uang(100)
                target.set_tambah_skor(100)
                self.update_action(2)
                self.alive = False

        self.update_animation()

        # membuat gambar pada layar
        surface.blit(self.image, (self.rect.x-15, self.rect.y-15))
    
    def update_animation(self):
        # mengset durasi animasi
        ANIMATION_COOLDOWN = 350
        # update gambar berdasarkan aksi saat ini
        self.image = self.animation_list[self.action][self.frame_index]
        # perikasa apakah waktu sudah cukup dari update terakhir
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # jika animasi sudah habis, kembali ke awal
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 2:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # periksa apakah aksi terbaru berbeda dari aksi sebelumnya
        if new_action != self.action:
            self.action = new_action
            # update animasi
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()