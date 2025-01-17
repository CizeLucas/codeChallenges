#include <stdio.h>
#include <stdlib.h>

typedef struct arvb ArvB;
struct arvb{
    char info;
    ArvB *esq;
    ArvB *dir;
};

ArvB* arv_cria_vazia(void);
ArvB* arvb_insere(ArvB *a, int c); 
int arvb_vazia(ArvB *a);
void arvb_imprime(ArvB *a);
int arv_pertence(ArvB *a,char c);
void arv_libera(ArvB *a);

int qtd_nos_arv(ArvB* a); //Prova AP2 2023.2

int main() {
    
    ArvB *t = arv_cria_vazia();

    t = arvb_insere(t, 5);
    t = arvb_insere(t, 11);
    t = arvb_insere(t, 3);
    t = arvb_insere(t, 2);
    t = arvb_insere(t, 6);
    t = arvb_insere(t, 67);
    t = arvb_insere(t, 0);
    t = arvb_insere(t, 80);

    arvb_imprime(t);

    printf("Existem %d numeros pares na árvore", qtd_nos_arv(t));
}

ArvB* arv_cria_vazia(void){
    return NULL;
}

int arvb_vazia(ArvB *a) {
    return (a == NULL);
}

ArvB* arvb_insere(ArvB *a, int c) {
    if(arvb_vazia(a)){
        a = (ArvB*)malloc(sizeof(ArvB));
        a->info = c;
        a->esq = NULL; 
        a->dir = NULL;
    }else if(a->info > c)
        a->esq = arvb_insere(a->esq,c);   
    else if (a->info < c)
        a->dir = arvb_insere(a->dir,c);   
    else
        printf("\nElemento Ja Pertence a Arvore");
    return a;  
}

void arvb_imprime(ArvB *a){
    if(!arvb_vazia(a)){
        arvb_imprime(a->esq);
        printf("%d ",a->info);
        arvb_imprime(a->dir);
    }
}

int qtd_nos_arv(ArvB* a) {
    if(a == NULL)
        return 0;

    int qtd = 0;

    qtd += qtd_nos_arv(a->dir);

    if((a->info)%2 == 0)
        qtd++;

    qtd += qtd_nos_arv(a->esq);
     
    return qtd;
}