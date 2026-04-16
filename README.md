# opensea-auto-mint-bot

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)
![Web3](https://img.shields.io/badge/Web3.py-7.12.0-orange?style=flat-square&logo=ethereum&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

Automated NFT minting bot for OpenSea drops. Multi-wallet parallel execution, pre-signed transactions, and automated asset management across 10 EVM networks.

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

- **God Mode** — pre-signs raw transactions before mint opens, broadcasts at T-0
- **Universal ABI** — supports `mint`, `publicMint`, `purchase`, `claim`, and custom functions
- **RPC Rotator** — auto-switches to backup nodes on failure or rate limit
- **Gas Guardian** — pauses if live gas exceeds your defined limit
- **Auto-Funder** — master wallet tops up workers before mint
- **Auto-Transfer** — sends NFTs to cold wallet immediately after mint
- **Dust Sweeper** — sweeps leftover ETH back to master wallet
- **Accountant** — logs every transaction and gas cost to `history.csv`
- **Contract Verifier** — checks source is published on block explorer before minting
- **Proxy support** — per-wallet HTTP proxy rotation

**Networks:** ETH · BASE · ARB · OP · POLY · BSC · AVAX · BERA · MONAD · ABSTRACT

---

## Installation

```bash
git clone https://github.com/genoshide/opensea-auto-mint-bot.git
cd opensea-auto-mint-bot
python -m venv venv
source venv/Scripts/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Configuration

**Credentials**

```
private_key.txt   — one worker private key per line
proxies.txt       — one proxy per line: user:pass@ip:port  (optional)
```

**Environment** — copy `.env.example` to `.env`:

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

# God Mode
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

# Optional
ACCOUNTANT_ENABLED=false
VERIFY_CONTRACT_ENABLED=false
EXPLORER_API_KEY=""
USE_PROXIES=false
```

---

## Usage

```bash
python main.py
```

Output files: `bot_activity.log` (runtime logs) · `history.csv` (transaction records)

Press `Ctrl+C` to stop.

---

## Disclaimer

For educational and experimental purposes only. Using this bot on mainnet involves real financial risk. The author is not liable for any losses, failed transactions, or gas fees. Use at your own risk.

**Genoshide** © 2025 · MIT License
