
CXX := g++
CXXFLAGS := -g -Wall -std=c++11 -Ofast
INCLUDE = -I/Users/SoChigusa/works/NumericalTools/
# BOOSTFLAGS = -I/opt/boost_1_71_0/include -L/opt/boost_1_71_0/lib
# BOOSTLIBS = -lboost_program_options
# ROOTFLAGS = $(shell root-config --cflags)
# ROOTLIBS = $(shell root-config --libs) -lMinuit2

all:		main.out
# g-2-constraints.out

main.out:	main.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDE) -o main.out main.cpp

# RGE.out: main_RGE.cpp sleptonEFT.h $(addprefix /Users/SoChigusa/works/RGEFlow/, *.o )
# 	$(CXX) $(CXXFLAGS) $(INCLUDE) $(BOOSTFLAGS) $(BOOSTLIBS) $(ROOTFLAGS) $(ROOTLIBS) -o RGE.out main_RGE.cpp $(addprefix /Users/SoChigusa/works/RGEFlow/, *.o)

clean:
	$(RM) *.o *.out
