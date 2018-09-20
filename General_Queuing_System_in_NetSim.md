## Modeling M/G/1 queue using NetSim Software- ##

We can easily simulate an M/D/1 or M/M/1 queue in Netsim using the NetSim GUI as given in instructions `https://www.tetcos.com/downloads/NetSim-v10-exp-manual/#t=Experiment_16.htm`. But how to simulate M/G/1 queue in NetSim? So here is a step-wise-step tutorial-

Step 1: Go to `C:\Program Files\NetSim Standard\src\Simulation`. Open `NetSim.sln` using Visual Studio 2015.
Step 2: In Solution Explorer look for `Distribution.c` in Application.
Step 3: In GUI mode only constant and exponential distribution is available, So replace the algorithm of one of the distributions with the one you wish to simulate.
For example- I commented the code of constant distribution and inserted a Normal distribution function there.
```C++
    case Distribution_Constant: /*Constant Distribution function*/
        
        /*Normal Distribution Function*/
        fFirstArg = args[0];
        fSecondArg = args[1];
        nRandOut = fnRandomNo(10000000, &fRand, uSeed, uSeed1);
        fRandomNumber = (double)(fRand);
        *fDistOut = (double)(fFirstArg + fSecondArg * sqrt(2) * ErrorFun(2
            * fRandomNumber - 1));
        break;
        /*
        fFirstArg = args[0];
        *fDistOut = fFirstArg;
        break;*/
```
Step 4: Save the new code and Rebuild the solution for `Application` only by right-clicking on it in Solution Explorer.
Make Sure you have selected the correct solution platform in `Build->Configuration Manager` in Menu.( Choose x64).

Step 5: Check in `C:\Program Files\NetSim Standard\src\Simulation\Dll`. `libApplication.dll` has been modified due to rebuilding of the solution.

Step 6: Copy the new `libApplication.dll` and save it in `C:\Program Files\NetSim Standard\bin`. Don't delete the original .dll file, either rename the original file or save it somewhere else.
Step 7: Open NetSim Standard GUI and simulate it as we did for `M/D/1` queue.
Step 8: It will show warning about changing the libApplication.dll. Press any key and wait for simulation to end.
**End**

For more details on simulating your code in NetSim see this video - `https://youtu.be/fdn9p_KN82s?t=9m42s`.
