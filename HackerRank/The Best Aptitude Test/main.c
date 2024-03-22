#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    
    int T = 0; //qtd de casos de teste
    int N = 0; //qtd de alunos desse teste
    
    scanf("%d", &T);
    scanf("%d", &N);
    
    float GPA[N];
    int** TESTS = (int**) malloc(N*sizeof(int*));;
    
    for(int i=0; i<N; i++){
        scanf("%f", (GPA + i));
        TESTS[i] = (int*)malloc(5*sizeof(int));    
    }
    
    for(int studentsIndex=0; studentsIndex<N; studentsIndex++){
        for(int gradesIndex=0; gradesIndex<5; gradesIndex++){
            scanf("%d", &TESTS[studentsIndex][gradesIndex]);
        }
    }
    
    
    printf("%d\n%d\n", T, N);
    
    for(int i=0; i<N; i++)
        printf("%.2f ", GPA[i]);
    
    printf("\n");
    for(int studentsIndex=0; studentsIndex<N; studentsIndex++){
        for(int gradesIndex=0; gradesIndex<5; gradesIndex++){
            printf("%d ", TESTS[studentsIndex][gradesIndex]);
        }
        printf("\n");
    }
    
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
