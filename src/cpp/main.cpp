#include <iostream>
#include <vector>
using namespace std;

void sortt(vector<int>& v, int l1, int r1, int l2, int r2)
{
	vector<int>L, R;
	int n1 = r1 - l1 + 1;
	int n2 = r2 - l2 + 1;

	for (int i = l1; i <= r1; i++)
		L.push_back(v[i]);

	for (int i = l2; i <= r2; i++)
		R.push_back(v[i]);

	int i = 0;
	int j = 0;
	int k = l1;

	while (i < n1 && j < n2)
	{
		if (L[i] <= R[j])
			v[k++] = L[i++];
		else
			v[k++] = R[j++];
	}

	while (j < n2)
		v[k++] = R[j++];

	while (i < n1)
		v[k++] = L[i++];
}

void divide(vector<int>& v, int l, int r)
{
	if (l < r)
	{
		int l1 = l, r1 = (l + r) / 2;
		int l2 = r1 + 1, r2 = r;
		divide(v, l1, r1);
		divide(v, l2, r2);
		sortt(v, l1, r1, l2, r2);
	}
}

int main()
{
	int n;
	cin >> n;
	vector<int> arr(n);

	for (int i = 0; i < n; i++)
		cin >> arr[i];

	divide(arr, 0, arr.size() - 1);

	for (int i = 0; i < arr.size(); i++)
		cout << arr[i] << " ";
}
