// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "HelperFunctions.generated.h"

/**
 * 
 */
UCLASS()
class AOC2021_API UHelperFunctions : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
public:
	UFUNCTION(BlueprintCallable) static int BinaryToDecimal(const FString& Binary);
	UFUNCTION(BlueprintCallable) static int CountOccurrencesInArray(const TArray<int>& Array, int Value, int& Count);
};
