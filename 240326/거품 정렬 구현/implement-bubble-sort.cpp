#include <iostream>
using namespace std;

int arr[100];
void bubbleSort(int arr[], int arrsize){
    bool sorted = false;
    int i =0;
    if(arr[i]> arr[i+1]){

        int temp = arr[i];
        arr[i] = arr[i+1];
        arr[i+1] = temp;
        
    }
    while(sorted == false){
        sorted = true;
        for(int i =0;i< arrsize; i++){

        if(arr[i]> arr[i+1]){
        
        int temp = arr[i];
        arr[i] = arr[i+1];
        arr[i+1] = temp;
        sorted = false;
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