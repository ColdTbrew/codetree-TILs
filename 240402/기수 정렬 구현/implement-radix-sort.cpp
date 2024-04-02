#include <iostream>
#include <vector>
#include <cmath> // For pow function
using namespace std;

// 최대 자릿수 찾기
int getMaxDigits(int arr[], int n) {
    int maxDigits = 0;
    for (int i = 0; i < n; i++) {
        int digits = 0;
        int num = arr[i];
        do {
            num /= 10;
            digits++;
        } while (num != 0);
        maxDigits = max(maxDigits, digits);
    }
    return maxDigits;
}

// 기수 정렬 함수
void radixSort(int arr[], int n) {
    int maxDigits = getMaxDigits(arr, n);

    for (int digit = 0; digit < maxDigits; digit++) {
        vector<int> count(10, 0); // 각 자릿수의 빈도수 저장
        vector<int> result(n); // 정렬된 결과 저장

        for (int i = 0; i < n; i++) {
            int num = arr[i];
            int digitValue = (num / static_cast<int>(pow(10, digit))) % 10;
            count[digitValue]++;
        }

        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }

        for (int i = n - 1; i >= 0; i--) {
            int num = arr[i];
            int digitValue = (num / static_cast<int>(pow(10, digit))) % 10;
            result[count[digitValue] - 1] = num;
            count[digitValue]--;
        }

        for (int i = 0; i < n; i++) {
            arr[i] = result[i];
        }
    }
}

int main() {
    int arr[100];
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    radixSort(arr, n);
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}