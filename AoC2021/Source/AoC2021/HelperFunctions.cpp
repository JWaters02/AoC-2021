// Fill out your copyright notice in the Description page of Project Settings.


#include "HelperFunctions.h"

int UHelperFunctions::BinaryToDecimal(const FString& Binary)
{
	int Ret = 0;
	const int Len = Binary.Len();
	for (int i = 0; i < Len; i++)
	{
		if (Binary[i] == '1')
		{
			Ret += pow(2, Len - i - 1);
		}
	}
	return Ret;
}

int UHelperFunctions::CountOccurrencesInArray(const TArray<int>& Array, const int Value, int& Count)
{
	Count = 0;
	for (int i = 0; i < Array.Num(); i++)
	{
		if (Array[i] == Value)
		{
			Count++;
		}
	}
	return Count;
}

void UHelperFunctions::Swap(int* A, int* B)
{
	const int T = *A;
	*A = *B;
	*B = T;
}

int UHelperFunctions::PartitionArray(TArray<int>& Array, const int Low, const int High)
{
	const int Pivot = Array[High];
	int i = Low - 1;
	for (int j = Low; j < High; j++)
	{
		if (Array[j] <= Pivot)
		{
			i++;
			/*const int Temp = Array[i];
			Array[i] = Array[j];
			Array[j] = Temp;*/
			Swap(&Array[i], &Array[j]);
		}
	}
	Swap(&Array[i + 1], &Array[High]);
	return i + 1;
}

void UHelperFunctions::QuickSort(const TArray<int>& Array, const int Low, const int High)
{
	TArray<int> SortedArray = Array;
	if (Low < High)
	{
		const int Pivot = PartitionArray(SortedArray, Low, High);
		QuickSort(Array, Low, Pivot - 1);
		QuickSort(Array, Pivot + 1, High);
	}
}
