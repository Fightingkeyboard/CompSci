#include <iostream>
#include <string>


std::string line(int l, std::string c){
  std::string ret_str = "";
  for (int i = 0; i < l ; i+=1){
    ret_str += c;
  }
  ret_str += "\n";
  return ret_str;
}

std::string rect(int w, int h) {
  std::string ret_str = "";
  for (int i = 0; i < h ; i+=1){
    std::string temp = line(w, "*");
    ret_str += temp;  }


  return ret_str;
}

/*
 *
 **
 ***
 ****
 */
std::string tri1(int h) {
  std::string ret_str = "";
  for (int i = 0; i < h ; i+=1){
    ret_str += line(i,"*");
    }

  return ret_str;
}


/*
   *
  ***
 *****
 */
std::string tri2(int h) {
  std::string ret_str = "";
  int spaces = h;
  int start = 1;
  for (int i = 0; i < h ; i++){
    for (int y = 0; y < spaces ; y++){
      ret_str += " ";
    }
    spaces -= 1;
    ret_str += line(start,"*");
    start += 2;
  }

  return ret_str;
}

/*
  *
 **
***
 */
std::string tri3(int h) {
  std::string ret_str = "";
  int start = 1;
  for (int i = 0; i < h ; i++){
    for (int y = 0; y < (h - i); y++){
      ret_str += " ";
    }
    ret_str += line(start, "*");
    start += 1;
  }
  return ret_str;
}
int main(){
  std::string f1 = line(10,"*");
  std::string rec = rect(10,5);
  std::string tri = tri1(5);
  std::string tria2 = tri2(3);
  std::string tria3 = tri3(5);
  std::cout << f1 << std::endl;
  std::cout << rec << std::endl;
  std::cout << tri << std::endl;
  std::cout << tria2 << std::endl;
  std::cout << tria3 << std::endl;
}