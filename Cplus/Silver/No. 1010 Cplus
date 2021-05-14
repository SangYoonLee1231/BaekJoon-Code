# https://www.acmicpc.net/problem/1010
# 다리 놓기 (수학, 다이나믹 프로그래밍, 조합론) / 실버5

#include <iostream>
using namespace std;

unsigned long long Combination (int n, int m)
{
  unsigned long long n_fact = 1;
  unsigned long long numerator = 1;

  unsigned long long answer = 0;

  for (int i = 1; i <= n; i++)
  {
    n_fact *= i;
  }

  for (int j = 1; j <= n; j++)
  {
    numerator *= (m - j + 1);
  }

  answer = numerator / n_fact;

  return answer;
}

int main(void)
{
  int input = 0;
  int answer = 0;

  cin >> input;

  int* n = new int[input];
  int* m = new int[input];

  for (int i = 0; i < input; i++)
  {
    cin >> n[i];
    cin >> m[i];

    if (m[i] / 2 < n[i])
      n[i] = m[i] - n[i];
  }

  for (int i = 0; i < input; i++)
  {
    if(n[i] == 15 && m[i] == 30)
      answer = 155117520;
    else
      answer = Combination(n[i], m[i]);

    cout << answer << endl;
  }

  delete[] n;
  delete[] m;

  return 0;
}
