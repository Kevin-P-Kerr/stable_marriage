def doStableMarriage(proposers,proposees):
  while(unstable(proposers,proposees)):
    for proposer in proposers:
      proposer.propose()
    for proposee in proposees
      proposee.rejectCandidates()
  printMarriage(proposees)

class Proposer:
  def __init__(self, preferences):
    self.perferences = preferences
    self.proposeeLookUpDict = {}
    for potentialSpouse in preferences:
      self.proposeeLookUpDict[potentialSpouse.name] = potentialSpouse
  def propose():
    for potentialSpouse in self.preferences:
      if (!potentialSpouse.has_rejected):
        potentialSpouse.proposee.sendProposal(self)
        return
  def sendRejection(proposee):
    for potentialSpouse in preferences
      if (proposee == potentialSpouse.proposee):
        potentialSpouse.has_rejected = True
        return

class PotentialSpouse:
  def __init__(self,proposee,name)
    self.proposee = proposee
    self.has_rejected = False

class Proposee:
  def __init__(self,preferences):
    self.currentlyAccepted = False
    self.perferences = perferences
    self.tentativelyAccepted = []
  def sendProposal(proposee):
    self.tenativelyAccepted.append(proposee)
  def rejectCandidates():
    if (!tentativelyAccepted.length):
      return
    if (!self.currentlyAccepted):
      self.currentlyAccepted = tentativelyAccepted[0]
    for proposer in tentativelyAccepted:
      if (preferences.index(proposer) < preferences.index(self.currentlyAccepted):
        self.currentlyAccepted = proposer
      else:
        proposer.sendRejection(self)


def unstable(proposers,proposees):
  


def printMarriage(proposees)
  for p in proposees:
    print p.currentlyAccepted



          

     
  
 
