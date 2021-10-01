#include <iostream>  
using namespace std;  
int main()  
{  
  int n, i, m=0;
  bool flag = false;  
  cout << "Enter the Number to check Prime or not: ";  
  cin >> n;  
  m=n/2;  
  for(i = 2; i <= m; i++)  
  {  
      if(n % i == 0)  
      {  
          cout<<n<<" is not Prime Number."<<endl;  
          flag=true;  
          break;  
      }  
  }  
  if (flag==0)  
      cout <<n<<" is a Prime Number."<<endl;  
  return 0;  
}  