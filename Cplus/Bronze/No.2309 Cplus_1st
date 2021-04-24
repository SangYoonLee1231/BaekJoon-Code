# https://www.acmicpc.net/problem/2309
# 일곱 난쟁이 (브루트포스 알고리즘) / 브론즈2

#include <iostream>
#include <cstdio>
using namespace std;


// 선택정렬 알고리즘을 구현한 두 개의 함수
int getMinIndexInRange(int* data, int n, int begin, int end)
{
  int minIndex = begin;
  int minValue = data[begin];

  for (int i = begin; i < n; i++)
  {
    if (minValue > data[i])
    {
      minValue = data[i];
      minIndex = i;
    }
  }
  return minIndex;
}

void selectionSort(int* data, int n)
{
  for (int i = 0; i < n-1; i++)
  {
    int minIndex = getMinIndexInRange(data, n, i, n-1);
    int temp = 0;

    temp = data[minIndex];
    data[minIndex] = data[i];
    data[i] = temp;
  }
}


// 메인 함수
int main()
{
  int tallSum = -100;
  int* tall = NULL;
  int* tall2 = NULL;

  tall = new int[9];
  tall2 = new int[7];
  
  // 난쟁이들 키를 입력 받을때부터 더해 합을 tallSum변수에 저장
  for (int i = 0; i < 9; i++)
  {
    scanf("%d", &tall[i]);
    tallSum += tall[i];
  }

  // 이중 반복문으로 두 명의 가짜 난쟁이를 탐색
  for (int i = 0; i < 9; i++) {
    for (int j = i+1; j < 9; j++) {
      if(tall[i] + tall[j] == tallSum) {
        tall[i] = 0; tall[j] = 0;
        goto EXIT;
      }
    }
  }

EXIT:
  // tall2 새 배열에 진짜 7명의 난쟁이들의 키를 대입
  int k = 0;
  int l = 0;
  while (k < 9)
  {
    if (tall[k] != 0)
    {
      tall2[l] = tall[k];
      l++;
    }
    k++;
  }

  // 선탣 정렬 알고리즘으로 키를 오름차순으로 나열
  selectionSort(tall2, 7);

  for (int i = 0; i < 7; i++)
  {
    cout << tall2[i] << endl;
  }

  delete[] tall;
  delete[] tall2;

  return 0;
}
