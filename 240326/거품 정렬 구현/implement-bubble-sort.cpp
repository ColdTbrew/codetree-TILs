#include <iostream>
using namespace std;

int arr[100];  //필요한 크기의 글로벌 어레이 선언 및 초기화
void bubbleSort(int arr[], int arrsize){
    bool sorted = false;   // 초기 상태 : 소팅 상태가 아님
    int i =0;
    
    while (!sorted) {
        sorted = true;
        for (int i = 0; i < arrsize - 1; i++) { // 배열의 모든 인접한 요소 쌍을 차례대로 비교하고 필요한 경우 swap
            if (arr[i] > arr[i + 1]) { // 인접한 두 요소가 정렬되어 있지 않으면 swap
                int temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
                sorted = false;// 배열이 정렬되지 않았음을 표시하기 위해 sorted 플래그를 false로 설정
            }
        }
    }
    
    for(int i =1;i< arrsize+1; i++){
        cout << arr[i] << " ";
    }
    cout << "\n";
}
int main() {
    int n;
    cin >> n;
    int arrsize = n;
    int i = 0;
    while(n--){
        cin >> arr[i++];
    }
    bubbleSort(arr, arrsize);
    return 0;
}
