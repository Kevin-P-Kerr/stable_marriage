# definitions
def doStableMarriage(proposers,proposees):
  while(unstable(proposers,proposees)):
    for proposer in proposers:
      proposer.propose()
    for proposee in proposees:
      proposee.rejectCandidates()
  printMarriage(proposees)

class Proposer:
  def __init__(self, preferences):
    self.loser = False
    self.preferences = preferences
    self.proposeeLookUpDict = {}
    for potentialSpouse in preferences:
      self.proposeeLookUpDict[potentialSpouse.name] = potentialSpouse
  def propose(self):
    for potentialSpouse in self.preferences:
      if (not potentialSpouse.has_rejected):
        potentialSpouse.proposee.sendProposal(self)
        return
      self.loser = True # every potential spouse has rejected the proposer
  def sendRejection(self,proposee):
    for potentialSpouse in preferences:
      if (proposee == potentialSpouse.proposee):
        potentialSpouse.has_rejected = True
        return

class PotentialSpouse:
  def __init__(self,proposee):
    self.proposee = proposee
    self.has_rejected = False

class Proposee:
  def __init__(self,preferences):
    self.currentlyAccepted = False
    self.preferences = preferences
    self.tentativelyAccepted = []
    self.has_been_proposed_to = False
  def sendProposal(self,proposee):
    self.tenativelyAccepted.append(proposee)
    self.has_been_proposed_to = True
  def rejectCandidates(self):
    if (not tentativelyAccepted.length):
      return
    if (not self.currentlyAccepted):
      self.currentlyAccepted = tentativelyAccepted[0]
    for proposer in tentativelyAccepted:
      if (preferences.index(proposer) < preferences.index(self.currentlyAccepted)):
        self.currentlyAccepted = proposer
      else:
        proposer.sendRejection(self)


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
    if (proposee.tentativelyAccepted == proposer):
      return True
  return False

def numProposed(proposees):
  numProposed = 0
  for p in proposees:
    if (p.tentativelyAccepted):
      numProposed+=1
  return numProposed

def printMarriage(proposees):
  for p in proposees:
    print p.currentlyAccepted

proposers = [Proposer([]),Proposer([]),Proposer([])]

proposeeA = Proposee([proposers[2],proposers[1],proposers[0]])
proposeeB = Proposee([proposers[0],proposers[2],proposers[1]])
proposeeC = Proposee([proposers[1],proposers[0],proposers[2]])
proposees = [proposeeA,proposeeB,proposeeC]

ps = PotentialSpouse
proposers[0].preferences = [ps(proposeeA),ps(proposeeB),ps(proposeeC)]
proposers[1].preferences = [ps(proposeeB),ps(proposeeC),ps(proposeeA)]
proposers[2].preferences = [ps(proposeeC),ps(proposeeA),ps(proposeeB)]

doStableMarriage(proposers,proposees)
 
