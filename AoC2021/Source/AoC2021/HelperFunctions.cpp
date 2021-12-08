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

TArray<int> UHelperFunctions::InsertionSort(const TArray<int>& Array)
{
	TArray<int> SortedArray = Array;
	for (int i = 1; i < SortedArray.Num(); i++)
	{
		const int Temp = SortedArray[i];
		int j = i - 1;
		while (j >= 0 && SortedArray[j] > Temp)
		{
			SortedArray[j + 1] = SortedArray[j];
			j--;
		}
		SortedArray[j + 1] = Temp;
	}
	return SortedArray;
}

TArray<int> UHelperFunctions::Day7Parse(const FString String)
{
	TArray<int> Array;
	std::stringstream SS(TCHAR_TO_UTF8(*String));
	while (SS.good())
	{
		std::string Substr;
		getline(SS, Substr, ',');
		Array.Add(std::stoi(Substr));
	}
	return Array;
}
