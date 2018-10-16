// expre_Equality_Operators.cpp
// compile with: /EHsc
#include <iostream>

using namespace std;

int main() {
   cout  << boolalpha
         << "The true expression 3 != 2 yields: "
         << !((2 == 2)&&(2==1)) << endl
         << "The false expression 20 == 10 yields: "
         << (20 == 10) << endl;
}
