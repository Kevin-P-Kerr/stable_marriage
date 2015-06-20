# definitions
def doStableMarriage(proposers,proposees):
  iterations = 0
  while(unstable(proposers,proposees)):
    iterations+=1
    for proposer in proposers:
      proposer.propose()
    for proposee in proposees:
      proposee.rejectCandidates()
    print iterations
  printMarriage(proposees)

class Proposer:
  def __init__(self, preferences, name):
    self.loser = False
    self.preferences = preferences
    self.proposeeLookUpDict = {}
    self.name = name
    for potentialSpouse in preferences:
      self.proposeeLookUpDict[potentialSpouse.name] = potentialSpouse
  def propose(self):
    for potentialSpouse in self.preferences:
      if (not potentialSpouse.has_rejected):
        potentialSpouse.proposee.sendProposal(self)
        return
      self.loser = True # every potential spouse has rejected the proposer
  def sendRejection(self,proposee):
    for potentialSpouse in self.preferences:
      if (proposee == potentialSpouse.proposee):
        potentialSpouse.has_rejected = True
        return

class PotentialSpouse:
  def __init__(self,proposee):
    self.proposee = proposee
    self.has_rejected = False

class Proposee:
  def __init__(self,preferences, name):
    self.currentlyAccepted = False
    self.preferences = preferences
    self.tenativelyAccepted = []
    self.has_been_proposed_to = False
    self.name = name
  def sendProposal(self,proposee):
    self.tenativelyAccepted.append(proposee)
    self.has_been_proposed_to = True
  def rejectCandidates(self):
    if (not len(self.tenativelyAccepted)):
      return
    if (not self.currentlyAccepted):
      self.currentlyAccepted = self.tenativelyAccepted[0]
    for proposer in self.tenativelyAccepted:
      if (self.preferences.index(proposer) < self.preferences.index(self.currentlyAccepted)):
        self.currentlyAccepted = proposer
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
    if (proposee.tenativelyAccepted == proposer):
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
    print p.name, p.currentlyAccepted.name

proposers = [Proposer([],'A'),Proposer([],'B'),Proposer([],'C')]

proposeeA = Proposee([proposers[2],proposers[1],proposers[0]],'a')
proposeeB = Proposee([proposers[0],proposers[2],proposers[1]],'b')
proposeeC = Proposee([proposers[1],proposers[0],proposers[2]],'c')
proposeeC = Proposee([proposers[1],proposers[0],proposers[2]],'c')
proposees = [proposeeA,proposeeB,proposeeC]

ps = PotentialSpouse
proposers[0].preferences = [ps(proposeeA),ps(proposeeB),ps(proposeeC)]
proposers[1].preferences = [ps(proposeeB),ps(proposeeC),ps(proposeeA)]
proposers[2].preferences = [ps(proposeeC),ps(proposeeA),ps(proposeeB)]

doStableMarriage(proposers,proposees)
 
