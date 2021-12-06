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

void UHelperFunctions::Day4P1(const TArray<FString>& Lines)
{
	// Copy the first element of Lines into Drawn
	const FString Drawn = Lines[0];

	// Copy the rest of the elements of Lines into Grids
	TArray<TArray<FString>> Grids;
	for (int i = 2; i < Lines.Num(); i++)
	{
		TArray<FString> Grid;
		Grid.Add(Lines[i]);
		Grids.Add(Grid);
	}

	// Split Drawn into a TArray of FStrings
	TArray<FString> DrawnArray;
	Drawn.ParseIntoArray(DrawnArray, TEXT(","), true);

	
}