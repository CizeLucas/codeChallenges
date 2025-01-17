#include <stdio.h>
#include <stdlib.h>

typedef struct lista_dupl ListaDupl;

struct lista_dupl {
  int info;
  ListaDupl *ant;
  ListaDupl *prox;
};

ListaDupl* lst_dupl_cria();
ListaDupl* lista_dupl_insere(ListaDupl *l, int info);
ListaDupl* lista_dupl_insere(ListaDupl *l, int info);
void lista_dupl_imprime(ListaDupl *l);
void lista_dupl_imprime_inverso(ListaDupl *l); 
int lst_vazia(ListaDupl *l);
ListaDupl* lst_dupl_busca(ListaDupl *l, int info);
ListaDupl* lst_dupl_remove(ListaDupl *l, int info);

ListaDupl* insere_fim_lista_dupl (ListaDupl* l, int x, int y); //Prova AP2 2024.2

int main() {

  ListaDupl* l = lst_dupl_cria();

  for(int i=1; i<=5; i++) {
    l = lista_dupl_insere(l, i);
    //printf("%X\n", l);
    }

  lista_dupl_imprime(l);
  printf("\n");
  lista_dupl_imprime_inverso(l);
  printf("\n");
  ListaDupl *node = lst_dupl_busca(l, 3);
  printf("%X", node);
  printf("\n");
  node = lst_dupl_busca(l, 99);
  printf("%X", node);
  printf("\n");

  printf("\n");
  printf("Remoção do 0:\n");
  l = lst_dupl_remove(l, 0);
  lista_dupl_imprime(l);
  printf("\n\n");

  printf("Remoção do 1:\n");
  l = lst_dupl_remove(l, 1);
  lista_dupl_imprime(l);
  printf("\n\n");

  printf("Remoção do 5:\n");
  l = lst_dupl_remove(l, 5);
  lista_dupl_imprime(l);
  printf("\n\n");

  printf("Remoção do 3:\n");
  l = lst_dupl_remove(l, 3);
  lista_dupl_imprime(l);
  printf("\n\n");

  l = insere_fim_lista_dupl(l, 10, 20);
  lista_dupl_imprime(l);
  printf("\n\n");

  ListaDupl *lNew = lst_dupl_cria();
  lNew = insere_fim_lista_dupl(lNew, 10, 20);
  lista_dupl_imprime(lNew);
  printf("\n\n");

  return 0;
}

ListaDupl* insere_fim_lista_dupl (ListaDupl* l, int x, int y) {

  ListaDupl *node_x = (ListaDupl*) malloc(sizeof(ListaDupl));
  ListaDupl *node_y = (ListaDupl*) malloc(sizeof(ListaDupl));
  node_x->info = x;
  node_y->info = y;
  node_x->ant = NULL;
  node_x->prox = node_y;
  node_y->ant = node_x;
  node_y->prox = NULL;

  if(l == NULL) {
    return node_x;

  } else {
    ListaDupl *lAux = l;
    
    while(lAux->prox != NULL)
      lAux = lAux->prox;

    lAux->prox = node_x;
    node_x->ant = lAux;

    return l;
  }
}

ListaDupl* lst_dupl_cria() {
  return NULL;
};

ListaDupl* lista_dupl_insere(ListaDupl *l, int info) {

  ListaDupl *l_new = (ListaDupl*) malloc(sizeof(ListaDupl));

  l_new->info = info;
  l_new->ant = NULL;
  l_new->prox = l;

  if(l != NULL) {
    l->ant = l_new;
  }

  return l_new;
}

void lista_dupl_imprime(ListaDupl *l) {
  if(l != NULL) {

    while(l != NULL) {
      printf("%d, ", l->info);
      l = l->prox;
    }
  }
}

void lista_dupl_imprime_inverso(ListaDupl *l) {

  if(l != NULL) {

    while (l->prox != NULL)
      l = l->prox;
      
      while(l != NULL){
        printf("%d, ", l->info);
        l = l->ant;
      }
  }
}

int lst_vazia(ListaDupl *l){
  return (l==NULL);
 }

ListaDupl* lst_dupl_busca(ListaDupl *l, int info) {
  if(l == NULL)
    return NULL;

  ListaDupl* lAux = l;

  while (lAux != NULL) {
    if(lAux->info == info)
      return lAux;
    lAux = lAux->prox;
  }

  return NULL;
}

ListaDupl* lst_dupl_remove(ListaDupl *l, int info) {
  if(l == NULL)
    return NULL;

  ListaDupl *lAux = l;

  while(lAux != NULL) {
    if(lAux->info == info) {
      printf("Nó com valor %d removido\n", lAux->info);

      if(lAux->ant != NULL) {
        (lAux->ant)->prox = lAux->prox; //Se não é primeiro nó
      } else {
        l = lAux->prox; //Se é o primeiro nó
      }
        
      if(lAux->prox != NULL) {
        (lAux->prox)->ant = lAux->ant; //Se não é o ultimo nó
      } else {
        lAux->prox == NULL; //Se é o ultimo nó
      }
      free(lAux);
    }
    lAux = lAux->prox;
  }

  return l;
}