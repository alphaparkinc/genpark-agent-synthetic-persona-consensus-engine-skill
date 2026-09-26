import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AgentSyntheticPersonaConsensusEngineClient

def main():
    client = AgentSyntheticPersonaConsensusEngineClient()
    res = client.arbitrate_decision_consensus()
    print("=== Agent Synthetic Persona Consensus Engine Output ===")
    print(f"Prompt: {res['decision_prompt']}")
    print(f"Approval: {res['approval_weight_percentage']} | Rejection: {res['rejection_weight_percentage']}")
    print(f"Consensus Achieved: {res['consensus_achieved']} | Final Verdict: {res['final_arbitrated_decision']}")
    print(f"Confidence: {res['decision_confidence_score']} | Dissenters: {res['dissenting_personas']}")

if __name__ == '__main__':
    main()
