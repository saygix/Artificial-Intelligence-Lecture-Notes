
import random

class OneMaxGA:
    def __init__(self, pop_size, chrom_size, max_iter):
        self.pop_size = pop_size
        self.chrom_size = chrom_size
        self.max_iter = max_iter
        self.population = []
        
    def create_population(self):
        for i in range(self.pop_size):
            chrom = [random.randint(0, 1) for j in range(self.chrom_size)]
            self.population.append(chrom)
        print("uretilen populasyon--->"+str(self.population))
         

    def fitness(self, chrom):
        return sum(chrom)
    
    def selection(self):
        # uygunluk oranlı seçim
        total_fitness = sum(self.fitness(chrom) for chrom in self.population)
        rand_val = random.uniform(0, 1)
        cumulative_prob = 0
        for i in range(len(self.population)):
            chrom = self.population[i]
            chrom_prob = self.fitness(chrom) / total_fitness
            cumulative_prob += chrom_prob
            if cumulative_prob >= rand_val:
                return i
        return len(self.population) - 1  # Yedek olarak son indeksi döndür
    
    def crossover(self, chrom1, chrom2):
        # tek nokta çaprazlama
        crossover_point = random.randint(1, self.chrom_size-1)
        child1 = chrom1[:crossover_point] + chrom2[crossover_point:]
        child2 = chrom2[:crossover_point] + chrom1[crossover_point:]
        print("caprazlama sonucu--->"+str(child1)+str(child2))
        return child1, child2
           
    def mutation(self, chrom):
        # bit çevirme mutasyonu
        mutation_point = random.randint(0, self.chrom_size-1)
        chrom[mutation_point] = 1 - chrom[mutation_point]
        print("mutasyon sonucu--->"+str(chrom))
        return chrom
        
    def create_new_population(self):
        new_population = []
        for i in range(self.pop_size):
            # İki ebeveyn seçin 
            parent1 = self.population[self.selection()]
            parent2 = self.population[self.selection()]         
            # İki ebeveyni çaprazlayarak iki çocuk oluşturun
            child1, child2 = self.crossover(parent1, parent2)          
            # Çocukları mutasyona uğratın
            child1 = self.mutation(child1)
            child2 = self.mutation(child2)         
            # Çocukları yeni popülasyona ekle
            new_population.append(child1)
            new_population.append(child2)
        print("uretilen yeni populasyon--->"+str(new_population))    
        # Popülasyonu güncelle
        self.population = new_population
        
    def run(self):
        # İlk popülasyonu oluştur
        self.create_population()
        # Maksimum iterasyon sayısı kadar evrimi tekrarla
        for i in range(self.max_iter):
            # Yeni popülasyon oluştur
            self.create_new_population()
            # Yeni popülasyonun uygunluğunu hesapla
            fitness_vals = [self.fitness(chrom) for chrom in self.population]
            # Sonlandırma koşulunu kontrol et
            if max(fitness_vals) == self.chrom_size:
                break
        # Bulunan en iyi bireyi döndür
        best_ind = self.population[fitness_vals.index(max(fitness_vals))]
        return best_ind
    
# Algoritmayı test et
pop_size = 2
chrom_size = 5
max_iter = 50

ga = OneMaxGA(pop_size, chrom_size, max_iter)
best_ind = ga.run()

print("En iyi çözüm --->"+str (best_ind) +" Fitness degeri--->"+str(sum(best_ind)))

