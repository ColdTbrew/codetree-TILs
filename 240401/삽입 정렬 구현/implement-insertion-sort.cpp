#include <iostream>
using namespace std;
int arr[100];
void insertionSort(int arr[], int size){
    for(int i =1 ;i< size;i++){
        int j = i-1;
        int key = arr[i];
        while(j>=0 && arr[j] > key){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
}
int main() {
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    insertionSort(arr, n);

    for(int i = 0; i < n; i++) {
    cout << arr[i] << " ";
    }
    return 0;
}