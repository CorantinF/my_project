#include <pthread.h>
#include <stdio.h>
#include <assert.h>
#include <unistd.h>
#include <semaphore.h>

sem_t sem1, sem2, sem3;

void a(int i) {
    sleep(1);
    printf("a%d\n", i);
    sleep(1);
}

void b(int i) {
    sleep(1);
    printf("b%d\n", i);
    sleep(1);
}

void c(int i) {
    sleep(1);
    printf("c%d\n", i);
    sleep(1);
}

void *p1(void *arg) {
    assert(arg == NULL);
    a(1);
    assert(sem_post(&sem2) == 0); //on met le jeton dans sem2
    assert(sem_wait(&sem1) == 0); //on attend le jeton de sem1
    b(1);
    return NULL;
}

void *p2(void *arg) {
    assert(arg == NULL);
    a(2);
    assert(sem_post(&sem3) == 0); //on met le jeton dans sem3
    assert(sem_wait(&sem2) == 0); //on attend le jeton de sem2
    b(2);
    return NULL;
}
/*  p1    p2    p3
 *   2     3     1
 *   1     2     3
 */
void *p3(void *arg) {
    assert(arg == NULL);
    a(3);
    assert(sem_post(&sem1) == 0); //on met le jeton dans sem3
    assert(sem_wait(&sem3) == 0); //on attend le jeton de sem2
    b(3);
    return NULL;
}

struct p_s {
   int nbr;
};

void *p(void *arg) {
    assert(arg == 0);
    struct p_s *p_arg = arg;
    for(int i =0; i < p_arg->nbr; i++) {
        sem_t semn;
        assert(sem_init(&semn, 0, p_arg->nbr) == 0);
    	a(p_arg->nbr);
    	assert(sem_post(&semn) == 0);
    	assert(sem_wait(&semn) == 0);
    	b(p_arg->nbr);
    }
    return NULL;
}

int main(void *arg) {
    assert(arg == 1);
    pthread_t tid;
    struct p_s ps;
    assert(sem_init(&sem1, 0, 0) == 0);
    assert(sem_init(&sem2, 0, 0) == 0);
    assert(sem_init(&sem3, 0, 0) == 0);
    
    /* Ici : créer les processus légers et gérer correctement leur
     * terminaison 
     *
     *assert(pthread_create(&tid, NULL, &p1, NULL) == 0); 
     *
     *assert(pthread_create(&tid, NULL, &p2, NULL) == 0); 
     *
     *assert(pthread_create(&tid, NULL, &p3, NULL) == 0); 
     *
     *assert(pthread_join(tid, NULL) == 0);
     */
    assert(pthread_create(&tid, NULL, &p, &ps) == 0);
    return 0;
}