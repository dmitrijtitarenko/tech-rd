---
name: Blockchain & Web3 Research
description: >
  DeFi, smart contracts, L1/L2 scaling, DAOs, tokenomics, zero-knowledge proofs, cross-chain systems.
  Address "blockchain for", "smart contract platform", "DeFi protocol", "Web3 architecture", "tokenomics" questions.
  Evaluate transaction throughput (TPS), finality, total value locked (TVL), security audit status, and developer ecosystem.
  Critical for building blockchain applications and understanding Web3 infrastructure.
---

# Blockchain & Web3 Research Domain

## Overview

Blockchain and Web3 research synthesizes consensus mechanisms, smart contract platforms, decentralized applications, and token economics to understand both technology and incentive structures. This domain encompasses Layer 1 blockchains (Ethereum, Solana, Polygon), Layer 2 scaling (Arbitrum, Optimism), and application layers (DeFi, DAOs, NFTs).

Effective research here means understanding: which blockchain meets your throughput/cost/finality requirements? How do smart contract vulnerabilities create risk? What does tokenomics actually do in practice?

## Key Research Dimensions

**Blockchain Fundamentals**
- Consensus mechanisms: Proof of Work (PoW), Proof of Stake (PoS), BFT variants
- Block time: How frequently new blocks are added (seconds vs minutes)
- Finality: When can transaction be considered irreversible? (slots vs epochs vs probabilistic)
- Throughput (TPS): Transactions per second at current network capacity
- Latency: Time from transaction submission to confirmation
- Decentralization: Number of validators/nodes, stake distribution

**Smart Contract Platforms**
- **Ethereum**: Largest TVL, Solidity language, most mature ecosystem
- **Solana**: High throughput, low cost, different architecture (parallel processing)
- **Polygon**: Ethereum scaling solution, compatibility with Ethereum tooling
- **Avalanche**: Multi-chain architecture, three separate blockchains
- **Cosmos**: Modular approach, IBC for inter-blockchain communication
- **Move-based chains**: Aptos, Sui emphasizing asset-oriented programming

**Layer 2 Scaling Solutions**
- **Optimistic Rollups**: Arbitrum, Optimism (assume transactions valid, prove if disputed)
- **ZK Rollups**: StarkNet, zkSync (prove validity with zero-knowledge proofs)
- **State Channels**: Faster for specific transaction patterns (payment channels)
- **Sidechains**: Independent chains with security guarantees from L1
- Trade-offs: Throughput vs cost, decentralization, developer experience

**DeFi & Protocol Economics**
- Lending protocols: collateral requirements, liquidation mechanics, oracle risk
- Decentralized exchanges (DEX): Automated Market Makers (AMM) vs order books
- Yield farming: Incentive structures, APY sustainability, impermanent loss
- Liquidity pools: How AMM liquidity is provided and risks to LPs
- Treasury management: How protocols manage reserve assets

**Smart Contract Security**
- Audit importance: Did professional auditors review code?
- Known vulnerabilities: Re-entrancy, integer overflow, front-running
- Formal verification: Mathematical proofs of correctness
- Bug bounty programs: Incentives for finding vulnerabilities
- Upgrade mechanisms: Can contracts be patched post-deployment?

**Token Economics & Governance**
- Distribution: How are tokens allocated at genesis and over time?
- Incentive alignment: Do token holders profit from protocol success?
- Governance: How are protocol changes decided? (voting power, quorum)
- Tokenomics sustainability: Can current incentive structure last long-term?
- Regulatory risk: Are tokens securities under applicable laws?

## Data Sources & Query Methods

**Blockchain Analytics & On-Chain Data**
- Glassnode: Blockchain metrics, holder distribution, transaction analysis
- Dune Analytics: SQL queries on blockchain data, community dashboards
- CryptoQuant: Institutional on-chain behavior, exchange flows
- Etherscan/Solscan: Block explorers with transaction details
- Query pattern: "blockchain metrics [network]", "on-chain analysis [protocol]"

**DeFi & Protocol Data**
- DefiLlama: Total Value Locked (TVL) across protocols and chains
- Aave data: Lending protocol metrics, risk parameters
- Uniswap info: DEX liquidity, trading volume, pool composition
- Protocol dashboards: Official dashboards showing protocol metrics
- Query pattern: "DeFi protocol comparison", "TVL trends"

**Smart Contract Audits & Security**
- TrailOfBits, Certora, OpenZeppelin audit reports (published)
- Security incident databases: BlockSec, Rekt (post-mortem analysis)
- Code4rena, Immunefi: Bug bounty platforms
- GitHub audit files: Public repositories with audit reports
- Query pattern: "smart contract audit [protocol]", "security vulnerability"

**Gas & Economics**
- ETH gas trackers: Real-time and historical gas price analysis
- L2 economics: Sequencer costs, proof costs
- Cost calculators: Tools to estimate transaction costs
- Query pattern: "gas cost analysis", "L2 transaction economics"

**Developer Ecosystem**
- GitHub: Commit activity, code quality, library maturity
- Stack Overflow: Developer adoption, question volume
- Dev conferences: Devcon, Solana Breakpoint talks and trends
- Grant programs: Foundation funding for builders
- Query pattern: "smart contract development tools", "blockchain SDK"

## Analysis Frameworks

**Blockchain Selection Matrix** (for application)
- **Throughput (TPS)**: Do you need 100s or 1000s of TPS?
- **Cost per transaction**: Gas fees + L2 overhead at scale
- **Finality**: Can you tolerate probabilistic confirmation (Bitcoin) or need instant?
- **Developer tools**: Language support, debugging, library maturity
- **Ecosystem**: User adoption, DEX liquidity, bridge availability
- **Risk profile**: Audits, time-tested code, known vulnerabilities

**DeFi Protocol Risk Assessment**
- **Smart contract risk**: Professional audits? Code age (battle-tested)?
- **Oracle risk**: How are price feeds obtained? Vulnerable to manipulation?
- **Liquidity risk**: Is liquidity deep enough to prevent slippage?
- **Counterparty risk**: Trust in protocol team, upgrade mechanism
- **Economic risk**: Is yield sustainable or running unsustainable subsidies?
- **Regulatory risk**: Are tokens classified as securities?

**Tokenomics Sustainability Model**
- **Supply**: Fixed total supply vs inflationary emission?
- **Incentives**: Are incentive programs (mining, staking rewards) sustainable?
- **Treasury**: Does protocol have reserves to sustain operations?
- **Governance**: Are stakeholders incentivized to vote for long-term health?
- **Competitive moat**: What prevents competitors from replicating protocol?

**Layer 2 Technology Decision**
- **Throughput**: Which L2 can handle target TPS?
- **Cost**: What are sequencer fees and proof costs at scale?
- **User experience**: How long to finality? Bridging complexity?
- **Composability**: Can L2 contracts interact with L1 and other L2s?
- **Security**: Does L2 have sufficient proof system? Batching period?
- **Decentralization**: Is sequencer centralized (trust assumption)?

**Smart Contract Audit Review**
- **Auditor quality**: Established firm (Trail of Bits, OpenZeppelin) vs unknown?
- **Scope**: Did audit cover all code paths? What was excluded?
- **Issues**: Were critical issues found? How were they resolved?
- **Follow-up**: Were issues actually fixed? Verified in follow-up audit?
- **Timeframe**: How old is the audit? Are recent changes unaudited?

## Output Format Templates

### Blockchain Platform Selection
```
Application: [dApp type, expected workload]
Performance Requirements: [TPS, finality, latency]

Platform Candidates: [Ethereum, Solana, Polygon, etc.]

Ethereum: [throughput, cost, ecosystem, maturity]
Solana: [throughput, cost, ecosystem, risk profile]
Polygon: [throughput, cost, ecosystem, L2 constraints]
[Others]

Recommendation: [which platform wins and why]
Cost Analysis: [gas fees at expected volume]
Developer Experience: [tooling, learning curve]
Risk Assessment: [known vulnerabilities, upgrade risks]
```

### DeFi Protocol Analysis
```
Protocol: [name, type: lending/DEX/derivative/etc.]
TVL: [current, growth trajectory]
Audit Status: [auditor, date, critical findings]

Key Metrics: [APY, utilization rate, collateral ratio]
Risk Assessment: [smart contract risk, oracle risk, economic risk]
Yield Sustainability: [is current APY sustainable?]
Governance: [who controls protocol changes?]
Recommendation: [safe to use?, yield expectations]
```

### Smart Contract Security Review
```
Contract: [protocol, contract name]
Critical Functions: [which functions control valuable assets?]

Audit Results: [auditor, date, issues found]
Code Review: [reentrancy, overflow, access control analysis]
Known Issues: [historical vulnerabilities, community reports]
Testing: [test coverage, formal verification status]

Risk Rating: [low/medium/high]
Recommended Actions: [if any issues require mitigation]
```

### Tokenomics Sustainability Analysis
```
Token: [name, symbol, purpose]
Supply Model: [fixed/inflationary/deflationary]

Initial Distribution: [team%, community%, reserve%]
Emission Schedule: [current annual emission rate]
Incentive Programs: [staking APY, farming rewards]
Treasury: [assets under management, burn rate]

Sustainability Assessment: [can current incentives be sustained?]
Competitive Risk: [what prevents competitors from replicating?]
Regulatory Risk: [is token classified as security?]
Long-term Outlook: [expected token value drivers]
```

## Key Metrics to Always Collect

For blockchain decisions, track:
1. **Network metrics**: TPS capacity, confirmation time, finality time
2. **Economic metrics**: Gas fees, transaction costs at scale, TVL trends
3. **Security**: Audit results, audit age, known vulnerabilities, exploit history
4. **Developer ecosystem**: GitHub activity, library maturity, community size
5. **Adoption**: User growth, transaction volume, protocol TVL
6. **Risks**: Centralization indicators, regulatory status, economic sustainability

## Computational Workflows

**Pre-built Analysis Scripts**
- `transaction_cost_analyzer.py` — Compute gas fees + L2 overhead across chains at expected volume using live pricing
- `tvl_sustainability_checker.py` — Analyze protocol treasury burn rate and incentive sustainability with pandas
- `yield_apy_validator.py` — Calculate expected annual yield accounting for inflation and sustainability with numpy
- `risk_score_aggregator.py` — Combine smart contract audit risk, oracle risk, liquidity risk into composite score

**Dynamic Computation Examples**
- When comparing blockchains, compute effective transaction cost accounting for finality delays and L2 fees
- When evaluating DeFi protocols, run Monte Carlo simulation on yield sustainability given treasury size and emission rates
- When assessing risk, aggregate audit findings, code age, and historical vulnerability incidents into confidence scoring

**Output Artifacts**
- Transaction cost comparison table (chains x transaction types with total cost including settlement)
- TVL vs circulating supply ratio chart (color: sustainability risk, red=unsustainable yield)
- Yield forecast projection (line: expected APY with confidence bands as treasury depletes)
- Mermaid flowchart showing smart contract risk assessment decision tree
- LaTeX formula: TVL_Burn_Rate ($/year) = Treasury / (Annual_Reward_Emissions * Token_Price)

## References

Load from `references/` directory:
- `blockchain-consensus-mechanisms.md` — PoW vs PoS vs BFT comparison
- `ethereum-vs-solana.md` — architecture and tradeoff analysis
- `layer-2-scaling-comparison.md` — rollup vs sidechain vs state channel
- `defi-risks-deep-dive.md` — smart contract, oracle, economic risks
- `smart-contract-audit-checklist.md` — security review methodology
- `tokenomics-framework.md` — analyzing incentive structures
- `web3-development-tools.md` — Hardhat, Foundry, etc. comparison

## Common Pitfalls to Avoid

- **TVL as adoption metric**: High TVL can mean unsustainable farming, not real adoption
- **Gas fee obsession**: Comparing gas prices without accounting for finality time or security
- **Audit false confidence**: Professional audit doesn't guarantee no bugs; code ages
- **Yield farming greed**: 500% APY from new incentives is unsustainable by definition
- **Bridge trust**: Bridges are high-value targets; bridging assets adds risk
- **Liquidation surprise**: Collateral ratio safe until price spike; understand liquidation mechanics
- **Token sales not investment**: Tokens don't guarantee protocol success; incentive misalignment is common
- **Regulatory blindness**: Tokens may be securities; legal classification affects viability
