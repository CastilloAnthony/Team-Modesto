#pragma once
#include <string>
#include <iostream>
#include <fstream>
#include <ctime>
#include <cstdio>
#include <pdh.h>
#include <pdhmsg.h>
#include <vector>

class monitor
{
private:
	std::string currentScheme;
	LPCSTR cpuCounterPath;

	clock_t initializedTime;
	clock_t startTime;

	PDH_HCOUNTER cpuCounter = INVALID_HANDLE_VALUE;
	PDH_HQUERY queryHandle = INVALID_HANDLE_VALUE;

	PDH_FMT_COUNTERVALUE cpuLoadValue;
	bool initialized;

	DWORD bufferSize, numItems;
	LPWSTR szDataSource, szMachineName;
	std::fstream inData;
	std::fstream outData;
	std::vector<double> cpuData;
	double totalCpuData;
	double fiveCpuData;
	int arraySize;

public:
	// Constructors & Deconstructors
	monitor();												//Constructor
	~monitor();												//Deconstructor

	// Mutators
	void updateScheme();									//Mutator
	void primaryRoutine();									//Mutator
	void setCurrentScheme(bool);							//Mutator
	void setStartTime();									//Mutator
	void updateCpuLoad();									//Mutator
	void collectCounterData();								//Mutator
	void updateDataArrays();								//Mutator

	//void readDataFromFile(std::string);					//Mutator
	//void writeData2File(std::string);						//Mutator

	// Accessors
	std::string viewCurrentScheme();						//Accessor
	clock_t viewStartTime();								//Accessor
	double viewCpuLoad();									//Accessor
	double readDataArray(double&);							//Accessor
}; // end monitor
