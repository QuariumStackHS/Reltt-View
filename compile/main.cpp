#include <iostream>
using namespace std;


class human{
    private:

    public:
        int j;
        int id;
        human(){
            j=0;
            id=0;
        }
        void setint(int k,int idd){
            j=k;
            id=idd;
        }


};

int main(){

    human h1= human();
    human h2= human();
    h2.setint(2,11);
    h1.setint(3,14);

    cout << h1.id <<" "<< h1.j <<endl;
    cout<<h2.id <<" "<<h2.j<< endl;





}
