// Fill out your copyright notice in the Description page of Project Settings.

#include "FileIOStuff.h"

#include "InputBehavior.h"

FString UFileIOStuff::ReadFile(const FString& Path)
{
	FString Result;
	if (FFileHelper::LoadFileToString(Result, *Path))
	{
		return Result;
	}
	return "";
}

TArray<FString> UFileIOStuff::Lines(const FString& Text)
{
	bool Eof = false;
	TArray<FString> Result;
	FString Temp = Text;
	
	while (!Eof)
	{
		FString LeftString;
		Eof = !Temp.Split("\n", &LeftString, &Temp);
		Result.Add(LeftString);
	}
	return Result;
}
