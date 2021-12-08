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
