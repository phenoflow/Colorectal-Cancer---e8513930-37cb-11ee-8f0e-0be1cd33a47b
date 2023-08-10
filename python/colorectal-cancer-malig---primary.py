# Caroline Fairhurst, Ian Watt, Fabiola Martin, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"B13","system":"readv2"},{"code":"B130","system":"readv2"},{"code":"B131","system":"readv2"},{"code":"B132","system":"readv2"},{"code":"B133","system":"readv2"},{"code":"B134","system":"readv2"},{"code":"B135","system":"readv2"},{"code":"B136","system":"readv2"},{"code":"B137","system":"readv2"},{"code":"B138","system":"readv2"},{"code":"B13y","system":"readv2"},{"code":"B13z","system":"readv2"},{"code":"B14","system":"readv2"},{"code":"B140","system":"readv2"},{"code":"B141","system":"readv2"},{"code":"B1420","system":"readv2"},{"code":"B143","system":"readv2"},{"code":"B14y","system":"readv2"},{"code":"B14z","system":"readv2"},{"code":"B5750","system":"readv2"},{"code":"B5751","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('colorectal-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["colorectal-cancer-malig---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["colorectal-cancer-malig---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["colorectal-cancer-malig---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
