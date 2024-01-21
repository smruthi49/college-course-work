#include <iostream>
#include <chrono>

using namespace std;
using namespace std:: chrono;

void display(int *a, int n){

    for(int i = 0; i<n; i++){
        for (int j = 0; j<n; j++){
            cout << *(a++) << "\t";
        }
        cout << endl;
    }
}

int main(){
    int A[600][600], B[600][600], C[600][600];

    for (int i =0; i<600; i++){
        for (int j = 0; j<600; j++){
            A[i][j] = 1;
            B[j][j] = 2;
            C[i][j] = 0;
        }
    }
    
    auto start = high_resolution_clock::now();

    //1
    for (int i =0; i<600; i++){
        for (int j = 0; j<600; j++){
            for (int k = 0;k<600;k++){
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);

    cout << C[0][0] << C[13][2] << endl;

    cout << "Time taken by method 1 :" << duration.count() << "ms" <<endl;

    for (int i =0; i<600; i++){
        for (int j = 0; j<600; j++){
            C[i][j] = 0;
        }
    }

    start = high_resolution_clock::now();
    //2
    for (int j =0; j<600; j++){
        for (int k = 0; k<600; k++){
            for (int i = 0;i<600;i++){
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    stop = high_resolution_clock::now();
    duration = duration_cast<microseconds>(stop - start);

    cout << C[0][0] << C[13][2] << endl;

    cout << "Time taken by method 2 :" << duration.count() << "ms" <<endl;

    return 0;

}