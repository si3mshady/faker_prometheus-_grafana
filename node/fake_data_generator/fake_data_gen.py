import requests, time, logging, sys
from faker import Faker

logging.basicConfig(level = logging.INFO, filename = 'responseData.log')
logging.basicConfig(level = logging.ERROR, filename = 'responseData.log')


def pushFakeData(count=60, domain="localhost", endpoint="data", port=8080):
    fake = Faker()
    while count != 0:
        print(f'Loops remaining {count}')
        ccn = int(fake.credit_card_number())
        try:            
            url = f"http://{domain}:{port}/{endpoint}"
            
            if count % 2 != 0:  #simulate 500 response error
                resp = requests.post(url,  data={"message":"badData"})
                if resp.status_code == 500:      

                    logging.error(f"{resp.status_code}:{resp.text}")               
            resp = requests.post(url, data={"message":ccn})

            if resp.status_code == 200:                            
                logging.info(f"{resp.status_code}:{resp.content}")

            time.sleep(1)
            count -= 1           
        except Exception as e:            
            logging.error(f"Exception:{e}")            
            time.sleep(1)
            count -= 1

if __name__ == "__main__":
    args = [val for val in sys.argv[1:]]    

    if len(args) == 4:
        pushFakeData(count=args[0],domain=args[1], \
             endpoint=args[2], port=args[3])


    elif len(args) == 1: #passing number of seconds   
        pushFakeData(count=int(args[0]),port=888)

    else:
        pushFakeData(port=888)    
   
    

#Elliott Arnold 
#Learning Prometheus, Cadvisor and Grafana 
#Push fake data to Node endpoint to generate metrics for learning purposes
#7-10-21 

