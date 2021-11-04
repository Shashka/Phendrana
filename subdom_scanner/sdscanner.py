import requests as req
import utils.utils as ut


class subd_scanner:

    prefix = ["http://", "https://"]

    def __init__(self, domain, csv_fields):

        self.domain = domain
        self.fields = csv_fields


    def subd_scan(self, domain, csv_fields):

        domain_lst = {}

        with open("C:\\Users\\rachid.meraoumia\\Desktop\\drift\\subdom_scanner\\sub.txt", "r") as sub:


            for line in sub:

                for pre in self.prefix:

                    try:

                        resp = req.get(str(pre)+line.strip()+domain)
                        if resp.status_code == 200:

                            print(str(pre)+line.strip()+domain+" RESPONSE => "+str(resp.status_code))
                            domain_lst[str(pre)+line.strip()+domain] = str(resp.status_code)
                        else:
                            print(str(pre)+line.strip()+domain + " RESPONSE => " + str(resp.status_code))
                            domain_lst[str(pre) + line.strip() + domain] = str(resp.status_code)
                    except Exception as e:

                        domain_lst[str(pre)+line.strip()+domain] = str(resp.status_code)
                        #print("[ERROR] "+str(e))
                        continue

        ut.export_csv_dict(domain_lst, self.fields, "../dashboard/data/subdom_result.csv")
