# opensea-auto-mint-bot

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)
![Web3](https://img.shields.io/badge/Web3.py-7.12.0-orange?style=flat-square&logo=ethereum&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)
![genosys](https://img.shields.io/badge/genosys-0.1.1-purple?style=flat-square)

Fully automated NFT minting bot for OpenSea drops. Supports multi-wallet parallel execution, pre-signed transactions (God Mode), and automated asset management across 10 EVM networks.

---

## Preview

```
╭──────────────────────────────────────────────────────────────────────────╮
│       TARGET: 0x79f...d2ee | QTY: 1 | NETWORK: BASE                     │
╰──────────────────────────────────────────────────────────────────────────╯
              WORKER SQUADRON — opensea-auto-mint-bot by Genoshide
╭────┬──────────┬────────────────┬─────────────────────────────────────────╮
│ ID │   Time   │ Wallet Balance │ Status / Activity                       │
├────┼──────────┼────────────────┼─────────────────────────────────────────┤
│  1 │ 13:45:10 │     0.0542 ETH │ [SUCCESS] Minted! TX: 0xabc...          │
│  2 │ 13:45:11 │     0.0210 ETH │ [SUCCESS] Transferring to Cold Wallet.. │
│  3 │ 13:45:12 │     0.0000 ETH │ [WARNING] Insolvent. Waiting funder...  │
╰────┴──────────┴────────────────┴─────────────────────────────────────────╯
```

---

## Features

**Execution**
- **God Mode** — pre-signs raw transactions before mint opens, broadcasts at T-0 with 0ms CPU latency
- **Universal ABI** — compatible with `mint`, `publicMint`, `purchase`, `claim` and any custom function
- **RPC Rotator** — auto-switches to backup nodes on failure or rate limit
- **Gas Guardian** — pauses execution if live gas price exceeds your defined limit

**Asset Management**
- **Auto-Funder** — master wallet tops up worker wallets before mint if balance is insufficient
- **Auto-Transfer** — sends minted NFTs to a cold wallet immediately after mint
- **Dust Sweeper** — sweeps leftover ETH back to master wallet post-execution
- **Accountant** — records every transaction, gas cost, and spend to `history.csv`

**Security**
- **Contract Verifier** — checks that the contract source is published on the block explorer before any transaction
- **Proxy support** — rotate HTTP proxies per wallet

**Monitoring**
- Rich TUI dashboard — live per-wallet status, balances, and logs
- Discord webhook alerts for mints and transfers
- File logging via [genosys](https://pypi.org/project/genosys/)

**Networks:** ETH · BASE · ARB · OP · POLY · BSC · AVAX · BERA · MONAD · ABSTRACT

---

## Installation

```bash
git clone https://github.com/genoshide/opensea-auto-mint-bot.git
cd opensea-auto-mint-bot
python -m venv venv
source venv/Scripts/activate  # Windows
# source venv/bin/activate    # Linux/Mac
pip install -r requirements.txt
```

---

## Configuration

**1. Credentials**

```
private_key.txt   — one worker private key per line
proxies.txt       — one proxy per line: user:pass@ip:port (optional)
```

**2. Environment**

Copy `.env.example` to `.env` and fill in your values:

```ini
# Target
NFT_CONTRACT_ADDRESS="0x..."
MINT_QUANTITY="1"
NETWORK="BASE"           # ETH | BASE | ARB | OP | POLY | BSC | AVAX | BERA | MONAD | ABSTRACT

# Minting
MINT_MODE="DIRECT"       # PROXY | DIRECT
MINT_FUNC_NAME="mint"    # mint | publicMint | purchase | claim
FORCE_START=false

# Performance
MAX_WORKERS="5"
GAS_PRICE_GWEI=""        # blank = auto
MAX_GAS_LIMIT="50"
RETRY_DELAY_MIN="1.5"
RETRY_DELAY_MAX="3.0"

# God Mode (pre-signed transactions)
PRE_SIGN_ENABLED=false
PRE_SIGN_GAS_MULTIPLIER="2.0"
PRE_SIGN_GAS_LIMIT="300000"

# Auto-Funder
AUTO_FUND_ENABLED=false
MASTER_PRIVATE_KEY="0x..."
MIN_WORKER_BALANCE="0.005"
FUNDING_AMOUNT="0.01"

# Auto-Transfer / Sweep
AUTO_TRANSFER_ENABLED=false
RECIPIENT_ADDRESS="0x..."
AUTO_SWEEP_ETH=false
MIN_ETH_TO_SWEEP="0.005"

# Notifications
DISCORD_ENABLED=false
DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."

# Optional modules
ACCOUNTANT_ENABLED=false
VERIFY_CONTRACT_ENABLED=false
EXPLORER_API_KEY=""
USE_PROXIES=false
```

**3. Find the NFT contract address**

Go to [opensea.io/drops](https://opensea.io/drops), open the drop page, and copy the contract address from the mint section.

---

## Usage

```bash
python main.py
```

| File | Purpose |
|---|---|
| `bot_activity.log` | Detailed runtime logs |
| `history.csv` | Transaction records (Accountant) |

Press `Ctrl+C` to stop gracefully.

---

## Project Structure

```
opensea-auto-mint-bot/
├── main.py
├── requirements.txt
├── .env.example
├── private_key.txt       # gitignored
├── proxies.txt           # gitignored
└── src/
    ├── config/           # Settings & ABIs
    ├── engine/           # Execution core
    ├── features/         # Funder, Transfer, Accountant
    ├── ui/               # TUI dashboard, logger, notifier
    └── utils/            # Verifier, helpers
```

---

## Disclaimer

This software is provided for **educational and experimental purposes only**. Using this bot on mainnet involves real financial risk.

By using this software you acknowledge that:
- The author is not liable for any financial losses, failed transactions, or gas fees
- The author is not liable if your wallet is flagged or restricted by any platform
- You use this software entirely at your own risk

**Genoshide** © 2025 · MIT License
