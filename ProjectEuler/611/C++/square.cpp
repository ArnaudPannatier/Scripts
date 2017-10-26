#include <iostream>
#include <time.h>
#include <string>
#include <math.h>
#include <tuple>
#include <queue>
#include <set>

using namespace std;

typedef std::tuple<unsigned long,unsigned long> Coordinates;

unsigned long sumSquare(unsigned long x, unsigned long y){
	return x*x+y*y;
}
bool endColumn(unsigned long x, unsigned long y){
	return (y>=x-1);
}
string expectedStr(int secs){
	secs = abs(secs);
	int days = secs /86400;
	secs %= 86400;
	int hours = secs/3600;
	secs %= 3600;
	int minutes = secs/60;
	secs %= 60;
	if(days > 1){
		return to_string(days) +" days " +to_string(hours)+"h"+to_string(minutes)+"m"+to_string(secs)+"s";
	}else if(hours > 1){
		return to_string(hours)+"h"+to_string(minutes)+"m"+to_string(secs)+"s";
	}else if(minutes >1){
		return to_string(minutes)+"m"+to_string(secs)+"s";
	}else {
		return to_string(secs)+"s";
	}
}



int main(){

	clock_t startT;
	clock_t currentT;

	double execTime = 0;
	string expectedTime = "";

	unsigned long infSquare = 4;
	unsigned long nextSquare = 9;
	queue<Coordinates> notFinishedCol = queue<Coordinates>();
	queue<Coordinates> notFinishedColForNextCateg = queue<Coordinates>();
	set<unsigned long> SetOfSquare = set<unsigned long>();
	unsigned long x = 2;
	unsigned long y = 1;
	unsigned long count = 0;
	unsigned long N = 0;
	unsigned long Max = 1e12;
	bool finishingCateg = true;
	unsigned long stop = floor(sqrt(Max));
	unsigned long square = 0;
	startT = clock();


	while(x < stop+1){
		N++;
		square = sumSquare(x,y);


		// Counting process
		if(square <= Max){
			if(SetOfSquare.find(square) != SetOfSquare.end()){
				SetOfSquare.erase(square);
				count--;
			}else{
				SetOfSquare.insert(square);
				count++;
			}
		}

		//Estimate the time 
		if(floor(log10(N)) == log10(N)){
			currentT = clock();
			execTime =  ((float) (currentT-startT)/(CLOCKS_PER_SEC));
			expectedTime =  expectedStr((int) ( (float) execTime/N*Max));
			cout << "Iteration : " << N << " Count : " << count << " Time : "  << execTime << " Expected total duration : "<< expectedTime << endl;
		}


		// Advance by categories
		if((sumSquare(x,y+1)<=nextSquare) && !(endColumn(x,y))){
			y +=1;
		}
		else{
			if(finishingCateg){
				finishingCateg = false;
				SetOfSquare.clear();
				infSquare = nextSquare;
				nextSquare = (x+2)*(x+2);
				if(!endColumn(x,y)){
					notFinishedColForNextCateg.push(make_tuple(x,y+1));
				}
				notFinishedCol = notFinishedColForNextCateg;
				notFinishedColForNextCateg = queue<Coordinates>();

			}else{
				if(!endColumn(x,y)){
					notFinishedColForNextCateg.push(make_tuple(x,y+1));
				}
			}

			// Next elem
			if(!notFinishedCol.empty()){
					Coordinates next = notFinishedCol.front();
					notFinishedCol.pop();
					x = get<0>(next);
					y = get<1>(next);
			}else {
					finishingCateg = true;
					x++;
					y = 1;
			}


		}

	}
	cout << "Solution: " << count << endl;

	return 0;
}