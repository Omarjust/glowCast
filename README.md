# glowCast
the convertion of the data from the NASA about theDevelop the Oracle of DSCOVR, fixed data and the algorith to predict the solar storm.

Once you obtain the datas of velocidad, Densidad ,Temperatura, you could use the data of Densidad and temperatura to have the principal measuremeants, then you use Poisson distribution with all the data to predict the upcoming median and then you use another Poisson distribution withn the data if the data is stadistically growing, thats mean a posible storm, the second Piosson distribution will use the media as 500 on velocidad and 5.5 on Densidad, to kwon if th distribution was from the right or the left side of the mean of the distribution.
