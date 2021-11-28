// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "FileIOStuff.generated.h"

/**
 * 
 */
UCLASS()
class AOC2021_API UFileIOStuff : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

public:
	UFUNCTION(BlueprintCallable) static FString ReadFile(const FString& Path);
	UFUNCTION(BlueprintCallable) static TArray<FString> Lines(const FString& Text);
};
