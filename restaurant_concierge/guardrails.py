from concurrent.futures import ThreadPoolExecutor
from config import TOOL_TIMEOUT

executor=ThreadPoolExecutor(max_workers=2)

def execute_with_timeout(function,*args,**kwargs):
    future=executor.submit(
        function,
        *args,
        **kwargs
    )
    try:
        return future.result(
            timeout=TOOL_TIMEOUT
        )
    except Exception:
        return None