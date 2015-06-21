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
      self.currentlyAccepted = self.tenativelyAccepted.pop(0)
    for proposer in self.tenativelyAccepted:
      if (self.preferences.index(proposer) < self.preferences.index(self.currentlyAccepted)):
        self.currentlyAccepted.sendRejection(self)
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
    if (p.currentlyAccepted):
      print p.name, p.currentlyAccepted.name
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
proposers[1].preferences = [ps(proposeeD),ps(proposeeB),ps(proposeeC),ps(proposeeA)]
proposers[2].preferences = [ps(proposeeB),ps(proposeeC),ps(proposeeA),ps(proposeeD)]
proposers[3].preferences = [ps(proposeeC),ps(proposeeA),ps(proposeeB),ps(proposeeD)]
doStableMarriage(proposers,proposees)
 
