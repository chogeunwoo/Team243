#include <stdio.h>

int sum(num1,num2);
void mul(num1,num2);

void main(){
  int calc=0;
  int num1=0;
  int num2=0;
  printf("계산기 프로그램\n");
  while(1){
    printf("첫번째 수와 두번째 수를 입력해주세요.\n");
    scanf_s("%d %d",&num1,&num2);
    printf("원하시는 사칙연산을 선택하세요.\n");
    printf("1)+ 2)- 3)* 4)/\n");
    scanf_s("%d",&calc);
    switch (calc) {
      case 1:
        sum(num1,num2);
        break;
      case 2:
        break;
      case 3:
        mul(num1,num2);
        break;
      case 4:
        break;
      default:
        printf("위의 번호로 골라주세요\n");
    }
  }
}
void sum(int num1,int num2){
  printf("%d + %d = %d\n", num1 ,num2 ,num1+num2);
}
void mul(int num1, int num2)
{
  printf(%d * %d = %d\n, num1, num1 ,num1*num2);
}
