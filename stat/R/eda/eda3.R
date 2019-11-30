# Exploratory data analysis (eda)
library(LearnEDA)
library(e1071)
library(sfsmisc)
library(qcc)
library(aplpack)
library(RSADBE)
library(ACSWR)

"In the late nineteenth century, a theory floated for the dispersion of light waves was 
that light also requires a medium of travel like any other waves, such as water waves 
or sound waves. The medium for light waves to propagate was conjectured to be luminiferous 
ether. Since it was well known at that time that light can travel through a vacuum too, 
it was believed that a vacuum must consist of luminiferous ether."

"Michelson devised an ingenious experiment for establishing the presence of ether. 
The device designed in this experiment is referred as an interferometer, in which a 
single source of light is sent through a half-silvered mirror, splitting the single 
light beam into two beams which travel at right angles to each other. Each beam travels 
to the end of a long arm, and from this end they are reflected back to the middle of 
small mirrors. Both the beams are combined at this middle point of the small mirrors. 
If the ether medium exists, the beam which travels to and from parallel to the flow of 
ether should take more time than the beam which reflects perpendicularly, as the time gained 
from traveling downwards is less than the one traveling upwards. This phenomenon should 
result in a delay for one of the light beams. It is proved that such a shift would be 
approximately 4%. This is the famous Michelson-Morley experiment. 

Some related R programs for graphical plots of this experiment can be found 
at http://en.wikipedia.org/wiki/File:Michelsonmorley-boxplot.svg. In the dataset morley, 
the output Speed contains the kilometers per second information recorded as the speed of 
light minus the speed registered at the experimental unit. Twenty runs of the experiment 
is carried out at five different centers. If there is the presence of ether, we would expect 
this speed to be less than the speed of light in a free medium."
