#include <iostream>
#include <fstream>
#include <string>
#include <list>
using namespace std;

int main(){
   fstream newfile;
   newfile.open("input.txt",ios::in); //open a file to perform read operation using file object
   if (newfile.is_open()){   //checking whether the file is open
      string tp;
      list <int> qlist;
      int num;
      while(getline(newfile, tp)){  //read data from file object and put it into string.   
         num = std::stoi(tp);
         cout << num << "\n";   //print the data of the string
         qlist.push_back(num);
      }
      newfile.close();   //close the file object.
      std::list<int>::iterator it;
      for (it = qlist.begin(); it != qlist.end(); it++){
          
      }

   }
}