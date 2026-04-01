# FlowAgent — AI Agents for Enterprise Back-Office Processes

## Problem Statement
Large enterprises run thousands of repetitive back-office processes: invoice matching, refund processing, crew scheduling exceptions, booking amendments, compliance checks. These processes are documented in wikis and SOPs but executed manually by operations teams following step-by-step procedures. RPA (UiPath, Automation Anywhere) promised to automate these but requires brittle screen-scraping scripts that break with every UI change. The gap: processes that are too complex for RPA but too repetitive for skilled humans.

## Target Customer (ICP)
Large European enterprises (airlines, logistics, insurance, banking) with 500+ back-office operations staff. Primary beachhead: airline operations teams (Karel's AF-KLM domain). These companies have documented SOPs, legacy systems with APIs (or screen interfaces), and massive manual processing volumes.

## Proposed Solution & Wedge
AI agents that read SOP documentation, understand the process logic, and execute it autonomously across enterprise systems (via APIs, not screen scraping). Human-in-the-loop for exceptions. Wedge: airline irregular operations (IROPS) — automated rebooking, compensation calculation, and passenger communication during disruptions.

## Pricing Model
- Per-process licensing: EUR 5-15K/month per automated process
- Volume discount for 5+ processes
- Implementation fee: EUR 20-50K per process (one-time setup + training)

## Go-to-Market
Karel's AF-KLM network for first design partner. Airline industry conferences (IATA, Aviation Festival). Direct outreach to VP Operations / VP Digital at European airlines. Expand to logistics and insurance after proving the model.

## Defensibility & Moat
Karel's insider knowledge of airline operations processes is rare and hard to replicate. Each deployed process generates training data for the AI agents (data flywheel). Deep integration into enterprise systems creates high switching costs. Domain-specific agent logic (IROPS rules, fare calculation, GDS integration) is complex to build from scratch.
