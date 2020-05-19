#------------------------------------------------------------------------------
# Text correction using Hidden Markov model and Viterbi algorithm
# JL Popyack, May 2020
#
# Uses Viterbi algorithm code, modified from
#   https://en.wikipedia.org/wiki/Viterbi_algorithm
#
# The user provides the following arguments:
#
# obs     : a list of periodic state observations (evidence)
# states  : a list of all possible states for the actual system
# start_p : a list of probabilities of occurrence for each state
# trans_p : transition probabilities for system states
# emit_p  : conditional probabilities of evidence values produced
#           by each state
#
# The algorithm determines the most likely states that explain the
#  
#
# An example given at
#   https://en.wikipedia.org/wiki/Viterbi_algorithm
# concerns a village doctor whose patients are either in Healthy or Fever state,
# but is able only to observe a whether a patient is normal, cold, or dizzy.
# After a few observations, the doctor is able to determine the most likely 
# state sequence that explains the evidence.
# The example uses the following values:
#
# obs = ('normal', 'cold', 'dizzy')
# states = ('Healthy', 'Fever')
# start_p = {'Healthy': 0.6, 'Fever': 0.4}
# trans_p = {
#    'Healthy' : {'Healthy': 0.7, 'Fever': 0.3},
#    'Fever' : {'Healthy': 0.4, 'Fever': 0.6}
#    }
# emit_p = {
#    'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
#    'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
#    }
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Viterbi algorithm from https://en.wikipedia.org/wiki/Viterbi_algorithm
# This has been modified so that instead of printing the table of 
# probabilities and the result (commented out), it returns the concatenated 
# results.
# For this program, the algorithm is used on strings of lowercase letters
# which represent words that have been garbled during Optical Character 
# Recognition (OCR). Expected occurrences of letters a..z are given in start_p,
# determined through analysis of a book written in English.  Transition 
# probabilities reflect the probability that the next character in sequence
# is a given letter, based on the previous k characters in the sequence, also
# determined through analysis of the same book.
#------------------------------------------------------------------------------

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    for st in states:
        V[0][st] = {"prob": start_p[st] * emit_p[st][obs[0]], "prev": None}

    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        for st in states:
            max_tr_prob = V[t-1][states[0]]["prob"]*trans_p[states[0]][st]
            prev_st_selected = states[0]
            for prev_st in states[1:]:
                tr_prob = V[t-1][prev_st]["prob"]*trans_p[prev_st][st]
                if tr_prob > max_tr_prob:
                    max_tr_prob = tr_prob
                    prev_st_selected = prev_st
                    
            max_prob = max_tr_prob * emit_p[st][obs[t]]
            V[t][st] = {"prob": max_prob, "prev": prev_st_selected}
                    
# commented out code from original:
#     for line in dptable(V):
#         print (line)
    
    opt = []
    max_prob = 0.0
    previous = None

    # Get most probable state and its backtrack
    for st, data in V[-1].items():
        if data["prob"] > max_prob:
            max_prob = data["prob"]
            best_st = st
    opt.append(best_st)
    previous = best_st
    
    # Follow the backtrack till the first observation
    for t in range(len(V) - 2, -1, -1):
        opt.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]
        
# inserted code - joins the optimized list to form a string:
    return(''.join(opt))

# commented out code from original:
#     print ('The steps of states are ' + ' '.join(opt) + ' with highest probability of %s' % max_prob)

def dptable(V):
    # Print a table of steps from dictionary
    yield " ".join(("%12d" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)

#------------------------------------------------------------------------------
# Used for comparing actual text with corrected text
#------------------------------------------------------------------------------
def countDifferences(str1,str2):
	print str(len(str1))+" - "+str(len(str2))
	numDiffs = 0
	for ch1,ch2 in zip(str1,str2):
		if ch1 != ch2:
			numDiffs = numDiffs + 1
	return numDiffs
		
		
#------------------------------------------------------------------------------
# The file of actual text has been modified so that it contains only spaces and
# lowercase letters.
#------------------------------------------------------------------------------
states = (' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

#------------------------------------------------------------------------------
# State probabilities computed through analyzing a body of English text.
#------------------------------------------------------------------------------
start_p = {  ' ':0.275022,   'a':0.0581153,   'b':0.010085,   'c':0.0165733,   'd':0.0377057,   'e':0.0930254,   'f':0.0146703,   'g':0.0145223,   'h':0.0507779,   'i':0.0426045,   'j':0.000796875,   'k':0.00790779,   'l':0.0307951,   'm':0.0162815,   'n':0.0444595,   'o':0.0589339,   'p':0.00946235,   'q':0.000631404,   'r':0.043053,   's':0.0406624,   't':0.0681132,   'u':0.0189987,   'v':0.00537346,   'w':0.0219032,   'x':0.000918801,   'y':0.0173571,   'z':0.00124974
}

#------------------------------------------------------------------------------
# Transition probabilities computed through analyzing a body of English text.
# The state is a single letter, with probability of transition to next letter.
# State transitions not observed during analysis are not listed, e.g., the
# letter 'q' was only followed by ' ' and 'u' in the text:
# 	  'q': {' ':0.0344828, 'u':0.965517}
# Zero probabilities for remaining states are filled in later.
#------------------------------------------------------------------------------
trans_nonzero = {
	  ' ': {' ':0.342274, 'a':0.0777744, 'b':0.0308438, 'c':0.0254762, 'd':0.0207578, 'e':0.0108302, 'f':0.0237345, 'g':0.0185411, 'h':0.0422598, 'i':0.0364647, 'j':0.0022642, 'k':0.00533591, 'l':0.0187311, 'm':0.023497, 'n':0.0129519, 'o':0.033678, 'p':0.0129043, 'q':0.00164669, 'r':0.0118752, 's':0.0540083, 't':0.117327, 'u':0.00745761, 'v':0.00239087, 'w':0.0551166, 'x':1.58336e-05, 'y':0.0116535, 'z':0.000190003},
	  'a': {' ':0.0663869, 'a':7.49288e-05, 'b':0.00839203, 'c':0.0247265, 'd':0.0585943, 'e':0.000224786, 'f':0.0106399, 'g':0.0167091, 'h':0.000974075, 'i':0.0587442, 'j':0.000149858, 'k':0.0113892, 'l':0.0730556, 'm':0.0236026, 'n':0.230706, 'p':0.0111644, 'r':0.110745, 's':0.111869, 't':0.0990559, 'u':0.0110895, 'v':0.0258504, 'w':0.0154353, 'x':0.00224786, 'y':0.0272741, 'z':0.000899146},
	  'b': {' ':0.00388601, 'a':0.10924, 'b':0.00388601, 'c':0.00388601, 'e':0.33506, 'i':0.0535406, 'j':0.000431779, 'l':0.0807427, 'o':0.0807427, 'r':0.104491, 's':0.00129534, 't':0.000431779, 'u':0.161917, 'x':0.000431779, 'y':0.0600173},
	  'c': {' ':0.00867052, 'a':0.202838, 'b':0.000262743, 'c':0.00315292, 'd':0.00157646, 'e':0.109564, 'h':0.166316, 'i':0.0359958, 'k':0.0982659, 'l':0.0483447, 'n':0.000262743, 'o':0.165791, 'r':0.101682, 's':0.00131372, 't':0.0336311, 'u':0.0162901, 'v':0.000525486, 'y':0.0055176},
	  'd': {' ':0.683335, 'a':0.0203257, 'c':0.000692921, 'd':0.00796859, 'e':0.0784155, 'f':0.00138584, 'g':0.00219425, 'h':0.000115487, 'i':0.0375332, 'k':0.000115487, 'l':0.0148978, 'm':0.0219425, 'n':0.00184779, 'o':0.0868461, 'r':0.0110867, 's':0.0194018, 'u':0.00381106, 'v':0.000923894, 'w':0.000577434, 'y':0.00658275},
	  'e': {' ':0.391752, 'a':0.0540654, 'b':0.000327669, 'c':0.0216262, 'd':0.0958199, 'e':0.0352479, 'f':0.00795768, 'g':0.0042597, 'h':0.00126387, 'i':0.00823854, 'j':9.36198e-05, 'k':0.000795768, 'l':0.0296775, 'm':0.0223751, 'n':0.0580443, 'o':0.00308945, 'p':0.0107195, 'q':0.000655339, 'r':0.12634, 's':0.0487759, 't':0.0249029, 'u':0.00014043, 'v':0.0129663, 'w':0.00683425, 'x':0.00711511, 'y':0.0268689, 'z':4.68099e-05},
	  'f': {' ':0.35144, 'a':0.057287, 'e':0.0685663, 'f':0.0261205, 'i':0.067379, 'l':0.0335411, 'o':0.205105, 'r':0.0848917, 's':0.000296824, 't':0.0480855, 'u':0.0560997, 'w':0.000296824, 'y':0.000890472},
	  'g': {' ':0.317541, 'a':0.0677661, 'd':0.0005997, 'e':0.123838, 'g':0.0107946, 'h':0.128936, 'i':0.0587706, 'l':0.026087, 'n':0.00149925, 'o':0.0872564, 'r':0.133133, 's':0.0230885, 't':0.00089955, 'u':0.0182909, 'y':0.00149925},
	  'h': {' ':0.0816397, 'a':0.125375, 'e':0.553983, 'f':0.000171512, 'i':0.0967327, 'k':0.0029157, 'l':0.00042878, 'o':0.0585713, 'r':0.0120058, 's':0.00154361, 't':0.0244404, 'u':0.00617443, 'w':0.000171512, 'y':0.035846},
	  'i': {' ':0.066946, 'a':0.00449714, 'b':0.00776778, 'c':0.0378168, 'd':0.066946, 'e':0.0417007, 'f':0.0262674, 'g':0.0302535, 'i':0.000306623, 'k':0.00735895, 'l':0.0650041, 'm':0.0389411, 'n':0.253168, 'o':0.0315822, 'p':0.00449714, 'r':0.0446648, 's':0.10139, 't':0.1435, 'u':0.0013287, 'v':0.018704, 'x':0.000204415, 'z':0.00715454},
	  'j': {'a':0.0491803, 'e':0.20765, 'o':0.409836, 'u':0.333333},
	  'k': {' ':0.2913, 'a':0.034141, 'e':0.403634, 'f':0.00550661, 'i':0.148128, 'l':0.0148678, 'm':0.00385463, 'n':0.0605727, 'o':0.000550661, 'r':0.000550661, 's':0.0242291, 'w':0.00165198, 'y':0.0110132},
	  'l': {' ':0.174915, 'a':0.0559955, 'b':0.000282805, 'c':0.000565611, 'd':0.0895079, 'e':0.15017, 'f':0.0127262, 'g':0.000424208, 'i':0.111567, 'k':0.0164027, 'l':0.162896, 'm':0.00141403, 'n':0.000141403, 'o':0.0879525, 'p':0.00692873, 'r':0.000424208, 's':0.0111708, 't':0.010181, 'u':0.00834276, 'v':0.00820136, 'w':0.00296946, 'y':0.0868213},
	  'm': {' ':0.228136, 'a':0.203263, 'b':0.0163145, 'c':0.000802354, 'd':0.00160471, 'e':0.244718, 'f':0.00294196, 'g':0.000534902, 'h':0.000802354, 'i':0.0607114, 'l':0.00240706, 'm':0.00802354, 'n':0.00160471, 'o':0.076491, 'p':0.0187216, 'r':0.00347687, 's':0.0267451, 'u':0.0441294, 'y':0.0585718},
	  'n': {' ':0.287659, 'a':0.00714985, 'b':0.00235064, 'c':0.0218413, 'd':0.235847, 'e':0.0817826, 'f':0.00166503, 'g':0.111655, 'h':0.00127326, 'i':0.0166503, 'j':0.000489716, 'k':0.0201763, 'l':0.00920666, 'm':9.79432e-05, 'n':0.00803134, 'o':0.0712047, 'q':0.0013712, 'r':0.0013712, 's':0.0346719, 't':0.0640548, 'u':0.00352595, 'v':0.000783546, 'w':9.79432e-05, 'x':0.00146915, 'y':0.015573},
	  'o': {' ':0.16248, 'a':0.00790601, 'b':0.00214275, 'c':0.00421162, 'd':0.0300724, 'e':0.0042855, 'f':0.0707847, 'g':0.00398995, 'h':0.00288163, 'i':0.0101965, 'j':0.00221664, 'k':0.0140387, 'l':0.0223881, 'm':0.0413773, 'n':0.105216, 'o':0.0588148, 'p':0.0155165, 'q':0.000517216, 'r':0.110241, 's':0.0135954, 't':0.0761785, 'u':0.13987, 'v':0.0134476, 'w':0.0715236, 'x':0.000517216, 'y':0.00258608, 'z':0.0130043},
	  'p': {' ':0.157386, 'a':0.0892775, 'b':0.00368155, 'd':0.000460193, 'e':0.163829, 'h':0.00460193, 'i':0.0487805, 'l':0.117809, 'm':0.00230097, 'o':0.121491, 'p':0.07133, 'r':0.117809, 's':0.0161068, 't':0.0271514, 'u':0.038196, 'w':0.000460193, 'y':0.0193281},
	  'q': {' ':0.0344828, 'u':0.965517},
	  'r': {' ':0.234247, 'a':0.0604835, 'b':0.000809143, 'c':0.00586629, 'd':0.0274097, 'e':0.249924, 'f':0.004956, 'g':0.00475372, 'h':0.00101143, 'i':0.0569435, 'k':0.0116314, 'l':0.0165874, 'm':0.0137554, 'n':0.0213412, 'o':0.14332, 'p':0.00606857, 'r':0.018408, 's':0.0341863, 't':0.0315566, 'u':0.015576, 'v':0.00192172, 'w':0.00161829, 'y':0.0376252},
	  's': {' ':0.383487, 'a':0.0639323, 'b':0.000107089, 'c':0.0324481, 'e':0.0948811, 'f':0.000428357, 'g':0.000107089, 'h':0.0930606, 'i':0.0274149, 'k':0.0214179, 'l':0.0104948, 'm':0.00685372, 'n':0.00267723, 'o':0.0658599, 'p':0.013172, 'q':0.000642536, 's':0.0266652, 't':0.121868, 'u':0.0199186, 'w':0.0130649, 'y':0.00149925},
	  't': {' ':0.259685, 'a':0.0166219, 'c':0.0118271, 'e':0.0598389, 'f':0.000831096, 'h':0.399437, 'i':0.0395729, 'l':0.0171973, 'm':0.000703235, 'n':0.000447513, 'o':0.110728, 'p':0.000191791, 'r':0.0278097, 's':0.010996, 't':0.0196266, 'u':0.00990922, 'v':6.39304e-05, 'w':0.00300473, 'x':0.000191791, 'y':0.0113157},
	  'u': {' ':0.127664, 'a':0.0105432, 'b':0.0061884, 'c':0.0304836, 'd':0.0128352, 'e':0.0277332, 'f':0.0077928, 'g':0.0577584, 'i':0.0256704, 'l':0.122393, 'm':0.013752, 'n':0.126289, 'p':0.0547788, 'r':0.116663, 's':0.0990144, 't':0.158836, 'z':0.0016044},
	  'v': {' ':0.000810373, 'a':0.00648298, 'e':0.884117, 'i':0.0656402, 'm':0.00486224, 'o':0.0307942, 'y':0.00729335},
	  'w': {' ':0.15666, 'a':0.193837, 'd':0.000994036, 'e':0.157256, 'f':0.00178926, 'h':0.138171, 'i':0.194632, 'k':0.000397614, 'l':0.00477137, 'n':0.0312127, 'o':0.108151, 'r':0.00337972, 's':0.00815109, 'u':0.000397614, 'y':0.000198807},
	  'x': {' ':0.056872, 'a':0.042654, 'c':0.123223, 'e':0.161137, 'h':0.00473934, 'i':0.0758294, 'p':0.109005, 't':0.42654},
	  'y': {' ':0.722529, 'a':0.00301054, 'b':0.000752634, 'c':0.00401405, 'e':0.0459107, 'f':0.00100351, 'i':0.0120421, 'l':0.000752634, 'm':0.000250878, 'o':0.169594, 'p':0.00100351, 'r':0.00150527, 's':0.0250878, 't':0.00978424, 'w':0.00250878, 'z':0.000250878},
	  'z': {' ':0.616725, 'a':0.160279, 'e':0.101045, 'i':0.0278746, 'l':0.0209059, 'o':0.0139373, 'u':0.00696864, 'y':0.0243902, 'z':0.0278746}
     }
     
#------------------------------------------------------------------------------
# Emission probabilities for this example state explain the probabilities that 
# certain letters are mistaken in the OCR process.  For instance, b and d are 
# often confused for each other, as are {c,e,o}, {h,l}, {i,j}, {m,n} and {v,w}.  
# In all cases, the probability that the actual letter is recognized correctly 
# is 60%, and the probability that it is recognized as one of the other letters # in its grouping is 40%, evenly divided among the alternatives. 
# The emission probabilities shown below contain only nonzero values, e.g.,
# 	  'e' : {'c':0.2, 'e':0.6 ,'o':0.2}
# Zero probabilities for remaining emissions are filled in later.
#------------------------------------------------------------------------------
emit_nonzero = {
  'b' : {'b':0.6, 'd':0.4}, 
  'd' : {'b':0.4, 'd':0.6}, 
  'c' : {'c':0.6, 'e':0.2 ,'o':0.2}, 
  'e' : {'c':0.2, 'e':0.6 ,'o':0.2}, 
  'o' : {'c':0.2, 'e':0.2 ,'o':0.6}, 
  'h' : {'h':0.6, 'l':0.4}, 
  'l' : {'h':0.4, 'l':0.6}, 
  'i' : {'i':0.6, 'j':0.4}, 
  'j' : {'i':0.4, 'j':0.6}, 
  'm' : {'m':0.6, 'n':0.4}, 
  'n' : {'m':0.4, 'n':0.6}, 
  'v' : {'v':0.6, 'w':0.4},
  'w' : {'v':0.4, 'w':0.6},

  ' ': {' ':1.0},

  'a': {'a':1.0},
  'f': {'f':1.0},
  'g': {'g':1.0},
  'k': {'k':1.0},
  'p': {'p':1.0},
  'q': {'q':1.0},
  'r': {'r':1.0},
  's': {'s':1.0},
  't': {'t':1.0},
  'u': {'u':1.0},
  'x': {'x':1.0},
  'y': {'y':1.0},
  'z': {'z':1.0}
   }
   
#------------------------------------------------------------------------------
# Create trans_p and emit_p from trans_nonzero and emit_nonzero by filling in 
# zero probabilities for unlisted transitions.
#------------------------------------------------------------------------------
trans_p = {}
emit_p = {}
from collections import defaultdict
for st in states:
	trans_p[st] = {s: 0 for s in states}
	trans_p[st].update(trans_nonzero[st])
	emit_p[st] = {s: 0 for s in states}
	emit_p[st].update(emit_nonzero[st])

#------------------------------------------------------------------------------
# Read actual text and text resulting from (simulated) poor OCR.
#------------------------------------------------------------------------------
actualfile = file('actual_text.txt','r')
actualtext = actualfile.read()
actualfile.close()
actualtext.strip()  #remove leading and trailing whitespace

infile = file('poor_ocr1b.txt','r') 
text = infile.read() 
infile.close() 
text = text.strip()  #remove leading and trailing whitespace

numDiffs = countDifferences(actualtext,text)
print "Differences between actual, poor OCR text: "+str(numDiffs)

print "\nCorrected text: "

word=""
newtext = ""
for word in text.split():
	obs = list(word)
	mostLikely = viterbi(obs,states,start_p,trans_p,emit_p)
	newtext += mostLikely + " "
	print mostLikely,
	
newtext = newtext.strip()
numDiffs = countDifferences(actualtext,newtext)
print "\n\nDifferences between actual, corrected text: "+str(numDiffs)
