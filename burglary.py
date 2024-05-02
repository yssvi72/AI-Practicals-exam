import matplotlib.pyplot as plt

def joint_probability(burglary,earthquake,alarm,john_calls,mary_calls):
  burglary_p=0.001
  earthquake_p=0.002
  #Conditional probability:
  p_alarm_given_BE = {
    (True,True): 0.95,
    (True,False):0.94,
    (False,True):0.29,
    (False,True):0.001
  }
  p_john_calls_given_alarm = {
  True:0.90,
  False:0.05
  }

  p_mary_calls_given_alarm = {
  True:0.70,
  False:0.01
  }

  p_burglary=burglary_p if (burglary==Ture) else (1-burglary)
  p_earthquake=earthquake_p if (earthquake==Ture) else (1-earthquake)
  p_alarm=p_alarm_given_BE[(burglary,earthquake)] if (earthquake==Ture) else (1-p_alarm_given_BE[(burglary,earthquake)])
  p_mary_calls=p_mary_calls_given_alarm(mary_calls)
  p_john_calls= p_john_calls_given_alarm(john_calls)

  return p_alarm * p_burglary * p_earthquake * p_john_calls * p_mary_calls


b = True if (input("Enter Burglary happened:")=="T") else False
e = True if (input("Enter if Earthquake happened: ") == "T") else False
a = True if (input("Enter if Alarm rang: ") == "T") else False
j = True if (input("Enter if John calls: ") == "T") else False
m = True if (input("Enter if Mary calls: ") == "T") else False

#Compute probability:
p_query=joint_probability(b,e,a,j,m)
print(f"Probility:{p_query:.10f}")
  

    

 

 
