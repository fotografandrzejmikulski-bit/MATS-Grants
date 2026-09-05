# Safety and containment

This project studies deceptive behaviour and misuse-relevant failure modes. The research must therefore be conducted in environments that prevent the experiments from becoming operational capabilities.

## Containment principles

1. Use toy or sandboxed environments and synthetic tasks whenever possible.
2. Do not connect experimental agents to production credentials, real-world control systems, personal accounts, or unrestricted external execution.
3. Prefer offline evaluation and allowlisted resources.
4. Store model checkpoints, prompts and logs with access controls appropriate to their sensitivity.
5. Do not use real biological, financial, credential theft, or intrusion targets merely to demonstrate a failure mode.
6. Separate measurement from intervention: first establish an effect, then test a minimally invasive causal intervention.

## Evaluation safety

The proposal's examples involving harmful domains should be converted into synthetic placeholders whenever possible. Safety-relevant behaviours can be tested with abstract task environments without reproducing actionable CBRN, fraud, or cyber instructions.

## Research integrity

Potentially exciting mechanistic findings require replication, negative controls and held-out evaluation. A probe correlating with a behaviour is not sufficient evidence that the probe represents an intention, goal or deception mechanism.

## Stop conditions

Pause an experiment if:

- the model begins producing operationally dangerous content beyond the approved evaluation scope;
- the sandbox boundary is violated or an external tool becomes reachable unexpectedly;
- a proposed intervention materially increases harmful capability outside the intended test environment;
- logging or access control is insufficient to reconstruct the experiment safely.

## Reporting

Publish methods, benchmarks, failure cases and negative results where safe. Do not publish operational exploit details when they would materially increase real-world misuse risk.
