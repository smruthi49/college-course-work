#include <iostream>
using namespace std;
int main(){

    int b = 10;
    int *a;

    a = &b;
    std::cout<<"address -" << a<< " Value -"<< *a << std::endl;
    (*a)++;
    std::cout<<"address -" << a<< " Value -"<< *a << std::endl;
    a ++;
    std::cout<<"address -" << a<< " Value -"<< *a << std::endl;

    int c[] = {1,2};
    a = &c[0]; 
    std::cout<<"address -" << a<< " Value -"<< *a << std::endl;
    (*a)++;
    std::cout<<"address -" << a<< " Value -"<< *a << std::endl;
    a++;
    std::cout<<"address -" << a<< " Value -"<< *a << std::endl;
    cout << c[0] << "\t" << c[1] << endl;
    return 0;
}