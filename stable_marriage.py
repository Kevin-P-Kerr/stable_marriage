def doStableMarriage(proposers,proposees):
  while(unstable(proposers,proposees)):
    for proposer in proposers:
      proposer.propose()
    for proposee in proposees
      proposee.rejectCandidates()
  return MarriageCard(proposees)

class Proposer:
  def __init__(self, preferences):
    self.perferences = preferences
    self.proposeeLookUpDict = {}
    for potentialSpouse in preferences:
      self.proposeeLookUpDict[potentialSpouse.name] = potentialSpouse
  def propose():
    for potentialSpouse in self.preferences:
      if (!potentialSpouse.has_rejected):
        potentialSpouse.proposee.sendProposal()
        return
  def sendRejection(proposeeName):
    self.proposeeLookUpDict[name].has_rejected = True
  
 
