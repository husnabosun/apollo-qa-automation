import pytest
import time
from utils.driver import get_driver

@pytest.fixture(scope="function", autouse=True, name="driver")
def driver_setup(request):
    driver = get_driver()

    if request.cls is not None:
        request.cls.driver = driver
        
    yield driver
    
    try:
        driver.close()  
        time.sleep(0.5) 
        driver.quit()   
    except Exception:
        pass