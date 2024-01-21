#include <iostream>
#include <omp.h>

using namespace std;

int main(){

    #pragma omp parallel
    {
        cout << "Hello WOrld!" << endl;
    }
    return 0;
}