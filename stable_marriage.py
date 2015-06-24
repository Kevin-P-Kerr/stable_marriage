import numpy
dot = numpy.dot
# definitions
def doStableMarriage(proposers,proposees):
  iterations = 0
  while(unstable(proposers,proposees)):
    iterations+=1
    for proposer in proposers:
      proposer.propose()
    for proposee in proposees:
      proposee.rejectCandidates()
  printMarriage(proposees)

class Proposer:
  def __init__(self, preferences, name):
    self.loser = False
    self.preferences = preferences
    self.proposeeLookUpDict = {}
    self.name = name
    self.has_been_rejected = True # maybe technically, but this has to be true in order to send proposals
    for potentialSpouse in preferences:
      self.proposeeLookUpDict[potentialSpouse.name] = potentialSpouse
  def propose(self):
    if (not self.has_been_rejected):
      return 
    self.has_been_rejected = False # be hopeful!
    for potentialSpouse in self.preferences:
      if (not potentialSpouse.has_rejected):
        print self.name + ' is proposing to ' + potentialSpouse.proposee.name
        potentialSpouse.proposee.sendProposal(self)
        return
      else:
        print self.name + ' has been rejected by ' + potentialSpouse.proposee.name
      self.loser = True # every potential spouse has rejected the proposer
  def sendRejection(self,proposee):
    self.has_been_rejected = True
    for potentialSpouse in self.preferences:
      if (proposee == potentialSpouse.proposee):
        print proposee.name + ' is rejecting ' + self.name
        potentialSpouse.has_rejected = True
        return
    print 'bug bug couldn\'t reject!'

class PotentialSpouse:
  def __init__(self,proposee):
    self.proposee = proposee
    if hasattr(proposee,'name'):
        self.name = proposee.name
    self.has_rejected = False

def acceptedSortMaker(preferences):
  def acceptedSort(p1,p2):
    return preferences.index(p1) < preferences.index(p2)
  return acceptedSort

class Proposee:
  def __init__(self,preferences, name, limit=1):
    self.currentlyAccepted = []
    self.preferences = preferences
    self.tenativelyAccepted = []
    self.has_been_proposed_to = False
    self.name = name
    self.limit = limit
    self.acceptedSort = acceptedSortMaker(preferences)
  def sendProposal(self,proposee):
    self.tenativelyAccepted.append(proposee)
    self.has_been_proposed_to = True
  def rejectCandidates(self):
    if (not len(self.tenativelyAccepted)):
      return
    if (len(self.currentlyAccepted) < self.limit):
      self.currentlyAccepted.append(self.tenativelyAccepted.pop(0))
      return
    for proposer in self.tenativelyAccepted:
      weakestAccepted = self.currentlyAccepted[len(self.currentlyAccepted)-1]
      if (self.preferences.index(proposer) < self.preferences.index(weakestAccepted)):
        weakestAccepted.sendRejection(self)
        self.currentlyAccepted.pop()
        self.currentlyAccepted.append(proposer)
        self.currentlyAccepted = sorted(self.currentlyAccepted, cmp=self.acceptedSort)
      else:
        proposer.sendRejection(self)
    self.tenativelyAccepted = [] # the round is concluded


def unstable(proposers,proposees):
  if (len(proposers) > len(proposees)):
    for proposer in proposers:
      if (not proposer.loser and not onString(proposer,proposees)):
        return True
    return False
  else:
    if (len(proposers) != numProposed(proposees)):
      return True
    return False

def onString(proposer, proposees):
  for proposee in proposees:
    if (proposer in proposee.currentlyAccepted):
      return True
  return False

def numProposed(proposees):
  numProposed = 0
  for p in proposees:
    if (p.has_been_proposed_to):
      numProposed+=1
  return numProposed

def printMarriage(proposees):
  for p in proposees:
    if (p.currentlyAccepted):
      for pp in p.currentlyAccepted:
        print p.name, pp.name
    else:
      print p.name, 'none accepted'

# example one from paper
#proposers = [Proposer([],'A'),Proposer([],'B'),Proposer([],'C')]
#
#proposeeA = Proposee([proposers[2],proposers[1],proposers[0]],'a')
#proposeeB = Proposee([proposers[0],proposers[2],proposers[1]],'b')
#proposeeC = Proposee([proposers[1],proposers[0],proposers[2]],'c')
#proposeeC = Proposee([proposers[1],proposers[0],proposers[2]],'c')
#proposees = [proposeeA,proposeeB,proposeeC]
#
#ps = PotentialSpouse
#proposers[0].preferences = [ps(proposeeA),ps(proposeeB),ps(proposeeC)]
#proposers[1].preferences = [ps(proposeeB),ps(proposeeC),ps(proposeeA)]
#proposers[2].preferences = [ps(proposeeC),ps(proposeeA),ps(proposeeB)]
#

#example 3 from paper (should take 10 iterations)
proposers = [Proposer([],'alpha'),Proposer([],'beta'),Proposer([],'gamma'),Proposer([],'delta')]

proposeeA = Proposee([proposers[2],proposers[3],proposers[0],proposers[1]],'a')
proposeeB = Proposee([proposers[3],proposers[0],proposers[1],proposers[2]],'b')
proposeeC = Proposee([proposers[0],proposers[1],proposers[2],proposers[3]],'c')
proposeeD = Proposee([proposers[3],proposers[2],proposers[0],proposers[1]],'d')
proposees = [proposeeA,proposeeB,proposeeC,proposeeD]

ps = PotentialSpouse
proposers[0].preferences = [ps(proposeeA),ps(proposeeB),ps(proposeeC),ps(proposeeD)]
proposers[1].preferences = [ps(proposeeA),ps(proposeeB),ps(proposeeC),ps(proposeeD)]
proposers[2].preferences = [ps(proposeeB),ps(proposeeC),ps(proposeeA),ps(proposeeD)]
proposers[3].preferences = [ps(proposeeC),ps(proposeeA),ps(proposeeB),ps(proposeeD)]
#doStableMarriage(proposers,proposees)

# the parser for yodle
class Circuit:
  def __init__(self, name, skill_vector):
    self.skill_vector = skill_vector
    self.name = name
    self.implicit_preferences = []

class Juggler:
  def __init__(self,name,preferences,skill_vector):
    self.name = name
    self.preferences = preferences
    self.skill_vector = skill_vector

def parse_val(st):
  return int(st.split(':')[1])

def makeCircuit(line):
  name = line[1]
  skills = [parse_val(line[2]),parse_val(line[3]),parse_val(line[4])]
  return Circuit(name,skills)

def makeJuggler(line):
  name = line[1]
  skills = [parse_val(line[2]),parse_val(line[3]),parse_val(line[4])]
  preferences = line[5].split(',')
  return Juggler(name,preferences,skills)


def parse(text):
  parsed = {'jugglers':[],'circuits':[]}
  text = text.split('\n')
  for line in text:
    if (len(line) < 2):
      continue
    line = line.split(' ')
    if line[0] == 'C':
      parsed['circuits'].append(makeCircuit(line))
    elif line[0] == 'J':
      parsed['jugglers'].append(makeJuggler(line))
    else: contiue
  return parsed

f = open('./input.txt','r')
#f = open('./testinput.txt','r')
problem_data = parse(f.read())
# now solve the problem
# first create the proposees
# then the proposers
# then the problem is solved

numJug  = len(problem_data['jugglers']) 
numCirc = len(problem_data['circuits'])
circPerJug = numJug/numCirc

proposees = {}
proposers = {}
proposeeArr = []
proposerArr = []
for proposee in problem_data['circuits']:
  proposees[proposee.name] = Proposee({},proposee.name,circPerJug)
  proposees[proposee.name].circuit = proposee
  proposeeArr.append(proposees[proposee.name])

for proposer in problem_data['jugglers']:
  preferences = []
  for proposeeName in  proposer.preferences:
    proposee = proposees[proposeeName]
    preferences.append(PotentialSpouse(proposee))
  proposers[proposer.name] = Proposer(preferences,proposer.name)
  proposers[proposer.name].juggler = proposer
  proposerArr.append(proposers[proposer.name])

# set the proposee preferenes
counter = 0
print len(proposeeArr)
print len(proposerArr)
for proposee in proposeeArr:
  counter += 1
  preferences = []
  proposee_skill_vector = proposee.circuit.skill_vector
  for proposer in proposerArr:
    proposer_skill_vector = proposer.juggler.skill_vector
    dp = dot(proposee_skill_vector,proposer_skill_vector)
    preferences.append({'dp':dp,'proposer':proposer})
  preferences = sorted(preferences,key=lambda p: p['dp'],reverse=True)
  true_preferences = []
  for p in preferences:
      true_preferences.append(p['proposer'])
  proposee.preferences = true_preferences
  proposee.acceptedSort = acceptedSortMaker(true_preferences)
doStableMarriage(proposerArr,proposeeArr)
