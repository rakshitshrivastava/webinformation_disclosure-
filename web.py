import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()
with open(f"domain.txt","r") as file_ptr:
    for url in file_ptr:
        try:
            headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'}    
            response = requests.get(url, allow_redirects=False,timeout=10,verify=False) 
            res = requests.get(url, allow_redirects=False,timeout=10,verify=False) 
            rest= res.headers.get('server')
            res.raise_for_status()
        except requests.exceptions.RequestException as err:
            rest = requests.get(url, timeout=10,verify=False) 
            rest= res.headers.get('server') 
            if (rest):
                a=response.headers['server']
                print(url,response.headers['server'])
                print(res)
                with open("yes.txt", "a") as myfile:
                 myfile.write(url)
                 myfile.write(a)
            else:
                print(f"{url} : No")
                with open("no.txt", "a") as myfile:
                 myfile.write(url)
        except requests.exceptions.HTTPError as errh:
            print(response.headers['Server'])
            print(response)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)  
        except requests.status_codes == 503:    
            print(url,"error")  
        except requests.status_code == 403:    
            print(url,"error") 
        
if __name__ == "__main__":
    main()
