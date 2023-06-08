#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <assert.h>
#include <pthread.h>

typedef struct fonct_arg_s {
	char *tampon;
	unsigned long taille;
    unsigned long res;
} fonct_arg_s;

unsigned long compteur_gc(char *tampon, unsigned long taille) {
    unsigned long i, cptr = 0;

    for (i = 0; i < taille; i++)
        if (tampon[i] == 'G' || tampon[i] == 'C')
            cptr++;

    return cptr;
}

void *compteur_wrapper(void *arg) {
	fonct_arg_s *p_arg = arg ;
	p_arg->res = compteur_gc(p_arg->tampon, p_arg->taille);
	
	return NULL;
}

int main(int argc, char *argv[]) {
    struct stat st;
    int fd;
    char *tampon;
    int lus;
    unsigned long cptr = 0;
    off_t taille = 0;
    struct timespec debut, fin;

    assert(argc > 2);

    /* Quelle taille ? */
    assert(stat(argv[1], &st) != -1);
    tampon = malloc(st.st_size);
    assert(tampon != NULL);

    /* Chargement en mémoire */
    fd = open(argv[1], O_RDONLY);
    assert(fd != -1);
    while ((lus = read(fd, tampon + taille, st.st_size - taille)) > 0)
        taille += lus;
    assert(lus != -1);
    assert(taille == st.st_size);
    close(fd);

    /* Nb de threads */
    int nThreads = strtol(argv[2], NULL, 10);
    assert(nThreads != -1);

    fonct_arg_s args[nThreads];
    pthread_t threads[nThreads];


    /* Calcul proprement dit */

    assert( clock_gettime(CLOCK_MONOTONIC, &debut) != -1 );

    int i;
    for (i = 0; i < nThreads; i++) {
        args[i].taille = st.st_size / nThreads;
        args[i].tampon = tampon + i * args[i].taille;
    }

    for (i = 0; i < nThreads; i++) {
        assert( pthread_create(&threads[i], NULL, &compteur_wrapper, &args[i]) == 0);
    }

    for (i = 0; i < nThreads; i++) {
        assert( pthread_join(threads[i], NULL) == 0 );
        cptr += args[i].res;
    }

    assert( clock_gettime(CLOCK_MONOTONIC, &fin) != -1 );

    free(tampon);

    fin.tv_sec  -= debut.tv_sec;
    fin.tv_nsec -= debut.tv_nsec;
    if (fin.tv_nsec < 0) {
        fin.tv_sec--;
        fin.tv_nsec += 1000000000;
    }
    
    printf("Nombres de GC:   %ld\n", cptr);
    printf("Taux de GC: %lf\n", ((double) cptr) / ((double) taille));

    printf("Nombres de thread: %d\n", nThreads);

    printf("Durée de calcul: %ld.%09ld\n", fin.tv_sec, fin.tv_nsec);
    printf("(Attention: très peu de chiffres après la virgule sont réellement significatifs !)\n");

    return 0;
}