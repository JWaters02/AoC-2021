// Fill out your copyright notice in the Description page of Project Settings.


#include "FileIO.h"

FString UFileIO::ReadFile(const FString& Path)
{
	FString Result;
	if (FFileHelper::LoadFileToString(Result, *Path))
	{
		return Result;
	}
	return "";
}

TArray<FString> UFileIO::Lines(const FString& Text)
{
	bool Eof = false;
	TArray<FString> Result;
	FString Temp = Text;
	
	while (!Eof)
	{
		FString LeftString;
		Eof = !Temp.Split("\r\n", &LeftString, &Temp);
		Result.Add(Eof ? Temp : LeftString);
	}
	return Result;
}