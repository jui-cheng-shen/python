#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char const *argv[])
{
    cout << "input a int number:";
    int a;
    cin >> a;

    if (a> 0)
        {
            ofstream file("math.txt");
            if (file.is_open())
            {
                cout << "file is open" << endl;
                file << a;
                file.close();
            }
            else
            {
                cout << "file is not open" << endl;
            }
        }
}