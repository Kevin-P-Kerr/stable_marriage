def doStableMarriage(proposers,proposees):
  while(unstable(proposers,proposees)):
    for proposer in proposers:
      proposer.propose()
    for proposee in proposees
      proposee.rejectCandidates()
  return MarriageCard(proposees)

  
