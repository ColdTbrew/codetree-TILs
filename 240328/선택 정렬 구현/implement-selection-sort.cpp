#include <iostream>
using namespace std;

int arr[100]; // 전역 배열 선언

int main() {
    int n; // 배열의 크기를 저장할 변수
    cin >> n; // 사용자로부터 배열의 크기 입력 받음
    int i = 0; // 배열 인덱스를 위한 변수
    int len = n; // 배열의 길이 저장, len은 n과 같음
    
    // 배열의 모든 요소를 입력 받음
    while (n--){
        cin >> arr[i++];
    }
    
    // 선택 정렬 시작
    for(int i =0; i < len-1; i++){ // n-1까지 반복, 마지막 요소는 자동으로 정렬됨
        int min = i; // 현재 반복에서 가장 작은 요소의 인덱스를 저장
        // 현재 위치 i 이후의 요소들 중에서 최소값 찾기
        for(int j = i+1; j < len; j++){
            if(arr[j] < arr[min]){
                min = j; // 새로운 최소값의 인덱스를 min에 저장
            }
        }
        // 현재 위치 i와 최소값을 가진 위치 min의 요소를 교환
        int tmp = arr[i];
        arr[i] = arr[min];
        arr[min] = tmp;
    }
    
    // 정렬된 배열 출력
    for(int i = 0; i < len; i++){
        cout << arr[i] <<" ";
    }
    cout << "\n"; // 줄바꿈으로 출력 마무리
    
    return 0; // 프로그램 종료
}