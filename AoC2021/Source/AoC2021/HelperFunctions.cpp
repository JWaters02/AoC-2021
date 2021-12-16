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

TArray<int64> UHelperFunctions::InsertionSort64(const TArray<int64>& Array)
{
	TArray<int64> SortedArray = Array;
	for (int i = 1; i < SortedArray.Num(); i++)
	{
		const int64 Temp = SortedArray[i];
		int64 j = i - 1;
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

int UHelperFunctions::MapBasins(TArray<FString> Lines)
{
	TArray<TArray<int>> Grid = TArray<TArray<int>>();
	for (int i = 0; i < Lines.Num(); i++)
	{
		Grid.Add(TArray<int>());
		for (int j = 0; j < Lines[i].Len(); j++)
		{
			Grid[i].Add(Lines[i][j] - '0');
		}
	}
	TArray<int> Basins = TArray<int>();
	std::set<int> Visited = std::set<int>();
	for (int i = 0; i < Grid.Num(); i++)
	{
		for (int j = 0; j < Grid[i].Num(); j++)
		{
			if (Visited.find(i * Grid[i].Num() + j) == Visited.end() && Grid[i][j] != 9)
			{
				const int Previous = Visited.size();
				DepthFirstSearch(Grid, i, j, Visited);
				Basins.Add(Visited.size() - Previous);
			}
		}
	}
	Basins.Sort();
	return Basins[Basins.Num() - 1] * Basins[Basins.Num() - 2] * Basins[Basins.Num() - 3];
}

void UHelperFunctions::DepthFirstSearch(TArray<TArray<int>>& Grid, const int StartX, const int StartY, std::set<int>& Visited)
{
	if (StartX < 0 || StartX >= Grid.Num() || StartY < 0 || StartY >= Grid[0].Num())
	{
		return;
	}
	if (Visited.find(StartX * Grid[0].Num() + StartY) != Visited.end() && Grid[StartX][StartY] != 9)
	{
		return;
	}
	Visited.insert(StartX * Grid[0].Num() + StartY);
	DepthFirstSearch(Grid, StartX - 1, StartY, Visited);
	DepthFirstSearch(Grid, StartX + 1, StartY, Visited);
	DepthFirstSearch(Grid, StartX, StartY - 1, Visited);
	DepthFirstSearch(Grid, StartX, StartY + 1, Visited);
}
