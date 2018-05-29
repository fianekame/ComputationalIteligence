import sys
import IPython
import numpy as np
from IPython.display import display
import sklearn
import matplotlib.pyplot as plt
%matplotlib inline
import skfuzzy as fuzz
from skfuzzy import control as ctrl

academic = ctrl.Antecedent(np.arange(3, 4, 0.1), 'academic')
relevancy = ctrl.Antecedent(np.arange(0, 11, 1), 'relevancy')
interview = ctrl.Antecedent(np.arange(0, 11, 1), 'interview')
candidate = ctrl.Consequent(np.arange(0, 11, 1), 'candidate')

academic["high"] = fuzz.trapmf(academic.universe,[3, 3, 3.3, 3.5])
academic["veryhigh"] = fuzz.trapmf(academic.universe,[3.3, 3.5, 4, 4])
academic.view()

relevancy["low"] = fuzz.trapmf(relevancy.universe,[0,0,3,5])
relevancy["medium"] = fuzz.trimf(relevancy.universe,[2,5,8])
relevancy["high"] = fuzz.trapmf(relevancy.universe,[5,7,10,10])
relevancy.view()

interview["low"] = fuzz.trapmf(interview.universe,[0,0,3,5])
interview["medium"] = fuzz.trimf(interview.universe,[3,5,7])
interview["high"] = fuzz.trapmf(interview.universe,[5,7,10,10])
interview.view()

candidate["least"] = fuzz.trapmf(candidate.universe,[0,0,2,4])
candidate["less"] = fuzz.trimf(candidate.universe,[2,4,6])
candidate["prefer"] = fuzz.trimf(candidate.universe,[4,6,8])
candidate["most"] = fuzz.trapmf(candidate.universe,[6,8,10,10])
candidate.view()

# A1
rule1 = ctrl.Rule(academic['high'] & relevancy['low'] & interview['low'], candidate['least'])
rule2 = ctrl.Rule(academic['high'] & relevancy['low'] & interview['medium'], candidate['least'])
rule3 = ctrl.Rule(academic['high'] & relevancy['low'] & interview['high'], candidate['less'])
rule4 = ctrl.Rule(academic['high'] & relevancy['medium'] & interview['low'], candidate['least'])
rule5 = ctrl.Rule(academic['high'] & relevancy['medium'] & interview['medium'], candidate['less'])
rule6 = ctrl.Rule(academic['high'] & relevancy['medium'] & interview['high'], candidate['prefer'])
rule7 = ctrl.Rule(academic['high'] & relevancy['high'] & interview['low'], candidate['less'])
rule8 = ctrl.Rule(academic['high'] & relevancy['high'] & interview['medium'], candidate['prefer'])
rule9 = ctrl.Rule(academic['high'] & relevancy['high'] & interview['high'], candidate['prefer'])
# A2
rule10 = ctrl.Rule(academic['veryhigh'] & relevancy['low'] & interview['low'], candidate['less'])
rule11 = ctrl.Rule(academic['veryhigh'] & relevancy['low'] & interview['medium'], candidate['less'])
rule12 = ctrl.Rule(academic['veryhigh'] & relevancy['low'] & interview['high'], candidate['prefer'])
rule13 = ctrl.Rule(academic['veryhigh'] & relevancy['medium'] & interview['low'], candidate['less'])
rule14 = ctrl.Rule(academic['veryhigh'] & relevancy['medium'] & interview['medium'], candidate['prefer'])
rule15 = ctrl.Rule(academic['veryhigh'] & relevancy['medium'] & interview['high'], candidate['most'])
rule16 = ctrl.Rule(academic['veryhigh'] & relevancy['high'] & interview['low'], candidate['prefer'])
rule17 = ctrl.Rule(academic['veryhigh'] & relevancy['high'] & interview['medium'], candidate['most'])
rule18 = ctrl.Rule(academic['veryhigh'] & relevancy['high'] & interview['high'], candidate['most'])

candidate_ctrl = ctrl.ControlSystem([rule1, rule2, rule3 , rule4, rule5, rule6, rule7, rule8, rule9,rule10, rule11, rule12, rule13 , rule14, rule15, rule16, rule17, rule18])
kadidat = ctrl.ControlSystemSimulation(candidate_ctrl)

kadidat.input['academic'] = 3.51
kadidat.input['relevancy'] = 8
kadidat.input['interview'] = 9
kadidat.compute()
kadidat.output['candidate']
candidate.view(sim=kadidat)
