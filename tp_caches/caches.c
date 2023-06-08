#include <stdio.h>
#include <stdlib.h>
#include <time.h>


#define RAM_SIZE 1024
#define CACHE_SIZE 128
#define WORD_SIZE 4
#define CACHE_ACCESS_TIME 1
#define RAM_ACCESS_TIME 10
#define NB_LINES_PER_SET 2

// Type énuméré pour représenter les différents types de caches.
typedef enum {DIRECT_MAPPING, FULLY_ASSOCIATIVE, SET_ASSOCIATIVE} cache_type;

// Structure pour représenter une ligne de cache.
typedef struct {
    int tag; // champ pour stocker le tag de la ligne
    int valid; // champ pour indiquer si la ligne est valide ou non
    int data[WORD_SIZE]; // champ pour stocker les données de la ligne
} cache_line;

// Structure pour représenter le cache.
typedef struct {
    cache_line *lines; // tableau de lignes de cache
    int nb_lines; // nombre de lignes dans le cache
    int nb_sets; // nombre d'ensembles dans le cache (pour le cache associatif par ensemble)
} cache;

// Fonction pour initialiser le cache.
void init_cache(cache *c, cache_type type) {
    // Calcul du nombre de lignes dans le cache.
    c->nb_lines = CACHE_SIZE / (WORD_SIZE * sizeof(int));
    
    // Si le type de cache est associatif par ensemble, on calcule également le nombre d'ensembles.
    if (type == SET_ASSOCIATIVE) {
        c->nb_sets = c->nb_lines / NB_LINES_PER_SET;
    } else {
        c->nb_sets = 0;
    }
    
    // Allocation de mémoire pour les lignes de cache.
    c->lines = malloc(c->nb_lines * sizeof(cache_line));
    
    // Initialisation des champs `tag`, `valid` et `data` pour chaque ligne de cache.
    for (int i = 0; i < c->nb_lines; i++) {
        c->lines[i].tag = -1;
        c->lines[i].valid = 0;
        for (int j = 0; j < WORD_SIZE; j++) {
            c->lines[i].data[j] = 0;
        }
    }
}

// Fonction pour libérer la mémoire allouée pour les lignes de cache.
void free_cache(cache *c) {
    free(c->lines);
}

// Fonction pour simuler l'accès au cache pour une adresse mémoire donnée.
int access_cache(cache *c, cache_type type, int address) {
    // Calcul de l'index du mot dans la RAM à partir de l'adresse mémoire.
    int word_index = address / WORD_SIZE;
    
    int line_index; // variable pour stocker l'index de ligne dans le cache
    int tag; // variable pour stocker la valeur du tag
    
    if (type == DIRECT_MAPPING) {
        // Pour un cache direct mapping, on calcule l'index de ligne et la valeur du tag à partir
        // de l'index du mot dans la RAM.
        line_index = word_index % c->nb_lines;
        tag = word_index / c->nb_lines;
        
        // On vérifie si la ligne correspondante dans le cache est valide et si son tag correspond
        // au tag calculé.
        // avant de renvoyer 0.
        if (c->lines[line_index].valid && c->lines[line_index].tag == tag) {
            return 1;
        } else {
            c->lines[line_index].valid = 1;
            c->lines[line_index].tag = tag;
            return 0;
        }
    } else if (type == FULLY_ASSOCIATIVE) {
        // Pour un cache fully associative, on parcourt toutes les lignes du cache pour vérifier si
        // l'une d'elles est valide et si son tag correspond à l'index du mot dans la RAM.
        // de renvoyer 0.
        for (line_index = 0; line_index < c->nb_lines; line_index++) {
            if (c->lines[line_index].valid && c->lines[line_index].tag == word_index) {
                return 1;
            }
        }
        line_index = rand() % c->nb_lines;
        c->lines[line_index].valid = 1;
        c->lines[line_index].tag = word_index;
        return 0;
    } else if (type == SET_ASSOCIATIVE) {
        // Pour un cache associatif par ensemble, on calcule l'index de l'ensemble et la valeur du tag
        // à partir de l'index du mot dans la RAM.
        int set_index = word_index % c->nb_sets;
        tag = word_index / c->nb_sets;
        
        // On parcourt ensuite les lignes de l'ensemble correspondant pour vérifier si l'une d'elles
        // est valide et si son tag correspond au tag calculé.
        for (int i = 0; i < NB_LINES_PER_SET; i++) {
            line_index = set_index * NB_LINES_PER_SET + i;
            if (c->lines[line_index].valid && c->lines[line_index].tag == tag) {
                return 1;
            }
        }
        line_index = set_index * NB_LINES_PER_SET + rand() % NB_LINES_PER_SET;
        c->lines[line_index].valid = 1;
        c->lines[line_index].tag = tag;
        return 0;
    }
}

// Fonction pour générer un fichier d'entrée contenant des adresses mémoires aléatoires.
void gen_input_file(int nb_words_in_ram) {
    FILE *f = fopen("input.txt", "w");
    for (int i = 0; i < 10000; i++) {
        fprintf(f, "%d\n", rand() % nb_words_in_ram);
    }
    fclose(f);
}

int main() {
    srand(time(NULL));
    
    cache_type type = SET_ASSOCIATIVE; // choix du type de cache ici
    cache c;
    
    init_cache(&c, type); // initialisation du cache
    
    gen_input_file(RAM_SIZE / WORD_SIZE); // génération du fichier d'entrée
    
    FILE *f = fopen("input.txt", "r"); // ouverture du fichier d'entrée
    
    int address; // variable pour stocker les adresses mémoires lues dans le fichier d'entrée
    int hits = 0; // compteur pour le nombre de succès (hits)
    int accesses = 0; // compteur pour le nombre d'accès au cache
    
    // Lecture des adresses mémoires une par une dans le fichier d'entrée.
    while (fscanf(f, "%d", &address) == 1) {
        accesses++; // incrémentation du compteur d'accès au cache
        hits += access_cache(&c, type, address); // appel à la fonction access_cache pour simuler l'accès au cache
    }
    
    fclose(f); // fermeture du fichier d'entrée
    

    // Calcul et affichage des résultats de la simulation.
    printf("Taux de succès: %f\n", (double)hits / accesses);
    printf("Temps global d’accès: %d\n", hits * CACHE_ACCESS_TIME + (accesses - hits) * RAM_ACCESS_TIME);
    printf("Temps moyen d’accès à une donnée: %f\n", (double)(hits * CACHE_ACCESS_TIME + (accesses - hits) * RAM_ACCESS_TIME) / accesses);
    printf("Speedup: %f\n", (double)(accesses * RAM_ACCESS_TIME) / (hits * CACHE_ACCESS_TIME + (accesses - hits) * RAM_ACCESS_TIME));
    
    free_cache(&c); // libération de la mémoire allouée pour les lignes de cache
    
    return 0;
}
    