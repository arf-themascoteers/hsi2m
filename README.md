#Sensors
**Camera**: (**In-situ**) Cubert UHD 285 hyperspectral snapshot camera recording 50 by 50 images with 125 spectral bands ranging from 450 nm to 950 nm and a spectral resolution of 4 nm.

**Moisture**: TRIME-PICO time-domain reflectometry (TDR) sensor in a depth of 2 cm measuring the soil moisture in percent.

#Algorithm

###Imaginary Data
Say, we have **3 bands**. Here is the sample data:

| Time Step | Band #1 | Band #2 | Band #3 | Moisture |
|-----------|---------|---------|---------|----------|
| 1         | 1.1     | 2.1     | 3.1     | 4.1      |
| 2         | 1.2     | 2.2     | 3.2     | 4.2      |
| 3         | 1.3     | 2.3     | 3.3     | 4.3      |
| 4         | 1.4     | 2.3     | 3.4     | 4.4      |
| 5         | 1.5     | 2.4     | 3.5     | 4.5      |
| 6         | 1.6     | 2.5     | 3.6     | 4.6      |
| 7         | 1.7     | 2.6     | 3.7     | 4.7      |
| 8         | 1.8     | 2.7     | 3.8     | 4.8      |
| 9         | 1.9     | 2.8     | 3.9     | 4.9      |

###Sequence

**Lookback window: 4**

Then, sequences are:

| Sequence                                               | Moisture | 
|--------------------------------------------------------|----------|
| [ (1.1, 2.1, 3.1) , (1.2, 2.2, 3.2), (1.3, 2.3, 3.3)   | 4.4      | 
| [ (1.2, 2.2, 3.2), (1.3, 2.3, 3.3),  (1.4, 2.4, 3.4) ] | 4.5      | 
| [ (1.3, 2.3, 3.3),  (1.4, 2.4, 3.4), (1.5, 2.5, 3.5) ] | 4.6      | 
| ...                                                    | ...      | 
