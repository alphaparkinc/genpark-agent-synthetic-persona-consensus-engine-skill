import json
from typing import Dict, Any, List, Optional

class AgentSyntheticPersonaConsensusEngineClient:
    """
    Production-grade multi-persona consensus and arbitration engine.
    Orchestrates deliberation between diverse synthetic expert personas (Security, Speed, Cost, UX)
    and computes weighted confidence consensus to resolve agent decision ambiguities.
    """
    def __init__(self):
        self.default_persona_weights = {
            "Security_Architect": 0.35,
            "Infrastructure_SRE": 0.25,
            "Product_Manager": 0.20,
            "FinOps_Economist": 0.20
        }

    def arbitrate_decision_consensus(
        self,
        decision_prompt: str = "Should we migrate from self-hosted Redis cluster to AWS ElastiCache Serverless?",
        persona_votes: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        if not persona_votes:
            persona_votes = [
                {"persona": "Security_Architect", "vote": "APPROVE", "confidence": 0.90, "rationale": "Automated AWS KMS encryption and SOC2 compliance out of the box."},
                {"persona": "Infrastructure_SRE", "vote": "APPROVE", "confidence": 0.85, "rationale": "Eliminates node failover on-call toil and automated scale management."},
                {"FinOps_Economist": "REJECT", "vote": "REJECT", "persona": "FinOps_Economist", "confidence": 0.75, "rationale": "Serverless request unit pricing could be 20% higher under consistent baseline traffic."},
                {"persona": "Product_Manager", "vote": "APPROVE", "confidence": 0.80, "rationale": "Faster feature iteration and zero maintenance downtime for end-users."}
            ]

        weighted_approve = 0.0
        weighted_reject = 0.0
        total_weight = 0.0

        for pv in persona_votes:
            p = pv["persona"]
            w = self.default_persona_weights.get(p, 0.25)
            conf = pv.get("confidence", 0.8)
            eff_weight = w * conf
            total_weight += eff_weight

            if pv.get("vote") == "APPROVE":
                weighted_approve += eff_weight
            else:
                weighted_reject += eff_weight

        consensus_ratio = round(weighted_approve / max(0.01, total_weight), 2)
        consensus_achieved = consensus_ratio >= 0.65

        final_verdict = "CONSENSUS_APPROVED" if consensus_achieved else "CONSENSUS_REJECTED"

        return {
            "arbitration_id": "cns_arb_6619",
            "decision_prompt": decision_prompt,
            "personas_deliberated_count": len(persona_votes),
            "approval_weight_percentage": f"{int(consensus_ratio * 100)}%",
            "rejection_weight_percentage": f"{int((1 - consensus_ratio) * 100)}%",
            "consensus_achieved": consensus_achieved,
            "final_arbitrated_decision": final_verdict,
            "dissenting_personas": [pv["persona"] for pv in persona_votes if pv.get("vote") != "APPROVE"],
            "decision_confidence_score": round(max(consensus_ratio, 1.0 - consensus_ratio), 2)
        }
