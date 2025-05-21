Title: Projects
Date: 2024-10-01
Category: Pages

---

## Sports Betting Arbitrage bot
Automated software that searches for arbitrage opportunities across several bookmakers. Integrations for football, basketball, tennis, F1. 
The code also programmatically saves a odds and sports data, in order to build a sports betting database with as much data as possible.
This second part is for conducting quantitative analysis, testing new strategies and gaining a better understanding of the betting markets.

## uniV3 AMM Liquidity Providing/Hedging Automation tool
Tool for programmatically fetching data from several web3 protocols across Solana (Meteora) and EVM chains (biggest protocols), integrations of other protocols (Orca, Raydium, Kamino) are still in progress.
This software fetches all necessary data for a comprehensive analysis of LP positions, ranges, pool liquidity, expected fees, and calculates the pnl in a consistent way, since is often difficult to understand where the pnl/fees numbers displayed in various web3 protocols comes from.
Second part of the project, it's a tool that connects to the Bitget exchange via ccxt library and andautomatically hedges the cumulative lp positions of the tracked wallets. The hedge used is linear, so it implements an autorebalancing of the hedge based on user provided parameters. The next step is automating also the LP positions rebalancing.

Hedging Impermanent Loss paper: https://arxiv.org/html/2407.05146v1

Code available at: https://github.com/marescialloNino/LP-hedging-strategy

## FLK Chess Engine
I'm building with my friend @sammas41 (github handle) an heuristic chess engine in C++.
We built from scratch the chessboard representation, searching and evaluation algorithms.
As of September 2024 the first release is available, we are still working on improving the performances
at least until the limits of heuristic chess engines allow us 🤔... Later on we will build also a deep learning version.

Code available at: https://github.com/Sammas41/FLK-Chess-Engine

![Alt Text]({static}/images/wizard.jpeg)
