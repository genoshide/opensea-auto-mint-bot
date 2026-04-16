# Changelog

All notable changes to this project are documented here.

---

## [v1.1.0] — 2026-04-16

### Fixed
- `execution.py` — guard `sea_addr` and `multi_addr` against `None` before checksum conversion; raise clear `ValueError` for missing `NFT_CONTRACT_ADDRESS` or `MULTIMINT_ADDRESS` in PROXY mode
- `execution.py` — skip `getPublicDrop` call when `SEA_DROP_ADDRESS` is not configured instead of crashing
- `execution.py` — TUI header showing `1970-01-01` (Unix epoch) when SeaDrop data is unavailable; now displays `Live Now`
- `execution.py` — remove unused variable in `_rotate_provider`
- `main.py` — replace deprecated `asyncio.get_event_loop()` with `asyncio.create_task()` (fixes RuntimeError on Python 3.12+)
- `funder.py` — add missing guard for invalid network ticker before RPC access
- `notifier.py` — fix mutable default argument `fields=[]` on `send_log`
- `notifier.py` — add missing ABSTRACT network explorer URL (`abscan.org`)
- `notifier.py` — remove unused `asyncio` import
- `logger.py` — remove unused `Any` import
- `verifier.py` — remove unused `datetime` and `ConfigurationManager` imports

### Added
- `main.py` — auto-install `pynosist` on startup if package is not present

### Changed
- `requirements.txt` — bump `genosys` to `>=0.1.2`; remove unused dependencies (`packaging`, `requests`, `colorama`)
- `README.md` — streamline: remove redundant sections, flatten feature list, condense disclaimer
- `.env.example` — clean sections, inline comments, consistent format

---

## [v1.0.0] — 2026-04-12

### Added
- Initial release
- Multi-wallet parallel execution with configurable worker limit (`MAX_WORKERS`)
- God Mode — pre-signs raw transactions before mint opens, broadcasts at T-0
- Universal ABI — supports `mint`, `publicMint`, `purchase`, `claim`, and custom functions via `MINT_FUNC_NAME`
- PROXY mode via `mintMulti` contract for OpenSea SeaDrop drops
- DIRECT mode for standard ERC-721 mint functions
- RPC Rotator — auto-switches to backup nodes on connection failure or rate limit
- Gas Guardian — pauses execution when live gas exceeds `MAX_GAS_LIMIT`
- Auto-Funder — master wallet tops up worker wallets before mint
- Auto-Transfer — sends minted NFTs to cold wallet immediately after mint
- Dust Sweeper — sweeps leftover native token back to master wallet
- Accountant — records all transactions and gas costs to `history.csv`
- Contract Verifier — checks contract source is published on block explorer before any transaction
- Per-wallet HTTP proxy rotation
- Rich TUI dashboard with live per-wallet status and balances
- Discord webhook notifications for mints and transfers
- File logging via `genosys`
- Network support: ETH, BASE, ARB, OP, POLY, BSC, AVAX, BERA, MONAD, ABSTRACT
