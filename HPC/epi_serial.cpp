#include <iostream>
#include <random>
#include <cmath>
#include <omp.h>

#define RADIUS 10.0
#define N_SAMPLES 1000000

using namespace std;

float get_rand_num(){
    std::random_device rd;  // Will be used to obtain a seed for the random number engine
    std::mt19937 gen(rd()); // Standard mersenne_twister_engine seeded with rd()
    std::uniform_real_distribution<> dis(-1.0*RADIUS, RADIUS);
    return (float)dis(gen);
}

int main()
{
    float pi_estimated = 0.0;
    size_t inside_circle = 0;
    double start = omp_get_wtime();
    for(size_t i=0; i<N_SAMPLES; i++){
        float x_ = get_rand_num();
        float y_ = get_rand_num();
        if(pow((x_*x_ + y_*y_), 0.5)<RADIUS)
            inside_circle++;
    }
    cout << "inside circle " << inside_circle << endl;
    double duration = omp_get_wtime() - start;
    cout << "Original value of pi is " << M_PI << endl;
    pi_estimated = 4.0*(inside_circle/(N_SAMPLES*1.0));
    cout << "Estimated value of pi is " << pi_estimated << endl;
    cout << "Time to estimate pi is " << duration << "s" <<endl;
    return 0;
}

// radius = 10
// points   time          pi
// 10       0.000853151s  3.6
// 100      0.00806026s    3.12
// 1000     0.0318614s     3.1
// 10000    0.281157s      3.15
// 100000   2.75285s       3.13
