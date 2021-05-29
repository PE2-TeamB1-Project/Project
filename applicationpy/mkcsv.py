import analysispy
from analysispy import *

df = pd.DataFrame(np.array(b),columns=['Lot','Wafer','Mask',
                                       'TestSite','Name','Date','Scrip ID','Script Version',
                                       "Script Owner","Operator","Row","Column"
                                        ,"ErrorFlag","Error description","Analysis Wavelengh",
                                       "Rsq of Ref.spectrum(6th)","Max transmission of Ref spec(dB)",
                                       "Rsq of IV","I at -1V[A]","I at 1V[A]"])

# df.to_csv("Analysis_B1.csv",mode="w")