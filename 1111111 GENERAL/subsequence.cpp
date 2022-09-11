#include <iostream>
using namespace std;

void solveWordWrap(int n , int arr[], int k){
//initialize total cost
	int total_cost = 0;
	for(int i = 0; i < n - 1; i++){
	//size of window left after the current element
		int size = k - 1 - arr[i];
	//cost of current line
		int sum = k - arr[i];
		while(size >= 0){
			size = size - arr[i+1] - 1;
		// breaks immidiately
			if(size < 0){break;}
			sum = sum - arr[i] - 1;
			i++;
		}
	//add current cost to total cost
		total_cost = total_cost + (sum+1*sum+1);
	}
//print the total cost
	cout << total_cost;
}

int main(){
	int n = 7;
	int nums[n] = {4,3,2,2};
	int k = 6;
	solveWordWrap(n, nums, k);
}
// this code is contributed by Sanyam Jain
